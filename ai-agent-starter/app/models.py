"""Pydantic data models used by the agent."""

from __future__ import annotations

from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    """Incoming request payload for the agent."""

    prompt: str = Field(..., min_length=1, description="User prompt for the agent")


class AgentResponse(BaseModel):
    """Outgoing response from the agent."""

    output: str
    used_tools: list[str] = Field(default_factory=list)
