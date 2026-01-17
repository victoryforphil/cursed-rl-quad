"""Simple evaluation script with Rerun visualization.

Runs a single episode and logs drone position, rotation, and goal waypoint to Rerun.
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import VecNormalize

from simhops.envs.quadcopter_env import QuadcopterEnv
from simhops.viz.rerun_viz import RerunVisualizer


def evaluate(
    model_path: str,
    realtime: bool = True,
    slow_motion: float = 1.0,
    disable_tilt_termination: bool = True,  # Don't crash on tilt during eval
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
    env = QuadcopterEnv(
        render_mode=None,
        add_sensor_noise=True,
        disable_tilt_termination=disable_tilt_termination,
        include_position=False,
        waypoint_noise=0.0,
    )
    print(f"Environment: {env.num_waypoints} waypoints (no randomization)")
    if disable_tilt_termination:
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
            except (AttributeError, RecursionError) as e:
                print(f"Warning: Could not load obs_rms: {e}")

    # Initialize Rerun visualizer
    viz = RerunVisualizer(app_id="simhops-eval", spawn=True)
    viz.init()

    # Run single episode
    print("\n--- Running evaluation episode ---")
    obs, info = env.reset()
    viz.reset()

    # Log the fixed waypoints
    viz.log_waypoints(
        info["waypoints"],
        info["current_waypoint_idx"],
        radius=env.waypoint_radius,
    )

    done = False
    total_reward = 0.0
    step = 0

    while not done:
        # Normalize observation if we have stats
        if obs_rms is not None and hasattr(obs_rms, "mean") and hasattr(obs_rms, "var"):
            obs_normalized = (obs - obs_rms.mean) / np.sqrt(obs_rms.var + 1e-8)
            obs_normalized = np.clip(obs_normalized, -10.0, 10.0)
        else:
            obs_normalized = obs

        # Get action (deterministic)
        action, _ = model.predict(obs_normalized, deterministic=True)

        # Step environment
        obs, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        total_reward += float(reward)
        step += 1

        # Get quadcopter state for visualization
        if env._quad is not None:
            state = env._quad.get_state()
            current_waypoint_idx = info["current_waypoint_idx"]

            # Clamp to valid index for logging
            wp_idx = min(current_waypoint_idx, env.num_waypoints - 1)
            current_waypoint = env._waypoints[wp_idx]

            # Log drone state
            viz.log_drone_position(
                step,
                position=state.position,
                velocity=state.velocity,
                orientation=state.orientation,
            )

            # Log current goal waypoint and drone info as text
            viz.log_waypoints_training(
                step,
                env._waypoints,
                current_waypoint_idx,
            )

            # Log metrics
            viz.log_training_metrics(
                step,
                episode_reward=float(reward),
            )

            viz.log_actions(step, action)

        # Real-time visualization
        if realtime:
            time.sleep(env.dt * slow_motion)

        # Print progress every 100 steps
        if step % 100 == 0:
            print(
                f"  Step {step}: waypoint={info['current_waypoint_idx']}/{env.num_waypoints}, "
                f"dist={info['distance']:.2f}m, speed={info['speed']:.2f}m/s"
            )

    # Episode complete
    success = info.get("success", False)
    crash = info.get("crash", None)

    print(f"\n=== Episode Results ===")
    print(f"Steps: {step}")
    print(f"Total reward: {total_reward:.1f}")
    print(f"Waypoints reached: {info['current_waypoint_idx']}/{env.num_waypoints}")

    if success:
        completion_steps = info.get("completion_steps", step)
        print(
            f"SUCCESS! Completed in {completion_steps} steps ({completion_steps * env.dt:.1f}s)"
        )
    elif crash:
        print(f"CRASH: {crash}")
    else:
        print("TIMEOUT: Did not complete all waypoints")

    env.close()


def demo_random(max_steps: int = 500) -> None:
    """Run demo with random actions for testing.

    Args:
        max_steps: Maximum steps per episode
    """
    print("Running demo with random actions...")

    env = QuadcopterEnv(render_mode=None, add_sensor_noise=True)

    viz = RerunVisualizer(app_id="simhops-demo", spawn=True)
    viz.init()

    obs, info = env.reset()
    viz.reset()
    viz.log_waypoints(info["waypoints"], 0, radius=env.waypoint_radius)

    done = False
    total_reward = 0.0
    step = 0

    while not done and step < max_steps:
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

        time.sleep(0.01)

    print(f"\nDone: steps={step}, reward={total_reward:.1f}")
    env.close()


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Evaluate quadcopter agent")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Evaluate subcommand
    eval_parser = subparsers.add_parser("eval", help="Evaluate trained model")
    eval_parser.add_argument("model_path", type=str, help="Path to model directory")
    eval_parser.add_argument(
        "--slow", type=float, default=1.0, help="Slow motion factor"
    )
    eval_parser.add_argument(
        "--fast",
        action="store_true",
        help="Run as fast as possible (no realtime delay)",
    )
    eval_parser.add_argument(
        "--strict-tilt",
        action="store_true",
        help="Enable tilt termination (default: disabled for eval)",
    )

    # Demo subcommand
    demo_parser = subparsers.add_parser("demo", help="Run random action demo")
    demo_parser.add_argument(
        "--steps", type=int, default=500, help="Max steps per episode"
    )

    args = parser.parse_args()

    if args.command == "eval":
        evaluate(
            model_path=args.model_path,
            realtime=not args.fast,
            slow_motion=args.slow,
            disable_tilt_termination=not args.strict_tilt,
        )
    elif args.command == "demo":
        demo_random(max_steps=args.steps)


if __name__ == "__main__":
    main()
