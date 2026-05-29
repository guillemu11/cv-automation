"""Navigate from an aggregator landing page to the real ATS form.

Job-board aggregators (jobsora, indeed, linkedin/jobs, glassdoor, google
jobs) never host the application form themselves — they show a CTA like
"Apply", "View offer in partner website", "Continue to application" that
redirects to the real ATS (Workday, Greenhouse, Lever, etc.).

This module locates that CTA on the current page (by text + role + href
heuristics, not brittle selectors), clicks it, follows new-tab pop-ups,
and reports the resulting page so the runner can re-extract the form.
"""
from __future__ import annotations

import logging
import re
from typing import Optional

from playwright.sync_api import BrowserContext, Page, TimeoutError as PWTimeout

logger = logging.getLogger(__name__)


# Text patterns that strongly suggest "this CTA leads to the application form".
# Ordered roughly by specificity — more-specific matches win.
# Use [\w'']+ to also catch "partner's", "employer's", apostrophe variants.
_APPLY_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"\bapply\s+(on|at|via|through)\s+(the\s+)?(partner|employer|company)", re.I),
    re.compile(r"\bview\s+(offer|job|details|listing)\s+(on|in|at)\s+(the\s+)?(partner|employer|company)", re.I),
    re.compile(r"\bcontinue\s+to\s+(the\s+)?application", re.I),
    re.compile(r"\bapply\s+now\b", re.I),
    re.compile(r"\bapply\s+(here|today|online|externally)\b", re.I),
    re.compile(r"\bapply\s+for\s+(this|the)\s+(job|role|position)\b", re.I),
    re.compile(r"\bapply\s+(on|via)\b", re.I),                       # any "Apply on/via X"
    re.compile(r"\bview\s+offer\b", re.I),
    re.compile(r"\bgo\s+to\s+(job|application|offer|posting)\b", re.I),
    re.compile(r"\bpartner['']?s?\s+(website|site|page)\b", re.I),   # "partner's website" / "partner site"
    re.compile(r"\bemployer['']?s?\s+(website|site|page)\b", re.I),
    re.compile(r"\bvisit\s+(employer|company|partner)\b", re.I),
    re.compile(r"\boriginal\s+(posting|listing|job)\b", re.I),
    re.compile(r"\bpostuler\b", re.I),                # FR
    re.compile(r"\bbewerben\b", re.I),                # DE
    re.compile(r"\bsolicitar\b", re.I),               # ES
    re.compile(r"^apply$", re.I),                      # bare "Apply"
    re.compile(r"^postular$", re.I),
]


# Cookie-banner text patterns — we close these before clicking Apply so they
# don't intercept the click. Order: prefer "decline" if present (less risk),
# then "accept" as fallback.
_COOKIE_DISMISS_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"^accept\s+all$", re.I),
    re.compile(r"^accept\s+cookies?$", re.I),
    re.compile(r"^i\s+(accept|agree)$", re.I),
    re.compile(r"^accept$", re.I),
    re.compile(r"^ok$", re.I),
    re.compile(r"^got\s+it$", re.I),
]

# Domains that signal "we've reached an ATS" — once we're on one of these,
# stop hopping and try to extract the form.
_ATS_DOMAINS = (
    "myworkdayjobs.com", "myworkdaysite.com", "wd1.myworkday", "wd3.myworkday", "wd5.myworkday",
    "jobs.lever.co", "boards.greenhouse.io", "greenhouse.io",
    "smartrecruiters.com", "bamboohr.com", "icims.com", "taleo.net",
    "successfactors.com", "successfactors.eu", "workable.com",
    "ashbyhq.com", "jobvite.com", "recruitee.com", "personio.com",
    "teamtailor.com", "applytojob.com", "breezy.hr",
)

# Domains we recognise as aggregators (definitely NOT the form).
_AGGREGATOR_DOMAINS = (
    "jobsora.com", "indeed.com", "linkedin.com/jobs", "glassdoor.com",
    "google.com/search", "ziprecruiter.com", "neuvoo.", "jooble.",
    "alllocaljobs.com", "trovit.", "jobrapido.", "talent.com",
)

# Aggregators that intercept leads (no real ATS link, just an email gate).
# When we detect one of these we don't even bother trying to navigate —
# we bypass the URL entirely and search the company's career site instead.
_LEAD_TRAP_DOMAINS = (
    "jobsora.com", "neuvoo.", "jooble.", "alllocaljobs.com",
    "trovit.", "jobrapido.", "talent.com",
)


def is_lead_trap(url: str) -> bool:
    """True if this aggregator intercepts leads with an email gate.

    These aggregators don't link to the real ATS — they show their own
    "enter your email" form to harvest the lead. We bypass them entirely.
    """
    if not url:
        return False
    u = url.lower()
    return any(d in u for d in _LEAD_TRAP_DOMAINS)


# Map of common companies → their career-page domain. Used as a fallback
# when we can't infer the domain from company name alone. Lowercase keys.
# Extend as we encounter more lead-trap detours.
_COMPANY_CAREER_DOMAINS: dict[str, str] = {
    "deliveroo": "deliveroo.com/careers",
    "careem": "careers.careem.com",
    "talabat": "careers.talabat.com",
    "noon": "careers.noon.com",
    "amazon": "amazon.jobs",
    "google": "careers.google.com",
    "meta": "metacareers.com",
    "uber": "uber.com/careers",
    "airbnb": "careers.airbnb.com",
    "spotify": "lifeatspotify.com",
    "netflix": "jobs.netflix.com",
    "apple": "jobs.apple.com",
    "microsoft": "careers.microsoft.com",
    "stripe": "stripe.com/jobs",
    "shopify": "shopify.com/careers",
}


def build_company_search_url(company: str, title: str, location: str = "Dubai") -> str:
    """Build a Google search URL that targets the company's careers page.

    Strategy:
      1. If we know the company → use ``site:<career-domain>`` for a precise hit
      2. Otherwise → use ``"<Company>" careers <Title> <Location>`` so Google
         ranks the company's own page first
    """
    from urllib.parse import quote_plus

    company_key = (company or "").strip().lower()
    title_q = (title or "").strip()
    location_q = (location or "").strip()

    # Strip noisy suffixes that often appear in scraped titles
    for noise in (" - apply", " - apply now", "- careers"):
        if title_q.lower().endswith(noise):
            title_q = title_q[: -len(noise)].strip()

    # Try exact match first
    domain = _COMPANY_CAREER_DOMAINS.get(company_key)
    if not domain:
        # Substring match (e.g. "Deliveroo ME" → "deliveroo")
        for key, dom in _COMPANY_CAREER_DOMAINS.items():
            if key in company_key:
                domain = dom
                break

    if domain:
        q = f'site:{domain} "{title_q}"'
    else:
        # Fallback: brand-anchored search. The quotes around the company
        # name help Google rank the company's own pages first.
        parts = [f'"{company}"', "careers"]
        if title_q:
            parts.append(f'"{title_q}"')
        if location_q:
            parts.append(location_q)
        q = " ".join(parts)

    return f"https://www.google.com/search?q={quote_plus(q)}"


def is_aggregator(url: str) -> bool:
    if not url:
        return False
    u = url.lower()
    return any(d in u for d in _AGGREGATOR_DOMAINS)


def is_ats(url: str) -> bool:
    if not url:
        return False
    u = url.lower()
    return any(d in u for d in _ATS_DOMAINS)


def _score_candidate(text: str, href: str) -> int:
    """Score 0..100 — how likely is this clickable element the apply CTA."""
    text = (text or "").strip()
    href = (href or "").lower()
    if not text and not href:
        return 0

    score = 0
    for i, pat in enumerate(_APPLY_PATTERNS):
        if pat.search(text):
            score += max(50, 100 - i * 5)
            break

    # href hints
    if "apply" in href:
        score += 20
    if any(d in href for d in _ATS_DOMAINS):
        score += 40   # links straight to a known ATS — gold

    # length heuristic: short button labels are more likely than long sentences
    if 1 <= len(text) <= 30:
        score += 5

    return score


def find_apply_candidates(page: Page) -> list[dict]:
    """Walk all visible <a> and <button> on the page, score each, return ranked list."""
    candidates_raw = page.evaluate(
        r"""
        () => {
          const isVisible = (el) => {
            if (!el.isConnected) return false;
            const r = el.getBoundingClientRect();
            if (r.width === 0 && r.height === 0) return false;
            const s = window.getComputedStyle(el);
            return s.display !== 'none' && s.visibility !== 'hidden';
          };
          const items = [];
          document.querySelectorAll('a, button, [role="button"], input[type="submit"], input[type="button"]').forEach(el => {
            if (!isVisible(el)) return;
            const text = (el.innerText || el.value || el.getAttribute('aria-label') || '').trim();
            const href = el.getAttribute('href') || '';
            const target = el.getAttribute('target') || '';
            if (!text && !href) return;
            items.push({
              text: text.slice(0, 200),
              href: href,
              target: target,
              tag: el.tagName.toLowerCase(),
              id: el.id || '',
            });
          });
          return items;
        }
        """
    )

    scored = []
    for c in candidates_raw:
        s = _score_candidate(c.get("text", ""), c.get("href", ""))
        if s >= 50:
            scored.append({**c, "score": s})

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored


def dismiss_cookie_banner(page: Page) -> bool:
    """Close any visible cookie consent banner. Returns True if one was clicked.

    Some agg sites (jobsora, indeed-EU) overlay the banner on top of the
    Apply button and intercept clicks. Best-effort — we never raise.
    """
    items = page.evaluate(
        r"""
        () => {
          const isVisible = (el) => {
            if (!el.isConnected) return false;
            const r = el.getBoundingClientRect();
            if (r.width === 0 && r.height === 0) return false;
            const s = window.getComputedStyle(el);
            return s.display !== 'none' && s.visibility !== 'hidden';
          };
          const items = [];
          // Cookie banners commonly use button OR div[role=button] OR plain div with onclick
          document.querySelectorAll('button, [role="button"], a, div').forEach(el => {
            if (!isVisible(el)) return;
            const text = (el.innerText || el.value || el.getAttribute('aria-label') || '').trim();
            if (!text || text.length > 30) return;
            items.push({
              text: text,
              tag: el.tagName.toLowerCase(),
              id: el.id || '',
            });
          });
          return items;
        }
        """
    )
    for item in items:
        for pat in _COOKIE_DISMISS_PATTERNS:
            if pat.search(item["text"]):
                try:
                    loc = page.get_by_text(item["text"], exact=True).first
                    if loc.count() == 0:
                        continue
                    loc.click(timeout=2000)
                    logger.info("navigator: dismissed cookie banner ('%s')", item["text"])
                    page.wait_for_timeout(500)  # let the overlay disappear
                    return True
                except Exception:
                    continue
    return False


def click_best_apply(page: Page, context: BrowserContext) -> Optional[Page]:
    """Find the best Apply CTA on `page` and click it. Returns the active Page after.

    Handles three cases:
      - Same-tab navigation: returns the same `page` after waiting.
      - New-tab popup: returns the popup page.
      - No suitable CTA found: returns None.
    """
    candidates = find_apply_candidates(page)
    if not candidates:
        logger.info("navigator: no apply-CTA candidates found on %s", page.url)
        return None

    best = candidates[0]
    logger.info("navigator: clicking '%s' (score=%d, href=%s)",
                best["text"][:60], best["score"], best.get("href", "")[:100])

    # Build a locator targeting that element. Prefer ID, then role+name, then text.
    locator = None
    if best.get("id"):
        try:
            cand = page.locator(f"#{best['id']}").first
            if cand.count() > 0:
                locator = cand
        except Exception:
            pass
    if locator is None:
        # Try role-based locator (most stable for buttons/links).
        # Use a regex anchored to the start of the text so duplicates and
        # case differences ("Apply" vs "APPLY") still match a single element.
        text_re = re.compile(re.escape(best["text"][:40]), re.I)
        for role in ("button", "link"):
            try:
                cand = page.get_by_role(role, name=text_re).first
                if cand.count() > 0:
                    locator = cand
                    break
            except Exception:
                continue
    if locator is None:
        try:
            cand = page.get_by_text(best["text"], exact=False).first
            if cand.count() > 0:
                locator = cand
        except Exception:
            pass
    if locator is None:
        return None

    try:
        locator.scroll_into_view_if_needed(timeout=3000)
    except Exception:
        pass

    # Anticipate a popup. If the click opens a new tab, expect_page captures it.
    new_page: Optional[Page] = None
    try:
        with context.expect_page(timeout=8_000) as new_page_info:
            try:
                locator.click(timeout=5_000)
            except PWTimeout:
                # Click timed out, but the popup may still arrive
                pass
        new_page = new_page_info.value
    except PWTimeout:
        # No popup happened — treat as same-tab navigation
        new_page = None
    except Exception as exc:
        logger.debug("navigator: click error: %s", exc)
        return None

    target = new_page or page
    try:
        target.wait_for_load_state("domcontentloaded", timeout=20_000)
        target.wait_for_load_state("networkidle", timeout=10_000)
    except PWTimeout:
        pass  # not all pages reach networkidle; proceed anyway

    return target
