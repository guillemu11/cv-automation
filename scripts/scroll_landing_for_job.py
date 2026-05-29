"""CLI: produce a scroll-driven campaign landing for a job in scored_jobs.json.

Usage:
  python scripts/scroll_landing_for_job.py --job-id <id> [--brand-url <url>] \
      [--parent <parent_name>] [--angle "<free text brief>"] \
      [--provider anthropic|gemini|chatqueue]

If ``--brand-url`` is omitted the script will try the company website inferred
from ``job.url`` (or fall back to ``https://<company>.com``).
"""
from __future__ import annotations

import logging
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import click

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.analyzer import JobAnalysis
from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import scroll_landing

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)-5s  %(name)s  %(message)s", datefmt="%H:%M:%S")


def _load_job(job_id: str) -> tuple[Job, JobAnalysis]:
    import json
    scored = json.loads((settings.data_dir / "scored_jobs.json").read_text(encoding="utf-8"))
    rec = next((r for r in scored if r.get("id", "").startswith(job_id)), None)
    if not rec:
        raise SystemExit(f"Job not found: {job_id}")
    job = Job(
        id=rec["id"], title=rec["title"], company=rec["company"],
        location=rec["location"], url=rec.get("url", ""), source=rec.get("source", "linkedin"),
        description=rec.get("description", ""),
    )
    analysis = JobAnalysis(
        score=rec.get("ai_score", 50), tier=rec.get("ai_tier", "Warm"),
        skills_match=rec.get("skills_match", []), missing_skills=rec.get("missing_skills", []),
        sector_fit=rec.get("sector_fit", ""), seniority_fit=rec.get("seniority_fit", ""),
        red_flags=rec.get("red_flags", []), ats_keywords=rec.get("ats_keywords", []),
        reasoning=rec.get("reasoning", ""),
    )
    return job, analysis


def _guess_brand_url(job: Job) -> str:
    """Best-effort: derive a brand URL from the job posting URL or company name."""
    if job.url:
        parsed = urlparse(job.url)
        host = parsed.netloc.lower()
        # skip job boards
        if not any(b in host for b in ("linkedin", "naukri", "indeed", "glassdoor", "bayt", "gulftalent", "bebee", "google", "basecareer")):
            return f"{parsed.scheme}://{parsed.netloc}/"
    slug = re.sub(r"[^a-z0-9]+", "", job.company.lower())
    return f"https://www.{slug}.com/"


@click.command()
@click.option("--job-id", required=True, help="Job ID or prefix from scored_jobs.json")
@click.option("--brand-url", default=None, help="Override the brand URL (sub-brand site recommended)")
@click.option("--parent", default=None, help="Parent brand display name (e.g. 'PepsiCo')")
@click.option("--angle", default=None, help="Free-text angle brief; otherwise LLM picks 1 of 3")
@click.option("--provider", default=None, type=click.Choice(["anthropic", "gemini", "chatqueue"]),
              help="Override LLM_PROVIDER for this run")
def main(job_id, brand_url, parent, angle, provider):
    if provider:
        settings.llm_provider = provider
        click.echo(f"[setup] llm_provider -> {provider}")

    job, analysis = _load_job(job_id)
    brand_url = brand_url or _guess_brand_url(job)
    click.echo(f"[start] {job.title} @ {job.company} ({job.location})")
    click.echo(f"        brand-url: {brand_url}")
    click.echo(f"        parent:    {parent or '(infer)'}")
    click.echo(f"        angle:     {angle or '(LLM picks)'}")

    out = scroll_landing.build_landing(
        job, analysis,
        brand_url=brand_url,
        parent_brand_name=parent,
        angle_brief=angle,
    )
    click.echo(f"\n[done] open {out}")


if __name__ == "__main__":
    main()
