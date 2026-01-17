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
_FILE_HANDLER: logging.FileHandler | None = None
_RERUN_HANDLER: logging.Handler | None = None
_STREAM_HANDLER: logging.StreamHandler | None = None


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
    global _FILE_HANDLER
    global _RERUN_HANDLER
    global _STREAM_HANDLER

    run_dir = Path(data_dir) / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    log_path = run_dir / "run.log"

    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    _LOGGER.setLevel(level)
    _LOGGER.propagate = False

    if _FILE_HANDLER is not None:
        _LOGGER.removeHandler(_FILE_HANDLER)
        _FILE_HANDLER.close()

    _FILE_HANDLER = logging.FileHandler(log_path, encoding="utf-8")
    _FILE_HANDLER.setLevel(level)
    _FILE_HANDLER.setFormatter(formatter)
    _LOGGER.addHandler(_FILE_HANDLER)

    if _STREAM_HANDLER is None:
        _STREAM_HANDLER = logging.StreamHandler()
        _STREAM_HANDLER.setFormatter(formatter)
        _LOGGER.addHandler(_STREAM_HANDLER)

    _STREAM_HANDLER.setLevel(level)

    if _RERUN_HANDLER is not None:
        _LOGGER.removeHandler(_RERUN_HANDLER)

    try:
        _RERUN_HANDLER = rr.LoggingHandler(rerun_entity_path)
        _RERUN_HANDLER.setLevel(level)
        _LOGGER.addHandler(_RERUN_HANDLER)
    except Exception:
        _RERUN_HANDLER = None

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
