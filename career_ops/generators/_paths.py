"""Shared path helper for content generators.

Lives in its own module to avoid circular imports — the package ``__init__``
imports from each generator, so the generators must not import from
``__init__``. Importing from this leaf module is safe.
"""
from __future__ import annotations

import re
from pathlib import Path

from ..config import settings
from ..discovery.normalize import Job


_FOLDER_SANITIZE = re.compile(r'[<>:"/\\|?*]')


def job_output_dir(job: Job) -> Path:
    """Return ``output/<Company> - <Role>/`` for this job, creating it if missing.

    Generators write here instead of the output root so files stay grouped by
    target. The dashboard's ``_index_generated_files`` scans ``output/``
    recursively and matches on company+title substrings inside each filename,
    so the folder name is only for human navigation — filenames inside are
    unchanged.
    """
    raw = f"{job.company} - {job.title}"
    safe = _FOLDER_SANITIZE.sub("", raw).strip()
    safe = re.sub(r"\s+", " ", safe)[:80] or "untitled"
    out = settings.output_dir / safe
    out.mkdir(parents=True, exist_ok=True)
    return out
