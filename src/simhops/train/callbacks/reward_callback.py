"""Callback for logging episode rewards (console only, no Rerun)."""

from __future__ import annotations

import numpy as np

from stable_baselines3.common.callbacks import BaseCallback


class RewardLoggerCallback(BaseCallback):
    """Callback for logging episode rewards (console only, no Rerun)."""

    def __init__(self, verbose: int = 0) -> None:
        super().__init__(verbose)
        self._episode_rewards: list[float] = []
        self._episode_lengths: list[int] = []
        self._waypoints_reached: list[int] = []
        self._total_episodes = 0

    def _on_step(self) -> bool:
        for info in self.locals.get("infos", []):
            if "episode" in info:
                self._episode_rewards.append(info["episode"]["r"])
                self._episode_lengths.append(info["episode"]["l"])

                # Track waypoints reached
                wp_idx = info.get("current_waypoint_idx", 0)
                self._waypoints_reached.append(wp_idx)
                self._total_episodes += 1

                if self._total_episodes % 50 == 0:
                    mean_reward = np.mean(self._episode_rewards[-100:])
                    mean_length = np.mean(self._episode_lengths[-100:])
                    mean_waypoints = np.mean(self._waypoints_reached[-100:])
                    print(
                        f"Episodes: {self._total_episodes}, "
                        f"Mean reward (100): {mean_reward:.2f}, "
                        f"Mean length (100): {mean_length:.0f}, "
                        f"Mean waypoints (100): {mean_waypoints:.1f}/10"
                    )

        return True
