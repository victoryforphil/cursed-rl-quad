"""Structured metrics logger for training runs."""

from __future__ import annotations

import csv
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path

import numpy as np

from simhops.config import Config


class MetricsLogger:
    """Structured metrics logger for training runs."""

    def __init__(self, run_path: Path) -> None:
        self._run_path = run_path
        self._start_time = time.time()
        self._episodes: list[dict[str, float | int | str | None]] = []
        self._updates: list[dict[str, float | int]] = []
        self._run_id = run_path.name

        self._episodes_path = run_path / "episodes.csv"
        self._updates_path = run_path / "updates.csv"
        self._summary_path = run_path / "training_summary.json"
        self._experiments_path = run_path.parent / "experiments.csv"

        self._episodes_file = self._episodes_path.open(
            "w", newline="", encoding="utf-8"
        )
        self._updates_file = self._updates_path.open("w", newline="", encoding="utf-8")

        self._episode_writer = csv.DictWriter(
            self._episodes_file,
            fieldnames=[
                "episode",
                "timestep",
                "reward",
                "length",
                "waypoints_reached",
                "success",
                "crash_type",
                "final_distance",
                "mean_speed",
                "max_tilt_deg",
                "time_to_first_wp",
            ],
        )
        self._episode_writer.writeheader()

        self._update_writer = csv.DictWriter(
            self._updates_file,
            fieldnames=[
                "update",
                "timestep",
                "policy_loss",
                "value_loss",
                "entropy",
                "kl_divergence",
                "clip_fraction",
                "explained_variance",
                "learning_rate",
                "mean_episode_reward",
            ],
        )
        self._update_writer.writeheader()

        self._write_config(run_path / "config.json")

    def _write_config(self, path: Path) -> None:
        cfg = Config.schema()
        payload = {
            "run_id": self._run_id,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "git_commit": self._git_commit(),
            "hyperparameters": {
                "learning_rate": cfg.ppo.learning_rate,
                "batch_size": cfg.ppo.batch_size,
                "gamma": cfg.ppo.gamma,
                "gae_lambda": cfg.ppo.gae_lambda,
                "clip_range": cfg.ppo.clip_range,
                "ent_coef": cfg.ppo.ent_coef,
                "n_envs": cfg.training.n_envs,
                "total_timesteps": cfg.training.total_timesteps,
            },
            "environment": {
                "waypoint_noise": cfg.env.waypoint_noise,
                "waypoint_radius": cfg.env.waypoint_radius,
                "max_episode_steps": cfg.env.max_episode_steps,
                "include_position": cfg.env.include_position,
                "add_sensor_noise": cfg.env.add_sensor_noise,
                "random_start_waypoint": cfg.env.random_start_waypoint,
                "max_waypoints": cfg.env.max_waypoints,
                "action_scale": cfg.env.action_scale,
                "random_start_position": cfg.env.random_start_position,
                "start_position_noise": cfg.env.start_position_noise,
            },
            "network": {
                "policy": "MlpPolicy",
                "net_arch": {
                    "pi": cfg.ppo.net_arch.pi,
                    "vf": cfg.ppo.net_arch.vf,
                },
            },
            "reward": {
                "progress_multiplier": cfg.reward.progress_multiplier,
                "time_penalty": cfg.reward.time_penalty,
                "waypoint_bonus": cfg.reward.waypoint_bonus,
                "path_complete_bonus": cfg.reward.path_complete_bonus,
                "completion_time_divisor": cfg.reward.completion_time_divisor,
                "close_proximity_3x_bonus": cfg.reward.close_proximity_3x_bonus,
                "close_proximity_3x_radius": cfg.reward.close_proximity_3x_radius,
                "close_proximity_1_5x_bonus": cfg.reward.close_proximity_1_5x_bonus,
                "close_proximity_1_5x_radius": cfg.reward.close_proximity_1_5x_radius,
                "collision_penalty": cfg.reward.collision_penalty,
                "tilt_penalty": cfg.reward.tilt_penalty,
                "out_of_bounds_penalty": cfg.reward.out_of_bounds_penalty,
            },
        }

        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    @staticmethod
    def _git_commit() -> str | None:
        try:
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                check=True,
                capture_output=True,
                text=True,
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            return None
        return result.stdout.strip() or None

    def log_episode(self, row: dict[str, float | int | str | None]) -> None:
        self._episodes.append(row)
        self._episode_writer.writerow(row)
        self._episodes_file.flush()

    def log_update(self, row: dict[str, float | int]) -> None:
        self._updates.append(row)
        self._update_writer.writerow(row)
        self._updates_file.flush()

    def write_interim_summary(self, total_timesteps: int, total_episodes: int) -> None:
        summary = self._build_summary(total_timesteps, total_episodes)
        self._summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        self._append_experiment(self._build_experiments_row(summary, total_timesteps))

    def write_checkpoint_summary(self, total_timesteps: int) -> None:
        summary = self._build_summary(total_timesteps, len(self._episodes))
        self._summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        self._append_experiment(self._build_experiments_row(summary, total_timesteps))

    def finalize(self, total_timesteps: int, total_episodes: int) -> None:
        if not self._episodes_file.closed:
            self._episodes_file.close()
        if not self._updates_file.closed:
            self._updates_file.close()

        summary = self._build_summary(total_timesteps, total_episodes)
        self._summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        self._append_experiment(self._build_experiments_row(summary, total_timesteps))

    def _build_experiments_row(
        self, summary: dict[str, object], total_timesteps: int
    ) -> dict[str, float | int | str | None]:
        performance = summary.get("performance", {})
        if not isinstance(performance, dict):
            performance = {}
        success_metrics = summary.get("success_metrics", {})
        if not isinstance(success_metrics, dict):
            success_metrics = {}

        timestamp = summary.get("timestamp")
        if not isinstance(timestamp, str):
            timestamp = None

        success_rate_value = success_metrics.get("success_rate")
        success_rate = (
            float(success_rate_value)
            if isinstance(success_rate_value, (int, float))
            else None
        )
        mean_reward_value = performance.get("mean_reward_last_100")
        mean_reward = (
            float(mean_reward_value)
            if isinstance(mean_reward_value, (int, float))
            else None
        )
        best_reward_value = performance.get("best_reward")
        best_reward = (
            float(best_reward_value)
            if isinstance(best_reward_value, (int, float))
            else None
        )

        return {
            "run_id": self._run_id,
            "timestamp": timestamp,
            "total_timesteps": total_timesteps,
            "success_rate": success_rate,
            "mean_reward": mean_reward,
            "best_reward": best_reward,
            "notes": "",
        }

    def _append_experiment(self, row: dict[str, float | int | str | None]) -> None:
        file_exists = self._experiments_path.exists()
        with self._experiments_path.open("a", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=[
                    "run_id",
                    "timestamp",
                    "total_timesteps",
                    "success_rate",
                    "mean_reward",
                    "best_reward",
                    "notes",
                ],
            )
            if not file_exists:
                writer.writeheader()
            writer.writerow(row)

    def _build_summary(
        self, total_timesteps: int, total_episodes: int
    ) -> dict[str, object]:
        elapsed = time.time() - self._start_time
        episode_rewards: list[float] = []
        success_flags: list[bool] = []
        crash_types: list[str] = []
        waypoints: list[float] = []
        completion_steps: list[float] = []

        for row in self._episodes:
            reward = row.get("reward")
            if isinstance(reward, (int, float)):
                episode_rewards.append(float(reward))

            success = row.get("success")
            success_flags.append(bool(success))

            crash = row.get("crash_type")
            if crash:
                crash_types.append(str(crash))

            waypoint = row.get("waypoints_reached")
            if isinstance(waypoint, (int, float)):
                waypoints.append(float(waypoint))

            length = row.get("length")
            if success and isinstance(length, (int, float)):
                completion_steps.append(float(length))

        last_100_rewards = episode_rewards[-100:] if episode_rewards else []
        best_reward = max(episode_rewards) if episode_rewards else 0.0
        mean_reward_last = float(np.mean(last_100_rewards)) if last_100_rewards else 0.0
        success_rate = (
            float(sum(1 for s in success_flags if s)) / len(success_flags)
            if success_flags
            else 0.0
        )
        mean_waypoints = float(np.mean(waypoints)) if waypoints else 0.0
        mean_completion = float(np.mean(completion_steps)) if completion_steps else None
        crash_counts: dict[str, int] = {}
        for crash in crash_types:
            crash_counts[crash] = crash_counts.get(crash, 0) + 1

        update_metrics = {
            "policy_loss": None,
            "value_loss": None,
            "entropy": None,
            "kl_divergence": None,
            "clip_fraction": None,
            "explained_variance": None,
        }
        if self._updates:
            last_update = self._updates[-1]
            update_metrics = {
                "policy_loss": last_update.get("policy_loss"),
                "value_loss": last_update.get("value_loss"),
                "entropy": last_update.get("entropy"),
                "kl_divergence": last_update.get("kl_divergence"),
                "clip_fraction": last_update.get("clip_fraction"),
                "explained_variance": last_update.get("explained_variance"),
            }

        return {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "performance": {
                "best_reward": best_reward,
                "mean_reward_last_100": mean_reward_last,
                "total_episodes": total_episodes,
            },
            "success_metrics": {
                "success_rate": success_rate,
                "mean_waypoints_reached": mean_waypoints,
                "mean_completion_steps": mean_completion,
                "first_success_episode": self._first_success_episode(),
            },
            "failure_analysis": {
                "crash_rate": self._crash_rate(),
                "timeout_rate": self._timeout_rate(),
                "crash_type_breakdown": crash_counts,
            },
            "training_health": {
                "final_losses": update_metrics,
            },
            "wall_time_seconds": elapsed,
            "total_timesteps": total_timesteps,
            "total_episodes": total_episodes,
        }

    def _first_success_episode(self) -> int | None:
        for row in self._episodes:
            if row.get("success") and isinstance(row.get("episode"), (int, float)):
                episode_value = row.get("episode")
                if isinstance(episode_value, (int, float)):
                    return int(episode_value)
        return None

    def _crash_rate(self) -> float:
        if not self._episodes:
            return 0.0
        crashes = [row for row in self._episodes if row["crash_type"]]
        return float(len(crashes) / len(self._episodes))

    def _timeout_rate(self) -> float:
        if not self._episodes:
            return 0.0
        timeouts = [row for row in self._episodes if row["crash_type"] == "timeout"]
        return float(len(timeouts) / len(self._episodes))
