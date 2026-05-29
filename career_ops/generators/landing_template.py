"""Static templates for the landing-page deliverable.

Rebuilt 2026-05-19 against the structured-pitch redesign. The previous
"editorial silence" attempt (≤120 words across 8 blocks) was too sparse —
readers couldn't see the proposal. New shape follows the validated
``output/landings/landing_gloria-jeans/`` reference: a 9-section pitch
deck with diagnosis → thesis → 3-phase plan → measurement, capped at
~600 words. Strong typography, generous whitespace, editorial register,
but with a real chapter index in the hero and named phases the reader
can scan in 30 seconds.

Public API:

    render(content: dict, brand: dict, *, landing_dir: Path | None = None)
        -> dict[str, str]

returning ``{"index.html": ..., "styles.css": ..., "scroll.js": ...}``.

Image discovery: when ``landing_dir`` is supplied, render checks
``landing_dir/assets/`` for files named ``hero/dip1/dip2/man/bleed/tri1/
tri2/tri3.{png,jpg}`` (kept the slot names stable so the existing
Higgsfield assets carry over).
"""
from __future__ import annotations

from html import escape as _html_escape
from pathlib import Path


# ───────────────────────────────────────────────────────────────────────────
# HTML — outer document + named section templates
# ───────────────────────────────────────────────────────────────────────────

HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="theme-color" content="{primary}">
  <title>For {company} — {candidate_name}</title>
  <meta name="description" content="A proposal for {company}, by {candidate_name}.">
  <meta name="robots" content="noindex, nofollow">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Italiana&family=Geist:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
{hero_block}
{diagnosis_block}
{thesis_block}
{plan_block}
{proof_block}
{win_block}
{closing_block}
  <script src="scroll.js"></script>
</body>
</html>
"""

HERO_TEMPLATE = """  <section class="b-hero {hero_state}" data-reveal>
    {hero_media}
    <div class="b-hero__inner">
      <p class="b-hero__support">{support}</p>
      <h1 class="b-hero__headline">{headline_html}</h1>
      <div class="b-hero__index">
        <span class="b-hero__index-label">In this proposal</span>
        <ol class="b-hero__index-list">
          {index_items}
        </ol>
      </div>
      <p class="b-hero__author">
        <span>{candidate_name}</span>
        <span aria-hidden="true">·</span>
        <span>Dubai</span>
      </p>
    </div>
  </section>
"""

HERO_INDEX_ITEM = '<li><span class="b-hero__index-num">{num}</span>{label}</li>'

DIAGNOSIS_TEMPLATE = """  <section class="b-diagnosis" data-reveal>
    <div class="b-diagnosis__inner">
      <div class="b-diagnosis__text">
        <p class="b-section-eyebrow">{eyebrow}</p>
        <h2 class="b-diagnosis__heading">{heading}</h2>
        <div class="b-diagnosis__body">
          {body_html}
        </div>
      </div>
      <figure class="b-diagnosis__figure">{media}</figure>
    </div>
  </section>
"""

THESIS_TEMPLATE = """  <section class="b-thesis" data-reveal>
    <div class="b-thesis__inner">
      <p class="b-section-eyebrow b-section-eyebrow--accent">{eyebrow}</p>
      <h2 class="b-thesis__headline">{headline}</h2>
      <div class="b-thesis__body">
        {body_html}
      </div>
    </div>
  </section>
"""

PLAN_TEMPLATE = """  <section class="b-plan" data-reveal>
    <div class="b-plan__inner">
      <header class="b-plan__header">
        <p class="b-section-eyebrow">{eyebrow}</p>
        <h2 class="b-plan__headline">{headline}</h2>
        <p class="b-plan__lede">{lede}</p>
      </header>
      <ol class="b-plan__phases">
        {phases_html}
      </ol>
    </div>
  </section>
"""

PLAN_PHASE_TEMPLATE = """        <li class="b-plan__phase">
          <div class="b-plan__phase-marker">
            <span class="b-plan__phase-num">{num}</span>
            <span class="b-plan__phase-span">{span}</span>
          </div>
          <div class="b-plan__phase-body">
            <h3 class="b-plan__phase-name">{name}</h3>
            <p class="b-plan__phase-text">{body}</p>
          </div>
        </li>"""

PROOF_TEMPLATE = """  <section class="b-proof" data-reveal>
    <div class="b-proof__inner">
      <header class="b-proof__header">
        <p class="b-section-eyebrow">{eyebrow}</p>
        <h2 class="b-proof__headline">{headline}</h2>
      </header>
      <ul class="b-proof__stats">
        {stats_html}
      </ul>
    </div>
  </section>
"""

PROOF_STAT_TEMPLATE = """      <li class="b-proof__stat">
        <span class="b-proof__num">{number}</span>
        <span class="b-proof__label">{label}</span>
        {sublabel_html}
      </li>"""

WIN_TEMPLATE = """  <section class="b-win" data-reveal>
    {win_media}
    <div class="b-win__inner">
      <p class="b-section-eyebrow b-section-eyebrow--inverted">{eyebrow}</p>
      <h2 class="b-win__headline">{headline}</h2>
      <ul class="b-win__metrics">
        {metrics_html}
      </ul>
    </div>
  </section>
"""

WIN_METRIC_TEMPLATE = '      <li class="b-win__metric"><span class="b-win__metric-num">{num}</span><span class="b-win__metric-text">{text}</span></li>'

CLOSING_TEMPLATE = """  <section class="b-closing" data-reveal>
    <div class="b-closing__inner">
      <p class="b-closing__paragraph">{paragraph}</p>
      <p class="b-closing__cta">{cta_line}</p>
      <p class="b-closing__contact">
        <a href="mailto:{candidate_email}">{candidate_email}</a>
        <span aria-hidden="true">·</span>
        <a href="tel:{candidate_phone_href}">{candidate_phone}</a>
        <span aria-hidden="true">·</span>
        <a href="{candidate_linkedin_url}" target="_blank" rel="noopener">{candidate_linkedin_display}</a>
      </p>
    </div>
  </section>
"""


# ───────────────────────────────────────────────────────────────────────────
# CSS
# ───────────────────────────────────────────────────────────────────────────

CSS_TEMPLATE = """/* Auto-generated landing — {company} × {candidate_name}
   Editorial pitch register. See .impeccable.md "Landings".
*/

:root {{
  --ink:        {ink};
  --paper:      {paper};
  --paper-deep: {paper_deep};
  --accent:     {accent};
  --muted:      {muted};

  --font-display: "Italiana", "Bodoni Moda", "Times New Roman", serif;
  --font-body:    "Geist", system-ui, -apple-system, "Helvetica Neue", sans-serif;

  --space-2xs: 4px;
  --space-xs:  8px;
  --space-sm:  12px;
  --space-md:  16px;
  --space-lg:  24px;
  --space-xl:  32px;
  --space-2xl: 48px;
  --space-3xl: 64px;
  --space-4xl: 96px;
  --space-5xl: 128px;

  --beat-wide:   clamp(96px, 12vw, 192px);
  --beat-narrow: clamp(48px, 7vw, 96px);
  --frame: clamp(24px, 5vw, 80px);
  --grid-max: 1280px;
}}

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }}
body {{
  font-family: var(--font-body);
  font-weight: 400;
  color: var(--ink);
  background: var(--paper);
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
  font-feature-settings: "kern" 1, "liga" 1, "ss01" 1;
}}
img {{ max-width: 100%; display: block; }}
a {{ color: inherit; text-decoration: none; }}
ol, ul {{ list-style: none; padding: 0; }}

::selection {{
  background: color-mix(in oklch, var(--accent) 70%, transparent);
  color: var(--paper);
}}

[data-reveal] {{
  opacity: 0;
  transform: translateY(12px);
  transition:
    opacity 600ms cubic-bezier(0.2, 0.9, 0.3, 1),
    transform 600ms cubic-bezier(0.2, 0.9, 0.3, 1);
}}
[data-reveal].is-visible {{ opacity: 1; transform: none; }}
@media (prefers-reduced-motion: reduce) {{
  [data-reveal], [data-reveal].is-visible {{
    opacity: 1; transform: none; transition: none;
  }}
}}

.b-section-eyebrow {{
  font-family: var(--font-body);
  font-size: 11px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  font-weight: 500;
  color: var(--muted);
  margin-bottom: var(--space-lg);
}}
.b-section-eyebrow--accent {{ color: var(--accent); font-weight: 600; }}
.b-section-eyebrow--inverted {{ color: color-mix(in oklch, var(--paper) 70%, var(--ink)); }}

/* ── Block 1 — HERO ─────────────────────────────────────────────────── */
.b-hero {{
  position: relative;
  min-height: clamp(640px, 92vh, 960px);
  display: flex;
  align-items: flex-end;
  padding: var(--space-4xl) var(--frame) var(--space-3xl);
  background: var(--paper-deep);
  overflow: hidden;
  color: var(--paper);
}}
.b-hero.has-paper {{
  background: var(--paper-deep);
  color: var(--ink);
  align-items: center;
}}
.b-hero__media {{ position: absolute; inset: 0; z-index: 0; }}
.b-hero__media img {{
  width: 100%; height: 100%;
  object-fit: cover; object-position: center;
}}
.b-hero__media::after {{
  content: "";
  position: absolute; inset: 0;
  background: linear-gradient(
    180deg,
    color-mix(in oklch, var(--ink) 8%, transparent) 0%,
    color-mix(in oklch, var(--ink) 40%, transparent) 55%,
    color-mix(in oklch, var(--ink) 80%, transparent) 100%
  );
}}
.b-hero__inner {{
  position: relative; z-index: 1;
  width: 100%;
  max-width: var(--grid-max);
  margin: 0 auto;
  display: grid;
  grid-template-columns: minmax(0, 7fr) minmax(0, 5fr);
  align-items: end;
  gap: var(--space-2xl);
}}
.b-hero__support {{
  grid-column: 1 / 2;
  font-size: 11px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  font-weight: 500;
  margin-bottom: var(--space-md);
  opacity: 0.85;
}}
.b-hero__headline {{
  grid-column: 1 / 2;
  font-family: var(--font-display);
  font-weight: 400;
  font-size: clamp(48px, 8vw, 128px);
  line-height: 0.96;
  letter-spacing: -0.01em;
  margin: 0 0 var(--space-2xl) 0;
}}
.b-hero__line {{ display: block; }}
.b-hero__index {{
  grid-column: 2 / 3;
  align-self: end;
  background: color-mix(in oklch, var(--paper) 8%, transparent);
  backdrop-filter: blur(6px);
  padding: var(--space-lg) var(--space-xl);
  border-left: 1px solid color-mix(in oklch, var(--paper) 30%, transparent);
}}
.b-hero__index-label {{
  font-size: 10px;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  font-weight: 600;
  margin-bottom: var(--space-md);
  opacity: 0.7;
}}
.b-hero__index-list li {{
  font-family: var(--font-display);
  font-size: clamp(16px, 1.5vw, 20px);
  line-height: 1.4;
  padding: var(--space-xs) 0;
  display: flex;
  gap: var(--space-md);
  align-items: baseline;
}}
.b-hero__index-num {{
  font-family: var(--font-body);
  font-size: 10px;
  letter-spacing: 0.2em;
  font-weight: 600;
  opacity: 0.6;
  min-width: 22px;
}}
.b-hero__author {{
  grid-column: 1 / -1;
  margin-top: var(--space-xl);
  padding-top: var(--space-lg);
  border-top: 1px solid color-mix(in oklch, var(--paper) 30%, transparent);
  font-size: 11px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  font-weight: 500;
  opacity: 0.85;
  display: flex;
  gap: var(--space-xs);
  align-items: baseline;
}}

/* ── Block 2 — DIAGNOSIS ────────────────────────────────────────────── */
.b-diagnosis {{
  background: var(--paper);
  padding: var(--beat-wide) var(--frame);
}}
.b-diagnosis__inner {{
  max-width: var(--grid-max);
  margin: 0 auto;
  display: grid;
  grid-template-columns: minmax(0, 6fr) minmax(0, 5fr);
  gap: clamp(32px, 5vw, 96px);
  align-items: start;
}}
.b-diagnosis__heading {{
  font-family: var(--font-display);
  font-weight: 400;
  font-size: clamp(36px, 4.5vw, 64px);
  line-height: 1.05;
  letter-spacing: -0.01em;
  margin-bottom: var(--space-xl);
}}
.b-diagnosis__body p {{
  font-size: clamp(16px, 1.3vw, 18px);
  line-height: 1.7;
  margin-bottom: var(--space-md);
  max-width: 56ch;
}}
.b-diagnosis__body p:last-child {{ margin-bottom: 0; }}
.b-diagnosis__figure {{
  margin: 0;
  background: var(--paper-deep);
  aspect-ratio: 4 / 5;
  overflow: hidden;
}}
.b-diagnosis__figure img {{
  width: 100%; height: 100%;
  object-fit: cover; object-position: center;
}}

/* ── Block 3 — THESIS ───────────────────────────────────────────────── */
.b-thesis {{
  background: var(--paper-deep);
  padding: var(--beat-wide) var(--frame);
}}
.b-thesis__inner {{
  max-width: var(--grid-max);
  margin: 0 auto;
  padding-left: clamp(0px, 8vw, 120px);
}}
.b-thesis__headline {{
  font-family: var(--font-display);
  font-style: italic;
  font-weight: 400;
  font-size: clamp(40px, 5.5vw, 88px);
  line-height: 1.05;
  letter-spacing: -0.005em;
  margin-bottom: var(--space-2xl);
  max-width: 18ch;
}}
.b-thesis__body p {{
  font-size: clamp(17px, 1.4vw, 19px);
  line-height: 1.65;
  max-width: 56ch;
  margin-bottom: var(--space-md);
}}
.b-thesis__body p:last-child {{ margin-bottom: 0; }}

/* ── Block 4 — PLAN (the spine) ─────────────────────────────────────── */
.b-plan {{
  background: var(--paper);
  padding: var(--beat-wide) var(--frame);
}}
.b-plan__inner {{
  max-width: var(--grid-max);
  margin: 0 auto;
}}
.b-plan__header {{
  margin-bottom: var(--space-4xl);
  max-width: 760px;
}}
.b-plan__headline {{
  font-family: var(--font-display);
  font-weight: 400;
  font-size: clamp(40px, 5.5vw, 80px);
  line-height: 1.05;
  letter-spacing: -0.01em;
  margin-bottom: var(--space-lg);
}}
.b-plan__lede {{
  font-size: clamp(17px, 1.4vw, 20px);
  line-height: 1.6;
  color: var(--muted);
  max-width: 56ch;
}}
.b-plan__phases {{
  display: grid;
  gap: var(--space-3xl);
}}
.b-plan__phase {{
  display: grid;
  grid-template-columns: minmax(0, 3fr) minmax(0, 8fr);
  gap: clamp(24px, 4vw, 64px);
  padding-top: var(--space-xl);
  border-top: 1px solid color-mix(in oklch, var(--ink) 14%, transparent);
}}
.b-plan__phase-marker {{
  display: flex;
  flex-direction: column;
  gap: var(--space-xs);
}}
.b-plan__phase-num {{
  font-family: var(--font-display);
  font-size: clamp(48px, 6vw, 96px);
  line-height: 0.9;
  color: var(--accent);
  font-weight: 400;
}}
.b-plan__phase-span {{
  font-size: 11px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  font-weight: 600;
  color: var(--muted);
}}
.b-plan__phase-name {{
  font-family: var(--font-display);
  font-weight: 400;
  font-size: clamp(28px, 3.2vw, 44px);
  line-height: 1.1;
  margin-bottom: var(--space-md);
  letter-spacing: -0.005em;
}}
.b-plan__phase-text {{
  font-size: clamp(16px, 1.3vw, 18px);
  line-height: 1.65;
  max-width: 56ch;
}}

/* ── Block 5 — PROOF (stats) ────────────────────────────────────────── */
.b-proof {{
  background: var(--paper-deep);
  padding: var(--beat-wide) var(--frame);
}}
.b-proof__inner {{
  max-width: var(--grid-max);
  margin: 0 auto;
}}
.b-proof__header {{
  margin-bottom: var(--space-3xl);
  max-width: 760px;
}}
.b-proof__headline {{
  font-family: var(--font-display);
  font-weight: 400;
  font-size: clamp(36px, 4.5vw, 64px);
  line-height: 1.05;
  letter-spacing: -0.005em;
}}
.b-proof__stats {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-xl);
}}
.b-proof__stat {{
  display: flex;
  flex-direction: column;
  gap: var(--space-sm);
  padding-top: var(--space-lg);
  border-top: 1px solid color-mix(in oklch, var(--ink) 14%, transparent);
}}
.b-proof__num {{
  font-family: var(--font-display);
  font-size: clamp(48px, 6vw, 88px);
  line-height: 0.9;
  letter-spacing: -0.02em;
  color: var(--accent);
}}
.b-proof__label {{
  font-size: 13px;
  font-weight: 600;
  color: var(--ink);
  text-transform: none;
}}
.b-proof__sublabel {{
  font-size: 12px;
  color: var(--muted);
  line-height: 1.5;
}}

/* ── Block 6 — WIN (what success looks like) ────────────────────────── */
.b-win {{
  position: relative;
  background: var(--ink);
  color: var(--paper);
  padding: var(--beat-wide) var(--frame);
  overflow: hidden;
}}
.b-win__media {{ position: absolute; inset: 0; z-index: 0; opacity: 0.35; }}
.b-win__media img {{
  width: 100%; height: 100%;
  object-fit: cover; object-position: center;
}}
.b-win__inner {{
  position: relative; z-index: 1;
  max-width: var(--grid-max);
  margin: 0 auto;
}}
.b-win__headline {{
  font-family: var(--font-display);
  font-weight: 400;
  font-size: clamp(40px, 5.5vw, 80px);
  line-height: 1.05;
  letter-spacing: -0.01em;
  margin-bottom: var(--space-2xl);
  max-width: 18ch;
}}
.b-win__metrics {{
  display: grid;
  gap: var(--space-lg);
  max-width: 720px;
}}
.b-win__metric {{
  display: flex;
  align-items: baseline;
  gap: var(--space-lg);
  padding: var(--space-md) 0;
  border-top: 1px solid color-mix(in oklch, var(--paper) 20%, transparent);
}}
.b-win__metric-num {{
  font-family: var(--font-display);
  font-size: clamp(28px, 3.2vw, 40px);
  line-height: 1;
  color: var(--accent);
  min-width: 96px;
}}
.b-win__metric-text {{
  font-size: clamp(15px, 1.2vw, 17px);
  line-height: 1.55;
}}

/* ── Block 7 — CLOSING ──────────────────────────────────────────────── */
.b-closing {{
  background: var(--paper);
  color: var(--ink);
  padding: var(--beat-wide) var(--frame);
}}
.b-closing__inner {{
  max-width: 720px;
  margin: 0 auto;
}}
.b-closing__paragraph {{
  font-family: var(--font-body);
  font-size: clamp(17px, 1.4vw, 20px);
  line-height: 1.6;
  font-weight: 400;
}}
.b-closing__cta {{
  margin-top: var(--space-2xl);
  font-family: var(--font-display);
  font-style: italic;
  font-weight: 400;
  font-size: clamp(28px, 3.6vw, 48px);
  line-height: 1.1;
}}
.b-closing__contact {{
  margin-top: var(--space-3xl);
  padding-top: var(--space-xl);
  border-top: 1px solid color-mix(in oklch, var(--ink) 18%, transparent);
  font-size: 11px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  font-weight: 500;
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-sm);
  color: var(--muted);
}}
.b-closing__contact a {{
  transition: color 200ms cubic-bezier(0.2, 0.9, 0.3, 1);
}}
.b-closing__contact a:hover,
.b-closing__contact a:focus-visible {{
  color: var(--accent);
}}
.b-closing__contact a:focus-visible {{
  outline: 1px solid var(--accent);
  outline-offset: 4px;
}}

/* ── Mobile ─────────────────────────────────────────────────────────── */
@media (max-width: 880px) {{
  .b-hero__inner {{
    grid-template-columns: 1fr;
    gap: var(--space-xl);
  }}
  .b-hero__index {{
    grid-column: 1 / -1;
    border-left: none;
    border-top: 1px solid color-mix(in oklch, var(--paper) 30%, transparent);
    padding: var(--space-lg) 0 0 0;
    background: transparent;
    backdrop-filter: none;
  }}
  .b-diagnosis__inner {{
    grid-template-columns: 1fr;
    gap: var(--space-2xl);
  }}
  .b-thesis__inner {{
    padding-left: 0;
  }}
  .b-plan__phase {{
    grid-template-columns: 1fr;
    gap: var(--space-md);
  }}
  .b-proof__stats {{
    grid-template-columns: 1fr;
  }}
  .b-win__metric {{
    flex-direction: column;
    gap: var(--space-xs);
  }}
  .b-win__metric-num {{ min-width: 0; }}
}}
"""


# ───────────────────────────────────────────────────────────────────────────
# JavaScript — IntersectionObserver reveal only
# ───────────────────────────────────────────────────────────────────────────

JS_TEMPLATE = """(function () {
  'use strict';
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var reveals = document.querySelectorAll('[data-reveal]');

  if (reveals.length && 'IntersectionObserver' in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-visible'); });
  }
})();
"""


# ───────────────────────────────────────────────────────────────────────────
# Render helpers
# ───────────────────────────────────────────────────────────────────────────

_IMAGE_SLOTS = ("hero", "dip1", "dip2", "man", "bleed", "tri1", "tri2", "tri3")


def _available_images(landing_dir: Path | None) -> set[str]:
    if landing_dir is None:
        return set()
    assets = Path(landing_dir) / "assets"
    if not assets.is_dir():
        return set()
    return {f.name for f in assets.iterdir() if f.is_file()}


def _img_for(slot: str, available: set[str], alt: str = "") -> str:
    """<img> tag for the slot if a file exists, otherwise empty string."""
    for ext in ("png", "jpg"):
        name = f"{slot}.{ext}"
        if name in available:
            return f'<img src="assets/{name}" alt="{_html_escape(alt)}" loading="lazy">'
    return ""


def _hero_media(available: set[str]) -> tuple[str, str]:
    img = _img_for("hero", available, alt="")
    if img:
        return "has-image", f'<div class="b-hero__media">{img}</div>'
    return "has-paper", ""


def _win_media(available: set[str]) -> str:
    img = _img_for("bleed", available, alt="")
    if img:
        return f'<div class="b-win__media">{img}</div>'
    return ""


def _split_headline(headline: str) -> str:
    """Render the headline as one or two staggered lines."""
    escaped = _html_escape(headline)
    words = escaped.split(" ")
    if len(words) <= 3:
        return f'<span class="b-hero__line">{escaped}</span>'
    midpoint = max(1, (len(words) + 1) // 2)
    line_1 = " ".join(words[:midpoint])
    line_2 = " ".join(words[midpoint:])
    return (
        f'<span class="b-hero__line">{line_1}</span>'
        f'<span class="b-hero__line">{line_2}</span>'
    )


def _phone_href(phone: str) -> str:
    return "".join(ch for ch in phone if ch.isdigit() or ch == "+")


def _linkedin_parts(linkedin: str) -> tuple[str, str]:
    raw = (linkedin or "").strip()
    if not raw:
        return ("", "")
    display = raw
    for prefix in ("https://", "http://"):
        if display.startswith(prefix):
            display = display[len(prefix):]
            break
    display = display.rstrip("/")
    return ("https://" + display, display)


def _paragraphs_to_html(paragraphs: list[str]) -> str:
    return "\n        ".join(f"<p>{_html_escape(p)}</p>" for p in paragraphs)


# ───────────────────────────────────────────────────────────────────────────
# Block renderers
# ───────────────────────────────────────────────────────────────────────────

def _render_hero(content: dict, available: set[str]) -> str:
    hero = content.get("hero", {})
    state, media = _hero_media(available)
    chapters = hero.get("chapters", []) or []
    index_items = []
    for i, ch in enumerate(chapters, start=1):
        index_items.append(HERO_INDEX_ITEM.format(
            num=f"{i:02d}",
            label=_html_escape(ch),
        ))
    return HERO_TEMPLATE.format(
        hero_state=state,
        hero_media=media,
        support=_html_escape(hero.get("support", "")),
        headline_html=_split_headline(hero.get("headline", "")),
        index_items="\n          ".join(index_items),
        candidate_name=_html_escape(content.get("candidate_name", "")),
    )


def _render_diagnosis(content: dict, available: set[str]) -> str:
    d = content.get("diagnosis", {})
    paragraphs = d.get("body_paragraphs", []) or []
    return DIAGNOSIS_TEMPLATE.format(
        eyebrow=_html_escape(d.get("eyebrow", "")),
        heading=_html_escape(d.get("heading", "")),
        body_html=_paragraphs_to_html(paragraphs),
        media=_img_for("man", available),
    )


def _render_thesis(content: dict) -> str:
    t = content.get("thesis", {})
    paragraphs = t.get("body_paragraphs", []) or []
    return THESIS_TEMPLATE.format(
        eyebrow=_html_escape(t.get("eyebrow", "")),
        headline=_html_escape(t.get("headline", "")),
        body_html=_paragraphs_to_html(paragraphs),
    )


def _render_plan(content: dict) -> str:
    plan = content.get("plan", {})
    phases = plan.get("phases", []) or []
    phases = (list(phases) + [{}, {}, {}])[:3]  # pad / truncate to 3
    rendered = []
    for i, ph in enumerate(phases, start=1):
        rendered.append(PLAN_PHASE_TEMPLATE.format(
            num=f"{i:02d}",
            span=_html_escape(ph.get("span", "")),
            name=_html_escape(ph.get("name", "")),
            body=_html_escape(ph.get("body", "")),
        ))
    return PLAN_TEMPLATE.format(
        eyebrow=_html_escape(plan.get("eyebrow", "")),
        headline=_html_escape(plan.get("headline", "")),
        lede=_html_escape(plan.get("lede", "")),
        phases_html="\n        ".join(rendered),
    )


def _render_proof(content: dict) -> str:
    proof = content.get("proof", {})
    stats = proof.get("stats", []) or []
    stats = (list(stats) + [{}, {}, {}])[:3]
    rendered = []
    for s in stats:
        sub = s.get("sublabel")
        sublabel_html = (
            f'<span class="b-proof__sublabel">{_html_escape(sub)}</span>'
            if sub else ""
        )
        rendered.append(PROOF_STAT_TEMPLATE.format(
            number=_html_escape(str(s.get("number", ""))),
            label=_html_escape(s.get("label", "")),
            sublabel_html=sublabel_html,
        ))
    return PROOF_TEMPLATE.format(
        eyebrow=_html_escape(proof.get("eyebrow", "")),
        headline=_html_escape(proof.get("headline", "")),
        stats_html="\n        ".join(rendered),
    )


def _render_win(content: dict, available: set[str]) -> str:
    win = content.get("win", {})
    metrics = win.get("metrics", []) or []
    rendered = []
    for m in metrics:
        rendered.append(WIN_METRIC_TEMPLATE.format(
            num=_html_escape(str(m.get("number", ""))),
            text=_html_escape(m.get("text", "")),
        ))
    return WIN_TEMPLATE.format(
        win_media=_win_media(available),
        eyebrow=_html_escape(win.get("eyebrow", "")),
        headline=_html_escape(win.get("headline", "")),
        metrics_html="\n        ".join(rendered),
    )


def _render_closing(content: dict) -> str:
    c = content.get("closing", {})
    phone = content.get("candidate_phone", "")
    li_url, li_display = _linkedin_parts(content.get("candidate_linkedin", ""))
    return CLOSING_TEMPLATE.format(
        paragraph=_html_escape(c.get("paragraph", "")),
        cta_line=_html_escape(c.get("cta_line", "")),
        candidate_email=_html_escape(content.get("candidate_email", "")),
        candidate_phone=_html_escape(phone),
        candidate_phone_href=_html_escape(_phone_href(phone)),
        candidate_linkedin_url=_html_escape(li_url),
        candidate_linkedin_display=_html_escape(li_display),
    )


# ───────────────────────────────────────────────────────────────────────────
# Public API
# ───────────────────────────────────────────────────────────────────────────

def render(
    content: dict,
    brand: dict,
    *,
    landing_dir: Path | None = None,
) -> dict[str, str]:
    """Return ``{filename: contents}`` for the three landing files.

    ``content`` shape (Claude's tool_use schema is the source of truth):

        {
            "company": str, "candidate_name": str,
            "candidate_email": str, "candidate_phone": str,
            "candidate_linkedin": str,
            "hero": {
                "headline": str (4-8 words),
                "support": str (≤14 words),
                "chapters": list[str] (3-4 short chapter labels for index)
            },
            "diagnosis": {
                "eyebrow": str (e.g. "01 — the gap"),
                "heading": str (≤12 words),
                "body_paragraphs": list[str] (2-3 paragraphs, total ≤80 words)
            },
            "thesis": {
                "eyebrow": str (e.g. "02 — the thesis"),
                "headline": str (≤12 words, italic display),
                "body_paragraphs": list[str] (1-2 paragraphs, ≤60 words)
            },
            "plan": {
                "eyebrow": str (e.g. "03 — the plan"),
                "headline": str (≤8 words, e.g. "Three phases. Six months."),
                "lede": str (≤30 words intro to the plan),
                "phases": [
                    {"span": "Weeks 1-4", "name": str, "body": str (≤45 words)},
                    ... (exactly 3)
                ]
            },
            "proof": {
                "eyebrow": str (e.g. "04 — what I bring"),
                "headline": str (≤12 words),
                "stats": [{"number": str, "label": str, "sublabel": str?}, ...]
            },
            "win": {
                "eyebrow": str (e.g. "05 — what success looks like"),
                "headline": str (≤12 words),
                "metrics": [{"number": str, "text": str}, ...] (2-4 items)
            },
            "closing": {
                "paragraph": str (≤30 words),
                "cta_line": str (≤10 words)
            }
        }
    """
    available = _available_images(landing_dir)

    html = HTML_TEMPLATE.format(
        primary=brand["ink"],
        company=_html_escape(content.get("company", "")),
        candidate_name=_html_escape(content.get("candidate_name", "")),
        hero_block=_render_hero(content, available),
        diagnosis_block=_render_diagnosis(content, available),
        thesis_block=_render_thesis(content),
        plan_block=_render_plan(content),
        proof_block=_render_proof(content),
        win_block=_render_win(content, available),
        closing_block=_render_closing(content),
    )

    css = CSS_TEMPLATE.format(
        ink=brand["ink"],
        paper=brand["paper"],
        paper_deep=brand["paper_deep"],
        accent=brand["accent"],
        muted=brand["muted"],
        company=_html_escape(content.get("company", "")),
        candidate_name=_html_escape(content.get("candidate_name", "")),
    )

    return {
        "index.html": html,
        "styles.css": css,
        "scroll.js": JS_TEMPLATE,
    }
