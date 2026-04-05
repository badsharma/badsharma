"""CLI entrypoint for ai-agent-starter."""

from __future__ import annotations

from app.agent import run_agent
from app.models import AgentRequest


def main() -> None:
    """Run a simple interactive loop."""

    print("AI Agent Starter (type 'exit' to quit)")
    while True:
        raw = input("You: ").strip()
        if raw.lower() in {"exit", "quit"}:
            print("Bye!")
            break

        response = run_agent(AgentRequest(prompt=raw))
        print(f"Agent: {response.output}")
        if response.used_tools:
            print(f"Tools used: {', '.join(response.used_tools)}")


if __name__ == "__main__":
    main()
