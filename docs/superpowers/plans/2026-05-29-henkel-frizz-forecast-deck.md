# Frizz Forecast Deck — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a 16:9 visual pitch deck (11 slides) for Paula's Henkel application around the "Frizz Forecast" concept, render it to PDF via headless Chromium, and merge the existing 2-page trade plan as an appendix.

**Architecture:** A single one-off build script `scripts/_henkel_frizz_forecast_deck.py` (mirrors the existing bespoke `scripts/_henkel_trade_plan.py`). It stages reusable image assets into a working dir, generates one self-contained `deck.html` (Schwarzkopf system: black/white/#C41E3A, Archivo+Inter, the 7 channel images + Paula's photo), renders it to a multi-page PDF with Playwright (`page.pdf()`, one `.slide` = one page), and merges the existing trade-plan PDF after it with `pypdf`.

**Tech Stack:** Python, Playwright (Chromium, already installed; render pattern mirrors `career_ops/generators/landing_generator.py:509`), pypdf 6.x, Google Fonts (Archivo+Inter).

**Spec:** [docs/superpowers/specs/2026-05-29-henkel-frizz-forecast-deck-design.md](../specs/2026-05-29-henkel-frizz-forecast-deck-design.md)

**Key constraints (from spec):** Nothing is sent — draft PDF only. No new image generation (reuse 7 assets + photo). Do not alter the existing trade-plan PDF. Contact/profile from `career_ops.config.settings`, never hardcoded. Static print-first CSS — no IntersectionObserver/reveal animations (they render as `opacity:0` headless); images eager; wait for `document.fonts.ready`.

---

## File Structure

- **Create:** `scripts/_henkel_frizz_forecast_deck.py` — the entire build (paths, asset staging, CSS, 11 slide builders, HTML assembly, render, merge, `main()` with `--html-only`).
- **Generated at runtime (not committed):**
  - `output/2026-05-29/Henkel - Trade & Shopper Marketing Manager - GCC/frizz_forecast_deck/deck.html` + `assets/*.jpg`
  - `.../Deliverable_Paula_Henkel_Frizz-Forecast_Deck.pdf` (deck only, 11 pages)
  - `.../Deliverable_Paula_Henkel_Frizz-Forecast_FULL.pdf` (deck + 2-page appendix = 13 pages)
- **Consumed read-only:** `.../landing_schwarzkopf/assets/{hero,creator,instore,pharmacy,marketplace,qcommerce,retailmedia}.jpg`, `templates/paula_photo.jpg`, `.../Deliverable_Paula_Henkel_Trade-Shopper-Plan_Schwarzkopf.pdf`.

The whole build is one focused file (~500 lines). It is a deck generator with one responsibility; keeping it single-file matches the `_henkel_trade_plan.py` precedent and keeps the slide copy + design in one place.

---

### Task 1: Script skeleton — paths, profile, asset staging, CLI

**Files:**
- Create: `scripts/_henkel_frizz_forecast_deck.py`

- [ ] **Step 1: Write the skeleton (paths + asset staging + arg parsing)**

```python
#!/usr/bin/env python3
"""Frizz Forecast — Schwarzkopf GCC pitch deck for Paula's Henkel application.

A 16:9 visual deck (11 slides) rendered HTML -> PDF via headless Chromium, then
merged with the existing 2-page trade plan as an appendix. One-off build script
(mirrors scripts/_henkel_trade_plan.py). Nothing is sent — produces a draft PDF.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings  # noqa: E402

HENKEL_DIR = ROOT / "output" / "2026-05-29" / "Henkel - Trade & Shopper Marketing Manager - GCC"
LANDING_ASSETS = HENKEL_DIR / "landing_schwarzkopf" / "assets"
PAULA_PHOTO = ROOT / "templates" / "paula_photo.jpg"

BUILD_DIR = HENKEL_DIR / "frizz_forecast_deck"
BUILD_ASSETS = BUILD_DIR / "assets"
HTML_PATH = BUILD_DIR / "deck.html"

DECK_PDF = HENKEL_DIR / "Deliverable_Paula_Henkel_Frizz-Forecast_Deck.pdf"
FULL_PDF = HENKEL_DIR / "Deliverable_Paula_Henkel_Frizz-Forecast_FULL.pdf"
APPENDIX_PDF = HENKEL_DIR / "Deliverable_Paula_Henkel_Trade-Shopper-Plan_Schwarzkopf.pdf"

P = settings.profile["personal"]
CHANNEL_IMAGES = ["hero", "creator", "instore", "pharmacy", "marketplace", "qcommerce", "retailmedia"]


def stage_assets() -> None:
    """Copy the 7 reusable channel images + Paula's photo into the build dir."""
    BUILD_ASSETS.mkdir(parents=True, exist_ok=True)
    for name in CHANNEL_IMAGES:
        shutil.copyfile(LANDING_ASSETS / f"{name}.jpg", BUILD_ASSETS / f"{name}.jpg")
    shutil.copyfile(PAULA_PHOTO, BUILD_ASSETS / "paula.jpg")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html-only", action="store_true", help="Write deck.html and stop (no PDF).")
    args = ap.parse_args()

    stage_assets()
    HTML_PATH.write_text(build_html(), encoding="utf-8")
    print(f"HTML: {HTML_PATH}")
    if args.html_only:
        return

    render_pdf(HTML_PATH, DECK_PDF)
    print(f"DECK PDF: {DECK_PDF}")
    merge_pdfs(DECK_PDF, APPENDIX_PDF, FULL_PDF)
    print(f"FULL PDF: {FULL_PDF}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Add temporary stubs so the skeleton imports/runs**

Add these stubs **above `main()`** (replaced in later tasks):

```python
def build_html() -> str:
    return "<!DOCTYPE html><html><body>stub</body></html>"


def render_pdf(html_path: Path, pdf_path: Path) -> None:  # replaced in Task 8
    raise NotImplementedError


def merge_pdfs(deck_pdf: Path, appendix_pdf: Path, out_pdf: Path) -> None:  # replaced in Task 9
    raise NotImplementedError
```

- [ ] **Step 3: Verify asset staging + HTML write works**

Run: `python scripts/_henkel_frizz_forecast_deck.py --html-only`
Expected: prints `HTML: ...deck.html`; no error. Then verify all 8 assets staged:
Run: `python -c "from pathlib import Path; d=Path(r'output/2026-05-29/Henkel - Trade & Shopper Marketing Manager - GCC/frizz_forecast_deck/assets'); print(sorted(p.name for p in d.glob('*.jpg')))"`
Expected: `['creator.jpg', 'hero.jpg', 'instore.jpg', 'marketplace.jpg', 'paula.jpg', 'pharmacy.jpg', 'qcommerce.jpg', 'retailmedia.jpg']`

- [ ] **Step 4: Commit**

```bash
git add scripts/_henkel_frizz_forecast_deck.py
git commit -m "feat(henkel): scaffold Frizz Forecast deck build script + asset staging"
```

---

### Task 2: Design system (CSS + HTML document shell)

**Files:**
- Modify: `scripts/_henkel_frizz_forecast_deck.py`

- [ ] **Step 1: Add the CSS constant + document shell**

Add near the top (after `CHANNEL_IMAGES`). This is a plain string (not f-string) so CSS braces are literal:

```python
CSS = """
*{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
@page{size:1280px 720px;margin:0}
html,body{background:#fff}
body{font-family:'Inter',system-ui,sans-serif;color:#0a0a0a}
.slide{position:relative;width:1280px;height:720px;overflow:hidden;background:#fff;page-break-after:always}
.slide:last-child{page-break-after:auto}
.dark{background:#0a0a0a;color:#fff}
.pad{position:absolute;inset:0;padding:74px 88px}
.red{color:#C41E3A}
.eyebrow{font-family:'Archivo',sans-serif;font-weight:800;font-size:14px;letter-spacing:3px;text-transform:uppercase;color:#C41E3A}
.wordmark{font-family:'Archivo',sans-serif;font-weight:900;letter-spacing:2px;font-size:17px}
.kicker{font-family:'Archivo',sans-serif;font-weight:800;font-size:13px;letter-spacing:2px;text-transform:uppercase;color:#9a9a9a}
.h2{font-family:'Archivo',sans-serif;font-weight:900;font-size:52px;line-height:.95;letter-spacing:-1.5px;color:#0a0a0a}
.h2.on-dark{color:#fff}
.lead{font-size:18px;line-height:1.5;color:#333;max-width:760px}
.lead.on-dark{color:#cfcfcf}
.pagenum{position:absolute;bottom:38px;right:60px;font-family:'Archivo',sans-serif;font-weight:900;font-size:40px;color:#C41E3A}
.foot{position:absolute;bottom:34px;left:88px;font-size:10.5px;color:#9a9a9a;letter-spacing:.4px}
ul.bullets{list-style:none;margin-top:8px}
ul.bullets li{position:relative;padding-left:24px;margin:15px 0;font-size:16px;line-height:1.45;color:#262626;max-width:560px}
ul.bullets li::before{content:"";position:absolute;left:0;top:8px;width:9px;height:9px;background:#C41E3A;border-radius:50%}
ul.bullets li b{color:#0a0a0a}
table.ps{width:100%;border-collapse:collapse;margin-top:22px;font-size:14px}
table.ps th{background:#0a0a0a;color:#fff;text-align:left;padding:13px 16px;font-family:'Archivo',sans-serif;font-weight:800;font-size:12.5px;letter-spacing:.6px;text-transform:uppercase}
table.ps td{border-bottom:1px solid #e6e6e6;padding:13px 16px;vertical-align:top;color:#222;line-height:1.4}
table.ps tr td:first-child{font-weight:700;color:#0a0a0a;width:260px}
table.ps b{color:#C41E3A}
/* cover */
.cover-img{position:absolute;right:0;top:0;width:560px;height:720px;object-fit:cover;filter:grayscale(.05)}
.cover-fade{position:absolute;right:480px;top:0;width:260px;height:720px;background:linear-gradient(90deg,#0a0a0a,transparent)}
.cover-title{font-family:'Archivo',sans-serif;font-weight:900;font-size:128px;line-height:.84;letter-spacing:-4px;color:#fff}
.cover-tag{font-size:21px;color:#fff;margin-top:26px;max-width:560px;line-height:1.35}
.cover-lockup{position:absolute;bottom:48px;left:88px;font-size:12px;color:#bdbdbd;letter-spacing:.4px;line-height:1.6}
/* agenda */
.agenda-row{display:flex;align-items:baseline;gap:22px;padding:16px 0;border-bottom:1px solid #ececec}
.agenda-num{font-family:'Archivo',sans-serif;font-weight:900;font-size:24px;color:#C41E3A;width:48px}
.agenda-txt{font-family:'Archivo',sans-serif;font-weight:800;font-size:26px;color:#0a0a0a;letter-spacing:-.5px}
/* big idea key visual */
.kv-card{position:absolute;left:88px;top:150px;width:330px;background:#fff;border-radius:14px;padding:26px 30px;box-shadow:0 24px 60px rgba(0,0,0,.45)}
.kv-card .lbl{font-family:'Archivo',sans-serif;font-weight:800;font-size:13px;letter-spacing:2px;color:#444}
.kv-card .val{font-family:'Archivo',sans-serif;font-weight:900;font-size:104px;line-height:.9;color:#C41E3A}
.kv-card .state{font-family:'Archivo',sans-serif;font-weight:900;font-size:22px;letter-spacing:3px;color:#0a0a0a}
.kv-card .bar{margin-top:14px;height:8px;border-radius:6px;background:linear-gradient(90deg,#f5c518,#C41E3A)}
.kv-bottle{position:absolute;right:150px;bottom:150px;width:96px;height:300px;border-radius:14px 14px 6px 6px;background:linear-gradient(180deg,#efefef,#c8c8c8)}
.kv-shelf{position:absolute;right:96px;bottom:138px;width:240px;height:14px;background:#fff}
.kv-talker{position:absolute;right:96px;bottom:118px;width:240px;height:22px;background:#C41E3A;color:#fff;font-family:'Archivo',sans-serif;font-weight:800;font-size:12px;letter-spacing:2px;display:flex;align-items:center;justify-content:center}
.kv-lockup{position:absolute;left:88px;bottom:70px;color:#fff;font-size:20px;line-height:1.3;max-width:480px}
/* how-it-works flow */
.flow{display:flex;align-items:stretch;gap:18px;margin-top:30px}
.flow .node{flex:1;background:#f6f6f6;border-left:5px solid #C41E3A;border-radius:8px;padding:20px}
.flow .node h4{font-family:'Archivo',sans-serif;font-weight:800;font-size:17px;margin-bottom:8px}
.flow .node p{font-size:13.5px;line-height:1.4;color:#444}
.two{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:26px}
.two .col h4{font-family:'Archivo',sans-serif;font-weight:800;font-size:19px;color:#0a0a0a;margin-bottom:6px}
.two .col .tagcol{font-size:12px;color:#C41E3A;font-weight:700;letter-spacing:1px;text-transform:uppercase}
/* channel cards */
.cards5{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:30px}
.cc{border-radius:10px;overflow:hidden;background:#fff;border:1px solid #ececec}
.cc img{width:100%;height:120px;object-fit:cover;display:block}
.cc .body{padding:12px 13px}
.cc h4{font-family:'Archivo',sans-serif;font-weight:800;font-size:14px;margin-bottom:6px;color:#0a0a0a}
.cc p{font-size:11.5px;line-height:1.35;color:#444}
/* why paula */
.why-photo{position:absolute;right:0;top:0;width:470px;height:720px;object-fit:cover}
.why-quote{font-family:'Archivo',sans-serif;font-weight:800;font-size:25px;line-height:1.25;color:#0a0a0a;max-width:600px;margin-top:18px}
.skillrow{display:flex;gap:10px;flex-wrap:wrap;margin-top:26px}
.skillrow span{font-size:12px;font-weight:600;color:#0a0a0a;border:1px solid #d8d8d8;border-radius:999px;padding:7px 14px}
/* contact */
.contact-big{font-family:'Archivo',sans-serif;font-weight:900;font-size:180px;line-height:.85;letter-spacing:-6px;color:#fff}
.contact-line{font-size:18px;color:#fff;margin-top:8px;letter-spacing:.5px}
"""


def html_doc(slides: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{slides}
</body>
</html>"""
```

- [ ] **Step 2: Replace the `build_html` stub** with the real assembler (calls one builder per slide; builders are added in Tasks 3–7):

```python
def build_html() -> str:
    slides = "\n".join([
        slide_cover(),
        slide_agenda(),
        slide_insight(),
        slide_big_idea(),
        slide_how(),
        slide_channels(),
        slide_perfect_store(),
        slide_calendar(),
        slide_kpis(),
        slide_why_paula(),
        slide_contact(),
    ])
    return html_doc(slides)
```

- [ ] **Step 3: Add placeholder builders so it runs** (each replaced in Tasks 3–7):

```python
def slide_cover() -> str: return '<section class="slide dark"><div class="pad">cover</div></section>'
def slide_agenda() -> str: return '<section class="slide"><div class="pad">agenda</div></section>'
def slide_insight() -> str: return '<section class="slide"><div class="pad">insight</div></section>'
def slide_big_idea() -> str: return '<section class="slide dark"><div class="pad">big idea</div></section>'
def slide_how() -> str: return '<section class="slide"><div class="pad">how</div></section>'
def slide_channels() -> str: return '<section class="slide"><div class="pad">channels</div></section>'
def slide_perfect_store() -> str: return '<section class="slide"><div class="pad">perfect store</div></section>'
def slide_calendar() -> str: return '<section class="slide"><div class="pad">calendar</div></section>'
def slide_kpis() -> str: return '<section class="slide"><div class="pad">kpis</div></section>'
def slide_why_paula() -> str: return '<section class="slide dark"><div class="pad">why paula</div></section>'
def slide_contact() -> str: return '<section class="slide dark"><div class="pad">contact</div></section>'
```

- [ ] **Step 4: Verify it assembles 11 slides**

Run: `python scripts/_henkel_frizz_forecast_deck.py --html-only`
Then: `python -c "p=open(r'output/2026-05-29/Henkel - Trade & Shopper Marketing Manager - GCC/frizz_forecast_deck/deck.html',encoding='utf-8').read(); print('slides=',p.count('<section class=\"slide')); print('fonts=','Archivo' in p)"`
Expected: `slides= 11` and `fonts= True`

- [ ] **Step 5: Commit**

```bash
git add scripts/_henkel_frizz_forecast_deck.py
git commit -m "feat(henkel): add Schwarzkopf design system CSS + 11-slide shell"
```

---

### Task 3: Slides 01–02 (Cover + Agenda)

**Files:**
- Modify: `scripts/_henkel_frizz_forecast_deck.py` (replace `slide_cover`, `slide_agenda`)

- [ ] **Step 1: Implement the two builders**

```python
def slide_cover() -> str:
    return f"""<section class="slide dark">
  <img class="cover-img" src="assets/hero.jpg" loading="eager" alt="">
  <div class="cover-fade"></div>
  <div class="pad">
    <div class="wordmark">SCHWARZKOPF</div>
    <div class="eyebrow" style="margin-top:54px">Trade &amp; Shopper Marketing Plan · Hair Care — GCC</div>
    <div class="cover-title" style="margin-top:18px">FRIZZ<br>FORECAST</div>
    <div class="cover-tag">When the humidity spikes, Schwarzkopf is already on the shelf.</div>
  </div>
  <div class="cover-lockup">
    Prepared by {P['name']} &nbsp;·&nbsp; 29 May 2026<br>
    For: Trade &amp; Shopper Marketing Manager – GCC, Henkel
  </div>
</section>"""


def slide_agenda() -> str:
    rows = [
        ("01", "Shopper insight — GCC"),
        ("02", "The big idea — Frizz Forecast"),
        ("03", "Perfect Store by channel"),
        ("04", "90-day activation calendar"),
        ("05", "KPIs, ROI &amp; cadence"),
        ("06", "Why Paula"),
    ]
    body = "".join(
        f'<div class="agenda-row"><div class="agenda-num">{n}</div><div class="agenda-txt">{t}</div></div>'
        for n, t in rows
    )
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">Agenda</div>
    <div class="h2" style="margin:6px 0 28px">The plan, end&nbsp;to&nbsp;end.</div>
    {body}
  </div>
  <div class="pagenum">01</div>
</section>"""
```

- [ ] **Step 2: Verify content present**

Run: `python scripts/_henkel_frizz_forecast_deck.py --html-only`
Then: `python -c "p=open(r'output/2026-05-29/Henkel - Trade & Shopper Marketing Manager - GCC/frizz_forecast_deck/deck.html',encoding='utf-8').read(); assert 'FRIZZ' in p and 'already on the shelf' in p and 'The big idea' in p; print('ok')"`
Expected: `ok`

- [ ] **Step 3: Commit**

```bash
git add scripts/_henkel_frizz_forecast_deck.py
git commit -m "feat(henkel): cover + agenda slides"
```

---

### Task 4: Slides 03–04 (Shopper insight + The Big Idea key visual)

**Files:**
- Modify: `scripts/_henkel_frizz_forecast_deck.py` (replace `slide_insight`, `slide_big_idea`)

- [ ] **Step 1: Implement the two builders**

```python
def slide_insight() -> str:
    return f"""<section class="slide">
  <img src="assets/creator.jpg" loading="eager" alt=""
       style="position:absolute;right:0;top:0;width:430px;height:720px;object-fit:cover">
  <div class="pad" style="padding-right:480px">
    <div class="kicker">01 · Shopper &amp; category insight — GCC</div>
    <div class="h2" style="margin:6px 0 18px">Hair damage here is<br>a daily, weather event.</div>
    <ul class="bullets">
      <li><b>Climate-driven need:</b> heat, sun &amp; humidity 8+ months/year make damage, frizz and scalp care year-round needs — Schwarzkopf can own "repair &amp; protect" (Gliss) and premium care (BC Bonacure).</li>
      <li><b>Two shoppers, two missions:</b> high-frequency replenishment in grocery/hyper vs. advice-led discovery in pharmacy.</li>
      <li><b>Premium + value polarity:</b> a premium expat segment and a value mass segment coexist — the range must serve both without trading down.</li>
      <li><b>Channels that matter:</b> Modern Trade (Carrefour/MAF, Lulu, Union Coop, Spinneys), pharmacy (BinSina, Aster, Life), e-tail (Noon, Amazon.ae), quick-commerce (Noon Minutes, Talabat).</li>
      <li><b>Seasonal peaks:</b> summer anti-frizz, Ramadan &amp; Eid gifting, back-to-school, DSF/GITEX.</li>
    </ul>
  </div>
  <div class="pagenum">02</div>
</section>"""


def slide_big_idea() -> str:
    return f"""<section class="slide dark">
  <div class="pad">
    <div class="eyebrow">02 · The big idea</div>
    <div class="cover-title" style="font-size:84px;margin-top:10px">FRIZZ FORECAST</div>
    <div class="lead on-dark" style="margin-top:18px;max-width:540px">
      Co-opt the one number every GCC shopper already checks — the weather — and turn it into a
      live <b style="color:#fff">FRIZZ INDEX (0–100)</b>. When it spikes, Schwarzkopf's repair block
      (Gliss) and premium care (BC Bonacure) become the category's pre-merchandised answer, in-store and online.
    </div>
  </div>
  <div class="kv-card">
    <div class="lbl">FRIZZ INDEX</div>
    <div class="val">87</div>
    <div class="state">HIGH</div>
    <div class="bar"></div>
  </div>
  <div class="kv-bottle"></div>
  <div class="kv-shelf"></div>
  <div class="kv-talker">FRIZZ INDEX · 87 HIGH</div>
  <div class="kv-lockup">"When the humidity spikes,<br>Schwarzkopf is already on the shelf."</div>
</section>"""
```

- [ ] **Step 2: Verify content present**

Run: `python scripts/_henkel_frizz_forecast_deck.py --html-only`
Then: `python -c "p=open(r'output/2026-05-29/Henkel - Trade & Shopper Marketing Manager - GCC/frizz_forecast_deck/deck.html',encoding='utf-8').read(); assert 'FRIZZ INDEX' in p and 'BinSina' in p and 'kv-card' in p; print('ok')"`
Expected: `ok`

- [ ] **Step 3: Commit**

```bash
git add scripts/_henkel_frizz_forecast_deck.py
git commit -m "feat(henkel): shopper-insight + big-idea key-visual slides"
```

---

### Task 5: Slides 05–06 (How it works + Across the shelf)

**Files:**
- Modify: `scripts/_henkel_frizz_forecast_deck.py` (replace `slide_how`, `slide_channels`)

- [ ] **Step 1: Implement the two builders**

```python
def slide_how() -> str:
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">02 · How it works</div>
    <div class="h2" style="margin:6px 0 4px">One index. Two layers.</div>
    <div class="flow">
      <div class="node"><h4>Weather</h4><p>Humidity + UV, the number every GCC shopper already checks daily.</p></div>
      <div class="node"><h4>Frizz Index 0–100</h4><p>Published weekly threshold → LOW / MED / HIGH.</p></div>
      <div class="node"><h4>Pre-merchandised answer</h4><p>Repair &amp; protect block becomes the obvious fix.</p></div>
    </div>
    <div class="two">
      <div class="col">
        <div class="tagcol">In-store · KAM-sellable</div>
        <h4>A weekly swap, not a gimmick</h4>
        <ul class="bullets">
          <li>Repair endcap ships with 3 pre-printed headers — <b>LOW / MED / HIGH</b>. Each Monday the published index says which is live.</li>
          <li>On HIGH weeks: swap to the HIGH header + a humidity price-pack bundle (Gliss shampoo+mask).</li>
          <li>New Perfect Store audit line: <b>"Frizz block compliance"</b> (header + correct tier + bundle faced).</li>
        </ul>
      </div>
      <div class="col">
        <div class="tagcol">Online · genuinely live</div>
        <h4>Automated where it can be</h4>
        <ul class="bullets">
          <li>E-tail "Today's Frizz Index" badge + search bids that scale on HIGH days.</li>
          <li>Q-commerce weather-triggered tiles + one-tap "Frizz Rescue" bundle.</li>
          <li>Retail-media display bids up on HIGH days — ROAS measurable against the index.</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="pagenum">03</div>
</section>"""


def slide_channels() -> str:
    cards = [
        ("instore", "Modern Trade", "Repair &amp; protect endcap, LOW/MED/HIGH swap headers, HIGH-week bundle, Frizz block compliance."),
        ("pharmacy", "Pharmacy", "\"Frizz Index clinic\": humidity-damage diagnostic → BC Bonacure tiers, advisor sampling, travel-mask GWP at till on HIGH weeks."),
        ("marketplace", "E-tail", "A+ content led by the Frizz Index, auto-updating \"Today's Frizz Index\" badge, search bids on frizz/repair, review seeding."),
        ("qcommerce", "Quick-commerce", "Weather-triggered \"Frizz Index High today\" tiles, one-tap \"Frizz Rescue\" bundle, creator codes on worst-humidity days."),
        ("retailmedia", "Retail media", "Always-on Noon/Amazon/Carrefour sponsored + weather-API display bidding up on HIGH days. ROAS vs the index."),
    ]
    cc = "".join(
        f'<div class="cc"><img src="assets/{img}.jpg" loading="eager" alt=""><div class="body"><h4>{title}</h4><p>{body}</p></div></div>'
        for img, title, body in cards
    )
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">02 · Across the shelf</div>
    <div class="h2" style="margin:6px 0 0">The same index, every channel.</div>
    <div class="cards5">{cc}</div>
  </div>
  <div class="pagenum">04</div>
</section>"""
```

- [ ] **Step 2: Verify content present**

Run: `python scripts/_henkel_frizz_forecast_deck.py --html-only`
Then: `python -c "p=open(r'output/2026-05-29/Henkel - Trade & Shopper Marketing Manager - GCC/frizz_forecast_deck/deck.html',encoding='utf-8').read(); assert 'Frizz block compliance' in p and 'Frizz Rescue' in p and p.count('class=\"cc\"')==5; print('ok')"`
Expected: `ok`

- [ ] **Step 3: Commit**

```bash
git add scripts/_henkel_frizz_forecast_deck.py
git commit -m "feat(henkel): how-it-works + across-the-shelf channel slides"
```

---

### Task 6: Slides 07–09 (Perfect Store table + Calendar + KPIs)

**Files:**
- Modify: `scripts/_henkel_frizz_forecast_deck.py` (replace `slide_perfect_store`, `slide_calendar`, `slide_kpis`)

- [ ] **Step 1: Add a shared table helper + the three builders**

```python
def _table(headers: list[str], rows: list[list[str]]) -> str:
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="ps"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def slide_perfect_store() -> str:
    rows = [
        ["Hypermarket / Modern Trade", "Hero SKU 100% availability · planogrammed block by benefit · <b>Frizz block compliance</b> (header + tier + bundle) · price-pack compliance · promo ROI tracked"],
        ["Pharmacy", "Advice fixture for premium care · trained staff/sampling · BC Bonacure &amp; repair range visible · GWP at till"],
        ["E-tail (Noon / Amazon.ae)", 'A+ content on hero SKUs · 4.3★+ review health · <b>"Today\\'s Frizz Index" badge</b> · search share on "shampoo/hair repair" · pack-shot &amp; title compliance'],
        ["Quick-commerce (Talabat / Noon Minutes)", '<b>"Frizz Rescue" bundle</b> · hero-SKU availability · weather-triggered discovery tiles · impulse pricing'],
    ]
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">03 · Perfect Store standards by channel</div>
    <div class="h2" style="margin:6px 0 2px">One measurable picture per channel.</div>
    <div class="lead" style="font-size:15px;margin-top:8px">Availability, visibility, pricing and activation — audited monthly and tied to KAM scorecards.</div>
    {_table(["Channel", "Perfect Store priorities"], rows)}
  </div>
  <div class="pagenum">05</div>
</section>"""


def slide_calendar() -> str:
    rows = [
        ["Wk 1–2", "Onboarding &amp; Perfect Store audit", "All", "Baseline scorecard + KAM 1:1s", "Diagnose gaps"],
        ["Wk 3–4", "Hero-SKU fix + Frizz block set-up", "MT + e-tail", "Must-stock list, A+ refresh, swap-header kit ship", "Distribution +X pts"],
        ["Month 2", "Summer HIGH-Frizz burst", "MT + pharmacy", "HIGH header + GWP + sampling + bundle", "Sell-out uplift"],
        ["Month 2", "Weather-triggered q-commerce push", "Talabat/Noon Min.", '"Frizz Rescue" tiles + creator codes', "Trial &amp; basket size"],
        ["Month 3", "Ramadan/premium gifting pre-build", "MT + pharmacy", "Gift packs + premium endcap", "Premium mix up"],
        ["Month 3", "Business review &amp; scale", "All", "Promo ROI readout, scale winners", "Lock Q4 plan"],
    ]
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">04 · 90-day trade activation calendar</div>
    <div class="h2" style="margin:6px 0 2px">From audit to scale in 90 days.</div>
    {_table(["Window", "Activation", "Channel", "Mechanic", "Objective"], rows)}
  </div>
  <div class="pagenum">06</div>
</section>"""


def slide_kpis() -> str:
    rows = [
        ['<b>Sell-out uplift vs baseline (HIGH-Frizz weeks)</b>', "Activation effectiveness — the hero KPI", "Per activity"],
        ["Numeric &amp; weighted distribution (hero SKUs)", "Availability foundation", "Monthly"],
        ["Perfect Store / Frizz block compliance %", "Execution quality", "Monthly audit"],
        ["Promo ROI / ROAS", "Spend efficiency", "Per activity + QBR"],
        ['E-tail search share ("anti-frizz/repair") &amp; review health', "Digital shelf strength (leading indicator)", "Bi-weekly"],
        ["Premium mix %", "Value growth, not just volume", "Monthly"],
    ]
    return f"""<section class="slide">
  <div class="pad">
    <div class="kicker">05 · KPIs, ROI &amp; cadence</div>
    <div class="h2" style="margin:6px 0 2px">Prove it moves the number.</div>
    {_table(["KPI", "What it proves", "Cadence"], rows)}
    <div class="lead" style="font-size:14px;margin-top:18px"><b class="red">Cadence:</b> monthly business reviews with Sales, Supply Chain, Finance &amp; Marketing; quarterly JBP checkpoints with key accounts; A&amp;P managed to ROI throughout.</div>
  </div>
  <div class="pagenum">07</div>
</section>"""
```

Note: the `Today\\'s` / single quotes inside the Python list strings are escaped for Python; the rendered HTML shows `Today's`. Keep the `\\'` exactly as written.

- [ ] **Step 2: Verify content present**

Run: `python scripts/_henkel_frizz_forecast_deck.py --html-only`
Then: `python -c "p=open(r'output/2026-05-29/Henkel - Trade & Shopper Marketing Manager - GCC/frizz_forecast_deck/deck.html',encoding='utf-8').read(); assert p.count('<table class=\"ps\"')==3 and 'Sell-out uplift' in p and 'Lock Q4 plan' in p; print('ok')"`
Expected: `ok`

- [ ] **Step 3: Commit**

```bash
git add scripts/_henkel_frizz_forecast_deck.py
git commit -m "feat(henkel): perfect-store + calendar + KPI table slides"
```

---

### Task 7: Slides 10–11 (Why Paula + Contact)

**Files:**
- Modify: `scripts/_henkel_frizz_forecast_deck.py` (replace `slide_why_paula`, `slide_contact`)

- [ ] **Step 1: Implement the two builders** (profile values from `settings`, never hardcoded)

```python
def slide_why_paula() -> str:
    return f"""<section class="slide">
  <img class="why-photo" src="assets/paula.jpg" loading="eager" alt="">
  <div class="pad" style="padding-right:500px">
    <div class="kicker">06 · Why Paula</div>
    <div class="why-quote">"Frizz Forecast is exactly how I think — take a real shopper truth, turn it into a mechanic the field can sell and audit, and prove it with ROI."</div>
    <ul class="bullets" style="margin-top:22px">
      <li>Builds trade &amp; shopper plans by channel across <b>50+ markets</b> at DoFreeze.</li>
      <li>Ran <b>42 key accounts to +30% GMV QoQ</b> at Alibaba's Miravia.</li>
      <li>Integrates brands into UAE modern trade &amp; quick-commerce (Noon, Talabat, Careem, Deliveroo).</li>
    </ul>
    <div class="skillrow">
      <span>Shopper &amp; category insight</span><span>Perfect Store &amp; JBP</span>
      <span>e-/quick-commerce</span><span>KPI &amp; ROI discipline</span>
    </div>
  </div>
  <div class="pagenum">08</div>
</section>"""


def slide_contact() -> str:
    linkedin = P.get("linkedin", "").replace("https://", "").replace("http://", "")
    return f"""<section class="slide dark">
  <div class="pad">
    <div class="wordmark">SCHWARZKOPF</div>
    <div class="contact-big" style="margin-top:150px">CONTACT</div>
    <div class="contact-line" style="margin-top:30px">{P['email']}</div>
    <div class="contact-line">{P['phone']}</div>
    <div class="contact-line">{linkedin}</div>
  </div>
</section>"""
```

- [ ] **Step 2: Verify profile values render (not literal keys)**

Run: `python scripts/_henkel_frizz_forecast_deck.py --html-only`
Then: `python -c "p=open(r'output/2026-05-29/Henkel - Trade & Shopper Marketing Manager - GCC/frizz_forecast_deck/deck.html',encoding='utf-8').read(); assert 'CONTACT' in p and '@' in p and '+30% GMV' in p and 'paula.jpg' in p; print('ok')"`
Expected: `ok`

- [ ] **Step 3: Commit**

```bash
git add scripts/_henkel_frizz_forecast_deck.py
git commit -m "feat(henkel): why-paula + contact slides"
```

---

### Task 8: Render HTML → multi-page PDF (Playwright)

**Files:**
- Modify: `scripts/_henkel_frizz_forecast_deck.py` (replace `render_pdf`)

- [ ] **Step 1: Implement `render_pdf`** (mirrors `landing_generator.py:535-544`; uses `page.pdf()` for true multi-page)

```python
def render_pdf(html_path: Path, pdf_path: Path) -> None:
    """HTML -> multi-page PDF (one .slide = one 1280x720 page) via headless Chromium."""
    from playwright.sync_api import sync_playwright

    url = html_path.resolve().as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            page.goto(url, wait_until="networkidle", timeout=60_000)
            page.evaluate("() => document.fonts.ready")
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(300)  # let webfonts paint
            page.emulate_media(media="print")
            page.pdf(
                path=str(pdf_path),
                width="1280px",
                height="720px",
                print_background=True,
                prefer_css_page_size=True,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            )
        finally:
            browser.close()
```

- [ ] **Step 2: Run the full build (no `--html-only`)**

Run: `python scripts/_henkel_frizz_forecast_deck.py`
Expected: prints `HTML: ...`, `DECK PDF: ...`. (The `merge_pdfs` stub still raises `NotImplementedError` AFTER the deck PDF is written — that's fine; the deck PDF is produced first. If the traceback is noisy, it still wrote `DECK PDF`.)

- [ ] **Step 3: Verify the deck PDF has exactly 11 pages**

Run: `python -c "from pypdf import PdfReader; n=len(PdfReader(r'output/2026-05-29/Henkel - Trade & Shopper Marketing Manager - GCC/Deliverable_Paula_Henkel_Frizz-Forecast_Deck.pdf').pages); print('pages=',n); assert n==11"`
Expected: `pages= 11`

If pages ≠ 11: a slide is taller than 720px (content overflow forcing an extra page). Fix by trimming copy / reducing font-size on the offending slide, re-run, re-check. This is the most likely failure mode.

- [ ] **Step 4: Commit**

```bash
git add scripts/_henkel_frizz_forecast_deck.py
git commit -m "feat(henkel): render deck HTML to 11-page PDF via Playwright"
```

---

### Task 9: Merge appendix (pypdf) + finalize `main()`

**Files:**
- Modify: `scripts/_henkel_frizz_forecast_deck.py` (replace `merge_pdfs`)

- [ ] **Step 1: Implement `merge_pdfs`**

```python
def merge_pdfs(deck_pdf: Path, appendix_pdf: Path, out_pdf: Path) -> None:
    """Deck PDF followed by the existing 2-page trade plan as an appendix."""
    from pypdf import PdfWriter

    writer = PdfWriter()
    writer.append(str(deck_pdf))
    if appendix_pdf.exists():
        writer.append(str(appendix_pdf))
    else:
        print(f"WARNING: appendix not found, writing deck only: {appendix_pdf}")
    with open(out_pdf, "wb") as f:
        writer.write(f)
```

- [ ] **Step 2: Run the full build end-to-end**

Run: `python scripts/_henkel_frizz_forecast_deck.py`
Expected: prints `HTML:`, `DECK PDF:`, `FULL PDF:` with no traceback.

- [ ] **Step 3: Verify the FULL PDF = 13 pages (11 deck + 2 appendix)**

Run: `python -c "from pypdf import PdfReader; n=len(PdfReader(r'output/2026-05-29/Henkel - Trade & Shopper Marketing Manager - GCC/Deliverable_Paula_Henkel_Frizz-Forecast_FULL.pdf').pages); print('pages=',n); assert n==13"`
Expected: `pages= 13`

- [ ] **Step 4: Commit**

```bash
git add scripts/_henkel_frizz_forecast_deck.py
git commit -m "feat(henkel): merge trade-plan appendix into final Frizz Forecast PDF"
```

---

### Task 10: Visual QA pass + polish

**Files:**
- Modify: `scripts/_henkel_frizz_forecast_deck.py` (CSS/copy tweaks as needed)

- [ ] **Step 1: Render each page to PNG for eyeballing**

Run:
```bash
python -c "from pypdf import PdfReader; print('FULL pages:', len(PdfReader(r'output/2026-05-29/Henkel - Trade & Shopper Marketing Manager - GCC/Deliverable_Paula_Henkel_Frizz-Forecast_FULL.pdf').pages))"
```
Then open `Deliverable_Paula_Henkel_Frizz-Forecast_FULL.pdf` and visually inspect (or use the Read tool on the PDF pages). Read the deck PDF pages with the Read tool (`pages: "1-11"`).

- [ ] **Step 2: Check the QA list and fix inline**

Verify and fix any of:
- No text clipped at slide edges; no slide overflowed to a 12th page (Task 8 already gates page count, but confirm visually no near-edge clipping).
- Cover: title legible over `hero.jpg`; gradient keeps text readable.
- Big-idea (slide 04): the FRIZZ INDEX card, bottle, shelf strip and red talker sit cleanly (no overlap with the lockup text).
- Channel cards (slide 06): all 5 images load, captions don't overflow the card.
- Tables (07–09): columns readable, header bar full black, `<b>` accents red.
- Why Paula (slide 10): photo not stretched; quote + bullets clear of the photo edge.
- Contact (slide 11): email/phone/LinkedIn from `settings` (not literal `P['email']`).
Re-run `python scripts/_henkel_frizz_forecast_deck.py` after each tweak; re-confirm 13 pages.

- [ ] **Step 3: Final commit**

```bash
git add scripts/_henkel_frizz_forecast_deck.py
git commit -m "polish(henkel): visual QA pass on Frizz Forecast deck"
```

---

## Self-Review

**1. Spec coverage:**
- Visual system (palette/fonts/assets) → Task 2 CSS + Task 1 staging. ✓
- 11 slides with exact copy → Tasks 3–7 (cover, agenda, insight, big idea, how, channels, perfect store, calendar, KPIs, why-paula, contact). ✓
- HTML→PDF headless print + gotchas (fonts.ready, eager images, static/no-reveal, print bg) → Task 8 (`loading="eager"` in builders; no reveal CSS anywhere; `document.fonts.ready`; `print_background=True`). ✓
- Merge appendix, 13 pages, output filenames/location → Task 9. ✓
- Profile from settings, nothing hardcoded → Task 7 + Task 1 (`P = settings.profile["personal"]`). ✓
- Nothing sent / draft only / no image regen / don't alter existing trade-plan PDF → no send code anywhere; appendix opened read-only. ✓

**2. Placeholder scan:** "Distribution +X pts" is intentional (spec open-questions note — reads as a plan template). No TBD/TODO/"handle edge cases". All code steps show full code. ✓

**3. Type/name consistency:** `build_html` calls the 11 `slide_*()` names defined as stubs in Task 2 and replaced 1:1 in Tasks 3–7. `render_pdf(html_path, pdf_path)` and `merge_pdfs(deck_pdf, appendix_pdf, out_pdf)` signatures match `main()`'s calls. `_table(headers, rows)` used only in Task 6. Path constants (`HTML_PATH`, `DECK_PDF`, `FULL_PDF`, `APPENDIX_PDF`, `BUILD_ASSETS`) defined in Task 1 and reused verbatim. ✓
