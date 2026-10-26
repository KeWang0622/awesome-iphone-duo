#!/usr/bin/env python3
"""Build the catalog README using only the Python standard library."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABELS = {"primary": "Primary", "curated": "Apple collection", "reported": "Reported", "community": "Community"}
STATUS = {"source-build": "Build from source", "beta": "Beta", "announced": "Announced", "unconfirmed": "Availability unconfirmed"}


def render():
    apps = json.loads((ROOT / "data/apps.json").read_text())
    categories = json.loads((ROOT / "data/categories.json").read_text())
    intro = (ROOT / "docs/readme-intro.md").read_text().rstrip()
    intro = intro.replace("{{COUNT}}", str(len(apps)))
    sections = [intro, "## Contents\n\n" + "\n".join(f'- [{c["name"]}](#{c["id"]})' for c in categories) + "\n- [References and related lists](#references-and-related-lists)\n- [Contributing](#contributing)"]
    for c in categories:
        entries = sorted((a for a in apps if a["category"] == c["name"]), key=lambda a: a["name"].casefold())
        lines = [f'## {c["name"]}', c["description"]]
        for a in entries:
            tags = [f'[{LABELS[a["tier"]]}]({a["evidence_url"]})']
            for extra in a.get("additional_evidence_urls", []):
                tags.append(f'[Details]({extra})')
            if a["availability"] in STATUS:
                tags.append(STATUS[a["availability"]])
            if a.get("source_url"):
                tags.append(f'[Source]({a["source_url"]})')
            lines.append(f'- [{a["name"]}]({a["url"]}) - {a["description"]} ' + " · ".join(tags) + ".")
        sections.append("\n\n".join(lines[:2]) + "\n\n" + "\n".join(lines[2:]))
    sections.append((ROOT / "docs/readme-outro.md").read_text().strip())
    return "\n\n".join(sections) + "\n"


if __name__ == "__main__":
    (ROOT / "README.md").write_text(render())
    print("Generated README.md")
