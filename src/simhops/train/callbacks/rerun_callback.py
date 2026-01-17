"""Training metrics Rerun callback for PPO visualization.

Logs aggregated metrics on PPO updates for efficient training visualization.
"""

from __future__ import annotations

from collections import deque

import numpy as np
from stable_baselines3.common.callbacks import BaseCallback

import rerun as rr
from simhops.viz.rerun_viz import RerunVisualizer


class TrainingMetricsCallback(BaseCallback):
    """Training metrics Rerun callback for efficient PPO visualization.

    Logs aggregated episode statistics and PPO diagnostics on each update.
    Also logs static waypoints for reference.
    """

    def __init__(
        self,
        visualizer: RerunVisualizer,
        verbose: int = 0,
    ) -> None:
        """Initialize training metrics callback.

        Args:
            visualizer: Rerun visualizer instance
            verbose: Verbosity level
        """
        super().__init__(verbose)
        self._viz = visualizer

        # Episode tracking for aggregated metrics
        self._episode_rewards: deque[float] = deque(maxlen=100)
        self._episode_lengths: deque[int] = deque(maxlen=100)
        self._episode_waypoints: deque[int] = deque(maxlen=100)
        self._episode_successes: deque[bool] = deque(maxlen=100)
        self._total_episodes = 0  # Track total episodes for logging frequency

        # Update tracking
        self._update_count = 0
        
        # Waypoint logging
        self._waypoints_logged = False

    def _on_step(self) -> bool:
        """Called after each environment step.

        Only collects episode completion statistics and logs waypoints once.
        """
        # Log waypoints from first environment (static reference)
        if not self._waypoints_logged:
            infos = self.locals.get("infos", [])
            if infos and "waypoints" in infos[0]:
                waypoints = infos[0]["waypoints"]
                self._viz.env.log_waypoints(waypoints, 0, radius=1.0)
                self._waypoints_logged = True
        
        # Check for completed episodes
        for info in self.locals.get("infos", []):
            if "episode" not in info:
                continue

            # Extract episode statistics
            ep_reward = float(info["episode"]["r"])
            ep_length = int(info["episode"]["l"])
            waypoint_idx = int(info.get("current_waypoint_idx", 0))
            success = bool(info.get("success", False))

            # Update rolling statistics
            self._episode_rewards.append(ep_reward)
            self._episode_lengths.append(ep_length)
            self._episode_waypoints.append(waypoint_idx)
            self._episode_successes.append(success)
            self._total_episodes += 1

            # Log progress periodically (every 50 episodes to reduce spam)
            if self._total_episodes % 50 == 0:
                mean_reward = float(np.mean(self._episode_rewards))
                mean_length = float(np.mean(self._episode_lengths))
                success_rate = float(np.mean(self._episode_successes))
                from simhops.logging import log

                log(
                    f"Episodes: {self._total_episodes}, "
                    f"Mean reward (100): {mean_reward:.2f}, "
                    f"Mean length (100): {mean_length:.0f}, "
                    f"Success rate: {success_rate:.2%}"
                )

        return True

    def _on_rollout_end(self) -> None:
        """Called after each PPO update (rollout collection + training).

        Logs aggregated metrics and PPO diagnostics every update.
        """
        self._update_count += 1
        rr.set_time("ppo_update", sequence=self._update_count)

        # Log PPO diagnostics from SB3 logger (every update for responsive visualization)
        if self.logger is not None:
            name_to_value = getattr(self.logger, "name_to_value", {})

            self._viz.training.log_losses(
                policy_loss=name_to_value.get("train/policy_gradient_loss"),
                value_loss=name_to_value.get("train/value_loss"),
                entropy_loss=name_to_value.get("train/entropy_loss"),
                total_loss=name_to_value.get("train/loss"),
            )

            self._viz.training.log_ppo_diagnostics(
                approx_kl=name_to_value.get("train/approx_kl"),
                clip_fraction=name_to_value.get("train/clip_fraction"),
                explained_variance=name_to_value.get("train/explained_variance"),
                learning_rate=self.model.learning_rate
                if isinstance(self.model.learning_rate, float)
                else None,
            )

        if not self._episode_rewards:
            return

        # Calculate aggregated statistics
        mean_reward = float(np.mean(self._episode_rewards))
        mean_length = float(np.mean(self._episode_lengths))
        waypoints_per_episode = float(np.mean(self._episode_waypoints))
        success_rate = float(np.mean(self._episode_successes))

        # Log aggregated training progress every update
        self._viz.training.log_aggregated_metrics(
            mean_reward=mean_reward,
            mean_length=mean_length,
            success_rate=success_rate,
            waypoints_per_episode=waypoints_per_episode,
        )
