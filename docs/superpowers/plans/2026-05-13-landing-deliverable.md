# Landing-Page Deliverable Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the ugly docx-to-PDF deliverable for speculative job targets with a navigable HTML+CSS+JS mini-landing per target, generated through Claude tool_use and integrated into the existing dashboard "Generate" flow.

**Architecture:** A new `landing_generator.py` module that (1) asks Claude to fill a structured JSON schema with 6 sections of editorial copy tilted by the job's `positioning_angle`, (2) renders that JSON into a self-contained HTML+CSS+JS bundle inside `output/<Company_Role>/landing/`, cloning the template + reveal/parallax system used by the existing `landing_gloria-jeans/`. The dashboard mounts `output/` as a static directory and adds a `/api/jobs/{id}/landing` endpoint that returns the landing URL. The "Generate" handler branches: speculative jobs call `generate_landing`, non-speculative jobs keep calling the old `generate_deliverable` untouched. Higgsfield image generation is stubbed for now — landings ship with placeholder gradient hero cards keyed off the brand palette and swap to real images once the CLI is wired.

**Tech Stack:** FastAPI, Anthropic SDK (existing `career_ops.llm`), Python 3.12, vanilla HTML/CSS/JS (Space Grotesk + Inter via Google Fonts CDN, IntersectionObserver), pytest.

---

## File Structure

**New files:**
- `career_ops/generators/landing_generator.py` — Claude → JSON → HTML/CSS/JS renderer
- `career_ops/generators/landing_template.py` — HTML/CSS/JS template strings (kept separate so we can iterate copy without touching renderer logic)
- `tests/test_landing_generator.py` — unit tests covering schema validation, file emission, brand palette plumbing
- `tests/__init__.py` — empty, so pytest discovers the tests dir
- `docs/superpowers/plans/2026-05-13-landing-deliverable.md` — this file (already exists)

**Modified files:**
- `career_ops/webapp/api.py` — mount `/output/` as static, add `GET /api/jobs/{id}/landing`, branch `_generate` to call `generate_landing` for speculative jobs
- `career_ops/generators/__init__.py` — re-export `generate_landing`
- `career_ops/webapp/static/index.html` — add "Open landing" link to the speculative-job detail card

**Untouched (intentional):**
- `career_ops/generators/deliverables.py` — kept for non-speculative jobs (AWPRO, CHOITHRAMS already have docx deliverables on disk; we won't churn them)
- `_index_generated_files` in api.py — landings live under `<Company_Role>/landing/`; the file-index logic doesn't need to know, because the new `landing` URL is fetched via a dedicated endpoint, not via the file index

---

## Decomposition rationale

- **Template strings in a sibling module** so editing the HTML/CSS doesn't force a re-read of the generator logic in Claude review.
- **Schema-driven copy** with Claude tool_use mirrors the cv_generator pattern — same `llm.generate_structured` call shape, same retry semantics, zero new infra.
- **Static mount over per-file endpoints** because a landing has 3-4 files (html, css, js, images) and writing one endpoint per filetype is silly.
- **No migration of existing deliverables** — YAGNI: nobody has asked for AWPRO/CHOITHRAMS to become landings.

---

## Task 1: Author the HTML/CSS/JS template module

**Files:**
- Create: `career_ops/generators/landing_template.py`

This file holds three module-level string constants (`HTML_TEMPLATE`, `CSS_TEMPLATE`, `JS_TEMPLATE`) and one function `render(content: dict, brand: dict) -> dict[str, str]` that returns `{filename: contents}` ready to write to disk.

The `content` dict shape is fixed and matches what Claude will produce (defined in Task 2):

```python
{
    "company": "Azadea",
    "role": "Marketing Manager (Speculative)",
    "candidate_name": "Paula De Francisco",
    "candidate_role": "Brand & Marketing Manager · Dubai, UAE",
    "candidate_email": "paulich98@hotmail.com",
    "candidate_phone": "+971 50 386 3656",
    "candidate_linkedin": "linkedin.com/in/paula-de-francisco-perez",
    "tagline": "A strategic proposal for Azadea",
    "hero_headline_line_1": "Orchestrating",
    "hero_headline_line_2": "fifty brands as one.",
    "hero_subtitle": "What if your portfolio behaved like an ecosystem instead of a holding?",
    "sections": [
        {
            "id": "thesis",
            "kicker": "01 — The thesis",
            "heading": "Section heading",
            "body_paragraphs": ["Para 1.", "Para 2."],
            "image_placeholder_label": "Editorial: storefront row, warm dusk light",
        },
        # 5 more sections, schema identical
    ],
    "closing_kicker": "Next step",
    "closing_text": "I'd like 30 minutes to walk you through this.",
}
```

`brand` dict shape (per-job, defined in Task 3):

```python
{
    "primary": "#1A1A1A",        # main text / background ink
    "accent": "#C8A876",         # CTA / accent color
    "surface": "#FAF7F2",        # warm off-white background
    "muted": "#8A8A8A",          # secondary text
    "scheme": "warm-editorial",  # used to pick gradient direction in placeholders
}
```

- [ ] **Step 1.1: Create the file with the HTML template constant**

```python
"""Static templates for the landing-page deliverable.

The render function injects per-job copy and brand palette into these
strings and returns ``{filename: file_contents}`` ready for writing to disk.
The HTML/CSS/JS structure mirrors ``output/landings/landing_gloria-jeans/``
which has been validated as production-quality editorial design (Space
Grotesk + Inter, scroll reveals, parallax-lite hero).
"""
from __future__ import annotations

HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="theme-color" content="{primary}">
  <title>{tagline} — {company}</title>
  <meta name="description" content="{tagline}. Prepared by {candidate_name}.">
  <meta name="robots" content="noindex, nofollow">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <nav class="top-nav">
    <div class="brand-mark">{company_initials}</div>
    <div class="nav-label">{tagline}</div>
  </nav>

  <section class="hero" data-reveal>
    <div class="hero-inner">
      <div class="hero-kicker">{tagline}</div>
      <h1 class="hero-headline">
        {hero_headline_line_1}<br>
        <span class="hero-accent">{hero_headline_line_2}</span>
      </h1>
      <p class="hero-sub">{hero_subtitle}</p>
      <div class="hero-author">
        <div class="author-name">{candidate_name}</div>
        <div class="author-role">{candidate_role}</div>
      </div>
      <div class="hero-scroll-hint" aria-hidden="true">
        <span class="hint-line"></span>
        <span class="hint-text">Scroll to explore</span>
      </div>
    </div>
  </section>

  {sections_html}

  <section class="closing" data-reveal>
    <div class="closing-inner">
      <div class="closing-kicker">{closing_kicker}</div>
      <p class="closing-text">{closing_text}</p>
      <div class="closing-contact">
        <span>{candidate_email}</span>
        <span>·</span>
        <span>{candidate_phone}</span>
        <span>·</span>
        <span>{candidate_linkedin}</span>
      </div>
    </div>
  </section>

  <script src="scroll.js"></script>
</body>
</html>
"""

SECTION_TEMPLATE = """  <section class="section" id="{section_id}" data-reveal>
    <div class="section-inner">
      <div class="section-kicker">{kicker}</div>
      <h2 class="section-heading">{heading}</h2>
      <div class="section-body">
        {body_html}
      </div>
      <figure class="section-figure">
        <div class="figure-placeholder" aria-hidden="true"></div>
        <figcaption>{image_placeholder_label}</figcaption>
      </figure>
    </div>
  </section>
"""
```

- [ ] **Step 1.2: Add the CSS template constant to the same file**

Append to `career_ops/generators/landing_template.py`:

```python
CSS_TEMPLATE = """/* Auto-generated landing — {company} × {candidate_name} */
:root {{
  --ink: {primary};
  --accent: {accent};
  --surface: {surface};
  --muted: {muted};
  --border: rgba(0,0,0,0.08);

  --font-display: "Space Grotesk", system-ui, -apple-system, sans-serif;
  --font-body: "Inter", system-ui, -apple-system, sans-serif;

  --space-1: 4px;
  --space-2: 8px;
  --space-3: 16px;
  --space-4: 32px;
  --space-5: 64px;
  --space-6: 128px;

  --max-width: 1100px;
}}

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }}
body {{
  font-family: var(--font-body);
  color: var(--ink);
  background: var(--surface);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
}}
img, svg {{ max-width: 100%; display: block; }}
a {{ color: inherit; text-decoration: none; }}

[data-reveal] {{
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.7s cubic-bezier(0.16,1,0.3,1),
              transform 0.7s cubic-bezier(0.16,1,0.3,1);
}}
[data-reveal].is-visible {{ opacity: 1; transform: translateY(0); }}

.top-nav {{
  position: fixed; top: 0; left: 0; right: 0;
  display: flex; justify-content: space-between; align-items: center;
  padding: var(--space-3) var(--space-4);
  z-index: 100;
  font-family: var(--font-display);
  font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--ink);
  background: linear-gradient(180deg, rgba(255,255,255,0.85) 0%, rgba(255,255,255,0) 100%);
  backdrop-filter: blur(8px);
}}
.brand-mark {{ font-weight: 700; }}

.hero {{
  min-height: 100vh;
  display: flex; align-items: center; justify-content: center;
  padding: var(--space-6) var(--space-4) var(--space-5);
  position: relative;
  background:
    radial-gradient(ellipse at top right, color-mix(in srgb, var(--accent) 18%, transparent), transparent 60%),
    radial-gradient(ellipse at bottom left, color-mix(in srgb, var(--accent) 10%, transparent), transparent 50%),
    var(--surface);
}}
.hero-inner {{
  max-width: var(--max-width);
  width: 100%;
}}
.hero-kicker {{
  font-family: var(--font-display);
  font-size: 12px; letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--muted);
  margin-bottom: var(--space-4);
}}
.hero-headline {{
  font-family: var(--font-display);
  font-weight: 700;
  font-size: clamp(48px, 8vw, 112px);
  line-height: 1.0;
  letter-spacing: -0.02em;
  margin-bottom: var(--space-4);
}}
.hero-accent {{ color: var(--accent); font-style: italic; }}
.hero-sub {{
  font-family: var(--font-body);
  font-size: clamp(18px, 1.6vw, 22px);
  color: var(--ink);
  max-width: 720px;
  margin-bottom: var(--space-5);
  font-weight: 400;
}}
.hero-author {{ padding-top: var(--space-3); border-top: 1px solid var(--border); }}
.author-name {{ font-family: var(--font-display); font-weight: 600; font-size: 16px; }}
.author-role {{ font-size: 13px; color: var(--muted); margin-top: 2px; }}
.hero-scroll-hint {{
  position: absolute; bottom: var(--space-5); left: 50%; transform: translateX(-50%);
  display: flex; flex-direction: column; align-items: center; gap: var(--space-2);
  font-family: var(--font-display);
  font-size: 10px; letter-spacing: 0.2em; text-transform: uppercase;
  color: var(--muted);
}}
.hint-line {{ width: 1px; height: 32px; background: var(--muted); animation: pulse 2s ease-in-out infinite; }}
@keyframes pulse {{ 0%,100% {{ opacity: 0.3; }} 50% {{ opacity: 1; }} }}

.section {{ padding: var(--space-6) var(--space-4); border-top: 1px solid var(--border); }}
.section-inner {{
  max-width: var(--max-width); margin: 0 auto;
  display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-5);
  align-items: start;
}}
@media (max-width: 880px) {{
  .section-inner {{ grid-template-columns: 1fr; }}
}}
.section-kicker {{
  font-family: var(--font-display);
  font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--accent); font-weight: 600;
  margin-bottom: var(--space-3);
}}
.section-heading {{
  font-family: var(--font-display); font-weight: 700;
  font-size: clamp(32px, 4vw, 48px);
  line-height: 1.1; letter-spacing: -0.01em;
  margin-bottom: var(--space-4);
}}
.section-body p {{
  font-size: 17px; color: var(--ink); margin-bottom: var(--space-3);
}}
.section-body p:last-child {{ margin-bottom: 0; }}
.section-figure {{ position: sticky; top: var(--space-5); }}
.figure-placeholder {{
  width: 100%; aspect-ratio: 4 / 5;
  background:
    linear-gradient(135deg, color-mix(in srgb, var(--accent) 60%, var(--ink)) 0%, var(--accent) 60%, color-mix(in srgb, var(--accent) 40%, white) 100%);
  border-radius: 2px;
  box-shadow: 0 30px 60px -20px rgba(0,0,0,0.25);
}}
.section-figure figcaption {{
  font-family: var(--font-display);
  font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase;
  color: var(--muted); margin-top: var(--space-2);
}}

.closing {{
  padding: var(--space-6) var(--space-4);
  background: var(--ink); color: var(--surface);
  text-align: center;
}}
.closing-inner {{ max-width: 720px; margin: 0 auto; }}
.closing-kicker {{
  font-family: var(--font-display);
  font-size: 12px; letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--accent); margin-bottom: var(--space-3);
}}
.closing-text {{
  font-family: var(--font-display); font-weight: 500;
  font-size: clamp(24px, 3vw, 36px); line-height: 1.3;
  margin-bottom: var(--space-4);
}}
.closing-contact {{
  font-size: 14px; color: var(--muted);
  display: flex; gap: var(--space-2); justify-content: center; flex-wrap: wrap;
}}
"""
```

- [ ] **Step 1.3: Add the JS template constant**

Append:

```python
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
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-visible'); });
  }
  if (!reduceMotion) {
    var hero = document.querySelector('.hero-inner');
    if (hero) {
      var ticking = false;
      window.addEventListener('scroll', function () {
        if (!ticking) {
          requestAnimationFrame(function () {
            var s = window.scrollY;
            if (s < window.innerHeight) {
              hero.style.transform = 'translateY(' + (s * 0.15) + 'px)';
              hero.style.opacity = Math.max(0, 1 - s / (window.innerHeight * 0.8));
            }
            ticking = false;
          });
          ticking = true;
        }
      }, { passive: true });
    }
  }
})();
"""
```

- [ ] **Step 1.4: Add the render function**

Append:

```python
def _initials(company: str) -> str:
    """First letter of each whitespace-separated word, max 3 chars."""
    parts = [p for p in company.split() if p]
    return "".join(p[0].upper() for p in parts[:3]) or "?"


def _paragraphs_to_html(paragraphs: list[str]) -> str:
    return "\n        ".join(f"<p>{p}</p>" for p in paragraphs)


def _sections_html(sections: list[dict]) -> str:
    out = []
    for s in sections:
        out.append(SECTION_TEMPLATE.format(
            section_id=s["id"],
            kicker=s["kicker"],
            heading=s["heading"],
            body_html=_paragraphs_to_html(s["body_paragraphs"]),
            image_placeholder_label=s.get("image_placeholder_label", ""),
        ))
    return "\n".join(out)


def render(content: dict, brand: dict) -> dict[str, str]:
    """Return ``{filename: contents}`` for the three landing files."""
    html = HTML_TEMPLATE.format(
        primary=brand["primary"],
        company=content["company"],
        company_initials=_initials(content["company"]),
        tagline=content["tagline"],
        candidate_name=content["candidate_name"],
        candidate_role=content["candidate_role"],
        candidate_email=content["candidate_email"],
        candidate_phone=content["candidate_phone"],
        candidate_linkedin=content["candidate_linkedin"],
        hero_headline_line_1=content["hero_headline_line_1"],
        hero_headline_line_2=content["hero_headline_line_2"],
        hero_subtitle=content["hero_subtitle"],
        sections_html=_sections_html(content["sections"]),
        closing_kicker=content["closing_kicker"],
        closing_text=content["closing_text"],
    )
    css = CSS_TEMPLATE.format(
        primary=brand["primary"],
        accent=brand["accent"],
        surface=brand["surface"],
        muted=brand["muted"],
        company=content["company"],
        candidate_name=content["candidate_name"],
    )
    return {
        "index.html": html,
        "styles.css": css,
        "scroll.js": JS_TEMPLATE,
    }
```

- [ ] **Step 1.5: Commit**

```bash
git add career_ops/generators/landing_template.py
git commit -m "feat(landing): add template strings + render helper"
```

---

## Task 2: Wire Claude tool_use to fill the content schema

**Files:**
- Create: `career_ops/generators/landing_generator.py`

This is the orchestrator. Same pattern as `cv_generator.py`: define a `_SYSTEM` prompt, a `_TOOL` schema describing the JSON shape Claude must return, call `llm.generate_structured`, hand the result to `landing_template.render`, write files to disk.

- [ ] **Step 2.1: Create the file with imports, brand resolver, and system prompt**

```python
"""Landing-page deliverable generator — replaces the old docx deliverable
for speculative job targets. Produces a self-contained HTML+CSS+JS bundle
inside ``output/<Company_Role>/landing/``.
"""
from __future__ import annotations

import logging
from pathlib import Path

from .. import llm
from ..analyzer import JobAnalysis
from ..config import settings
from ..discovery.normalize import Job
from . import angles
from . import landing_template
from ._paths import job_output_dir

logger = logging.getLogger(__name__)


# Warm-editorial palette used for every landing today. Per-company palette
# extraction is a future improvement (would need to scrape the brand site,
# which is what Firecrawl was meant for — leaving it for when we have a key).
_DEFAULT_BRAND = {
    "primary": "#1A1A1A",
    "accent": "#C8A876",
    "surface": "#FAF7F2",
    "muted": "#8A8A8A",
    "scheme": "warm-editorial",
}


_SYSTEM = """\
You are writing a single-page strategic-proposal landing for Paula De Francisco,
a Brand & Marketing Manager based in Dubai applying speculatively to a target
company in fashion retail.

The landing has SIX sections. You must fill every field of the supplied schema.

Rules:
1. Editorial tone — write like a brand magazine feature, not a consulting deck.
   Short sentences. Confident. No buzzwords ("synergy", "leverage", "ecosystem"
   used more than once, "best-in-class").
2. Body paragraphs in each section: 2-3 paragraphs, each 2-4 sentences.
3. Hero headline must split cleanly across two lines for visual rhythm — line
   one is the setup, line two is the payoff in italic accent.
4. Each section's `kicker` is "0N — <Theme>" (e.g. "01 — The diagnosis").
5. Each section's `image_placeholder_label` describes the editorial photo that
   would go there in 8-12 words (no full sentences) — used as a figcaption.
6. Stay strictly inside the candidate's real experience. Do not invent
   metrics, projects, or relationships.
7. The closing CTA is direct: ask for 30 minutes, by name, in one short line.
8. Output via the submit_landing_content tool.
"""
```

- [ ] **Step 2.2: Add the tool schema (continue same file)**

```python
_TOOL = {
    "name": "submit_landing_content",
    "description": "Submit the structured content for the strategic-proposal landing",
    "input_schema": {
        "type": "object",
        "properties": {
            "tagline": {"type": "string", "description": "One short line under the nav, e.g. 'A strategic proposal for Azadea'"},
            "hero_headline_line_1": {"type": "string", "description": "First line of the hero headline (setup, plain weight)"},
            "hero_headline_line_2": {"type": "string", "description": "Second line of the hero headline (payoff, italic accent color)"},
            "hero_subtitle": {"type": "string", "description": "One sentence under the headline, max 22 words"},
            "sections": {
                "type": "array",
                "minItems": 6,
                "maxItems": 6,
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "URL-safe id, e.g. 'thesis'"},
                        "kicker": {"type": "string", "description": "'0N — Theme' label"},
                        "heading": {"type": "string", "description": "Section heading, 3-8 words"},
                        "body_paragraphs": {
                            "type": "array",
                            "minItems": 2, "maxItems": 3,
                            "items": {"type": "string"},
                        },
                        "image_placeholder_label": {"type": "string", "description": "8-12 word description of the editorial photo"},
                    },
                    "required": ["id", "kicker", "heading", "body_paragraphs", "image_placeholder_label"],
                },
            },
            "closing_kicker": {"type": "string", "description": "Short uppercase label above the CTA, e.g. 'Next step'"},
            "closing_text": {"type": "string", "description": "One sentence asking for the meeting, addressed by name if known"},
        },
        "required": [
            "tagline", "hero_headline_line_1", "hero_headline_line_2",
            "hero_subtitle", "sections", "closing_kicker", "closing_text",
        ],
    },
}
```

- [ ] **Step 2.3: Add the Claude invocation + write-to-disk function**

```python
def _ask_claude(job: Job, analysis: JobAnalysis) -> dict | None:
    angle = angles.get((job.raw or {}).get("positioning_angle"))

    system_msg = _SYSTEM
    angle_block = ""
    if angle:
        system_msg = _SYSTEM + "\n\n" + angle.system_addendum + (
            "\n\nDELIVERABLE BRIEF: " + angle.deliverable_brief
        )
        angle_block = (
            "\n\n## Positioning angle\n"
            + angle.user_addendum
            + "\n\nDeliverable brief: " + angle.deliverable_brief
        )

    p = settings.profile
    user_msg = f"""\
Write the landing for a speculative outreach to {job.company}.

## Target
- Company: {job.company}
- Role framing: {job.title}
- Location: {job.location}

### Context provided to inform the proposal
{(job.description or 'No additional context.')[:4000]}

## Candidate
{p['personal']['name']} — {p['headline']}
{p['professional_summary']}

Key experience anchors:
- 42 multibrand key accounts at Miravia/Alibaba (Beauty, Fragrances, Fashion), +30% GMV QoQ
- Glovo Retail vertical — onboarded fashion + lifestyle brands into the marketplace
- DoFreeze — currently leading Brand & Marketing across 50+ countries (Dubai-based)
- Massimo Dutti factory store (Las Rozas) — premium fashion retail foundations
- Already in Dubai with UAE Residence Visa{angle_block}

Use the submit_landing_content tool to return all sections."""

    data = llm.generate_structured(
        system=system_msg,
        user=user_msg,
        tool_schema=_TOOL,
        tier="sonnet",
        max_tokens=4096,
    )
    if not data:
        logger.warning("LLM did not return landing content")
    return data
```

- [ ] **Step 2.4: Add the public `generate_landing` function**

```python
def _build_content(job: Job, claude_data: dict) -> dict:
    """Merge Claude's content with candidate identity fields."""
    p = settings.profile["personal"]
    return {
        "company": job.company,
        "role": job.title,
        "candidate_name": p["name"],
        "candidate_role": "Brand & Marketing Manager · Dubai, UAE",
        "candidate_email": p["email"],
        "candidate_phone": p["phone"],
        "candidate_linkedin": p.get("linkedin", "linkedin.com/in/paula-de-francisco-perez"),
        **claude_data,
    }


def generate_landing(job: Job, analysis: JobAnalysis) -> Path | None:
    """Generate the landing-page deliverable. Returns the path to index.html."""
    available, reason = llm.is_available()
    if not available:
        logger.warning("LLM not available (%s) — cannot generate landing", reason)
        return None

    logger.info("generating landing for %s @ %s", job.title[:40], job.company)

    claude_data = _ask_claude(job, analysis)
    if not claude_data:
        return None

    content = _build_content(job, claude_data)
    files = landing_template.render(content, _DEFAULT_BRAND)

    landing_dir = job_output_dir(job) / "landing"
    landing_dir.mkdir(parents=True, exist_ok=True)
    for name, body in files.items():
        (landing_dir / name).write_text(body, encoding="utf-8")

    index = landing_dir / "index.html"
    logger.info("landing saved: %s", index)
    return index
```

- [ ] **Step 2.5: Commit**

```bash
git add career_ops/generators/landing_generator.py
git commit -m "feat(landing): add Claude-driven content generator"
```

---

## Task 3: Re-export from the package + add unit tests

**Files:**
- Modify: `career_ops/generators/__init__.py`
- Create: `tests/__init__.py`
- Create: `tests/test_landing_generator.py`

- [ ] **Step 3.1: Re-export the new function**

Open `career_ops/generators/__init__.py` and change it to:

```python
"""Content generators — CV, cover letter, outreach, deliverables, and form responses."""
from ._paths import job_output_dir
from .cover_letter import generate_cover_letter
from .cv_generator import generate_cv
from .deliverables import generate_all_deliverables, generate_deliverable
from .form_responses import generate_form_responses
from .landing_generator import generate_landing
from .outreach import create_outreach_draft, generate_outreach

__all__ = [
    "generate_cv",
    "generate_cover_letter",
    "generate_outreach",
    "create_outreach_draft",
    "generate_deliverable",
    "generate_all_deliverables",
    "generate_form_responses",
    "generate_landing",
    "job_output_dir",
]
```

- [ ] **Step 3.2: Create the tests package marker**

Create `tests/__init__.py` as an empty file:

```python
```

- [ ] **Step 3.3: Write the failing test for template rendering**

Create `tests/test_landing_generator.py`:

```python
"""Unit tests for landing-page deliverable generation.

These tests exercise the deterministic parts — schema → HTML rendering and
file emission. The Claude call is mocked because it is non-deterministic.
"""
from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from career_ops.generators import landing_template


SAMPLE_CONTENT = {
    "company": "Azadea",
    "role": "Marketing Manager (Speculative)",
    "candidate_name": "Paula De Francisco",
    "candidate_role": "Brand & Marketing Manager · Dubai, UAE",
    "candidate_email": "paulich98@hotmail.com",
    "candidate_phone": "+971 50 386 3656",
    "candidate_linkedin": "linkedin.com/in/paula-de-francisco-perez",
    "tagline": "A strategic proposal for Azadea",
    "hero_headline_line_1": "Orchestrating",
    "hero_headline_line_2": "fifty brands as one.",
    "hero_subtitle": "What if your portfolio behaved like an ecosystem instead of a holding?",
    "sections": [
        {
            "id": f"sec{i}",
            "kicker": f"0{i} — Theme {i}",
            "heading": f"Heading {i}",
            "body_paragraphs": [f"Para {i}.A", f"Para {i}.B"],
            "image_placeholder_label": f"Editorial photo {i}",
        }
        for i in range(1, 7)
    ],
    "closing_kicker": "Next step",
    "closing_text": "Half an hour, by phone or coffee.",
}

SAMPLE_BRAND = {
    "primary": "#1A1A1A",
    "accent": "#C8A876",
    "surface": "#FAF7F2",
    "muted": "#8A8A8A",
    "scheme": "warm-editorial",
}


def test_render_returns_three_files():
    files = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)
    assert set(files.keys()) == {"index.html", "styles.css", "scroll.js"}
```

- [ ] **Step 3.4: Run the test, confirm it passes (template already implements this)**

```bash
cd c:/Users/gmunoz02/Desktop/CV_Automation && python -m pytest tests/test_landing_generator.py::test_render_returns_three_files -v
```

Expected: `PASSED` (template was written first in Task 1).

- [ ] **Step 3.5: Add the rest of the rendering assertions**

Append to `tests/test_landing_generator.py`:

```python
def test_render_injects_brand_palette():
    files = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)
    css = files["styles.css"]
    assert "--ink: #1A1A1A" in css
    assert "--accent: #C8A876" in css
    assert "--surface: #FAF7F2" in css


def test_render_injects_company_initials():
    files = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)
    html = files["index.html"]
    # "Azadea" → "A"
    assert ">A</div>" in html or 'class="brand-mark">A<' in html


def test_render_emits_all_six_sections():
    files = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)
    html = files["index.html"]
    for i in range(1, 7):
        assert f'id="sec{i}"' in html
        assert f"Heading {i}" in html
        assert f"Para {i}.A" in html
        assert f"Para {i}.B" in html


def test_render_includes_hero_headline_split():
    files = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)
    html = files["index.html"]
    assert "Orchestrating" in html
    assert "fifty brands as one." in html
    assert '<span class="hero-accent">fifty brands as one.</span>' in html


def test_render_includes_closing_cta():
    files = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)
    html = files["index.html"]
    assert "Next step" in html
    assert "Half an hour, by phone or coffee." in html


def test_render_includes_contact_details():
    files = landing_template.render(SAMPLE_CONTENT, SAMPLE_BRAND)
    html = files["index.html"]
    assert "paulich98@hotmail.com" in html
    assert "+971 50 386 3656" in html
    assert "linkedin.com/in/paula-de-francisco-perez" in html
```

- [ ] **Step 3.6: Run all the render tests**

```bash
python -m pytest tests/test_landing_generator.py -v -k "render"
```

Expected: 6 PASSED.

- [ ] **Step 3.7: Add the integration test for `generate_landing`**

Append:

```python
def test_generate_landing_writes_files_to_disk(tmp_path, monkeypatch):
    """generate_landing should call Claude, fill the schema, and write 3 files."""
    from career_ops.config import settings
    from career_ops.discovery.normalize import Job
    from career_ops.analyzer import JobAnalysis
    from career_ops.generators import landing_generator

    # Redirect output_dir to a tmp dir so we don't litter the real output/
    monkeypatch.setattr(settings, "output_dir", tmp_path)

    job = Job(
        id="testid", title="Marketing Manager (Speculative)", company="Azadea",
        location="Dubai, UAE", url="", source="speculative",
        description="Multibrand fashion holding. Portfolio of 50+ brands.",
        raw={"positioning_angle": "fashion_commerce_bridge", "speculative": True},
    )
    analysis = JobAnalysis(
        score=85, tier="Hot", skills_match=[], missing_skills=[],
        sector_fit="Fashion Retail", seniority_fit="Mid-Senior",
        red_flags=[], ats_keywords=[], reasoning="speculative",
    )

    fake_claude_payload = {k: v for k, v in SAMPLE_CONTENT.items() if k in {
        "tagline", "hero_headline_line_1", "hero_headline_line_2",
        "hero_subtitle", "sections", "closing_kicker", "closing_text",
    }}

    with patch.object(landing_generator.llm, "is_available", return_value=(True, "anthropic")), \
         patch.object(landing_generator.llm, "generate_structured", return_value=fake_claude_payload):
        out = landing_generator.generate_landing(job, analysis)

    assert out is not None
    assert out.name == "index.html"
    assert out.parent.name == "landing"
    assert (out.parent / "styles.css").exists()
    assert (out.parent / "scroll.js").exists()
    html = out.read_text(encoding="utf-8")
    assert "Azadea" in html
    assert "Paula De Francisco" in html


def test_generate_landing_returns_none_when_llm_unavailable(tmp_path, monkeypatch):
    from career_ops.config import settings
    from career_ops.discovery.normalize import Job
    from career_ops.analyzer import JobAnalysis
    from career_ops.generators import landing_generator

    monkeypatch.setattr(settings, "output_dir", tmp_path)

    job = Job(
        id="x", title="x", company="X", location="x", url="", source="speculative",
        description="", raw={"speculative": True},
    )
    analysis = JobAnalysis(
        score=0, tier="Cold", skills_match=[], missing_skills=[],
        sector_fit="", seniority_fit="", red_flags=[], ats_keywords=[], reasoning="",
    )

    with patch.object(landing_generator.llm, "is_available", return_value=(False, "no key")):
        out = landing_generator.generate_landing(job, analysis)

    assert out is None
```

- [ ] **Step 3.8: Run the full test file**

```bash
python -m pytest tests/test_landing_generator.py -v
```

Expected: 8 PASSED.

- [ ] **Step 3.9: Commit**

```bash
git add career_ops/generators/__init__.py tests/__init__.py tests/test_landing_generator.py
git commit -m "feat(landing): re-export + unit tests"
```

---

## Task 4: Hook into the dashboard

**Files:**
- Modify: `career_ops/webapp/api.py`

Three changes: (1) mount `/output/` static, (2) add `GET /api/jobs/{id}/landing` returning the URL, (3) in `_generate`, branch to `generate_landing` when the job is speculative.

- [ ] **Step 4.1: Mount the output directory**

Open `career_ops/webapp/api.py`. Find the line:

```python
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
```

Add immediately after:

```python
# Expose the output/ tree so per-job landings can be navigated to in-browser.
# Each landing is self-contained (HTML + CSS + JS + assets) under
# output/<Company_Role>/landing/, and the browser fetches sibling files via
# relative URLs once it has loaded index.html.
app.mount("/output", StaticFiles(directory=str(settings.output_dir)), name="output")
```

- [ ] **Step 4.2: Replace the speculative branch in `_generate`**

Find the existing function inside `generate_documents` (around line 442):

```python
        # Speculative targets: also generate the angle's differentiating
        # deliverable in the same click. Automation-first — Paula gets the
        # full outreach package without needing to fire a second action.
        if (job.raw or {}).get("speculative"):
            try:
                from ..generators.deliverables import generate_deliverable
                generate_deliverable(job, analysis)
            except Exception:
                logger.exception("speculative deliverable generation failed for %s", job.id)
```

Replace with:

```python
        # Speculative targets: in lieu of the docx deliverable, build a
        # navigable HTML landing under output/<Company_Role>/landing/.
        # The dashboard exposes it via /api/jobs/{id}/landing.
        if (job.raw or {}).get("speculative"):
            try:
                from ..generators import generate_landing
                generate_landing(job, analysis)
            except Exception:
                logger.exception("speculative landing generation failed for %s", job.id)
```

- [ ] **Step 4.3: Add a helper that resolves the landing URL for a job**

Place this directly above the `# API: Documents` divider (around line 477, just after the `generate_documents` endpoint):

```python
def _landing_url_for(job_data: dict) -> str | None:
    """Return the in-dashboard URL to a job's landing, or None if not built yet."""
    from ..generators._paths import job_output_dir
    from ..discovery.normalize import Job

    job = Job(
        id=job_data["id"],
        title=job_data.get("title", ""),
        company=job_data.get("company", ""),
        location=job_data.get("location", ""),
        url=job_data.get("url", ""),
        source=job_data.get("source", "indeed"),
        description="",
    )
    index = job_output_dir(job) / "landing" / "index.html"
    if not index.exists():
        return None
    rel = index.relative_to(settings.output_dir)
    return "/output/" + str(rel).replace("\\", "/")
```

- [ ] **Step 4.4: Add the GET endpoint**

Directly after the `/deliverable` endpoint (around line 565, right before the `# API: Contacts` divider):

```python
@app.get("/api/jobs/{job_id}/landing")
async def get_landing_url(job_id: str):
    """Return the in-dashboard URL of this job's landing deliverable.

    The frontend uses this to render an 'Open landing →' link on speculative
    job cards. Returns ``{url: null}`` if the landing hasn't been generated
    yet so the UI can show a disabled state.
    """
    jobs = _load_jobs(include_hidden=True)
    job_data = _find_job(job_id, jobs)
    if not job_data:
        raise HTTPException(404, f"Job not found: {job_id}")
    return {"url": _landing_url_for(job_data)}
```

- [ ] **Step 4.5: Surface the landing URL inside the job's `_files` block**

Find `_index_generated_files` (around line 240). It returns a dict keyed by job_id with `cv/cl/form/form_json/deliverable`. Add a sibling `landing` key.

Inside the function, after `result = {j["id"]: {...} for j in jobs}`, change the initialiser to include `"landing": None`:

```python
    result: dict[str, dict] = {
        j["id"]: {"cv": None, "cl": None, "form": None, "form_json": None,
                  "deliverable": None, "landing": None}
        for j in jobs
    }
```

Then at the bottom of the function, just before `return result`, add:

```python
    # Landing URLs (HTML deliverables for speculative jobs)
    for j in jobs:
        index = output / _job_filename_key(j)[0]  # placeholder; we want the folder
    # Walk for landings — they live at output/<folder>/landing/index.html
    for landing in output.rglob("landing/index.html"):
        try:
            rel = landing.relative_to(output)
        except ValueError:
            continue
        if rel.parts and rel.parts[0] in _EXCLUDED_TOP_DIRS:
            continue
        folder_name = rel.parts[0]
        # Match this folder back to a job by checking company/title substrings
        for job_id, (company, title) in job_keys:
            if company and title and company in folder_name and title in folder_name:
                result[job_id]["landing"] = "/output/" + str(rel).replace("\\", "/")
                break

    return result
```

Wait — the placeholder line `for j in jobs: index = output / _job_filename_key(j)[0]` is dead. Remove it. Final form of the appended block:

```python
    # Landings live at output/<Company_Role>/landing/index.html — expose as URL
    for landing in output.rglob("landing/index.html"):
        try:
            rel = landing.relative_to(output)
        except ValueError:
            continue
        if rel.parts and rel.parts[0] in _EXCLUDED_TOP_DIRS:
            continue
        folder_name = rel.parts[0]
        for job_id, (company, title) in job_keys:
            if company and title and company in folder_name and title in folder_name:
                result[job_id]["landing"] = "/output/" + str(rel).replace("\\", "/")
                break

    return result
```

(The existing `return result` is replaced by this block; we re-introduce `return result` at the end of the block.)

- [ ] **Step 4.6: Smoke test the dashboard import**

```bash
cd c:/Users/gmunoz02/Desktop/CV_Automation && python -c "from career_ops.webapp.api import app; print('app loaded ok, routes:', len(app.routes))"
```

Expected: prints a route count > 30, no traceback.

- [ ] **Step 4.7: Commit**

```bash
git add career_ops/webapp/api.py
git commit -m "feat(landing): mount /output, wire GET /landing, branch generate"
```

---

## Task 5: Surface the "Open landing" link in the dashboard UI

**Files:**
- Modify: `career_ops/webapp/static/index.html`

The detail card already renders CV/CL/Deliverable/Form download buttons by reading `job._files`. We add an "Open landing →" anchor that opens the landing URL in a new tab when `job._files.landing` is non-null.

- [ ] **Step 5.1: Locate where document buttons are rendered**

```bash
grep -n "Download CV\|_files.cv\|job.\\._files\\.cv" c:/Users/gmunoz02/Desktop/CV_Automation/career_ops/webapp/static/index.html | head -20
```

Note the surrounding template literal in the detail view (the file is a vanilla SPA).

- [ ] **Step 5.2: Add the landing button next to the deliverable button**

Find the snippet that renders the deliverable download (search for `Deliverable`). It looks like:

```javascript
${j._files.deliverable ? `<a class="btn btn-ghost" href="/api/jobs/${j.id}/deliverable" target="_blank">Deliverable PDF</a>` : ''}
```

Add immediately after it:

```javascript
${j._files.landing ? `<a class="btn btn-purple" href="${j._files.landing}" target="_blank">Open landing →</a>` : ''}
```

(If the exact button-row HTML uses different wrappers, match the surrounding pattern — the goal is one anchor element, opens in new tab, only renders when `_files.landing` exists.)

- [ ] **Step 5.3: Reload the dashboard and confirm**

Start (or already running) dashboard on port 8064. Open `http://localhost:8064/` in the browser. There won't be any landings yet, so the new button doesn't render — that's correct.

- [ ] **Step 5.4: Commit**

```bash
git add career_ops/webapp/static/index.html
git commit -m "feat(landing): show 'Open landing' button on job detail card"
```

---

## Task 6: End-to-end test — produce the two real landings

**Files:** none modified. This step runs the live pipeline.

- [ ] **Step 6.1: Confirm both speculative targets still exist in `data/scored_jobs.json`**

```bash
cd c:/Users/gmunoz02/Desktop/CV_Automation && python -c "
import json
js = json.load(open('data/scored_jobs.json', encoding='utf-8'))
spec = [(j['id'], j['company'], j.get('positioning_angle')) for j in js if j.get('speculative')]
for s in spec: print(s)
"
```

Expected: prints `('acfd6b135aaed081', 'Gloria Jeans', 'inditex_insider')` and `('a1969563804a8468', 'Azadea', 'fashion_commerce_bridge')`.

- [ ] **Step 6.2: Delete the obsolete docx deliverables for the two speculative jobs**

```bash
cd c:/Users/gmunoz02/Desktop/CV_Automation && \
rm -f "output/Gloria Jeans - Brand Marketing Manager (Speculative)/Deliverable_Paula_"*.pdf && \
rm -f "output/Azadea - Marketing Manager (Speculative)/Deliverable_Paula_"*.pdf && \
ls "output/Gloria Jeans - Brand Marketing Manager (Speculative)/" "output/Azadea - Marketing Manager (Speculative)/"
```

Expected: no `Deliverable_*.pdf` remaining; CV + CL still present.

- [ ] **Step 6.3: Generate the two landings via the Python API (Anthropic direct, bypassing chatqueue)**

```bash
cd c:/Users/gmunoz02/Desktop/CV_Automation && python << 'PYEOF'
from career_ops.config import settings
settings.llm_provider = "anthropic"
settings.dry_run = False

from career_ops.generators import generate_landing
from career_ops.webapp.api import _load_jobs, _find_job, _reconstruct_job

for jid in ("acfd6b135aaed081", "a1969563804a8468"):
    jd = _find_job(jid, _load_jobs(include_hidden=True))
    job, an = _reconstruct_job(jd)
    out = generate_landing(job, an)
    print(f"  {jd['company']:<14} -> {out}")
PYEOF
```

Expected output:

```
  Gloria Jeans   -> .../landing/index.html
  Azadea         -> .../landing/index.html
```

- [ ] **Step 6.4: Validate each landing renders in a browser**

Restart the dashboard if not running:

```bash
cd c:/Users/gmunoz02/Desktop/CV_Automation && CAREEROPS_AUTO_BROWSER=0 nohup python scripts/run_webapp.py --port 8064 > /tmp/dash.log 2>&1 & disown
```

Open in browser:
- `http://127.0.0.1:8064/output/Gloria%20Jeans%20-%20Brand%20Marketing%20Manager%20(Speculative)/landing/index.html`
- `http://127.0.0.1:8064/output/Azadea%20-%20Marketing%20Manager%20(Speculative)/landing/index.html`

Manual checks:
- Hero loads with split headline + accent on line 2
- Six sections present, kickers numbered 01–06
- Scroll reveals fire (items fade up as they enter viewport)
- No mention of "Inditex" anywhere on the Gloria Jeans landing
- "30 minutes" CTA appears at the bottom

If any check fails, do not proceed — iterate on the prompt in `_SYSTEM` or the CSS in `landing_template.py`.

- [ ] **Step 6.5: Confirm the dashboard surfaces the landing URL**

```bash
curl -s "http://127.0.0.1:8064/api/jobs/acfd6b135aaed081/landing"
```

Expected: `{"url":"/output/Gloria Jeans - Brand Marketing Manager (Speculative)/landing/index.html"}`.

- [ ] **Step 6.6: Commit the generated landings**

```bash
git add "output/Gloria Jeans - Brand Marketing Manager (Speculative)/landing/" \
        "output/Azadea - Marketing Manager (Speculative)/landing/"
git commit -m "feat(landing): ship Azadea + Gloria Jeans first cuts"
```

---

## Self-Review

**Spec coverage:** Six requirements were stated:
1. Replace docx deliverable for speculative jobs → Task 4.2 swaps `generate_deliverable` for `generate_landing`. ✓
2. Two landings (Azadea + Gloria Jeans) — Task 6 produces both. ✓
3. Avoid "Inditex" in Gloria Jeans output — `_SYSTEM` rule 6 + manual check in Task 6.4. ✓
4. 6 sections, premium editorial — schema in Task 2.2 enforces exactly 6 sections; CSS template in Task 1.2 implements editorial design. ✓
5. Higgsfield deferred — `image_placeholder_label` is a figcaption today; CSS `.figure-placeholder` renders a brand-tinted gradient. Swap-point for real images is one place: change `<div class="figure-placeholder">` to `<img>` in `SECTION_TEMPLATE`. ✓
6. Dashboard integration — Tasks 4 + 5 mount static, expose URL endpoint, surface button. ✓

**Placeholder scan:** Searched for "TBD", "TODO", "implement later", "Similar to Task". None found.

**Type consistency:** `content` schema in Task 1 ↔ tool schema in Task 2.2 ↔ test fixture in Task 3.3 all use the same field names (`tagline`, `hero_headline_line_1`, etc.). `brand` dict has `primary/accent/surface/muted` consistently. `generate_landing(job, analysis) → Path | None` matches sibling generators.

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-05-13-landing-deliverable.md`. Two execution options:

1. **Subagent-Driven (recommended)** — I dispatch a fresh subagent per task, review between tasks, fast iteration.
2. **Inline Execution** — Execute tasks in this session using executing-plans, batch execution with checkpoints.

Which approach?
