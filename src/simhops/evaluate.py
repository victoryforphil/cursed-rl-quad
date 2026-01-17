"""Simple evaluation script with Rerun visualization.

Runs a single episode and logs drone position, rotation, and goal waypoint to Rerun.
"""

from __future__ import annotations

import argparse
import csv
import time
from pathlib import Path

import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import VecNormalize

from simhops.config import Config
from simhops.envs.quadcopter_env import QuadcopterEnv
from simhops.viz.rerun_viz import RerunVisualizer


def evaluate(
    model_path: str,
    eval_output: Path | None = None,
    episodes: int = 1,
) -> None:
    """Evaluate trained model with Rerun visualization.

    Runs a single episode on the fixed 10-waypoint path.
    Logs: drone position, drone rotation, current goal waypoint.

    Args:
        model_path: Path to saved model directory
        realtime: Sleep between steps to match real-time
        slow_motion: Slow motion factor (1.0 = realtime)
        disable_tilt_termination: If True, don't terminate on excessive tilt
    """
    cfg = Config.schema()
    eval_cfg = cfg.evaluation
    model_dir = Path(model_path)

    # Find model file
    model_file = None
    for candidate in [
        model_dir / "ppo_quadcopter.zip",
        model_dir / "ppo_quadcopter",
        model_dir / "best_model.zip",
        model_dir,
    ]:
        if candidate.exists() or Path(str(candidate) + ".zip").exists():
            model_file = candidate
            break

    if model_file is None:
        raise FileNotFoundError(f"Could not find model in {model_path}")

    print(f"Loading model from {model_file}")
    model = PPO.load(str(model_file))

    # Create environment (no waypoint noise for consistent evaluation)
    env_cfg = eval_cfg.env
    env = QuadcopterEnv(
        render_mode=None,
        add_sensor_noise=env_cfg.add_sensor_noise,
        disable_tilt_termination=env_cfg.disable_tilt_termination,
        include_position=env_cfg.include_position,
        waypoint_noise=env_cfg.waypoint_noise,
    )
    print(f"Environment: {env.num_waypoints} waypoints (no randomization)")
    if env_cfg.disable_tilt_termination:
        print("Tilt termination disabled for evaluation")

    # Load normalization stats if available
    vec_normalize_path = model_dir / "vec_normalize.pkl"
    obs_rms = None
    if vec_normalize_path.exists():
        print(f"Loading normalization stats from {vec_normalize_path}")
        import pickle

        with open(vec_normalize_path, "rb") as f:
            vec_normalize = pickle.load(f)
            try:
                if isinstance(vec_normalize, VecNormalize):
                    obs_rms = vec_normalize.obs_rms
                elif hasattr(vec_normalize, "mean") and hasattr(vec_normalize, "var"):
                    obs_rms = vec_normalize
            except (AttributeError, RecursionError) as error:
                print(f"Warning: Could not load obs_rms: {error}")

    # Initialize Rerun visualizer
    viz = RerunVisualizer(
        app_id=cfg.visualization.eval_app_id, spawn=cfg.visualization.spawn
    )
    viz.init()

    eval_writer = None
    eval_file = None
    if eval_output is not None:
        eval_output.parent.mkdir(parents=True, exist_ok=True)
        eval_file = eval_output.open("w", newline="", encoding="utf-8")
        eval_writer = csv.DictWriter(
            eval_file,
            fieldnames=[
                "eval_run",
                "model_path",
                "episode",
                "reward",
                "length",
                "waypoints_reached",
                "success",
                "crash_type",
                "completion_time_s",
            ],
        )
        eval_writer.writeheader()

    for episode_idx in range(1, episodes + 1):
        print("\n--- Running evaluation episode ---")
        obs, info = env.reset()
        viz.reset()

        viz.log_waypoints(
            info["waypoints"],
            info["current_waypoint_idx"],
            radius=env.waypoint_radius,
        )

        done = False
        total_reward = 0.0
        step = 0

        while not done:
            if (
                obs_rms is not None
                and hasattr(obs_rms, "mean")
                and hasattr(obs_rms, "var")
            ):
                obs_mean = getattr(obs_rms, "mean")
                obs_var = getattr(obs_rms, "var")
                obs_normalized = (obs - obs_mean) / np.sqrt(obs_var + 1e-8)
                obs_normalized = np.clip(obs_normalized, -10.0, 10.0)
            else:
                obs_normalized = obs

            action, _ = model.predict(obs_normalized, deterministic=True)

            obs, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated
            total_reward += float(reward)
            step += 1

            if env._quad is not None:
                state = env._quad.get_state()
                current_waypoint_idx = info["current_waypoint_idx"]

                wp_idx = min(current_waypoint_idx, env.num_waypoints - 1)

                viz.log_drone_position(
                    step,
                    position=state.position,
                    velocity=state.velocity,
                    orientation=state.orientation,
                )

                viz.log_waypoints_training(
                    step,
                    env._waypoints,
                    current_waypoint_idx,
                )

                viz.log_training_metrics(
                    step,
                    episode_reward=float(reward),
                )

                viz.log_actions(step, action)

            if eval_cfg.realtime:
                time.sleep(env.dt * eval_cfg.slow_motion)

            if step % 100 == 0:
                print(
                    f"  Step {step}: waypoint={info['current_waypoint_idx']}/{env.num_waypoints}, "
                    f"dist={info['distance']:.2f}m, speed={info['speed']:.2f}m/s"
                )

        success = info.get("success", False)
        crash = info.get("crash", None)

        print(f"\n=== Episode Results ===")
        print(f"Steps: {step}")
        print(f"Total reward: {total_reward:.1f}")
        print(f"Waypoints reached: {info['current_waypoint_idx']}/{env.num_waypoints}")

        completion_steps = None
        if success:
            completion_steps = info.get("completion_steps", step)
            print(
                f"SUCCESS! Completed in {completion_steps} steps ({completion_steps * env.dt:.1f}s)"
            )
        elif crash:
            print(f"CRASH: {crash}")
        else:
            print("TIMEOUT: Did not complete all waypoints")

        if eval_writer is not None:
            eval_writer.writerow(
                {
                    "eval_run": episode_idx,
                    "model_path": str(model_dir),
                    "episode": episode_idx,
                    "reward": total_reward,
                    "length": step,
                    "waypoints_reached": info.get("current_waypoint_idx", 0),
                    "success": bool(success),
                    "crash_type": crash,
                    "completion_time_s": completion_steps * env.dt
                    if completion_steps is not None
                    else None,
                }
            )

    if eval_file is not None:
        eval_file.close()

    env.close()


def demo_random() -> None:
    """Run demo with random actions for testing."""
    cfg = Config.schema()
    demo_cfg = cfg.demo
    env_cfg = demo_cfg.env
    print("Running demo with random actions...")

    env = QuadcopterEnv(
        render_mode=None,
        add_sensor_noise=env_cfg.add_sensor_noise,
        disable_tilt_termination=env_cfg.disable_tilt_termination,
        include_position=env_cfg.include_position,
        waypoint_noise=env_cfg.waypoint_noise,
    )

    viz = RerunVisualizer(
        app_id=cfg.visualization.demo_app_id, spawn=cfg.visualization.spawn
    )
    viz.init()

    obs, info = env.reset()
    viz.reset()
    viz.log_waypoints(info["waypoints"], 0, radius=env.waypoint_radius)

    done = False
    total_reward = 0.0
    step = 0

    while not done and step < demo_cfg.max_steps:
        # Random action with slight upward bias
        action = np.random.uniform(-0.3, 0.3, size=4).astype(np.float64)
        action[0] = np.random.uniform(-0.1, 0.3)

        obs, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        total_reward += float(reward)
        step += 1

        if env._quad is not None:
            state = env._quad.get_state()
            viz.log_drone_position(
                step,
                position=state.position,
                velocity=state.velocity,
                orientation=state.orientation,
            )
            viz.log_waypoints_training(
                step, env._waypoints, info["current_waypoint_idx"]
            )
            viz.log_actions(step, action)

        if step % 50 == 0 and env._quad is not None:
            state = env._quad.get_state()
            print(f"  Step {step}: pos={state.position}, dist={info['distance']:.2f}m")

        time.sleep(demo_cfg.sleep_time)

    print(f"\nDone: steps={step}, reward={total_reward:.1f}")
    env.close()


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Evaluate quadcopter agent")
    parser.add_argument(
        "--config",
        type=str,
        default="cfg_default.yaml",
        help="Path to YAML config file",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Evaluate subcommand
    eval_parser = subparsers.add_parser("eval", help="Evaluate trained model")
    eval_parser.add_argument("model_path", type=str, help="Path to model directory")
    eval_parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Optional CSV path for eval_results",
    )
    eval_parser.add_argument(
        "--episodes",
        type=int,
        default=1,
        help="Number of evaluation episodes",
    )

    # Demo subcommand
    subparsers.add_parser("demo", help="Run random action demo")

    args = parser.parse_args()

    Config.load(args.config)

    if args.command == "eval":
        output_path = Path(args.output) if args.output else None
        evaluate(
            model_path=args.model_path,
            eval_output=output_path,
            episodes=args.episodes,
        )
    elif args.command == "demo":
        demo_random()


if __name__ == "__main__":
    main()
