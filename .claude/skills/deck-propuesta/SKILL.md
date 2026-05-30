---
name: deck-propuesta
description: Use when Paula wants a high-impact application deliverable for a target role in her Dubai job search — a concept-led 16:9 visual pitch deck plus a rigorous trade & shopper marketing plan, in the company's own brand system. Trigger on "/deck-propuesta <empresa>", "hazme un deck para <empresa>", "monta una propuesta tipo Henkel / Frizz Forecast", "quiero un deck de candidatura", "plan de trade + deck para esta oferta", "una propuesta como la de mi amiga para Absolut", or whenever she wants to turn a job opening into a deck + plan she can attach. Worked example: Henkel "Frizz Forecast" (Trade & Shopper Mgr, GCC). Use this even if she doesn't say the word "deck" but clearly wants a designed proposal/pitch for an application.
---

# Deck-propuesta — concept-led pitch deck + trade plan

Turns one target role in Paula's job search into a **send-ready application package**: a beautiful 16:9 visual pitch deck that opens with ONE ownable creative idea, backed by a rigorous trade & shopper marketing plan attached as an appendix. The reference build is the **Henkel "Frizz Forecast"** deliverable — read [scripts/_henkel_frizz_forecast_deck.py](../../../scripts/_henkel_frizz_forecast_deck.py) and [scripts/_henkel_trade_plan.py](../../../scripts/_henkel_trade_plan.py) as the worked example whenever something here is unclear.

This is the **"wow" deliverable** half of an application. The CV/CL pairs and the plain trade plan are produced elsewhere; this skill is what makes a recruiter stop scrolling.

## What it produces (format "C")

A single, layered package, all in the **company's real brand system**:

1. **Deck PDF** — ~11 slides, 16:9, HTML→PDF. Opens with a creative key visual, then proves the thinking.
2. **Trade & shopper plan** — the detailed 2-page plan, appended after the deck (the "detail").
3. **FULL PDF** = deck + plan merged (this is the headline attachment).

Output goes to the existing job folder: `output/<date>/<Company - Role>/Deliverable_Paula_<Company>_<Concept>_Deck.pdf` and `..._FULL.pdf`. **Nothing is ever sent** — these are drafts for Paula to review, consistent with the repo's core rule.

## The pipeline

Work top to bottom. Each step has a worked example in the Henkel scripts and detailed mechanics in the reference files.

### 1 · Brand system + assets (reuse first)

The hardest part — a coherent brand system — is usually already solved. Look for a campaign landing for this company first: `output/<date>/<Company - Role>/landing_*/`.

- If it exists, **reuse it**: read its `brand.json` (palette, display+body fonts, tagline, tone) and reuse its `assets/*.jpg` (typically `hero`, `instore`, `pharmacy`, `qcommerce`, `marketplace`, `retailmedia`, `creator` — they map almost 1:1 to trade channels). This is why `deck-propuesta` pairs naturally with the `campaign-landing` skill.
- If it doesn't exist, derive a `brand.json` from the company's site (palette, two Google Fonts — a bold display + a clean body, a tagline) and generate the channel images with `higgsfield-generate` (GPT Image 2). Prefer reuse; only generate what's missing.

Paula's photo for the "Why Paula" slide lives at `templates/paula_photo.jpg`.

### 2 · Trade & shopper plan (the appendix)

If a plan PDF already exists for this role (e.g. `Deliverable_Paula_<Company>_..._Plan_*.pdf`), reuse it as the appendix as-is. Otherwise author it — six sections, modelled on `_henkel_trade_plan.py`: shopper & category insight → Perfect Store by channel → key account / JBP plan → 90-day activation calendar → shopper mechanics & NPD → KPIs/ROI & cadence. Keep it specific to the market (for GCC: heat/humidity year-round, premium-expat + value-mass polarity, Modern Trade + pharmacy + e-tail + quick-commerce, Ramadan/Eid/DSF peaks).

### 3 · The creative concept (the differentiator) — present 3, let her pick

This is what separates Paula from a generic deck. Generate **three distinct trade-&-shopper concepts** and let her choose the one to open with. Follow [references/concept-generation.md](references/concept-generation.md) — it runs a fan-out + judge-panel `Workflow` (6 strategic lenses → adversarial scoring → 3 mutually-distinct winners with different hero KPIs).

**The one hard constraint:** the concept must be unmistakably **Trade & Shopper** — it lives at the shelf / Perfect Store / digital shelf / quick-commerce / retail media, runs on real shopper mechanics (GWP, sampling, displays, bundles, creator codes), and moves measurable trade KPIs (sell-out uplift, distribution, Perfect Store compliance, promo ROI/ROAS, premium mix). It must **NOT** drift into a brand-ATL film, a celebrity endorsement, or a fashion co-branding stunt. A Trade & Shopper hiring manager has to read it and think *"she knows how to win the shelf,"* not *"nice ad."*

Present the 3 with a mockup of each key visual (use the brainstorming visual companion if helpful), one-line tagline, the big idea, channel activation, and the hero KPI. Per Paula's standing preference, always show **exactly three** distinct options — never one or two. Recommend one, but let her decide; she may also ask to graft pieces of one onto another.

### 4 · Build the deck (~11 slides)

Build a one-off script `scripts/_<company>_<concept>_deck.py` modelled on `_henkel_frizz_forecast_deck.py`. The slide spine (adapt copy to the chosen concept):

1. **Cover** — concept name huge, tagline, applicant lockup, `hero` image.
2. **Agenda** — the six section numbers.
3. **Shopper & category insight** — the market truth, with a lifestyle image.
4. **The big idea ★** — the chosen concept's key visual (build it in HTML/CSS).
5. **How it works** — the mechanic, split into an in-store (KAM-sellable) layer and a digital/live layer.
6. **Across the shelf** — 5 channel cards, each using a channel image.
7. **Perfect Store by channel** — the table, with the concept's new audit line folded in.
8. **90-day activation calendar** — the calendar table, reframed around the concept.
9. **KPIs · ROI · cadence** — the table; mark the concept's hero KPI in the accent colour.
10. **Why Paula** — `paula_photo.jpg`, her real credentials (pull figures she actually has), one authentic personal line.
11. **Contact** — big "CONTACT", email/phone/LinkedIn from `settings.profile["personal"]`.

All design/build mechanics — the CSS token system, slide-builder pattern, `_table` helper — are in [references/deck-build.md](references/deck-build.md).

### 5 · Render + merge

Render HTML→PDF with headless Chromium (`page.pdf()`, one `.slide` = one 1280×720 page), then merge the trade-plan PDF after it with `pypdf`. Full reusable code is in [references/deck-build.md](references/deck-build.md). Verify: deck = number of slides; FULL = slides + appendix pages.

### 6 · Visual QA (do not skip)

Headless rendering hides layout bugs that page-count checks miss. Screenshot every slide and look at it (the controller has vision — review the PNGs directly). The snippet is in [references/deck-build.md](references/deck-build.md). The most common failures, in order: (a) absolutely-positioned key-visual elements overlapping body text on the big-idea slide; (b) a slide taller than 720px splitting into an extra page; (c) caption overflow on channel cards. Fix in the builder/CSS and re-render until clean.

## Hard rules

- **Drafts only.** Never send, email, or publish. Output PDFs land in the job folder for Paula to review.
- **Trade & Shopper, not Brand.** The concept must win the shelf and be measurable. Re-read step 3 if tempted by an ATL idea.
- **Reuse, don't regenerate.** Reuse an existing landing's `brand.json` + images and any existing trade-plan PDF before building new ones. No needless image generation.
- **Three options at the concept choice** (and any design/copy fork) — never one or two. This is a standing preference.
- **Config from `settings`.** Contact and profile come from `career_ops.config.settings`, never hardcoded.
- **Print-first, static deck.** No scroll-reveal / IntersectionObserver animations (they render as `opacity:0` in headless print); images `loading="eager"`; wait for `document.fonts.ready` before printing. Details in [references/deck-build.md](references/deck-build.md).
- **Build scripts, not user steps.** These scripts are run by you (the dev), not by Paula — never hand her a terminal command. The artifact she touches is the finished PDF in the job folder.

## Reference files

- [references/concept-generation.md](references/concept-generation.md) — the fan-out + judge-panel `Workflow` that produces 3 distinct, defensible trade-shopper concepts.
- [references/deck-build.md](references/deck-build.md) — the reusable build core: brand-token CSS system, slide-builder pattern, the `_table` helper, the Playwright multi-page `render_pdf`, the `pypdf` `merge_pdfs`, and the QA-screenshot snippet.
