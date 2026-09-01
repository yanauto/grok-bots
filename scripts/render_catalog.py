#!/usr/bin/env python3
"""Print a markdown table from data/bots.json. Does not rewrite README.md."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOTS_PATH = ROOT / "data" / "bots.json"
REQUIRED = ("name", "role", "url", "verified")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def load_bots() -> list[dict]:
    bots = json.loads(BOTS_PATH.read_text(encoding="utf-8"))
    if not isinstance(bots, list):
        raise SystemExit("data/bots.json must be an array")
    seen: set[str] = set()
    for i, bot in enumerate(bots):
        missing = [k for k in REQUIRED if k not in bot]
        if missing:
            raise SystemExit(f"bot[{i}] missing fields: {missing}")
        url = bot["url"]
        if not str(url).startswith("https://x.ai/bot/"):
            raise SystemExit(f"bot[{i}] url is not a share link: {url}")
        if not DATE_RE.fullmatch(str(bot["verified"])):
            raise SystemExit(f"bot[{i}] verified must be YYYY-MM-DD")
        if url in seen:
            raise SystemExit(f"duplicate url: {url}")
        seen.add(url)
    return bots


def md_cell(value: str) -> str:
    return (value or "").replace("|", "\\|")


def main() -> None:
    bots = load_bots()
    print(f"{len(bots)} verified bots from {BOTS_PATH.relative_to(ROOT)}.")
    print()
    print("| Name | Role | Share URL | Verified |")
    print("| --- | --- | --- | --- |")
    for bot in bots:
        print(
            "| {name} | {role} | {url} | {verified} |".format(
                name=md_cell(bot["name"]),
                role=md_cell(bot["role"]),
                url=md_cell(bot["url"]),
                verified=md_cell(bot["verified"]),
            )
        )


if __name__ == "__main__":
    main()
