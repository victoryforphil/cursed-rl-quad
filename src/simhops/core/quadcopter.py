"""Quadcopter dynamics simulation using MuJoCo."""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

import mujoco
import numpy as np

if TYPE_CHECKING:
    from numpy.typing import NDArray


# MuJoCo XML model for quadcopter
QUADCOPTER_XML = """
<mujoco model="quadcopter">
  <compiler angle="radian"/>
  
  <option timestep="0.01" gravity="0 0 -9.81" integrator="RK4"/>
  
  <asset>
    <texture type="skybox" builtin="gradient" rgb1="0.3 0.5 0.7" rgb2="0 0 0" width="512" height="512"/>
    <texture name="grid" type="2d" builtin="checker" width="512" height="512" rgb1="0.1 0.2 0.3" rgb2="0.2 0.3 0.4"/>
    <material name="grid" texture="grid" texrepeat="8 8" reflectance="0.2"/>
    <material name="body" rgba="0.2 0.2 0.8 1"/>
    <material name="motor_cw" rgba="1 0 0 1"/>
    <material name="motor_ccw" rgba="0 1 0 1"/>
  </asset>
  
  <worldbody>
    <light directional="true" diffuse="0.8 0.8 0.8" specular="0.3 0.3 0.3" pos="0 0 5" dir="0 0 -1"/>
    <geom name="ground" type="plane" size="50 50 0.1" material="grid"/>
    
    <body name="quadcopter" pos="0 0 1">
      <freejoint name="root"/>
      <inertial pos="0 0 0" mass="0.5" diaginertia="0.0023 0.0023 0.004"/>
      
      <!-- Main body -->
      <geom name="body" type="box" size="0.05 0.05 0.02" material="body"/>
      
      <!-- Arms -->
      <geom name="arm_front" type="capsule" fromto="0 0 0 0.17 0 0" size="0.01" rgba="0.5 0.5 0.5 1"/>
      <geom name="arm_back" type="capsule" fromto="0 0 0 -0.17 0 0" size="0.01" rgba="0.3 0.3 0.3 1"/>
      <geom name="arm_left" type="capsule" fromto="0 0 0 0 0.17 0" size="0.01" rgba="0.4 0.4 0.4 1"/>
      <geom name="arm_right" type="capsule" fromto="0 0 0 0 -0.17 0" size="0.01" rgba="0.4 0.4 0.4 1"/>
      
      <!-- Motor mounts (visual only, mass in inertial) -->
      <geom name="motor0" type="cylinder" pos="0.17 0 0" size="0.02 0.01" material="motor_cw"/>
      <geom name="motor1" type="cylinder" pos="-0.17 0 0" size="0.02 0.01" material="motor_cw"/>
      <geom name="motor2" type="cylinder" pos="0 0.17 0" size="0.02 0.01" material="motor_ccw"/>
      <geom name="motor3" type="cylinder" pos="0 -0.17 0" size="0.02 0.01" material="motor_ccw"/>
      
      <!-- Sites for force application -->
      <site name="motor0_site" pos="0.17 0 0.01" size="0.01"/>
      <site name="motor1_site" pos="-0.17 0 0.01" size="0.01"/>
      <site name="motor2_site" pos="0 0.17 0.01" size="0.01"/>
      <site name="motor3_site" pos="0 -0.17 0.01" size="0.01"/>
      <site name="body_center" pos="0 0 0" size="0.01"/>
      
      <!-- IMU sensor site -->
      <site name="imu_site" pos="0 0 0" size="0.005"/>
    </body>
  </worldbody>
  
  <sensor>
    <accelerometer name="accel" site="imu_site"/>
    <gyro name="gyro" site="imu_site"/>
    <framepos name="pos" objtype="site" objname="body_center"/>
    <framequat name="quat" objtype="site" objname="body_center"/>
    <framelinvel name="linvel" objtype="site" objname="body_center"/>
    <frameangvel name="angvel" objtype="site" objname="body_center"/>
  </sensor>
  
  <actuator>
    <!-- We'll apply forces directly, but define actuators for structure -->
  </actuator>
</mujoco>
"""


@dataclass
class QuadcopterParams:
    """Physical parameters for the quadcopter."""

    mass: float = 0.5  # kg
    arm_length: float = 0.17  # meters from center to motor
    thrust_to_weight: float = 2.0  # max thrust / weight ratio
    inertia: tuple[float, float, float] = (0.0023, 0.0023, 0.004)  # Ixx, Iyy, Izz
    drag_coeff: float = 0.01  # linear drag coefficient
    motor_time_constant: float = 0.02  # seconds, first-order motor response

    @property
    def max_thrust_per_motor(self) -> float:
        """Maximum thrust per motor in Newtons."""
        return (self.mass * 9.81 * self.thrust_to_weight) / 4.0

    @property
    def torque_to_thrust(self) -> float:
        """Ratio of reactive torque to thrust for each motor."""
        return 0.01  # typical value


@dataclass
class QuadcopterState:
    """Full state of the quadcopter."""

    position: NDArray[np.float64] = field(default_factory=lambda: np.zeros(3))
    velocity: NDArray[np.float64] = field(default_factory=lambda: np.zeros(3))
    orientation: NDArray[np.float64] = field(
        default_factory=lambda: np.array([1.0, 0.0, 0.0, 0.0])
    )  # quaternion wxyz (MuJoCo convention)
    angular_velocity: NDArray[np.float64] = field(default_factory=lambda: np.zeros(3))
    motor_speeds: NDArray[np.float64] = field(
        default_factory=lambda: np.zeros(4)
    )  # normalized 0-1


class Quadcopter:
    """MuJoCo-based quadcopter simulation.

    The quadcopter uses a "+" configuration:
        Motor 0: +X (front)
        Motor 1: -X (back)
        Motor 2: +Y (left)
        Motor 3: -Y (right)

    Action space: [throttle, roll_rate, pitch_rate, yaw_rate] in [-1, 1]
    These are mixed to motor commands using a standard mixer.
    """

    def __init__(
        self,
        model: mujoco.MjModel,
        data: mujoco.MjData,
        params: QuadcopterParams | None = None,
        start_position: NDArray[np.float64] | None = None,
        start_orientation: NDArray[np.float64] | None = None,
    ) -> None:
        self.model = model
        self.data = data
        self.params = params or QuadcopterParams()
        self._start_pos = (
            start_position if start_position is not None else np.array([0.0, 0.0, 1.0])
        )
        # MuJoCo uses wxyz quaternion convention
        self._start_orn = (
            start_orientation
            if start_orientation is not None
            else np.array([1.0, 0.0, 0.0, 0.0])
        )

        self._motor_positions = self._compute_motor_positions()
        self._target_motor_speeds = np.zeros(4)
        self._current_motor_speeds = np.zeros(4)

        # Get site IDs for force application
        self._motor_site_ids = [
            mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_SITE, f"motor{i}_site")
            for i in range(4)
        ]
        self._body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "quadcopter")

    def _compute_motor_positions(self) -> list[NDArray[np.float64]]:
        """Compute motor positions relative to body center."""
        L = self.params.arm_length
        return [
            np.array([L, 0.0, 0.0]),  # front (+X)
            np.array([-L, 0.0, 0.0]),  # back (-X)
            np.array([0.0, L, 0.0]),  # left (+Y)
            np.array([0.0, -L, 0.0]),  # right (-Y)
        ]

    def reset(
        self,
        position: NDArray[np.float64] | None = None,
        orientation: NDArray[np.float64] | None = None,
    ) -> QuadcopterState:
        """Reset the quadcopter to initial state."""
        pos = position if position is not None else self._start_pos
        orn = orientation if orientation is not None else self._start_orn

        mujoco.mj_resetData(self.model, self.data)

        # Set initial position and orientation (freejoint: 3 pos + 4 quat)
        self.data.qpos[:3] = pos
        self.data.qpos[3:7] = orn  # wxyz

        # Zero velocities
        self.data.qvel[:] = 0

        self._current_motor_speeds = np.zeros(4)
        self._target_motor_speeds = np.zeros(4)

        mujoco.mj_forward(self.model, self.data)

        return self.get_state()

    def get_state(self) -> QuadcopterState:
        """Get current quadcopter state."""
        # Position and orientation from qpos
        pos = self.data.qpos[:3].copy()
        orn = self.data.qpos[3:7].copy()  # wxyz

        # Velocities from qvel
        vel = self.data.qvel[:3].copy()
        ang_vel = self.data.qvel[3:6].copy()

        return QuadcopterState(
            position=pos,
            velocity=vel,
            orientation=orn,
            angular_velocity=ang_vel,
            motor_speeds=self._current_motor_speeds.copy(),
        )

    def apply_action(self, action: NDArray[np.float64], dt: float) -> None:
        """Apply control action and update motor forces.

        Args:
            action: [throttle, roll_rate, pitch_rate, yaw_rate] each in [-1, 1]
            dt: timestep in seconds
        """
        # Clamp action
        action = np.clip(action, -1.0, 1.0)
        throttle, roll_cmd, pitch_cmd, yaw_cmd = action

        # Mix to motor speeds (+ configuration)
        base_throttle = (throttle + 1.0) / 2.0

        # Mixer gains
        roll_mix = 0.3
        pitch_mix = 0.3
        yaw_mix = 0.2

        self._target_motor_speeds[0] = (
            base_throttle - pitch_cmd * pitch_mix + yaw_cmd * yaw_mix
        )
        self._target_motor_speeds[1] = (
            base_throttle + pitch_cmd * pitch_mix + yaw_cmd * yaw_mix
        )
        self._target_motor_speeds[2] = (
            base_throttle - roll_cmd * roll_mix - yaw_cmd * yaw_mix
        )
        self._target_motor_speeds[3] = (
            base_throttle + roll_cmd * roll_mix - yaw_cmd * yaw_mix
        )

        # Clamp motor speeds
        self._target_motor_speeds = np.clip(self._target_motor_speeds, 0.0, 1.0)

        # First-order motor dynamics
        alpha = dt / (self.params.motor_time_constant + dt)
        self._current_motor_speeds = (
            alpha * self._target_motor_speeds + (1 - alpha) * self._current_motor_speeds
        )

        # Apply forces
        self._apply_motor_forces()

    def _apply_motor_forces(self) -> None:
        """Apply thrust and torque from each motor."""
        state = self.get_state()

        # Get rotation matrix from quaternion (wxyz)
        rot_matrix = np.zeros(9)
        mujoco.mju_quat2Mat(rot_matrix, state.orientation)
        rot_matrix = rot_matrix.reshape(3, 3)

        # Body Z-axis in world frame (thrust direction)
        body_z = rot_matrix @ np.array([0.0, 0.0, 1.0])

        # Clear external forces
        self.data.xfrc_applied[self._body_id] = 0

        total_force = np.zeros(3)
        total_torque = np.zeros(3)

        for i, (motor_pos, speed) in enumerate(
            zip(self._motor_positions, self._current_motor_speeds)
        ):
            # Thrust force
            thrust = speed * self.params.max_thrust_per_motor
            force = thrust * body_z
            total_force += force

            # Torque from thrust at offset position
            world_motor_pos = rot_matrix @ motor_pos
            thrust_torque = np.cross(world_motor_pos, force)
            total_torque += thrust_torque

            # Reaction torque (yaw) - motors 0,1 spin CW, motors 2,3 spin CCW
            direction = 1.0 if i < 2 else -1.0
            reaction_torque = direction * thrust * self.params.torque_to_thrust * body_z
            total_torque += reaction_torque

        # Apply drag
        drag_force = -self.params.drag_coeff * state.velocity
        total_force += drag_force

        # Apply to body (xfrc_applied: [force, torque])
        self.data.xfrc_applied[self._body_id, :3] = total_force
        self.data.xfrc_applied[self._body_id, 3:6] = total_torque

    def check_collision(self) -> bool:
        """Check if the quadcopter has collided with anything."""
        for i in range(self.data.ncon):
            contact = self.data.contact[i]
            geom1 = self.model.geom(contact.geom1).name
            geom2 = self.model.geom(contact.geom2).name
            # Check if either geom belongs to quadcopter and other is ground
            quad_geoms = {
                "body",
                "arm_front",
                "arm_back",
                "arm_left",
                "arm_right",
                "motor0",
                "motor1",
                "motor2",
                "motor3",
            }
            if (geom1 in quad_geoms and geom2 == "ground") or (
                geom2 in quad_geoms and geom1 == "ground"
            ):
                return True
        return False

    def get_tilt_angle(self) -> float:
        """Get the tilt angle from vertical in radians."""
        state = self.get_state()
        rot_matrix = np.zeros(9)
        mujoco.mju_quat2Mat(rot_matrix, state.orientation)
        rot_matrix = rot_matrix.reshape(3, 3)
        body_z = rot_matrix @ np.array([0.0, 0.0, 1.0])
        world_z = np.array([0.0, 0.0, 1.0])
        cos_angle = np.clip(np.dot(body_z, world_z), -1.0, 1.0)
        return math.acos(cos_angle)


def create_quadcopter_model() -> tuple[mujoco.MjModel, mujoco.MjData]:
    """Create MuJoCo model and data for quadcopter."""
    model = mujoco.MjModel.from_xml_string(QUADCOPTER_XML)
    data = mujoco.MjData(model)
    return model, data
