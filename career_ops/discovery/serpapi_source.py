"""Discovery via SerpAPI Google Jobs.

Google Jobs aggregates listings from Bayt, GulfTalent, Naukrigulf, Monster Gulf,
Laimoon and career pages — this is the widest net for Dubai. SerpAPI wraps it.

Docs: https://serpapi.com/google-jobs-api
"""
from __future__ import annotations

import logging
import re
from datetime import date, datetime, timedelta
from typing import Any

from ..config import settings
from .normalize import Job

logger = logging.getLogger(__name__)

_SALARY_RE = re.compile(
    r"(?P<cur>AED|USD|EUR|GBP|SAR|QAR|KWD|BHD|OMR|\$|€|£|Dhs)\s*"
    r"(?P<min>[\d,\.]+)\s*(?P<min_k>[kK])?"
    r"\s*[–\-]+\s*(?:AED|USD|EUR|GBP|SAR|QAR|KWD|BHD|OMR|\$|€|£|Dhs)?\s*"
    r"(?P<max>[\d,\.]+)\s*(?P<max_k>[kK])?"
    r"\s*(?:a|/|per\s+)?(?:\s*)(?P<int>month|year|annum|annual|week|day|hour|mo|yr|wk|d|hr)?",
    re.IGNORECASE,
)
_SINGLE_SALARY_RE = re.compile(
    r"(?P<cur>AED|USD|EUR|GBP|Dhs)\s*(?P<amt>[\d,\.]+)\s*(?P<amt_k>[kK])?\s*(?:/|per\s+)?(?P<int>month|year|annum|mo|yr)?",
    re.IGNORECASE,
)

_SYMBOL_TO_CODE = {"$": "USD", "€": "EUR", "£": "GBP", "Dhs": "AED"}
_INTERVAL_MONTHLY = {
    "year": 1 / 12, "annum": 1 / 12, "annual": 1 / 12, "yr": 1 / 12,
    "month": 1.0, "mo": 1.0,
    "week": 52 / 12, "wk": 52 / 12,
    "day": 365 / 12, "d": 365 / 12,
    "hour": (40 * 52) / 12, "hr": (40 * 52) / 12,
}


def _to_aed(amount: float, currency: str, interval: str | None) -> int | None:
    code = _SYMBOL_TO_CODE.get(currency, currency.upper())
    rate = settings.currency_to_aed.get(code, 1.0 if code == "AED" else None)
    if rate is None:
        return None
    mult = _INTERVAL_MONTHLY.get((interval or "month").lower(), 1.0)
    return int(round(amount * rate * mult))


def _parse_salary(text: str | None) -> tuple[str | None, int | None, int | None]:
    """Best-effort extraction of a salary from free-form text. Returns (raw, aed_min, aed_max)."""
    if not text:
        return None, None, None
    m = _SALARY_RE.search(text)
    if m:
        try:
            lo = float(m["min"].replace(",", ""))
            hi = float(m["max"].replace(",", ""))
            if m.group("min_k"):
                lo *= 1000
            if m.group("max_k"):
                hi *= 1000
            return m.group(0), _to_aed(lo, m["cur"], m["int"]), _to_aed(hi, m["cur"], m["int"])
        except Exception:
            pass
    m = _SINGLE_SALARY_RE.search(text)
    if m:
        try:
            amt = float(m["amt"].replace(",", ""))
            if m.group("amt_k"):
                amt *= 1000
            aed = _to_aed(amt, m["cur"], m["int"])
            return m.group(0), aed, aed
        except Exception:
            pass
    return text, None, None


def _parse_posted(posted_at: str | None) -> date | None:
    """'3 days ago', '12 hours ago', '2 weeks ago' → approximate date."""
    if not posted_at:
        return None
    m = re.match(r"(\d+)\s+(hour|day|week|month)s?\s+ago", posted_at.lower())
    if not m:
        return None
    n = int(m.group(1))
    unit = m.group(2)
    delta = {"hour": timedelta(hours=n), "day": timedelta(days=n), "week": timedelta(weeks=n), "month": timedelta(days=30 * n)}[unit]
    return (datetime.now() - delta).date()


def _apply_link(job: dict[str, Any]) -> str:
    opts = job.get("apply_options") or []
    if opts and isinstance(opts, list):
        return opts[0].get("link") or ""
    return job.get("share_link") or ""


def fetch(
    queries: list[str],
    locations: list[str],
    limit: int = 30,
    hours_old: int = 48,
) -> list[Job]:
    if not settings.serpapi_key:
        logger.info("SERPAPI_KEY not set — skipping SerpAPI source")
        return []

    try:
        from serpapi import GoogleSearch  # type: ignore
    except ImportError:
        logger.warning("google-search-results not installed — skipping SerpAPI source")
        return []

    out: list[Job] = []
    primary_location = locations[0] if locations else "Dubai, United Arab Emirates"

    for query in queries:
        params = {
            "engine": "google_jobs",
            "q": f"{query} {primary_location}",
            "hl": "en",
            "location": primary_location,
            "api_key": settings.serpapi_key,
        }
        # Google Jobs paginates via next_page_token; fetch up to 2 pages for now.
        pages = 0
        next_token: str | None = None
        while pages < 2:
            if next_token:
                params["next_page_token"] = next_token
            try:
                results = GoogleSearch(params).get_dict()
            except Exception as exc:  # noqa: BLE001
                logger.warning("serpapi query=%r failed: %s", query, exc)
                break

            jobs_results = results.get("jobs_results") or []
            if not jobs_results:
                break

            for j in jobs_results:
                try:
                    extensions = j.get("detected_extensions") or {}
                    salary_raw, aed_min, aed_max = _parse_salary(extensions.get("salary") or j.get("description", ""))

                    job = Job.build(
                        title=j.get("title") or "",
                        company=j.get("company_name") or "",
                        location=j.get("location") or primary_location,
                        url=_apply_link(j),
                        source="google_jobs",
                        description=j.get("description") or "",
                        salary_raw=salary_raw,
                        salary_aed_min=aed_min,
                        salary_aed_max=aed_max,
                        posted_date=_parse_posted(extensions.get("posted_at")),
                        raw={
                            "query": query,
                            "via": j.get("via"),
                            "job_id": j.get("job_id"),
                            "apply_options": j.get("apply_options"),
                            "extensions": extensions,
                        },
                    )
                    if job.title and job.company:
                        out.append(job)
                except Exception as exc:  # noqa: BLE001
                    logger.debug("serpapi row mapping failed: %s", exc)
                    continue

            pagination = results.get("serpapi_pagination") or {}
            next_token = pagination.get("next_page_token")
            pages += 1
            if not next_token or len(out) >= limit * len(queries):
                break

    logger.info("serpapi fetched total=%d across %d queries", len(out), len(queries))
    return out
