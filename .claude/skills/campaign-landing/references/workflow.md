# Workflow — campaign-landing skill

Detailed 6-phase workflow. Read this only when actually running the skill.

## Phase 0 — Resolve inputs

1. Parse `company_name`, `company_url`, optional `job_id`, optional `brand_override`, optional `campaign_brief`.
2. If `job_id` is provided: load the JD from `data/scored_jobs.json` (first) and `data/analysis_cache.sqlite` (fallback). Extract `title`, `description`, `ai_score`, `ats_keywords`, `skills_match`. These feed phase 2.
3. If `company_url` is missing: use WebSearch for `"<company_name> official site"` and take the first canonical result.
4. Compute `slug = (brand_override or company_name).lower().replace(" ", "-").replace("&", "and")`.
5. Create `output/landing_<slug>/` if missing.

## Phase 1 — Brand extraction

Full procedure in `brand-extraction.md`. Output: `output/landing_<slug>/brand.json` with this shape:

```json
{
  "name": "Lipton",
  "tagline_real": "Be More Tea",
  "palette": {
    "primary": "#FFD500",
    "secondary": "#E30613",
    "accent": "#1A1A1A",
    "bg": "#FFFFFF",
    "text": "#111111"
  },
  "typography": {
    "display": "Inter",
    "body": "Inter",
    "fallback": "system-ui, sans-serif"
  },
  "logo_hint": "yellow L with red accent, vertical lockup",
  "tone": ["optimistic", "refreshing", "accessible", "playful"],
  "source_url": "https://www.lipton.com"
}
```

If Firecrawl is unavailable, WebFetch the homepage and infer the palette from the most visually dominant colors described in the response. Accept "best guess" — phase 5 uses these as CSS custom properties and they can be edited later.

## Phase 2 — Campaign ideation

Using the JD (if any) + brand.json, produce **exactly 3** distinct campaign angles. Each angle follows this shape:

```text
Angle N: <2-word campaign name>
  Tagline: <one line, ≤8 words>
  Insight: <one sentence consumer/market insight>
  Hero idea: <visual direction for the scroll-stopper>
  KPI: <primary metric the fictional campaign would optimize for>
  Why this role: <how the angle showcases a skill from skills_match[]>
```

**Present the 3 angles in a single message and stop.** Wait for the user to pick one (by number or name) before proceeding. Do not start coding anything in phase 3 until the user has chosen.

## Phase 3 — Structure planning

Once an angle is picked, decide the sections. Default structure for a PepsiCo/FMCG campaign:

1. **Hero** — scroll-driven animation. Reveal tagline.
2. **The Insight** — oversized number or stat that justifies the campaign.
3. **Manifesto** — 3-5 short paragraphs, display typography.
4. **Campaign Executions** — grid of 4-6 touchpoint mockups (OOH / social / in-store / digital / AR / influencer).
5. **KPIs & Measurement** — how the fictional campaign would be measured.
6. **Credits** — subtle footer: "Proposed by Paula De Francisco — application for \<role_title\>".

Adjust the section list based on the angle. Not every campaign needs all 6.

## Phase 4 — Asset generation

Two paths:

**Path A — User will generate real assets later.** Produce a `assets/PROMPTS.md` in the output folder listing:

- For each image needed: a Nano Banana 2 prompt following `animation-patterns.md` rules (16×9, 2K, 4 iterations, clean background, reference-image chain for consistency).
- For any video needed: a Kling / Seedance prompt with keyframe strategy.

**Path B — Generate NOW using palette-based placeholders.** Write simple colored SVG placeholders into `assets/` that use the brand palette and brand typography for text. Never use stock photos. Never use emoji. Output is usable immediately; real assets can replace placeholders later by file-name convention.

Default: **Path B** so the landing is viewable end-to-end on first run, plus a `PROMPTS.md` for later.

## Phase 5 — Code generation

1. Copy `templates/base.html` → `output/landing_<slug>/index.html`.
2. Copy `templates/styles.css` → same folder, inject CSS custom properties from `brand.json`:
   - `--brand-primary`, `--brand-secondary`, `--brand-accent`, `--brand-bg`, `--brand-text`
   - `--font-display`, `--font-body`
3. Copy `templates/scroll.js` → same folder. It's ready to consume `data-scroll` attributes in the HTML.
4. Fill copy slots in `index.html` with the chosen campaign angle text (tagline, insight, manifesto, exec grid, KPIs, credits).
5. Ensure `<meta>` tags: OG title, OG description, OG image, Twitter card, viewport, theme-color = `--brand-primary`.
6. **Serve locally for verification**: run `python -m http.server 8000 --directory output/landing_<slug>/` in a background Bash and tell the user to open `http://localhost:8000`. Do NOT auto-open a browser.
7. Test at widths 375, 768, 1440 mentally (flag obvious issues like hero overflow, nav collapse).

## Phase 6 — Deploy (optional)

See `deploy.md`. Always ask the user before executing. Respect `PIPELINE_DRY_RUN=true`.

## Stop conditions

Stop and ask the user when:

- Brand extraction returns nothing usable (both Firecrawl and WebFetch failed).
- The JD can't be found and no `campaign_brief` was given — without either, angles are generic.
- After phase 2, always wait for angle selection.
- Before phase 6, always confirm deploy.