"""Unit tests for ai-agent-starter agent behavior."""

from __future__ import annotations

import re
import unittest

from app.agent import run_agent
from app.models import AgentRequest


class AgentTests(unittest.TestCase):
    def test_echo_flow_when_no_tool_keyword(self) -> None:
        response = run_agent(AgentRequest(prompt="hello there"))

        self.assertEqual(response.output, "Agent received: hello there")
        self.assertEqual(response.used_tools, [])

    def test_time_keyword_triggers_time_tool(self) -> None:
        response = run_agent(AgentRequest(prompt="what is the time right now?"))

        self.assertIn("Current UTC time:", response.output)
        self.assertEqual(response.used_tools, ["get_current_utc_time"])
        self.assertRegex(
            response.output,
            r"Current UTC time: \d{4}-\d{2}-\d{2}T",
        )


if __name__ == "__main__":
    unittest.main()
