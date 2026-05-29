"""Contact finder — locates hiring managers and peers via Google → LinkedIn.

LinkedIn closes profiles behind login, but Google has indexed millions of
public LinkedIn profile pages. We use SerpAPI (already configured for the
discovery pipeline) to run targeted `site:linkedin.com/in` searches and
extract names, current titles, and profile URLs from the snippets.

No emails — Google does not index them. The frontend already handles
contacts without email by hiding the email button and surfacing only the
LinkedIn link. The user reaches out via LinkedIn InMail or connection request.

Pipeline:
  1. Gemini infers 3-4 likely hiring-manager titles from job_title + JD
  2. SerpAPI runs queries: site:linkedin.com/in <Company> <Location> "<Title>"
  3. Snippets are parsed for {name, title, linkedin_url}
  4. Heuristics filter out ex-employees, wrong geography, dupes
  5. Each survivor gets a role_type (Hiring Manager / Peer / HR/Recruiter)
"""
from __future__ import annotations

import json
import logging
import re
from dataclasses import asdict, dataclass

import httpx

from .config import settings

logger = logging.getLogger(__name__)

SERPAPI_URL = "https://serpapi.com/search"

# Locations we'll restrict the search to. Job-specific location overrides.
_DEFAULT_LOCATION = "United Arab Emirates"

# Snippet markers that mean "this person no longer works at the company".
_EX_EMPLOYEE_MARKERS = (
    "ex ", "ex-", "former ", "previously at", "previously ", "past:",
    "alumna", "alumnus", "alumni",
)

# Static fallback if Gemini is unreachable — generic senior titles for any role.
_FALLBACK_HM_TITLES = [
    "Head of Marketing", "Marketing Director", "VP Marketing", "General Manager",
]

# HR titles to find recruiters. We keep them static because they don't depend
# on the job — recruiters at a company are recruiters regardless of which req.
_HR_TITLES = [
    "Talent Acquisition", "HR Manager", "Recruiter", "Head of People",
]


@dataclass
class Contact:
    """A person found at a target company.

    NOTE: kept structurally identical to the old Apollo-era Contact so the
    pipeline + dashboard render unchanged. `email` will always be None with
    the Google→LinkedIn approach (Google doesn't index emails).
    """
    name: str
    title: str
    company: str
    email: str | None = None
    linkedin_url: str | None = None
    role_type: str = "Hiring Manager"  # Hiring Manager | HR/Recruiter | Peer
    source: str = "LinkedIn (via Google)"

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Contact":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


# -------------------------------------------------------------------
# Title inference via Gemini (with hardcoded fallback)
# -------------------------------------------------------------------

def _infer_hiring_manager_titles(job_title: str, job_description: str = "") -> list[str]:
    """Ask Gemini for 3-4 plausible hiring-manager titles. Falls back to generic."""
    if not settings.gemini_api_key:
        return _FALLBACK_HM_TITLES

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        logger.warning("google-genai not installed — using fallback titles")
        return _FALLBACK_HM_TITLES

    prompt = (
        f"Job title: {job_title}\n\n"
        f"Description excerpt:\n{(job_description or '')[:1200]}\n\n"
        "Return a JSON array of 3-4 job titles for the person who would be 1-2 levels "
        "above this role at the same company in Dubai/UAE — the likely hiring "
        "decision maker. Use titles common in GCC: 'Head of …', 'Director', 'VP', "
        "'General Manager'. Just the array, no prose."
    )

    try:
        client = genai.Client(api_key=settings.gemini_api_key)
        resp = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema={"type": "ARRAY", "items": {"type": "STRING"}},
                temperature=0.2,
                max_output_tokens=200,
                thinking_config=types.ThinkingConfig(thinking_budget=0),
            ),
        )
        if resp.text:
            titles = json.loads(resp.text)
            if isinstance(titles, list) and titles:
                return [str(t) for t in titles[:4]]
    except Exception as exc:  # noqa: BLE001
        logger.warning("Gemini title inference failed: %s — using fallback", exc)

    return _FALLBACK_HM_TITLES


# -------------------------------------------------------------------
# SerpAPI Google search
# -------------------------------------------------------------------

def _serpapi_search(query: str, num: int = 6) -> list[dict]:
    """Run one SerpAPI Google search. Returns list of organic_results dicts."""
    if not settings.serpapi_key:
        logger.warning("SERPAPI_KEY not set — cannot search")
        return []
    try:
        r = httpx.get(SERPAPI_URL, params={
            "engine": "google",
            "q": query,
            "api_key": settings.serpapi_key,
            "num": num,
            "hl": "en",
            "gl": "ae",  # bias toward UAE results
        }, timeout=30)
        r.raise_for_status()
        data = r.json()
        return data.get("organic_results") or []
    except httpx.HTTPError as exc:
        logger.error("SerpAPI search failed for %r: %s", query, exc)
        return []


# -------------------------------------------------------------------
# Snippet parsing
# -------------------------------------------------------------------

# LinkedIn page <title> patterns Google indexes:
#   "Firstname Lastname - Current Title at Company"
#   "Firstname Lastname - Current Title | LinkedIn"
#   "‏Firstname Lastname‏ - ‏Current Title‏" (Arabic-flavored when gl=ae)
_TITLE_SPLIT = re.compile(r"\s*[-–|·]\s+", re.UNICODE)
# Strip RTL/LTR markers and other zero-width junk from titles
_INVISIBLE = re.compile(r"[‎‏‪-‮⁦-⁩؜]")


def _clean(s: str) -> str:
    return _INVISIBLE.sub("", s or "").strip()


def _parse_result(hit: dict, company: str) -> Contact | None:
    """Pull (name, current_title, linkedin_url) from one SerpAPI hit."""
    title_field = _clean(hit.get("title", ""))
    link = hit.get("link", "")
    snippet = _clean(hit.get("snippet", ""))

    if not title_field or "linkedin.com/in/" not in link:
        return None

    # Drop common trailing tokens
    title_field = re.sub(r"\s*\|\s*LinkedIn\s*$", "", title_field, flags=re.I)

    parts = _TITLE_SPLIT.split(title_field, maxsplit=1)
    if len(parts) < 2:
        return None
    name = parts[0].strip()
    headline = parts[1].strip()

    # Drop hits where the name is empty or where headline is still 'LinkedIn'
    if not name or headline.lower() in ("linkedin", ""):
        return None

    return Contact(
        name=name,
        title=headline,
        company=company,
        email=None,
        linkedin_url=link,
        role_type="Hiring Manager",  # default; caller overrides per query type
        source="LinkedIn (via Google)",
    )


def _is_currently_at_company(
    contact: Contact, snippet: str, company: str, *, strict: bool = True,
) -> bool:
    """Heuristic: is this person CURRENTLY at the target company?

    LinkedIn page <title> always shows the *current* role, so if the headline
    contains the company name we're confident. Otherwise we look at the snippet
    for ex-employee markers.

    `strict=False` accepts hits where company appears anywhere in snippet
    without an explicit ex-marker — useful for tiny companies whose employees
    don't put the company in their LinkedIn headline.
    """
    company_lc = company.lower()
    headline_lc = contact.title.lower()
    snippet_lc = snippet.lower()

    if company_lc in headline_lc:
        return True
    # Ex-marker veto (always applied)
    for marker in _EX_EMPLOYEE_MARKERS:
        if f"{marker}{company_lc}" in snippet_lc or f"{marker}{company_lc}" in headline_lc:
            return False
    # "Present" / "Current" markers
    if "الحالي" in snippet or "present" in snippet_lc or "current" in snippet_lc:
        if company_lc in snippet_lc:
            return True
    if strict:
        return company_lc in headline_lc
    # Loose mode: accept if company appears anywhere in snippet without ex-marker veto
    return company_lc in snippet_lc


def _location_ok(contact: Contact, snippet: str) -> bool:
    """Reject obvious wrong-geo hits.

    LinkedIn URLs are subdomain-prefixed by country (in./kw./uk./sa./...).
    We accept ae.* and unprefixed (www.linkedin.com); for ANY other country
    subdomain the snippet must explicitly mention Dubai/UAE (and not the
    country the subdomain implies).
    """
    url = (contact.linkedin_url or "").lower()
    snippet_lc = snippet.lower()

    if "://ae.linkedin.com" in url or "://www.linkedin.com" in url:
        return True

    # Other-country subdomain — require strong UAE signal in the snippet
    if not ("dubai" in snippet_lc or "united arab emirates" in snippet_lc or "uae" in snippet_lc
            or "abu dhabi" in snippet_lc or "sharjah" in snippet_lc):
        return False

    # Subdomain implies a country — reject if snippet clearly describes that other country
    foreign_markers = {
        "://in.linkedin.com": ["india", "mumbai", "bangalore", "delhi", "chennai", "hyderabad"],
        "://uk.linkedin.com": ["london", "manchester"],
        "://kw.linkedin.com": ["kuwait"],
        "://sa.linkedin.com": ["riyadh", "saudi"],
        "://us.linkedin.com": ["new york", "san francisco", "chicago"],
        "://eg.linkedin.com": ["cairo", "egypt"],
        "://lb.linkedin.com": ["beirut", "lebanon"],
        "://qa.linkedin.com": ["qatar", "doha"],
    }
    for sub, markers in foreign_markers.items():
        if sub in url:
            for m in markers:
                if m in snippet_lc:
                    return False
    return True


# -------------------------------------------------------------------
# Public API
# -------------------------------------------------------------------

def _run_query_round(
    queries: list[tuple[str, str]],
    company: str,
    seen_urls: set[str],
    contacts: list[Contact],
    *,
    strict: bool = True,
    cap_per_role: int = 3,
    num_per_query: int = 8,
) -> int:
    """Execute a list of (query, role_type) and append survivors. Returns count of new hits."""
    added = 0
    for q, role_type in queries:
        hits = _serpapi_search(q, num=num_per_query)
        for hit in hits:
            c = _parse_result(hit, company)
            if not c:
                continue
            url_key = (c.linkedin_url or "").rstrip("/").lower()
            if url_key in seen_urls:
                continue
            snippet = _clean(hit.get("snippet", ""))
            if not _location_ok(c, snippet):
                continue
            if not _is_currently_at_company(c, snippet, company, strict=strict):
                continue
            c.role_type = role_type
            seen_urls.add(url_key)
            contacts.append(c)
            added += 1
            # Cap per role_type to avoid floods of the same kind
            if sum(1 for x in contacts if x.role_type == role_type) >= cap_per_role:
                break
    return added


def find_contacts(
    company: str,
    job_title: str,
    job_description: str = "",
) -> list[Contact]:
    """Find hiring manager + peer + HR contacts at a company via Google→LinkedIn.

    Cascading strategy: start strict (precision), broaden if too few results.
      Round 1: targeted role-specific queries, headline-must-match company
      Round 2: broader queries (no Dubai required, looser snippet match)
      Round 3: any senior person at the company (founder/director/manager)

    Returns 0–10 unique contacts. Email is always None with this approach.
    """
    if not settings.serpapi_key:
        logger.warning("SERPAPI_KEY not set — skipping contact finder")
        return []

    if settings.dry_run:
        logger.info("[DRY RUN] Skipping contact search for %s", company)
        return [Contact(
            name="Mock Hiring Manager", title="Head of Marketing",
            company=company, linkedin_url="https://linkedin.com/in/mock",
            role_type="Hiring Manager",
        )]

    hm_titles = _infer_hiring_manager_titles(job_title, job_description)
    logger.info("contact search for %s: hm_titles=%s", company, hm_titles)

    seen_urls: set[str] = set()
    contacts: list[Contact] = []

    # ---- ROUND 1: specific titles, strict filter ----
    round1: list[tuple[str, str]] = []
    for t in hm_titles[:3]:
        round1.append((f'site:linkedin.com/in "{company}" Dubai "{t}"', "Hiring Manager"))
    round1.append((f'site:linkedin.com/in "{company}" Dubai "{job_title}"', "Peer"))
    hr_or = " OR ".join(f'"{t}"' for t in _HR_TITLES[:3])
    round1.append((f'site:linkedin.com/in "{company}" Dubai ({hr_or})', "HR/Recruiter"))
    _run_query_round(round1, company, seen_urls, contacts, strict=True)
    logger.info("round1 done: %d contacts at %s", len(contacts), company)

    # ---- ROUND 2: broader (no Dubai literal, loose filter) ----
    if len(contacts) < 5:
        round2: list[tuple[str, str]] = [
            (f'site:linkedin.com/in "{company}" UAE marketing', "Hiring Manager"),
            (f'site:linkedin.com/in "{company}" "Head of"', "Hiring Manager"),
            (f'site:linkedin.com/in "{company}" "Director"', "Hiring Manager"),
            (f'site:linkedin.com/in "{company}" {job_title}', "Peer"),
            (f'site:linkedin.com/in "{company}" recruiter OR talent', "HR/Recruiter"),
        ]
        _run_query_round(round2, company, seen_urls, contacts, strict=False)
        logger.info("round2 done: %d contacts at %s", len(contacts), company)

    # ---- ROUND 3: anyone senior at the company (last resort, tiny companies) ----
    if len(contacts) < 3:
        round3: list[tuple[str, str]] = [
            (f'site:linkedin.com/in "{company}" founder OR CEO OR partner', "Hiring Manager"),
            (f'site:linkedin.com/in "{company}" manager', "Peer"),
            (f'site:linkedin.com/in "{company}"', "Peer"),  # very wide net
        ]
        _run_query_round(round3, company, seen_urls, contacts, strict=False, cap_per_role=4)
        logger.info("round3 done: %d contacts at %s", len(contacts), company)

    logger.info("FINAL: %d contacts at %s", len(contacts), company)
    return contacts
