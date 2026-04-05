"""Core agent orchestration logic."""

from __future__ import annotations

from app.models import AgentRequest, AgentResponse
from app.tools import get_current_utc_time


def run_agent(request: AgentRequest) -> AgentResponse:
    """Run a tiny example agent flow.

    Behavior:
    - If prompt asks for time, call a tool.
    - Otherwise echo the prompt with a prefix.
    """

    prompt = request.prompt.strip()

    if "time" in prompt.lower():
        timestamp = get_current_utc_time()
        return AgentResponse(
            output=f"Current UTC time: {timestamp}",
            used_tools=["get_current_utc_time"],
        )

    return AgentResponse(output=f"Agent received: {prompt}")
