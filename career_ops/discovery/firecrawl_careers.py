"""Discovery via Firecrawl on career pages of 25+ target Dubai employers.

Firecrawl's ``/extract`` endpoint takes a URL + a JSON schema and returns
structured data. We ask it to return a list of current openings with title,
location, department, apply URL. Each result becomes a Job.

For companies where extract fails (heavy JS, login walls, ATS iframes), we
fall back to ``/scrape`` and rely on the analyzer to ignore junk.
"""
from __future__ import annotations

import logging
from typing import Any

from ..config import settings
from .normalize import Job

logger = logging.getLogger(__name__)

# Each entry: (company, careers_url).
# Keep this list maintained — it is the main lever for career-page coverage.
TARGET_COMPANIES: list[tuple[str, str]] = [
    ("Chalhoub Group", "https://careers.chalhoubgroup.com/en/all-jobs"),
    ("L'Oréal Middle East", "https://careers.loreal.com/en_US/jobs/SearchJobs/?3_18_3=11430"),
    ("Estée Lauder ME", "https://www.elcompanies.com/en/careers/search-jobs"),
    ("Unilever Gulf", "https://careers.unilever.com/search-jobs/United%20Arab%20Emirates"),
    ("P&G Gulf", "https://www.pgcareers.com/global/en/search-results?keywords=%22United%20Arab%20Emirates%22"),
    ("Nestlé Middle East", "https://www.nestle.com/jobs/search-jobs?country=United%20Arab%20Emirates"),
    ("Mars", "https://www.mars.com/careers/jobs?location=United%20Arab%20Emirates"),
    ("Reckitt", "https://careers.reckitt.com/global/en/search-results?keywords=Dubai"),
    ("Al Futtaim", "https://www.alfuttaimcareers.com/search/?q=&locationsearch=Dubai"),
    ("Majid Al Futtaim", "https://careers.majidalfuttaim.com/jobs"),
    ("Landmark Group", "https://www.landmarkgroup.com/en/careers"),
    ("Apparel Group", "https://careers.apparelglobal.com/"),
    ("Noon", "https://jobs.noon.com/"),
    ("Talabat", "https://careers.talabat.com/jobs/search?location=United%20Arab%20Emirates"),
    ("Careem", "https://www.careem.com/careers/"),
    ("Deliveroo UAE", "https://careers.deliveroo.co.uk/?country=ae"),
    ("Alshaya Group", "https://careers.alshaya.com/"),
    ("Azadea Group", "https://www.azadea.com/careers/"),
    ("PepsiCo MENA", "https://www.pepsicojobs.com/main/jobs?location=United%20Arab%20Emirates"),
    ("Coca-Cola (CCBA/HBC)", "https://careers.coca-colacompany.com/search-jobs/United%20Arab%20Emirates"),
    ("Mondelez Middle East", "https://www.mondelezinternational.com/careers/"),
    ("Amazon UAE", "https://www.amazon.jobs/en/locations/united-arab-emirates"),
    ("Namshi", "https://www.namshi.com/uae-en/careers/"),
    ("LVMH Middle East", "https://www.lvmh.com/talents/join-us/our-job-offers/?region=Middle%20East"),
    ("Kibsons", "https://kibsons.com/careers/"),
]

_EXTRACTION_SCHEMA = {
    "type": "object",
    "properties": {
        "jobs": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "location": {"type": "string"},
                    "department": {"type": "string"},
                    "apply_url": {"type": "string"},
                    "short_description": {"type": "string"},
                },
                "required": ["title"],
            },
        }
    },
    "required": ["jobs"],
}

_EXTRACTION_PROMPT = (
    "Extract ALL currently open job postings visible on this career page. "
    "For each, return title, location (city/country), department if shown, "
    "the direct apply URL, and a one-line description if available. "
    "Ignore navigation, employee benefits sections, and generic copy. "
    "Only return actual open positions."
)


def _matches_query(title: str, queries: list[str]) -> bool:
    t = (title or "").lower()
    return any(q.lower() in t for q in queries) if queries else True


def _is_uae(location: str | None) -> bool:
    if not location:
        return True  # assume UAE if not specified (many GCC pages filter upstream)
    loc = location.lower()
    return any(needle in loc for needle in [
        "uae", "united arab emirates", "dubai", "abu dhabi", "sharjah", "ajman", "ras al khaimah", "fujairah"
    ])


def fetch(
    queries: list[str],
    locations: list[str],
    limit: int = 30,
    hours_old: int = 48,
) -> list[Job]:
    if not settings.firecrawl_api_key:
        logger.info("FIRECRAWL_API_KEY not set — skipping Firecrawl source")
        return []

    try:
        from firecrawl import FirecrawlApp  # type: ignore
    except ImportError:
        logger.warning("firecrawl-py not installed — skipping Firecrawl source")
        return []

    app = FirecrawlApp(api_key=settings.firecrawl_api_key)
    out: list[Job] = []

    for company, url in TARGET_COMPANIES:
        try:
            # firecrawl-py >=1.6 exposes extract() with schema + prompt
            result: dict[str, Any] = app.extract(
                urls=[url],
                params={
                    "prompt": _EXTRACTION_PROMPT,
                    "schema": _EXTRACTION_SCHEMA,
                },
            )
        except Exception as exc:  # noqa: BLE001
            logger.warning("firecrawl extract failed for %s (%s): %s", company, url, exc)
            continue

        data = result.get("data") if isinstance(result, dict) else None
        jobs_payload = (data or {}).get("jobs") or []

        for item in jobs_payload:
            try:
                title = (item.get("title") or "").strip()
                if not title:
                    continue
                if not _matches_query(title, queries):
                    continue
                loc = (item.get("location") or "").strip()
                if loc and not _is_uae(loc):
                    continue

                job = Job.build(
                    title=title,
                    company=company,
                    location=loc or "Dubai, United Arab Emirates",
                    url=(item.get("apply_url") or url).strip(),
                    source="firecrawl",
                    description=item.get("short_description") or "",
                    raw={"career_page": url, "department": item.get("department")},
                )
                out.append(job)
            except Exception as exc:  # noqa: BLE001
                logger.debug("firecrawl item mapping failed for %s: %s", company, exc)
                continue

    logger.info("firecrawl fetched total=%d across %d companies", len(out), len(TARGET_COMPANIES))
    return out
