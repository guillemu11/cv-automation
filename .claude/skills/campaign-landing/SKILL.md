---
name: campaign-landing
description: Use when Paula needs to generate a jaw-dropping animated landing page presenting a fictional marketing campaign for a target company from her Dubai job search. Produces a deployable HTML/CSS/JS site with brand-accurate colors/typography extracted from the company's real website, scroll-driven animations, and a shareable Vercel link to include in outreach emails. Trigger on "/campaign-landing <company>" or when user says "haz una landing para <empresa>".
---

# Campaign Landing

Generates a fictional marketing-campaign landing page for a target company as a differentiating deliverable for Paula's "hot" job applications (>80 score). Output is a static HTML/CSS/JS folder deployable to Vercel in one shot.

**Stack**: HTML + CSS + vanilla JS. No build step. Deploy target: Vercel CLI (fallback Netlify).

## Two modes

The skill supports two distinct landing types. Pick one based on the role Paula is applying to:

- **`mode: pitch`** (default) — internal agency-pitch landing. Structured like a strategy doc: insight → manifesto → executions → KPIs → credits. Target audience: CMO / Marketing Director. Signals Paula's strategic thinking. Use for **brand / strategy / planning** roles.
- **`mode: consumer`** — live consumer ad-landing. Structured as a conversion funnel: hook → value prop → how-it-works → social proof → lead capture form → legal footer. Target audience: the actual end consumer after clicking a Meta/TikTok ad. Signals Paula's performance / growth / digital marketing chops. Use for **performance / growth / digital** roles, or as a bonus deliverable alongside a pitch landing to show full-stack versatility.

Both modes share phases 1-2 (brand extraction + campaign ideation) and phase 6 (deploy). Phases 3-5 (structure + assets + code) branch by mode. See `references/consumer-mode.md` for the consumer-specific structure.

## Hard rules

- **Never stock photos.** Use brand colors + typography as the visual system. Generate real brand imagery in-project via `career_ops.generators.images` (Google Gemini image API — `gemini-3-pro-image`, aka "Nano Banana"). Higgsfield is deprecated. NOTE: image models need a **billing-enabled** Google project (free tier = 0 image quota); text scoring still works free.
- **Never generic shadcn/gradient slop.** The taste layer is Anthropic's `/frontend-design` skill plus the anti-slop rules in `references/animation-patterns.md`.
- **Respect `PIPELINE_DRY_RUN`.** If set, phase 6 prints the deploy command but does NOT run it.
- **Always private repo** when pushing to GitHub (real company names on landings = sensitive).
- **Mobile-first responsive** is non-negotiable. Test at 375 / 768 / 1440.
- **Credits footer** must read "Proposed by Paula De Francisco — application for \<role\>" in a subtle style.

## Inputs

- `company_name` (required)
- `company_url` (required — will WebSearch if missing)
- `job_id` (optional — if present, read JD from `data/scored_jobs.json` or `data/analysis_cache.sqlite` to align the campaign with the role)
- `brand_override` (optional — if the target is a sub-brand of a parent company, e.g. Lipton under PepsiCo, use this to focus extraction on the sub-brand)
- `campaign_brief` (optional — if absent, skill proposes 3 angles and asks the user to pick one)

## The 6-phase workflow

Read `references/workflow.md` for full detail. High-level:

1. **Brand extraction** — Firecrawl or WebFetch on `company_url`. Outputs `output/landing_<slug>/brand.json` (palette, fonts, logo refs, tone). See `references/brand-extraction.md`.
2. **Campaign ideation** — propose 3 fictional campaign angles tied to the JD. User picks one.
3. **Structure planning** — decide sections (hero, insight, manifesto, executions, KPIs, credits).
4. **Asset generation** — generate real stills in-project via `career_ops.generators.images.generate_batch` (Google Gemini image API); otherwise palette-based placeholders (never stock). See `references/animation-patterns.md`.
5. **Code generation** — fill `templates/base.html` + `templates/styles.css` + `templates/scroll.js` with brand tokens and campaign copy. Write to `output/landing_<slug>/`.
6. **Deploy (optional)** — `vercel deploy` from the output folder. See `references/deploy.md`. Honors `PIPELINE_DRY_RUN`.

## Output location

All generated files land under `output/landing_<slug>/` where `<slug>` is `company_name.lower().replace(" ", "-")` plus an optional campaign-name suffix. Never write outside `output/`.

## When to stop and ask

- After phase 2, always show the 3 campaign angles and wait for user pick.
- Before phase 6, confirm the user wants to deploy (even a preview URL is public once Vercel generates it).
- If brand extraction fails (Firecrawl quota, site 403s), fall back to WebFetch on the homepage and proceed with whatever you recovered rather than blocking.

## Compounding

Every time the skill is used and the output has a problem, update `references/` with the fix. The skill gets sharper with each use. Source concepts live in `wiki/concepts/` — keep references in sync when the wiki evolves.
