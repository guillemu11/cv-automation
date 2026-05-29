# Frizz Forecast — Schwarzkopf GCC pitch deck (Paula → Henkel)

**Date:** 2026-05-29
**Owner:** Guille / Paula
**Status:** Approved storyboard → ready for implementation plan

## Goal

Upgrade Paula's Henkel application deliverable from a dense 2-page trade document into a
visually striking, agency-grade **pitch deck** — inspired by the craft of a friend's Absolut
Brand Manager deck (Helena de Alba), but adapted to a **Trade & Shopper Marketing** role.

The deck opens with a single, ownable creative idea (**Frizz Forecast**) and backs it with
Paula's rigorous trade plan, so a hiring manager reads it as: *"she can turn a real shopper
truth into a mechanic the field can sell and audit, and prove it with ROI."*

## Decisions locked (from brainstorming)

| Decision | Choice | Why |
|---|---|---|
| Direction | **B — Hybrid campaign + trade** | Borrow Helena's visual craft + one creative key visual, but keep the trade rigor that differentiates Paula from a generic brand-campaign deck. |
| Format | **C — 16:9 deck + trade plan as appendix** | Wow on open, rigor on close. The detailed 2-page plan stays as "the detail." |
| Opening concept | **A — Frizz Forecast** (top-scored, 31.5/40 by judge panel) | Most ownable consumer-truth hook; weather → FRIZZ INDEX → pre-merchandised answer across shelf + digital shelf. |
| Build method | **HTML 16:9 slides → PDF (headless print)**, then merge appendix | HTML gives full design control and reuses the existing landing's visual system. python-docx (used by the old deliverable) can't achieve this craft. |
| CV | **Separate attachment, not embedded** | She already has a polished CV PDF; embedding dilutes focus on the idea. |

## Visual system (reuse from existing landing)

Source of truth: `output/2026-05-29/Henkel - Trade & Shopper Marketing Manager - GCC/landing_schwarzkopf/brand.json`

- **Palette:** primary `#000000`, secondary `#FFFFFF`, accent/signal-red `#C41E3A`, bg `#FFFFFF`, text `#0A0A0A`.
- **Type:** Archivo (display, 600/800/900) + Inter (body, 400/500/600), Google Fonts (same `<link>` the landing uses).
- **Tagline:** "Because it's your hair." Brand wordmark: `SCHWARZKOPF` (bold sans, black-on-white / white-on-black).
- **Tone:** premium, professional, confident, editorial.

### Image assets (already generated — reuse, do not regenerate)

From `landing_schwarzkopf/assets/`:
- `hero.jpg` — model with red-streaked hair on black → **Cover (01)**
- `creator.jpg` — creator/lifestyle → **Insight (03)**
- `instore.jpg` — Modern Trade aisle → **Across the shelf (06)** Modern Trade card
- `pharmacy.jpg` → pharmacy card
- `marketplace.jpg` → e-tail card
- `qcommerce.jpg` → quick-commerce card
- `retailmedia.jpg` → retail-media card

Plus `templates/paula_photo.jpg` → **Why Paula (10)**.

The hero "FRIZZ INDEX 87 · HIGH" weather card and the system diagram are **built in HTML/CSS**
(no generated image needed).

## Deck structure — 11 slides + appendix

Each slide is a full-bleed 16:9 page. Copy below is the source content (derived from the
approved Frizz Forecast concept + the existing trade plan).

### 01 · Cover
- Eyebrow: `TRADE & SHOPPER MARKETING PLAN · SCHWARZKOPF HAIR CARE — GCC`
- Title (huge, Archivo 900): **FRIZZ FORECAST**
- Tagline: *"When the humidity spikes, Schwarzkopf is already on the shelf."*
- Sub: "A weather-triggered shopper-activation system for Modern Trade, pharmacy and e-/quick-commerce."
- Lockup: `Prepared by Paula De Francisco Pérez · 29 May 2026 · For: Trade & Shopper Marketing Manager – GCC, Henkel`
- Visual: `hero.jpg`, black gradient, `SCHWARZKOPF` wordmark top-left.

### 02 · Agenda
`01 Shopper insight (GCC) · 02 The big idea — Frizz Forecast · 03 Perfect Store by channel · 04 90-day activation calendar · 05 KPIs, ROI & cadence · 06 Why Paula`

### 03 · Shopper & category insight (GCC)
- **Climate-driven need:** heat, sun & humidity 8+ months/year make damage, frizz and scalp care year-round needs — Schwarzkopf can own "repair & protect" (Gliss) and premium care (BC Bonacure).
- **Two shoppers, two missions:** high-frequency replenishment (grocery/hyper) vs advice-led discovery (pharmacy).
- **Premiumisation + value polarity:** premium expat segment + value-driven mass segment coexist; range and pack-price must serve both without trading down.
- **Channels that matter:** Modern Trade (Carrefour/MAF, Lulu, Union Coop, Spinneys), pharmacy (BinSina, Aster, Life), e-tail (Noon, Amazon.ae), quick-commerce (Noon Minutes, Talabat).
- **Seasonal peaks:** summer (anti-frizz/sun), Ramadan & Eid (gifting, premium), back-to-school, DSF/GITEX.
- Image: `creator.jpg`.

### 04 · The Big Idea ★ (key visual)
- Headline: **FRIZZ FORECAST**
- Insight: in this climate, hair damage isn't a vague worry — it's a daily, predictable, weather-driven event, yet nobody connects the forecast to the fix at the point of purchase.
- Idea: co-opt the one number every GCC shopper already checks (the weather) → a **FRIZZ INDEX (0–100, humidity + UV)** that pulls shelf, digital shelf, retail media and q-commerce in the same direction. When the index spikes, Schwarzkopf's repair-and-protect block (Gliss) and premium care (BC Bonacure) become the category's obvious, pre-merchandised answer.
- Key visual (HTML/CSS): white+red "weather card" reading `FRIZZ INDEX: 87 · HIGH` with a minimal UAE coastline glyph; a hero Gliss bottle on a white shelf strip with a red shelf-edge talker echoing `87 HIGH`. Lockup bottom-left: *"When the humidity spikes, Schwarzkopf is already on the shelf."*

### 05 · How it works (two-layer system)
- **In-store (KAM-sellable):** repair-and-protect secondary display/endcap ships with 3 pre-printed swap-in headers — **LOW / MED / HIGH**. Each Monday a published Frizz Index threshold tells the field which header is live — one recurring summer mechanic, not a real-time gimmick. On HIGH weeks: HIGH header + humidity price-pack bundle (Gliss shampoo+mask). New Perfect Store audit line: **"Frizz block compliance"** (header present + correct tier + bundle faced).
- **Online (genuinely live/automated):** e-tail auto-updating "Today's Frizz Index" badge + search bids scaling on HIGH days; q-commerce weather-triggered "Frizz Index High today" tiles + one-tap "Frizz Rescue" bundle; retail-media weather-API-triggered display bidding up on HIGH days.
- Diagram: `WEATHER → FRIZZ INDEX → [in-store weekly swap] + [online live] → sell-out`.

### 06 · Across the shelf (channel activation, 5 image cards)
- **Modern Trade** (`instore.jpg`): repair-and-protect endcap, LOW/MED/HIGH swap headers, HIGH-week bundle, Frizz block compliance.
- **Pharmacy** (`pharmacy.jpg`): "Frizz Index clinic" — humidity-damage diagnostic card → BC Bonacure tiers; advisor sampling; travel-mask GWP at till on HIGH weeks.
- **E-tail** (`marketplace.jpg`): A+ content leads with the Frizz Index story; auto-updating "Today's Frizz Index" badge; search bids on frizz/humidity/repair scale on HIGH days; review seeding.
- **Quick-commerce** (`qcommerce.jpg`): weather-triggered "Frizz Index High today" tiles; one-tap "Frizz Rescue" bundle; creator codes on worst-humidity days.
- **Retail media & search** (`retailmedia.jpg`): always-on Noon/Amazon/Carrefour sponsored + weather-API-triggered display bidding up on HIGH days; ROAS measurable against the index.

### 07 · Perfect Store standards by channel (table)
Definition line: *a single, measurable picture of success per channel tier — availability, visibility, pricing and activation — audited monthly and tied to KAM scorecards.*

| Channel | Perfect Store priorities |
|---|---|
| Hypermarket / Modern Trade | Hero SKU 100% availability · planogrammed block by benefit · **Frizz block compliance** (header + tier + bundle) · price-pack compliance · promo ROI tracked |
| Pharmacy | Advice fixture for premium care · trained staff/sampling · BC Bonacure & repair range visible · GWP at till |
| E-tail (Noon / Amazon.ae) | A+ content on hero SKUs · 4.3★+ review health · "Today's Frizz Index" badge · search share on "shampoo/hair repair" · pack-shot & title compliance |
| Quick-commerce (Talabat / Noon Minutes) | "Frizz Rescue" bundle · hero-SKU availability · weather-triggered discovery tiles · impulse pricing |

### 08 · 90-day trade activation calendar (timeline)
| Window | Activation | Channel | Mechanic | Objective |
|---|---|---|---|---|
| Wk 1–2 | Onboarding & Perfect Store audit | All | Baseline scorecard + KAM 1:1s | Diagnose gaps |
| Wk 3–4 | Hero-SKU availability fix + Frizz block set-up | MT + e-tail | Must-stock list, A+ refresh, swap-header kit ship | Distribution +X pts |
| Month 2 | Summer HIGH-Frizz burst | MT + pharmacy | HIGH header + GWP + sampling + bundle | Sell-out uplift |
| Month 2 | Weather-triggered q-commerce push | Talabat/Noon Min. | "Frizz Rescue" tiles + creator codes | Trial & basket size |
| Month 3 | Ramadan/premium gifting pre-build | MT + pharmacy | Gift packs + premium endcap | Premium mix up |
| Month 3 | Business review & scale | All | Promo ROI readout, scale winners | Lock Q4 plan |

### 09 · KPIs, ROI & cadence (dashboard)
| KPI | What it proves | Cadence |
|---|---|---|
| **Sell-out uplift vs baseline (HIGH-Frizz weeks)** — HERO | Activation effectiveness | Per activity |
| Numeric & weighted distribution (hero SKUs) | Availability foundation | Monthly |
| Perfect Store / Frizz block compliance % | Execution quality | Monthly audit |
| Promo ROI / ROAS | Spend efficiency | Per activity + QBR |
| E-tail search share ("anti-frizz/repair") & review health | Digital shelf strength (leading indicator) | Bi-weekly |
| Premium mix % | Value growth, not just volume | Monthly |

Cadence line: *monthly business reviews (Sales, Supply Chain, Finance, Marketing); quarterly JBP checkpoints with key accounts; A&P managed to ROI throughout.*

### 10 · Why Paula
- Photo: `templates/paula_photo.jpg`.
- "Why I can land this fast": builds trade & shopper plans by channel across **50+ markets at DoFreeze**; ran **42 key accounts to +30% GMV QoQ at Alibaba's Miravia**; integrates brands into UAE modern trade and quick-commerce (Noon, Talabat, Careem, Deliveroo).
- Personal close (authentic, Helena-style): *"Frizz Forecast is exactly how I think — take a real shopper truth, turn it into a mechanic the field can sell and audit, and prove it with ROI."*
- Skills row: shopper/category insight · Perfect Store & JBP · e-/quick-commerce · KPI & ROI discipline.

### 11 · Contact
- `CONTACT` (huge). `paulich98@hotmail.com · +971 50 386 3656 · linkedin.com/in/paula-de-francisco-perez`.
- Pull contact details from `settings.profile["personal"]` (do not hardcode).

### Appendix A1–A2
- The existing 2-page **Trade & Shopper Marketing Plan — Schwarzkopf Hair Care, GCC** PDF (`Deliverable_Paula_Henkel_Trade-Shopper-Plan_Schwarzkopf.pdf`), appended after the deck.

## Build approach

New one-off build script `scripts/_henkel_frizz_forecast_deck.py` (prefixed `_`, mirroring the
existing bespoke `scripts/_henkel_trade_plan.py` pattern — a dev/maintenance one-shot, not a
Paula-facing action). Steps:

1. **Render HTML deck** — one `deck.html` with 11 `.slide` sections, the Schwarzkopf system,
   inline references to the asset images and `paula_photo.jpg`. Built next to the assets so
   relative image paths resolve, e.g. a working dir under the Henkel folder.
2. **HTML → PDF** via headless Chromium print (Playwright — already used by the repo's
   scroll-landing pipeline; `playwright install chromium` auto-handled). Print CSS:
   `@page { size: 1280px 720px landscape; margin: 0 }`, each `.slide { width:1280px; height:720px; page-break-after: always }`, `printBackground: true`.
3. **Merge** deck PDF + the existing trade-plan PDF into one final file using `pypdf`.
4. **Output:** `output/2026-05-29/Henkel - Trade & Shopper Marketing Manager - GCC/Deliverable_Paula_Henkel_Frizz-Forecast_Deck.pdf` (deck only) and `..._Frizz-Forecast_FULL.pdf` (deck + appendix).

### Headless-print gotchas (from the `landing-to-pdf` skill — must honor)
- **No scroll-reveal / IntersectionObserver animations** — they render as `opacity:0` in headless
  screenshots. The deck is fully static (print-first CSS); any reveal effect must default to visible
  when printing.
- **Eager-load all images** (`loading="eager"`, no lazy) so every asset is fetched before print.
- Wait for `fonts.ready` / network idle before printing so Archivo/Inter are embedded.

## Non-goals / constraints

- **Nothing is sent.** This produces a draft PDF for human review only (repo's core principle).
- **No dashboard button this round.** Consistent with the existing `_henkel_trade_plan.py` one-off;
  wiring a reusable "Generate deck" dashboard action is a possible follow-up, not in scope here.
- **No new image generation.** Reuse the 7 existing assets + Paula's photo.
- **Do not regenerate or alter the existing trade-plan PDF** — it is consumed as the appendix as-is.
- Config/contact details come from `career_ops.config.settings`, never hardcoded.

## Open questions

None blocking. (Placeholder figures like "Distribution +X pts" stay as written — they read as a
plan template, matching the existing deliverable's tone.)
