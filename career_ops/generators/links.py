"""Per-job external-link sidecar (e.g. deployed Vercel landing URLs).

External links are not files, so the dashboard's ``output/`` walk can't discover
them like it does CVs or deliverable PDFs. This module writes a small JSON sidecar
next to a job's generated files — ``LINKS_Paula_<Company>_<Role>.json`` — which the
dashboard reads via the same company-substring matcher it uses for everything else.

Shape on disk::

    [{"label": "Frizz Forecast", "url": "https://paula-pitch-c.vercel.app"}]

Call :func:`register_link` whenever a landing is deployed (the deploy step), so the
link attaches to the dashboard automatically, no manual step.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

_FILENAME_SANITIZE = re.compile(r'[<>:"/\\|?*&]')


def _stem_key(value: str) -> str:
    """Sanitise a company/title the same way generated filenames are keyed."""
    return _FILENAME_SANITIZE.sub("", value).strip().replace(" ", "_")[:50]


def links_sidecar_path(job_dir: Path, company: str, title: str) -> Path:
    """Path of the links sidecar for a job folder (not created)."""
    return job_dir / f"LINKS_Paula_{_stem_key(company)}_{_stem_key(title)}.json"


def load_links(path: Path) -> list[dict]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
    return data if isinstance(data, list) else []


def register_link(job_dir: Path, company: str, title: str,
                  label: str, url: str) -> Path:
    """Add (or update) a ``{label, url}`` entry in the job's links sidecar.

    Idempotent: dedupes by URL. If the URL already exists its label is refreshed.
    Returns the sidecar path written.
    """
    job_dir.mkdir(parents=True, exist_ok=True)
    path = links_sidecar_path(job_dir, company, title)
    links = load_links(path)
    for entry in links:
        if entry.get("url") == url:
            entry["label"] = label
            break
    else:
        links.append({"label": label, "url": url})
    path.write_text(json.dumps(links, indent=2, ensure_ascii=False), encoding="utf-8")
    return path
