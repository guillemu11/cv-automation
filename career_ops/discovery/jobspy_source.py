"""Discovery via python-jobspy (Indeed, LinkedIn, Glassdoor, ZipRecruiter).

jobspy returns a pandas DataFrame with a fixed column set:
    title, company, location, job_url, description, date_posted,
    min_amount, max_amount, currency, interval, site, ...

We iterate queries × sites sequentially (jobspy already parallelizes
internally per site) and map each row to the common Job schema. Salaries are
converted to AED using the table in blacklist.yaml.
"""
from __future__ import annotations

import logging
import math
from datetime import date
from typing import Any

from ..config import settings
from .normalize import Job, Source

logger = logging.getLogger(__name__)

# Sites jobspy supports with decent UAE coverage.
# Glassdoor and ZipRecruiter don't support UAE ("Glassdoor is not available
# for UNITEDARABEMIRATES").
# Which of these actually run is controlled by settings.jobspy_sites
# (env JOBSPY_SITES), Indeed-only by default — LinkedIn blocks scrapers hard and
# Paula's search is Indeed-only. See _sites().
_ALL_SITES: list[tuple[str, Source]] = [
    ("indeed", "indeed"),
    ("linkedin", "linkedin"),
]


def _sites() -> list[tuple[str, Source]]:
    """Sites to scrape, filtered by settings.jobspy_sites (Indeed-only default)."""
    wanted = settings.jobspy_sites
    return [(name, src) for name, src in _ALL_SITES if name in wanted]

_INTERVAL_TO_MONTHLY = {
    "yearly": 1 / 12,
    "annually": 1 / 12,
    "monthly": 1.0,
    "weekly": 52 / 12,
    "daily": 365 / 12,
    "hourly": (40 * 52) / 12,  # assume 40h/week
}


def _to_monthly_aed(amount: float | None, currency: str | None, interval: str | None) -> int | None:
    if amount is None or (isinstance(amount, float) and math.isnan(amount)):
        return None
    rate = settings.currency_to_aed.get((currency or "AED").upper(), 1.0 if (currency or "AED").upper() == "AED" else None)
    if rate is None:
        return None
    multiplier = _INTERVAL_TO_MONTHLY.get((interval or "monthly").lower(), 1.0)
    return int(round(amount * rate * multiplier))


def _parse_date(val: Any) -> date | None:
    if val is None:
        return None
    try:
        # jobspy returns pandas Timestamp or str
        if hasattr(val, "date"):
            return val.date()
        if isinstance(val, str) and val:
            return date.fromisoformat(val[:10])
    except Exception:
        return None
    return None


def fetch(
    queries: list[str],
    locations: list[str],
    limit: int = 30,
    hours_old: int = 48,
) -> list[Job]:
    try:
        from jobspy import scrape_jobs  # type: ignore
    except ImportError:
        logger.warning("python-jobspy not installed — skipping jobspy source")
        return []

    out: list[Job] = []
    primary_location = locations[0] if locations else "Dubai, United Arab Emirates"
    sites = _sites()
    if not sites:
        logger.warning("jobspy: no sites enabled in JOBSPY_SITES — skipping")
        return []

    for site_name, source in sites:
        for query in queries:
            kwargs: dict[str, Any] = {
                "site_name": [site_name],
                "search_term": query,
                "location": primary_location,
                "results_wanted": limit,
                "hours_old": hours_old,
                "verbose": 0,
            }
            if site_name == "indeed":
                kwargs["country_indeed"] = "United Arab Emirates"
            try:
                df = scrape_jobs(**kwargs)
            except Exception as exc:  # noqa: BLE001
                logger.warning("jobspy %s query=%r failed: %s", site_name, query, exc)
                continue

            if df is None or df.empty:
                continue

            for _, row in df.iterrows():
                try:
                    salary_min = _to_monthly_aed(
                        row.get("min_amount"), row.get("currency"), row.get("interval")
                    )
                    salary_max = _to_monthly_aed(
                        row.get("max_amount"), row.get("currency"), row.get("interval")
                    )
                    salary_raw = None
                    if row.get("min_amount") or row.get("max_amount"):
                        salary_raw = f"{row.get('currency','?')} {row.get('min_amount','?')}–{row.get('max_amount','?')} / {row.get('interval','?')}"

                    job = Job.build(
                        title=str(row.get("title") or ""),
                        company=str(row.get("company") or ""),
                        location=str(row.get("location") or primary_location),
                        url=str(row.get("job_url") or ""),
                        source=source,
                        description=str(row.get("description") or ""),
                        salary_raw=salary_raw,
                        salary_aed_min=salary_min,
                        salary_aed_max=salary_max,
                        posted_date=_parse_date(row.get("date_posted")),
                        raw={
                            "site": site_name,
                            "query": query,
                            "job_type": row.get("job_type"),
                        },
                    )
                    if job.title and job.company:
                        out.append(job)
                except Exception as exc:  # noqa: BLE001
                    logger.debug("jobspy row mapping failed: %s", exc)
                    continue

    logger.info("jobspy fetched total=%d across %d sites × %d queries", len(out), len(sites), len(queries))
    return out
