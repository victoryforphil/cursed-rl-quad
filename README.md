# SimHops - Quadcopter RL Training

A quadcopter reinforcement learning environment using MuJoCo physics and Stable-Baselines3 PPO, with Rerun visualization for training and evaluation.

## Commands

```bash
# Train with Rerun visualization
scripts/train.sh --rerun --timesteps 500000

# Train with custom waypoint noise
scripts/train.sh --waypoint-noise 2.0 --timesteps 1000000

# Evaluate trained model
scripts/eval.sh eval models/final_model

# Demo with random actions
scripts/eval.sh demo
```

## Scripts

- `scripts/train.sh` wraps `uv run python -m simhops.train` and forwards arguments.
- `scripts/eval.sh` wraps `uv run python -m simhops.evaluate` and forwards arguments.
