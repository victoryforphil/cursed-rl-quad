"""Rerun visualization for quadcopter simulation.

Composes EnvLogger and TrainingLogger for unified visualization.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import rerun as rr

from simhops.viz.env_logger import EnvLogger
from simhops.viz.training_logger import TrainingLogger

if TYPE_CHECKING:
    import numpy as np
    from numpy.typing import NDArray

    from simhops.core.quadcopter import QuadcopterState


class RerunVisualizer:
    """Unified Rerun visualizer for quadcopter simulation.

    Composes:
    - EnvLogger: Ground truth/physics state (drone, waypoints, trajectory)
    - TrainingLogger: RL training metrics (rewards, losses, diagnostics)

    Usage:
        viz = RerunVisualizer(app_id="simhops", spawn=True)
        viz.init()

        # Environment logging
        viz.env.log_drone(position, velocity, orientation)
        viz.env.log_waypoints(waypoints, current_idx)

        # Training logging
        rr.set_time("timestep", sequence=step)
        viz.training.log_episode(reward, length)
        viz.training.log_actions(action)
    """

    def __init__(
        self,
        app_id: str = "simhops",
        spawn: bool = True,
        ground_size: float = 25.0,
        recording_name: str | None = None,
        session_markdown: str | None = None,
    ) -> None:
        """Initialize Rerun visualizer.

        Args:
            app_id: Application ID for Rerun
            spawn: Whether to spawn the Rerun viewer
            ground_size: Size of ground plane in meters
            recording_name: Optional name shown in the viewer
            session_markdown: Optional markdown text for session context
        """
        self.app_id = app_id
        self._spawn = spawn
        self._recording_name = recording_name
        self._session_markdown = session_markdown
        self._initialized = False

        # Sub-loggers
        self.env = EnvLogger(ground_size=ground_size)
        self.training = TrainingLogger()

    def init(self) -> None:
        """Initialize Rerun recording and world setup."""
        if self._initialized:
            return

        rr.init(self.app_id, spawn=self._spawn)
        if self._recording_name:
            rr.send_recording_name(self._recording_name)
        self._initialized = True

        # Initialize world (ground plane, coordinates)
        self.env.init_world()

        if self._session_markdown:
            rr.log(
                "session/config",
                rr.TextDocument(
                    self._session_markdown, media_type=rr.MediaType.MARKDOWN
                ),
                static=True,
            )
            try:
                import rerun.blueprint as rrb

                blueprint = rrb.Blueprint(
                    rrb.TextDocumentView(
                        origin="session/config",
                        name="Session",
                    ),
                    collapse_panels=True,
                )
                rr.send_blueprint(blueprint)
            except Exception:
                pass

    def reset(self) -> None:
        """Reset for new episode."""
        self.env.reset_trajectory()

    # =========================================================================
    # Convenience methods that delegate to sub-loggers
    # =========================================================================

    def log_drone_position(
        self,
        timestep: int,
        position: NDArray[np.float64],
        velocity: NDArray[np.float64] | None = None,
        orientation: NDArray[np.float64] | None = None,
        relative_waypoint: NDArray[np.float64] | None = None,
        arm_length: float = 0.17,
    ) -> None:
        """Log drone position (convenience method with timestep).

        Args:
            timestep: Current timestep for time series
            position: [x, y, z] position
            velocity: [vx, vy, vz] velocity (optional)
            orientation: [qw, qx, qy, qz] quaternion (optional)
            relative_waypoint: Unused, kept for backward compatibility
            arm_length: Quadcopter arm length
        """
        if not self._initialized:
            self.init()

        rr.set_time("timestep", sequence=timestep)
        self.env.log_drone(position, velocity, orientation, arm_length)

    def log_quadcopter(
        self,
        state: QuadcopterState,
        arm_length: float = 0.17,
    ) -> None:
        """Log quadcopter from state object.

        Args:
            state: Quadcopter state from simulation
            arm_length: Quadcopter arm length
        """
        if not self._initialized:
            self.init()

        self.env.log_drone(
            position=state.position,
            velocity=state.velocity,
            orientation=state.orientation,
            arm_length=arm_length,
        )

    def log_waypoints(
        self,
        waypoints: list[NDArray[np.float64]],
        current_idx: int,
        radius: float = 0.5,
    ) -> None:
        """Log waypoint positions."""
        if not self._initialized:
            self.init()

        self.env.log_waypoints(waypoints, current_idx, radius)

    def log_waypoints_training(
        self,
        timestep: int,
        waypoints: list[NDArray[np.float64]],
        current_idx: int,
        radius: float = 0.5,
    ) -> None:
        """Log waypoints with timestep for training visualization."""
        if not self._initialized:
            self.init()

        rr.set_time("timestep", sequence=timestep)
        self.env.log_waypoints(waypoints, current_idx, radius)

    def log_training_metrics(
        self,
        timestep: int,
        *,
        episode_reward: float | None = None,
        episode_length: int | None = None,
        mean_reward: float | None = None,
        policy_loss: float | None = None,
        value_loss: float | None = None,
        entropy_loss: float | None = None,
        total_loss: float | None = None,
        approx_kl: float | None = None,
        clip_fraction: float | None = None,
        explained_variance: float | None = None,
        learning_rate: float | None = None,
    ) -> None:
        """Log training metrics (convenience method).

        Args:
            timestep: Current training timestep
            episode_reward: Reward for completed episode
            episode_length: Length of completed episode
            mean_reward: Rolling mean reward
            policy_loss: Policy gradient loss
            value_loss: Value function loss
            entropy_loss: Entropy bonus loss
            total_loss: Combined loss
            approx_kl: Approximate KL divergence
            clip_fraction: Fraction of clipped updates
            explained_variance: Explained variance
            learning_rate: Current learning rate
        """
        if not self._initialized:
            self.init()

        rr.set_time("timestep", sequence=timestep)

        # Episode metrics
        if episode_reward is not None and episode_length is not None:
            self.training.log_episode(
                episode_reward=episode_reward,
                episode_length=episode_length,
                mean_reward=mean_reward,
            )
        elif episode_reward is not None:
            rr.log("training/episode_reward", rr.Scalars(episode_reward))

        # Losses
        if any(
            x is not None for x in [policy_loss, value_loss, entropy_loss, total_loss]
        ):
            self.training.log_losses(
                policy_loss=policy_loss,
                value_loss=value_loss,
                entropy_loss=entropy_loss,
                total_loss=total_loss,
            )

        # PPO diagnostics
        if any(
            x is not None
            for x in [approx_kl, clip_fraction, explained_variance, learning_rate]
        ):
            self.training.log_ppo_diagnostics(
                approx_kl=approx_kl,
                clip_fraction=clip_fraction,
                explained_variance=explained_variance,
                learning_rate=learning_rate,
            )

    def log_actions(
        self,
        timestep: int,
        action: NDArray[np.float64],
    ) -> None:
        """Log policy action outputs."""
        if not self._initialized:
            self.init()

        rr.set_time("timestep", sequence=timestep)
        self.training.log_actions(action)

    def log_clipped_actions(
        self,
        timestep: int,
        action: NDArray[np.float64],
    ) -> None:
        """Log clipped action outputs."""
        if not self._initialized:
            self.init()

        rr.set_time("timestep", sequence=timestep)
        self.training.log_actions_clipped(action)

    def log_metrics(
        self,
        step: int,
        reward: float,
        distance: float,
        speed: float,
        waypoint_idx: int,
    ) -> None:
        """Log scalar metrics (legacy method)."""
        if not self._initialized:
            self.init()

        rr.set_time("step", sequence=step)
        rr.log("metrics/reward", rr.Scalars(reward))
        rr.log("metrics/distance", rr.Scalars(distance))
        rr.log("metrics/speed", rr.Scalars(speed))
        rr.log("metrics/waypoint_idx", rr.Scalars(waypoint_idx))

    def log_action(
        self,
        step: int,
        action: NDArray[np.float64],
    ) -> None:
        """Log action values (legacy method)."""
        if not self._initialized:
            self.init()

        rr.set_time("step", sequence=step)
        self.training.log_actions(action)
