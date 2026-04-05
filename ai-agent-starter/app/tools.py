"""Tool registry for the AI agent."""

from __future__ import annotations

from datetime import datetime, timezone


def get_current_utc_time() -> str:
    """Simple tool returning the current UTC timestamp."""

    return datetime.now(timezone.utc).isoformat()


def list_tools() -> dict[str, str]:
    """Expose available tools with descriptions."""

    return {
        "get_current_utc_time": "Returns current UTC time in ISO format.",
    }
