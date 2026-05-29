"""Smoke test for career_ops.generators.scroll_landing.

Runs ONLY phases 1, 2, and 5 (brand extraction + LLM content proposal +
HTML/CSS rendering). Skips the Higgsfield image/video generation so we can
validate the wiring without burning credits.

Picks the Deliveroo Marketing Manager job from scored_jobs.json as the
non-Opella validation case.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.analyzer import JobAnalysis
from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import scroll_landing

# Force Anthropic — .env has chatqueue which blocks for human reply
settings.llm_provider = "anthropic"

JOB_ID = "43127902da4f"  # Deliveroo Marketing Manager, HOP and Retail


def main() -> None:
    scored = json.loads((settings.data_dir / "scored_jobs.json").read_text(encoding="utf-8"))
    rec = next(r for r in scored if r["id"].startswith(JOB_ID))
    job = Job(id=rec["id"], title=rec["title"], company=rec["company"],
              location=rec["location"], url=rec.get("url", ""),
              source=rec.get("source", "linkedin"), description=rec.get("description", ""))
    analysis = JobAnalysis(score=rec.get("ai_score", 50), tier=rec.get("ai_tier", "Warm"),
                           skills_match=rec.get("skills_match", []),
                           missing_skills=rec.get("missing_skills", []),
                           sector_fit=rec.get("sector_fit", ""),
                           seniority_fit=rec.get("seniority_fit", ""),
                           red_flags=rec.get("red_flags", []),
                           ats_keywords=rec.get("ats_keywords", []),
                           reasoning=rec.get("reasoning", ""))

    print(f"=== Smoke test: {job.title} @ {job.company} ===\n")

    # Phase 1
    brand_url = "https://deliveroo.ae/"
    print(f"[1] extract_brand_from_url({brand_url})")
    brand = scroll_landing.extract_brand_from_url(brand_url)
    brand["name"] = job.company
    brand["parent"] = job.company
    print(f"    palette  = {brand['palette']}")
    print(f"    typo     = {brand['typography']}")
    print(f"    source   = {brand.get('source')}")
    print(f"    tone     = {brand.get('tone')}\n")

    # Phase 2
    print("[2] propose_landing_content (one structured LLM call)")
    content = scroll_landing.propose_landing_content(job, analysis, brand)
    print(f"    angle_name = {content.angle_name}")
    print(f"    tagline    = '{content.tagline_first} {content.tagline_accent}'")
    print(f"    insight    = '{content.insight_stat}{content.insight_pct}' — {content.insight_body[:80]}...")
    print(f"    executions = {len(content.executions)} cards: " + ", ".join(e['slug'] for e in content.executions))
    print(f"    kpis       = {len(content.kpis)}\n")

    # Phase 5 — render HTML/CSS/ANGLES.md to a temp dir, no Higgsfield
    out_dir = settings.output_dir / "landings" / "_smoke_test_deliveroo"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "assets").mkdir(exist_ok=True)
    (out_dir / "assets" / "frames").mkdir(exist_ok=True)
    (out_dir / "assets" / "executions").mkdir(exist_ok=True)
    (out_dir / "brand.json").write_text(json.dumps(brand, indent=2, ensure_ascii=False), encoding="utf-8")
    (out_dir / "index.html").write_text(
        scroll_landing._render_index(content, brand, job, brand.get("parent", job.company)),
        encoding="utf-8")
    (out_dir / "styles.css").write_text(scroll_landing._render_styles(brand), encoding="utf-8")
    (out_dir / "scroll.js").write_text(scroll_landing._SCROLL_JS_PATH.read_text(encoding="utf-8"), encoding="utf-8")
    (out_dir / "ANGLES.md").write_text(scroll_landing._render_angles_md(content, job, brand), encoding="utf-8")

    print(f"[5] rendered into {out_dir}")
    print(f"    open {out_dir / 'index.html'}")
    print("    (note: hero/exec images NOT generated — this is content+render smoke test only)")
    print("\nIf this looks right, run the real CLI to generate images:")
    print(f"  python scripts/scroll_landing_for_job.py --job-id {JOB_ID} --brand-url {brand_url} --provider anthropic")


if __name__ == "__main__":
    main()
