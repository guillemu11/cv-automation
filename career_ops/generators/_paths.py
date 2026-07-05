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


# Standing rule (set 2026-05-31): every position folder is organised
# día → posición → category. Generators must write into the matching
# subfolder so positions are born organised and nobody reorders by hand.
# The dashboard indexer scans recursively, so these subfolders are
# transparent to file matching.
_CATEGORY_SUBDIRS = {
    "cv_cl": "01_CV_y_Carta",          # CV_* + CL_*
    "deliverables": "02_Deliverables",  # Deliverable_* + landings + decks
    "outreach": "03_Outreach",          # *_Outreach_Pack.docx, Outreach.md, contacts_*
    "application": "04_Aplicacion",     # FORM_*, LINKS_*, README, manifests
}


def job_subdir(job: Job, category: str) -> Path:
    """Return the standard category subfolder inside the job's output dir.

    ``category`` is one of ``cv_cl``, ``deliverables``, ``outreach``,
    ``application`` — mapped to the ``01_``…``04_`` numbered folders. Creates
    it if missing.
    """
    try:
        name = _CATEGORY_SUBDIRS[category]
    except KeyError:
        raise ValueError(
            f"unknown output category {category!r}; "
            f"expected one of {sorted(_CATEGORY_SUBDIRS)}"
        ) from None
    out = job_output_dir(job) / name
    out.mkdir(parents=True, exist_ok=True)
    return out
