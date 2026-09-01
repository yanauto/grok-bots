#!/usr/bin/env python3
"""Render per-category catalog pages and the homepage index from data/<category>.json."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
CATALOG_DIR = ROOT / "catalog"
HOMEPAGE_PATH = ROOT / "README.md"

REQUIRED = ("name", "author", "role", "url", "verified")

CATEGORIES = (
    ("coding-dev", "Coding / dev", "Apps, code, PRs, shipping, site audits"),
    ("content-writing", "Content / writing", "Copy, slides, SEO briefs, outreach drafts"),
    ("x-social", "X / social", "X briefs, growth, posting, account coaching"),
    ("ops-productivity", "Ops / productivity", "Inbox, calendar, CoS, sales ops, support"),
    ("research-news", "Research / news", "Research, papers, news, competitor diffs"),
    ("shopping-commerce", "Shopping / commerce", "Refunds, shopping, selling, subscriptions"),
    ("home-life", "Home / life", "Home, travel, food, personal life door"),
    ("other", "Other", "Bot craft and anything that does not fit above"),
)

INDEX_RE = re.compile(
    r"<!-- catalog-index:start -->.*?<!-- catalog-index:end -->",
    re.DOTALL,
)


def load_category(slug: str) -> list[dict]:
    path = DATA_DIR / f"{slug}.json"
    if not path.exists():
        raise SystemExit(f"missing {path}")
    bots = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(bots, list):
        raise SystemExit(f"{path} must be an array")
    for i, bot in enumerate(bots):
        missing = [k for k in REQUIRED if k not in bot]
        if missing:
            raise SystemExit(f"{path} bot[{i}] missing fields: {missing}")
        if not str(bot["url"]).startswith("https://x.ai/bot/"):
            raise SystemExit(f"{path} bot[{i}] url is not a share link: {bot['url']}")
    return bots


def load_all() -> dict[str, list[dict]]:
    by_cat: dict[str, list[dict]] = {}
    seen: set[str] = set()
    for slug, _title, _blurb in CATEGORIES:
        bots = load_category(slug)
        for bot in bots:
            url = bot["url"]
            if url in seen:
                raise SystemExit(f"duplicate url across category files: {url}")
            seen.add(url)
        by_cat[slug] = bots
    return by_cat


def md_cell(value: str) -> str:
    return (value or "").replace("|", "\\|")


def render_category_page(slug: str, title: str, blurb: str, bots: list[dict]) -> str:
    lines = [
        f"# {title}",
        "",
        f"{blurb}.",
        "",
        f"Generated from [`data/{slug}.json`](../data/{slug}.json). Edit that file, then run `python3 scripts/render_catalog.py`.",
        "",
        "Verified means the share page loaded and showed Add to Grok Bot. It is not an endorsement.",
        "",
        f"{len(bots)} bots.",
        "",
        "| Name | Author | Role | Share URL | Verified |",
        "| --- | --- | --- | --- | --- |",
    ]
    for bot in bots:
        lines.append(
            "| {name} | {author} | {role} | {url} | {verified} |".format(
                name=md_cell(bot["name"]),
                author=md_cell(bot["author"] or "—"),
                role=md_cell(bot["role"]),
                url=md_cell(bot["url"]),
                verified=md_cell(bot["verified"]),
            )
        )
    lines.append("")
    return "\n".join(lines)


def render_index(by_cat: dict[str, list[dict]]) -> str:
    total = sum(len(v) for v in by_cat.values())
    rows = [
        "<!-- catalog-index:start -->",
        f"{total} verified bots, grouped by use case. Full tables live under [`catalog/`](catalog/). Source lists are [`data/<category>.json`](data/).",
        "",
        "| Category | Count | What lives here |",
        "| --- | ---: | --- |",
    ]
    for slug, title, blurb in CATEGORIES:
        n = len(by_cat[slug])
        rows.append(f"| [{title}](catalog/{slug}.md) | {n} | {blurb} |")
    rows.append("<!-- catalog-index:end -->")
    return "\n".join(rows)


def update_homepage(by_cat: dict[str, list[dict]]) -> None:
    text = HOMEPAGE_PATH.read_text(encoding="utf-8")
    if not INDEX_RE.search(text):
        raise SystemExit("README.md is missing catalog-index markers")
    HOMEPAGE_PATH.write_text(
        INDEX_RE.sub(render_index(by_cat), text, count=1),
        encoding="utf-8",
    )


def main() -> None:
    by_cat = load_all()
    CATALOG_DIR.mkdir(parents=True, exist_ok=True)
    for slug, title, blurb in CATEGORIES:
        (CATALOG_DIR / f"{slug}.md").write_text(
            render_category_page(slug, title, blurb, by_cat[slug]),
            encoding="utf-8",
        )
    update_homepage(by_cat)
    total = sum(len(v) for v in by_cat.values())
    print(f"rendered {total} bots across {len(CATEGORIES)} categories")


if __name__ == "__main__":
    main()
