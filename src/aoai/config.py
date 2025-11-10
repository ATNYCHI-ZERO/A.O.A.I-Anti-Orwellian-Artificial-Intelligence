"""Configuration loader for A.O.A.I."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import yaml
from pydantic import BaseModel, Field


class TelemetryConfig(BaseModel):
    enabled: bool = False
    endpoint: str | None = None


class MediaShieldConfig(BaseModel):
    enable: bool = False
    motion_threshold: float = Field(default=1_000_000, ge=0)
    red_threshold: float = Field(default=0.02, ge=0.0, le=1.0)
    blur_kernel: int = Field(default=51, ge=1)


class TruthEngineConfig(BaseModel):
    knowledge_base: Path
    max_references: int = Field(default=5, ge=1)
    kmath_epsilon: float = Field(default=1e-6, gt=0)


class LSAConfig(BaseModel):
    poll_interval: float = Field(default=2.0, gt=0)
    watch_permissions: list[str] = Field(default_factory=lambda: ["camera", "microphone", "biometric"])
    allowed_processes: list[str] = Field(default_factory=list)


class AOAIConfig(BaseModel):
    lsa: LSAConfig
    truth_engine: TruthEngineConfig
    media_shield: MediaShieldConfig
    telemetry: TelemetryConfig = Field(default_factory=TelemetryConfig)


def load_config(path: Path) -> AOAIConfig:
    """Load configuration from a YAML file."""

    data: Dict[str, Any] = yaml.safe_load(path.read_text())
    return AOAIConfig.model_validate(data)


__all__ = [
    "AOAIConfig",
    "LSAConfig",
    "TruthEngineConfig",
    "MediaShieldConfig",
    "TelemetryConfig",
    "load_config",
]
