"""Training metrics logging to Rerun.

Logs RL training data:
- Aggregated episode statistics (on PPO updates)
- Policy/value losses
- PPO diagnostics (KL, clip fraction, etc.)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import rerun as rr

if TYPE_CHECKING:
    import numpy as np
    from numpy.typing import NDArray


class TrainingLogger:
    """Logs RL training metrics to Rerun.

    Handles scalar time-series data:
    - Aggregated episode statistics
    - Loss curves
    - PPO diagnostics
    """

    def log_aggregated_metrics(
        self,
        *,
        mean_reward: float,
        mean_length: float,
        success_rate: float,
        waypoints_per_episode: float,
    ) -> None:
        """Log smoothed training progress (called on PPO update).

        Args:
            mean_reward: Rolling mean episode reward
            mean_length: Rolling mean episode length
            success_rate: Success rate (% episodes completing path)
            waypoints_per_episode: Average waypoints reached per episode
        """
        rr.log("progress/mean_reward", rr.Scalars(mean_reward))
        rr.log("progress/mean_length", rr.Scalars(mean_length))
        rr.log("progress/success_rate", rr.Scalars(success_rate))
        rr.log("progress/waypoints_avg", rr.Scalars(waypoints_per_episode))

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
