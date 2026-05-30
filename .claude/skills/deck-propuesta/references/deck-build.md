# Building & rendering the deck

The reusable build core behind the deck. The canonical, working implementation is
[scripts/_henkel_frizz_forecast_deck.py](../../../scripts/_henkel_frizz_forecast_deck.py) — read it
alongside this file; everything below is extracted from that worked example so it stays in sync.

Build a **one-off script** per company (`scripts/_<company>_<concept>_deck.py`), don't try to
parameterise a single generic builder — each deck's copy is bespoke. Copy the Henkel script and
swap the brand tokens, slide copy, and image set.

## The shape

- One self-contained Python script. It writes a `deck.html`, renders it to a multi-page PDF with
  headless Chromium (one `.slide` = one 1280×720 page), then merges the trade-plan PDF after it.
- It runs **off the candidate's `settings`** for contact/profile (`settings.profile["personal"]`),
  never hardcoded. Everything else (palette, copy, images) is per-build.
- Paths point into the existing job folder: `output/<date>/<Company - Role>/`. Assets are staged
  into a `<concept>_deck/assets/` subdir; outputs are `Deliverable_Paula_<Company>_<Concept>_Deck.pdf`
  and `..._FULL.pdf`.

## 1 · Brand-token CSS system

One `CSS` string is the whole design system — a flat set of tokens you re-skin per brand. The
Henkel build uses a Schwarzkopf-red accent (`#C41E3A`), near-black ink (`#0a0a0a`), an `Archivo`
black display face + `Inter` body, loaded from Google Fonts. To re-skin: change the accent hex
(it appears in `.red`, `.eyebrow`, bullets, table `<b>`, `.pagenum`, the key-visual), the two font
families, and nothing structural.

Non-negotiable rules baked into the CSS, all required for correct **print** rendering:

```css
*{ -webkit-print-color-adjust:exact; print-color-adjust:exact }   /* keep backgrounds/colours in PDF */
@page{ size:1280px 720px; margin:0 }                              /* 16:9 page, no chrome */
.slide{ width:1280px; height:720px; overflow:hidden; page-break-after:always }
.slide:last-child{ page-break-after:auto }                        /* no trailing blank page */
```

The reusable layout primitives (reuse these names across builds):

- `.slide` / `.slide.dark` — a page; `.dark` flips to the near-black background.
- `.pad` — `position:absolute; inset:0; padding:74px 88px` — the standard content frame.
- `.eyebrow` / `.kicker` — the small uppercase section labels (accent / grey).
- `.h2` (+ `.on-dark`) — the big slide headline.
- `.lead` (+ `.on-dark`) — body paragraph.
- `ul.bullets` — bulleted list with accent-dot markers (`li b` highlights).
- `table.ps` — the Perfect-Store/calendar/KPI table (see `_table` below).
- `.pagenum` — the big accent page number bottom-right.

Slide-specific blocks (`.cover-*`, `.agenda-*`, `.bigidea`/`.kv*`, `.flow`/`.two`, `.cards5`/`.cc`,
`.why-*`, `.contact-*`) live in the same CSS string, grouped by comment. Keep that grouping.

## 2 · Slide-builder pattern

Each slide is a pure function returning an HTML `<section class="slide">…</section>` string. The
document is assembled by joining them, then wrapping in `html_doc()`:

```python
def html_doc(slides: str) -> str:
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{slides}</body></html>"""

def build_html() -> str:
    return html_doc("\n".join([
        slide_cover(), slide_agenda(), slide_insight(), slide_big_idea(),
        slide_how(), slide_channels(), slide_perfect_store(), slide_calendar(),
        slide_kpis(), slide_why_paula(), slide_contact(),
    ]))
```

Why functions, not a template engine: each slide's copy is bespoke and the layouts differ enough
that a loop would obscure more than it saves. One function per slide keeps each one independently
editable and easy to screenshot-review in QA.

**Image rule:** every `<img>` is `loading="eager"` and assets are referenced by *relative* path
(`assets/hero.jpg`) so headless Chromium fetches them from the local `deck.html` location. Lazy
images never fetch off-viewport in print and render blank — see the landing-to-pdf skill for the
same gotcha.

## 3 · The `_table` helper

All three data tables (Perfect Store, 90-day calendar, KPIs) share one builder. Cells accept raw
HTML so you can bold the accent (`<b>…</b>` → accent colour via `table.ps b`):

```python
def _table(headers: list[str], rows: list[list[str]]) -> str:
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="ps"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'
```

Mark the concept's **hero KPI** by wrapping it in `<b>` in the KPI table so it renders in the
accent colour — that's the one visual cue tying the data back to the big idea.

## 4 · Stage assets

Copy the channel images (reused from the campaign-landing's `assets/`) and Paula's photo into the
build dir before rendering, so all `src` paths resolve locally:

```python
CHANNEL_IMAGES = ["hero", "creator", "instore", "pharmacy", "marketplace", "qcommerce", "retailmedia"]

def stage_assets() -> None:
    BUILD_ASSETS.mkdir(parents=True, exist_ok=True)
    for name in CHANNEL_IMAGES:
        shutil.copyfile(LANDING_ASSETS / f"{name}.jpg", BUILD_ASSETS / f"{name}.jpg")
    shutil.copyfile(PAULA_PHOTO, BUILD_ASSETS / "paula.jpg")
```

## 5 · Render HTML → multi-page PDF (Playwright + headless Chromium)

`page.pdf()` paginates on the `.slide` page-breaks. The order of the waits matters — fonts must be
ready and the network idle *before* printing, or the first slide renders in a fallback face:

```python
def render_pdf(html_path: Path, pdf_path: Path) -> None:
    from playwright.sync_api import sync_playwright
    url = html_path.resolve().as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            page.goto(url, wait_until="networkidle", timeout=60_000)
            page.evaluate("() => document.fonts.ready")
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(300)              # let webfonts paint
            page.emulate_media(media="print")       # honour @page + print-color-adjust
            page.pdf(
                path=str(pdf_path), width="1280px", height="720px",
                print_background=True, prefer_css_page_size=True,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            )
        finally:
            browser.close()
```

`prefer_css_page_size=True` makes Chromium honour the `@page{size:1280px 720px}` so every slide is
exactly one page. If Chromium isn't installed, `playwright install chromium` runs once (trigger it
transparently — never hand Paula a command).

## 6 · Merge the trade plan as an appendix (pypdf)

The headline attachment is `FULL` = deck followed by the existing 2-page trade-plan PDF:

```python
def merge_pdfs(deck_pdf: Path, appendix_pdf: Path, out_pdf: Path) -> None:
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

The `main()` wires it together: `stage_assets()` → write `deck.html` → `render_pdf` (DECK) →
`merge_pdfs` (FULL). Keep a `--html-only` flag to write the HTML and stop for fast iteration.

## 7 · Visual QA screenshot snippet (do not skip)

Page-count checks pass even when a slide is visually broken. Screenshot every slide as PNG and
**look at each one** (the controller has vision — review the PNGs directly):

```python
def screenshot_slides(html_path: Path, out_dir: Path) -> None:
    from playwright.sync_api import sync_playwright
    out_dir.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page(viewport={"width": 1280, "height": 720})
            page.goto(html_path.resolve().as_uri(), wait_until="networkidle", timeout=60_000)
            page.evaluate("() => document.fonts.ready")
            for i, el in enumerate(page.query_selector_all(".slide"), 1):
                el.screenshot(path=str(out_dir / f"slide_{i:02d}.png"))
        finally:
            browser.close()
```

Most common failures, in order:
1. Absolutely-positioned key-visual elements (`.kv-*` on the big-idea slide) overlapping body text.
2. A slide taller than 720px silently splitting into an extra page — check `FULL` page count =
   slides + appendix pages.
3. Caption overflow on the 5 channel cards (`.cc p`).

Fix in the builder/CSS and re-render until every PNG is clean.

## Verify

- `DECK` PDF page count == number of `slide_*()` functions (11 for the Henkel spine).
- `FULL` PDF page count == deck slides + trade-plan appendix pages.
- Open the PNGs: no overlap, no split slides, no caption clipping, fonts loaded (not Times fallback).
