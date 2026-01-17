# Metrics + Logging Plan for Agent Iteration

## Context + Findings

- Training currently logs to Rerun (visual), TensorBoard (binary), and EvalCallback NPZ files.
- No agent-friendly file logs exist (CSV/JSONL) for rapid iteration.
- Key gaps: success rate, crash breakdown, waypoint completion stats, and easy run-to-run comparison.

## Goals

- Give agents structured metrics to diagnose learning issues and compare experiments.
- Preserve existing Rerun + TensorBoard while adding CSV/JSON summaries.
- Keep logs compact but comprehensive for RL research iteration.

## Proposed Run Layout

```
models/
├── experiments.csv
└── run_YYYYMMDD_HHMMSS/
    ├── config.json
    ├── training_summary.json
    ├── episodes.csv
    ├── updates.csv
    ├── eval_results.csv
    ├── checkpoints/
    ├── final_model/
    └── tensorboard/
```

## File Specs

### config.json
- Run metadata: run_id, timestamp, git_commit
- Hyperparameters: lr, batch_size, gamma, gae_lambda, clip_range, ent_coef, n_envs, total_timesteps
- Environment: waypoint_noise, waypoint_radius, max_episode_steps, include_position, add_sensor_noise
- Network: policy and layer sizes
- Reward weights (documented constants)

### training_summary.json
- performance: best reward, mean reward (last 100), improvement
- success_metrics: success rate, mean waypoints reached, mean completion steps, first success episode
- failure_analysis: crash rate, timeout rate, crash type breakdown
- training_health: final losses, mean KL, entropy trend
- wall_time_seconds, total_episodes, total_timesteps

### episodes.csv
- episode, timestep, reward, length
- waypoints_reached, success, crash_type
- final_distance, mean_speed, max_tilt_deg, time_to_first_wp

### updates.csv
- update, timestep
- policy_loss, value_loss, entropy, kl_divergence
- clip_fraction, explained_variance, learning_rate
- mean_episode_reward (rolling)

### experiments.csv
- run_id, timestamp, total_timesteps
- success_rate, mean_reward, best_reward
- notes

### eval_results.csv
- eval_run, model_path, episode, reward
- length, waypoints_reached, success
- crash_type, completion_time_s

## Environment Metrics Additions

Add to info dict or internal trackers:
- max_tilt_deg per episode
- mean_speed per episode
- time_to_first_wp
- final_distance at termination

## Agent Usage Examples

Quick triage:
- Low success_rate or high crash_rate indicates unstable policy.
- Excessive_tilt crashes suggest more conservative action limits or reward shaping.
- Long time_to_first_wp suggests poor initial stabilization.

Run comparison:
- `experiments.csv` is the primary index for best runs.
- `training_summary.json` provides immediate context.

## Integration Points

- train.py: add MetricsLogger callback to write episodes.csv and updates.csv.
- evaluate.py: add optional structured logging and multi-episode eval.
- Keep Rerun/TensorBoard unchanged.

## Open Questions

- Whether to add optional per-step JSONL logging (large files).
- Whether to log normalized vs raw reward in summary files.
