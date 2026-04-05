"""Data models used by the agent."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class AgentRequest:
    """Incoming request payload for the agent."""

    prompt: str

    def __post_init__(self) -> None:
        if not self.prompt or not self.prompt.strip():
            raise ValueError("prompt must be a non-empty string")


@dataclass(frozen=True)
class AgentResponse:
    """Outgoing response from the agent."""

    output: str
    used_tools: list[str] = field(default_factory=list)
