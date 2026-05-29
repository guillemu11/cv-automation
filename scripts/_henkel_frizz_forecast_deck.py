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

# Consumed by slide_why_paula() and slide_contact() (added in later tasks)
P = settings.profile["personal"]
CHANNEL_IMAGES = ["hero", "creator", "instore", "pharmacy", "marketplace", "qcommerce", "retailmedia"]

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


def stage_assets() -> None:
    """Copy the channel images and Paula's photo into the build dir."""
    if not LANDING_ASSETS.is_dir():
        raise FileNotFoundError(
            f"Landing assets not found: {LANDING_ASSETS}\n"
            "Run the Schwarzkopf landing build first."
        )
    if not PAULA_PHOTO.exists():
        raise FileNotFoundError(f"Paula's photo not found: {PAULA_PHOTO}")
    BUILD_ASSETS.mkdir(parents=True, exist_ok=True)
    for name in CHANNEL_IMAGES:
        shutil.copyfile(LANDING_ASSETS / f"{name}.jpg", BUILD_ASSETS / f"{name}.jpg")
    shutil.copyfile(PAULA_PHOTO, BUILD_ASSETS / "paula.jpg")


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


def render_pdf(html_path: Path, pdf_path: Path) -> None:  # replaced in Task 8
    raise NotImplementedError


def merge_pdfs(deck_pdf: Path, appendix_pdf: Path, out_pdf: Path) -> None:  # replaced in Task 9
    raise NotImplementedError


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html-only", action="store_true", help="Write deck.html and stop (no PDF).")
    args = ap.parse_args()

    stage_assets()
    HTML_PATH.parent.mkdir(parents=True, exist_ok=True)
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
