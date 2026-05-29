#!/usr/bin/env python3
"""Prep for chat-driven autofill test (2026-05-29).

A. Inject the 5 conversational Indeed finds into data/scored_jobs.json so the
   dashboard/API can reconstruct them and the Autofill button works.
B. (done in runner.py) recursive file resolution.
C. Pre-generate Henkel's FORM_Paula_*.json via llm.override so the only
   chatqueue call left at autofill time is the live field-mapping (serviced
   from the chat).

Importing _run_2026_05_29 reuses the exact Job + JobAnalysis objects already
authored there (and sets output_dir to output/2026-05-29 as a side effect).
"""
from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import _run_2026_05_29 as gen  # noqa: E402  (sets settings.output_dir = output/2026-05-29)
from career_ops import llm  # noqa: E402
from career_ops.config import settings  # noqa: E402
from career_ops.generators.form_responses import generate_form_responses  # noqa: E402

SCORED = settings.data_dir / "scored_jobs.json"


# ---------------------------------------------------------------
# A. Inject jobs
# ---------------------------------------------------------------

def inject_jobs() -> None:
    existing = json.loads(SCORED.read_text(encoding="utf-8")) if SCORED.exists() else []
    by_id = {j.get("id") for j in existing}
    added = 0
    for spec in gen.JOBS:
        job = spec["job"]
        an = spec["analysis"]
        if job.id in by_id:
            print(f"  skip (already present): {job.id}")
            continue
        jd = asdict(job)
        entry = {
            **jd,
            "ai_score": an.score,
            "ai_tier": an.tier,
            "skills_match": an.skills_match,
            "missing_skills": an.missing_skills,
            "sector_fit": an.sector_fit,
            "seniority_fit": an.seniority_fit,
            "red_flags": an.red_flags,
            "ats_keywords": an.ats_keywords,
            "reasoning": an.reasoning,
            "scored_by": "claude:buscar-trabajos",
            "freshness": "fresh",
            "discovered_at": "2026-05-29T00:00:00+00:00",
            "status": "CV Ready",
        }
        existing.append(entry)
        added += 1
        print(f"  added: {job.id}  ({job.company} - {job.title})")
    SCORED.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"injected {added} job(s); scored_jobs.json now has {len(existing)} entries")


# ---------------------------------------------------------------
# C. Pre-generate Henkel FORM responses (I author them)
# ---------------------------------------------------------------

HENKEL_FORM = {
    "current_title": "Brand & Marketing Manager",
    "years_of_experience": "4+ years",
    "current_company": "DoFreeze LLC",
    "notice_period": "30 days",
    "why_interested": (
        "Henkel's leadership in Modern Trade across the GCC and its Perfect Store ambition map "
        "directly to what I do every day. As Brand & Marketing Manager at a Dubai-based FMCG "
        "distributor operating in 50+ markets, I build trade and shopper plans by channel and would "
        "love to bring that hands-on GCC experience to Henkel's portfolio."
    ),
    "why_good_fit": (
        "I develop trade and shopper marketing plans by channel and turn them into customer plans "
        "with the sales team. At Alibaba's Miravia I managed 42 key accounts and grew GMV +30% QoQ "
        "through pricing, assortment and promotions, and led category expansion as PIC Fragrances "
        "(30+ stores in two months). At DoFreeze I run A&P budgets to ROI and lead NPD go-to-market "
        "end-to-end across six launches — exactly the trade, shopper and category remit of this role."
    ),
    "greatest_achievement": (
        "Growing GMV +30% quarter-over-quarter across 42 key accounts at Miravia (Alibaba) by "
        "rebuilding pricing, assortment and promotional strategy — while simultaneously leading the "
        "Fragrances category expansion that onboarded 30+ new stores in two months."
    ),
    "salary_expectation": "AED 22,000 - 28,000 per month",
    "availability": "Available to start within 30 days",
    "additional_qa": [
        {"question": "How did you hear about this position?",
         "answer": "Through Indeed / Henkel's careers listing."},
        {"question": "Are you legally authorized to work in the UAE?",
         "answer": "Yes — I hold a UAE Residence Visa and am already based in Dubai."},
        {"question": "Will you now or in the future require sponsorship for employment visa status?",
         "answer": "No. I have a valid UAE Residence Visa, so no sponsorship is required."},
        {"question": "Are you willing to relocate?",
         "answer": "No relocation needed — I am already based in Dubai, UAE."},
        {"question": "Do you have experience in the FMCG industry?",
         "answer": "Yes — currently FMCG at DoFreeze (Befit, Eurocake, Flair) and a category-planning "
                   "foundation at Mondelez, plus beauty/fragrance e-commerce at Alibaba's Miravia."},
        {"question": "Do you have experience with GCC Modern Trade and key retailers?",
         "answer": "Yes — I integrate brands into UAE modern trade and quick-commerce (Noon, Talabat, "
                   "Careem, Deliveroo) and build channel/customer plans across GCC and MENA markets."},
        {"question": "Are you willing to undergo a background check?",
         "answer": "Yes, I am happy to undergo a standard background check."},
        {"question": "Please describe your experience managing cross-functional projects.",
         "answer": "I lead NPD launches end-to-end, coordinating brief, packaging, pricing and "
                   "go-to-market across marketing, sales, supply chain and finance in 50+ markets."},
    ],
}


def pregen_henkel_form() -> None:
    spec = next(s for s in gen.JOBS if s["job"].company == "Henkel")
    job, analysis = spec["job"], spec["analysis"]
    with llm.override({"submit_form_responses": HENKEL_FORM}):
        result = generate_form_responses(job, analysis, ats_platform="generic")
    if result:
        jpath, ppath = result
        print(f"FORM json: {jpath}")
        print(f"FORM pdf:  {ppath}")
    else:
        print("FORM generation FAILED")


if __name__ == "__main__":
    print("== A. Injecting jobs into scored_jobs.json ==")
    inject_jobs()
    print("\n== C. Pre-generating Henkel FORM responses ==")
    pregen_henkel_form()
    print("\nPrep done.")
