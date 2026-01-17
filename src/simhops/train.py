"""Training script using Stable-Baselines3 PPO."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path

import numpy as np

from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import (
    BaseCallback,
    CheckpointCallback,
    EvalCallback,
)
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import SubprocVecEnv, VecNormalize

from simhops.config import Config
from simhops.envs.quadcopter_env import QuadcopterEnv
from simhops.viz.rerun_viz import RerunVisualizer


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

    def finalize(self, total_timesteps: int, total_episodes: int) -> None:
        if not self._episodes_file.closed:
            self._episodes_file.close()
        if not self._updates_file.closed:
            self._updates_file.close()

        summary = self._build_summary(total_timesteps, total_episodes)
        self._summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

        performance = summary.get("performance", {})
        if not isinstance(performance, dict):
            performance = {}
        success_metrics = summary.get("success_metrics", {})
        if not isinstance(success_metrics, dict):
            success_metrics = {}

        timestamp = summary.get("timestamp")
        success_rate = success_metrics.get("success_rate")
        mean_reward = performance.get("mean_reward_last_100")
        best_reward = performance.get("best_reward")

        experiments_row = {
            "run_id": self._run_id,
            "timestamp": timestamp,
            "total_timesteps": total_timesteps,
            "success_rate": success_rate,
            "mean_reward": mean_reward,
            "best_reward": best_reward,
            "notes": "",
        }
        self._append_experiment(experiments_row)

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


class MetricsLoggerCallback(BaseCallback):
    """Callback that writes agent-friendly CSV/JSON logs."""

    def __init__(self, metrics_logger: MetricsLogger, verbose: int = 0) -> None:
        super().__init__(verbose)
        self._metrics_logger = metrics_logger
        self._episode_rewards: list[float] = []
        self._episode_count = 0
        self._update_count = 0
        self._finalized = False

    def _on_step(self) -> bool:
        for info in self.locals.get("infos", []):
            if "episode" not in info:
                continue
            self._episode_count += 1

            episode_info = info.get("episode", {})
            ep_reward_value = None
            ep_length_value = None
            if isinstance(episode_info, dict):
                ep_reward_value = episode_info.get("r")
                ep_length_value = episode_info.get("l")

            if isinstance(ep_reward_value, (int, float)):
                ep_reward = float(ep_reward_value)
            else:
                ep_reward = 0.0
            if isinstance(ep_length_value, (int, float)):
                ep_length = int(ep_length_value)
            else:
                ep_length = 0

            self._episode_rewards.append(ep_reward)

            mean_reward = (
                float(np.mean(self._episode_rewards[-100:]))
                if self._episode_rewards
                else 0.0
            )
            crash_type = info.get("crash")
            if info.get("time_limit_reached"):
                crash_type = "timeout"

            waypoint_idx = info.get("current_waypoint_idx")
            if isinstance(waypoint_idx, (int, float)):
                waypoints_reached = int(waypoint_idx)
            else:
                waypoints_reached = 0

            distance_value = info.get("distance")
            if isinstance(distance_value, (int, float)):
                final_distance = float(distance_value)
            else:
                final_distance = 0.0

            mean_speed_value = info.get("mean_speed")
            if isinstance(mean_speed_value, (int, float)):
                mean_speed = float(mean_speed_value)
            else:
                mean_speed = 0.0

            max_tilt_value = info.get("max_tilt_deg")
            if isinstance(max_tilt_value, (int, float)):
                max_tilt_deg = float(max_tilt_value)
            else:
                max_tilt_deg = 0.0

            row = {
                "episode": self._episode_count,
                "timestep": int(self.num_timesteps),
                "reward": ep_reward,
                "length": ep_length,
                "waypoints_reached": waypoints_reached,
                "success": bool(info.get("success", False)),
                "crash_type": crash_type,
                "final_distance": final_distance,
                "mean_speed": mean_speed,
                "max_tilt_deg": max_tilt_deg,
                "time_to_first_wp": info.get("time_to_first_wp"),
            }
            self._metrics_logger.log_episode(row)

        return True

    def _on_rollout_end(self) -> None:
        if self.logger is None:
            return

        name_to_value = getattr(self.logger, "name_to_value", {})
        self._update_count += 1
        mean_reward = (
            float(np.mean(self._episode_rewards[-100:]))
            if self._episode_rewards
            else 0.0
        )
        learning_rate = (
            self.model.learning_rate
            if isinstance(self.model.learning_rate, float)
            else None
        )
        row = {
            "update": self._update_count,
            "timestep": int(self.num_timesteps),
            "policy_loss": name_to_value.get("train/policy_gradient_loss"),
            "value_loss": name_to_value.get("train/value_loss"),
            "entropy": name_to_value.get("train/entropy_loss"),
            "kl_divergence": name_to_value.get("train/approx_kl"),
            "clip_fraction": name_to_value.get("train/clip_fraction"),
            "explained_variance": name_to_value.get("train/explained_variance"),
            "learning_rate": learning_rate,
            "mean_episode_reward": mean_reward,
        }
        self._metrics_logger.log_update(row)

    def _on_training_end(self) -> None:
        self.finalize()

    def finalize(self) -> None:
        if self._finalized:
            return
        self._metrics_logger.finalize(self.num_timesteps, self._episode_count)
        self._finalized = True


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


class RewardLoggerCallback(BaseCallback):
    """Callback for logging episode rewards (console only, no Rerun)."""

    def __init__(self, verbose: int = 0) -> None:
        super().__init__(verbose)
        self._episode_rewards: list[float] = []
        self._episode_lengths: list[int] = []
        self._waypoints_reached: list[int] = []

    def _on_step(self) -> bool:
        for info in self.locals.get("infos", []):
            if "episode" in info:
                self._episode_rewards.append(info["episode"]["r"])
                self._episode_lengths.append(info["episode"]["l"])

                # Track waypoints reached
                wp_idx = info.get("current_waypoint_idx", 0)
                self._waypoints_reached.append(wp_idx)

                if len(self._episode_rewards) % 10 == 0:
                    mean_reward = np.mean(self._episode_rewards[-100:])
                    mean_length = np.mean(self._episode_lengths[-100:])
                    mean_waypoints = np.mean(self._waypoints_reached[-100:])
                    print(
                        f"Episodes: {len(self._episode_rewards)}, "
                        f"Mean reward: {mean_reward:.2f}, "
                        f"Mean length: {mean_length:.0f}, "
                        f"Mean waypoints: {mean_waypoints:.1f}/10"
                    )

        return True


def train() -> None:
    """Train PPO agent on 10-waypoint path with randomization."""
    cfg = Config.schema()
    output_path = Path(cfg.training.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now()
    run_path = output_path / f"run_{timestamp:%Y%m%d_%H%M%S}"
    run_path.mkdir(parents=True, exist_ok=True)
    Config.dump_yaml(run_path / "config.yaml")

    print(f"Creating {cfg.training.n_envs} parallel environments...")
    print(
        f"Training on 10-waypoint path with +/-{cfg.env.waypoint_noise}m randomization"
    )

    # Create vectorized environment
    env = make_vec_env(
        lambda: QuadcopterEnv(
            render_mode=None,
            add_sensor_noise=cfg.env.add_sensor_noise,
            include_position=cfg.env.include_position,
            waypoint_noise=cfg.env.waypoint_noise,
        ),
        n_envs=cfg.training.n_envs,
        seed=cfg.training.seed,
        vec_env_cls=SubprocVecEnv,
    )

    # Normalize rewards only (observations are already normalized in env)
    env = VecNormalize(
        env,
        norm_obs=cfg.vecnormalize.norm_obs,
        norm_reward=cfg.vecnormalize.norm_reward,
        clip_obs=cfg.vecnormalize.clip_obs,
        clip_reward=cfg.vecnormalize.clip_reward,
        gamma=cfg.ppo.gamma,
    )

    # Create evaluation environment (no noise for consistent eval)
    eval_env_cfg = cfg.evaluation.env
    eval_env = make_vec_env(
        lambda: QuadcopterEnv(
            render_mode=None,
            add_sensor_noise=eval_env_cfg.add_sensor_noise,
            include_position=eval_env_cfg.include_position,
            waypoint_noise=eval_env_cfg.waypoint_noise,
            disable_tilt_termination=eval_env_cfg.disable_tilt_termination,
        ),
        n_envs=1,
        seed=cfg.training.seed + 1000,
    )
    eval_env = VecNormalize(
        eval_env,
        norm_obs=cfg.vecnormalize.norm_obs,
        norm_reward=cfg.vecnormalize.eval_norm_reward,
        clip_obs=cfg.vecnormalize.clip_obs,
        training=False,
    )

    # Callbacks
    checkpoint_callback = CheckpointCallback(
        save_freq=cfg.callbacks.checkpoint_freq // cfg.training.n_envs,
        save_path=str(run_path / "checkpoints"),
        name_prefix="ppo_quadcopter",
        save_vecnormalize=True,
    )

    eval_callback = EvalCallback(
        eval_env,
        best_model_save_path=str(run_path / "best_model"),
        log_path=str(run_path / "eval_logs"),
        eval_freq=cfg.callbacks.eval_freq // cfg.training.n_envs,
        n_eval_episodes=cfg.callbacks.n_eval_episodes,
        deterministic=True,
    )

    metrics_logger = MetricsLogger(run_path)
    metrics_callback = MetricsLoggerCallback(metrics_logger)

    callbacks: list[BaseCallback] = [
        checkpoint_callback,
        eval_callback,
        metrics_callback,
    ]

    if cfg.training.use_rerun:
        print("Initializing Rerun visualizer for training metrics...")
        viz = RerunVisualizer(
            app_id=cfg.visualization.training_app_id, spawn=cfg.visualization.spawn
        )
        viz.init()
        rerun_callback = RerunTrainingCallback(
            viz, log_3d_freq=cfg.callbacks.log_3d_freq
        )
        callbacks.append(rerun_callback)
    else:
        callbacks.append(RewardLoggerCallback())

    # Create or load model
    if cfg.training.resume_from:
        print(f"Resuming from {cfg.training.resume_from}")
        model = PPO.load(cfg.training.resume_from, env=env)
    else:
        print("Creating new PPO model...")
        model = PPO(
            "MlpPolicy",
            env,
            learning_rate=cfg.ppo.learning_rate,
            n_steps=cfg.ppo.n_steps,
            batch_size=cfg.ppo.batch_size,
            n_epochs=cfg.ppo.n_epochs,
            gamma=cfg.ppo.gamma,
            gae_lambda=cfg.ppo.gae_lambda,
            clip_range=cfg.ppo.clip_range,
            ent_coef=cfg.ppo.ent_coef,
            vf_coef=cfg.ppo.vf_coef,
            max_grad_norm=cfg.ppo.max_grad_norm,
            verbose=1,
            tensorboard_log=str(run_path / "tensorboard"),
            seed=cfg.training.seed,
            policy_kwargs={
                "net_arch": {
                    "pi": cfg.ppo.net_arch.pi,
                    "vf": cfg.ppo.net_arch.vf,
                },
            },
        )

    print(f"Starting training for {cfg.training.total_timesteps} timesteps...")

    try:
        model.learn(
            total_timesteps=cfg.training.total_timesteps,
            callback=callbacks,
            progress_bar=True,
        )
    except KeyboardInterrupt:
        print("\nTraining interrupted by user.")
    finally:
        metrics_callback.finalize()

    # Save final model
    final_model_path = run_path / "final_model"
    model.save(str(final_model_path / "ppo_quadcopter"))
    env.save(str(final_model_path / "vec_normalize.pkl"))

    print(f"Model saved to {final_model_path}")

    env.close()
    eval_env.close()


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Train quadcopter RL agent")
    parser.add_argument(
        "--config",
        type=str,
        default="cfg_default.yaml",
        help="Path to YAML config file",
    )

    args = parser.parse_args()
    Config.load(args.config)
    train()


if __name__ == "__main__":
    main()
