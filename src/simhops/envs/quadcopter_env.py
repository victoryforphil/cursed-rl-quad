"""Gymnasium environment for quadcopter waypoint tracking."""

from __future__ import annotations

import math
from typing import Any, SupportsFloat

import gymnasium as gym
import mujoco
import numpy as np
from gymnasium import spaces
from numpy.typing import NDArray

from simhops.config import Config
from simhops.core.quadcopter import (
    Quadcopter,
    QuadcopterParams,
    create_quadcopter_model,
)
from simhops.core.sensors import SensorModel, SensorNoiseParams, SensorReadings


class QuadcopterEnv(gym.Env[NDArray[np.float64], NDArray[np.float64]]):
    """Gymnasium environment for quadcopter waypoint path following.

    The goal is to navigate through a FIXED 10-waypoint path as quickly as possible.
    The path is deterministic - same waypoints every episode for consistent training.

    Observation space (19 or 22 dimensions):
        - Velocity (3): world frame [vx, vy, vz]
        - Orientation (4): quaternion [qw, qx, qy, qz] (MuJoCo wxyz)
        - Body acceleration (3): body frame [ax, ay, az]
        - Body angular velocity (3): body frame [wx, wy, wz]
        - Relative waypoint (3): normalized to [-1, 1] (direction to goal)
        - Waypoint progress (1): 0 = first waypoint, 1 = last waypoint
        - Distance to waypoint (1): normalized 0 = at target, 1 = far (>=goal_max_distance)
        - Speed (1): normalized 0 = stopped, 1 = fast (>=5 m/s)
        - Optional global position (3): included only if include_position=True

    Action space (4 dimensions):
        - Throttle: [-1, 1] where 0 is hover
        - Roll rate command: [-1, 1]
        - Pitch rate command: [-1, 1]
        - Yaw rate command: [-1, 1]

    Reward:
        - Dense distance-based reward (closer = better)
        - Time penalty (encourages speed)
        - Waypoint reach bonus
        - Completion time bonus
        - Crash penalty
    """

    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 30}

    # Fixed 10-waypoint path - an expanded course with wider spread and varied heights
    # Each waypoint can be randomized by +/- waypoint_noise meters on reset
    FIXED_WAYPOINTS: list[tuple[float, float, float]] = [
        (4.0, 0.0, 2.5),  # 1: Forward
        (8.0, 4.0, 3.5),  # 2: Forward-right, climb
        (6.0, 9.0, 5.0),  # 3: Right, climb more
        (0.0, 11.0, 6.0),  # 4: Left turn, highest point
        (-6.0, 8.0, 5.0),  # 5: Continue left, descend
        (-9.0, 3.0, 4.0),  # 6: Back toward start side
        (-8.0, -3.0, 3.0),  # 7: Cross to other side
        (-4.0, -8.0, 4.0),  # 8: Continue around
        (3.0, -6.0, 2.5),  # 9: Heading back
        (6.0, -2.0, 2.0),  # 10: Final approach (lower)
    ]

    def __init__(
        self,
        render_mode: str | None = None,
        waypoint_radius: float | None = None,  # 1m radius to pass through
        waypoint_noise: float | None = None,  # +/- meters randomization per reset
        max_episode_steps: int | None = None,  # Enough time for full path
        arena_size: float | None = None,  # Large arena for expanded path
        max_altitude: float | None = None,
        max_tilt_angle: float | None = None,  # ~80 degrees - allow aggressive flight
        disable_tilt_termination: bool
        | None = None,  # For evaluation - don't crash on tilt
        goal_max_distance: float
        | None = None,  # Max distance for normalization (larger for expanded path)
        include_position: bool | None = None,  # Include global position in observations
        random_start_waypoint: bool
        | None = None,  # Start from random waypoint (curriculum)
        quad_params: QuadcopterParams | None = None,
        sensor_params: SensorNoiseParams | None = None,
        add_sensor_noise: bool | None = None,
    ) -> None:
        super().__init__()

        cfg = Config.schema()
        env_cfg = cfg.env

        self.render_mode = render_mode
        self.num_waypoints = len(self.FIXED_WAYPOINTS)  # Always 10
        self.waypoint_radius = (
            waypoint_radius if waypoint_radius is not None else env_cfg.waypoint_radius
        )
        self.waypoint_noise = (
            waypoint_noise if waypoint_noise is not None else env_cfg.waypoint_noise
        )
        self.max_episode_steps = (
            max_episode_steps
            if max_episode_steps is not None
            else env_cfg.max_episode_steps
        )
        self.arena_size = arena_size if arena_size is not None else env_cfg.arena_size
        self.max_altitude = (
            max_altitude if max_altitude is not None else env_cfg.max_altitude
        )
        self.max_tilt_angle = (
            max_tilt_angle if max_tilt_angle is not None else env_cfg.max_tilt_angle
        )
        self.disable_tilt_termination = (
            disable_tilt_termination
            if disable_tilt_termination is not None
            else env_cfg.disable_tilt_termination
        )
        self.goal_max_distance = (
            goal_max_distance
            if goal_max_distance is not None
            else env_cfg.goal_max_distance
        )
        self.include_position = (
            include_position
            if include_position is not None
            else env_cfg.include_position
        )
        self.random_start_waypoint = (
            random_start_waypoint
            if random_start_waypoint is not None
            else env_cfg.random_start_waypoint
        )
        self.add_sensor_noise = (
            add_sensor_noise
            if add_sensor_noise is not None
            else env_cfg.add_sensor_noise
        )
        self._speed_normalization = env_cfg.speed_normalization
        self._bounds_margin = env_cfg.bounds_margin
        self._ground_threshold = env_cfg.ground_threshold
        self._reward_cfg = cfg.reward

        quad_defaults = cfg.quadcopter

        sensor_defaults = cfg.sensor
        self._quad_params = quad_params or QuadcopterParams(
            mass=quad_defaults.mass,
            arm_length=quad_defaults.arm_length,
            thrust_to_weight=quad_defaults.thrust_to_weight,
            inertia=quad_defaults.inertia,
            drag_coeff=quad_defaults.drag_coeff,
            motor_time_constant=quad_defaults.motor_time_constant,
        )
        self._sensor_params = sensor_params or SensorNoiseParams(
            accel_noise_std=sensor_defaults.accel_noise_std,
            accel_bias_std=sensor_defaults.accel_bias_std,
            accel_bias_time_constant=sensor_defaults.accel_bias_time_constant,
            gyro_noise_std=sensor_defaults.gyro_noise_std,
            gyro_bias_std=sensor_defaults.gyro_bias_std,
            gyro_bias_time_constant=sensor_defaults.gyro_bias_time_constant,
            position_noise_std=sensor_defaults.position_noise_std,
            velocity_noise_std=sensor_defaults.velocity_noise_std,
        )

        # Physics timestep (100 Hz)
        self.dt = env_cfg.timestep

        # MuJoCo setup
        self._model: mujoco.MjModel | None = None
        self._data: mujoco.MjData | None = None
        self._quad: Quadcopter | None = None
        self._sensor: SensorModel | None = None
        self._renderer: mujoco.Renderer | None = None

        # Episode state
        self._waypoints: list[NDArray[np.float64]] = []
        self._current_waypoint_idx: int = 0
        self._episode_step: int = 0
        self._total_reward: float = 0.0
        self._prev_distance: float | None = None

        # Observation space: sensor readings + waypoint info
        base_obs_dim = SensorReadings.observation_size() + 6
        obs_dim = base_obs_dim if self.include_position else base_obs_dim - 3
        self.observation_space = spaces.Box(
            low=-np.inf,
            high=np.inf,
            shape=(obs_dim,),
            dtype=np.float64,
        )

        # Action space: [throttle, roll_rate, pitch_rate, yaw_rate]
        self.action_space = spaces.Box(
            low=-1.0,
            high=1.0,
            shape=(4,),
            dtype=np.float64,
        )

    def _setup_physics(self) -> None:
        """Initialize MuJoCo model and data."""
        self._model, self._data = create_quadcopter_model()

        # Ensure timestep matches our desired dt
        self._model.opt.timestep = self.dt

    def _generate_waypoints(
        self, rng: np.random.Generator
    ) -> list[NDArray[np.float64]]:
        """Generate waypoints with optional randomization.

        Returns the fixed waypoint path with random noise added to each point.
        The noise is uniformly sampled from [-waypoint_noise, +waypoint_noise]
        for each axis (x, y, z), with z clamped to stay above ground.

        Args:
            rng: NumPy random generator

        Returns:
            List of waypoint positions as numpy arrays
        """
        waypoints = []
        for base_wp in self.FIXED_WAYPOINTS:
            wp = np.array(base_wp)

            # Add random noise if waypoint_noise > 0
            if self.waypoint_noise > 0:
                noise = rng.uniform(-self.waypoint_noise, self.waypoint_noise, size=3)
                wp = wp + noise

                # Ensure z stays above minimum height (0.5m)
                wp[2] = max(wp[2], 0.5)

            waypoints.append(wp)

        return waypoints

    def _get_observation(self, sensor_readings: SensorReadings) -> NDArray[np.float64]:
        """Construct observation from sensor readings and waypoint info."""
        # Current waypoint relative position
        # If all waypoints completed, use last waypoint
        wp_idx = min(self._current_waypoint_idx, self.num_waypoints - 1)
        current_wp = self._waypoints[wp_idx]
        relative_wp = current_wp - sensor_readings.position

        # Distance to waypoint
        distance = float(np.linalg.norm(relative_wp))

        # Normalize relative waypoint position to [-1, 1] range
        relative_wp_normalized = np.clip(
            relative_wp / self.goal_max_distance, -1.0, 1.0
        )

        # Normalized distance: 1.0 = far (at goal_max_distance), 0.0 = at waypoint
        distance_normalized = min(distance / self.goal_max_distance, 1.0)

        # Speed (normalized by a reasonable max speed)
        speed = float(np.linalg.norm(sensor_readings.velocity))
        speed_normalized = min(speed / self._speed_normalization, 1.0)

        # Normalized waypoint progress (0 = first waypoint, 1 = last waypoint)
        progress = min(self._current_waypoint_idx, self.num_waypoints - 1) / max(
            1, self.num_waypoints - 1
        )

        # Build sensor observation (optionally exclude position)
        if self.include_position:
            sensor_obs = sensor_readings.to_array()
        else:
            sensor_obs = np.concatenate(
                [
                    sensor_readings.velocity,
                    sensor_readings.orientation,
                    sensor_readings.acceleration,
                    sensor_readings.angular_velocity,
                ]
            )

        # Combine all observations
        obs = np.concatenate(
            [
                sensor_obs,
                relative_wp_normalized,
                np.array([progress]),
                np.array([distance_normalized]),
                np.array([speed_normalized]),
            ]
        )

        return obs

    def reset(
        self,
        *,
        seed: int | None = None,
        options: dict[str, Any] | None = None,
    ) -> tuple[NDArray[np.float64], dict[str, Any]]:
        """Reset the environment."""
        super().reset(seed=seed)

        # Initialize physics if needed
        if self._model is None:
            self._setup_physics()

        assert self._model is not None
        assert self._data is not None

        # Create quadcopter wrapper
        start_pos = np.array([0.0, 0.0, 1.0])
        self._quad = Quadcopter(
            self._model,
            self._data,
            params=self._quad_params,
            start_position=start_pos,
        )

        # Create sensor model
        self._sensor = SensorModel(params=self._sensor_params, seed=seed)

        # Generate fixed waypoints
        assert self.np_random is not None
        self._waypoints = self._generate_waypoints(self.np_random)
        if self.random_start_waypoint:
            self._current_waypoint_idx = int(
                self.np_random.integers(0, self.num_waypoints)
            )
        else:
            self._current_waypoint_idx = 0
        self._episode_step = 0
        self._total_reward = 0.0
        self._prev_distance = None

        # Reset quadcopter
        state = self._quad.reset()
        sensor_readings = self._sensor.get_readings(
            state, self.dt, add_noise=self.add_sensor_noise
        )
        obs = self._get_observation(sensor_readings)

        info = {
            "waypoints": self._waypoints.copy(),
            "current_waypoint_idx": self._current_waypoint_idx,
        }

        return obs, info

    def step(
        self, action: NDArray[np.float64]
    ) -> tuple[NDArray[np.float64], SupportsFloat, bool, bool, dict[str, Any]]:
        """Execute one step in the environment."""
        assert self._quad is not None
        assert self._sensor is not None
        assert self._model is not None
        assert self._data is not None

        self._episode_step += 1

        # Apply action
        self._quad.apply_action(action, self.dt)

        # Step physics
        mujoco.mj_step(self._model, self._data)

        # Get state and sensor readings
        state = self._quad.get_state()
        sensor_readings = self._sensor.get_readings(
            state, self.dt, add_noise=self.add_sensor_noise
        )

        # Current waypoint
        current_wp = self._waypoints[self._current_waypoint_idx]

        # Distance and speed
        distance = float(np.linalg.norm(state.position - current_wp))
        speed = float(np.linalg.norm(state.velocity))

        # Check if passed through waypoint (simple radius check)
        waypoint_reached = distance < self.waypoint_radius

        # Calculate reward
        reward = self._compute_reward(distance, speed, waypoint_reached)
        self._total_reward += float(reward)

        # Check termination conditions
        terminated = False
        truncated = False
        info: dict[str, Any] = {
            "distance": distance,
            "speed": speed,
            "current_waypoint_idx": self._current_waypoint_idx,
            "waypoint_reached": waypoint_reached,
            "episode_step": self._episode_step,
            # Ground truth for visualization (passed through info dict)
            "position": state.position.copy(),
            "velocity": state.velocity.copy(),
            "orientation": state.orientation.copy(),
            "waypoints": self._waypoints,
        }

        # Waypoint reached - advance to next
        if waypoint_reached:
            self._current_waypoint_idx += 1
            self._prev_distance = None  # Reset for next waypoint

            if self._current_waypoint_idx >= self.num_waypoints:
                # All waypoints completed! Big time bonus
                terminated = True
                # Bonus inversely proportional to time taken
                time_bonus = max(
                    0,
                    (self.max_episode_steps - self._episode_step)
                    / self._reward_cfg.completion_time_divisor,
                )
                reward += self._reward_cfg.path_complete_bonus + time_bonus
                info["success"] = True
                info["completion_steps"] = self._episode_step

        # Check for crash (ground collision or excessive tilt)
        if self._quad.check_collision():
            terminated = True
            reward -= self._reward_cfg.collision_penalty
            info["crash"] = "collision"

        tilt = self._quad.get_tilt_angle()
        if tilt > self.max_tilt_angle and not self.disable_tilt_termination:
            terminated = True
            reward -= self._reward_cfg.tilt_penalty
            info["crash"] = "excessive_tilt"

        # Check bounds (generous margins beyond waypoint area)
        pos = state.position
        if (
            abs(pos[0]) > self.arena_size / 2 + self._bounds_margin
            or abs(pos[1]) > self.arena_size / 2 + self._bounds_margin
            or pos[2] > self.max_altitude + self._bounds_margin
            or pos[2] < self._ground_threshold
        ):
            terminated = True
            reward -= self._reward_cfg.out_of_bounds_penalty
            info["crash"] = "out_of_bounds"

        # Check time limit
        if self._episode_step >= self.max_episode_steps:
            truncated = True
            info["time_limit_reached"] = True

        # Get observation
        obs = self._get_observation(sensor_readings)

        return obs, reward, terminated, truncated, info

    def _compute_reward(
        self, distance: float, speed: float, waypoint_reached: bool
    ) -> float:
        """Compute reward for current step.

        Reward shaping focused on speed and progress:
        - Progress reward: reward for getting closer to waypoint
        - Small time penalty to encourage speed
        - Waypoint completion bonus
        """
        reward = 0.0

        # Reward for making progress (reducing distance)
        # This is the primary reward signal
        if self._prev_distance is not None:
            progress = self._prev_distance - distance
            reward += progress * self._reward_cfg.progress_multiplier
        self._prev_distance = distance

        # Small time penalty to encourage speed (not too harsh)
        reward -= self._reward_cfg.time_penalty

        # Big bonus for reaching waypoint
        if waypoint_reached:
            reward += self._reward_cfg.waypoint_bonus

        # Graduated bonus for being close
        if distance < self.waypoint_radius * self._reward_cfg.close_proximity_3x_radius:
            reward += self._reward_cfg.close_proximity_3x_bonus
            if (
                distance
                < self.waypoint_radius * self._reward_cfg.close_proximity_1_5x_radius
            ):
                reward += self._reward_cfg.close_proximity_1_5x_bonus

        return reward

    def render(self) -> NDArray[np.uint8] | None:
        """Render the environment."""
        if self.render_mode == "rgb_array":
            if self._model is None or self._data is None:
                return None

            if self._renderer is None:
                self._renderer = mujoco.Renderer(self._model, height=480, width=640)

            # Update scene
            self._renderer.update_scene(self._data)

            # Render
            return self._renderer.render()

        return None

    def close(self) -> None:
        """Clean up resources."""
        if self._renderer is not None:
            self._renderer.close()
            self._renderer = None
