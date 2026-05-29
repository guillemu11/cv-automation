"""Job-agnostic scroll-driven campaign landing generator.

Takes any ``(job, brand_url)`` pair and produces a deployable
``output/landings/landing_<slug>/`` folder with:
  - ``brand.json``        — palette + typography extracted from ``brand_url``
  - ``ANGLES.md``         — the 3 campaign angles considered; chosen marked
  - ``index.html``        — sticky scroll stage + executions + KPIs + credits
  - ``styles.css``        — single-source CSS using brand tokens
  - ``scroll.js``         — frame-binding + chapter orchestration
  - ``assets/``           — hero keyframes A+B, hero-loop.mp4, 149 frames,
                            4 execution images (all Higgsfield-generated)

Pipeline (mirrors campaign-landing skill's 6 phases):
  1. ``extract_brand_from_url(url)``            — Firecrawl → WebFetch fallback
  2. ``propose_landing_content(job, brand)``    — one LLM call returns
                                                   tagline + insight + manifesto
                                                   + 4 executions + 4 KPIs +
                                                   all 7 Higgsfield prompts
  3. Higgsfield generation                       — gpt_image_2 ×6 + seedance_2_0
  4. Frame extraction                            — ffmpeg fps=29.47 → 149 jpg
  5. HTML/CSS/JS render                          — template fill, write to disk

The orchestrator script ``scripts/scroll_landing_for_job.py`` wraps this for
CLI use with ``--job-id <id>``.
"""
from __future__ import annotations

import json
import logging
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

import requests

from .. import llm
from ..analyzer import JobAnalysis
from ..config import settings
from ..discovery.normalize import Job

logger = logging.getLogger(__name__)

HF_BIN = Path(
    r"C:\Users\gmunoz02\node\node-v20.20.0-win-x64\node_modules\@higgsfield\cli\vendor\hf.exe"
)
FIRECRAWL_URL = "https://api.firecrawl.dev/v2/scrape"


# =====================================================================
# 1. Brand extraction
# =====================================================================

_BRAND_FALLBACK = {
    "palette": {
        "primary": "#0E0F12",
        "secondary": "#737373",
        "accent": "#FFB400",
        "bg": "#FFFFFF",
        "text": "#0E0F12",
    },
    "typography": {
        "display": "Manrope",
        "body": "Inter",
        "serif": "Source Serif 4",
    },
    "logo_hint": "Wordmark in display sans-serif",
    "tone": ["modern", "direct", "credible"],
}


def _firecrawl_branding(url: str) -> dict | None:
    if not settings.firecrawl_api_key:
        return None
    try:
        r = requests.post(
            FIRECRAWL_URL,
            headers={"Authorization": f"Bearer {settings.firecrawl_api_key}"},
            json={"url": url, "formats": ["branding"]},
            timeout=60,
        )
        if r.status_code != 200:
            logger.warning("Firecrawl branding %s -> HTTP %d", url, r.status_code)
            return None
        data = r.json().get("data") or {}
        branding = data.get("branding") or {}
        if not branding:
            return None
        # Firecrawl branding shape: {colors: {...}, fonts: {...}, logos: [...]}
        colors = branding.get("colors") or {}
        fonts = branding.get("fonts") or {}
        return {
            "palette": _normalize_palette(colors),
            "typography": _normalize_fonts(fonts),
            "logo_hint": _logo_hint(branding.get("logos") or []),
            "tone": branding.get("tone") or ["modern", "credible"],
            "source": f"firecrawl:{url}",
        }
    except Exception as exc:  # noqa: BLE001
        logger.warning("Firecrawl branding error %s: %s", url, exc)
        return None


def _normalize_palette(colors: Any) -> dict:
    """Coerce a Firecrawl colors object into our 5-slot palette shape."""
    hexes = []
    if isinstance(colors, dict):
        for v in colors.values():
            if isinstance(v, str) and re.match(r"^#[0-9a-fA-F]{3,8}$", v):
                hexes.append(v)
            elif isinstance(v, list):
                hexes += [x for x in v if isinstance(x, str) and x.startswith("#")]
    if isinstance(colors, list):
        hexes = [x for x in colors if isinstance(x, str) and x.startswith("#")]

    hexes = list(dict.fromkeys(hexes))  # dedupe preserve order
    palette = dict(_BRAND_FALLBACK["palette"])
    if hexes:
        palette["primary"] = hexes[0]
    if len(hexes) > 1:
        palette["accent"] = hexes[1]
    # secondary defaults to a near-black; only override if we have a dark hex
    return palette


def _normalize_fonts(fonts: Any) -> dict:
    if not isinstance(fonts, dict):
        return dict(_BRAND_FALLBACK["typography"])
    # Try to find display + body names; otherwise use defaults so Google Fonts loads
    typo = dict(_BRAND_FALLBACK["typography"])
    for key in ("display", "heading", "h1"):
        v = fonts.get(key)
        if isinstance(v, str) and v.strip():
            typo["display"] = v.strip()
            break
    for key in ("body", "paragraph", "default"):
        v = fonts.get(key)
        if isinstance(v, str) and v.strip():
            typo["body"] = v.strip()
            break
    return typo


def _logo_hint(logos: list) -> str:
    if not logos:
        return "Wordmark in display sans-serif"
    first = logos[0]
    if isinstance(first, dict):
        return first.get("alt") or first.get("type") or "Wordmark"
    return "Wordmark"


def _webfetch_branding(url: str) -> dict | None:
    """Last-resort: fetch the HTML ourselves and let the LLM mine it for tokens.

    Claude/Gemini APIs don't have browse access, so passing them a URL alone
    yields nothing useful. We pull the page with httpx, strip to ~12 KB of the
    raw HTML + inline-CSS, and feed THAT to ``llm.generate_structured``.
    """
    try:
        r = requests.get(url, timeout=20,
                         headers={"User-Agent": "Mozilla/5.0 (CV_Automation scroll_landing)"})
        r.raise_for_status()
        html = r.text
    except Exception as exc:  # noqa: BLE001
        logger.warning("HTTP fetch failed for %s: %s", url, exc)
        return None

    # Compress: keep <head>, <style>, hex colors, CSS custom props, font-family
    # declarations, plus the first ~3 KB of <body> text. Cap at ~14 KB total.
    head_m = re.search(r"<head[^>]*>.*?</head>", html, flags=re.S | re.I)
    head = head_m.group(0) if head_m else ""
    style_blocks = "\n".join(re.findall(r"<style[^>]*>.*?</style>", html, flags=re.S | re.I)[:6])
    hex_hits = " ".join(list(dict.fromkeys(re.findall(r"#[0-9a-fA-F]{6}", html)))[:40])
    font_hits = "\n".join(re.findall(r"font-family\s*:\s*[^;{}]+", html)[:30])
    body_text = re.sub(r"<[^>]+>", " ", html)
    body_text = re.sub(r"\s+", " ", body_text)[:2500]
    digest = (
        f"URL: {url}\n\n--- <head> ---\n{head[:4000]}\n\n"
        f"--- <style> blocks ---\n{style_blocks[:4000]}\n\n"
        f"--- hex colors observed ---\n{hex_hits}\n\n"
        f"--- font-family declarations ---\n{font_hits[:1500]}\n\n"
        f"--- body copy excerpt ---\n{body_text}"
    )

    tool = {
        "name": "submit_brand",
        "description": "Submit the extracted brand identity for a webpage.",
        "input_schema": {
            "type": "object",
            "properties": {
                "primary": {"type": "string", "description": "Dominant brand hex (NOT a near-white or near-black — the actual brand color)"},
                "secondary": {"type": "string", "description": "Secondary hex (often dark text or near-black)"},
                "accent": {"type": "string", "description": "Accent/highlight hex"},
                "bg": {"type": "string", "description": "Background hex (often white)"},
                "text": {"type": "string", "description": "Body text hex"},
                "display_font": {"type": "string", "description": "Display/headline font family. If custom, return 'Manrope'."},
                "body_font": {"type": "string", "description": "Body font family. If custom, return 'Inter'."},
                "logo_hint": {"type": "string"},
                "tone": {"type": "array", "items": {"type": "string"}, "description": "3 single-word adjectives describing the voice"},
            },
            "required": ["primary", "bg", "text", "tone"],
        },
    }
    user = (
        "Below is a digest of a brand homepage. Extract the brand identity into the "
        "submit_brand tool.\n\n"
        "Rules:\n"
        "- `primary`: pick the dominant brand color from the hex list — NOT white, NOT black. "
        "Look at <style> blocks and CSS custom properties for `--primary`-style declarations.\n"
        "- `bg` and `text`: defaults are #FFFFFF and #0E0F12 unless the digest clearly says otherwise.\n"
        "- Fonts: if the font-family declarations name a custom face you cannot map to a "
        "Google Font, use 'Manrope' (display) and 'Inter' (body).\n"
        "- Tone: 3 single-word adjectives from the body copy.\n\n"
        f"{digest}"
    )
    try:
        data = llm.generate_structured(
            system="You extract brand identity from a single webpage. Be literal — never invent values.",
            user=user,
            tool_schema=tool,
            tier="sonnet",
            max_tokens=512,
        )
    except Exception as exc:  # noqa: BLE001
        logger.warning("WebFetch-style brand extraction failed for %s: %s", url, exc)
        return None
    if not data:
        return None
    return {
        "palette": {
            "primary": data.get("primary", "#0E0F12"),
            "secondary": data.get("secondary", "#0E0F12"),
            "accent": data.get("accent", "#FFB400"),
            "bg": data.get("bg", "#FFFFFF"),
            "text": data.get("text", "#0E0F12"),
        },
        "typography": {
            "display": data.get("display_font", "Manrope"),
            "body": data.get("body_font", "Inter"),
            "serif": "Source Serif 4",
        },
        "logo_hint": data.get("logo_hint", "Wordmark"),
        "tone": data.get("tone") or ["modern", "credible"],
        "source": f"llm_webread:{url}",
    }


def extract_brand_from_url(url: str) -> dict:
    """Phase 1 of the workflow. Firecrawl → WebFetch → safe fallback."""
    for fn in (_firecrawl_branding, _webfetch_branding):
        result = fn(url)
        if result:
            return result
    logger.warning("Brand extraction fully failed for %s — using safe fallback", url)
    return {**_BRAND_FALLBACK, "source": "fallback"}


# =====================================================================
# 2. Campaign content via single LLM call
# =====================================================================

@dataclass
class LandingContent:
    """All the copy + Higgsfield prompts to build one landing."""
    angle_name: str
    tagline_first: str
    tagline_accent: str
    insight_label: str
    insight_stat: str          # e.g. "73", "4M"
    insight_pct: str           # e.g. "%", "+"
    insight_body: str
    insight_source: str
    manifesto: list[str]       # 4 paragraphs — last one is styled as the final line
    transition_first: str
    transition_accent: str
    transition_sub: str
    executions: list[dict] = field(default_factory=list)  # 4 × {label,title,body,foot,prompt}
    kpis: list[dict] = field(default_factory=list)         # 4 × {value,label}
    keyframe_a_prompt: str = ""
    keyframe_b_prompt: str = ""
    hero_video_prompt: str = ""
    alt_angles: list[dict] = field(default_factory=list)   # the 2 not chosen


_CONTENT_TOOL = {
    "name": "submit_landing_content",
    "description": "Submit the full content + image prompts for one scroll-driven campaign landing.",
    "input_schema": {
        "type": "object",
        "properties": {
            "angle_name": {"type": "string", "description": "Short campaign codename"},
            "tagline_first": {"type": "string", "description": "First half of the hero tagline (no period)"},
            "tagline_accent": {"type": "string", "description": "Second half, colored in brand-primary (no period)"},
            "insight_label": {"type": "string", "description": "Short kicker, e.g. 'The insight' or 'The audience'"},
            "insight_stat": {"type": "string", "description": "Big number/word, e.g. '73' or '4M'"},
            "insight_pct": {"type": "string", "description": "Suffix on the stat, e.g. '%' or '+'"},
            "insight_body": {"type": "string", "description": "1-2 sentences explaining the stat"},
            "insight_source": {"type": "string", "description": "Citation line. Plausible sources only — Nielsen/Euromonitor/etc + year"},
            "manifesto": {"type": "array", "items": {"type": "string"}, "description": "4 paragraphs, each 1-2 sentences. Editorial voice. The LAST one becomes the brand-primary-colored final line."},
            "transition_first": {"type": "string"},
            "transition_accent": {"type": "string"},
            "transition_sub": {"type": "string"},
            "executions": {
                "type": "array",
                "minItems": 6,
                "maxItems": 6,
                "items": {
                    "type": "object",
                    "properties": {
                        "slug": {"type": "string", "description": "filesystem-safe slug"},
                        "label": {"type": "string", "description": "Channel/category chip"},
                        "title": {"type": "string"},
                        "body": {"type": "string", "description": "2-3 sentences"},
                        "foot": {"type": "string", "description": "Pilot/footprint metric"},
                        "image_prompt": {"type": "string", "description": "Photoreal image-gen prompt for this exec card. ALL on-image text MUST be in English."},
                    },
                    "required": ["slug", "label", "title", "body", "foot", "image_prompt"],
                },
                "description": "EXACTLY 6 executions — 3+3 grid fits cleanly at desktop widths; 4 leaves an ugly 3+1.",
            },
            "kpis": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "value": {"type": "string", "description": "Short value, e.g. '+200%' or '€8M'"},
                        "label": {"type": "string", "description": "Two-line label, use <br> for the line break"},
                    },
                    "required": ["value", "label"],
                },
                "description": "Exactly 4 KPIs",
            },
            "keyframe_a_prompt": {"type": "string", "description": "Photoreal image-gen prompt for hero keyframe A (start of the 8s loop)"},
            "keyframe_b_prompt": {"type": "string", "description": "Photoreal image-gen prompt for hero keyframe B (end of the 8s loop)"},
            "hero_video_prompt": {"type": "string", "description": "Seedance 2.0 prompt for the 5-8s transition from A to B"},
            "alt_angles": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "tagline": {"type": "string"},
                        "insight": {"type": "string"},
                        "hero": {"type": "string"},
                        "kpi": {"type": "string"},
                    },
                },
                "description": "The 2 alternate campaign angles considered but not chosen (for ANGLES.md).",
            },
        },
        "required": [
            "angle_name", "tagline_first", "tagline_accent",
            "insight_label", "insight_stat", "insight_pct", "insight_body", "insight_source",
            "manifesto", "transition_first", "transition_accent", "transition_sub",
            "executions", "kpis",
            "keyframe_a_prompt", "keyframe_b_prompt", "hero_video_prompt",
        ],
    },
}


def propose_landing_content(
    job: Job,
    analysis: JobAnalysis,
    brand: dict,
    angle_brief: str | None = None,
) -> LandingContent:
    """Single Claude call to produce the entire landing's content + prompts.

    ``angle_brief`` is optional free text from the user pre-committing to a
    direction. If absent, the LLM picks the strongest of 3 angles itself.
    """
    p = settings.profile
    system = (
        "You are a brand strategist writing a speculative campaign landing for a job "
        "candidate to attach to her outreach. The landing has 4 sticky-scroll chapters "
        "(hero, insight, manifesto, transition) followed by EXACTLY 6 execution cards "
        "and 4 KPIs. Your output must be cinematic-editorial in tone — think Monocle, "
        "Business of Fashion, Stripe Press. Never generic. Never AI-slop adjectives "
        "like 'innovative', 'cutting-edge', 'revolutionary', 'leverage', 'unleash'. "
        "Every paragraph earns its place. Every stat has a plausible source.\n\n"
        "You also write the IMAGE GENERATION PROMPTS used to make the hero video and "
        "the 6 execution cards. Image prompts must be photoreal, cinematic, 16:9 or "
        "4:3, concrete (specific places, specific times of day, specific products), "
        "and free of made-up logos.\n\n"
        "CRITICAL LANGUAGE RULE: ALL on-image text inside image-gen prompts must be "
        "in ENGLISH ONLY. This includes app UI mockups, OOH billboard taglines, price "
        "stickers, signage, and any readable copy. The applications are for international "
        "roles — every visual must read as native English. The ONLY exception is "
        "real-world signage in a foreign language that's contextually authentic to the "
        "location (e.g. 'PHARMACIE' on a real Paris pharmacy facade) — and even then "
        "only if it's incidental, never the headline.\n\n"
        "GRID RULE: exactly 6 executions, no more, no less. A 3+3 grid renders cleanly "
        "at desktop and 2-up on mobile; 4 cards leaves an ugly 3+1 trailing row."
    )
    user = (
        f"## Target role\n"
        f"{p['personal']['name']} is applying for {job.title} at {job.company} ({job.location}).\n"
        f"Score: {analysis.score}/100, tier {analysis.tier}.\n\n"
        f"## Job posting excerpt\n{(job.description or '')[:2500]}\n\n"
        f"## Brand identity (extracted from {brand.get('source','live site')})\n"
        f"Palette: {json.dumps(brand['palette'])}\n"
        f"Typography: {json.dumps(brand['typography'])}\n"
        f"Tone: {brand.get('tone')}\n"
        f"Logo hint: {brand.get('logo_hint')}\n\n"
        f"## Candidate differentiators (use sparingly, only where relevant)\n"
        f"- {p['headline']}\n"
        f"- UAE quick-commerce track (Noon, Talabat, Careem, Deliveroo)\n"
        f"- +30% GMV QoQ across 42 key accounts at Alibaba/Miravia\n"
        f"- Already in Dubai with residence visa\n\n"
    )
    if angle_brief:
        user += f"## User-chosen angle\n{angle_brief}\n\n"
    else:
        user += (
            "## Angle selection\nPick THE strongest single angle for this brand+role. "
            "Surface 2 alternates in `alt_angles` so the doc shows what was considered.\n\n"
        )
    user += "Use the submit_landing_content tool. All 4 executions, all 4 KPIs, all 7 prompts required."

    data = llm.generate_structured(
        system=system, user=user, tool_schema=_CONTENT_TOOL,
        tier="sonnet", max_tokens=4096, temperature=0.4,
    )
    if not data:
        raise RuntimeError("LLM returned no content")
    return LandingContent(**{k: v for k, v in data.items() if k in LandingContent.__dataclass_fields__})


# =====================================================================
# 3. Higgsfield orchestration
# =====================================================================

def _hf_run(args: list[str], label: str) -> dict:
    cmd = [str(HF_BIN)] + args + ["--wait", "--json"]
    logger.info("hf[%s] starting", label)
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if proc.returncode != 0:
        logger.error("hf[%s] failed: %s", label, proc.stderr[-500:])
        raise RuntimeError(f"hf.exe failed for {label}")
    out = proc.stdout.strip()
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        # tolerate per-line JSON
        last = [l for l in out.splitlines() if l.strip().startswith(("{", "["))]
        data = json.loads(last[-1]) if last else {}
    job = data[0] if isinstance(data, list) and data else data
    logger.info("hf[%s] done", label)
    return job


def _job_url(job: dict) -> str | None:
    for key in ("media_url", "result_url", "output_url", "url"):
        v = job.get(key)
        if isinstance(v, str) and v.startswith("http"):
            return v
    for r in (job.get("results") or job.get("outputs") or []):
        if isinstance(r, dict):
            for key in ("url", "media_url", "output_url"):
                v = r.get(key)
                if isinstance(v, str) and v.startswith("http"):
                    return v
    m = re.search(r"https?://[^\s\"']+\.(?:png|jpg|jpeg|webp|mp4)", json.dumps(job))
    return m.group(0) if m else None


def _download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = requests.get(url, timeout=180)
    r.raise_for_status()
    dest.write_bytes(r.content)


def _generate_image(prompt: str, dest: Path, *, aspect: str, label: str) -> None:
    if dest.exists():
        logger.info("hf[%s] cached, skipping", label)
        return
    job = _hf_run([
        "generate", "create", "gpt_image_2",
        "--prompt", prompt,
        "--aspect_ratio", aspect,
        "--resolution", "2k", "--quality", "high",
    ], label)
    url = _job_url(job)
    if not url:
        raise RuntimeError(f"No URL in hf response for {label}")
    _download(url, dest)


def _generate_hero_video(prompt: str, start: Path, end: Path, dest: Path, *, label: str) -> None:
    if dest.exists():
        logger.info("hf[%s] cached, skipping", label)
        return
    job = _hf_run([
        "generate", "create", "seedance_2_0",
        "--prompt", prompt,
        "--start-image", str(start),
        "--end-image", str(end),
        "--duration", "5",
        "--aspect_ratio", "16:9",
        "--resolution", "720p",
    ], label)
    url = _job_url(job)
    if not url:
        raise RuntimeError(f"No video URL for {label}")
    _download(url, dest)


def _extract_frames(mp4: Path, frames_dir: Path, *, n_frames: int = 149) -> None:
    if frames_dir.exists() and len(list(frames_dir.glob("frame_*.jpg"))) >= n_frames - 1:
        logger.info("ffmpeg: %d frames already on disk, skipping", n_frames)
        return
    import imageio_ffmpeg
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    frames_dir.mkdir(parents=True, exist_ok=True)
    probe = subprocess.run([ffmpeg, "-i", str(mp4)], capture_output=True, text=True, encoding="utf-8")
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", probe.stderr)
    duration = 5.0
    if m:
        duration = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    fps = n_frames / duration
    out = frames_dir / "frame_%04d.jpg"
    subprocess.run([
        ffmpeg, "-y", "-i", str(mp4),
        "-vf", f"fps={fps:.4f}",
        "-vframes", str(n_frames), "-q:v", "3", str(out),
    ], check=True, capture_output=True)
    logger.info("ffmpeg: extracted %d frames at %.2ffps", n_frames, fps)


# =====================================================================
# 4. HTML render — template strings
# =====================================================================

_INDEX_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="theme-color" content="{primary}">
  <title>{tagline_first} {tagline_accent} — {brand_name} x {parent}</title>
  <meta name="description" content="A speculative {brand_name} campaign concept by Paula De Francisco.">
  <meta property="og:title" content="{tagline_first} {tagline_accent} — {brand_name}">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family={display_font_url}&family={body_font_url}&family={serif_font_url}&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <nav class="top-nav">
    <div class="brand-mark">{brand_name} · {parent}</div>
    <div class="campaign-chip">{location_chip} · 2026</div>
  </nav>

  <section class="scrollstage" data-scrollstage
           data-frame-count="149" data-frame-dir="assets/frames" data-frame-ext="jpg">
    <div class="stage-sticky">
      <img class="hero-frame" src="assets/hero-keyframe-a.png" alt="Hero opening frame for {tagline_first}">
      <div class="stage-vignette"></div>
      <div class="hero-loading" data-frame-progress>Loading 0%</div>

      <div class="chapter chapter--hero" data-chapter data-chapter-start="0.00" data-chapter-end="0.22">
        <div class="chapter-kicker">A campaign concept for {brand_name} · {parent}</div>
        <h1 class="chapter-headline">{tagline_first}<br><span class="accent">{tagline_accent}</span></h1>
        <p class="chapter-sub">{insight_body}</p>
        <div class="chapter-scrollhint">scroll ↓</div>
      </div>

      <div class="chapter chapter--insight" data-chapter data-chapter-start="0.26" data-chapter-end="0.48">
        <div class="chapter-label">{insight_label}</div>
        <div class="huge-stat">{insight_stat}<span class="stat-pct">{insight_pct}</span></div>
        <p class="huge-body">{insight_body}</p>
        <p class="chapter-source">{insight_source}</p>
      </div>

      <div class="chapter chapter--manifesto" data-chapter data-chapter-start="0.52" data-chapter-end="0.78">
        <div class="chapter-label">The manifesto</div>
        <div class="manifesto-text">
{manifesto_paragraphs}
        </div>
      </div>

      <div class="chapter chapter--transition" data-chapter data-chapter-start="0.82" data-chapter-end="1.00">
        <div class="chapter-label">Now watch it happen</div>
        <h2 class="chapter-headline">{transition_first}<br><span class="accent">{transition_accent}</span></h2>
        <p class="chapter-sub">{transition_sub}</p>
      </div>
    </div>
  </section>

  <section class="executions" data-reveal>
    <h2 class="section-heading">Campaign executions</h2>
    <p class="section-sub">Four moves across the {location_chip} surface area.</p>
    <div class="executions-grid">
{execution_cards}
    </div>
  </section>

  <section class="kpis" data-reveal>
    <h2 class="section-heading">How we'd measure it</h2>
    <p class="section-sub">The four north-star KPIs for the 12-month activation.</p>
    <div class="kpis-grid">
{kpi_cards}
    </div>
  </section>

  <footer class="credits">
    <p class="credits-line">Proposed by <strong>Paula De Francisco</strong> — application for <em>{role}</em> at {company}.</p>
    <p class="credits-disclaimer">Fictional campaign concept. Not affiliated with or endorsed by {company} or any third party named here. Created as an application deliverable only.</p>
  </footer>

  <script src="scroll.js"></script>
</body>
</html>
"""


_EXEC_CARD = """      <article class="execution-card">
        <img class="execution-card-img" src="assets/executions/{slug}.jpg" alt="{title}" loading="lazy">
        <div class="execution-card-inner">
          <div class="execution-card-label">{label}</div>
          <div class="execution-card-title">{title}</div>
          <p class="execution-card-body">{body}</p>
          <div class="execution-card-foot">{foot}</div>
        </div>
      </article>"""


_KPI_CARD = """      <div class="kpi-card">
        <div class="kpi-value">{value}</div>
        <div class="kpi-label">{label}</div>
      </div>"""


def _font_url(name: str, weights: str) -> str:
    return name.replace(" ", "+") + ":wght@" + weights


def _render_index(content: LandingContent, brand: dict, job: Job, parent: str) -> str:
    manifesto_para = []
    for i, p in enumerate(content.manifesto):
        cls = ' class="manifesto-final"' if i == len(content.manifesto) - 1 else ""
        manifesto_para.append(f"          <p{cls}>{p}</p>")
    exec_cards = "\n".join(_EXEC_CARD.format(**ex) for ex in content.executions)
    kpi_cards = "\n".join(_KPI_CARD.format(**k) for k in content.kpis)
    typo = brand["typography"]
    return _INDEX_TEMPLATE.format(
        primary=brand["palette"]["primary"],
        brand_name=job.company,
        parent=parent,
        location_chip=job.location.split(",")[0].strip() or "Global",
        tagline_first=content.tagline_first,
        tagline_accent=content.tagline_accent,
        insight_label=content.insight_label,
        insight_stat=content.insight_stat,
        insight_pct=content.insight_pct,
        insight_body=content.insight_body,
        insight_source=content.insight_source,
        manifesto_paragraphs="\n".join(manifesto_para),
        transition_first=content.transition_first,
        transition_accent=content.transition_accent,
        transition_sub=content.transition_sub,
        execution_cards=exec_cards,
        kpi_cards=kpi_cards,
        role=job.title,
        company=job.company,
        display_font_url=_font_url(typo.get("display", "Manrope"), "500;700;800"),
        body_font_url=_font_url(typo.get("body", "Inter"), "400;500;700"),
        serif_font_url=_font_url(typo.get("serif", "Source Serif 4"), "400;500;600"),
    )


_STYLES_TEMPLATE_PATH = Path(__file__).parent / "_scroll_landing_styles.css.tmpl"


def _render_styles(brand: dict) -> str:
    """Substitute brand tokens in the Lipton-derived CSS template.

    We use ``str.replace`` rather than ``.format`` so unrelated CSS braces don't
    blow up. Tokens are spelled ``__TOKEN__`` in the template file.
    """
    base = _STYLES_TEMPLATE_PATH.read_text(encoding="utf-8")
    palette = brand["palette"]
    typo = brand["typography"]
    subs = {
        "__PRIMARY__":  palette["primary"],
        "__SECONDARY__": palette.get("secondary", "#0E0F12"),
        "__ACCENT__":   palette.get("accent", "#FFB400"),
        "__BG__":       palette.get("bg", "#FFFFFF"),
        "__TEXT__":     palette.get("text", "#0E0F12"),
        "__DARK__":     palette.get("dark", "#0F1A12"),
        "__DISPLAY__":  typo.get("display", "Manrope"),
        "__BODY__":     typo.get("body", "Inter"),
        "__SERIF__":    typo.get("serif", "Source Serif 4"),
    }
    for k, v in subs.items():
        base = base.replace(k, v)
    return base


_SCROLL_JS_PATH = Path(__file__).parent / "_scroll_landing_scroll.js"


def _render_angles_md(content: LandingContent, job: Job, brand: dict) -> str:
    out = [f"# {job.company} — Campaign Angles",
           "",
           f"Job: **{job.title}** @ {job.company} ({job.location}) · job_id `{job.id}`",
           f"Brand source: {brand.get('source','—')}",
           f"Generated: scroll_landing.py",
           "",
           f"## Angle 1 — {content.angle_name} ★ CHOSEN",
           "",
           f"- **Tagline**: {content.tagline_first} {content.tagline_accent}.",
           f"- **Insight**: {content.insight_body} ({content.insight_source})",
           f"- **KPIs**: " + " · ".join(f"{k['value']} {k['label'].replace(chr(60)+'br'+chr(62),' ')}" for k in content.kpis),
           ""]
    for i, alt in enumerate(content.alt_angles or [], start=2):
        out += [f"## Angle {i} — {alt.get('name','')} (alternate)",
                "",
                f"- **Tagline**: {alt.get('tagline','')}",
                f"- **Insight**: {alt.get('insight','')}",
                f"- **Hero**: {alt.get('hero','')}",
                f"- **KPI**: {alt.get('kpi','')}",
                ""]
    return "\n".join(out)


# =====================================================================
# 5. Top-level builder
# =====================================================================

def build_landing(
    job: Job,
    analysis: JobAnalysis,
    *,
    brand_url: str,
    parent_brand_name: str | None = None,
    angle_brief: str | None = None,
    landings_root: Path | None = None,
) -> Path:
    """End-to-end: extract brand → propose content → Higgsfield → frames → HTML.

    Returns the path to the generated ``index.html``.
    """
    landings_root = landings_root or (settings.output_dir / "landings")
    landings_root.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+", "-", job.company.lower()).strip("-")
    landing_dir = landings_root / f"landing_{slug}"
    assets = landing_dir / "assets"
    assets.mkdir(parents=True, exist_ok=True)

    # 1. Brand
    logger.info("phase 1: extracting brand from %s", brand_url)
    brand = extract_brand_from_url(brand_url)
    brand["name"] = job.company
    if parent_brand_name:
        brand["parent"] = parent_brand_name
    (landing_dir / "brand.json").write_text(
        json.dumps(brand, indent=2, ensure_ascii=False), encoding="utf-8")

    # 2. Content + prompts
    logger.info("phase 2: proposing landing content via LLM")
    content = propose_landing_content(job, analysis, brand, angle_brief=angle_brief)

    # 3. Higgsfield: keyframes + hero video + 4 executions
    logger.info("phase 3: Higgsfield generation")
    kfa = assets / "hero-keyframe-a.png"
    kfb = assets / "hero-keyframe-b.png"
    _generate_image(content.keyframe_a_prompt, kfa, aspect="16:9", label=f"{slug} kfA")
    _generate_image(content.keyframe_b_prompt, kfb, aspect="16:9", label=f"{slug} kfB")
    mp4 = assets / "hero-loop.mp4"
    _generate_hero_video(content.hero_video_prompt, kfa, kfb, mp4, label=f"{slug} hero")

    # Execution images — parallel
    execs_dir = assets / "executions"
    execs_dir.mkdir(exist_ok=True)
    def _gen_exec(ex):
        path = execs_dir / f"{ex['slug']}.jpg"
        _generate_image(ex["image_prompt"], path, aspect="4:3", label=f"{slug} {ex['slug']}")
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(_gen_exec, content.executions))

    # 4. Frames
    logger.info("phase 4: frame extraction")
    _extract_frames(mp4, assets / "frames")

    # 5. HTML/CSS/JS
    logger.info("phase 5: rendering HTML/CSS/JS")
    parent = parent_brand_name or brand.get("parent") or job.company
    (landing_dir / "index.html").write_text(
        _render_index(content, brand, job, parent), encoding="utf-8")
    (landing_dir / "styles.css").write_text(_render_styles(brand), encoding="utf-8")
    (landing_dir / "scroll.js").write_text(
        _SCROLL_JS_PATH.read_text(encoding="utf-8"), encoding="utf-8")
    (landing_dir / "ANGLES.md").write_text(
        _render_angles_md(content, job, brand), encoding="utf-8")

    logger.info("landing built: %s", landing_dir)
    return landing_dir / "index.html"
