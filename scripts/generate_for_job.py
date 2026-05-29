#!/usr/bin/env python3
"""Generate CV + cover letter + outreach for a specific job.

Usage:
    python scripts/generate_for_job.py --job-id <id>
    python scripts/generate_for_job.py --job-id <id> --email recruiter@example.com
    python scripts/generate_for_job.py --list          # show available jobs

Reads from the analysis cache (data/analysis_cache.sqlite) and scored jobs
(data/scored_jobs.json). Generates all documents to output/.
"""
from __future__ import annotations

import json
import logging
import sqlite3
import sys
from pathlib import Path

import click

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.analyzer import JobAnalysis
from career_ops.config import settings
from career_ops.contact_finder import Contact, find_contacts
from career_ops.discovery.normalize import Job
from career_ops.generators import generate_cover_letter, generate_cv, generate_form_responses
from career_ops.generators.deliverables import DELIVERABLE_TYPES, generate_all_deliverables, generate_deliverable
from career_ops.generators.outreach import create_outreach_draft, generate_outreach

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)-5s  %(message)s", datefmt="%H:%M:%S")
logger = logging.getLogger(__name__)


def _load_scored_jobs() -> list[dict]:
    """Load scored jobs from data/scored_jobs.json."""
    path = settings.data_dir / "scored_jobs.json"
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _find_job(job_id: str, scored: list[dict]) -> tuple[Job, JobAnalysis] | None:
    """Find a job by ID (exact or prefix match) in scored jobs."""
    for rec in scored:
        if rec.get("id", "").startswith(job_id):
            # Reconstruct Job and JobAnalysis from the flat dict
            job = Job(
                id=rec["id"],
                title=rec.get("title", ""),
                company=rec.get("company", ""),
                location=rec.get("location", ""),
                url=rec.get("url", ""),
                source=rec.get("source", "indeed"),
                description=rec.get("description", ""),
                salary_raw=rec.get("salary_raw"),
            )
            analysis = JobAnalysis(
                score=rec.get("ai_score", rec.get("score", 50)),
                tier=rec.get("ai_tier", rec.get("tier", "Warm")),
                skills_match=rec.get("skills_match", []),
                missing_skills=rec.get("missing_skills", []),
                sector_fit=rec.get("sector_fit", ""),
                seniority_fit=rec.get("seniority_fit", ""),
                red_flags=rec.get("red_flags", []),
                ats_keywords=rec.get("ats_keywords", []),
                reasoning=rec.get("reasoning", ""),
            )
            return job, analysis
    return None


@click.command()
@click.option("--job-id", type=str, help="Job ID (or prefix) to generate for")
@click.option("--email", type=str, default=None, help="Recruiter email for outreach draft")
@click.option("--contact", type=str, default=None, help="Contact name for cover letter")
@click.option("--list", "list_jobs", is_flag=True, help="List available jobs with scores")
@click.option("--cv-only", is_flag=True, help="Only generate CV")
@click.option("--cl-only", is_flag=True, help="Only generate cover letter")
@click.option("--outreach-only", is_flag=True, help="Only generate outreach messages")
@click.option("--form-only", is_flag=True, help="Only generate form responses")
@click.option("--contacts", "find_contacts_flag", is_flag=True, help="Find contacts at the company via Apollo")
@click.option("--deliverable", type=str, default=None,
              help="Generate deliverable (digital_audit|ecommerce_teardown|brand_analysis|action_plan|all|auto)")
@click.option("--ats", type=str, default=None, help="ATS platform hint (workday, lever, greenhouse, etc.)")
def main(job_id, email, contact, list_jobs, cv_only, cl_only, outreach_only, form_only,
         find_contacts_flag, deliverable, ats):
    """Generate personalized application materials for a specific job."""
    scored = _load_scored_jobs()

    if not scored:
        click.echo("No scored jobs found. Run the pipeline first: python -m career_ops")
        sys.exit(1)

    if list_jobs:
        click.echo(f"\n{'ID':<18} {'Score':>5}  {'Tier':<5}  {'Title':<40}  {'Company':<25}")
        click.echo("-" * 100)
        for rec in sorted(scored, key=lambda x: x.get("ai_score", x.get("score", 0)), reverse=True):
            score = rec.get("ai_score", rec.get("score", "?"))
            tier = rec.get("ai_tier", rec.get("tier", "?"))
            click.echo(
                f"{rec.get('id', '?'):<18} "
                f"{score:>5}  "
                f"{tier:<5}  "
                f"{rec.get('title', '?')[:40]:<40}  "
                f"{rec.get('company', '?')[:25]:<25}"
            )
        return

    if not job_id:
        click.echo("Provide --job-id <id> or use --list to see available jobs")
        sys.exit(1)

    result = _find_job(job_id, scored)
    if not result:
        click.echo(f"Job not found: {job_id}")
        click.echo("Use --list to see available jobs")
        sys.exit(1)

    job, analysis = result
    click.echo(f"\nGenerating for: {job.title} @ {job.company} (score: {analysis.score})")

    generate_all = not (cv_only or cl_only or outreach_only or form_only
                        or find_contacts_flag or deliverable)
    cv_path = None
    cl_path = None
    form_json_path = None
    form_pdf_path = None
    deliverable_path = None
    contacts: list[Contact] = []

    # --- CV ---
    if generate_all or cv_only:
        cv_path = generate_cv(job, analysis)
        if cv_path:
            click.echo(f"  CV:           {cv_path}")
        else:
            click.echo("  CV:           FAILED (check logs)")

    # --- Cover Letter ---
    if generate_all or cl_only:
        cl_path = generate_cover_letter(job, analysis, contact_name=contact)
        if cl_path:
            click.echo(f"  Cover Letter: {cl_path}")
        else:
            click.echo("  Cover Letter: FAILED (check logs)")

    # --- Outreach ---
    if generate_all or outreach_only:
        outreach = generate_outreach(job, analysis, contact_name=contact)
        if outreach:
            click.echo(f"\n  Email Subject: {outreach.email_subject}")
            click.echo(f"  LinkedIn Note: {outreach.linkedin_connection}")

            if email:
                draft_id = create_outreach_draft(
                    job, analysis, email, contact_name=contact,
                    cv_path=cv_path, cl_path=cl_path, deliverable_path=deliverable_path,
                )
                if draft_id:
                    click.echo(f"  Email Draft:   {draft_id}")
            elif contacts:
                # Use first contact with an email
                email_contact = next((c for c in contacts if c.email), None)
                if email_contact:
                    draft_id = create_outreach_draft(
                        job, analysis, email_contact.email,
                        contact_name=email_contact.name,
                        cv_path=cv_path, cl_path=cl_path, deliverable_path=deliverable_path,
                    )
                    if draft_id:
                        click.echo(f"  Email Draft:   {draft_id} (to {email_contact.name})")
                else:
                    click.echo("  (no contacts with email found — use --email to create a draft)")
            else:
                click.echo("  (use --email or --contacts to create a draft)")
        else:
            click.echo("  Outreach:     FAILED (check logs)")

    # --- Form Responses ---
    if generate_all or form_only:
        form_result = generate_form_responses(job, analysis, ats_platform=ats)
        if form_result:
            form_json_path, form_pdf_path = form_result
            click.echo(f"  Form (JSON):  {form_json_path}")
            click.echo(f"  Form (PDF):   {form_pdf_path}")
        else:
            click.echo("  Form:         FAILED (check logs)")

    # --- Contact Finding ---
    if generate_all or find_contacts_flag:
        contacts = find_contacts(job.company, job.title, job.description or "")
        if contacts:
            click.echo(f"\n  Contacts found ({len(contacts)}):")
            for c in contacts:
                email_str = c.email or "no email"
                li_str = c.linkedin_url or "no LinkedIn"
                click.echo(f"    [{c.role_type}] {c.name} — {c.title}")
                click.echo(f"      Email: {email_str}")
                click.echo(f"      LinkedIn: {li_str}")

            # Sync to Notion
            from career_ops.notion_sync import sync_contacts as _sync_contacts
            contact_stats = _sync_contacts(contacts)
            if contact_stats["inserted"]:
                click.echo(f"    → {contact_stats['inserted']} contacts synced to Notion")
        else:
            click.echo("\n  Contacts:     None found (check Apollo API key)")

    # --- Deliverables ---
    if deliverable:
        click.echo("")
        if deliverable == "all":
            click.echo("  Generating all 4 deliverable types...")
            paths = generate_all_deliverables(job, analysis)
            for p in paths:
                click.echo(f"  Deliverable:  {p}")
            if paths:
                deliverable_path = paths[0]  # use first for email attachment
        else:
            dtype = None if deliverable == "auto" else deliverable
            if dtype and dtype not in DELIVERABLE_TYPES:
                click.echo(f"  Unknown type: {dtype} (valid: {', '.join(DELIVERABLE_TYPES)}, all, auto)")
            else:
                deliverable_path = generate_deliverable(job, analysis, deliverable_type=dtype)
                if deliverable_path:
                    click.echo(f"  Deliverable:  {deliverable_path}")
                else:
                    click.echo("  Deliverable:  FAILED (check logs)")

    # --- Upload to Notion ---
    from career_ops.notion_cv import update_job_with_cv
    outreach_data = outreach if "outreach" in dir() and outreach else None
    ok = update_job_with_cv(
        job_id=job.id,
        cv_path=cv_path,
        cl_path=cl_path,
        form_path=form_pdf_path,
        outreach_email_subject=outreach_data.email_subject if outreach_data else "",
        outreach_email_body=outreach_data.email_body if outreach_data else "",
        outreach_linkedin=outreach_data.linkedin_connection if outreach_data else "",
    )
    if ok:
        click.echo("\n  Notion:       Updated -> CV Ready")
    else:
        click.echo("\n  Notion:       SKIPPED (check config)")

    click.echo("\nDone!")


if __name__ == "__main__":
    main()
