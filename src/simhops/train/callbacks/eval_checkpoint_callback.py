"""Evaluation checkpoint callback for periodic model evaluation."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from stable_baselines3.common.callbacks import BaseCallback


class EvalCheckpointCallback(BaseCallback):
    """Callback that runs evaluation on checkpoints and saves to .rrd files.

    Triggers at checkpoint save frequency and spawns a subprocess to run
    evaluation, saving results to .rrd files for visualization correlation.
    """

    def __init__(
        self,
        checkpoint_dir: Path,
        eval_rrd_dir: Path,
        run_dir: Path,
        checkpoint_freq: int,
        n_eval_episodes: int = 1,
        stage_index: int = 1,
        stage_name: str = "default",
        verbose: int = 0,
    ) -> None:
        """Initialize evaluation checkpoint callback.

        Args:
            checkpoint_dir: Directory where checkpoints are saved
            eval_rrd_dir: Directory to save evaluation .rrd files
            run_dir: Run directory containing training metrics
            checkpoint_freq: Checkpoint frequency (in timesteps)
            n_eval_episodes: Number of episodes to run per evaluation
            stage_index: Current curriculum stage index
            stage_name: Current curriculum stage name
            verbose: Verbosity level
        """
        super().__init__(verbose)
        self._checkpoint_dir = checkpoint_dir
        self._eval_rrd_dir = eval_rrd_dir
        self._run_dir = run_dir
        self._checkpoint_freq = checkpoint_freq
        self._n_eval_episodes = n_eval_episodes
        self._stage_index = stage_index
        self._stage_name = stage_name
        self._last_eval_timestep = 0

        # Create eval recording directory
        self._eval_rrd_dir.mkdir(parents=True, exist_ok=True)

    def _on_step(self) -> bool:
        """Check if we should trigger evaluation."""
        # Check if we've passed a checkpoint boundary
        if self.num_timesteps - self._last_eval_timestep >= self._checkpoint_freq:
            self._run_evaluation()
            self._last_eval_timestep = self.num_timesteps

        return True

    def _run_evaluation(self) -> None:
        """Spawn subprocess to run evaluation and save to .rrd."""
        # Find the most recent checkpoint
        checkpoint_pattern = f"ppo_quadcopter_stage_{self._stage_index}_{self.num_timesteps}_steps.zip"
        checkpoint_path = self._checkpoint_dir / checkpoint_pattern

        if not checkpoint_path.exists():
            if self.verbose > 0:
                print(f"[EvalCheckpoint] Checkpoint not found: {checkpoint_path}")
            return

        # Output .rrd file path
        output_rrd = self._eval_rrd_dir / f"eval_stage_{self._stage_index}_{self.num_timesteps}.rrd"

        # Build command to run evaluation
        # We'll call eval_to_rrd directly via Python
        cmd = [
            sys.executable,
            "-c",
            f"from pathlib import Path; "
            f"from simhops.evaluate import eval_to_rrd; "
            f"eval_to_rrd("
            f"'{checkpoint_path}', "
            f"Path('{output_rrd}'), "
            f"episodes={self._n_eval_episodes}, "
            f"recording_name='eval:{self._stage_name}:{self.num_timesteps}', "
            f"spawn_viewer=True, "
            f"run_dir=Path('{self._run_dir}')"
            f")",
        ]

        if self.verbose > 0:
            print(
                f"[EvalCheckpoint] Running evaluation at {self.num_timesteps} steps "
                f"-> {output_rrd.name}"
            )

        # Run subprocess in background (non-blocking)
        try:
            subprocess.Popen(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
            )
        except Exception as e:
            if self.verbose > 0:
                print(f"[EvalCheckpoint] Failed to spawn evaluation: {e}")
