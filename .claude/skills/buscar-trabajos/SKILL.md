---
name: buscar-trabajos
description: Use when Paula asks for relevant job openings in her Dubai job search — e.g. "dame las 10 ofertas más relevantes para mí hoy", "busca trabajos para mí", "scame ofertas en Indeed", "qué hay nuevo hoy", "find me jobs", "/buscar-trabajos". Searches Indeed for FREE via the Indeed connector across her target titles in the UAE, hard-filters obvious rejects, ranks by fit against her profile, and returns the best 10 with clickable apply links. Indeed is the ONLY source (no paid APIs, no SerpAPI, no LinkedIn scraping). Trigger this whenever Paula wants to discover jobs interactively, even if she doesn't say "Indeed" or "skill".
---

# Buscar Trabajos (Indeed, gratis)

Paula's daily interactive job search. She opens a session, asks for the best openings, and gets a ranked top-10 with apply links — searched **for free** against Indeed's official API via the Indeed connector. No paid sources, no fragile scraping, no LinkedIn.

This is the **conversational** half of the discovery system. The other half is an unattended daily pipeline (`jobspy` restricted to Indeed → dashboard); this skill is what Paula uses live when she wants results *now*.

## Hard rules

- **Indeed only, always free.** Use the `mcp__claude_ai_Indeed__search_jobs` connector. Never reach for SerpAPI, Apify, Firecrawl, or any paid API — Paula has no credits and this must cost nothing.
- **Embed the apply link on every job title.** The connector returns a `View Job URL` per result; make each job title a clickable markdown link to it. Keep the URL intact (don't strip query params) — it's how she applies.
- **Never apply or send anything.** This skill *discovers and ranks*. Generating CVs/cover letters/outreach is a separate dashboard action. Surface the jobs; let Paula decide.
- **Always exactly 10** unless Paula asks for a different number. If fewer than 10 survive filtering, return what you have and say so plainly — don't pad with weak matches.

## Inputs (the candidate)

Read these two files at the start of every run — they are the single source of truth for what fits and what to reject. Don't hardcode the criteria into this skill; they change as Paula's search evolves.

- `profile.yaml` → `target_titles`, `target_sectors`, `target_locations`, `ats_keywords_high_value`, `differentiators`. These drive the **ranking**.
- `blacklist.yaml` → `seniority_reject`, `keywords_reject`, `allowed_locations`, `min_salary_aed_month`, `title_reject_patterns`, `companies`. These drive the **hard filter**.

## Workflow

### 1. Search Indeed (a few targeted queries, not all titles)

Running one query per target title is wasteful and returns heavy overlap. Instead fire **4–6 broad queries** that cover her title clusters, then dedupe. Good default set (adjust to `target_titles`):

| Query (`search`) | Covers |
|---|---|
| `Brand Manager` | Brand / Senior Brand / Brand & Marketing |
| `Marketing Manager` | Marketing / Senior Marketing / Digital Marketing |
| `E-Commerce Manager` | E-Commerce / Marketing & E-Commerce |
| `Key Account Manager` | Key Account / Senior KAM / Commercial |
| `Trade Marketing Manager` | Trade / Shopper / Category |

For each query call the connector with:
- `location`: `"Dubai"` (Paula is Dubai-based). Optionally also run `"Abu Dhabi"` if she asks to widen the net.
- `country_code`: `"AE"`
- `job_type`: `"fulltime"`

Run the queries in parallel (multiple tool calls in one turn).

### 2. Dedupe

The same role surfaces under multiple queries. Collapse duplicates by normalized **(title + company)**. Keep the first occurrence and its apply URL.

### 3. Hard-filter (drop the obvious rejects — same rules as the pipeline)

Reject a job if **any** of these match (case-insensitive substring on title, and on description when available):
- Title/desc contains a `seniority_reject` term (`Intern`, `Trainee`, `Junior`, `Entry Level`, `Graduate`, …).
- Title/desc contains a `keywords_reject` term (`commission only`, `MLM`, `internship`, …).
- Title matches a `title_reject_patterns` entry.
- Company is in `blacklist.yaml → companies`.
- Location is clearly outside `allowed_locations` (UAE-only by default). Indeed results for `AE` are usually fine; drop anything explicitly elsewhere.

Salary almost never appears in Indeed search results — **do not** reject for a missing salary. Let unscored salaries pass (same convention as the pipeline's hard filter).

### 4. Rank by fit

Score each surviving job 0–100 on how well it matches Paula. Use judgment, weighting roughly:
- **Title match** to `target_titles` (exact title cluster > adjacent). Highest weight.
- **Sector match** to `target_sectors` (FMCG, Beauty & Fragrances, Quick-commerce, E-commerce, Luxury/Fashion, Retail…). Beauty/fragrance/FMCG/quick-commerce are her sweet spot — see `differentiators`.
- **High-value keywords** present in the title/company (`ats_keywords_high_value`: NPD, influencer marketing, quick-commerce, Noon, Talabat, key account, GMV, trade marketing…).
- **Recency** — newer postings rank higher; flag anything older than ~30 days.
- **Seniority fit** — Manager/Senior Manager ideal; "Head/Director" is a stretch-up (keep but note), "Executive/Coordinator/Assistant" is a step-down (rank low or drop).

You may call `mcp__claude_ai_Indeed__get_job_details` on the **top ~12 candidates only** to read the full JD and sharpen the ranking and the "why it fits" line. Don't fetch details for everything — it's slower and the title+company already separates strong from weak.

### 5. Present the top 10

Use this exact structure:

```
## Top 10 ofertas para Paula — <fecha> (Indeed, gratis)

Busqué N consultas en Indeed, encontré M ofertas únicas, descarté K por filtros. Aquí el top 10 por encaje:
```

Then a table, **best fit first**:

| # | Puesto (link para aplicar) | Empresa | Sector | Publicada | Encaje | Por qué |
|---|---|---|---|---|---|---|

- **Puesto** = markdown link `[Title](apply_url)` — clickable, opens Indeed to apply.
- **Encaje** = the 0–100 score with a 🟢 (≥75) / 🟡 (50–74) / 🔴 (<50) dot.
- **Por qué** = one short line tying it to her profile (e.g. "Beauty + brand global, su sector exacto").

Close with a one-line nudge: which 1–2 are the strongest and whether she wants deliverables (CV/landing/outreach) generated for any — but don't generate them unless she says yes.

## After presenting (optional)

If Paula says she wants any of these jobs tracked, offer to add them to the dashboard (`data/scored_jobs.json`) so they show up alongside pipeline finds and she can generate deliverables from there. Map your fit score → `ai_score`, and tier by 🟢/🟡/🔴 → `Hot`/`Warm`/`Cold`. Set `source: "indeed"` and `freshness: "fresh"`. Only do this on request — don't auto-pollute the board.

## Setup note (one-time, for the developer)

This skill depends on the **Indeed connector** being enabled in the claude.ai account Paula uses in Claude Code. If `mcp__claude_ai_Indeed__search_jobs` isn't available in a session, the connector needs to be turned on in her Connectors settings — surface that clearly rather than silently falling back to a paid source (there is no paid fallback by design).
