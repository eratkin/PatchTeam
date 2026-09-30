"""PatchTeam: four tiny agents that turn CISA's exploited-vulnerability list
into a prioritized weekly patch briefing.

Each agent has ONE job, reads a shared 'state' dictionary, adds its results,
and hands it on. The orchestrator (main.py) runs them in order.
"""
from __future__ import annotations

import datetime as dt
import json
import os
from pathlib import Path

import requests

KEV_URL = (
    "https://www.cisa.gov/sites/default/files/feeds/"
    "known_exploited_vulnerabilities.json"
)
ROOT = Path(__file__).parent
SAMPLE_FILE = ROOT / "data" / "sample_kev.json"
CACHE_FILE = ROOT / "data" / "kev_cache.json"
REPORT_DIR = ROOT / "reports"


class Agent:
    """Base class: every agent has a name and a run() method."""

    name = "Agent"

    def say(self, message: str) -> None:
        print(f"[{self.name}] {message}")

    def run(self, state: dict) -> dict:
        raise NotImplementedError


# --------------------------------------------------------------------------
# Agent 1: goes and gets the data
# --------------------------------------------------------------------------
class CollectorAgent(Agent):
    name = "Collector"

    def __init__(self, offline: bool = False):
        self.offline = offline

    def _load_sample(self, today: dt.date) -> dict:
        """Sample entries store 'days ago' offsets; turn them into real dates
        so the demo always looks fresh."""
        data = json.loads(SAMPLE_FILE.read_text(encoding="utf-8"))
        for v in data["vulnerabilities"]:
            v["dateAdded"] = str(today - dt.timedelta(days=v.pop("_addedDaysAgo")))
            v["dueDate"] = str(today + dt.timedelta(days=v.pop("_dueInDays")))
        return data

    def run(self, state: dict) -> dict:
        today = state["today"]
        data, source = None, ""

        if not self.offline:
            try:
                self.say("Downloading the live CISA KEV catalog...")
                resp = requests.get(
                    KEV_URL, timeout=30, headers={"User-Agent": "patchteam-portfolio"}
                )
                resp.raise_for_status()
                data, source = resp.json(), "live CISA KEV feed"
                CACHE_FILE.write_text(json.dumps(data), encoding="utf-8")
            except Exception as exc:  # network down, blocked, etc.
                self.say(f"Live download failed ({exc}).")
                if CACHE_FILE.exists():
                    data = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
                    source = "cached copy of CISA KEV feed"

        if data is None:
            self.say("Using bundled SAMPLE data.")
            data, source = self._load_sample(today), "bundled sample data"

        state["vulns"] = data["vulnerabilities"]
        state["source"] = source
        state["catalog_version"] = data.get("catalogVersion", "unknown")
        self.say(f"Loaded {len(state['vulns'])} vulnerabilities from {source}.")
        return state


# --------------------------------------------------------------------------
# Agent 2: scores every vulnerability and explains why
# --------------------------------------------------------------------------
class TriageAgent(Agent):
    name = "Triage"

    def run(self, state: dict) -> dict:
        cfg, today = state["config"], state["today"]
        stack = [s.lower() for s in cfg["my_stack"]]
        cutoff = today - dt.timedelta(days=cfg["lookback_days"])
        scored = []

        for v in state["vulns"]:
            added = dt.date.fromisoformat(v["dateAdded"])
            if added < cutoff:
                continue  # too old for this briefing

            score, reasons = 10, ["Actively exploited in the wild (+10)"]
            label = f"{v['vendorProject']} {v['product']}".lower()

            in_stack = any(item in label for item in stack)
            if in_stack:
                score += 30
                reasons.append("Vendor/product is in YOUR tech stack (+30)")

            if str(v.get("knownRansomwareCampaignUse", "")).lower() == "known":
                score += 40
                reasons.append("Used in ransomware campaigns (+40)")

            if (today - added).days <= 7:
                score += 15
                reasons.append("Added to the catalog in the last 7 days (+15)")

            days_left = (dt.date.fromisoformat(v["dueDate"]) - today).days
            if days_left < 0:
                score += 15
                reasons.append(f"Government patch deadline passed {-days_left} days ago (+15)")
            elif days_left <= 7:
                score += 10
                reasons.append(f"Government patch deadline in {days_left} days (+10)")

            scored.append({**v, "score": min(score, 100), "reasons": reasons,
                           "in_stack": in_stack})

        state["scored"] = scored
        matched = sum(1 for i in scored if i["in_stack"])
        self.say(f"Scored {len(scored)} vulnerabilities inside the "
                 f"{cfg['lookback_days']}-day window; {matched} match your stack "
                 f"{cfg['my_stack']}.")
        return state


# --------------------------------------------------------------------------
# Agent 3: the skeptic. Double-checks Triage and applies policy rules
# --------------------------------------------------------------------------
class ReviewerAgent(Agent):
    name = "Reviewer"

    def run(self, state: dict) -> dict:
        seen, reviewed, overrides = set(), [], 0

        for item in sorted(state["scored"], key=lambda x: -x["score"]):
            if item["cveID"] in seen:  # rule 1: no duplicates
                continue
            seen.add(item["cveID"])

            tier = ("PATCH NOW" if item["score"] >= 60
                    else "THIS WEEK" if item["score"] >= 40 else "WATCH")
            note = ""

            # rule 2: don't cry wolf about software you don't run
            if tier == "PATCH NOW" and not item["in_stack"]:
                tier, overrides = "THIS WEEK", overrides + 1
                note = "Downgraded: high score but not in your stack."
            # rule 3: ransomware + your stack is always urgent
            elif item["in_stack"] and str(
                item.get("knownRansomwareCampaignUse", "")).lower() == "known" \
                    and tier != "PATCH NOW":
                tier, overrides = "PATCH NOW", overrides + 1
                note = "Upgraded: ransomware-linked and in your stack."

            reviewed.append({**item, "tier": tier, "review_note": note})

        state["reviewed"] = reviewed
        self.say(f"Reviewed {len(reviewed)} items, changed {overrides} decision(s).")
        return state


# --------------------------------------------------------------------------
# Agent 4: writes the briefing (optionally with an AI-written summary)
# --------------------------------------------------------------------------
class ReporterAgent(Agent):
    name = "Reporter"
    TIERS = [("PATCH NOW", "🔴"), ("THIS WEEK", "🟠"), ("WATCH", "🟡")]

    def _ai_summary(self, items: list[dict]) -> str:
        """Optional: needs `pip install anthropic` and ANTHROPIC_API_KEY."""
        if not os.getenv("ANTHROPIC_API_KEY") or not items:
            return ""
        try:
            import anthropic

            facts = "\n".join(
                f"- {i['cveID']} {i['vendorProject']} {i['product']} "
                f"(tier {i['tier']}, score {i['score']})" for i in items[:5]
            )
            msg = anthropic.Anthropic().messages.create(
                model="claude-sonnet-5-5",
                max_tokens=300,
                messages=[{"role": "user", "content":
                    "Write a 3-sentence plain-English summary for a busy IT "
                    "manager of this week's top vulnerabilities:\n" + facts}],
            )
            return msg.content[0].text.strip()
        except Exception as exc:
            self.say(f"AI summary skipped ({exc}).")
            return ""

    def run(self, state: dict) -> dict:
        today, cfg = state["today"], state["config"]
        items = state["reviewed"]
        limit = cfg["max_items_per_tier"]
        counts = {t: sum(1 for i in items if i["tier"] == t) for t, _ in self.TIERS}

        lines = [
            f"# Weekly Patch Briefing - {today}",
            "",
            f"*Data source: {state['source']} (catalog version {state['catalog_version']})*  ",
            f"*Tech stack watched: {', '.join(cfg['my_stack'])}*",
            "",
            "| Tier | Count |", "|---|---|",
        ]
        lines += [f"| {e} {t} | {counts[t]} |" for t, e in self.TIERS]

        summary = self._ai_summary(items)
        if summary:
            lines += ["", "## AI summary", "", summary]

        for tier, emoji in self.TIERS:
            group = [i for i in items if i["tier"] == tier][:limit]
            if not group:
                continue
            lines += ["", f"## {emoji} {tier}"]
            for i in group:
                lines += [
                    "", f"### {i['cveID']} - {i['vendorProject']} {i['product']} (score {i['score']})",
                    f"**{i['vulnerabilityName']}**  ",
                    i["shortDescription"], "",
                    f"**What to do:** {i['requiredAction']}  ",
                    f"**Deadline (CISA):** {i['dueDate']}", "",
                    "Why it ranked here:",
                ]
                lines += [f"- {r}" for r in i["reasons"]]
                if i["review_note"]:
                    lines.append(f"- *Reviewer: {i['review_note']}*")

        report = "\n".join(lines) + "\n"
        REPORT_DIR.mkdir(exist_ok=True)
        dated = REPORT_DIR / f"briefing-{today}.md"
        dated.write_text(report, encoding="utf-8")
        (REPORT_DIR / "latest.md").write_text(report, encoding="utf-8")
        state["report_path"] = dated
        self.say(f"Wrote {dated.name} and latest.md")
        return state
