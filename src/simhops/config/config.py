from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from typing import Any

import yaml

from simhops.config.schema import SimHopsConfig, load_config


class Config:
    """Global configuration singleton with dot-notation access."""

    _schema: SimHopsConfig | None = None
    _raw: dict[str, Any] | None = None
    _path: Path | None = None

    @classmethod
    def load(cls, path: str | Path | None = None) -> SimHopsConfig:
        """Load configuration from YAML file.

        Args:
            path: Path to YAML config file. Defaults to cfg_default.yaml in cwd.
        """
        if path is None:
            path = Path("cfg_default.yaml")
        else:
            path = Path(path)

        cls._path = path
        cls._schema, cls._raw = load_config(path)
        return cls._schema

    @classmethod
    def ensure_loaded(cls) -> SimHopsConfig:
        """Ensure a config is loaded, falling back to default."""
        if cls._schema is None:
            cls.load()
        if cls._schema is None:
            raise RuntimeError("Config failed to load")
        return cls._schema

    @classmethod
    def get(cls, key: str, default: Any | None = None) -> Any:
        """Get a config value by dot-notation key."""
        schema = cls.ensure_loaded()
        data = asdict(schema)
        parts = key.split(".")

        current: Any = data
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return default

        return current

    @classmethod
    def __class_getitem__(cls, key: str) -> Any:
        return cls.get(key)

    @classmethod
    def schema(cls) -> SimHopsConfig:
        return cls.ensure_loaded()

    @classmethod
    def raw(cls) -> dict[str, Any]:
        cls.ensure_loaded()
        return cls._raw or {}

    @classmethod
    def path(cls) -> Path | None:
        return cls._path

    @classmethod
    def dump_yaml(cls, path: str | Path) -> None:
        """Dump the loaded config to a YAML file."""
        schema = cls.ensure_loaded()
        output_path = Path(path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8") as handle:
            yaml.safe_dump(asdict(schema), handle, sort_keys=False)
