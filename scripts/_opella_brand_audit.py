"""Audit: pull REAL brand identities for Opella + Buscopan + Doliprane via
Firecrawl ``formats: ["branding"]`` and compare against the palettes I made up
when generating the scroll landings.

This is the missing Phase 1 of the campaign-landing skill — I skipped it on
the first pass and used the product-pack colors from memory. Per the skill
rule: sub-brands extract from their own site, not the parent's.

Outputs:
  output/landings/_brand_audit.json — per-target {our_palette, real_palette, diff}
  Prints a side-by-side comparison so we can decide whether to regenerate.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings

TARGETS = [
    {
        "slug": "opella_parent",
        "url": "https://www.opella.com/",
        "our_brand_json": None,  # no landing exists for parent
    },
    {
        "slug": "buscopan",
        "url": "https://www.buscopan.com/",
        "our_brand_json": ROOT / "output" / "landings" / "landing_opella_buscopan" / "brand.json",
    },
    {
        "slug": "doliprane",
        "url": "https://www.doliprane.fr/",
        "our_brand_json": ROOT / "output" / "landings" / "landing_opella_doliprane" / "brand.json",
    },
]

FIRECRAWL_URL = "https://api.firecrawl.dev/v2/scrape"


def firecrawl_branding(url: str) -> dict:
    """Hit Firecrawl ``formats: ["branding"]``. Returns the raw JSON payload
    (or an ``{"error": ...}`` dict on failure)."""
    r = requests.post(
        FIRECRAWL_URL,
        headers={
            "Authorization": f"Bearer {settings.firecrawl_api_key}",
            "Content-Type": "application/json",
        },
        json={"url": url, "formats": ["branding"]},
        timeout=90,
    )
    if r.status_code != 200:
        return {"error": f"HTTP {r.status_code}: {r.text[:300]}"}
    return r.json()


def main() -> None:
    out_path = ROOT / "output" / "landings" / "_brand_audit.json"
    report = []
    for tgt in TARGETS:
        slug = tgt["slug"]
        url = tgt["url"]
        print(f"\n=== {slug} ({url}) ===")
        raw = firecrawl_branding(url)
        if "error" in raw:
            print(f"  Firecrawl error: {raw['error']}")
            report.append({"slug": slug, "url": url, "error": raw["error"]})
            continue
        # The branding format lives under data.branding in v2.
        data = raw.get("data") or raw
        branding = data.get("branding") or {}
        # Print a digest
        colors = branding.get("colors") or branding.get("palette") or {}
        fonts = branding.get("fonts") or {}
        logos = branding.get("logos") or branding.get("logo") or []
        print(f"  Colors keys: {list(colors)[:8]}")
        print(f"  Fonts keys:  {list(fonts)[:8]}")
        print(f"  Logos: {len(logos) if isinstance(logos, list) else 'n/a'}")
        entry = {"slug": slug, "url": url, "real": branding}

        ours_path = tgt.get("our_brand_json")
        if ours_path and ours_path.exists():
            ours = json.loads(ours_path.read_text(encoding="utf-8"))
            entry["ours"] = ours.get("palette", {})
            print(f"  Our palette: {entry['ours']}")
        report.append(entry)

    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
