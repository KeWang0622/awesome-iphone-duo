#!/usr/bin/env python3
"""Check catalog integrity and local Markdown links; no network required."""
import datetime
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build_readme import ROOT, render


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def anchor(text):
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    return re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-")


def main():
    apps = json.loads((ROOT / "data/apps.json").read_text())
    categories = json.loads((ROOT / "data/categories.json").read_text())
    category_names = {c["name"] for c in categories}
    require(len(category_names) == len(categories), "Duplicate category")
    for c in categories:
        require(anchor(c["name"]) == c["id"], f'Wrong category anchor: {c["name"]}')
        require(any(a["category"] == c["name"] for a in apps), f'Empty category: {c["name"]}')
    seen = {"id": set(), "name": set(), "url": set()}
    for app in apps:
        for key in ("id", "name", "category", "url", "description", "evidence_url", "evidence_note", "tier", "availability", "checked_at"):
            require(isinstance(app.get(key), str) and app[key].strip(), f'Missing {key}: {app.get("name")}')
        for key, values in seen.items():
            value = app[key].casefold().rstrip("/")
            require(value not in values, f'Duplicate {key}: {app[key]}')
            values.add(value)
        require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", app["id"]), f'Invalid id: {app["id"]}')
        require(app["category"] in category_names, f'Unknown category: {app["name"]}')
        require(app["tier"] in {"primary", "curated", "reported", "community"}, f'Unknown evidence: {app["name"]}')
        require(app["availability"] in {"available", "source-build", "beta", "announced", "unconfirmed"}, f'Unknown availability: {app["name"]}')
        require(app["description"].endswith("."), f'Description needs final period: {app["name"]}')
        date = datetime.date.fromisoformat(app["checked_at"])
        require(date <= datetime.date.today(), f'Future check date: {app["name"]}')
        for key in ("url", "evidence_url", "source_url"):
            if key in app:
                parts = urlsplit(app[key])
                require(parts.scheme == "https" and parts.netloc, f'Invalid {key}: {app["name"]}')
                require(not any(p in parts.query.lower() for p in ("utm_", "afid=", "affiliate=")), f'Tracking link: {app["name"]}')
        if app["availability"] in {"beta", "announced", "unconfirmed"}:
            require(app["category"] == "Previews and watchlist", f'Preview in released section: {app["name"]}')
        if app["availability"] == "source-build":
            require(app["category"] == "Source projects and experiments", f'Source build in released section: {app["name"]}')
    require((ROOT / "README.md").read_text() == render(), "README is stale; run python3 scripts/build_readme.py")
    for path in ROOT.rglob("*.md"):
        # These fragments are rendered into README.md and use its relative paths.
        if path in {ROOT / "docs/readme-intro.md", ROOT / "docs/readme-outro.md"}:
            continue
        text = path.read_text()
        require("\t" not in text, f'Tab character in {path}')
        for dest in re.findall(r"\]\(([^)\s]+)\)", text):
            if urlsplit(dest).scheme or dest.startswith("//"):
                continue
            filename, _, fragment = unquote(dest).partition("#")
            target = (path.parent / filename).resolve() if filename else path
            require(target.exists(), f'Broken local link in {path.name}: {dest}')
            if fragment and target.suffix == ".md":
                headings = {anchor(h) for h in re.findall(r"^#{1,6} (.+)$", target.read_text(), re.M)}
                require(fragment in headings, f'Broken anchor in {path.name}: {dest}')
    print(f'OK: {len(apps)} unique entries, {len(categories)} categories, evidence fields, README and local links.')


if __name__ == "__main__":
    main()
