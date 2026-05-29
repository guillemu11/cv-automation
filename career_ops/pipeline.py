"""Pipeline orchestrator — chains discovery → dedupe → filter → score → sync.

Entry point: ``python -m career_ops`` (or ``python -m career_ops.pipeline``).
Honors ``PIPELINE_DRY_RUN=true`` to skip external writes (Notion, email).
"""
from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass, field
from datetime import date

from .analyzer import JobAnalysis, analyze_jobs
from .config import settings
from .contact_finder import Contact, find_contacts
from .discovery import discover_all
from .discovery.normalize import Job
from .filters.dedupe import filter_new
from .filters.hard_filters import apply_hard_filters
from .notion_sync import sync_contacts, sync_jobs

logger = logging.getLogger(__name__)


# -------------------------------------------------------------------
# Pipeline result
# -------------------------------------------------------------------

@dataclass
class PipelineResult:
    """Stats from a single pipeline run, passed to the digest builder."""
    discovered: int = 0
    dedupe_new: int = 0
    dedupe_skipped: int = 0
    filter_passed: int = 0
    filter_rejected: int = 0
    analyzed: int = 0
    hot: int = 0
    warm: int = 0
    cold: int = 0
    contacts_found: int = 0
    notion_inserted: int = 0
    notion_skipped: int = 0
    notion_errors: int = 0
    scored_jobs: list[tuple[Job, JobAnalysis]] = field(default_factory=list)
    job_contacts: dict = field(default_factory=dict)  # job_id -> list[Contact]
    errors: list[str] = field(default_factory=list)
    duration_seconds: float = 0.0


# -------------------------------------------------------------------
# Internal helpers
# -------------------------------------------------------------------

def _setup_logging() -> None:
    """Configure root logger: console (INFO) + file (DEBUG)."""
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(logging.Formatter("%(asctime)s  %(levelname)-5s  %(name)s  %(message)s", datefmt="%H:%M:%S"))
    root.addHandler(ch)

    # File handler
    log_path = settings.logs_dir / f"pipeline_{date.today().isoformat()}.log"
    fh = logging.FileHandler(str(log_path), encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter("%(asctime)s  %(levelname)-8s  %(name)s  %(message)s"))
    root.addHandler(fh)


def _save_scored_jobs(scored: list[tuple[Job, JobAnalysis]]) -> None:
    """Persist scored jobs to data/scored_jobs.json for the dashboard."""
    from datetime import datetime, timezone
    now_iso = datetime.now(timezone.utc).isoformat()
    records = []
    for job, analysis in scored:
        rec = job.to_dict()
        # Use ai_score/ai_tier to match the format already in scored_jobs.json
        a = analysis.to_dict()
        rec["ai_score"] = a.pop("score", 0)
        rec["ai_tier"] = a.pop("tier", "Warm")
        rec.update(a)
        # Mark as fresh from this run so dashboard can distinguish vs older runs
        rec["freshness"] = "fresh"
        rec["discovered_at"] = now_iso
        records.append(rec)

    path = settings.data_dir / "scored_jobs.json"
    # Merge with existing scored jobs (don't overwrite prior runs)
    existing: list[dict] = []
    if path.exists():
        with path.open("r", encoding="utf-8") as f:
            try:
                existing = json.load(f)
            except json.JSONDecodeError:
                existing = []

    existing_ids = {r["id"] for r in existing if "id" in r}
    for rec in records:
        if rec["id"] not in existing_ids:
            existing.append(rec)

    with path.open("w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

    logger.info("saved %d scored jobs to %s (total: %d)", len(records), path.name, len(existing))


# -------------------------------------------------------------------
# Main pipeline
# -------------------------------------------------------------------

def run() -> PipelineResult:
    """Execute the full pipeline. Returns stats for digest."""
    t0 = time.time()
    result = PipelineResult()
    prefix = "[DRY RUN] " if settings.dry_run else ""

    # --- Stage 1: Discovery ---
    logger.info("%s=== Stage 1: Discovery ===", prefix)
    try:
        jobs = discover_all(
            queries=settings.target_titles,
            locations=settings.target_locations,
            limit=settings.max_results_per_query,
            hours_old=settings.hours_old,
        )
        result.discovered = len(jobs)
        logger.info("%sdiscovered %d jobs from all sources", prefix, len(jobs))
    except Exception as exc:
        result.errors.append(f"Discovery failed: {exc}")
        logger.exception("discovery failed — aborting pipeline")
        result.duration_seconds = time.time() - t0
        return result

    if not jobs:
        logger.info("%sno jobs discovered — nothing to do", prefix)
        result.duration_seconds = time.time() - t0
        return result

    # --- Stage 2: Cross-run dedup ---
    logger.info("%s=== Stage 2: Deduplication ===", prefix)
    try:
        new_jobs, skipped = filter_new(jobs)
        result.dedupe_new = len(new_jobs)
        result.dedupe_skipped = skipped
        logger.info("%s%d new, %d already seen", prefix, len(new_jobs), skipped)
    except Exception as exc:
        result.errors.append(f"Dedupe failed: {exc}")
        logger.exception("dedupe failed — treating all jobs as new")
        new_jobs = jobs
        result.dedupe_new = len(jobs)

    if not new_jobs:
        logger.info("%sno new jobs after dedup — nothing to analyze", prefix)
        result.duration_seconds = time.time() - t0
        return result

    # --- Stage 3: Hard filters ---
    logger.info("%s=== Stage 3: Hard Filters ===", prefix)
    try:
        filter_result = apply_hard_filters(new_jobs)
        result.filter_passed = filter_result.passed_count
        result.filter_rejected = filter_result.rejected_count
        logger.info("%s%d passed, %d rejected", prefix, filter_result.passed_count, filter_result.rejected_count)
    except Exception as exc:
        result.errors.append(f"Filters failed: {exc}")
        logger.exception("filters failed — skipping all jobs for safety")
        result.duration_seconds = time.time() - t0
        return result

    if not filter_result.passed:
        logger.info("%sno jobs passed hard filters", prefix)
        result.duration_seconds = time.time() - t0
        return result

    # --- Stage 4: Claude scoring ---
    logger.info("%s=== Stage 4: Analysis (Claude) ===", prefix)
    try:
        scored = analyze_jobs(filter_result.passed)
        result.analyzed = len(scored)
        result.scored_jobs = scored
        result.hot = sum(1 for _, a in scored if a.tier == "Hot")
        result.warm = sum(1 for _, a in scored if a.tier == "Warm")
        result.cold = sum(1 for _, a in scored if a.tier == "Cold")
        logger.info(
            "%sanalyzed %d jobs: %d Hot, %d Warm, %d Cold",
            prefix, len(scored), result.hot, result.warm, result.cold,
        )
    except Exception as exc:
        result.errors.append(f"Analysis failed: {exc}")
        logger.exception("analysis failed")
        result.duration_seconds = time.time() - t0
        return result

    # --- Stage 5: Save scored jobs locally ---
    if settings.dry_run:
        logger.info("[DRY RUN] Skipping save to scored_jobs.json")
    else:
        _save_scored_jobs(scored)

    # --- Stage 6: Contact finding (Warm + Hot, score ≥ 60) ---
    warm_and_hot = [(j, a) for j, a in scored if a.score >= 60]
    if warm_and_hot:
        logger.info("%s=== Stage 6: Contact Finding (Apollo) ===", prefix)
        all_contacts: list[Contact] = []
        for job, analysis in warm_and_hot:
            try:
                contacts = find_contacts(job.company, job.title, job.description or "")
                result.job_contacts[job.id] = contacts
                all_contacts.extend(contacts)
                result.contacts_found += len(contacts)
            except Exception as exc:  # noqa: BLE001
                logger.error("contact finder failed for %s: %s", job.company, exc)
                result.errors.append(f"Contact finder failed for {job.company}: {exc}")

        # Sync contacts to Notion (disabled by default — dashboard is source of truth)
        if not settings.dry_run and settings.notion_enabled and all_contacts:
            try:
                sync_contacts(all_contacts)
            except Exception as exc:
                logger.error("contacts Notion sync failed: %s", exc)
                result.errors.append(f"Contacts sync failed: {exc}")

        logger.info("%sfound %d contacts across %d jobs", prefix, result.contacts_found, len(warm_and_hot))

    # --- Stage 7: Notion sync (jobs) ---
    if settings.dry_run:
        logger.info("[DRY RUN] Skipping Notion sync")
    elif not settings.notion_enabled:
        logger.info("Notion sync disabled (NOTION_ENABLED=false) — dashboard is source of truth")
    else:
        logger.info("=== Stage 7: Notion Sync (Jobs) ===")
        try:
            notion_stats = sync_jobs(scored)
            result.notion_inserted = notion_stats["inserted"]
            result.notion_skipped = notion_stats["skipped"]
            result.notion_errors = notion_stats["errors"]
        except Exception as exc:
            result.errors.append(f"Notion sync failed: {exc}")
            logger.exception("notion sync failed")

    result.duration_seconds = time.time() - t0
    return result


# -------------------------------------------------------------------
# CLI entry point
# -------------------------------------------------------------------

def _print_summary(result: PipelineResult) -> None:
    """Print a formatted summary table to the console."""
    try:
        from rich.console import Console
        from rich.table import Table

        console = Console()
        prefix = "[DRY RUN] " if settings.dry_run else ""

        table = Table(title=f"{prefix}Pipeline Summary", show_lines=True)
        table.add_column("Stage", style="bold")
        table.add_column("Result", justify="right")

        table.add_row("Discovered", str(result.discovered))
        table.add_row("New (after dedup)", str(result.dedupe_new))
        table.add_row("Passed filters", str(result.filter_passed))
        table.add_row("Analyzed", str(result.analyzed))
        table.add_row("[red]Hot[/red]", str(result.hot))
        table.add_row("[yellow]Warm[/yellow]", str(result.warm))
        table.add_row("[blue]Cold[/blue]", str(result.cold))
        if result.contacts_found:
            table.add_row("Contacts found", str(result.contacts_found))
        if not settings.dry_run:
            table.add_row("Notion inserted", str(result.notion_inserted))
        table.add_row("Duration", f"{result.duration_seconds:.1f}s")

        if result.errors:
            table.add_row("[red]Errors[/red]", str(len(result.errors)))

        console.print(table)

        if result.errors:
            console.print("\n[red bold]Errors:[/red bold]")
            for err in result.errors:
                console.print(f"  - {err}")

    except ImportError:
        # Fallback if rich is not installed
        print(f"\n{'[DRY RUN] ' if settings.dry_run else ''}Pipeline Summary")
        print(f"  Discovered:      {result.discovered}")
        print(f"  New (dedup):     {result.dedupe_new}")
        print(f"  Passed filters:  {result.filter_passed}")
        print(f"  Analyzed:        {result.analyzed}")
        print(f"  Hot/Warm/Cold:   {result.hot}/{result.warm}/{result.cold}")
        if result.contacts_found:
            print(f"  Contacts found:  {result.contacts_found}")
        print(f"  Duration:        {result.duration_seconds:.1f}s")
        if result.errors:
            print(f"  Errors:          {len(result.errors)}")
            for err in result.errors:
                print(f"    - {err}")


def main() -> None:
    """CLI entry point for ``python -m career_ops``."""
    _setup_logging()

    if settings.dry_run:
        logger.info("[DRY RUN] Pipeline starting — external writes disabled")
    else:
        logger.info("Pipeline starting")

    result = run()
    _print_summary(result)

    # Send digest (only on real runs with results)
    if not settings.dry_run and result.scored_jobs:
        try:
            from .daily_digest import send_digest
            send_digest(result)
        except ImportError:
            logger.info("daily_digest module not available — skipping digest")
        except Exception as exc:
            logger.exception("digest failed: %s", exc)

    logger.info("Pipeline finished in %.1fs", result.duration_seconds)
