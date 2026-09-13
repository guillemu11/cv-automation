# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project context

Automated job-search pipeline for **Paula De Francisco** (Brand/Marketing Manager, Dubai). Daily flow: multi-source discovery → hard filters → Claude-based scoring → Notion CRM → drafts of personalized CVs and outreach emails. **Nothing is ever sent automatically** — every output must land as a draft for human review.

Primary design doc (single source of truth): `Plan_Sistema_Busqueda_Empleo_Dubai.md`. README.md shows the intended runbook and target architecture.

## Automation-first principle (IMPORTANT)

Always propose and implement the **most automated** solution available. Paula and Guille should never need to touch a terminal, run CLI scripts, or perform manual steps that a machine could do for them.

Concrete rules:
- **Prefer dashboard buttons over CLI scripts.** Any new user-facing action goes into the local web dashboard (`scripts/dashboard.py`), not a `python scripts/foo.py` invocation.
- **Combine steps when possible.** If feature A normally precedes feature B, the UI should offer a single "do A and B" action rather than two separate ones — even if it's slightly slower.
- **Auto-install dependencies on first use.** If a feature needs setup (e.g. `playwright install chromium`), trigger it transparently from the running app and show progress in the UI; do not ask the user to run a command.
- **Never propose terminal commands as part of the user flow.** Terminal commands are acceptable only for one-off developer setup (initial `pip install`, env var config) — and even then, prefer in-app config when feasible.
- **When presenting options, the most-automated option is the default recommendation.** "More clicks for more control" is a valid alternative but never the default.

## Current state (important)

The repo is **early scaffolding**. Only the following are implemented:

- `career_ops/config.py` — central settings loader
- `profile.yaml`, `blacklist.yaml` — candidate profile + hard-filter rules
- `requirements.txt`, `.env.example`

The following directories exist but are **empty** and must be created when implementing: `career_ops/discovery/`, `career_ops/filters/`, `career_ops/generators/`, `scripts/`, `templates/`, `.github/workflows/`. `career_ops/pipeline.py`, `analyzer.py`, `notion_sync.py`, `daily_digest.py`, `contact_finder.py`, `gmail_client.py`, `outlook_client.py` are planned in README but not yet written. Do not assume any of these exist — check before referencing them, and follow the module boundaries laid out in README.md "Estructura" and `Plan_Sistema_Busqueda_Empleo_Dubai.md` when adding new code.

## Architecture

Pipeline stages (each a module under `career_ops/`):

```
discovery/  →  filters/  →  analyzer  →  contact_finder  →  notion_sync  →  daily_digest
  jobspy        dedupe       Claude       Apollo.io           Notion API      Outlook/Gmail
  (Indeed       salary       SQLite cache
   only)        blacklist
```

**Discovery is Indeed-only and free** (see "Discovery: Indeed only" below). The
other source modules (`serpapi_source`, `firecrawl_careers`) remain in the tree
but are **off by default** — SerpAPI is out of credits and nothing else is paid.

Key architectural rules:

- **All config goes through `career_ops.config.settings`** (a cached `Settings` singleton). Modules must never read env vars or load YAML directly — import `from career_ops.config import settings`. This keeps secrets and tunables testable and centralized. See [career_ops/config.py](career_ops/config.py).
- **`profile.yaml` describes the candidate** (target titles, sectors, experience); **`blacklist.yaml` defines hard rejection rules** (keywords, seniority floors, `min_salary_aed_month`, allowed locations, currency→AED conversion). Hard filters run **before** Claude scoring to avoid spending tokens on obvious rejects.
- **Deduplication is cross-source**: each job hashed by (normalized title + company + location), persisted in `data/seen_jobs.json` plus a flag in Notion. Analyzer results are cached in `data/analysis_cache.sqlite` so re-runs don't re-pay Claude for the same JD.
- **Email channel is pluggable**: Microsoft Graph (Outlook, preferred — uses Paula's existing hotmail) or Gmail API. Config picks one via env vars. Both must produce drafts only.
- **`PIPELINE_DRY_RUN=true`** short-circuits all external writes (Notion, email drafts, file generation). Any new pipeline step must honor this flag.

## Execution model — fully automated

**Paula does NOT run scripts manually.** Everything ships via scheduled automation (cron/Task Scheduler/GitHub Actions) or is triggered from the dashboard UI. Treat the codebase as a service, not a CLI toolbox.

Operational rules for Claude:

- **Never instruct Paula to run a command.** No "run `python -m career_ops.pipeline`", no "execute `scripts/foo.py`". If something needs to happen, either (a) it already runs on a schedule, (b) it has a dashboard button/endpoint, or (c) you need to wire one of those — that's the task.
- **No "Para probar" sections with shell commands** in summaries. If a feature needs verification, describe what to click in the dashboard, not what to type in a terminal.
- **New functionality must be either scheduled or dashboard-triggered.** Don't add CLI-only features. If a script exists in `scripts/`, assume it's invoked by a scheduler or by a FastAPI endpoint — find the caller before assuming users run it directly.
- **Verifying your own changes**: you may run commands yourself (imports, syntax checks, smoke tests) to confirm code works, but never hand the command back to Paula as a "next step."

### How things actually run

| Trigger | What runs | Where it's wired |
|---|---|---|
| Daily cron | Full pipeline (discovery → filter → analyze → contacts) | Scheduler (cron / Task Scheduler / GH Actions) |
| Dashboard button | CV/CL generation, contact search, outreach generation | FastAPI endpoints in [career_ops/webapp/api.py](career_ops/webapp/api.py) |
| Server startup | Status reconcile from disk | `_startup_sync` in api.py |
| Nightly 23:00 (launchd) | Auto-commit + push to GitHub if anything changed | [scripts/auto_push.sh](scripts/auto_push.sh), `~/Library/LaunchAgents/com.cvautomation.autopush.plist`; log in `logs/auto_push.log` |

The scripts under `scripts/` (`calibrate_scorer.py`, `setup_notion_db.py`, etc.) are **one-off / maintenance** utilities run by the developer (you), not Paula. Never surface them as user actions.

### Reference: scripts and their callers

For Claude's own use when investigating — these exist but Paula does not invoke them:

- `python -m career_ops.pipeline` — invoked by the scheduler
- `scripts/setup_notion_db.py`, `scripts/calibrate_scorer.py` — dev-only one-shots
- `scripts/generate_for_job.py` — superseded by the dashboard "Generate" button
- `scripts/run_webapp.py` — server bootstrap, runs as a service

There are currently no tests, linter config, or CI workflows. When adding them, prefer `pytest` (implied by the Python stack) and keep test fixtures under `data/` small and committed.

## Domain conventions

- **Salary floor is in AED/month** (`min_salary_aed_month`, default 20000). Non-AED salaries must be normalized via `settings.currency_to_aed` before comparison. Jobs with no visible salary **pass** the hard filter and are left to the scorer.
- **Allowed locations** are UAE-only by default (`blacklist.yaml` → `allowed_locations`). Anything else is a hard reject.
- **Seniority rejects** (`Intern`, `Trainee`, `Junior`, `Entry Level`, `Graduate`) and keyword rejects (`commission only`, `MLM`, `internship`, etc.) are case-insensitive substring matches on title+description.
- **Target companies for career-page scraping** live in `career_ops/discovery/firecrawl_careers.py` → `TARGET_COMPANIES` (to be created).
- **Output files** go to `output/CV_Paula_<Company>_<Role>.docx`. Templates live in `templates/cv_paula_template.docx` and `templates/cover_letter_template.docx` (python-docx).

## Discovery: Indeed only (free)

Discovery is **Indeed-only and costs nothing**. There are two complementary paths,
both Indeed-only:

- **Conversational (Paula's primary use):** the `buscar-trabajos` skill
  (`.claude/skills/buscar-trabajos/`). Paula asks in a session ("dame las 10
  ofertas más relevantes hoy") and Claude searches Indeed via the **Indeed
  connector** (`mcp__claude_ai_Indeed__search_jobs`), hard-filters, ranks by fit
  against `profile.yaml`, and returns the top 10 with apply links. Free, no
  scraping, no paid API. Requires the Indeed connector enabled in her claude.ai
  Connectors. **This is the reliable path** — prefer it for live searches.
- **Unattended pipeline (background):** `python -m career_ops` (scheduled) runs
  `discover_all`, which honors `settings.discovery_sources` (default `["jobspy"]`)
  and `settings.jobspy_sites` (default `["indeed"]`). `jobspy` scrapes Indeed
  natively for free. LinkedIn is **off** by default (it blocks scrapers). SerpAPI
  / Firecrawl modules stay in the tree but are disabled (no credits).

Do **not** re-enable SerpAPI/Apify/Firecrawl or jobspy's LinkedIn site without an
explicit ask — Paula's search is free-and-Indeed-only by design. To change either,
set `DISCOVERY_SOURCES` / `JOBSPY_SITES` in `.env` (never hardcode in modules).

## When adding discovery sources

Each source module under `career_ops/discovery/` should expose a single `fetch() -> list[Job]` function returning a normalized shape (title, company, location, description, url, posted_at, salary_min/max/currency). Dedup + filtering happens downstream, so sources must not pre-filter beyond what the source API supports natively. Respect `settings.max_results_per_query` and `settings.hours_old`. New sources are registered in `discover_all`'s `registry` and gated by `settings.discovery_sources` — add the key there, but leave it out of the default unless it's free.
