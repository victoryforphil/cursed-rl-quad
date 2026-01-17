"""Training script using Stable-Baselines3 PPO."""

from __future__ import annotations

import argparse
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

    callbacks: list[BaseCallback] = [checkpoint_callback, eval_callback]

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
