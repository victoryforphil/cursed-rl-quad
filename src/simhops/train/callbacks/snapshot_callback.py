"""Append experiment snapshots on checkpoint cadence."""

from __future__ import annotations

from stable_baselines3.common.callbacks import BaseCallback

from simhops.train.metrics import MetricsLogger


class ExperimentSnapshotCallback(BaseCallback):
    """Append experiment snapshots on checkpoint cadence."""

    def __init__(
        self, metrics_logger: MetricsLogger, snapshot_freq: int, verbose: int = 0
    ) -> None:
        super().__init__(verbose)
        self._metrics_logger = metrics_logger
        self._snapshot_freq = max(1, snapshot_freq)

    def _on_step(self) -> bool:
        if self.n_calls == 0:
            return True
        if self.n_calls % self._snapshot_freq != 0:
            return True

        self._metrics_logger.write_checkpoint_summary(int(self.num_timesteps))
        return True
