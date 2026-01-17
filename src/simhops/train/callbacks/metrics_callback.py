"""Callback that writes agent-friendly CSV/JSON logs."""

from __future__ import annotations

import numpy as np

from stable_baselines3.common.callbacks import BaseCallback

from simhops.train.metrics import MetricsLogger


class MetricsLoggerCallback(BaseCallback):
    """Callback that writes agent-friendly CSV/JSON logs."""

    def __init__(
        self,
        metrics_logger: MetricsLogger,
        summary_update_freq: int,
        finalize_on_end: bool = True,
        verbose: int = 0,
    ) -> None:
        super().__init__(verbose)
        self._metrics_logger = metrics_logger
        self._summary_update_freq = max(1, summary_update_freq)
        self._finalize_on_end = finalize_on_end
        self._episode_rewards: list[float] = []
        self._episode_count = 0
        self._update_count = 0
        self._finalized = False

    def _on_step(self) -> bool:
        for info in self.locals.get("infos", []):
            if "episode" not in info:
                continue
            self._episode_count += 1

            episode_info = info.get("episode", {})
            ep_reward_value = None
            ep_length_value = None
            if isinstance(episode_info, dict):
                ep_reward_value = episode_info.get("r")
                ep_length_value = episode_info.get("l")

            if isinstance(ep_reward_value, (int, float)):
                ep_reward = float(ep_reward_value)
            else:
                ep_reward = 0.0
            if isinstance(ep_length_value, (int, float)):
                ep_length = int(ep_length_value)
            else:
                ep_length = 0

            self._episode_rewards.append(ep_reward)

            mean_reward = (
                float(np.mean(self._episode_rewards[-100:]))
                if self._episode_rewards
                else 0.0
            )
            crash_type = info.get("crash")
            if info.get("time_limit_reached"):
                crash_type = "timeout"

            waypoint_idx = info.get("current_waypoint_idx")
            if isinstance(waypoint_idx, (int, float)):
                waypoints_reached = int(waypoint_idx)
            else:
                waypoints_reached = 0

            distance_value = info.get("distance")
            if isinstance(distance_value, (int, float)):
                final_distance = float(distance_value)
            else:
                final_distance = 0.0

            mean_speed_value = info.get("mean_speed")
            if isinstance(mean_speed_value, (int, float)):
                mean_speed = float(mean_speed_value)
            else:
                mean_speed = 0.0

            max_tilt_value = info.get("max_tilt_deg")
            if isinstance(max_tilt_value, (int, float)):
                max_tilt_deg = float(max_tilt_value)
            else:
                max_tilt_deg = 0.0

            row = {
                "episode": self._episode_count,
                "timestep": int(self.num_timesteps),
                "reward": ep_reward,
                "length": ep_length,
                "waypoints_reached": waypoints_reached,
                "success": bool(info.get("success", False)),
                "crash_type": crash_type,
                "final_distance": final_distance,
                "mean_speed": mean_speed,
                "max_tilt_deg": max_tilt_deg,
                "time_to_first_wp": info.get("time_to_first_wp"),
            }
            self._metrics_logger.log_episode(row)

        return True

    def _on_rollout_end(self) -> None:
        if self.logger is None:
            return

        name_to_value = getattr(self.logger, "name_to_value", {})
        self._update_count += 1
        mean_reward = (
            float(np.mean(self._episode_rewards[-100:]))
            if self._episode_rewards
            else 0.0
        )
        learning_rate = (
            self.model.learning_rate
            if isinstance(self.model.learning_rate, float)
            else None
        )
        row = {
            "update": self._update_count,
            "timestep": int(self.num_timesteps),
            "policy_loss": name_to_value.get("train/policy_gradient_loss"),
            "value_loss": name_to_value.get("train/value_loss"),
            "entropy": name_to_value.get("train/entropy_loss"),
            "kl_divergence": name_to_value.get("train/approx_kl"),
            "clip_fraction": name_to_value.get("train/clip_fraction"),
            "explained_variance": name_to_value.get("train/explained_variance"),
            "learning_rate": learning_rate,
            "mean_episode_reward": mean_reward,
        }
        self._metrics_logger.log_update(row)
        if self._update_count % self._summary_update_freq == 0:
            self._metrics_logger.write_interim_summary(
                self.num_timesteps, self._episode_count
            )

    def _on_training_end(self) -> None:
        if self._finalize_on_end:
            self.finalize()

    def finalize(self) -> None:
        if self._finalized:
            return
        self._metrics_logger.finalize(self.num_timesteps, self._episode_count)
        self._finalized = True
