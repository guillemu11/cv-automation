"""Hard filters applied before the scorer.

These are binary pass/fail checks — no scoring, no nuance. A job that fails
any hard filter is rejected and never reaches the Claude API scorer (saves $).

Filter logic:
  - Salary: ONLY reject if a salary IS visible AND max < 20K AED/month.
    No salary = pass. This is critical because ~80% of Dubai jobs don't
    publish salary.
  - Location: must mention a UAE location.
  - Keywords: reject if title or description contains blacklisted keywords.
  - Seniority: reject Intern/Junior/Entry Level.
  - Company: reject blacklisted companies.
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field

from ..config import settings
from ..discovery.normalize import Job
from .salary_parser import parse_salary

logger = logging.getLogger(__name__)


@dataclass
class FilterResult:
    """Outcome of filtering a batch of jobs."""
    passed: list[Job] = field(default_factory=list)
    rejected: list[tuple[Job, str]] = field(default_factory=list)  # (job, reason)

    @property
    def passed_count(self) -> int:
        return len(self.passed)

    @property
    def rejected_count(self) -> int:
        return len(self.rejected)


def _check_location(job: Job) -> str | None:
    """Returns rejection reason or None if OK."""
    allowed = settings.allowed_locations
    if not allowed:
        return None
    loc = (job.location or "").lower()
    # Also check description for location mentions (some jobs have empty location)
    text = f"{loc} {(job.description or '')[:500].lower()}"
    if any(a.lower() in text for a in allowed):
        return None
    return f"location '{job.location}' not in allowed UAE locations"


def _check_salary(job: Job) -> str | None:
    """Returns rejection reason or None if OK.

    CRITICAL: no salary info = PASS. Only reject when salary IS visible
    AND max < floor.
    """
    floor = settings.min_salary_aed
    if not floor:
        return None

    # Try pre-parsed values from discovery first
    aed_min = job.salary_aed_min
    aed_max = job.salary_aed_max

    # If discovery didn't parse salary, try our own parser on salary_raw
    if aed_max is None and job.salary_raw:
        aed_min, aed_max = parse_salary(job.salary_raw)

    # No salary info at all → PASS (most Dubai jobs don't publish salary)
    if aed_max is None:
        return None

    # Salary visible but below floor → REJECT
    if aed_max < floor:
        return f"salary AED {aed_max}/month < floor AED {floor}/month"

    return None


def _check_keywords(job: Job) -> str | None:
    """Returns rejection reason if blacklisted keyword found in title or description.

    Uses word-boundary matching to avoid false positives like "international"
    matching "intern", or "volunteering" matching "volunteer".
    """
    reject_kw = settings.keywords_reject
    if not reject_kw:
        return None
    title_lower = (job.title or "").lower()
    desc_lower = (job.description or "")[:2000].lower()
    for kw in reject_kw:
        pattern = rf"\b{re.escape(kw)}\b"
        if re.search(pattern, title_lower):
            return f"blacklisted keyword '{kw}' in title"
        if re.search(pattern, desc_lower):
            return f"blacklisted keyword '{kw}' in description"
    return None


def _check_seniority(job: Job) -> str | None:
    """Returns rejection reason if title suggests rejected seniority level."""
    reject_levels = settings.seniority_reject
    if not reject_levels:
        return None
    title_lower = (job.title or "").lower()
    for level in reject_levels:
        # Word-boundary match to avoid "Senior" matching "seniority"
        if re.search(rf"\b{re.escape(level)}\b", title_lower):
            return f"seniority '{level}' in title"
    return None


def _check_title_patterns(job: Job) -> str | None:
    """Reject if the title matches a title_reject_patterns entry.

    Title-only (not description) to avoid false positives where a JD merely
    mentions tech/construction in passing. Substring match — patterns like
    'software engineer' won't false-positive because they're already specific.
    """
    patterns = settings.title_reject_patterns
    if not patterns:
        return None
    title_lower = (job.title or "").lower()
    for p in patterns:
        if p in title_lower:
            return f"title pattern '{p}' rejected"
    return None


def _check_company(job: Job) -> str | None:
    """Returns rejection reason if company is blacklisted."""
    blacklist = settings.companies_blacklist
    if not blacklist:
        return None
    company_lower = (job.company or "").lower()
    for blocked in blacklist:
        if blocked in company_lower:
            return f"company '{job.company}' is blacklisted"
    return None


# All checks in order. Put cheap checks first to short-circuit early.
_CHECKS = [
    _check_company,
    _check_seniority,
    _check_title_patterns,
    _check_keywords,
    _check_location,
    _check_salary,
]


def apply_hard_filters(jobs: list[Job]) -> FilterResult:
    """Run all hard filters on a list of jobs. Returns FilterResult."""
    result = FilterResult()
    for job in jobs:
        rejected = False
        for check in _CHECKS:
            reason = check(job)
            if reason:
                result.rejected.append((job, reason))
                rejected = True
                break
        if not rejected:
            result.passed.append(job)

    logger.info(
        "hard_filters: %d passed, %d rejected",
        result.passed_count,
        result.rejected_count,
    )
    if result.rejected:
        reasons = {}
        for _, reason in result.rejected:
            key = reason.split("'")[0].strip()
            reasons[key] = reasons.get(key, 0) + 1
        for reason, count in sorted(reasons.items(), key=lambda x: -x[1]):
            logger.debug("  rejected %dx: %s", count, reason)

    return result
