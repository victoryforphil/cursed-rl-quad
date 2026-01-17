"""Training script using Stable-Baselines3 PPO."""

from __future__ import annotations

import argparse
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


def train(
    output_dir: str = "models",
    total_timesteps: int = 1_000_000,
    n_envs: int = 8,
    seed: int = 42,
    learning_rate: float = 3e-4,
    batch_size: int = 256,
    n_epochs: int = 10,
    gamma: float = 0.99,
    gae_lambda: float = 0.95,
    clip_range: float = 0.2,
    ent_coef: float = 0.01,
    waypoint_noise: float = 1.0,
    resume_from: str | None = None,
    use_rerun: bool = False,
) -> None:
    """Train PPO agent on 10-waypoint path with randomization.

    Args:
        output_dir: Directory to save models and logs
        total_timesteps: Total training timesteps
        n_envs: Number of parallel environments
        seed: Random seed
        learning_rate: Learning rate
        batch_size: Minibatch size
        n_epochs: Number of epochs per update
        gamma: Discount factor
        gae_lambda: GAE lambda
        clip_range: PPO clip range
        ent_coef: Entropy coefficient
        waypoint_noise: +/- meters of waypoint randomization per reset
        resume_from: Path to checkpoint to resume from
        use_rerun: Enable Rerun visualization for training metrics
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    print(f"Creating {n_envs} parallel environments...")
    print(f"Training on 10-waypoint path with +/-{waypoint_noise}m randomization")

    # Create vectorized environment
    env = make_vec_env(
        lambda: QuadcopterEnv(
            render_mode=None,
            add_sensor_noise=True,
            include_position=False,
            waypoint_noise=waypoint_noise,
        ),
        n_envs=n_envs,
        seed=seed,
        vec_env_cls=SubprocVecEnv,
    )

    # Normalize rewards only (observations are already normalized in env)
    env = VecNormalize(
        env,
        norm_obs=False,
        norm_reward=True,
        clip_obs=10.0,
        clip_reward=10.0,
        gamma=gamma,
    )

    # Create evaluation environment (no noise for consistent eval)
    eval_env = make_vec_env(
        lambda: QuadcopterEnv(
            render_mode=None,
            add_sensor_noise=True,
            include_position=False,
            waypoint_noise=0.0,  # No randomization for evaluation
        ),
        n_envs=1,
        seed=seed + 1000,
    )
    eval_env = VecNormalize(
        eval_env,
        norm_obs=False,
        norm_reward=False,
        clip_obs=10.0,
        training=False,
    )

    # Callbacks
    checkpoint_callback = CheckpointCallback(
        save_freq=50_000 // n_envs,
        save_path=str(output_path / "checkpoints"),
        name_prefix="ppo_quadcopter",
        save_vecnormalize=True,
    )

    eval_callback = EvalCallback(
        eval_env,
        best_model_save_path=str(output_path / "best_model"),
        log_path=str(output_path / "eval_logs"),
        eval_freq=10_000 // n_envs,
        n_eval_episodes=5,
        deterministic=True,
    )

    callbacks: list[BaseCallback] = [checkpoint_callback, eval_callback]

    if use_rerun:
        print("Initializing Rerun visualizer for training metrics...")
        viz = RerunVisualizer(app_id="simhops-training", spawn=True)
        viz.init()
        rerun_callback = RerunTrainingCallback(viz)
        callbacks.append(rerun_callback)
    else:
        callbacks.append(RewardLoggerCallback())

    # Create or load model
    if resume_from:
        print(f"Resuming from {resume_from}")
        model = PPO.load(resume_from, env=env)
    else:
        print("Creating new PPO model...")
        model = PPO(
            "MlpPolicy",
            env,
            learning_rate=learning_rate,
            n_steps=2048,
            batch_size=batch_size,
            n_epochs=n_epochs,
            gamma=gamma,
            gae_lambda=gae_lambda,
            clip_range=clip_range,
            ent_coef=ent_coef,
            vf_coef=0.5,
            max_grad_norm=0.5,
            verbose=1,
            tensorboard_log=str(output_path / "tensorboard"),
            seed=seed,
            policy_kwargs={
                "net_arch": {"pi": [256, 256], "vf": [256, 256]},
            },
        )

    print(f"Starting training for {total_timesteps} timesteps...")

    try:
        model.learn(
            total_timesteps=total_timesteps,
            callback=callbacks,
            progress_bar=True,
        )
    except KeyboardInterrupt:
        print("\nTraining interrupted by user.")

    # Save final model
    final_model_path = output_path / "final_model"
    model.save(str(final_model_path / "ppo_quadcopter"))
    env.save(str(final_model_path / "vec_normalize.pkl"))

    print(f"Model saved to {final_model_path}")

    env.close()
    eval_env.close()


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Train quadcopter RL agent")
    parser.add_argument(
        "--output-dir", type=str, default="models", help="Output directory"
    )
    parser.add_argument(
        "--timesteps", type=int, default=1_000_000, help="Total training timesteps"
    )
    parser.add_argument(
        "--n-envs", type=int, default=8, help="Number of parallel environments"
    )
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--lr", type=float, default=3e-4, help="Learning rate")
    parser.add_argument("--batch-size", type=int, default=256, help="Batch size")
    parser.add_argument(
        "--waypoint-noise",
        type=float,
        default=1.0,
        help="Waypoint randomization in meters (+/-)",
    )
    parser.add_argument(
        "--resume", type=str, default=None, help="Path to checkpoint to resume"
    )
    parser.add_argument(
        "--rerun",
        action="store_true",
        help="Enable Rerun visualization for training metrics",
    )

    args = parser.parse_args()

    train(
        output_dir=args.output_dir,
        total_timesteps=args.timesteps,
        n_envs=args.n_envs,
        seed=args.seed,
        learning_rate=args.lr,
        batch_size=args.batch_size,
        waypoint_noise=args.waypoint_noise,
        resume_from=args.resume,
        use_rerun=args.rerun,
    )


if __name__ == "__main__":
    main()
