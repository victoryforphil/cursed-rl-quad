"""Environment/ground truth data logging to Rerun.

Logs physical simulation state:
- Drone position, velocity, orientation
- Waypoints and progress
- Snapshot trajectory visualization
- Ground plane and world setup
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
import rerun as rr

if TYPE_CHECKING:
    from numpy.typing import NDArray

    from simhops.core.quadcopter import QuadcopterState


class EnvLogger:
    """Logs environment/simulation ground truth to Rerun.

    Handles all 3D world visualization:
    - Drone pose and motion
    - Waypoints with progress coloring
    - Snapshot trajectory visualization
    - World coordinate system and ground plane
    """

    def __init__(self, ground_size: float = 25.0) -> None:
        """Initialize environment logger.

        Args:
            ground_size: Size of ground plane in meters
        """
        self._ground_size = ground_size
        self._initialized = False

    def init_world(self) -> None:
        """Set up 3D world coordinate system and ground plane."""
        if self._initialized:
            return

        # Set up 3D view coordinates
        rr.log("world", rr.ViewCoordinates.RIGHT_HAND_Z_UP, static=True)

        # Log ground plane
        ground_vertices = np.array(
            [
                [-self._ground_size, -self._ground_size, 0],
                [self._ground_size, -self._ground_size, 0],
                [self._ground_size, self._ground_size, 0],
                [-self._ground_size, self._ground_size, 0],
            ]
        )
        ground_indices = np.array([[0, 1, 2], [0, 2, 3]])
        rr.log(
            "world/ground",
            rr.Mesh3D(
                vertex_positions=ground_vertices,
                triangle_indices=ground_indices,
                vertex_colors=[[80, 80, 80, 80]] * 4,
            ),
            static=True,
        )

        # Log axis indicators at origin
        rr.log(
            "world/origin",
            rr.Arrows3D(
                origins=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                vectors=[[2, 0, 0], [0, 2, 0], [0, 0, 2]],
                colors=[[255, 0, 0, 200], [0, 255, 0, 200], [0, 0, 255, 200]],
            ),
            static=True,
        )

        self._initialized = True

    def log_drone(
        self,
        position: NDArray[np.float64],
        velocity: NDArray[np.float64] | None = None,
        orientation: NDArray[np.float64] | None = None,
        arm_length: float = 0.17,
    ) -> None:
        """Log drone position and orientation.

        Args:
            position: [x, y, z] world position
            velocity: [vx, vy, vz] world velocity (optional)
            orientation: [qw, qx, qy, qz] quaternion (optional)
            arm_length: Quadcopter arm length for visualization
        """
        # Log position as a point
        rr.log(
            "world/drone/center",
            rr.Points3D(
                positions=[position],
                colors=[[50, 50, 200, 255]],
                radii=[0.08],
            ),
        )

        # Log velocity vector if provided
        if velocity is not None:
            speed = float(np.linalg.norm(velocity))
            if speed > 0.1:
                rr.log(
                    "world/drone/velocity",
                    rr.Arrows3D(
                        origins=[position],
                        vectors=[velocity * 0.3],
                        colors=[[0, 200, 255, 200]],
                    ),
                )

        # Log orientation if provided
        if orientation is not None:
            qw, qx, qy, qz = orientation
            rot_matrix = self._quat_to_rotation_matrix(qx, qy, qz, qw)

            # Motor positions in body frame (+ configuration)
            motor_offsets = np.array(
                [
                    [arm_length, 0, 0],  # front
                    [-arm_length, 0, 0],  # back
                    [0, arm_length, 0],  # left
                    [0, -arm_length, 0],  # right
                ]
            )
            motor_positions = position + (rot_matrix @ motor_offsets.T).T

            # Log arms
            arm_lines = [
                [position, motor_positions[0]],
                [position, motor_positions[1]],
                [position, motor_positions[2]],
                [position, motor_positions[3]],
            ]
            rr.log(
                "world/drone/arms",
                rr.LineStrips3D(
                    arm_lines,
                    colors=[
                        [255, 50, 50, 255],  # front - red
                        [100, 100, 100, 255],  # back - gray
                        [50, 255, 50, 255],  # left - green
                        [50, 255, 50, 255],  # right - green
                    ],
                ),
            )

            # Log body up direction
            body_z = rot_matrix @ np.array([0, 0, 0.25])
            rr.log(
                "world/drone/up",
                rr.Arrows3D(
                    origins=[position],
                    vectors=[body_z],
                    colors=[[255, 255, 0, 200]],
                ),
            )

    def log_drone_from_state(self, state: QuadcopterState) -> None:
        """Log drone from QuadcopterState object.

        Args:
            state: Quadcopter state from simulation
        """
        self.log_drone(
            position=state.position,
            velocity=state.velocity,
            orientation=state.orientation,
        )

    def log_waypoints(
        self,
        waypoints: list[NDArray[np.float64]],
        current_idx: int,
        radius: float = 0.5,
    ) -> None:
        """Log waypoints with progress coloring.

        Args:
            waypoints: List of [x, y, z] waypoint positions
            current_idx: Index of current target waypoint
            radius: Waypoint sphere radius for visualization
        """
        positions = np.array(waypoints)
        colors = []
        radii = []

        for i in range(len(waypoints)):
            if i < current_idx:
                colors.append([0, 255, 0, 100])  # Green - completed
                radii.append(radius * 0.5)
            elif i == current_idx:
                colors.append([255, 255, 0, 255])  # Yellow - current target
                radii.append(radius)
            else:
                colors.append([255, 128, 0, 150])  # Orange - upcoming
                radii.append(radius * 0.7)

        rr.log(
            "world/waypoints",
            rr.Points3D(
                positions=positions,
                colors=colors,
                radii=radii,
            ),
        )

        # Log path connecting waypoints
        if len(waypoints) > 1:
            rr.log(
                "world/waypoint_path",
                rr.LineStrips3D(
                    [positions],
                    colors=[[180, 180, 180, 80]],
                ),
            )

    def log_target_arrow(
        self,
        position: NDArray[np.float64],
        target: NDArray[np.float64],
    ) -> None:
        """Log arrow from drone to current target waypoint.

        Args:
            position: Current drone position
            target: Target waypoint position
        """
        direction = target - position
        distance = float(np.linalg.norm(direction))

        if distance > 0.1:
            # Normalize and scale for visibility
            direction_normalized = direction / distance
            arrow_length = min(distance, 3.0)  # Cap arrow length
            vector = direction_normalized * arrow_length

            rr.log(
                "world/drone/to_target",
                rr.Arrows3D(
                    origins=[position],
                    vectors=[vector],
                    colors=[[255, 100, 100, 200]],
                ),
            )

    def log_snapshot_trajectory(
        self,
        positions: list[NDArray[np.float64]],
        orientations: list[NDArray[np.float64]] | None = None,
        waypoints: list[NDArray[np.float64]] | None = None,
        final_waypoint_idx: int = 0,
        episode_reward: float | None = None,
        arm_length: float = 0.17,
    ) -> None:
        """Log a complete episode trajectory as a snapshot.

        Args:
            positions: List of [x, y, z] positions throughout episode
            orientations: List of [qw, qx, qy, qz] quaternions (optional)
            waypoints: List of waypoint positions (optional)
            final_waypoint_idx: Final waypoint index reached
            episode_reward: Total episode reward (optional)
            arm_length: Quadcopter arm length
        """
        if not positions:
            return

        # Log complete trajectory as single line (static reference)
        trajectory_array = np.array(positions)
        rr.log(
            "world/snapshot/trajectory_line",
            rr.LineStrips3D(
                [trajectory_array],
                colors=[[100, 100, 255, 180]],
            ),
        )

        # Log waypoints if provided (static)
        if waypoints:
            self.log_waypoints(waypoints, final_waypoint_idx)

        # Log episode summary (static)
        if episode_reward is not None and waypoints:
            summary_text = (
                f"**Episode Snapshot**\n\n"
                f"- Reward: {episode_reward:.1f}\n"
                f"- Waypoints: {final_waypoint_idx}/{len(waypoints)}\n"
                f"- Steps: {len(positions)}"
            )
            rr.log(
                "snapshot/summary",
                rr.TextDocument(summary_text, media_type=rr.MediaType.MARKDOWN),
            )

        # Now log animated drone flying through the course
        # Each step gets its own timestamp on snapshot_step timeline
        has_orientations = orientations and len(orientations) == len(positions)
        
        for step_idx, pos in enumerate(positions):
            # Set the step timeline for animation
            rr.set_time("snapshot_step", sequence=step_idx)
            
            # Log drone center
            rr.log(
                "world/snapshot/drone/center",
                rr.Points3D(
                    positions=[pos],
                    colors=[[50, 50, 200, 255]],
                    radii=[0.08],
                ),
            )
            
            # Log orientation if available
            if has_orientations:
                orient = orientations[step_idx]
                qw, qx, qy, qz = orient
                rot_matrix = self._quat_to_rotation_matrix(qx, qy, qz, qw)

                # Motor positions
                motor_offsets = np.array(
                    [
                        [arm_length, 0, 0],
                        [-arm_length, 0, 0],
                        [0, arm_length, 0],
                        [0, -arm_length, 0],
                    ]
                )
                motor_positions = pos + (rot_matrix @ motor_offsets.T).T

                # Log arms
                arm_lines = [
                    [pos, motor_positions[0]],
                    [pos, motor_positions[1]],
                    [pos, motor_positions[2]],
                    [pos, motor_positions[3]],
                ]
                rr.log(
                    "world/snapshot/drone/arms",
                    rr.LineStrips3D(
                        arm_lines,
                        colors=[
                            [255, 50, 50, 255],
                            [100, 100, 100, 255],
                            [50, 255, 50, 255],
                            [50, 255, 50, 255],
                        ],
                    ),
                )

                # Log up vector
                body_z = rot_matrix @ np.array([0, 0, 0.25])
                rr.log(
                    "world/snapshot/drone/up",
                    rr.Arrows3D(
                        origins=[pos],
                        vectors=[body_z],
                        colors=[[255, 255, 0, 200]],
                    ),
                )

    def reset_trajectory(self) -> None:
        """Clear trajectory for new episode (deprecated, kept for compatibility)."""
        pass

    @staticmethod
    def _quat_to_rotation_matrix(
        qx: float, qy: float, qz: float, qw: float
    ) -> NDArray[np.float64]:
        """Convert quaternion to rotation matrix."""
        n = np.sqrt(qx * qx + qy * qy + qz * qz + qw * qw)
        if n < 1e-10:
            return np.eye(3)
        qx, qy, qz, qw = qx / n, qy / n, qz / n, qw / n

        return np.array(
            [
                [
                    1 - 2 * (qy * qy + qz * qz),
                    2 * (qx * qy - qz * qw),
                    2 * (qx * qz + qy * qw),
                ],
                [
                    2 * (qx * qy + qz * qw),
                    1 - 2 * (qx * qx + qz * qz),
                    2 * (qy * qz - qx * qw),
                ],
                [
                    2 * (qx * qz - qy * qw),
                    2 * (qy * qz + qx * qw),
                    1 - 2 * (qx * qx + qy * qy),
                ],
            ]
        )
