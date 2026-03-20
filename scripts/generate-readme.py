#!/usr/bin/env python3
"""
Regenerate README.md from all service JSON files.
"""
import json
from pathlib import Path
from collections import defaultdict
import datetime

REPO_ROOT = Path(__file__).parent.parent
SERVICES_DIR = REPO_ROOT / "services"

CATEGORY_LABELS = {
    "email": "📧 Email",
    "calendar": "📅 Calendar & Scheduling",
    "browser": "🌐 Browser & Web Automation",
    "crm": "👥 CRM & Sales",
    "support": "🎧 Support & Ticketing",
    "messaging": "💬 Messaging & Chat",
    "voice": "🎙️ Voice",
    "marketplace": "🏪 Agent Marketplaces & Directories",
    "orchestration": "⚙️ Orchestration & Protocols",
    "workflow": "🔄 Workflow Automation",
    "tool-gateway": "🔌 Tool Gateways & MCP",
}

SCORE_LABELS = {5: "★★★★★", 4: "★★★★☆", 3: "★★★☆☆", 2: "★★☆☆☆", 1: "★☆☆☆☆"}

def load_services():
    by_category = defaultdict(list)
    for f in sorted(SERVICES_DIR.rglob("*.json")):
        try:
            data = json.loads(f.read_text())
            by_category[data["category"]].append(data)
        except Exception as e:
            print(f"Error loading {f}: {e}")
    return by_category

def render_table(services):
    rows = []
    rows.append("| Service | Score | Protocols | Capabilities | Auth | Pricing |")
    rows.append("|---------|-------|-----------|--------------|------|---------|")
    for s in sorted(services, key=lambda x: -x["agent_native_score"]):
        name = f"[{s['name']}]({s['url']})"
        score = SCORE_LABELS.get(s["agent_native_score"], "?")
        protocols = ", ".join(s.get("protocols", [])[:3]) or "—"
        caps = ", ".join(s.get("capabilities", [])[:3]) or "—"
        auth = s.get("auth", "—")
        pricing = s.get("pricing", "—")
        rows.append(f"| {name} | {score} | {protocols} | {caps} | {auth} | {pricing} |")
    return "\n".join(rows)

def main():
    by_category = load_services()
    total = sum(len(v) for v in by_category.values())
    today = datetime.date.today().isoformat()

    sections = [f"""# Agent Native Hub

> A continuously-updated catalog of services, tools, and platforms built specifically for AI agents to use.

**{total} services** across {len(by_category)} categories | Last updated: {today}

Maintained by [Harper Labs](https://github.com/harper-labs) | Contributions welcome

## What belongs here

Services where an AI agent is the **primary user** — not a human with an AI assistant bolted on.
A service belongs here if an agent can directly send email, schedule meetings, browse the web,
update CRM records, or take other real-world actions through it.

## Agent-Native Score

- ★★★★★ Built specifically for agents, full autonomous action
- ★★★★☆ Agent-first with some human UI
- ★★★☆☆ Usable by agents via API, not designed primarily for them
- ★★☆☆☆ Agent-adjacent with some automation
- ★☆☆☆☆ Mostly human-first

---
"""]

    for cat, label in CATEGORY_LABELS.items():
        services = by_category.get(cat, [])
        if not services:
            continue
        sections.append(f"## {label}\n")
        sections.append(render_table(services))
        sections.append("")

    sections.append("""---

## Contributing

1. Fork this repo
2. Add a JSON file in `services/<category>/` following `schema/service.schema.json`
3. Run `python3 scripts/generate-readme.py`
4. Submit a PR

## Discovery

This catalog is updated automatically 2x daily by a search agent that scans for new agent-native services.
Discovered candidates go into `staging/` for review before promotion.

## License

MIT — Harper Labs
""")

    readme = "\n".join(sections)
    (REPO_ROOT / "README.md").write_text(readme)
    print(f"README generated: {total} services across {len(by_category)} categories")

if __name__ == "__main__":
    main()
