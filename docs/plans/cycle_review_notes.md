# Cycle-By-Cycle Review Notes

These notes capture issues/observations found in short cycles. Each cycle documents the why, a small snippet anchor, the suggested fix, and a risk level. No code changes are applied here.

## Cycle 1 - Curriculum Stage Loop (Training)
- Why: `VecNormalize` is recreated each stage, so running stats reset between stages and can destabilize training.
- Snippet: `env = VecNormalize(...)` inside the stage loop in `src/simhops/train.py`.
- Suggested fix: persist or reload running stats per stage; alternatively, reuse a single `VecNormalize` instance across stages.
- Risk: medium (behavior shift in training dynamics).

## Cycle 2 - Evaluation Consistency (Training)
- Why: evaluation env is created with stage-specific overrides, so “eval” is not a stable baseline across stages.
- Snippet: `eval_env = make_vec_env(..., random_start_waypoint=stage_env_cfg.random_start_waypoint, ...)`.
- Suggested fix: add a fixed global eval env that ignores stage overrides; optionally keep stage eval as separate metrics.
- Risk: medium (changes comparability of results, but improves clarity).

## Cycle 3 - Reward Logger Output
- Why: Reward logger prints `Mean waypoints ... /10`, but `max_waypoints` can be lower during curriculum stages.
- Snippet: `f"Mean waypoints: {mean_waypoints:.1f}/10"` in `RewardLoggerCallback`.
- Suggested fix: use `info.get("max_waypoints")` or `env.num_waypoints` for the divisor.
- Risk: low (log-only adjustment).

## Cycle 4 - Stage Metadata in Run Config
- Why: `config.json` from `MetricsLogger` reflects base `cfg.env`, not stage overrides.
- Snippet: `cfg = Config.schema()` in `MetricsLogger._write_config`.
- Suggested fix: write per-stage config metadata (stage name/index, stage-specific env values) or produce stage-specific config files.
- Risk: low (logging correctness).

## Cycle 5 - Stage Timesteps vs Total Timesteps
- Why: `training.total_timesteps` is still present, but curriculum stages can exceed or ignore it without validation.
- Snippet: `stage.total_timesteps if stage is not None else cfg.training.total_timesteps`.
- Suggested fix: validate stage totals; optionally log a warning when curriculum is enabled and `training.total_timesteps` is ignored.
- Risk: low (clarity/safety).

## Cycle 6 - Waypoint Cap Off-by-One
- Why: `_current_waypoint_idx` increments before completion check; if capped, logs may show idx == max.
- Snippet: `self._current_waypoint_idx += 1` then `if >= max_waypoints`.
- Suggested fix: clamp index or ensure info output uses `min(idx, max_waypoints)` after increment.
- Risk: low (log/metrics accuracy).

## Cycle 7 - Eval Results Metadata
- Why: `eval_results.csv` lacks stage metadata when curriculum is enabled.
- Snippet: `eval_writer.writerow({"eval_run": ...})` in `src/simhops/evaluate.py`.
- Suggested fix: include `stage_name` and `stage_index` when running eval during curriculum.
- Risk: low (data annotation only).

## Cycle 8 - Metrics Logger Type Safety
- Why: `MetricsLoggerCallback` assumes `episode` info dict always has `r`/`l`; any changes in wrapper format could insert zeros and skew summary stats.
- Snippet: `episode_info = info.get("episode", {})` in `MetricsLoggerCallback._on_step`.
- Suggested fix: skip rows when `episode` data is missing or invalid; log a debug warning once per run.
- Risk: low (logging/analysis only).

## Cycle 9 - Curriculum Stage Overlap in Checkpoints
- Why: `CheckpointCallback` writes all stages into the same `checkpoints` directory; stage-specific prefixes help but still share a folder.
- Snippet: `save_path=str(run_path / "checkpoints")`.
- Suggested fix: separate into stage subfolders (e.g., `checkpoints/stage_1`).
- Risk: low (artifact organization only).

## Cycle 10 - Config Validation Gaps
- Why: `max_waypoints`, `waypoint_noise`, `max_episode_steps` can be negative or invalid, but no validation or warnings exist.
- Snippet: `EnvConfig(**data["env"])`.
- Suggested fix: validate config ranges at load time and warn/raise for invalid values.
- Risk: low (safety guardrails).

## Cycle 11 - Env Observation Consistency
- Why: `_get_observation` uses `self.num_waypoints` even when `max_waypoints` < total; relative waypoint selection may refer to future waypoints beyond the cap.
- Snippet: `wp_idx = min(self._current_waypoint_idx, self.num_waypoints - 1)`.
- Suggested fix: cap waypoint selection to `self._max_waypoints_effective - 1` when curriculum is active.
- Risk: low (reward/obs consistency).

## Cycle 12 - Eval CSV Multi-Episode Summary
- Why: `evaluate.py` writes per-episode rows but no summary for multi-episode runs (means/median).
- Snippet: `for episode_idx in range(1, episodes + 1): ... eval_writer.writerow(...)`.
- Suggested fix: add a final summary row or separate summary JSON to avoid manual aggregation.
- Risk: low (analysis convenience).
