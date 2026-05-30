"""FastAPI backend for the Career Ops dashboard.

Serves the SPA, provides REST API for jobs, documents, and pipeline control.
All data comes from the existing pipeline files (scored_jobs.json, output/).
"""
from __future__ import annotations

import json
import logging
import math
import re
import threading
from datetime import date
from pathlib import Path

from fastapi import BackgroundTasks, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

from ..config import settings

logger = logging.getLogger(__name__)

app = FastAPI(title="Career Ops", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (JS, CSS)
STATIC_DIR = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Expose the output/ tree so per-job landings can be navigated to in-browser.
# Each landing is self-contained (HTML + CSS + JS + assets) under
# output/<Company_Role>/landing/, and the browser fetches sibling files via
# relative URLs once it has loaded index.html.
app.mount("/output", StaticFiles(directory=str(settings.output_dir)), name="output")

# Pipeline run state
_pipeline_state = {"running": False, "last_run": None, "last_result": None}
_pipeline_lock = threading.Lock()


@app.on_event("startup")
def _startup_sync() -> None:
    """At server boot: scan output/ and reconcile job statuses with disk.

    Catches CVs generated outside the dashboard (CLI scripts, prior crashed
    runs) so the table doesn't show 'Inbox' for jobs that already have a CV.
    """
    try:
        all_jobs = _load_jobs(include_hidden=True)
        n = _sync_status_from_disk(all_jobs)
        if n:
            logger.info("startup status reconcile: patched %d jobs", n)
    except Exception as exc:  # noqa: BLE001
        logger.exception("startup status reconcile failed: %s", exc)


@app.on_event("startup")
def _startup_browser() -> None:
    """Launch Chromium with the dashboard in tab 1 as soon as the server is up.

    Disabled when ``CAREEROPS_AUTO_BROWSER=0`` (e.g. running in CI).
    Disabled if Playwright isn't installed yet — autofill clicks will still
    install Chromium on demand.
    """
    import os
    import subprocess
    import sys as _sys
    if os.environ.get("CAREEROPS_AUTO_BROWSER", "1") == "0":
        return

    try:
        import playwright  # noqa: F401
    except ImportError:
        logger.info("playwright not installed; skipping auto-browser launch")
        return

    # Quick check: does Chromium binary exist? If not, install it before the
    # worker tries to use it. Running this at startup avoids doing it from
    # the FastAPI handler (which is async and would conflict with sync_playwright).
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            try:
                b = pw.chromium.launch(headless=True)
                b.close()
            except Exception:
                logger.info("Installing Chromium binary (one-off, ~150MB)...")
                subprocess.run(
                    [_sys.executable, "-m", "playwright", "install", "chromium"],
                    capture_output=True, timeout=300,
                )
    except Exception as exc:
        logger.warning("auto-browser: Chromium install check failed: %s", exc)

    # Default to localhost on the configured port. The endpoint /autofill
    # also passes the request's base_url, so a wrong default here only
    # affects the very first auto-launch (which can navigate later if needed).
    port = int(os.environ.get("CAREEROPS_PORT", "0") or 0)
    dashboard_url = f"http://127.0.0.1:{port}/" if port else "http://127.0.0.1:8064/"

    try:
        from ..autofill.browser_worker import get_worker
        worker = get_worker(dashboard_url=dashboard_url)
        worker.start()
        logger.info("auto-browser: BrowserWorker started, dashboard will load at %s", dashboard_url)
    except Exception:
        logger.exception("auto-browser: failed to start BrowserWorker")


# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------

def _sanitize_json(obj):
    """Replace NaN/Inf floats with None.

    Pandas-backed sources (jobspy) leak NaN into raw.job_type when the source
    has no value for that field. Python's json.dump accepts NaN by default, but
    Starlette's response encoder does not, causing /api/jobs to 500.
    """
    if isinstance(obj, float):
        if math.isnan(obj) or math.isinf(obj):
            return None
        return obj
    if isinstance(obj, dict):
        return {k: _sanitize_json(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_sanitize_json(v) for v in obj]
    return obj


def _load_jobs(include_hidden: bool = False) -> list[dict]:
    """Load scored jobs from data/scored_jobs.json.

    By default excludes Cold tier and `expired` freshness — the dashboard only
    surfaces actionable, possibly-still-live jobs. Pass include_hidden=True to
    get the raw list (used by stats and admin endpoints).
    """
    path = settings.data_dir / "scored_jobs.json"
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        jobs = _sanitize_json(json.load(f))
    if include_hidden:
        return jobs
    visible = []
    for j in jobs:
        tier = str(j.get("ai_tier", j.get("tier", ""))).strip().lower()
        if tier == "cold":
            continue
        fresh = str(j.get("freshness", "")).strip().lower()
        if fresh == "expired":
            continue
        visible.append(j)
    return visible


def _save_jobs(jobs: list[dict]) -> None:
    """Save jobs back to scored_jobs.json."""
    path = settings.data_dir / "scored_jobs.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=2, ensure_ascii=False)


# Statuses that are "ahead of" CV Ready in the pipeline. We don't want to
# downgrade Applied / Interview / Offer just because a CV file exists on disk.
_STATUSES_AFTER_CV_READY = {
    "CV Ready", "Applied", "Followed Up", "Interview", "Offer", "Rejected",
}


def _sync_status_from_disk(jobs: list[dict]) -> int:
    """Patch jobs whose CV exists on disk but status is still Inbox.

    Returns count of jobs patched. Persists to disk if any changed.
    Idempotent — safe to call repeatedly.
    """
    files_index = _index_generated_files(jobs)
    changed = 0
    for j in jobs:
        files = files_index.get(j["id"], {})
        if not files.get("cv"):
            continue
        current = j.get("status", "Inbox")
        if current in _STATUSES_AFTER_CV_READY:
            continue
        # CV file exists, but status doesn't reflect it — patch it.
        j["status"] = "CV Ready"
        changed += 1
    if changed:
        _save_jobs(jobs)
        logger.info("status sync: patched %d jobs to CV Ready (CV file present)", changed)
    return changed


def _find_job(job_id: str, jobs: list[dict]) -> dict | None:
    """Find a job by ID or prefix."""
    for j in jobs:
        if j.get("id", "").startswith(job_id):
            return j
    return None


def _get_stats(jobs: list[dict]) -> dict:
    """Compute dashboard stats."""
    stats = {
        "total": len(jobs), "hot": 0, "warm": 0, "cold": 0,
        "fresh": 0, "active_old": 0, "expired": 0, "unknown": 0,
    }
    status_counts: dict[str, int] = {}
    for j in jobs:
        tier = j.get("ai_tier", j.get("tier", "")).lower()
        if tier == "hot":
            stats["hot"] += 1
        elif tier == "warm":
            stats["warm"] += 1
        elif tier == "cold":
            stats["cold"] += 1
        fresh = str(j.get("freshness", "")).lower()
        if fresh in stats:
            stats[fresh] += 1
        status = j.get("status", "Inbox")
        status_counts[status] = status_counts.get(status, 0) + 1
    stats["by_status"] = status_counts
    return stats


_FILENAME_SANITIZE = re.compile(r'[<>:"/\\|?*]')


def _job_filename_key(job: dict) -> tuple[str, str]:
    """Build the (company, title) stems used when naming generated files."""
    company = _FILENAME_SANITIZE.sub("", job.get("company", "")).strip().replace(" ", "_")[:50]
    title = _FILENAME_SANITIZE.sub("", job.get("title", "")).strip().replace(" ", "_")[:50]
    return company, title


def _index_generated_files(jobs: list[dict]) -> dict[str, dict]:
    """Walk output/ recursively and return {job_id: {cv, cl, form, form_json, deliverable}}.

    Files are now organised one folder per job (e.g. ``output/Gloria_Jeans/CV...``).
    We rglob the tree so the dashboard finds them, but skip ``_archive/``,
    ``notes/`` and ``landings/`` so historical or auxiliary files don't get
    re-indexed as if they were current.
    """
    output = settings.output_dir
    result: dict[str, dict] = {
        j["id"]: {"cv": None, "cl": None, "form": None, "form_json": None,
                  "deliverable": None, "deliverables": [], "outreach": None,
                  "links": [], "landing": None}
        for j in jobs
    }
    # Pre-compute filename keys so the inner loop is pure string matching.
    job_keys: list[tuple[str, tuple[str, str]]] = [
        (j["id"], _job_filename_key(j)) for j in jobs
    ]

    _EXCLUDED_TOP_DIRS = {"_archive", "notes", "landings"}

    def _scan(pattern: str) -> list[Path]:
        # rglob picks up both root-level files and per-job subfolders. We
        # filter out the archive/notes/landings trees so historical content
        # doesn't masquerade as live job output, and skip Office lock files
        # (``~$Foo.docx``) which would otherwise match *.docx patterns.
        hits = []
        for f in output.rglob(pattern):
            if f.name.startswith("~$"):
                continue
            try:
                rel = f.relative_to(output)
            except ValueError:
                continue
            if rel.parts and rel.parts[0] in _EXCLUDED_TOP_DIRS:
                continue
            hits.append(f)
        return hits

    patterns = {
        "cv": "CV_Paula_*.pdf",
        "cl": "CL_Paula_*.pdf",
        "form": "FORM_Paula_*.pdf",
        "form_docx": "FORM_Paula_*.docx",
        "form_json": "FORM_Paula_*.json",
        "deliverable_pdf": "Deliverable_Paula_*.pdf",
        "deliverable_docx": "Deliverable_Paula_*.docx",
        "outreach": "*_Outreach_Pack.docx",
        "links": "LINKS_Paula_*.json",
    }
    cached = {key: _scan(pat) for key, pat in patterns.items()}

    def _match(files: list[Path]) -> dict[str, str]:
        # Store the path relative to output_dir (e.g. "Gloria_Jeans/CV.pdf")
        # so the download endpoints can resolve it via ``output_dir / value``
        # regardless of whether the file lives at the root or in a per-job
        # subfolder.
        out: dict[str, str] = {}
        for f in files:
            stem = f.stem
            try:
                rel = f.relative_to(output)
            except ValueError:
                rel = Path(f.name)
            for job_id, (company, title) in job_keys:
                if job_id in out:
                    continue
                if company and title and company in stem and title in stem:
                    out[job_id] = str(rel).replace("\\", "/")
                    break
        return out

    def _match_multi_by_company(files: list[Path]) -> dict[str, list[str]]:
        # Concept-named artifacts (e.g. Deliverable_Paula_Henkel_Frizz-Forecast,
        # Henkel_Outreach_Pack) carry the company but NOT the role title, so the
        # strict company+title matcher above misses them. Match on company alone;
        # when several jobs share a company, prefer the one whose title also
        # appears in the stem. Returns ALL matches per job (a job can have many
        # deliverables), relative-to-output and sorted for stable ordering.
        out: dict[str, list[str]] = {}
        for f in sorted(files, key=lambda p: p.name):
            stem = f.stem
            try:
                rel = f.relative_to(output)
            except ValueError:
                rel = Path(f.name)
            candidates = [(jid, comp, ttl) for jid, (comp, ttl) in job_keys
                          if comp and comp in stem]
            if not candidates:
                continue
            # Prefer a candidate whose title also matches; else first by company.
            best = next((c for c in candidates if c[2] and c[2] in stem), candidates[0])
            out.setdefault(best[0], []).append(str(rel).replace("\\", "/"))
        return out

    for job_id, name in _match(cached["cv"]).items():
        result[job_id]["cv"] = name
    for job_id, name in _match(cached["cl"]).items():
        result[job_id]["cl"] = name
    for job_id, name in _match(cached["form"]).items():
        result[job_id]["form"] = name
    # Fallback: DOCX if no PDF
    for job_id, name in _match(cached["form_docx"]).items():
        if not result[job_id]["form"]:
            result[job_id]["form"] = name
    for job_id, name in _match(cached["form_json"]).items():
        result[job_id]["form_json"] = name

    # Deliverables: collect ALL (pdf + docx) per job by company. If a *_FULL.pdf
    # exists, surface only it (its Deck/Plan parts are already merged inside —
    # the Henkel case); otherwise keep every deliverable (Opella has 4 distinct
    # docx analyses and no FULL). ``deliverable`` (singular) stays for back-compat.
    deliverable_hits = _match_multi_by_company(
        cached["deliverable_pdf"] + cached["deliverable_docx"]
    )
    for job_id, names in deliverable_hits.items():
        full = [n for n in names if n.lower().endswith("_full.pdf")]
        chosen = full if full else names
        result[job_id]["deliverables"] = chosen
        result[job_id]["deliverable"] = chosen[0] if chosen else None

    # Outreach pack docx (named "<Company>_Outreach_Pack.docx") — company match.
    for job_id, names in _match_multi_by_company(cached["outreach"]).items():
        result[job_id]["outreach"] = names[0]

    # External links sidecars (deployed Vercel landings etc.) — company match.
    for job_id, names in _match_multi_by_company(cached["links"]).items():
        merged: list[dict] = []
        for rel in names:
            try:
                data = json.loads((output / rel).read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                continue
            if isinstance(data, list):
                merged.extend(e for e in data if isinstance(e, dict) and e.get("url"))
        result[job_id]["links"] = merged

    # Landings live at output/<Company_Role>/landing/index.html — expose as URL.
    # Folder names use job_output_dir's sanitisation (spaces preserved), while
    # job_keys uses _job_filename_key (spaces -> underscores). Normalise both
    # to lowercase-underscore form before substring matching.
    def _norm(s: str) -> str:
        out = s.replace(" ", "_").lower()
        # Collapse repeated underscores so "Brand / Marketing" (which sanitises
        # to "Brand__Marketing" in filenames but stays single-underscored in
        # folder names) still substring-matches.
        while "__" in out:
            out = out.replace("__", "_")
        return out

    for landing in output.rglob("landing/index.html"):
        try:
            rel = landing.relative_to(output)
        except ValueError:
            continue
        if rel.parts and rel.parts[0] in _EXCLUDED_TOP_DIRS:
            continue
        folder_norm = _norm(rel.parts[0])
        for job_id, (company, title) in job_keys:
            if company and title and _norm(company) in folder_norm and _norm(title) in folder_norm:
                result[job_id]["landing"] = "/output/" + str(rel).replace("\\", "/")
                break

    return result


def _index_pending_llm(jobs: list[dict]) -> dict[str, list[dict]]:
    """Walk data/chat_queue/inbox/ and return {job_id: [{id, kind, tool, caller, created_at}, ...]}.

    Match heuristic: a request belongs to a job if both the job's company and
    title appear as substrings inside the request's ``user`` field. This is the
    same loose-match style used by ``_index_generated_files`` for output/ files.
    """
    inbox = settings.chatqueue_dir / "inbox"
    result: dict[str, list[dict]] = {j["id"]: [] for j in jobs}
    if not inbox.exists():
        return result

    job_keys: list[tuple[str, str, str]] = [
        (j["id"], (j.get("company") or "").lower(), (j.get("title") or "").lower())
        for j in jobs
    ]

    for f in inbox.glob("*.json"):
        try:
            req = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        user = (req.get("user") or "").lower()
        if not user:
            continue
        for job_id, company, title in job_keys:
            if company and title and company in user and title in user:
                result[job_id].append({
                    "id": req.get("id"),
                    "kind": req.get("kind"),
                    "tool": req.get("tool_name"),
                    "caller": req.get("caller"),
                    "created_at": req.get("created_at"),
                })
                break
    return result


def _generated_files(job_id: str, jobs: list[dict] | None = None) -> dict:
    """Single-job lookup used by /api/jobs/{job_id}. Not used by the list endpoint."""
    jobs = jobs if jobs is not None else _load_jobs()
    job = _find_job(job_id, jobs)
    if not job:
        return {"cv": None, "cl": None, "form": None, "form_json": None,
                "deliverable": None, "deliverables": [], "outreach": None,
                "links": [], "landing": None}
    return _index_generated_files([job]).get(
        job["id"],
        {"cv": None, "cl": None, "form": None, "form_json": None,
         "deliverable": None, "deliverables": [], "outreach": None,
         "links": [], "landing": None},
    )


# -------------------------------------------------------------------
# SPA entry point
# -------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def index():
    """Serve the SPA."""
    index_path = STATIC_DIR / "index.html"
    return index_path.read_text(encoding="utf-8")


@app.get("/job/{job_id}", response_class=HTMLResponse)
async def job_page(job_id: str):
    """Serve the SPA for job detail (client-side routing)."""
    index_path = STATIC_DIR / "index.html"
    return index_path.read_text(encoding="utf-8")


# -------------------------------------------------------------------
# API: Jobs
# -------------------------------------------------------------------

@app.get("/api/jobs")
async def list_jobs(
    tier: str | None = None,
    status: str | None = None,
    q: str | None = None,
    include_hidden: bool = False,
):
    """List all jobs, optionally filtered.

    By default Cold tier and expired-freshness jobs are hidden. Pass
    include_hidden=true to surface them (admin/debug only).
    """
    jobs = _load_jobs(include_hidden=include_hidden)

    if tier:
        tier_l = tier.lower()
        jobs = [j for j in jobs if j.get("ai_tier", j.get("tier", "")).lower() == tier_l]
    if status:
        jobs = [j for j in jobs if j.get("status", "Inbox") == status]
    if q:
        q_lower = q.lower()
        jobs = [j for j in jobs if q_lower in j.get("title", "").lower() or q_lower in j.get("company", "").lower()]

    # Add generated file info — single pass over output/ for ALL jobs.
    files_index = _index_generated_files(jobs)
    pending_index = _index_pending_llm(jobs)
    for j in jobs:
        j["_files"] = files_index.get(j["id"], {
            "cv": None, "cl": None, "form": None, "form_json": None,
            "deliverable": None, "deliverables": [], "outreach": None,
            "links": [], "landing": None,
        })
        j["_pending_llm"] = pending_index.get(j["id"], [])

    return {"jobs": jobs, "stats": _get_stats(_load_jobs(include_hidden=True))}


@app.get("/api/jobs/{job_id}")
async def get_job(job_id: str):
    """Get a single job with full details."""
    jobs = _load_jobs(include_hidden=True)
    job = _find_job(job_id, jobs)
    if not job:
        raise HTTPException(404, f"Job not found: {job_id}")
    job["_files"] = _generated_files(job["id"])
    job["_pending_llm"] = _index_pending_llm([job]).get(job["id"], [])
    return job


@app.post("/api/jobs/{job_id}/status")
async def update_status(job_id: str, body: dict):
    """Update a job's status."""
    new_status = body.get("status")
    if not new_status:
        raise HTTPException(400, "Missing 'status' field")

    jobs = _load_jobs(include_hidden=True)
    job = _find_job(job_id, jobs)
    if not job:
        raise HTTPException(404, f"Job not found: {job_id}")

    job["status"] = new_status
    _save_jobs(jobs)
    return {"ok": True, "status": new_status}


@app.post("/api/jobs/{job_id}/generate")
async def generate_documents(job_id: str, background_tasks: BackgroundTasks):
    """Trigger CV + CL + outreach generation for a job."""
    jobs = _load_jobs(include_hidden=True)
    job_data = _find_job(job_id, jobs)
    if not job_data:
        raise HTTPException(404, f"Job not found: {job_id}")

    def _generate():
        from ..generators import generate_cover_letter, generate_cv
        from ..generators.outreach import generate_outreach
        from ..notion_cv import update_job_with_cv

        job, analysis = _reconstruct_job(job_data)

        cv_path = generate_cv(job, analysis)
        cl_path = generate_cover_letter(job, analysis)
        outreach = generate_outreach(job, analysis)

        # Speculative targets: in lieu of the docx deliverable, build a
        # navigable HTML landing under output/<Company_Role>/landing/.
        # The dashboard exposes it via /api/jobs/{id}/landing.
        if (job.raw or {}).get("speculative"):
            try:
                from ..generators import generate_landing
                generate_landing(job, analysis)
            except Exception:
                logger.exception("speculative landing generation failed for %s", job.id)

        # Update status — load FULL list (not the dashboard-filtered one) so
        # we don't accidentally drop Cold/expired rows when saving.
        all_jobs = _load_jobs(include_hidden=True)
        target = _find_job(job_id, all_jobs)
        if target:
            target["status"] = "CV Ready"
            _save_jobs(all_jobs)

        # Update Notion
        update_job_with_cv(
            job_id=job.id,
            cv_path=cv_path,
            cl_path=cl_path,
            outreach_email_subject=outreach.email_subject if outreach else "",
            outreach_email_body=outreach.email_body if outreach else "",
            outreach_linkedin=outreach.linkedin_connection if outreach else "",
        )

    background_tasks.add_task(_generate)
    return {"ok": True, "message": "Generation started in background"}


def _landing_url_for(job_data: dict) -> str | None:
    """Return the in-dashboard URL to a job's landing, or None if not built yet."""
    from ..generators._paths import job_output_dir
    from ..discovery.normalize import Job

    job = Job(
        id=job_data["id"],
        title=job_data.get("title", ""),
        company=job_data.get("company", ""),
        location=job_data.get("location", ""),
        url=job_data.get("url", ""),
        source=job_data.get("source", "indeed"),
        description="",
    )
    index = job_output_dir(job) / "landing" / "index.html"
    if not index.exists():
        return None
    rel = index.relative_to(settings.output_dir)
    return "/output/" + str(rel).replace("\\", "/")


# -------------------------------------------------------------------
# API: Documents
# -------------------------------------------------------------------

@app.get("/api/jobs/{job_id}/cv")
async def download_cv(job_id: str):
    """Download the generated CV PDF."""
    files = _generated_files(job_id)
    if not files["cv"]:
        raise HTTPException(404, "CV not generated yet")
    path = settings.output_dir / files["cv"]
    return FileResponse(str(path), media_type="application/pdf", filename=Path(files["cv"]).name)


@app.get("/api/jobs/{job_id}/cl")
async def download_cl(job_id: str):
    """Download the generated Cover Letter PDF."""
    files = _generated_files(job_id)
    if not files["cl"]:
        raise HTTPException(404, "Cover letter not generated yet")
    path = settings.output_dir / files["cl"]
    return FileResponse(str(path), media_type="application/pdf", filename=Path(files["cl"]).name)


@app.get("/api/jobs/{job_id}/form")
async def download_form(job_id: str):
    """Download the generated Form Responses (PDF or DOCX)."""
    files = _generated_files(job_id)
    if not files["form"]:
        raise HTTPException(404, "Form responses not generated yet")
    path = settings.output_dir / files["form"]
    media = "application/pdf" if files["form"].endswith(".pdf") else "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    return FileResponse(str(path), media_type=media, filename=Path(files["form"]).name)


@app.get("/api/jobs/{job_id}/form-json")
async def download_form_json(job_id: str):
    """Download the form responses JSON (machine-readable)."""
    files = _generated_files(job_id)
    if not files.get("form_json"):
        raise HTTPException(404, "Form responses JSON not generated yet")
    path = settings.output_dir / files["form_json"]
    return FileResponse(str(path), media_type="application/json", filename=Path(files["form_json"]).name)


@app.get("/api/jobs/{job_id}/deliverable")
async def download_deliverable(job_id: str):
    """Download the generated Deliverable PDF."""
    files = _generated_files(job_id)
    if not files["deliverable"]:
        raise HTTPException(404, "Deliverable not generated yet")
    path = settings.output_dir / files["deliverable"]
    return FileResponse(str(path), media_type="application/pdf", filename=Path(files["deliverable"]).name)


@app.get("/api/jobs/{job_id}/outreach-pack")
async def download_outreach_pack(job_id: str):
    """Download the personalized outreach pack (.docx)."""
    files = _generated_files(job_id)
    if not files.get("outreach"):
        raise HTTPException(404, "Outreach pack not generated yet")
    path = settings.output_dir / files["outreach"]
    return FileResponse(
        str(path),
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename=Path(files["outreach"]).name,
    )


@app.get("/api/jobs/{job_id}/landing")
async def get_landing_url(job_id: str):
    """Return the in-dashboard URL of this job's landing deliverable.

    The frontend uses this to render an 'Open landing →' link on speculative
    job cards. Returns ``{url: null}`` if the landing hasn't been generated
    yet so the UI can show a disabled state.
    """
    jobs = _load_jobs(include_hidden=True)
    job_data = _find_job(job_id, jobs)
    if not job_data:
        raise HTTPException(404, f"Job not found: {job_id}")
    return {"url": _landing_url_for(job_data)}


# -------------------------------------------------------------------
# API: Contacts
# -------------------------------------------------------------------

@app.post("/api/jobs/{job_id}/contacts")
async def find_job_contacts(job_id: str, background_tasks: BackgroundTasks):
    """Find hiring manager + peer contacts for a job via Google→LinkedIn.

    User-initiated, so we ignore PIPELINE_DRY_RUN (which protects the batch
    pipeline only). Returns immediately; results are written to
    data/contacts/<job_id>.json and the frontend polls GET to retrieve them.
    """
    jobs = _load_jobs(include_hidden=True)
    job_data = _find_job(job_id, jobs)
    if not job_data:
        raise HTTPException(404, f"Job not found: {job_id}")

    def _find():
        # Bypass dry-run for explicit user action from the dashboard.
        prev_dry = settings.dry_run
        settings.dry_run = False
        try:
            from ..contact_finder import find_contacts
            contacts = find_contacts(
                company=job_data.get("company", ""),
                job_title=job_data.get("title", ""),
                job_description=job_data.get("description", ""),
            )
        finally:
            settings.dry_run = prev_dry
        contacts_dir = settings.data_dir / "contacts"
        contacts_dir.mkdir(parents=True, exist_ok=True)
        contacts_path = contacts_dir / f"{job_id}.json"
        meta_path = contacts_dir / f"{job_id}.meta.json"
        with contacts_path.open("w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in contacts], f, indent=2, ensure_ascii=False)
        from datetime import datetime, timezone
        meta = {
            "searched_at": datetime.now(timezone.utc).isoformat(),
            "count": len(contacts),
            "company": job_data.get("company", ""),
            "job_title": job_data.get("title", ""),
        }
        with meta_path.open("w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2, ensure_ascii=False)

    background_tasks.add_task(_find)
    return {"ok": True, "message": "Contact search started"}


@app.get("/api/jobs/{job_id}/contacts")
async def get_job_contacts(job_id: str):
    """Get saved contacts for a job, enriched with outreach state.

    Each contact is augmented with `id` (stable hash for outreach storage),
    `outreach_status`, `outreach_preview` (first ~140 chars of current body),
    and `outreach_variant` so the dashboard can render cards in one round trip.
    """
    from .. import outreach_store

    contacts_path = settings.data_dir / "contacts" / f"{job_id}.json"
    meta_path = settings.data_dir / "contacts" / f"{job_id}.meta.json"
    if not contacts_path.exists():
        return {"contacts": [], "meta": None}
    with contacts_path.open("r", encoding="utf-8") as f:
        contacts = json.load(f)

    outreach = outreach_store.load(job_id)
    for c in contacts:
        cid = outreach_store.contact_id(c.get("name", ""), c.get("linkedin_url"))
        c["id"] = cid
        co = outreach.get(cid)
        if co and co.current():
            cur = co.current()
            c["outreach_status"] = co.status
            c["outreach_variant"] = cur.variant
            c["outreach_preview"] = cur.body[:140]
            c["outreach_versions"] = len(co.versions)
        else:
            c["outreach_status"] = "pending"
            c["outreach_variant"] = None
            c["outreach_preview"] = None
            c["outreach_versions"] = 0

    meta = None
    if meta_path.exists():
        with meta_path.open("r", encoding="utf-8") as f:
            meta = json.load(f)
    return {"contacts": contacts, "meta": meta}


# -------------------------------------------------------------------
# API: Outreach messages (per contact, with versioning)
# -------------------------------------------------------------------

def _load_contacts_raw(job_id: str) -> list[dict]:
    p = settings.data_dir / "contacts" / f"{job_id}.json"
    if not p.exists():
        return []
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def _find_contact_by_id(job_id: str, contact_id: str) -> dict | None:
    from .. import outreach_store
    for c in _load_contacts_raw(job_id):
        if outreach_store.contact_id(c.get("name", ""), c.get("linkedin_url")) == contact_id:
            return c
    return None


def _generate_one_message(job_data: dict, contact: dict, variant: str) -> str:
    """Run Claude for a single contact+variant, return the message body."""
    from ..generators.outreach import generate_outreach

    job, analysis = _reconstruct_job(job_data)
    content = generate_outreach(job, analysis, contact_name=contact.get("name"))
    if not content:
        raise RuntimeError("outreach generation failed")
    if variant == "linkedin_connection":
        return content.linkedin_connection
    if variant == "linkedin_inmail":
        return content.linkedin_inmail
    if variant == "email":
        # Strip basic HTML tags for the dashboard preview/edit experience.
        body = content.email_body
        return f"Subject: {content.email_subject}\n\n{body}"
    raise ValueError(f"unknown variant: {variant}")


@app.get("/api/jobs/{job_id}/outreach")
async def get_outreach(job_id: str):
    """Return the full outreach map: {contact_id: {versions, status, ...}}."""
    from .. import outreach_store
    data = outreach_store.load(job_id)
    return {cid: co.to_dict() for cid, co in data.items()}


# Tracks batch generation so the frontend can poll progress.
_batch_state: dict[str, dict] = {}
_batch_lock = threading.Lock()


# IMPORTANT: literal-path routes (generate-all, batch-status) MUST be declared
# BEFORE the parametric `/{contact_id}` route. FastAPI matches routes in
# declaration order — putting the parametric one first would make it swallow
# "generate-all" as a contact_id and 404 with "Contact not found: generate-all".
@app.post("/api/jobs/{job_id}/outreach/generate-all")
async def generate_outreach_all(job_id: str, background_tasks: BackgroundTasks, body: dict = {}):
    """Generate messages for every contact without one (status='pending').

    Pass `force=true` to regenerate everyone regardless of state. Runs in
    background; poll /outreach/batch-status for progress.
    """
    from .. import outreach_store

    jobs = _load_jobs(include_hidden=True)
    job_data = _find_job(job_id, jobs)
    if not job_data:
        raise HTTPException(404, f"Job not found: {job_id}")

    variant = body.get("variant", "linkedin_connection")
    force = bool(body.get("force", False))
    contacts = _load_contacts_raw(job_id)

    with _batch_lock:
        if _batch_state.get(job_id, {}).get("running"):
            return {"ok": False, "message": "Batch already running for this job"}
        _batch_state[job_id] = {
            "running": True, "total": 0, "done": 0, "failed": 0, "errors": [],
        }

    def _run():
        existing = outreach_store.load(job_id)
        targets: list[dict] = []
        for c in contacts:
            cid = outreach_store.contact_id(c.get("name", ""), c.get("linkedin_url"))
            co = existing.get(cid)
            if force or not co or co.status == "pending" or not co.current():
                targets.append({"contact": c, "cid": cid})

        with _batch_lock:
            _batch_state[job_id]["total"] = len(targets)

        for t in targets:
            try:
                msg = _generate_one_message(job_data, t["contact"], variant)
                outreach_store.add_version(job_id, t["cid"], variant, msg)
                with _batch_lock:
                    _batch_state[job_id]["done"] += 1
            except Exception as exc:  # noqa: BLE001
                logger.exception("batch outreach failed for %s", t["cid"])
                with _batch_lock:
                    _batch_state[job_id]["failed"] += 1
                    _batch_state[job_id]["errors"].append({
                        "contact": t["contact"].get("name", ""), "error": str(exc),
                    })

        with _batch_lock:
            _batch_state[job_id]["running"] = False

    background_tasks.add_task(_run)
    return {"ok": True, "total": len(contacts), "variant": variant}


@app.get("/api/jobs/{job_id}/outreach/batch-status")
async def outreach_batch_status(job_id: str):
    return _batch_state.get(job_id, {"running": False, "total": 0, "done": 0, "failed": 0})


@app.post("/api/jobs/{job_id}/outreach/{contact_id}")
async def generate_outreach_for_contact(job_id: str, contact_id: str, body: dict = {}):
    """Generate (or regenerate) a message for one contact. Synchronous — one
    Claude call takes 3-5s, fast enough to await without backgrounding."""
    from .. import outreach_store

    # Defense against route-order bugs: contact_ids are always `c_<hex>`.
    # If something else lands here (e.g. "generate-all" because a literal
    # route was declared after this one), reject early instead of matching it
    # as a (missing) contact.
    if not contact_id.startswith("c_"):
        raise HTTPException(404, f"Not a contact id: {contact_id}")

    jobs = _load_jobs(include_hidden=True)
    job_data = _find_job(job_id, jobs)
    if not job_data:
        raise HTTPException(404, f"Job not found: {job_id}")
    contact = _find_contact_by_id(job_id, contact_id)
    if not contact:
        raise HTTPException(404, f"Contact not found: {contact_id}")

    variant = body.get("variant", "linkedin_connection")
    if variant not in outreach_store.VARIANTS:
        raise HTTPException(400, f"Invalid variant: {variant}")

    try:
        msg = _generate_one_message(job_data, contact, variant)
    except Exception as exc:
        logger.exception("outreach generation failed for %s", contact_id)
        raise HTTPException(500, f"Generation failed: {exc}") from exc

    co = outreach_store.add_version(job_id, contact_id, variant, msg)
    return {"ok": True, "contact_id": contact_id, "outreach": co.to_dict()}


@app.post("/api/jobs/{job_id}/outreach/{contact_id}/edit")
async def edit_outreach(job_id: str, contact_id: str, body: dict):
    from .. import outreach_store
    new_body = body.get("body")
    if new_body is None:
        raise HTTPException(400, "Missing 'body' field")
    co = outreach_store.update_body(job_id, contact_id, new_body)
    if not co:
        raise HTTPException(404, "No message to edit")
    return {"ok": True, "outreach": co.to_dict()}


@app.post("/api/jobs/{job_id}/outreach/{contact_id}/version")
async def switch_version(job_id: str, contact_id: str, body: dict):
    from .. import outreach_store
    v = body.get("version")
    if not isinstance(v, int):
        raise HTTPException(400, "Missing integer 'version'")
    co = outreach_store.set_current(job_id, contact_id, v)
    if not co:
        raise HTTPException(404, "Version not found")
    return {"ok": True, "outreach": co.to_dict()}


@app.post("/api/jobs/{job_id}/outreach/{contact_id}/status")
async def set_outreach_status(job_id: str, contact_id: str, body: dict):
    from .. import outreach_store
    status = body.get("status")
    if status not in outreach_store.STATUSES:
        raise HTTPException(400, f"Invalid status. Must be one of {outreach_store.STATUSES}")
    co = outreach_store.set_status(job_id, contact_id, status)
    if not co:
        raise HTTPException(404, "Contact has no outreach yet")
    return {"ok": True, "outreach": co.to_dict()}


# -------------------------------------------------------------------
# API: Form Responses
# -------------------------------------------------------------------

@app.post("/api/jobs/{job_id}/form-responses")
async def generate_form(job_id: str, background_tasks: BackgroundTasks, body: dict = {}):
    """Generate form responses for a job."""
    jobs = _load_jobs(include_hidden=True)
    job_data = _find_job(job_id, jobs)
    if not job_data:
        raise HTTPException(404, f"Job not found: {job_id}")

    def _gen():
        from ..analyzer import JobAnalysis
        from ..discovery.normalize import Job
        from ..generators.form_responses import generate_form_responses

        job, analysis = _reconstruct_job(job_data)
        generate_form_responses(job, analysis, ats_platform=body.get("ats_platform"))

    background_tasks.add_task(_gen)
    return {"ok": True, "message": "Form responses generation started"}


# -------------------------------------------------------------------
# API: Autofill (open browser + fill ATS form)
# -------------------------------------------------------------------

@app.post("/api/jobs/{job_id}/autofill")
async def autofill_job(job_id: str, request: Request):
    """Generate form responses if missing, then open a new tab in the shared
    Chromium and autofill the form.

    All autofill tabs share the same Chromium window as the dashboard, so
    Paula sees a single browser with multiple tabs (dashboard + one tab per
    autofill in flight).
    Runs on the BrowserWorker thread; poll /api/jobs/{job_id}/autofill/status.
    """
    jobs = _load_jobs(include_hidden=True)
    job_data = _find_job(job_id, jobs)
    if not job_data:
        raise HTTPException(404, f"Job not found: {job_id}")

    if not job_data.get("url"):
        raise HTTPException(400, "Job has no application URL")

    # Build dashboard URL from the incoming request — the worker will load
    # this into tab 1 the first time it starts a Chromium.
    base = str(request.base_url).rstrip("/")
    from ..autofill.runner import run_autofill_async
    job, analysis = _reconstruct_job(job_data)
    run_autofill_async(job, analysis, dashboard_url=base)
    return {"ok": True, "message": "Autofill queued — a new tab will open in the dashboard's Chromium."}


@app.get("/api/jobs/{job_id}/autofill/status")
async def autofill_status(job_id: str):
    """Return the current stage of an in-flight autofill run."""
    from ..autofill.runner import get_status
    return get_status(job_id)


# -------------------------------------------------------------------
# API: Deliverables
# -------------------------------------------------------------------

@app.post("/api/jobs/{job_id}/deliverable")
async def generate_job_deliverable(job_id: str, background_tasks: BackgroundTasks, body: dict = {}):
    """Generate a value-add deliverable for a job."""
    jobs = _load_jobs(include_hidden=True)
    job_data = _find_job(job_id, jobs)
    if not job_data:
        raise HTTPException(404, f"Job not found: {job_id}")

    def _gen():
        try:
            from ..generators.deliverables import generate_deliverable

            job, analysis = _reconstruct_job(job_data)
            out = generate_deliverable(
                job, analysis,
                deliverable_type=body.get("deliverable_type"),
                company_url=body.get("company_url"),
            )
            logger.info("deliverable background task done: %s", out)
        except Exception:
            logger.exception("deliverable background task crashed")

    background_tasks.add_task(_gen)
    return {"ok": True, "message": "Deliverable generation started"}


# -------------------------------------------------------------------
# Shared helper: reconstruct Job + JobAnalysis from dict
# -------------------------------------------------------------------

def _reconstruct_job(job_data: dict):
    """Reconstruct Job + JobAnalysis from a scored_jobs.json entry.

    Speculative targets stash extra context (positioning_angle, speculative
    flag, manually-supplied contact email) under the job's ``raw`` dict so
    downstream generators can branch on them without changing Job's schema.
    """
    from ..analyzer import JobAnalysis
    from ..discovery.normalize import Job

    raw = dict(job_data.get("raw") or {})
    for key in ("positioning_angle", "speculative", "speculative_email"):
        if key in job_data and key not in raw:
            raw[key] = job_data[key]

    job = Job(
        id=job_data["id"],
        title=job_data.get("title", ""),
        company=job_data.get("company", ""),
        location=job_data.get("location", ""),
        url=job_data.get("url", ""),
        source=job_data.get("source", "indeed"),
        description=job_data.get("description", ""),
        salary_raw=job_data.get("salary_raw"),
        raw=raw,
    )
    analysis = JobAnalysis(
        score=job_data.get("ai_score", job_data.get("score", 50)),
        tier=job_data.get("ai_tier", job_data.get("tier", "Warm")),
        skills_match=job_data.get("skills_match", []),
        missing_skills=job_data.get("missing_skills", []),
        sector_fit=job_data.get("sector_fit", ""),
        seniority_fit=job_data.get("seniority_fit", ""),
        red_flags=job_data.get("red_flags", []),
        ats_keywords=job_data.get("ats_keywords", []),
        reasoning=job_data.get("reasoning", ""),
    )
    return job, analysis


# -------------------------------------------------------------------
# API: Speculative targets (cold outreach to a company without a posting)
# -------------------------------------------------------------------

@app.get("/api/angles")
async def list_positioning_angles():
    """Return the registered positioning angles for the dashboard dropdown."""
    from ..generators import angles as angles_mod
    return {"angles": angles_mod.list_angles()}


_SPECULATIVE_DESCRIPTION_TEMPLATE = (
    "Speculative outreach — no public posting.\n\n"
    "Paula is reaching out about a potential opportunity at {company} in Dubai. "
    "{notes}\n\n"
    "Campaign angle: {angle_name}.\n"
    "Generators should treat this as a cold introduction to the company, not a "
    "response to a specific vacancy. Lean on the angle's positioning brief when "
    "personalising the CV, cover letter and outreach copy."
)


@app.post("/api/targets/speculative")
async def create_speculative_target(body: dict):
    """Create a speculative target (synthetic job) for cold outreach.

    Body fields:
      - company (str, required)
      - title (str, optional — default 'Marketing Manager (Speculative)')
      - angle (str, required — must be a key from /api/angles)
      - contact_email (str, optional — seeded into the job's contacts)
      - contact_name (str, optional — friendly name for the contact)
      - contact_title (str, optional — used for outreach personalisation)
      - notes (str, optional — extra context appended to the synthetic JD)

    Returns: ``{ok, job_id}`` so the dashboard can navigate to /job/<id>.
    """
    from ..generators import angles as angles_mod
    from ..discovery.normalize import job_hash

    company = (body.get("company") or "").strip()
    angle_key = (body.get("angle") or "").strip()
    if not company:
        raise HTTPException(400, "Missing 'company'")
    angle = angles_mod.get(angle_key)
    if not angle:
        raise HTTPException(400, f"Unknown angle '{angle_key}'. See GET /api/angles.")

    title = (body.get("title") or "Marketing Manager (Speculative)").strip()
    location = (body.get("location") or "Dubai, UAE").strip()
    notes = (body.get("notes") or "").strip() or (
        "Paula has identified the company as a strong fit and the team is "
        "actively hiring or expanding."
    )
    description = _SPECULATIVE_DESCRIPTION_TEMPLATE.format(
        company=company, notes=notes, angle_name=angle.name,
    )

    job_id = job_hash(title, company, location)
    jobs = _load_jobs(include_hidden=True)
    existing = _find_job(job_id, jobs)
    new_entry = {
        "id": job_id,
        "title": title,
        "company": company,
        "location": location,
        "url": (body.get("url") or "").strip(),
        "source": "speculative",
        "description": description,
        "ai_score": 85,
        "ai_tier": "Hot",
        "tier": "Hot",
        "score": 85,
        "skills_match": [],
        "missing_skills": [],
        "sector_fit": "Fashion Retail / Multibrand",
        "seniority_fit": "Mid–Senior",
        "red_flags": [],
        "ats_keywords": [],
        "reasoning": f"Speculative target — angle: {angle.name}",
        "status": "Inbox",
        "freshness": "fresh",
        "speculative": True,
        "positioning_angle": angle.key,
        "speculative_email": (body.get("contact_email") or "").strip() or None,
    }
    if existing:
        # Re-seeding the same target overrides the angle/contact (the user
        # likely changed their mind) but preserves status if past Inbox.
        for k, v in new_entry.items():
            if k == "status" and existing.get("status") not in (None, "", "Inbox"):
                continue
            existing[k] = v
    else:
        jobs.append(new_entry)
    _save_jobs(jobs)

    # Seed a single manual contact if email was supplied — bypasses the
    # SerpAPI/Google→LinkedIn flow entirely. Mirrors contact_finder.Contact
    # shape so the existing dashboard rendering and outreach endpoints work.
    contact_email = (body.get("contact_email") or "").strip()
    if contact_email:
        contact = {
            "name": (body.get("contact_name") or "").strip() or "Hiring Team",
            "title": (body.get("contact_title") or "").strip() or "Hiring Manager",
            "company": company,
            "email": contact_email,
            "linkedin_url": None,
            "role_type": "Hiring Manager",
        }
        contacts_dir = settings.data_dir / "contacts"
        contacts_dir.mkdir(parents=True, exist_ok=True)
        contacts_path = contacts_dir / f"{job_id}.json"
        meta_path = contacts_dir / f"{job_id}.meta.json"
        with contacts_path.open("w", encoding="utf-8") as f:
            json.dump([contact], f, indent=2, ensure_ascii=False)
        from datetime import datetime, timezone
        meta = {
            "searched_at": datetime.now(timezone.utc).isoformat(),
            "count": 1,
            "company": company,
            "job_title": title,
            "manual": True,
        }
        with meta_path.open("w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2, ensure_ascii=False)

    return {"ok": True, "job_id": job_id, "angle": angle.key, "created": not existing}


@app.post("/api/jobs/{job_id}/contacts/manual")
async def add_manual_contact(job_id: str, body: dict):
    """Append a manually-supplied contact to a job. Useful when Paula already
    has an email/name and wants to skip the Google→LinkedIn search.
    """
    name = (body.get("name") or "").strip()
    email = (body.get("email") or "").strip()
    if not name and not email:
        raise HTTPException(400, "Provide at least 'name' or 'email'")

    jobs = _load_jobs(include_hidden=True)
    job_data = _find_job(job_id, jobs)
    if not job_data:
        raise HTTPException(404, f"Job not found: {job_id}")

    contact = {
        "name": name or "Hiring Team",
        "title": (body.get("title") or "").strip() or "Hiring Manager",
        "company": job_data.get("company", ""),
        "email": email or None,
        "linkedin_url": (body.get("linkedin_url") or "").strip() or None,
        "role_type": (body.get("role_type") or "Hiring Manager"),
    }

    contacts_dir = settings.data_dir / "contacts"
    contacts_dir.mkdir(parents=True, exist_ok=True)
    contacts_path = contacts_dir / f"{job_id}.json"
    existing: list[dict] = []
    if contacts_path.exists():
        with contacts_path.open("r", encoding="utf-8") as f:
            existing = json.load(f)
    # De-dupe by email or linkedin_url
    def _key(c: dict) -> str:
        return (c.get("email") or c.get("linkedin_url") or c.get("name") or "").lower()
    if not any(_key(c) == _key(contact) for c in existing):
        existing.append(contact)
    with contacts_path.open("w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

    return {"ok": True, "count": len(existing), "contact": contact}


# -------------------------------------------------------------------
# API: Admin (server lifecycle)
# -------------------------------------------------------------------

@app.post("/api/_admin/restart")
async def admin_restart():
    """Re-execute this Python process so route changes take effect.

    Necessary because uvicorn's auto-reload picks its watcher backend at
    startup — if `watchfiles` was installed AFTER launch, reload silently
    falls back to a poller that doesn't fire on Windows. One restart bridges
    that gap and from then on hot-reload works for every future edit.

    Listens only on 127.0.0.1, so this is a local-dev convenience, not a
    public endpoint.
    """
    import os
    import sys

    def _exec():
        # Defer slightly so the HTTP response can flush before exec replaces us.
        import time
        time.sleep(0.4)
        os.execv(sys.executable, [sys.executable, *sys.argv])

    threading.Thread(target=_exec, daemon=True).start()
    return {"ok": True, "message": "Server restarting…"}


# -------------------------------------------------------------------
# API: Pipeline
# -------------------------------------------------------------------

@app.post("/api/pipeline/run")
async def run_pipeline(background_tasks: BackgroundTasks):
    """Trigger a full pipeline run in the background."""
    with _pipeline_lock:
        if _pipeline_state["running"]:
            return {"ok": False, "message": "Pipeline already running"}
        _pipeline_state["running"] = True

    def _run():
        try:
            from ..pipeline import run
            result = run()
            _pipeline_state["last_result"] = {
                "discovered": result.discovered,
                "dedupe_new": result.dedupe_new,
                "filter_passed": result.filter_passed,
                "analyzed": result.analyzed,
                "hot": result.hot,
                "warm": result.warm,
                "cold": result.cold,
                "duration": round(result.duration_seconds, 1),
            }
            _pipeline_state["last_run"] = date.today().isoformat()
        except Exception as exc:
            logger.exception("pipeline failed: %s", exc)
            _pipeline_state["last_result"] = {"error": str(exc)}
        finally:
            _pipeline_state["running"] = False

    background_tasks.add_task(_run)
    return {"ok": True, "message": "Pipeline started"}


@app.get("/api/pipeline/status")
async def pipeline_status():
    """Check pipeline run status."""
    return _pipeline_state


@app.get("/api/stats")
async def stats():
    """Get dashboard stats."""
    return _get_stats(_load_jobs())


# -------------------------------------------------------------------
# API: Chat-queue (chatqueue provider)
# -------------------------------------------------------------------

@app.get("/api/llm/queue")
async def list_llm_queue():
    """List all pending chatqueue requests across all jobs.

    Used by the dashboard to render a "waiting in chat" tray so Paula can see
    at-a-glance what's stalled on the human-in-the-loop reviewer.
    """
    inbox = settings.chatqueue_dir / "inbox"
    if not inbox.exists():
        return {"pending": [], "provider": settings.llm_provider}

    pending: list[dict] = []
    for f in sorted(inbox.glob("*.json"), key=lambda p: p.stat().st_mtime):
        try:
            req = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        pending.append({
            "id": req.get("id"),
            "kind": req.get("kind"),
            "tool": req.get("tool_name"),
            "caller": req.get("caller"),
            "created_at": req.get("created_at"),
        })
    return {"pending": pending, "provider": settings.llm_provider}


@app.get("/api/llm/requests/{req_id}")
async def get_llm_request(req_id: str):
    """Return the human-readable markdown for a parked chatqueue request.

    The frontend uses this to populate a 'copy to clipboard' button so Guille
    can paste the prompt into a chat (Claude Code / Cowork) without ever
    touching the filesystem.
    """
    inbox = settings.chatqueue_dir / "inbox"
    md = inbox / f"{req_id}.md"
    if not md.exists():
        raise HTTPException(404, f"Request not found: {req_id}")
    return {"id": req_id, "markdown": md.read_text(encoding="utf-8")}
