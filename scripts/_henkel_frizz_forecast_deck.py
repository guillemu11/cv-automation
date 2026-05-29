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


def build_html() -> str:
    return "<!DOCTYPE html><html><body>stub</body></html>"


def render_pdf(html_path: Path, pdf_path: Path) -> None:  # replaced in Task 8
    raise NotImplementedError


def merge_pdfs(deck_pdf: Path, appendix_pdf: Path, out_pdf: Path) -> None:  # replaced in Task 9
    raise NotImplementedError


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
