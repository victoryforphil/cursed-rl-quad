# Rerun Visualization Refactor - 2026-01-17

## Summary

Refactored training visualization from continuous per-step logging to snapshot-based approach, reducing data volume by ~99% while preserving training insight.

## Changes Made

### 1. Config Updates

**Files Modified:**
- `src/simhops/config/schema.py`
- `cfg_default.yaml`

**Changes:**
- Removed `log_3d_freq` from `CallbackConfig`
- Added `snapshot_freq_updates: int = 20` (capture every N PPO updates)
- Added `snapshot_max_steps: int = 500` (cap snapshot episode length)
- Added `log_aggregated_metrics: bool = True` to `VisualizationConfig`

### 2. TrainingLogger Simplification

**File:** `src/simhops/viz/training_logger.py`

**Removed:**
- `log_episode()` - per-episode metrics
- `log_actions()` - per-step action logging
- `log_actions_clipped()` - per-step clipped actions
- `log_step_metrics()` - per-step distance/speed/reward

**Added:**
- `log_aggregated_metrics()` - smoothed metrics on PPO updates
  - `mean_reward`: Rolling mean episode reward
  - `mean_length`: Rolling mean episode length
  - `success_rate`: % episodes completing path
  - `waypoints_per_episode`: Average waypoints reached

### 3. EnvLogger Updates

**File:** `src/simhops/viz/env_logger.py`

**Changes:**
- Removed incremental trajectory accumulation from `log_drone()`
- Removed `_trajectory` list tracking
- Made `reset_trajectory()` a no-op (kept for compatibility)

**Added:**
- `log_snapshot_trajectory()` - logs complete episode as single snapshot
  - Accepts full position/orientation lists
  - Logs trajectory, final drone state, waypoints, episode summary

### 4. RerunVisualizer Cleanup

**File:** `src/simhops/viz/rerun_viz.py`

**Changes:**
- Simplified blueprint: "Latest Policy" + "Training Progress" + "Losses"
- Removed training-specific convenience methods:
  - `log_drone_position()`
  - `log_waypoints_training()`
  - `log_training_metrics()`
  - `log_actions()`
  - `log_clipped_actions()`
  - `log_metrics()`
  - `log_action()`
- Kept only evaluation-relevant methods:
  - `log_quadcopter()` - for eval/demo
  - `log_waypoints()` - for eval/demo

### 5. New SnapshotRerunCallback

**File:** `src/simhops/train/callbacks/rerun_callback.py`

**Complete Rewrite:**

**Old Approach (RerunTrainingCallback):**
- Logged 3D state every 5 steps (~3M logs over 15M timesteps)
- Logged every episode completion
- Logged actions every step
- Accumulated trajectory continuously

**New Approach (SnapshotRerunCallback):**
- Logs aggregated metrics only on PPO updates (~750 over 15M timesteps)
- Captures complete episode snapshots periodically
- Uses dual timelines:
  - `ppo_update`: Training progress (sequence)
  - `snapshot`: Visualization episodes (sequence)

**Key Features:**
- Episode statistics tracking (rewards, lengths, waypoints, successes)
- Periodic snapshot capture (every N PPO updates)
- Max step cap for snapshots (default 500)
- Complete episode trajectory logging
- Print progress every 10 episodes

### 6. Integration Updates

**Files:**
- `src/simhops/train/callbacks/__init__.py` - renamed export
- `src/simhops/train/trainer.py` - uses `SnapshotRerunCallback` with new config

## Expected Impact

| Metric | Before | After | Reduction |
|--------|--------|-------|-----------|
| 3D log calls | ~3,000,000 | ~750 | 99.975% |
| Scalar episode logs | ~100,000+ | ~750 | 99.25% |
| Data size | Large (GB) | Small (MB) | ~99% |
| Training overhead | Noticeable | Negligible | Significant |
| Insight quality | Noisy | Smooth trends | Better |

## What Users Will See in Rerun

### Before:
- Extremely noisy episode reward curves
- Dense 3D trajectory that slowed viewer
- Thousands of datapoints per metric

### After:
- Smooth aggregated progress curves (mean reward, success rate, etc.)
- Periodic "snapshots" showing latest policy behavior
- Clean, interpretable timelines
- Responsive viewer even during long training runs

## Timelines

1. **ppo_update** (main): Shows training progress over PPO updates
   - Progress metrics (mean_reward, success_rate, etc.)
   - Losses (policy, value, entropy)
   - PPO diagnostics (KL, clip fraction, etc.)

2. **snapshot**: Shows visualization episode captures
   - Complete trajectory for selected episode
   - Final drone position and orientation
   - Waypoints with progress
   - Episode summary (reward, waypoints, steps)

## Configuration

Default settings (in `cfg_default.yaml`):
```yaml
callbacks:
  snapshot_freq_updates: 20     # Every 20 PPO updates
  snapshot_max_steps: 500       # Cap snapshot at 500 steps

visualization:
  log_aggregated_metrics: true  # Enable smoothed metrics
```

For 15M timesteps with n_steps=2048, n_envs=10:
- ~732 PPO updates total
- ~37 snapshots (every 20 updates)
- Each snapshot ≤500 steps

## Breaking Changes

- `RerunTrainingCallback` renamed to `SnapshotRerunCallback`
- Different initialization parameters (removed `log_3d_freq`, added `snapshot_freq_updates`, `snapshot_max_steps`)
- No more per-step 3D logging during training
- Removed many convenience methods from `RerunVisualizer`

## Backward Compatibility

- Evaluation and demo workflows unchanged
- `log_quadcopter()` and `log_waypoints()` still available
- `reset_trajectory()` kept as no-op for compatibility
