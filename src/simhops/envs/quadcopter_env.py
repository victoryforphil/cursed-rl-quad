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

    The goal is to navigate through a 10-waypoint base path as quickly as possible.
    The base path can be rotated around the origin each episode to avoid overfitting.

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
        (5.5, 0.0, 3.3),  # 1: Forward
        (10.5, 5.5, 4.5),  # 2: Forward-right, climb
        (7.5, 11.5, 6.2),  # 3: Right, climb more
        (0.0, 14.0, 7.2),  # 4: Left turn, highest point
        (-7.5, 10.0, 6.2),  # 5: Continue left, descend
        (-11.5, 4.0, 5.2),  # 6: Back toward start side
        (-10.0, -4.0, 4.2),  # 7: Cross to other side
        (-5.5, -10.5, 5.2),  # 8: Continue around
        (4.5, -7.5, 3.5),  # 9: Heading back
        (7.5, -2.5, 3.0),  # 10: Final approach (lower)
    ]

    def __init__(
        self,
        render_mode: str | None = None,
        waypoint_radius: float | None = None,  # 1m radius to pass through
        waypoint_noise: float | None = None,  # +/- meters randomization per reset
        waypoint_yaw_random: bool | None = None,  # Randomize waypoint yaw each reset
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
        max_waypoints: int | None = None,  # Limit number of waypoints for curriculum
        action_scale: float | None = None,  # Scale action magnitude (curriculum)
        random_start_position: bool | None = None,  # Randomize initial position
        start_position_noise: float | None = None,  # +/- meters per axis
        quad_params: QuadcopterParams | None = None,
        sensor_params: SensorNoiseParams | None = None,
        add_sensor_noise: bool | None = None,
    ) -> None:
        super().__init__()

        cfg = Config.schema()
        env_cfg = cfg.env

        self.render_mode = render_mode
        self.num_waypoints = len(self.FIXED_WAYPOINTS)  # Always 10
        self._max_waypoints_effective = self.num_waypoints
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
        self.waypoint_yaw_random = (
            waypoint_yaw_random
            if waypoint_yaw_random is not None
            else env_cfg.waypoint_yaw_random
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
        self.max_waypoints = (
            max_waypoints if max_waypoints is not None else env_cfg.max_waypoints
        )
        self.add_sensor_noise = (
            add_sensor_noise
            if add_sensor_noise is not None
            else env_cfg.add_sensor_noise
        )
        self.action_scale = (
            action_scale if action_scale is not None else env_cfg.action_scale
        )
        self.random_start_position = (
            random_start_position
            if random_start_position is not None
            else env_cfg.random_start_position
        )
        self.start_position_noise = (
            start_position_noise
            if start_position_noise is not None
            else env_cfg.start_position_noise
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
        self._waypoint_yaw: float = 0.0
        self._current_waypoint_idx: int = 0
        self._episode_step: int = 0
        self._total_reward: float = 0.0
        self._prev_distance: float | None = None
        self._episode_speed_sum: float = 0.0
        self._episode_speed_steps: int = 0
        self._episode_max_tilt: float = 0.0
        self._time_to_first_wp: int | None = None

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
    ) -> tuple[list[NDArray[np.float64]], float]:
        """Generate waypoints with optional randomization.

        Returns the fixed waypoint path with random yaw rotation applied first,
        then noise added to each point. Noise is uniformly sampled from
        [-waypoint_noise, +waypoint_noise] for each axis (x, y, z), with z
        clamped to stay above ground. Rotation is disabled when
        waypoint_yaw_random is false.

        Args:
            rng: NumPy random generator

        Returns:
            List of waypoint positions as numpy arrays and the applied yaw (rad)
        """
        yaw = float(rng.uniform(0.0, 2 * math.pi)) if self.waypoint_yaw_random else 0.0
        cos_yaw = math.cos(yaw)
        sin_yaw = math.sin(yaw)

        waypoints = []
        for base_wp in self.FIXED_WAYPOINTS:
            wp = np.array(base_wp, dtype=np.float64)

            rotated_xy = np.array(
                [
                    wp[0] * cos_yaw - wp[1] * sin_yaw,
                    wp[0] * sin_yaw + wp[1] * cos_yaw,
                ]
            )
            wp[:2] = rotated_xy

            # Add random noise if waypoint_noise > 0
            if self.waypoint_noise > 0:
                noise = rng.uniform(-self.waypoint_noise, self.waypoint_noise, size=3)
                wp = wp + noise

                # Ensure z stays above minimum height (0.5m)
                wp[2] = max(wp[2], 0.5)

            waypoints.append(wp)

        return waypoints, yaw

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
        max_waypoints = max(1, self._max_waypoints_effective)
        progress = min(self._current_waypoint_idx, max_waypoints - 1) / max(
            1, max_waypoints - 1
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
        if self.random_start_position and self.start_position_noise > 0:
            start_pos = start_pos + self.np_random.uniform(
                -self.start_position_noise, self.start_position_noise, size=3
            )
            start_pos[2] = max(start_pos[2], self._ground_threshold + 0.1)
        elif self.random_start_position:
            jitter = self._ground_threshold + 0.1
            start_pos = start_pos + self.np_random.uniform(-jitter, jitter, size=3)
            start_pos[2] = max(start_pos[2], self._ground_threshold + 0.1)
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
        self._waypoints, self._waypoint_yaw = self._generate_waypoints(self.np_random)
        max_waypoints = (
            self.max_waypoints if self.max_waypoints is not None else self.num_waypoints
        )
        max_waypoints = max(1, min(max_waypoints, self.num_waypoints))
        self._max_waypoints_effective = max_waypoints
        if self.random_start_waypoint:
            self._current_waypoint_idx = int(self.np_random.integers(0, max_waypoints))
        else:
            self._current_waypoint_idx = 0
        self._episode_step = 0
        self._total_reward = 0.0
        self._prev_distance = None
        self._episode_speed_sum = 0.0
        self._episode_speed_steps = 0
        self._episode_max_tilt = 0.0
        self._time_to_first_wp = None

        # Reset quadcopter
        state = self._quad.reset()
        sensor_readings = self._sensor.get_readings(
            state, self.dt, add_noise=self.add_sensor_noise
        )
        obs = self._get_observation(sensor_readings)

        info = {
            "waypoints": self._waypoints.copy(),
            "waypoint_yaw": self._waypoint_yaw,
            "current_waypoint_idx": self._current_waypoint_idx,
            "max_waypoints": max_waypoints,
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
        scaled_action = action * self.action_scale
        self._quad.apply_action(scaled_action, self.dt)

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

        self._episode_speed_sum += speed
        self._episode_speed_steps += 1

        tilt = self._quad.get_tilt_angle()
        if tilt > self._episode_max_tilt:
            self._episode_max_tilt = tilt

        # Check if passed through waypoint (simple radius check)
        waypoint_reached = distance < self.waypoint_radius

        # Calculate reward
        reward = self._compute_reward(distance, speed, waypoint_reached)
        self._total_reward += float(reward)

        max_waypoints = self._max_waypoints_effective

        # Check termination conditions
        terminated = False
        truncated = False
        mean_speed = (
            self._episode_speed_sum / self._episode_speed_steps
            if self._episode_speed_steps > 0
            else 0.0
        )

        info: dict[str, Any] = {
            "distance": distance,
            "speed": speed,
            "mean_speed": mean_speed,
            "max_tilt_deg": math.degrees(self._episode_max_tilt),
            "time_to_first_wp": self._time_to_first_wp,
            "current_waypoint_idx": self._current_waypoint_idx,
            "max_waypoints": max_waypoints,
            "waypoint_reached": waypoint_reached,
            "episode_step": self._episode_step,
            "waypoint_yaw": self._waypoint_yaw,
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
            if self._time_to_first_wp is None:
                self._time_to_first_wp = self._episode_step

            if self._current_waypoint_idx >= max_waypoints:
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
