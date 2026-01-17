"""Sensor simulation with realistic noise models."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

import mujoco
import numpy as np

if TYPE_CHECKING:
    from numpy.typing import NDArray

    from simhops.core.quadcopter import QuadcopterState


@dataclass
class SensorNoiseParams:
    """Noise parameters for IMU sensors."""

    # Accelerometer
    accel_noise_std: float = 0.1  # m/s^2
    accel_bias_std: float = 0.02  # m/s^2, bias random walk
    accel_bias_time_constant: float = 100.0  # seconds

    # Gyroscope
    gyro_noise_std: float = 0.01  # rad/s
    gyro_bias_std: float = 0.001  # rad/s, bias random walk
    gyro_bias_time_constant: float = 100.0  # seconds

    # Position (e.g., from motion capture or GPS)
    position_noise_std: float = 0.01  # meters

    # Velocity
    velocity_noise_std: float = 0.05  # m/s


@dataclass
class SensorState:
    """Current state of sensor biases."""

    accel_bias: NDArray[np.float64] = field(default_factory=lambda: np.zeros(3))
    gyro_bias: NDArray[np.float64] = field(default_factory=lambda: np.zeros(3))


@dataclass
class SensorReadings:
    """Sensor readings with noise applied."""

    # World frame
    position: NDArray[np.float64]  # meters
    velocity: NDArray[np.float64]  # m/s
    orientation: NDArray[np.float64]  # quaternion wxyz (MuJoCo convention)

    # Body frame
    acceleration: NDArray[np.float64]  # m/s^2 (includes gravity in body frame)
    angular_velocity: NDArray[np.float64]  # rad/s

    def to_array(self) -> NDArray[np.float64]:
        """Convert to flat array for observation space."""
        return np.concatenate(
            [
                self.position,  # 3
                self.velocity,  # 3
                self.orientation,  # 4
                self.acceleration,  # 3
                self.angular_velocity,  # 3
            ]
        )

    @staticmethod
    def observation_size() -> int:
        """Size of the flattened observation."""
        return 16  # 3 + 3 + 4 + 3 + 3


class SensorModel:
    """Simulates noisy IMU and position sensors."""

    def __init__(
        self,
        params: SensorNoiseParams | None = None,
        seed: int | None = None,
    ) -> None:
        self.params = params or SensorNoiseParams()
        self.rng = np.random.default_rng(seed)
        self.state = SensorState()
        self._prev_velocity: NDArray[np.float64] | None = None
        self._prev_time: float | None = None

    def reset(self, seed: int | None = None) -> None:
        """Reset sensor biases."""
        if seed is not None:
            self.rng = np.random.default_rng(seed)
        self.state = SensorState()
        self._prev_velocity = None
        self._prev_time = None

    def update_biases(self, dt: float) -> None:
        """Update sensor biases with random walk."""
        # Ornstein-Uhlenbeck process for bias drift
        alpha_accel = dt / self.params.accel_bias_time_constant
        alpha_gyro = dt / self.params.gyro_bias_time_constant

        self.state.accel_bias = (1 - alpha_accel) * self.state.accel_bias + np.sqrt(
            alpha_accel
        ) * self.params.accel_bias_std * self.rng.standard_normal(3)

        self.state.gyro_bias = (1 - alpha_gyro) * self.state.gyro_bias + np.sqrt(
            alpha_gyro
        ) * self.params.gyro_bias_std * self.rng.standard_normal(3)

    def get_readings(
        self,
        state: QuadcopterState,
        dt: float,
        add_noise: bool = True,
    ) -> SensorReadings:
        """Get noisy sensor readings from true state.

        Args:
            state: True quadcopter state
            dt: Time since last reading
            add_noise: Whether to add noise (disable for debugging)

        Returns:
            Noisy sensor readings
        """
        # Update biases
        if add_noise:
            self.update_biases(dt)

        # Get rotation matrix from quaternion (wxyz - MuJoCo convention)
        rot_matrix = np.zeros(9)
        mujoco.mju_quat2Mat(rot_matrix, state.orientation)
        rot_matrix = rot_matrix.reshape(3, 3)

        # Compute true acceleration in world frame
        if self._prev_velocity is not None and self._prev_time is not None:
            true_accel_world = (state.velocity - self._prev_velocity) / dt
        else:
            true_accel_world = np.zeros(3)

        self._prev_velocity = state.velocity.copy()

        # Add gravity to get specific force (what accelerometer measures)
        gravity = np.array([0.0, 0.0, -9.81])
        specific_force_world = true_accel_world - gravity

        # Transform to body frame
        body_accel = rot_matrix.T @ specific_force_world
        body_angular_vel = rot_matrix.T @ state.angular_velocity

        if add_noise:
            # Add noise to position
            position = state.position + self.rng.normal(
                0, self.params.position_noise_std, 3
            )

            # Add noise to velocity
            velocity = state.velocity + self.rng.normal(
                0, self.params.velocity_noise_std, 3
            )

            # Add noise and bias to accelerometer
            acceleration = (
                body_accel
                + self.state.accel_bias
                + self.rng.normal(0, self.params.accel_noise_std, 3)
            )

            # Add noise and bias to gyroscope
            angular_velocity = (
                body_angular_vel
                + self.state.gyro_bias
                + self.rng.normal(0, self.params.gyro_noise_std, 3)
            )

            # Orientation is typically less noisy (from sensor fusion)
            orientation = state.orientation.copy()
        else:
            position = state.position.copy()
            velocity = state.velocity.copy()
            acceleration = body_accel
            angular_velocity = body_angular_vel
            orientation = state.orientation.copy()

        return SensorReadings(
            position=position,
            velocity=velocity,
            orientation=orientation,
            acceleration=acceleration,
            angular_velocity=angular_velocity,
        )
