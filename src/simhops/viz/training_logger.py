"""Training metrics logging to Rerun.

Logs RL training data:
- Episode rewards and lengths
- Policy/value losses
- PPO diagnostics (KL, clip fraction, etc.)
- Actions
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import rerun as rr

if TYPE_CHECKING:
    import numpy as np
    from numpy.typing import NDArray


class TrainingLogger:
    """Logs RL training metrics to Rerun.

    Handles all scalar time-series data:
    - Episode statistics (reward, length)
    - Loss curves
    - PPO diagnostics
    - Action distributions
    """

    def log_episode(
        self,
        episode_reward: float,
        episode_length: int,
        mean_reward: float | None = None,
        waypoints_reached: int | None = None,
    ) -> None:
        """Log episode completion metrics.

        Args:
            episode_reward: Total reward for episode
            episode_length: Number of steps in episode
            mean_reward: Rolling mean reward (optional)
            waypoints_reached: Number of waypoints reached (optional)
        """
        rr.log("training/episode_reward", rr.Scalars(episode_reward))
        rr.log("training/episode_length", rr.Scalars(episode_length))

        if mean_reward is not None:
            rr.log("training/mean_reward_100", rr.Scalars(mean_reward))

        if waypoints_reached is not None:
            rr.log("training/waypoints_reached", rr.Scalars(waypoints_reached))

    def log_losses(
        self,
        *,
        policy_loss: float | None = None,
        value_loss: float | None = None,
        entropy_loss: float | None = None,
        total_loss: float | None = None,
    ) -> None:
        """Log training losses.

        Args:
            policy_loss: Policy gradient loss
            value_loss: Value function loss
            entropy_loss: Entropy bonus loss
            total_loss: Combined loss
        """
        if policy_loss is not None:
            rr.log("losses/policy", rr.Scalars(policy_loss))
        if value_loss is not None:
            rr.log("losses/value", rr.Scalars(value_loss))
        if entropy_loss is not None:
            rr.log("losses/entropy", rr.Scalars(entropy_loss))
        if total_loss is not None:
            rr.log("losses/total", rr.Scalars(total_loss))

    def log_ppo_diagnostics(
        self,
        *,
        approx_kl: float | None = None,
        clip_fraction: float | None = None,
        explained_variance: float | None = None,
        learning_rate: float | None = None,
    ) -> None:
        """Log PPO-specific diagnostics.

        Args:
            approx_kl: Approximate KL divergence
            clip_fraction: Fraction of clipped updates
            explained_variance: Value function explained variance
            learning_rate: Current learning rate
        """
        if approx_kl is not None:
            rr.log("ppo/approx_kl", rr.Scalars(approx_kl))
        if clip_fraction is not None:
            rr.log("ppo/clip_fraction", rr.Scalars(clip_fraction))
        if explained_variance is not None:
            rr.log("ppo/explained_variance", rr.Scalars(explained_variance))
        if learning_rate is not None:
            rr.log("ppo/learning_rate", rr.Scalars(learning_rate))

    def log_actions(self, action: NDArray[np.float64]) -> None:
        """Log policy action outputs.

        Args:
            action: [throttle, roll_rate, pitch_rate, yaw_rate]
        """
        rr.log("actions/throttle", rr.Scalars(action[0]))
        rr.log("actions/roll_rate", rr.Scalars(action[1]))
        rr.log("actions/pitch_rate", rr.Scalars(action[2]))
        rr.log("actions/yaw_rate", rr.Scalars(action[3]))

    def log_actions_clipped(self, action: NDArray[np.float64]) -> None:
        """Log clipped action outputs.

        Args:
            action: [throttle, roll_rate, pitch_rate, yaw_rate] after clipping
        """
        rr.log("actions_clipped/throttle", rr.Scalars(action[0]))
        rr.log("actions_clipped/roll_rate", rr.Scalars(action[1]))
        rr.log("actions_clipped/pitch_rate", rr.Scalars(action[2]))
        rr.log("actions_clipped/yaw_rate", rr.Scalars(action[3]))

    def log_step_metrics(
        self,
        *,
        distance: float | None = None,
        speed: float | None = None,
        reward: float | None = None,
    ) -> None:
        """Log per-step metrics.

        Args:
            distance: Distance to current waypoint
            speed: Current speed
            reward: Step reward
        """
        if distance is not None:
            rr.log("step/distance", rr.Scalars(distance))
        if speed is not None:
            rr.log("step/speed", rr.Scalars(speed))
        if reward is not None:
            rr.log("step/reward", rr.Scalars(reward))
