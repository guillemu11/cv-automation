"""Cross-run deduplication using seen_jobs.json.

The intra-run dedupe (across sources in the same run) is handled by
``discovery/__init__.py``. This module handles cross-run dedupe so we don't
re-analyze and re-insert jobs that were already processed in a prior run.

Storage: a flat JSON dict  { job_id: {"first_seen": "2026-04-10", "source": "indeed"} }
kept in ``data/seen_jobs.json``.
"""
from __future__ import annotations

import json
import logging
from datetime import date
from pathlib import Path

from ..config import settings
from ..discovery.normalize import Job

logger = logging.getLogger(__name__)


def _load(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _save(path: Path, data: dict[str, dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def filter_new(jobs: list[Job]) -> tuple[list[Job], int]:
    """Return only jobs not seen in previous runs. Persists newly seen jobs.

    Returns (new_jobs, skipped_count).
    """
    path = settings.seen_jobs_path
    seen = _load(path)
    today = date.today().isoformat()

    new: list[Job] = []
    skipped = 0
    for job in jobs:
        if job.id in seen:
            skipped += 1
            continue
        seen[job.id] = {"first_seen": today, "source": job.source}
        new.append(job)

    _save(path, seen)
    logger.info("dedupe: %d new, %d skipped (total seen: %d)", len(new), skipped, len(seen))
    return new, skipped
