"""Orchestrator: runs the four agents in order (the "team").

Usage:
    python main.py            # live data (falls back to sample if offline)
    python main.py --offline  # force the bundled sample data
"""
import argparse
import datetime as dt
import json
from pathlib import Path

from agents import CollectorAgent, ReporterAgent, ReviewerAgent, TriageAgent


def main() -> None:
    parser = argparse.ArgumentParser(description="PatchTeam patch-briefing agents")
    parser.add_argument("--offline", action="store_true", help="use sample data")
    args = parser.parse_args()

    config_path = Path(__file__).parent / "config.json"
    config = json.loads(config_path.read_text())
    print(f"Using config file: {config_path}")
    state = {"config": config, "today": dt.date.today()}

    team = [CollectorAgent(offline=args.offline), TriageAgent(),
            ReviewerAgent(), ReporterAgent()]

    for agent in team:  # each agent hands the state to the next
        state = agent.run(state)

    print(f"\nDone! Open {state['report_path']}")


if __name__ == "__main__":
    main()
