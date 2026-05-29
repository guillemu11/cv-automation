"""End-to-end driver for the Opella Brand Manager application pack.

This script:
  1. Loads the injected Opella job from scored_jobs.json.
  2. Patches settings.llm_provider -> 'anthropic' (the .env default is
     'chatqueue' which would block on human-in-chat replies).
  3. Generates: CV, cover letter, all 4 deliverables, landing pitch.

Run after scripts/_inject_opella.py.
"""
from __future__ import annotations

import json
import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# Patch provider BEFORE anything else imports settings transitively.
from career_ops.config import settings

settings.llm_provider = "anthropic"
print(f"[setup] llm_provider patched -> {settings.llm_provider}")

from career_ops.analyzer import JobAnalysis  # noqa: E402
from career_ops.discovery.normalize import Job  # noqa: E402
from career_ops.generators import generate_cover_letter, generate_cv  # noqa: E402
from career_ops.generators.deliverables import (  # noqa: E402
    DELIVERABLE_TYPES,
    generate_deliverable,
)
from career_ops.generators.landing_generator import generate_landing  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-5s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

OPELLA_ID_PREFIX = "f324f5af0ff41e06"


def _load_opella():
    path = settings.data_dir / "scored_jobs.json"
    scored = json.loads(path.read_text(encoding="utf-8"))
    rec = next((r for r in scored if r.get("id", "").startswith(OPELLA_ID_PREFIX)), None)
    if not rec:
        raise SystemExit(f"Opella job not found ({OPELLA_ID_PREFIX}) — run _inject_opella.py first")
    job = Job(
        id=rec["id"],
        title=rec.get("title", ""),
        company=rec.get("company", ""),
        location=rec.get("location", ""),
        url=rec.get("url", ""),
        source=rec.get("source", "linkedin"),
        description=rec.get("description", ""),
        salary_raw=rec.get("salary_raw"),
    )
    analysis = JobAnalysis(
        score=rec.get("ai_score", 50),
        tier=rec.get("ai_tier", "Warm"),
        skills_match=rec.get("skills_match", []),
        missing_skills=rec.get("missing_skills", []),
        sector_fit=rec.get("sector_fit", ""),
        seniority_fit=rec.get("seniority_fit", ""),
        red_flags=rec.get("red_flags", []),
        ats_keywords=rec.get("ats_keywords", []),
        reasoning=rec.get("reasoning", ""),
    )
    return job, analysis


def main() -> None:
    job, analysis = _load_opella()
    print(f"[start] {job.title} @ {job.company} (id={job.id}, tier={analysis.tier})")

    import os
    skip_cv_cl = os.getenv("SKIP_CV_CL", "false").lower() == "true"

    if skip_cv_cl:
        print("\n[1/7] CV: SKIPPED (already generated)")
        print("[2/7] CL: SKIPPED (already generated)")
    else:
        # 1) CV
        print("\n[1/7] CV...")
        cv_path = generate_cv(job, analysis)
        print(f"  CV: {cv_path}")

        # 2) Cover letter
        print("\n[2/7] Cover letter...")
        cl_path = generate_cover_letter(job, analysis)
        print(f"  CL: {cl_path}")

    # 3-6) Deliverables (all 4 types)
    for i, dtype in enumerate(DELIVERABLE_TYPES, start=3):
        print(f"\n[{i}/7] Deliverable: {dtype}...")
        try:
            path = generate_deliverable(job, analysis, deliverable_type=dtype)
            print(f"  -> {path}")
        except Exception as exc:  # noqa: BLE001
            print(f"  FAILED: {exc}")

    # 7) Landing
    print("\n[7/7] Landing pitch...")
    try:
        landing_dir = generate_landing(job, analysis)
        print(f"  -> {landing_dir}")
    except Exception as exc:  # noqa: BLE001
        print(f"  FAILED: {exc}")

    print("\nAll done.")


if __name__ == "__main__":
    main()
