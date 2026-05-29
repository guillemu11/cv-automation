"""End-to-end autofill orchestrator — called from the dashboard.

Flow (one click from the UI):
1. Reconstruct Job + JobAnalysis from scored_jobs.json.
2. If FORM_Paula_*.json doesn't exist for this job, generate it (calls
   ``generate_form_responses``).
3. If Playwright's Chromium is missing, install it transparently.
4. Launch a visible Chromium, navigate to job.url.
5. Extract form fields, ask Claude to map them, apply actions.
6. Auto-attach CV / cover-letter PDFs to file inputs.
7. Leave the browser open via ``page.pause()`` so Paula can review and
   submit manually. Browser closes when she closes the window.

The runner is meant to be invoked from a background thread (see the
``/api/jobs/{job_id}/autofill`` endpoint), so it blocks until the user
closes the browser. It never raises into the caller — all errors are
captured into the status dict.
"""
from __future__ import annotations

import json
import logging
import re
import subprocess
import sys
import threading
from dataclasses import asdict
from pathlib import Path
from typing import Any

from ..config import settings

logger = logging.getLogger(__name__)


# -------------------------------------------------------------------
# Status tracking — read by /api/autofill/status?job_id=...
# -------------------------------------------------------------------

_status: dict[str, dict[str, Any]] = {}
_status_lock = threading.Lock()


def _set_status(job_id: str, **patch) -> None:
    with _status_lock:
        cur = _status.setdefault(job_id, {"job_id": job_id})
        cur.update(patch)


def get_status(job_id: str) -> dict[str, Any]:
    with _status_lock:
        return dict(_status.get(job_id, {"job_id": job_id, "stage": "idle"}))


# -------------------------------------------------------------------
# Helpers — find files saved by form_responses.py
# -------------------------------------------------------------------

def _sanitize(s: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', "", s).strip().replace(" ", "_")[:50]


def _find_under_output(filename: str) -> Path:
    """Locate a generated file anywhere under output/ (recursively).

    Generators write into per-job subfolders (``output/<Company> - <Role>/``
    and, for dated batches, ``output/<YYYY-MM-DD>/<Company> - <Role>/``), so a
    flat ``output_dir / filename`` no longer finds them. Search recursively and
    fall back to the legacy root path when nothing matches (callers test
    ``.exists()``).
    """
    root = settings.output_dir
    try:
        match = next(root.rglob(filename), None)
    except Exception:
        match = None
    return match if match is not None else (root / filename)


def _form_json_path(company: str, role: str) -> Path:
    return _find_under_output(f"FORM_Paula_{_sanitize(company)}_{_sanitize(role)}.json")


def _cv_pdf_path(company: str, role: str) -> Path:
    return _find_under_output(f"CV_Paula_{_sanitize(company)}_{_sanitize(role)}.pdf")


def _cover_pdf_path(company: str, role: str) -> Path:
    # Generators write CL_Paula_*; older code used COVER_Paula_*. Prefer CL_.
    cl = _find_under_output(f"CL_Paula_{_sanitize(company)}_{_sanitize(role)}.pdf")
    if cl.exists():
        return cl
    return _find_under_output(f"COVER_Paula_{_sanitize(company)}_{_sanitize(role)}.pdf")


# -------------------------------------------------------------------
# Playwright bootstrap — auto-install Chromium if missing
# -------------------------------------------------------------------

def _ensure_chromium_installed(job_id: str) -> bool:
    """Install Playwright's Chromium binary on first use. Returns True on success."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        _set_status(job_id, stage="error", error="playwright package not installed; pip install playwright")
        return False

    try:
        with sync_playwright() as pw:
            try:
                browser = pw.chromium.launch(headless=True)
                browser.close()
                return True
            except Exception:
                pass  # binary missing — install below

        _set_status(job_id, stage="installing_chromium",
                    message="First-time setup: downloading Chromium (~150MB)...")
        result = subprocess.run(
            [sys.executable, "-m", "playwright", "install", "chromium"],
            capture_output=True, text=True, timeout=300,
        )
        if result.returncode != 0:
            _set_status(job_id, stage="error",
                        error=f"playwright install failed: {result.stderr[-400:]}")
            return False
        return True
    except Exception as exc:
        _set_status(job_id, stage="error", error=f"chromium check failed: {exc}")
        return False


# -------------------------------------------------------------------
# Form responses — generate if missing
# -------------------------------------------------------------------

def _ensure_form_responses(job, analysis, job_id: str) -> dict | None:
    """Return the FORM_Paula_*.json contents, generating it first if missing."""
    json_path = _form_json_path(job.company, job.title)

    if not json_path.exists():
        _set_status(job_id, stage="generating_responses",
                    message="Generating personalized form answers with Claude...")
        from ..generators.form_responses import generate_form_responses
        result = generate_form_responses(job, analysis)
        if not result:
            _set_status(job_id, stage="error",
                        error="failed to generate form responses (check ANTHROPIC_API_KEY and template)")
            return None

    try:
        with json_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as exc:
        _set_status(job_id, stage="error", error=f"could not read {json_path.name}: {exc}")
        return None


# -------------------------------------------------------------------
# Main entry point — runs in a **shared** browser context (a tab in the
# same Chromium that's hosting the dashboard).
# -------------------------------------------------------------------

def run_autofill_in_tab(context, job, analysis) -> dict[str, Any]:
    """Open a new tab in ``context`` and autofill the form for ``job``.

    The browser/context lifecycle is owned by ``BrowserWorker``; this
    function never closes them. The autofill tab itself is left open
    after we finish — Paula reviews and submits manually, and closing
    that tab is what advances the job from awaiting_human to done.

    Args:
        context: a Playwright BrowserContext owned by BrowserWorker
        job: career_ops.discovery.normalize.Job
        analysis: career_ops.analyzer.JobAnalysis

    Returns:
        Status dict (also retrievable via get_status(job.id)).
    """
    job_id = job.id
    _set_status(job_id, stage="starting", error=None, message=None)

    if not job.url:
        _set_status(job_id, stage="error", error="job has no URL")
        return get_status(job_id)

    # 1. Form responses — generate if missing (network-bound, can run before browser work)
    responses = _ensure_form_responses(job, analysis, job_id)
    if responses is None:
        return get_status(job_id)

    from .extractor import extract_form_fields
    from .filler import apply_actions, auto_upload_files
    from .mapper import map_fields
    from .navigator import (
        build_company_search_url,
        click_best_apply,
        dismiss_cookie_banner,
        is_aggregator,
        is_ats,
        is_lead_trap,
    )

    cv = _cv_pdf_path(job.company, job.title)
    cover = _cover_pdf_path(job.company, job.title)

    MIN_FIELDS_FOR_FORM = 3
    MAX_NAVIGATION_HOPS = 4

    try:
        _set_status(job_id, stage="opening_browser",
                    message=f"Opening a new tab for {job.company}...")
        # Open a NEW TAB in the existing context. That's the whole point
        # of the browser_worker refactor — one Chromium, many tabs.
        page = context.new_page()
        try:
            page.bring_to_front()
        except Exception:
            pass

        # Lead-trap aggregators (jobsora, neuvoo, jooble) don't link to
        # the real ATS — they harvest emails. Bypass them: open Google
        # scoped to the company's career site so Paula can pick the real
        # listing in one click.
        if is_lead_trap(job.url):
            search_url = build_company_search_url(job.company, job.title, job.location)
            _set_status(
                job_id, stage="bypassing_aggregator",
                message=(f"{job.url.split('/')[2]} is a lead-trap aggregator. "
                         f"Opening Google scoped to {job.company}'s career site instead — "
                         f"click the right result and the autofill will continue from there."),
            )
            page.goto(search_url, wait_until="domcontentloaded", timeout=45_000)
        else:
            page.goto(job.url, wait_until="domcontentloaded", timeout=45_000)
        try:
            page.wait_for_load_state("networkidle", timeout=10_000)
        except Exception:
            pass

        # ---- Find the form ----
        bypass_active = is_lead_trap(job.url)
        fields = []
        hops_taken = 0

        if not bypass_active:
            for hop in range(MAX_NAVIGATION_HOPS + 1):
                try:
                    dismiss_cookie_banner(page)
                except Exception:
                    pass

                _set_status(job_id, stage="extracting_fields",
                            message=f"Reading form fields (page: {page.url[:80]}...)")
                fields = extract_form_fields(page)
                if len(fields) >= MIN_FIELDS_FOR_FORM:
                    break

                if hop >= MAX_NAVIGATION_HOPS:
                    break

                hint = "aggregator" if is_aggregator(page.url) else (
                    "ATS landing" if is_ats(page.url) else "unknown")
                _set_status(
                    job_id, stage="navigating_to_form",
                    message=(f"Only {len(fields)} fields here ({hint}). "
                             f"Looking for Apply button (hop {hop + 1}/{MAX_NAVIGATION_HOPS})..."),
                )
                next_page = click_best_apply(page, context)
                if next_page is None:
                    break
                if next_page is not page:
                    page = next_page
                    try:
                        page.bring_to_front()
                    except Exception:
                        pass
                hops_taken += 1

        if len(fields) < MIN_FIELDS_FOR_FORM:
            _set_status(
                job_id, stage="waiting_for_navigation",
                message=("Pick the right job in the browser. The autofill will "
                         "kick in automatically as soon as you reach the application form."),
            )
            # Restrict polling to non-dashboard tabs only — never autofill the dashboard itself.
            page, fields = _wait_for_form_in_any_tab(context, timeout_s=600,
                                                    skip_predicate=_looks_like_dashboard)
            if page is None:
                _set_status(
                    job_id, stage="awaiting_human",
                    message=("No application form detected in the browser yet. "
                             "Tab stays open — finish manually if you'd like. "
                             "Close the tab when you're done."),
                )
                _wait_until_tab_closed(page if page else None)
                _set_status(job_id, stage="done", message="Tab closed.")
                return get_status(job_id)
            try:
                page.bring_to_front()
            except Exception:
                pass

        # ---- Form found: map, fill, attach files ----
        _set_status(job_id, stage="mapping_fields",
                    message=f"Form found ({len(fields)} fields). Mapping with Claude...")
        actions = map_fields(fields, responses)

        _set_status(job_id, stage="filling",
                    message=f"Filling {len(actions)} fields...")
        report = apply_actions(page, actions)

        _set_status(job_id, stage="uploading_files",
                    message="Attaching CV / cover letter where required...")
        auto_upload_files(page, fields, cv if cv.exists() else None,
                          cover if cover.exists() else None, report)

        _set_status(
            job_id,
            stage="awaiting_human",
            message=("Form filled. Review the tab, fix anything Claude got wrong, "
                     "then submit manually. Close the tab when you're done."),
            report=report.to_dict(),
        )

        _wait_until_tab_closed(page)
        _set_status(job_id, stage="done", message="Tab closed.")
        return get_status(job_id)

    except Exception as exc:
        logger.exception("autofill failed for %s", job_id)
        _set_status(job_id, stage="error", error=f"{exc.__class__.__name__}: {exc}")
        return get_status(job_id)


def _looks_like_dashboard(page) -> bool:
    """True if a page is the local dashboard (we never autofill our own UI)."""
    try:
        url = (page.url or "").lower()
    except Exception:
        return False
    return "127.0.0.1" in url or "localhost" in url


def _wait_until_tab_closed(page) -> None:
    """Block until the given tab is closed by the user. The other tabs
    (notably the dashboard) stay open."""
    if page is None:
        return
    while True:
        try:
            if page.is_closed():
                return
        except Exception:
            return
        time_module = __import__("time")
        time_module.sleep(1.5)


def _cleanup_stale_lockfile(profile_dir: Path) -> None:
    """Remove the Chromium ``lockfile`` if no live chrome.exe is using it.

    On Windows, killing the parent process with taskkill /F (or the dev
    server reloading mid-launch) leaves the profile's lockfile behind.
    The next launch then fails with exitCode=21 'profile already in use'.

    We only delete the lockfile when there's no chrome.exe whose
    --user-data-dir matches our profile path — otherwise we'd corrupt a
    legitimately-running session.
    """
    lock = profile_dir / "lockfile"
    if not lock.exists():
        return

    profile_str = str(profile_dir).lower()
    try:
        import subprocess
        # WMIC is deprecated but still ships with Win11 — it's the simplest
        # way to inspect the command line of running processes from the shell.
        out = subprocess.run(
            ["wmic", "process", "where", "name='chrome.exe'", "get", "CommandLine", "/format:csv"],
            capture_output=True, text=True, timeout=8,
        )
        cmdlines = (out.stdout or "").lower()
        if profile_str in cmdlines:
            # A chrome.exe is genuinely using this profile — leave it alone
            logger.info("autofill: lockfile present and a chrome.exe is using the profile — not removing")
            return
    except Exception as exc:
        logger.debug("autofill: could not inspect chrome processes (%s); removing lockfile anyway", exc)

    try:
        lock.unlink()
        logger.info("autofill: removed stale lockfile from %s", profile_dir)
    except Exception as exc:
        logger.warning("autofill: could not remove stale lockfile: %s", exc)


def _wait_for_form_in_any_tab(context, timeout_s: int = 600, poll_s: float = 2.0,
                              skip_predicate=None):
    """Poll every tab in the context until one shows a real application form.

    Returns ``(page, fields)`` when a tab passes the threshold, or
    ``(None, [])`` if the user closes everything before a form appears.

    Args:
        context: BrowserContext
        timeout_s: how long to keep polling
        poll_s: poll interval
        skip_predicate: optional callable(page) -> bool. If True for a page,
            we skip it (used to avoid matching the dashboard tab itself).
    """
    import time as _t
    from .extractor import extract_form_fields
    from .navigator import dismiss_cookie_banner

    deadline = _t.time() + timeout_s

    while _t.time() < deadline:
        try:
            pages = [p for p in context.pages if not p.is_closed()]
        except Exception:
            return None, []
        if not pages:
            return None, []

        for p in pages:
            try:
                if skip_predicate is not None and skip_predicate(p):
                    continue
                url = p.url
                if not url or url == "about:blank":
                    continue

                try:
                    dismiss_cookie_banner(p)
                except Exception:
                    pass

                fields = extract_form_fields(p)
                if len(fields) >= 3:
                    return p, fields
            except Exception:
                continue

        _t.sleep(poll_s)

    return None, []


def _wait_until_browser_closed(context) -> None:
    """Block silently until the user closes every page in the context.

    Replaces ``page.pause()`` (which opens the Playwright Inspector — visually
    confusing and unreliable on some Windows setups). Polls every 1.5s until
    no pages remain open, then returns so the with-block can dispose Chromium.
    """
    import time as _t
    while True:
        try:
            pages = [p for p in context.pages if not p.is_closed()]
        except Exception:
            return
        if not pages:
            return
        _t.sleep(1.5)


# -------------------------------------------------------------------
# Convenience: enqueue on the singleton BrowserWorker (used by FastAPI)
# -------------------------------------------------------------------

def run_autofill_async(job, analysis, dashboard_url: str | None = None) -> None:
    """Enqueue an autofill task on the shared browser worker.

    The worker owns a single Chromium with the dashboard in tab 1; each
    autofill task opens a new tab in that same browser. Chromium install
    check (which uses sync_playwright) runs inside the worker thread to
    avoid Playwright greenlet conflicts with FastAPI's asyncio loop.
    """
    from .browser_worker import get_worker
    worker = get_worker(dashboard_url=dashboard_url)
    worker.submit_autofill(job, analysis)
