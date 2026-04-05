"""Application configuration and environment loading."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Runtime settings for the AI agent app."""

    app_name: str = os.getenv("APP_NAME", "ai-agent-starter")
    model_name: str = os.getenv("MODEL_NAME", "gpt-4o-mini")
    temperature: float = float(os.getenv("TEMPERATURE", "0.2"))


def get_settings() -> Settings:
    """Return strongly-typed settings."""

    return Settings()
