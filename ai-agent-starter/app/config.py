"""Application configuration from environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Runtime settings for the AI agent app."""

    app_name: str
    model_name: str
    temperature: float


def get_settings() -> Settings:
    """Return strongly-typed settings with sensible defaults."""

    return Settings(
        app_name=os.getenv("APP_NAME", "ai-agent-starter"),
        model_name=os.getenv("MODEL_NAME", "gpt-4o-mini"),
        temperature=float(os.getenv("TEMPERATURE", "0.2")),
    )
