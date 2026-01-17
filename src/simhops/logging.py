"""Unified logging helpers for SimHops."""

from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path
from typing import Final

import rerun as rr

_LOGGER_NAME: Final[str] = "simhops"
_LOGGER = logging.getLogger(_LOGGER_NAME)
_CONFIGURED = False
_LOG_PATH: Path | None = None
_RUN_ID: str | None = None


def setup_run_logging(
    run_id: str,
    data_dir: Path | str = "data",
    *,
    level: int = logging.INFO,
    rerun_entity_path: str = "logs",
) -> Path:
    """Configure logging for a run.

    Args:
        run_id: Run identifier used for the log file directory.
        data_dir: Root directory for per-run logs.
        level: Logger level to apply.
        rerun_entity_path: Entity path prefix for Rerun TextLog entries.

    Returns:
        Path to the log file.
    """
    global _CONFIGURED
    global _LOG_PATH
    global _RUN_ID

    run_dir = Path(data_dir) / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    log_path = run_dir / "run.log"

    if not _CONFIGURED:
        _LOGGER.setLevel(level)
        _LOGGER.propagate = False

        formatter = logging.Formatter(
            fmt="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        _LOGGER.addHandler(file_handler)

        try:
            rerun_handler = rr.LoggingHandler(rerun_entity_path)
            rerun_handler.setLevel(level)
            _LOGGER.addHandler(rerun_handler)
        except Exception:
            pass

        _CONFIGURED = True

    _LOG_PATH = log_path
    _RUN_ID = run_id
    return log_path


def log(message: str, level: int | str = "info") -> None:
    """Log a message through the configured logger."""
    if isinstance(level, str):
        level = logging._nameToLevel.get(level.upper(), logging.INFO)
    _LOGGER.log(level, message)


def log_run_start(run_id: str) -> None:
    """Log a standard run start line."""
    timestamp = datetime.now().isoformat(timespec="seconds")
    log(f"Run {run_id} started at {timestamp}")


def log_path() -> Path | None:
    """Return the current log file path if configured."""
    return _LOG_PATH


def run_id() -> str | None:
    """Return the current run id if configured."""
    return _RUN_ID
