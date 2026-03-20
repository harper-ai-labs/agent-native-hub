#!/usr/bin/env python3
"""
Review staged candidates and promote verified ones to services/.
"""
import json
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
STAGING_DIR = REPO_ROOT / "staging"
SERVICES_DIR = REPO_ROOT / "services"

def main():
    candidates = list(STAGING_DIR.glob("*.json"))
    if not candidates:
        print("No staged candidates.")
        return

    print(f"{len(candidates)} staged candidates:")
    for f in candidates:
        data = json.loads(f.read_text())
        print(f"\n{'='*50}")
        print(f"Name: {data['name']}")
        print(f"Category: {data['category']}")
        print(f"Score: {data['agent_native_score']}/5")
        print(f"URL: {data['url']}")
        print(f"Description: {data['description'][:100]}...")
        print(f"Source: {data.get('source', 'N/A')}")
        print(f"File: {f.name}")

    print(f"\nTo promote: mv staging/<file>.json services/<category>/<file>.json")
    print("Then run: python3 scripts/generate-readme.py")

if __name__ == "__main__":
    main()
