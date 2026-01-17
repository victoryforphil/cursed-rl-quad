"""Training script using Stable-Baselines3 PPO."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import BaseCallback, CheckpointCallback, EvalCallback
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import SubprocVecEnv, VecNormalize

from simhops.config import Config
from simhops.config.schema import CurriculumStageConfig, EnvConfig
from simhops.envs.quadcopter_env import QuadcopterEnv
from simhops.train.callbacks import (
    ExperimentSnapshotCallback,
    MetricsLoggerCallback,
    RewardLoggerCallback,
    RerunTrainingCallback,
)
from simhops.train.metrics import MetricsLogger
from simhops.viz.rerun_viz import RerunVisualizer


def _apply_stage_env(cfg: EnvConfig, stage: CurriculumStageConfig | None) -> EnvConfig:
    env_cfg = cfg
    if stage is None:
        return env_cfg

    return EnvConfig(
        waypoint_radius=env_cfg.waypoint_radius,
        waypoint_noise=stage.waypoint_noise
        if stage.waypoint_noise is not None
        else env_cfg.waypoint_noise,
        waypoint_yaw_random=env_cfg.waypoint_yaw_random,
        max_episode_steps=stage.max_episode_steps
        if stage.max_episode_steps is not None
        else env_cfg.max_episode_steps,
        arena_size=env_cfg.arena_size,
        max_altitude=env_cfg.max_altitude,
        max_tilt_angle=env_cfg.max_tilt_angle,
        disable_tilt_termination=env_cfg.disable_tilt_termination,
        goal_max_distance=env_cfg.goal_max_distance,
        include_position=env_cfg.include_position,
        random_start_waypoint=stage.random_start_waypoint
        if stage.random_start_waypoint is not None
        else env_cfg.random_start_waypoint,
        add_sensor_noise=stage.add_sensor_noise
        if stage.add_sensor_noise is not None
        else env_cfg.add_sensor_noise,
        max_waypoints=stage.max_waypoints
        if stage.max_waypoints is not None
        else env_cfg.max_waypoints,
        action_scale=stage.action_scale
        if stage.action_scale is not None
        else env_cfg.action_scale,
        random_start_position=stage.random_start_position
        if stage.random_start_position is not None
        else env_cfg.random_start_position,
        start_position_noise=stage.start_position_noise
        if stage.start_position_noise is not None
        else env_cfg.start_position_noise,
        speed_normalization=env_cfg.speed_normalization,
        bounds_margin=env_cfg.bounds_margin,
        ground_threshold=env_cfg.ground_threshold,
        timestep=env_cfg.timestep,
    )


def train() -> None:
    """Train PPO agent on 10-waypoint path with optional curriculum."""
    cfg = Config.schema()
    output_path = Path(cfg.training.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now()
    run_path = output_path / f"run_{timestamp:%Y%m%d_%H%M%S}"
    run_path.mkdir(parents=True, exist_ok=True)
    Config.dump_yaml(run_path / "config.yaml")

    stages = cfg.curriculum.stages if cfg.curriculum.enabled else []
    if not stages:
        stages = [None]

    metrics_logger = MetricsLogger(run_path)
    metrics_callback = MetricsLoggerCallback(
        metrics_logger,
        summary_update_freq=cfg.callbacks.summary_update_freq,
        finalize_on_end=False,
    )

    model: PPO | None = None

    for stage_index, stage in enumerate(stages, start=1):
        stage_env_cfg = _apply_stage_env(cfg.env, stage)
        stage_label = stage.name if stage is not None else "default"
        stage_timesteps = (
            stage.total_timesteps if stage is not None else cfg.training.total_timesteps
        )

        print(
            f"Starting stage {stage_index}/{len(stages)}: {stage_label} ({stage_timesteps} timesteps)"
        )
        print(
            "Env: noise={:.2f}, yaw_random={}, sensor_noise={}, random_start={}, max_waypoints={}, action_scale={}, start_pos_random={}, start_pos_noise={}".format(
                stage_env_cfg.waypoint_noise,
                stage_env_cfg.waypoint_yaw_random,
                stage_env_cfg.add_sensor_noise,
                stage_env_cfg.random_start_waypoint,
                stage_env_cfg.max_waypoints,
                stage_env_cfg.action_scale,
                stage_env_cfg.random_start_position,
                stage_env_cfg.start_position_noise,
            )
        )

        env = make_vec_env(
            lambda: QuadcopterEnv(
                render_mode=None,
                add_sensor_noise=stage_env_cfg.add_sensor_noise,
                include_position=stage_env_cfg.include_position,
                waypoint_noise=stage_env_cfg.waypoint_noise,
                waypoint_yaw_random=stage_env_cfg.waypoint_yaw_random,
                random_start_waypoint=stage_env_cfg.random_start_waypoint,
                max_waypoints=stage_env_cfg.max_waypoints,
                max_episode_steps=stage_env_cfg.max_episode_steps,
                action_scale=stage_env_cfg.action_scale,
                random_start_position=stage_env_cfg.random_start_position,
                start_position_noise=stage_env_cfg.start_position_noise,
            ),
            n_envs=cfg.training.n_envs,
            seed=cfg.training.seed,
            vec_env_cls=SubprocVecEnv,
        )

        env = VecNormalize(
            env,
            norm_obs=cfg.vecnormalize.norm_obs,
            norm_reward=cfg.vecnormalize.norm_reward,
            clip_obs=cfg.vecnormalize.clip_obs,
            clip_reward=cfg.vecnormalize.clip_reward,
            gamma=cfg.ppo.gamma,
        )

        eval_env_cfg = cfg.evaluation.env
        eval_env = make_vec_env(
            lambda: QuadcopterEnv(
                render_mode=None,
                add_sensor_noise=eval_env_cfg.add_sensor_noise,
                include_position=eval_env_cfg.include_position,
                waypoint_noise=eval_env_cfg.waypoint_noise,
                waypoint_yaw_random=eval_env_cfg.waypoint_yaw_random,
                disable_tilt_termination=eval_env_cfg.disable_tilt_termination,
                random_start_waypoint=stage_env_cfg.random_start_waypoint,
                max_waypoints=stage_env_cfg.max_waypoints,
                max_episode_steps=stage_env_cfg.max_episode_steps,
                action_scale=stage_env_cfg.action_scale,
                random_start_position=stage_env_cfg.random_start_position,
                start_position_noise=stage_env_cfg.start_position_noise,
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

        checkpoint_path = run_path / "checkpoints" / f"stage_{stage_index}"
        checkpoint_path.mkdir(parents=True, exist_ok=True)
        checkpoint_callback = CheckpointCallback(
            save_freq=cfg.callbacks.checkpoint_freq // cfg.training.n_envs,
            save_path=str(checkpoint_path),
            name_prefix=f"ppo_quadcopter_stage_{stage_index}",
            save_vecnormalize=True,
        )

        experiment_snapshot = ExperimentSnapshotCallback(
            metrics_logger,
            snapshot_freq=cfg.callbacks.checkpoint_freq // cfg.training.n_envs,
        )

        eval_callback = EvalCallback(
            eval_env,
            best_model_save_path=str(run_path / "best_model"),
            log_path=str(run_path / "eval_logs"),
            eval_freq=cfg.callbacks.eval_freq // cfg.training.n_envs,
            n_eval_episodes=cfg.callbacks.n_eval_episodes,
            deterministic=True,
        )

        callbacks: list[BaseCallback] = [
            checkpoint_callback,
            eval_callback,
            metrics_callback,
            experiment_snapshot,
        ]

        if cfg.training.use_rerun:
            print("Initializing Rerun visualizer for training metrics...")
            session_markdown = "\n".join(
                [
                    "# SimHops Training Session",
                    f"- stage: {stage_label} ({stage_index}/{len(stages)})",
                    f"- timesteps: {stage_timesteps}",
                    f"- config: {Config.path() or 'cfg_default.yaml'}",
                    "",
                    "## Environment",
                    f"- waypoint_noise: {stage_env_cfg.waypoint_noise}",
                    f"- waypoint_yaw_random: {stage_env_cfg.waypoint_yaw_random}",
                    f"- waypoint_radius: {stage_env_cfg.waypoint_radius}",
                    f"- max_waypoints: {stage_env_cfg.max_waypoints}",
                    f"- random_start_waypoint: {stage_env_cfg.random_start_waypoint}",
                    f"- random_start_position: {stage_env_cfg.random_start_position}",
                    f"- start_position_noise: {stage_env_cfg.start_position_noise}",
                    f"- action_scale: {stage_env_cfg.action_scale}",
                    f"- max_episode_steps: {stage_env_cfg.max_episode_steps}",
                    "",
                    "## PPO",
                    f"- learning_rate: {cfg.ppo.learning_rate}",
                    f"- n_steps: {cfg.ppo.n_steps}",
                    f"- batch_size: {cfg.ppo.batch_size}",
                    f"- n_epochs: {cfg.ppo.n_epochs}",
                ]
            )
            recording_name = f"{cfg.visualization.training_app_id}:{stage_label}"
            viz = RerunVisualizer(
                app_id=cfg.visualization.training_app_id,
                spawn=cfg.visualization.spawn,
                recording_name=recording_name,
                session_markdown=session_markdown,
            )
            viz.init()
            rerun_callback = RerunTrainingCallback(
                viz, log_3d_freq=cfg.callbacks.log_3d_freq
            )
            callbacks.append(rerun_callback)
        else:
            callbacks.append(RewardLoggerCallback())

        if model is None:
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
        else:
            model.set_env(env)

        print(f"Starting training for {stage_timesteps} timesteps...")

        try:
            model.learn(
                total_timesteps=stage_timesteps,
                callback=callbacks,
                progress_bar=True,
                reset_num_timesteps=False,
            )
        except KeyboardInterrupt:
            print("\nTraining interrupted by user.")
            break
        finally:
            env.close()
            eval_env.close()

    metrics_callback.finalize()

    if model is None:
        print("Training did not start; no model created.")
        return

    final_model_path = run_path / "final_model"
    model.save(str(final_model_path / "ppo_quadcopter"))
    env_save_path = final_model_path / "vec_normalize.pkl"
    vec_env = model.get_env()
    if isinstance(vec_env, VecNormalize):
        vec_env.save(str(env_save_path))

    print(f"Model saved to {final_model_path}")


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
