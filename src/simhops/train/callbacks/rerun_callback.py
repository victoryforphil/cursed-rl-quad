"""Callback for logging training metrics and ground truth to Rerun.

Ground truth (position, waypoints) is passed via the info dict from
the environment, allowing accurate 3D visualization even with SubprocVecEnv.
"""

from __future__ import annotations

import numpy as np

from stable_baselines3.common.callbacks import BaseCallback

from simhops.viz.rerun_viz import RerunVisualizer


class RerunTrainingCallback(BaseCallback):
    """Callback for logging training metrics and ground truth to Rerun.

    Ground truth (position, waypoints) is passed via the info dict from
    the environment, allowing accurate 3D visualization even with SubprocVecEnv.
    """

    def __init__(
        self,
        visualizer: RerunVisualizer,
        log_3d_freq: int = 3,
        verbose: int = 0,
    ) -> None:
        """Initialize callback.

        Args:
            visualizer: Rerun visualizer instance
            log_3d_freq: Log 3D data every N steps (~30fps at 100Hz sim)
            verbose: Verbosity level
        """
        super().__init__(verbose)
        self._viz = visualizer
        self._log_3d_freq = log_3d_freq
        self._episode_rewards: list[float] = []
        self._episode_lengths: list[int] = []

    def _on_step(self) -> bool:
        # Log 3D position and actions at high rate (~30fps)
        if self.num_timesteps % self._log_3d_freq == 0:
            self._log_3d_state()
            self._log_actions()

        # Check for completed episodes
        for info in self.locals.get("infos", []):
            # Check for terminal info - episode ended
            if "terminal_observation" in info:
                self._viz.reset()

            if "episode" in info:
                ep_reward = info["episode"]["r"]
                ep_length = info["episode"]["l"]
                self._episode_rewards.append(ep_reward)
                self._episode_lengths.append(ep_length)

                mean_reward = float(np.mean(self._episode_rewards[-100:]))

                # Log to Rerun
                self._viz.log_training_metrics(
                    self.num_timesteps,
                    episode_reward=ep_reward,
                    episode_length=ep_length,
                    mean_reward=mean_reward,
                )

                if len(self._episode_rewards) % 10 == 0:
                    mean_length = np.mean(self._episode_lengths[-100:])
                    print(
                        f"Episodes: {len(self._episode_rewards)}, "
                        f"Mean reward (100): {mean_reward:.2f}, "
                        f"Mean length (100): {mean_length:.0f}"
                    )

        return True

    def _log_3d_state(self) -> None:
        """Log 3D drone state from ground truth in info dict."""
        try:
            infos = self.locals.get("infos", [])
            if not infos:
                return

            # Use first environment's info
            info = infos[0]

            # Log drone position from ground truth
            if "position" in info:
                self._viz.log_drone_position(
                    self.num_timesteps,
                    position=info["position"],
                    velocity=info.get("velocity"),
                    orientation=info.get("orientation"),
                )

            # Log actual randomized waypoints
            if "waypoints" in info:
                self._viz.log_waypoints_training(
                    self.num_timesteps,
                    info["waypoints"],
                    info.get("current_waypoint_idx", 0),
                )

        except Exception:
            pass  # Silently fail - 3D viz is optional

    def _log_actions(self) -> None:
        """Log PPO actions/policy outputs."""
        actions = self.locals.get("actions")
        if actions is None or len(actions) == 0:
            return

        action = actions[0]
        self._viz.log_actions(self.num_timesteps, action=action)

        clipped_actions = self.locals.get("clipped_actions")
        if clipped_actions is not None and len(clipped_actions) > 0:
            self._viz.log_clipped_actions(self.num_timesteps, action=clipped_actions[0])

    def _on_rollout_end(self) -> None:
        """Log losses after each PPO update."""
        if self.logger is not None:
            name_to_value = getattr(self.logger, "name_to_value", {})

            self._viz.log_training_metrics(
                self.num_timesteps,
                policy_loss=name_to_value.get("train/policy_gradient_loss"),
                value_loss=name_to_value.get("train/value_loss"),
                entropy_loss=name_to_value.get("train/entropy_loss"),
                total_loss=name_to_value.get("train/loss"),
                approx_kl=name_to_value.get("train/approx_kl"),
                clip_fraction=name_to_value.get("train/clip_fraction"),
                explained_variance=name_to_value.get("train/explained_variance"),
                learning_rate=self.model.learning_rate
                if isinstance(self.model.learning_rate, float)
                else None,
            )
