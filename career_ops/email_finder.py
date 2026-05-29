"""Email pattern guessing + Hunter.io verification.

Two-stage enrichment for contacts whose LinkedIn we found via Google but whose
email is not public:

  1. ``guess_emails(full_name, domain)`` — produce N candidate addresses from
     common corporate patterns (firstname.lastname, flastname, etc.).
  2. ``verify_email(email)`` — call Hunter.io to verify deliverability when
     ``settings.hunter_api_key`` is set; otherwise mark candidates as
     ``status="unverified"`` and let the human decide.

A single ``domain_pattern(domain)`` call (Hunter ``domain-search``) can detect
the dominant pattern for a company once, so subsequent lookups can short-circuit
straight to the right template.

NOTE: never auto-sends. Email is only used downstream to create draft messages.
"""
from __future__ import annotations

import logging
import re
import unicodedata
from dataclasses import asdict, dataclass

import httpx

from .config import settings

logger = logging.getLogger(__name__)

HUNTER_VERIFIER_URL = "https://api.hunter.io/v2/email-verifier"
HUNTER_DOMAIN_SEARCH_URL = "https://api.hunter.io/v2/domain-search"

# Corporate email patterns ordered by global frequency. {first}, {last}, {f},
# {l} placeholders. Used to fan out candidate addresses for an unknown person.
EMAIL_PATTERNS = (
    "{first}.{last}",      # most common at large multinationals (Sanofi-era)
    "{f}{last}",           # second most common
    "{first}",             # smaller orgs / consumer brands
    "{first}{last}",
    "{first}_{last}",
    "{first}-{last}",
    "{last}.{first}",
    "{f}.{last}",
    "{first}{l}",
    "{last}{f}",
)


@dataclass
class EmailCandidate:
    email: str
    pattern: str
    status: str = "unverified"  # deliverable | risky | undeliverable | unknown | unverified
    score: int | None = None    # 0-100 from Hunter, None if unverified
    source: str = ""            # "pattern" | "hunter:verifier" | "hunter:domain-search"

    def to_dict(self) -> dict:
        return asdict(self)


# -------------------------------------------------------------------
# Name normalization
# -------------------------------------------------------------------

_DROPPABLE_PARTICLES = {"de", "del", "la", "le", "van", "von", "der", "den", "di", "da", "el", "al", "bin", "ibn"}


def _strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def split_name(full_name: str) -> tuple[str, str] | None:
    """Best-effort first/last split for corporate-email pattern fill-in.

    Drops Arabic articles and Spanish particles to keep the surname compact:
    'Paula De Francisco' -> ('paula', 'francisco').
    Returns None if we cannot extract at least one first + one last token.
    """
    if not full_name:
        return None
    cleaned = _strip_accents(full_name)
    cleaned = re.sub(r"[^A-Za-z\s'-]", " ", cleaned)
    tokens = [t for t in re.split(r"\s+", cleaned.strip()) if t]
    tokens = [t for t in tokens if t.lower() not in _DROPPABLE_PARTICLES]
    if len(tokens) < 2:
        return None
    first = tokens[0].lower()
    last = tokens[-1].lower()
    if not first or not last:
        return None
    return first, last


# -------------------------------------------------------------------
# Pattern guessing
# -------------------------------------------------------------------

def guess_emails(full_name: str, domain: str, patterns: tuple[str, ...] | None = None) -> list[EmailCandidate]:
    """Return ordered list of candidate addresses for the person at ``domain``.

    Empty list if the name can't be parsed.
    """
    split = split_name(full_name)
    if not split:
        return []
    first, last = split
    f = first[0]
    l = last[0]  # noqa: E741
    domain = domain.strip().lower().lstrip("@")
    out: list[EmailCandidate] = []
    seen: set[str] = set()
    for pat in patterns or EMAIL_PATTERNS:
        local = pat.format(first=first, last=last, f=f, l=l)
        email = f"{local}@{domain}"
        if email in seen:
            continue
        seen.add(email)
        out.append(EmailCandidate(email=email, pattern=pat, source="pattern"))
    return out


# -------------------------------------------------------------------
# Hunter.io integration (optional)
# -------------------------------------------------------------------

def verify_email(email: str) -> EmailCandidate | None:
    """Verify deliverability via Hunter.io. Returns None if no API key set."""
    if not settings.hunter_api_key:
        return None
    try:
        r = httpx.get(
            HUNTER_VERIFIER_URL,
            params={"email": email, "api_key": settings.hunter_api_key},
            timeout=15,
        )
        r.raise_for_status()
        data = r.json().get("data") or {}
    except httpx.HTTPError as exc:
        logger.warning("Hunter verify failed for %s: %s", email, exc)
        return None
    return EmailCandidate(
        email=email,
        pattern="",
        status=str(data.get("status", "unknown")),
        score=data.get("score"),
        source="hunter:verifier",
    )


def domain_pattern(domain: str) -> str | None:
    """Detect the dominant pattern for a company via Hunter domain-search.

    Returns the Hunter-style pattern string (e.g. ``'{first}.{last}'``,
    ``'{f}{last}'``) or None if no API key / no signal.
    """
    if not settings.hunter_api_key:
        return None
    try:
        r = httpx.get(
            HUNTER_DOMAIN_SEARCH_URL,
            params={"domain": domain.lstrip("@"), "api_key": settings.hunter_api_key, "limit": 1},
            timeout=15,
        )
        r.raise_for_status()
        data = r.json().get("data") or {}
    except httpx.HTTPError as exc:
        logger.warning("Hunter domain-search failed for %s: %s", domain, exc)
        return None
    pat = data.get("pattern")
    if not pat:
        return None
    # Hunter uses {first}/{last}/{f}/{l} placeholders — same as us. Return as-is.
    return str(pat)


def enrich_name(
    full_name: str,
    domain: str,
    *,
    max_verify: int = 3,
) -> list[EmailCandidate]:
    """High-level helper: produce candidates and (if Hunter is set) verify the
    top ``max_verify`` of them.

    Strategy:
      1. If we have Hunter, ask for the corporate pattern once → put that
         candidate first and verify it.
      2. Otherwise (or if Hunter pattern is unknown) fan out via
         ``EMAIL_PATTERNS`` and verify the first ``max_verify``.
    """
    base_pattern = domain_pattern(domain) if settings.hunter_api_key else None
    patterns: tuple[str, ...] | None = None
    if base_pattern:
        # Put the corporate pattern first; keep the rest as fallback.
        rest = tuple(p for p in EMAIL_PATTERNS if p != base_pattern)
        patterns = (base_pattern, *rest)

    candidates = guess_emails(full_name, domain, patterns=patterns)
    if not settings.hunter_api_key:
        return candidates

    # Verify the top ``max_verify`` candidates; preserve order, replace status.
    for i, c in enumerate(candidates[:max_verify]):
        verified = verify_email(c.email)
        if verified:
            c.status = verified.status
            c.score = verified.score
            c.source = "hunter:verifier"
    return candidates
