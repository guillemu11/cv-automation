"""In-process orchestration API for chat-driven workflows.

This module is the bridge between a chat agent (Claude Code, Cowork) and the
existing pipeline. The agent reads jobs from the dashboard's data files,
**reasons** about each artefact (scoring, CV, cover letter, deliverable,
form responses, outreach), and calls the functions here to persist the
result exactly where the FastAPI dashboard already looks for it.

Why not just hit the REST endpoints?
  - In ``LLM_PROVIDER=chatqueue`` mode each endpoint blocks waiting for a
    chat reply. An agent driving from chat can't write to the queue AND
    answer it without deadlock.
  - Going in-process lets the agent pass its own reasoning straight into
    the generators via ``llm.override()``, skipping API/chatqueue entirely.

Design rules:
  - Every function takes a ``job_id`` and the **fully-reasoned content**
    needed for that artefact. The agent does the LLM work; this module
    just plumbs.
  - Persistence paths match exactly what the dashboard already polls
    (``output/CV_Paula_*.pdf``, ``data/outreach/{job_id}.json``,
    ``data/contacts/{job_id}.json``, ``data/scored_jobs.json``).
  - Functions return a small dict ``{ok, path|payload, ...}`` so the CLI
    wrapper can print a one-line summary.

All functions are safe to call repeatedly — re-running a generator just
overwrites the existing output.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from . import llm
from .analyzer import JobAnalysis, _tier
from .config import settings
from .discovery.normalize import Job

logger = logging.getLogger(__name__)


# -------------------------------------------------------------------
# Shared helpers (mirrors career_ops/webapp/api.py)
# -------------------------------------------------------------------

def _scored_jobs_path() -> Path:
    return settings.data_dir / "scored_jobs.json"


def _load_jobs_raw() -> list[dict]:
    path = _scored_jobs_path()
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def _save_jobs_raw(jobs: list[dict]) -> None:
    path = _scored_jobs_path()
    path.write_text(json.dumps(jobs, indent=2, ensure_ascii=False), encoding="utf-8")


def _find_job(job_id: str) -> dict | None:
    """Match by full id or prefix (same convention as the dashboard)."""
    for j in _load_jobs_raw():
        if j.get("id", "").startswith(job_id):
            return j
    return None


def _reconstruct(job_data: dict) -> tuple[Job, JobAnalysis]:
    job = Job(
        id=job_data["id"],
        title=job_data.get("title", ""),
        company=job_data.get("company", ""),
        location=job_data.get("location", ""),
        url=job_data.get("url", ""),
        source=job_data.get("source", "indeed"),
        description=job_data.get("description", ""),
        salary_raw=job_data.get("salary_raw"),
    )
    analysis = JobAnalysis(
        score=job_data.get("ai_score", 50),
        tier=job_data.get("ai_tier", "Warm"),
        skills_match=job_data.get("skills_match", []),
        missing_skills=job_data.get("missing_skills", []),
        sector_fit=job_data.get("sector_fit", ""),
        seniority_fit=job_data.get("seniority_fit", ""),
        red_flags=job_data.get("red_flags", []),
        ats_keywords=job_data.get("ats_keywords", []),
        reasoning=job_data.get("reasoning", ""),
        scored_by=job_data.get("scored_by", ""),
    )
    return job, analysis


# -------------------------------------------------------------------
# Discovery / listing
# -------------------------------------------------------------------

def list_jobs(
    tier: str | None = None,
    status: str | None = None,
    needs: str | None = None,
    limit: int = 50,
) -> list[dict]:
    """Return jobs filtered by tier/status/needs. Lightweight projection.

    ``needs`` filters by missing artefacts:
      - "cv"          → no ``output/CV_Paula_<company>_<title>.pdf|docx``
      - "contacts"    → no ``data/contacts/{job_id}.json``
      - "outreach"    → no ``data/outreach/{job_id}.json`` OR no versions inside
      - "form"        → no ``output/FORM_Paula_*.json``
      - "deliverable" → no ``output/Deliverable_Paula_*``
    """
    jobs = _load_jobs_raw()
    if tier:
        t = tier.lower()
        jobs = [j for j in jobs if (j.get("ai_tier") or "").lower() == t]
    if status:
        jobs = [j for j in jobs if j.get("status", "Inbox") == status]

    output = settings.output_dir
    contacts_dir = settings.data_dir / "contacts"
    outreach_dir = settings.data_dir / "outreach"

    def _has_file(prefix: str, j: dict) -> bool:
        # Reuse the dashboard's sanitization logic loosely — we don't need
        # exact filename match, just "does any file exist that mentions
        # this company AND this job title".
        co = (j.get("company") or "").replace(" ", "_")[:50]
        ti = (j.get("title") or "").replace(" ", "_")[:50]
        if not co or not ti:
            return False
        for f in output.glob(f"{prefix}_Paula_*"):
            stem = f.stem
            if co in stem and ti in stem:
                return True
        return False

    if needs:
        n = needs.lower()
        if n == "cv":
            jobs = [j for j in jobs if not _has_file("CV", j)]
        elif n == "contacts":
            jobs = [j for j in jobs if not (contacts_dir / f"{j['id']}.json").exists()]
        elif n == "outreach":
            def _has_outreach(j: dict) -> bool:
                p = outreach_dir / f"{j['id']}.json"
                if not p.exists():
                    return False
                try:
                    data = json.loads(p.read_text(encoding="utf-8"))
                except json.JSONDecodeError:
                    return False
                return any(c.get("versions") for c in data.values()) if isinstance(data, dict) else False
            jobs = [j for j in jobs if not _has_outreach(j)]
        elif n == "form":
            jobs = [j for j in jobs if not _has_file("FORM", j)]
        elif n == "deliverable":
            jobs = [j for j in jobs if not _has_file("Deliverable", j)]
        else:
            raise ValueError(f"Unknown needs filter: {needs!r}")

    projection = []
    for j in jobs[:limit]:
        projection.append({
            "id": j["id"],
            "tier": j.get("ai_tier"),
            "score": j.get("ai_score"),
            "status": j.get("status", "Inbox"),
            "company": j.get("company"),
            "title": j.get("title"),
            "location": j.get("location"),
            "url": j.get("url"),
        })
    return projection


def show_job(job_id: str) -> dict | None:
    """Full record for a single job — used by the agent to read JD/profile data."""
    return _find_job(job_id)


# -------------------------------------------------------------------
# Status mutation
# -------------------------------------------------------------------

def set_status(job_id: str, new_status: str) -> dict:
    jobs = _load_jobs_raw()
    for j in jobs:
        if j.get("id", "").startswith(job_id):
            old = j.get("status", "Inbox")
            j["status"] = new_status
            _save_jobs_raw(jobs)
            return {"ok": True, "job_id": j["id"], "old": old, "new": new_status}
    return {"ok": False, "error": f"job not found: {job_id}"}


# -------------------------------------------------------------------
# Scoring (analyzer)
# -------------------------------------------------------------------

def score_job(job_id: str, analysis: dict) -> dict:
    """Persist a chat-reasoned analysis for a job.

    ``analysis`` must contain the fields produced by analyzer's
    ``submit_analysis`` tool: score, skills_match, missing_skills,
    sector_fit, seniority_fit, ats_keywords, reasoning (red_flags
    optional). Patches the row in ``data/scored_jobs.json`` in place.
    """
    jobs = _load_jobs_raw()
    target = None
    for j in jobs:
        if j.get("id", "").startswith(job_id):
            target = j
            break
    if not target:
        return {"ok": False, "error": f"job not found: {job_id}"}

    score = int(analysis.get("score", 0))
    target["ai_score"] = score
    target["ai_tier"] = _tier(score)
    target["skills_match"] = analysis.get("skills_match", [])
    target["missing_skills"] = analysis.get("missing_skills", [])
    target["sector_fit"] = analysis.get("sector_fit", "")
    target["seniority_fit"] = analysis.get("seniority_fit", "")
    target["red_flags"] = analysis.get("red_flags", [])
    target["ats_keywords"] = analysis.get("ats_keywords", [])
    target["reasoning"] = analysis.get("reasoning", "")
    target["scored_by"] = "agent_ops:chat"

    _save_jobs_raw(jobs)

    # Mirror to analyzer sqlite cache so a re-run of the pipeline doesn't
    # re-queue this job for scoring.
    try:
        from .analyzer import JobAnalysis, _cache_set, _get_cache_conn
        conn = _get_cache_conn()
        ja = JobAnalysis(
            score=score,
            tier=_tier(score),
            skills_match=target["skills_match"],
            missing_skills=target["missing_skills"],
            sector_fit=target["sector_fit"],
            seniority_fit=target["seniority_fit"],
            red_flags=target["red_flags"],
            ats_keywords=target["ats_keywords"],
            reasoning=target["reasoning"],
            scored_by="agent_ops:chat",
        )
        _cache_set(conn, target["id"], ja)
        conn.close()
    except Exception:  # noqa: BLE001
        logger.exception("could not mirror score to analyzer sqlite cache")

    return {"ok": True, "job_id": target["id"], "score": score, "tier": _tier(score)}


# -------------------------------------------------------------------
# CV
# -------------------------------------------------------------------

def generate_cv(job_id: str, cv_content: dict) -> dict:
    """Generate the adapted CV using chat-reasoned content.

    ``cv_content`` must match ``submit_cv_content`` input_schema (see
    ``career_ops/generators/cv_generator.py``).
    """
    from .generators.cv_generator import generate_cv as _gen

    job_data = _find_job(job_id)
    if not job_data:
        return {"ok": False, "error": f"job not found: {job_id}"}

    job, analysis = _reconstruct(job_data)
    with llm.override({"submit_cv_content": cv_content}):
        path = _gen(job, analysis)
    if path is None:
        return {"ok": False, "error": "generator returned None — check templates and logs"}

    # Mirror the dashboard's behaviour: bump status to CV Ready once the file is on disk.
    _set_status_if_below(job_id, "CV Ready")
    return {"ok": True, "job_id": job.id, "path": str(path)}


# -------------------------------------------------------------------
# Cover letter
# -------------------------------------------------------------------

def generate_cover_letter(job_id: str, letter_content: dict, contact_name: str | None = None) -> dict:
    """Generate the cover letter using chat-reasoned content.

    ``letter_content`` keys: ``opening_paragraph``, ``body_paragraph_1``,
    ``body_paragraph_2``, ``closing_paragraph``.
    """
    from .generators.cover_letter import generate_cover_letter as _gen

    job_data = _find_job(job_id)
    if not job_data:
        return {"ok": False, "error": f"job not found: {job_id}"}

    job, analysis = _reconstruct(job_data)
    with llm.override({"submit_cover_letter": letter_content}):
        path = _gen(job, analysis, contact_name=contact_name)
    if path is None:
        return {"ok": False, "error": "generator returned None — check templates"}
    return {"ok": True, "job_id": job.id, "path": str(path)}


# -------------------------------------------------------------------
# Deliverable
# -------------------------------------------------------------------

def generate_deliverable(
    job_id: str,
    deliverable_content: dict,
    deliverable_type: str,
    company_url: str | None = None,
) -> dict:
    """Generate a value-add deliverable using chat-reasoned content.

    ``deliverable_type`` ∈ {digital_audit, ecommerce_teardown, brand_analysis, action_plan}.
    ``deliverable_content`` keys: title, subtitle, sections[], closing.
    """
    from .generators.deliverables import generate_deliverable as _gen

    job_data = _find_job(job_id)
    if not job_data:
        return {"ok": False, "error": f"job not found: {job_id}"}

    job, analysis = _reconstruct(job_data)
    with llm.override({"submit_deliverable": deliverable_content}):
        path = _gen(job, analysis, deliverable_type=deliverable_type, company_url=company_url)
    if path is None:
        return {"ok": False, "error": "generator returned None"}
    return {"ok": True, "job_id": job.id, "type": deliverable_type, "path": str(path)}


# -------------------------------------------------------------------
# Form responses
# -------------------------------------------------------------------

def generate_form_responses(job_id: str, responses: dict, ats_platform: str | None = None) -> dict:
    """Generate ATS form responses using chat-reasoned content.

    ``responses`` keys: see ``submit_form_responses`` input_schema.
    """
    from .generators.form_responses import generate_form_responses as _gen

    job_data = _find_job(job_id)
    if not job_data:
        return {"ok": False, "error": f"job not found: {job_id}"}

    job, analysis = _reconstruct(job_data)
    with llm.override({"submit_form_responses": responses}):
        result = _gen(job, analysis, ats_platform=ats_platform)
    if result is None:
        return {"ok": False, "error": "generator returned None"}
    pdf_path, json_path = result
    return {"ok": True, "job_id": job.id, "pdf": str(pdf_path), "json": str(json_path)}


# -------------------------------------------------------------------
# Outreach (per contact)
# -------------------------------------------------------------------

def generate_outreach_for_contact(
    job_id: str,
    contact_id: str,
    variant: str,
    message: dict,
) -> dict:
    """Persist a chat-reasoned outreach message for a specific contact.

    ``variant`` ∈ {email, linkedin_connection, linkedin_inmail}.
    ``message`` must include all keys from ``submit_outreach`` schema
    (email_subject, email_body, linkedin_connection, linkedin_inmail) —
    only the requested variant is stored; the rest is kept for record.
    """
    from . import outreach_store
    from .generators.outreach import generate_outreach as _gen

    if variant not in outreach_store.VARIANTS:
        return {"ok": False, "error": f"invalid variant {variant!r}"}

    job_data = _find_job(job_id)
    if not job_data:
        return {"ok": False, "error": f"job not found: {job_id}"}

    contact = _find_contact(job_data["id"], contact_id)
    if not contact:
        return {"ok": False, "error": f"contact not found: {contact_id}"}

    job, analysis = _reconstruct(job_data)
    with llm.override({"submit_outreach": message}):
        content = _gen(job, analysis, contact_name=contact.get("name"))
    if content is None:
        return {"ok": False, "error": "generator returned None"}

    # Pick the body for the requested variant
    body_map = {
        "email": (content.email_subject, content.email_body),
        "linkedin_connection": ("", content.linkedin_connection),
        "linkedin_inmail": ("", content.linkedin_inmail),
    }
    subject, body = body_map[variant]
    outreach_store.add_version(
        job_id=job.id,
        contact_id=contact_id,
        variant=variant,
        subject=subject,
        body=body,
        author="agent_ops:chat",
    )
    return {"ok": True, "job_id": job.id, "contact_id": contact_id, "variant": variant}


def _find_contact(job_id: str, contact_id: str) -> dict | None:
    path = settings.data_dir / "contacts" / f"{job_id}.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    for c in data:
        # contact_id convention: c_<sha1(name+linkedin_url)[:10]>
        import hashlib
        cid = "c_" + hashlib.sha1(
            ((c.get("name") or "") + (c.get("linkedin_url") or "")).encode("utf-8")
        ).hexdigest()[:10]
        if cid == contact_id:
            c["_id"] = cid
            return c
    return None


# -------------------------------------------------------------------
# Contacts
# -------------------------------------------------------------------

def save_contacts(job_id: str, contacts: list[dict]) -> dict:
    """Persist chat-discovered contacts for a job.

    ``contacts``: list of dicts with keys matching ``contact_finder.Contact``:
    ``name``, ``title``, ``company``, ``email`` (optional), ``linkedin_url``
    (optional), ``role_type``, ``source``.

    Useful when the chat agent finds contacts via WebSearch and wants to
    register them in the dashboard's contact tray for outreach generation.
    """
    job_data = _find_job(job_id)
    if not job_data:
        return {"ok": False, "error": f"job not found: {job_id}"}

    contacts_dir = settings.data_dir / "contacts"
    contacts_dir.mkdir(parents=True, exist_ok=True)
    p = contacts_dir / f"{job_data['id']}.json"
    p.write_text(json.dumps(contacts, indent=2, ensure_ascii=False), encoding="utf-8")

    from datetime import datetime, timezone
    meta = {
        "searched_at": datetime.now(timezone.utc).isoformat(),
        "count": len(contacts),
        "company": job_data["company"],
        "job_title": job_data["title"],
        "via": "agent_ops:chat",
    }
    (contacts_dir / f"{job_data['id']}.meta.json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8",
    )
    return {"ok": True, "job_id": job_data["id"], "count": len(contacts)}


# -------------------------------------------------------------------
# Internal helpers
# -------------------------------------------------------------------

_STATUSES_AFTER_CV_READY = {
    "CV Ready", "Applied", "Followed Up", "Interview", "Offer", "Rejected",
}


def _set_status_if_below(job_id: str, target_status: str) -> None:
    """Promote a job to ``target_status`` unless it's already further along."""
    jobs = _load_jobs_raw()
    changed = False
    for j in jobs:
        if not j.get("id", "").startswith(job_id):
            continue
        current = j.get("status", "Inbox")
        if target_status == "CV Ready" and current in _STATUSES_AFTER_CV_READY:
            return
        j["status"] = target_status
        changed = True
        break
    if changed:
        _save_jobs_raw(jobs)
