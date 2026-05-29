"""Normalized Job schema + stable hashing used across all discovery sources."""
from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass, field
from datetime import date
from typing import Any, Literal

Source = Literal["indeed", "linkedin", "glassdoor", "zip_recruiter", "google_jobs", "apify", "firecrawl"]


_WS_RE = re.compile(r"\s+")
_NON_ALNUM_RE = re.compile(r"[^a-z0-9 ]+")


def _norm(s: str | None) -> str:
    """Lowercase, strip, collapse whitespace, drop punctuation — for hashing."""
    if not s:
        return ""
    s = s.lower().strip()
    s = _NON_ALNUM_RE.sub(" ", s)
    s = _WS_RE.sub(" ", s)
    return s.strip()


def _city(location: str | None) -> str:
    """Extract just the city component for hashing.

    'Dubai, UAE' → 'dubai'
    'Dubai, United Arab Emirates' → 'dubai'
    'Abu Dhabi - UAE' → 'abu dhabi'

    This keeps cross-source dedupe robust against country-name variants.
    """
    if not location:
        return ""
    first = re.split(r"[,;\-·•|]", location, maxsplit=1)[0]
    return _norm(first)


def job_hash(title: str, company: str, location: str) -> str:
    """Stable hash for dedupe. Same job from different sources → same id.

    Uses city only (not full location) so 'Dubai, UAE' and 'Dubai, United
    Arab Emirates' collapse to the same hash.
    """
    key = f"{_norm(title)}|{_norm(company)}|{_city(location)}"
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:16]


@dataclass
class Job:
    id: str
    title: str
    company: str
    location: str
    url: str
    source: Source
    description: str = ""
    salary_raw: str | None = None
    salary_aed_min: int | None = None
    salary_aed_max: int | None = None
    posted_date: date | None = None
    raw: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def build(
        cls,
        *,
        title: str,
        company: str,
        location: str,
        url: str,
        source: Source,
        description: str = "",
        salary_raw: str | None = None,
        salary_aed_min: int | None = None,
        salary_aed_max: int | None = None,
        posted_date: date | None = None,
        raw: dict[str, Any] | None = None,
    ) -> "Job":
        return cls(
            id=job_hash(title, company, location),
            title=(title or "").strip(),
            company=(company or "").strip(),
            location=(location or "").strip(),
            url=(url or "").strip(),
            source=source,
            description=description or "",
            salary_raw=salary_raw,
            salary_aed_min=salary_aed_min,
            salary_aed_max=salary_aed_max,
            posted_date=posted_date,
            raw=raw or {},
        )

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        if self.posted_date:
            d["posted_date"] = self.posted_date.isoformat()
        return d
