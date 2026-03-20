#!/usr/bin/env python3
"""
Agent Native Hub — Discovery Script
Searches the web for new agent-native services and updates the repository.
Run 2x daily via cron.
"""

import json
import os
import subprocess
import datetime
import time
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SERVICES_DIR = REPO_ROOT / "services"
STAGING_DIR = REPO_ROOT / "staging"
STAGING_DIR.mkdir(exist_ok=True)

TODAY = datetime.date.today().isoformat()

# Search queries to run
SEARCH_QUERIES = [
    "agent-native service AI agents 2026",
    "MCP server new release agent tools",
    "\"built for AI agents\" service API",
    "\"agent-first\" application launch 2026",
    "\"AI agent\" email calendar browser service",
    "A2A protocol agent services directory",
    "agent marketplace new platform 2026",
    "\"agent-native\" app service tool",
    "AI agent CRM support voice tool",
    "\"for AI agents\" API service launch",
]

# Known services to skip (already in repo)
def get_known_services():
    known = set()
    for f in SERVICES_DIR.rglob("*.json"):
        try:
            data = json.loads(f.read_text())
            known.add(data.get("url", "").lower().rstrip("/"))
            known.add(data.get("name", "").lower())
        except:
            pass
    return known

def search_web(query):
    """Use web_search equivalent — calls out to Kiko's web search."""
    # In the cron context, we'll use the web_search tool via a subagent
    # This script outputs queries; the cron agent does the actual searching
    return query

def score_service(name, description, url):
    """Heuristic scoring based on description keywords."""
    text = (name + " " + description).lower()
    score = 1

    strong_signals = ["built for ai agents", "agent-native", "agent-first", "for ai agents", "mcp server", "agent inbox"]
    medium_signals = ["ai agent", "autonomous agent", "agentic", "agent sdk", "agent api"]
    weak_signals = ["ai-powered", "ai assistant", "automation", "api-first"]

    if any(s in text for s in strong_signals):
        score = 5
    elif any(s in text for s in medium_signals):
        score = 3
    elif any(s in text for s in weak_signals):
        score = 2

    return score

def save_candidate(name, url, category, description, source_url):
    """Save a discovered candidate to staging."""
    safe_name = re.sub(r'[^a-z0-9-]', '-', name.lower()).strip('-')
    out_file = STAGING_DIR / f"{safe_name}.json"

    candidate = {
        "name": name,
        "vendor": "",
        "category": category,
        "description": description,
        "agent_native_score": score_service(name, description, url),
        "protocols": [],
        "capabilities": [],
        "interaction_model": "unknown",
        "auth": "unknown",
        "pricing": "unknown",
        "open_source": False,
        "url": url,
        "source": source_url,
        "verified": False,
        "last_verified": TODAY,
        "notes": "AUTO-DISCOVERED — needs review",
        "tags": [category]
    }

    out_file.write_text(json.dumps(candidate, indent=2))
    return out_file

def main():
    print(f"Agent Native Hub Discovery — {TODAY}")
    known = get_known_services()
    print(f"Known services: {len(known)}")

    print("\nSearch queries to run:")
    for q in SEARCH_QUERIES:
        print(f"  - {q}")

    print("\nNote: This script outputs the search strategy.")
    print("The cron agent performs actual web searches and calls save_candidate() for discoveries.")
    print(f"Staging dir: {STAGING_DIR}")
    print("Run validate.py to review and promote staged candidates.")

if __name__ == "__main__":
    main()
