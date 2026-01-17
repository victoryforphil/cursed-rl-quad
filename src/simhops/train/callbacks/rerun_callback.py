"""Snapshot-based Rerun callback for training visualization.

Logs aggregated metrics on PPO updates and captures periodic episode snapshots
to dramatically reduce data volume while preserving training insight.
"""

from __future__ import annotations

import time
from collections import deque

import numpy as np
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.vec_env import VecEnv

import rerun as rr
from simhops.viz.rerun_viz import RerunVisualizer


class SnapshotRerunCallback(BaseCallback):
    """Snapshot-based Rerun callback for efficient training visualization.

    Instead of logging every step, this callback:
    1. Logs aggregated metrics on each PPO update
    2. Captures and logs complete episode snapshots periodically
    3. Uses dual timelines: 'ppo_update' for training progress, 'snapshot' for viz

    This reduces data volume by ~99% while maintaining visibility into training.
    """

    def __init__(
        self,
        visualizer: RerunVisualizer,
        snapshot_freq_updates: int = 20,
        snapshot_max_steps: int = 500,
        verbose: int = 0,
    ) -> None:
        """Initialize snapshot callback.

        Args:
            visualizer: Rerun visualizer instance
            snapshot_freq_updates: Log 3D snapshot every N PPO updates
            snapshot_max_steps: Maximum steps to capture in snapshot episode
            verbose: Verbosity level
        """
        super().__init__(verbose)
        self._viz = visualizer
        self._snapshot_freq_updates = snapshot_freq_updates
        self._snapshot_max_steps = snapshot_max_steps

        # Episode tracking for aggregated metrics
        self._episode_rewards: deque[float] = deque(maxlen=100)
        self._episode_lengths: deque[int] = deque(maxlen=100)
        self._episode_waypoints: deque[int] = deque(maxlen=100)
        self._episode_successes: deque[bool] = deque(maxlen=100)
        self._total_episodes = 0  # Track total episodes for logging frequency

        # Update tracking
        self._update_count = 0
        self._snapshot_count = 0
        self._last_snapshot_time = time.time()

        # Snapshot episode capture state
        self._capturing_snapshot = False
        self._snapshot_positions: list[np.ndarray] = []
        self._snapshot_orientations: list[np.ndarray] = []
        self._snapshot_waypoints: list[np.ndarray] | None = None
        self._snapshot_waypoint_idx = 0
        self._snapshot_reward = 0.0

    def _on_step(self) -> bool:
        """Called after each environment step.

        Only collects episode completion statistics, no 3D logging.
        """
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

            # Print progress periodically (every 50 episodes to reduce spam)
            if self._total_episodes % 50 == 0:
                mean_reward = float(np.mean(self._episode_rewards))
                mean_length = float(np.mean(self._episode_lengths))
                success_rate = float(np.mean(self._episode_successes))
                print(
                    f"Episodes: {self._total_episodes}, "
                    f"Mean reward (100): {mean_reward:.2f}, "
                    f"Mean length (100): {mean_length:.0f}, "
                    f"Success rate: {success_rate:.2%}"
                )

        # Check if we should start capturing a snapshot
        if self._should_capture_snapshot():
            self._start_snapshot_capture()

        # Capture snapshot data if active
        if self._capturing_snapshot:
            self._update_snapshot_capture()

        return True

    def _on_rollout_end(self) -> None:
        """Called after each PPO update (rollout collection + training).

        Logs aggregated metrics and PPO diagnostics.
        """
        self._update_count += 1
        rr.set_time("ppo_update", sequence=self._update_count)

        # Log PPO diagnostics from SB3 logger
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

        # Log aggregated training progress
        self._viz.training.log_aggregated_metrics(
            mean_reward=mean_reward,
            mean_length=mean_length,
            success_rate=success_rate,
            waypoints_per_episode=waypoints_per_episode,
        )

        # Debug: Check if we should capture snapshot
        if self._should_capture_snapshot():
            print(f"[DEBUG] Should capture snapshot at update {self._update_count}")

    def _should_capture_snapshot(self) -> bool:
        """Check if we should start capturing a new snapshot."""
        if self._capturing_snapshot:
            return False

        # Capture first snapshot at update 1, then every snapshot_freq_updates
        if self._update_count == 1:
            return True
        
        # Capture based on update frequency
        if self._update_count > 0 and self._update_count % self._snapshot_freq_updates == 0:
            return True

        return False

    def _start_snapshot_capture(self) -> None:
        """Start capturing a snapshot episode."""
        self._capturing_snapshot = True
        self._snapshot_positions = []
        self._snapshot_orientations = []
        self._snapshot_waypoints = None
        self._snapshot_waypoint_idx = 0
        self._snapshot_reward = 0.0
        
        print(f"[Snapshot {self._snapshot_count + 1}] Capturing episode at update {self._update_count}...")

    def _update_snapshot_capture(self) -> None:
        """Update snapshot capture with current step data."""
        try:
            infos = self.locals.get("infos", [])
            if not infos:
                return

            # Use first environment's info
            info = infos[0]

            # Capture position and orientation
            if "position" in info:
                self._snapshot_positions.append(info["position"].copy())
            if "orientation" in info:
                self._snapshot_orientations.append(info["orientation"].copy())

            # Capture waypoints (only once)
            if self._snapshot_waypoints is None and "waypoints" in info:
                self._snapshot_waypoints = [wp.copy() for wp in info["waypoints"]]

            # Track current waypoint
            if "current_waypoint_idx" in info:
                self._snapshot_waypoint_idx = int(info["current_waypoint_idx"])

            # Track episode completion
            if "episode" in info:
                self._snapshot_reward = float(info["episode"]["r"])
                self._finish_snapshot_capture()
            elif len(self._snapshot_positions) >= self._snapshot_max_steps:
                # Cap snapshot at max steps
                self._finish_snapshot_capture()

        except Exception:
            self._capturing_snapshot = False

    def _finish_snapshot_capture(self) -> None:
        """Finish capturing and log the snapshot episode."""
        if not self._snapshot_positions:
            self._capturing_snapshot = False
            return

        try:
            self._snapshot_count += 1

            # Set snapshot timeline
            rr.set_time("snapshot", sequence=self._snapshot_count)
            rr.set_time("ppo_update", sequence=self._update_count)

            # Log the complete snapshot trajectory
            self._viz.env.log_snapshot_trajectory(
                positions=self._snapshot_positions,
                orientations=self._snapshot_orientations
                if len(self._snapshot_orientations) == len(self._snapshot_positions)
                else None,
                waypoints=self._snapshot_waypoints,
                final_waypoint_idx=self._snapshot_waypoint_idx,
                episode_reward=self._snapshot_reward if self._snapshot_reward != 0.0 else None,
            )
            
            print(
                f"[Snapshot {self._snapshot_count}] Logged {len(self._snapshot_positions)} steps, "
                f"waypoints: {self._snapshot_waypoint_idx}, reward: {self._snapshot_reward:.1f}"
            )

        except Exception as e:
            print(f"[Snapshot {self._snapshot_count}] Error: {e}")
            pass

        finally:
            self._capturing_snapshot = False
            self._snapshot_positions = []
            self._snapshot_orientations = []
            self._snapshot_waypoints = None
