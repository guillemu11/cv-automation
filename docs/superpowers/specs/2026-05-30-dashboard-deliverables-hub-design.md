# Dashboard deliverables hub — design

**Date:** 2026-05-30
**Goal:** Surface every generated artifact for a job (CV, Cover Letter, deliverable
PDF, outreach pack, and the deployed Vercel landing links) in the local dashboard,
and make new artifacts attach automatically as they are created. Backfill Opella +
Henkel now.

## Context

The dashboard (`career_ops/webapp/api.py`, FastAPI + `static/index.html`) already
discovers artifacts by `rglob`-ing `output/` on every request
(`_index_generated_files`). So for **files**, auto-attach already exists — we only
add patterns. **External links** (Vercel URLs) are not files, so they need a tiny
sidecar the same walk can read.

## Decisions

- **External links:** stored in a per-job sidecar `LINKS_Paula_<Company>_<Role>.json`
  in the job folder, shape `[{"label": str, "url": str}]`. Written by a helper
  `register_link()` (called from the deploy step going forward, and once now to
  backfill). The dashboard reads it via the existing company/title matcher.
- **Deliverables:** if a `*_FULL.pdf` exists for the job, show **only** it (its Deck
  and Plan components are already merged inside, so hiding them avoids redundancy —
  the Henkel case). Otherwise show **all** `Deliverable_Paula_*` files (Opella has 4
  distinct `.docx` analyses and no FULL). Pattern includes `.pdf` **and** `.docx`.
- **Form responses:** explicitly out of scope (per user).

## Matching

Concept-named artifacts (e.g. `Deliverable_Paula_Henkel_Frizz-Forecast_FULL.pdf`,
`Henkel_Outreach_Pack.docx`) carry the **company** but not the role title, so the
existing strict `company AND title in stem` matcher misses them. Therefore:

- **CV / CL / FORM** — keep the strict `company + title` match (they are named with the role).
- **deliverable / outreach / links** — match by **company** (title only as a tiebreaker
  when several jobs share a company). Skip Office lock files (`~$*`).

## Changes

1. `_index_generated_files` (api.py):
   - add `outreach` pattern `*_Outreach_Pack.docx` (company match, skip `~$*`).
   - add `links` from the `LINKS_Paula_*.json` sidecar (company match, parse JSON).
   - deliverable: collect a **list**; prefer the `*_FULL.pdf` member, else keep all;
     include `.docx`.
   - extend the per-job result dict with `outreach`, `links` (list), `deliverables` (list).
2. New endpoint `GET /api/jobs/{job_id}/outreach-pack` → `FileResponse` of the docx.
   Deliverables already downloadable via `/output/...` static mount; expose their
   relative paths. Links are external → returned in the job JSON, rendered as `<a>`.
3. `static/index.html`: in the job card, render the outreach-pack download, the
   deliverables list, and the links list.
4. `career_ops/generators/links.py`: `register_link(job, label, url)` — create/update
   the sidecar idempotently (dedupe by url). One-off backfill for Opella a/b + Henkel c.

## Auto-attach summary

- CV/CL/deliverable/outreach docx: automatic — already discovered by the `output/` walk.
- Vercel links: `register_link()` writes the sidecar at deploy time → discovered by the
  same walk. No scheduler, no manual step.

## Verification

- `/api/jobs` returns, for Opella: CV, CL, 4 deliverable docx, outreach pack, 2 links
  (paula-pitch-a/b). For Henkel: CV, CL, FULL pdf only, outreach pack, 1 link (paula-pitch-c).
- Dashboard job cards render all of the above; links open the Vercel sites; downloads work.
