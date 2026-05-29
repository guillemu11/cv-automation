"""Rescue jobs from Notion into data/scored_jobs.json (one-shot migration).

Why: we are moving Notion out of the pipeline and making the dashboard
(`scored_jobs.json`) the source of truth. Prior runs inserted jobs into Notion
that never made it into the local JSON, so we need to pull them back before
disconnecting Notion writes.

Merge policy: **local wins on every field**. Jobs that exist only in Notion are
added. Jobs that exist in both are left untouched (local version — including
`status` — is preserved, because the local status reflects real actions like
"CV Ready" from PDFs already generated).

Usage:
    python scripts/import_from_notion.py            # dry run (default)
    python scripts/import_from_notion.py --apply    # write changes
"""
from __future__ import annotations

import argparse
import json
import logging
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import httpx

# allow running as a loose script from the repo root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from career_ops.config import settings  # noqa: E402

logger = logging.getLogger("import_from_notion")

NOTION_API = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

# Reverse of _SOURCE_MAP in notion_sync.py — Notion "Source" select → local source key.
_SOURCE_REVERSE = {
    "Indeed": "indeed",
    "LinkedIn": "linkedin",
    "Google Jobs": "google_jobs",
    "Apify": "apify",
    "Firecrawl": "firecrawl",
}


def _rt_plain(prop: dict[str, Any]) -> str:
    """Concatenate all rich_text chunks into a single string."""
    chunks = prop.get("rich_text") or prop.get("title") or []
    return "".join(c.get("plain_text", "") for c in chunks)


def _select(prop: dict[str, Any]) -> str:
    sel = prop.get("select")
    if sel and isinstance(sel, dict):
        return sel.get("name", "") or ""
    return ""


def _number(prop: dict[str, Any]) -> float | int | None:
    return prop.get("number")


def _url(prop: dict[str, Any]) -> str:
    return prop.get("url") or ""


def _split_csv(text: str) -> list[str]:
    """Parse a comma-joined rich_text value back into a list of strings."""
    if not text:
        return []
    return [part.strip() for part in text.split(",") if part.strip()]


def _split_red_flags(text: str) -> list[str]:
    """Red flags were joined with ' | ' — see notion_sync._build_page_properties."""
    if not text:
        return []
    return [part.strip() for part in text.split("|") if part.strip()]


def _fetch_all_pages(db_id: str) -> list[dict[str, Any]]:
    headers = {
        "Authorization": f"Bearer {settings.notion_token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }
    pages: list[dict[str, Any]] = []
    cursor: str | None = None
    while True:
        body: dict[str, Any] = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        resp = httpx.post(
            f"{NOTION_API}/databases/{db_id}/query",
            headers=headers,
            json=body,
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()
        pages.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return pages


def _page_to_record(page: dict[str, Any]) -> dict[str, Any] | None:
    """Map a Notion page into a scored_jobs.json record.

    Returns None if the page has no Job ID (shouldn't happen, but defensive).
    """
    props = page.get("properties", {})

    job_id = _rt_plain(props.get("Job ID", {})).strip()
    if not job_id:
        return None

    title = _rt_plain(props.get("Job Title", {})).strip()
    company = _rt_plain(props.get("Company", {})).strip()
    source_label = _select(props.get("Source", {}))
    source = _SOURCE_REVERSE.get(source_label, source_label.lower() or "notion")

    score_raw = _number(props.get("Score", {}))
    # Notion stores score as number; keep original type if possible
    ai_score = int(score_raw) if isinstance(score_raw, (int, float)) else 0

    tier = _select(props.get("Priority", {})) or "Warm"
    status = _select(props.get("Status", {})) or "Analyzed"

    record: dict[str, Any] = {
        "id": job_id,
        "title": title,
        "company": company,
        "location": "",  # not stored in Notion
        "url": _url(props.get("Link", {})),
        "source": source,
        "description": "",  # full JD not reliably reconstructible from Notion
        "salary_raw": _rt_plain(props.get("Salary Range", {})) or None,
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": None,
        "raw": {"imported_from": "notion"},
        "ai_score": ai_score,
        "ai_tier": tier,
        "reasoning": _rt_plain(props.get("Analysis", {})),
        "skills_match": _split_csv(_rt_plain(props.get("Skills Match", {}))),
        "missing_skills": _split_csv(_rt_plain(props.get("Missing Skills", {}))),
        "sector_fit": _rt_plain(props.get("Sector Fit", {})),
        "seniority_fit": _rt_plain(props.get("Seniority Fit", {})),
        "red_flags": _split_red_flags(_rt_plain(props.get("Red Flags", {}))),
        "ats_keywords": _split_csv(_rt_plain(props.get("ATS Keywords", {}))),
        "status": status,
    }
    return record


def _load_local_jobs(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            logger.warning("scored_jobs.json is invalid JSON — treating as empty")
            return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes to scored_jobs.json (default is dry run)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show details for every job that would be imported",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    if not settings.notion_token or not settings.notion_db_jobs:
        logger.error("NOTION_TOKEN and NOTION_DB_JOBS must be set in .env")
        return 1

    target_path = settings.data_dir / "scored_jobs.json"
    local = _load_local_jobs(target_path)
    local_ids = {rec.get("id") for rec in local if rec.get("id")}
    logger.info("local: %d jobs in %s", len(local), target_path.name)

    logger.info("fetching Notion pages from DB %s...", settings.notion_db_jobs[:8])
    pages = _fetch_all_pages(settings.notion_db_jobs)
    logger.info("notion: fetched %d pages", len(pages))

    notion_records: list[dict[str, Any]] = []
    skipped_no_id = 0
    for page in pages:
        rec = _page_to_record(page)
        if rec is None:
            skipped_no_id += 1
            continue
        notion_records.append(rec)

    notion_ids = {rec["id"] for rec in notion_records}
    only_in_notion = notion_ids - local_ids
    only_in_local = local_ids - notion_ids
    in_both = notion_ids & local_ids

    to_add = [rec for rec in notion_records if rec["id"] in only_in_notion]

    print()
    print("=" * 60)
    print("  NOTION -> LOCAL IMPORT PREVIEW")
    print("=" * 60)
    print(f"  Notion pages fetched:     {len(pages)}")
    print(f"  Notion pages w/o Job ID:  {skipped_no_id}")
    print(f"  Unique Notion jobs:       {len(notion_records)}")
    print(f"  Local jobs currently:     {len(local)}")
    print()
    print(f"  Only in Notion (to add):  {len(only_in_notion)}")
    print(f"  Only in local (kept):     {len(only_in_local)}")
    print(f"  In both (local wins):     {len(in_both)}")
    print("-" * 60)

    if to_add:
        tier_counts: dict[str, int] = {}
        source_counts: dict[str, int] = {}
        for rec in to_add:
            tier_counts[rec["ai_tier"]] = tier_counts.get(rec["ai_tier"], 0) + 1
            source_counts[rec["source"]] = source_counts.get(rec["source"], 0) + 1
        print("  New jobs by tier:")
        for tier, count in sorted(tier_counts.items(), key=lambda x: -x[1]):
            print(f"    {tier:12s} {count}")
        print("  New jobs by source:")
        for src, count in sorted(source_counts.items(), key=lambda x: -x[1]):
            print(f"    {src:12s} {count}")

    if args.verbose and to_add:
        print("-" * 60)
        print("  Jobs to import:")
        for rec in to_add:
            print(
                f"    [{rec['ai_tier']:5s}] {rec['ai_score']:3d}  "
                f"{rec['title'][:50]:50s}  @  {rec['company'][:30]}"
            )

    print("=" * 60)

    if not args.apply:
        print()
        print("  DRY RUN - no changes written. Re-run with --apply to commit.")
        return 0

    if not to_add:
        print()
        print("  Nothing to import. Local is already up to date.")
        return 0

    # Backup before writing
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = target_path.with_suffix(f".json.bak-{ts}")
    if target_path.exists():
        shutil.copy2(target_path, backup)
        logger.info("backup written: %s", backup.name)

    merged = list(local) + to_add
    with target_path.open("w", encoding="utf-8") as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)

    print()
    print(f"  APPLIED: added {len(to_add)} jobs. Local total is now {len(merged)}.")
    print(f"  Backup: {backup.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
