#!/usr/bin/env python3
"""Interactive scorer calibration script.

Fetches real job postings from Dubai, presents them to Paula one by one,
and asks her to rate each as Hot / Warm / Cold / Reject. Her ratings become
the golden set used as few-shot examples in the analyzer prompt.

Usage:
    python scripts/calibrate_scorer.py              # first calibration (30 jobs)
    python scripts/calibrate_scorer.py --recalibrate # add more examples
    python scripts/calibrate_scorer.py --test        # score golden set & show accuracy

The golden set is saved to data/golden_set.yaml.
"""
from __future__ import annotations

import sys
import textwrap
from pathlib import Path

import click
import yaml

# Ensure project root is on path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from career_ops.config import Settings
import career_ops.config as cfg


def _reload_settings() -> None:
    cfg.get_settings.cache_clear()
    cfg.settings = Settings()


def _fetch_jobs(count: int = 30) -> list:
    """Fetch real jobs for calibration."""
    from career_ops.discovery import jobspy_source

    queries = cfg.settings.target_titles[:6]  # first 6 titles
    jobs = jobspy_source.fetch(
        queries=queries,
        locations=cfg.settings.target_locations,
        limit=max(count // len(queries), 5),
        hours_old=336,  # 2 weeks window for more variety
    )
    # Prefer jobs with descriptions
    with_desc = [j for j in jobs if j.description and len(j.description) > 100]
    without_desc = [j for j in jobs if not j.description or len(j.description) <= 100]
    return (with_desc + without_desc)[:count]


def _present_job(job, index: int, total: int) -> dict | None:
    """Show a job to the user and collect their rating."""
    click.echo(f"\n{'='*70}")
    click.echo(f"  Job {index+1}/{total}")
    click.echo(f"{'='*70}")
    click.echo(f"  Title:    {job.title}")
    click.echo(f"  Company:  {job.company}")
    click.echo(f"  Location: {job.location}")
    click.echo(f"  Source:   {job.source}")
    click.echo(f"  Salary:   {job.salary_raw or 'Not specified'}")
    click.echo(f"  URL:      {job.url[:80]}")

    if job.description:
        click.echo(f"\n  Description (first 800 chars):")
        wrapped = textwrap.fill(job.description[:800], width=72, initial_indent="    ", subsequent_indent="    ")
        click.echo(wrapped)
        if len(job.description) > 800:
            click.echo(f"    ... ({len(job.description)} total chars)")

    click.echo()
    click.echo("  Rate this job for Paula:")
    click.echo("    [H] Hot     — Perfect fit, should apply ASAP")
    click.echo("    [W] Warm    — Decent fit, worth considering")
    click.echo("    [C] Cold    — Poor fit, skip")
    click.echo("    [R] Reject  — Not relevant at all")
    click.echo("    [S] Skip    — Not sure / need more info")
    click.echo("    [Q] Quit    — Save progress and exit")

    while True:
        choice = click.prompt("  Your rating", type=str, default="S").strip().upper()
        if choice in ("H", "W", "C", "R", "S", "Q"):
            break
        click.echo("  Please enter H, W, C, R, S, or Q")

    if choice == "Q":
        return None
    if choice == "S":
        return "skip"

    tier_map = {"H": "Hot", "W": "Warm", "C": "Cold", "R": "Reject"}
    score_map = {"H": 90, "W": 70, "C": 40, "R": 10}

    reasoning = click.prompt("  Why? (brief, or press Enter to skip)", default="", show_default=False)

    return {
        "job_id": job.id,
        "title": job.title,
        "company": job.company,
        "location": job.location,
        "source": job.source,
        "tier": tier_map[choice],
        "score": score_map[choice],
        "reasoning": reasoning or f"Rated {tier_map[choice]} by Paula during calibration",
        "description_preview": (job.description or "")[:500],
    }


def _load_golden_set(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data if isinstance(data, list) else []


def _save_golden_set(path: Path, data: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    click.echo(f"\n  Saved {len(data)} examples to {path}")


@click.command()
@click.option("--count", default=30, help="Number of jobs to present for calibration")
@click.option("--recalibrate", is_flag=True, help="Add more examples to existing golden set")
@click.option("--test", is_flag=True, help="Score the golden set and show accuracy vs Paula's labels")
def main(count: int, recalibrate: bool, test: bool) -> None:
    _reload_settings()
    golden_path = cfg.settings.golden_set_path

    if test:
        _run_test(golden_path)
        return

    click.echo("\n  Career Ops — Scorer Calibration")
    click.echo("  ================================")
    click.echo(f"  This will show you {count} real job postings from Dubai.")
    click.echo("  Rate each one for Paula (Hot / Warm / Cold / Reject).")
    click.echo("  Your ratings train the AI scorer to match your judgment.\n")

    existing = _load_golden_set(golden_path) if recalibrate else []
    existing_ids = {e["job_id"] for e in existing}

    if existing and not recalibrate:
        if not click.confirm(f"  {len(existing)} existing examples found. Overwrite?", default=False):
            click.echo("  Use --recalibrate to add more. Exiting.")
            return
        existing = []
        existing_ids = set()

    click.echo("  Fetching jobs from Indeed + LinkedIn...")
    jobs = _fetch_jobs(count + 10)  # extra in case some are skipped
    # Filter out already-rated jobs
    jobs = [j for j in jobs if j.id not in existing_ids]
    click.echo(f"  Found {len(jobs)} new jobs to rate.\n")

    if not jobs:
        click.echo("  No new jobs to rate. Try increasing --count or wait for new postings.")
        return

    rated = list(existing)
    for i, job in enumerate(jobs[:count]):
        result = _present_job(job, i, min(count, len(jobs)))
        if result is None:  # Quit
            break
        if result == "skip":
            continue
        rated.append(result)

    if rated:
        _save_golden_set(golden_path, rated)
        tiers = {}
        for r in rated:
            tiers[r["tier"]] = tiers.get(r["tier"], 0) + 1
        click.echo(f"  Distribution: {tiers}")
    else:
        click.echo("  No ratings collected.")


def _run_test(golden_path: Path) -> None:
    """Score the golden set with the analyzer and compare to Paula's labels."""
    golden = _load_golden_set(golden_path)
    if not golden:
        click.echo("  No golden set found. Run calibration first.")
        return

    click.echo(f"\n  Testing scorer against {len(golden)} golden set examples...")

    from career_ops.discovery.normalize import Job
    from career_ops.analyzer import analyze_jobs

    # Build Job objects from golden set
    jobs = []
    for g in golden:
        j = Job.build(
            title=g["title"],
            company=g["company"],
            location=g.get("location", "Dubai, UAE"),
            url="",
            source=g.get("source", "indeed"),
            description=g.get("description_preview", ""),
        )
        jobs.append((j, g))

    # Score them (will use cache if available)
    results = analyze_jobs([j for j, _ in jobs])
    result_map = {j.id: a for j, a in results}

    # Compare
    matches = 0
    total = 0
    click.echo(f"\n  {'Title':<40} {'Paula':<8} {'AI':<8} {'Score':<6} {'Match'}")
    click.echo(f"  {'-'*40} {'-'*8} {'-'*8} {'-'*6} {'-'*5}")

    for job, g in jobs:
        ai = result_map.get(job.id)
        if not ai:
            continue
        total += 1
        paula_tier = g["tier"]
        ai_tier = ai.tier
        match = paula_tier == ai_tier or (
            # Allow adjacent tier as partial match
            {paula_tier, ai_tier} in [{"Hot", "Warm"}, {"Warm", "Cold"}]
        )
        if paula_tier == ai_tier:
            matches += 1
            symbol = "=="
        elif match:
            matches += 0.5
            symbol = "~="
        else:
            symbol = "!!"

        click.echo(f"  {g['title'][:40]:<40} {paula_tier:<8} {ai_tier:<8} {ai.score:<6} {symbol}")

    accuracy = (matches / total * 100) if total else 0
    click.echo(f"\n  Accuracy: {accuracy:.0f}% ({matches}/{total})")
    if accuracy >= 80:
        click.echo("  PASS — scorer is calibrated. Safe to enable daily cron.")
    else:
        click.echo("  NEEDS WORK — review the few-shot examples and adjust.")


if __name__ == "__main__":
    main()
