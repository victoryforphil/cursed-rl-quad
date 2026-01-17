# Staged Training Plan (Curriculum)

## Goal

Train the quadcopter policy with a staged curriculum that moves from easy, low-variance tasks to harder, randomized conditions. This improves learning stability and final robustness without changing reward shaping.

The plan is aligned with the current environment knobs in:
- `src/simhops/envs/quadcopter_env.py` (waypoint noise, random start waypoint, sensor noise)
- `src/simhops/train.py` (PPO training entry point)

## Guiding Principles

- Start deterministic and low-noise to learn stable control.
- Increase waypoint noise gradually to build generalization.
- Introduce random start waypoints last to force recovery and partial-route capability.
- Keep PPO hyperparameters stable across stages unless a stage is unstable.

## Stages

### Stage 0: Hover + Single Waypoint

- Purpose: Learn stabilization and target approach with minimal variance.
- Environment:
  - `waypoint_noise=0.0`
  - `add_sensor_noise=false`
  - `random_start_waypoint=false`
  - Waypoints: 1 (first waypoint only)
- Notes:
  - If limiting to 1 waypoint is not supported, keep all waypoints but terminate after reaching the first.

### Stage 1: Short Path (Waypoints 1-3)

- Purpose: Learn sequential waypoint transitions.
- Environment:
  - `waypoint_noise=0.25`
  - `add_sensor_noise=true`
  - `random_start_waypoint=false`
  - Waypoints: 3

### Stage 2: Full Path, Low Randomization

- Purpose: Solve the full task with mild randomness.
- Environment:
  - `waypoint_noise=0.5`
  - `add_sensor_noise=true`
  - `random_start_waypoint=false`
  - Waypoints: 10 (full course)

### Stage 3: Full Path, Default Randomization

- Purpose: Match current default training conditions.
- Environment:
  - `waypoint_noise=1.0`
  - `add_sensor_noise=true`
  - `random_start_waypoint=false`
  - Waypoints: 10

### Stage 4: Full Path, Hard Randomization + Random Starts

- Purpose: Robustness to large waypoint offsets and partial starts.
- Environment:
  - `waypoint_noise=1.5-2.0`
  - `add_sensor_noise=true`
  - `random_start_waypoint=true`
  - Waypoints: 10

## Stage Transitions

Advance to the next stage when performance is stable, not just improving. Suggested criteria:

- Success rate is stable for at least 50-100 episodes.
- Mean waypoints reached stops increasing for multiple evaluations.
- Crash types shift away from tilt/collision to timeouts.

## Suggested Timesteps Per Stage

- Stage 0: 100k-200k
- Stage 1: 200k-400k
- Stage 2: 300k-600k
- Stage 3: 500k-1M
- Stage 4: 500k-1M

These are starting points. Adjust based on observed learning speed.

## Implementation Options

1) Add a `num_waypoints` or `max_waypoints` argument to the environment to limit path length for early stages.
2) Introduce a stage-specific termination condition (e.g., early stop after waypoint N).
3) Keep the env unchanged and use `random_start_waypoint` + shorter `max_episode_steps` to approximate partial paths.

## Research Rationale (Brief)

- Curriculum learning is commonly used to reduce variance in early policy updates and improve convergence in RL.
- Domain randomization improves robustness, but introducing variability gradually tends to stabilize policy learning.
- PPO is sensitive to high-variance environments early on; stable early tasks yield more consistent gradient updates.

Reference ideas to anchor these principles:
- Curriculum learning concepts in RL (e.g., Bengio et al., 2009).
- Domain randomization for robotic transfer (e.g., Tobin et al., 2017).
- PPO stability and sample efficiency (Schulman et al., 2017).
