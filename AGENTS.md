# SimHops - Quadcopter RL Training

## Project Overview

A quadcopter reinforcement learning environment using MuJoCo physics and Stable-Baselines3 PPO, with Rerun visualization for training and evaluation.

## Git Workflow

### Branches
- `master` - Main development branch
- Use feature branches for significant changes: `feature/<name>`

### Commit Guidelines
- Use conventional commits: `feat:`, `fix:`, `refactor:`, `docs:`, `chore:`
- Keep commits atomic and focused
- Don't commit model checkpoints (they're in .gitignore)

### What's Tracked
- Source code (`src/`)
- Configuration (`pyproject.toml`, `.python-version`)
- Documentation (`README.md`, `AGENTS.md`)

### What's Ignored
- Model checkpoints (`models/checkpoints/`, `*.zip`, `*.pkl`)
- TensorBoard logs (`models/tensorboard/`)
- Virtual environments (`.venv/`)
- Python cache (`__pycache__/`)

## Key Files

### Training
- `src/simhops/train.py` - PPO training with Rerun visualization
- `src/simhops/evaluate.py` - Model evaluation with 3D visualization

### Environment
- `src/simhops/envs/quadcopter_env.py` - Gymnasium environment
  - Fixed 10-waypoint expanded path
  - Configurable waypoint randomization (`waypoint_noise`)
  - 100Hz physics simulation

### Visualization
- `src/simhops/viz/env_logger.py` - Ground truth/physics logging
- `src/simhops/viz/training_logger.py` - RL metrics logging
- `src/simhops/viz/rerun_viz.py` - Unified visualizer

### Physics
- `src/simhops/core/quadcopter.py` - Quadcopter dynamics
- `src/simhops/core/sensors.py` - Sensor models with noise

## Commands

```bash
# Train with Rerun visualization
uv run python -m simhops.train --rerun --timesteps 500000

# Train with custom waypoint noise
uv run python -m simhops.train --waypoint-noise 2.0 --timesteps 1000000

# Evaluate trained model
uv run python -m simhops.evaluate eval models/final_model

# Demo with random actions
uv run python -m simhops.evaluate demo
```

## Configuration

### Waypoint Path (Expanded)
```
1: (5.5, 0, 3.3)    2: (10.5, 5.5, 4.5)    3: (7.5, 11.5, 6.2)
4: (0, 14, 7.2)     5: (-7.5, 10, 6.2)     6: (-11.5, 4, 5.2)
7: (-10, -4, 4.2)   8: (-5.5, -10.5, 5.2)  9: (4.5, -7.5, 3.5)
10: (7.5, -2.5, 3.0)
```

### Default Parameters
- `waypoint_noise`: 1.0m (+/- per reset)
- `waypoint_radius`: 1.0m
- `arena_size`: 25m
- `max_episode_steps`: 5000

## Agent Notes

- Model checkpoints are NOT committed - save important models externally
- Use `--waypoint-noise 0.0` for deterministic evaluation
- The 3D visualization estimates drone position from relative waypoint observations
- `include_position` is considered a cheat for training runs; keep it disabled unless explicitly needed

## Logging Plan (Agent-Focused)

The logging plan is documented in `docs/plans/metrics_logging_plan.md`.

Key goals for agents:
- Structured, readable logs (CSV + JSON) for fast iteration
- Episode summaries, PPO update metrics, and evaluation results
- Run-to-run comparison via a global `experiments.csv` index

Proposed run layout (inside `models/`):
- `run_YYYYMMDD_HHMMSS/` per experiment
- `config.json`, `training_summary.json`, `episodes.csv`, `updates.csv`, `eval_results.csv`

This plan is intended to support automated tuning of hyperparameters, reward shaping, and policy architecture.
