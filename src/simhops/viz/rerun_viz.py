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

        self._send_blueprint()

    def reset(self) -> None:
        """Reset for new episode."""
        self.env.reset_trajectory()

    def _send_blueprint(self) -> None:
        try:
            import rerun.blueprint as rrb

            blueprint = rrb.Blueprint(
                rrb.Horizontal(
                    rrb.Spatial3DView(
                        origin="world",
                        name="Latest Policy",
                    ),
                    rrb.Vertical(
                        rrb.TimeSeriesView(
                            origin="progress",
                            name="Training Progress",
                        ),
                        rrb.TimeSeriesView(
                            origin="losses",
                            name="Losses",
                        ),
                        rrb.TextDocumentView(
                            origin="session/config",
                            name="Config",
                        ),
                        rrb.TextLogView(
                            origin="logs",
                            name="Logs",
                        ),
                        name="Metrics",
                    ),
                    column_shares=[2, 1],
                ),
                collapse_panels=True,
            )
            rr.send_blueprint(blueprint)
        except Exception:
            return

    # =========================================================================
    # Convenience methods that delegate to sub-loggers
    # =========================================================================

    def log_quadcopter(
        self,
        state: QuadcopterState,
        arm_length: float = 0.17,
    ) -> None:
        """Log quadcopter from state object (for evaluation/demo).

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
        """Log waypoint positions (for evaluation/demo).

        Args:
            waypoints: List of waypoint positions
            current_idx: Current waypoint index
            radius: Waypoint visualization radius
        """
        if not self._initialized:
            self.init()

        self.env.log_waypoints(waypoints, current_idx, radius)
