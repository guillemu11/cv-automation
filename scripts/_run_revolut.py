#!/usr/bin/env python3
"""One-off: value-add deliverable for Revolut — Marketing Manager (Brand), UAE (2026-06-23).

Honest positioning: Revolut is fintech (sector stretch for Paula). The deliverable
leans on transferable strengths — go-to-market, full-funnel performance, AI
automation, localisation, marketplace growth — without claiming fintech experience.
"""
from __future__ import annotations

import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops import llm
from career_ops.analyzer import JobAnalysis
from career_ops.config import settings
from career_ops.discovery.normalize import Job, job_hash
from career_ops.generators import generate_deliverable

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)-5s  %(message)s", datefmt="%H:%M:%S")

settings.output_dir = ROOT / "output" / "2026-06-23"
settings.output_dir.mkdir(parents=True, exist_ok=True)

job = Job(
    id=job_hash("Marketing Manager (Brand)", "Revolut", "Dubai, UAE"),
    title="Marketing Manager (Brand)",
    company="Revolut",
    location="Dubai, UAE",
    url="https://to.indeed.com/aamfmtl9cvwp",
    source="indeed",
    description=(
        "Marketing Manager to lead Revolut's brand and growth efforts in the UAE. Own local campaign "
        "development, refine market positioning, and launch initiatives that bring features to life. "
        "Partner with regional leadership and global marketing. Drive impactful go-to-market product "
        "launches owning audience strategy, messaging and communications. Develop research plans to "
        "uncover customer insights and validate roadmaps. Build market-leading campaign calendars across "
        "the full funnel, acquisition to retention. Own tone of voice and adapt global campaigns to local "
        "nuances. Run experiments to test hypotheses with analytical rigour. 5+ years B2C marketing in a "
        "fast-paced hyper-growth global tech company; knowledge of fintech/payments; data-into-insight skill."
    ),
)

analysis = JobAnalysis(
    score=58, tier="Warm",
    skills_match=["go-to-market", "campaign development", "audience & messaging", "full-funnel growth", "experiments / data-led", "localisation", "generative AI automation"],
    missing_skills=["fintech / payments sector knowledge", "hyper-growth tech B2C tenure"],
    sector_fit="Fintech (outside Paula's FMCG/beauty/e-commerce core)",
    seniority_fit="Manager-level fit on craft; sector is a transferable stretch",
    red_flags=["fintech sector + hyper-growth-tech requirement"],
    ats_keywords=["brand", "growth", "go-to-market", "campaign", "full funnel", "experiments", "positioning", "customer insights", "localisation"],
    reasoning="Brand+growth craft maps well (go-to-market, full-funnel, experiments, AI automation, +30% GMV); fintech sector is the gap, handled transparently.",
)

deliverable = {
    "title": "Revolut UAE — Brand & Growth Lens",
    "subtitle": "Three observations on building Revolut's brand and growth in the UAE, from a go-to-market and performance marketer.",
    "sections": [
        {
            "heading": "Localise the story, not just the campaign",
            "finding": "Revolut wins markets by adapting global campaigns to local nuances — and the UAE has very specific money moments: remittances for a large expat base, travel and multi-currency FX, and everyday spend.",
            "insight": "A generic 'global super-app' message converts worse here than a story anchored on the use cases UAE customers feel daily — sending money home, spending abroad without the FX sting.",
            "recommendation": "Lead the UAE go-to-market with remittance and travel-FX as the hero narrative, with audience and messaging built per segment — exactly the local-adaptation and go-to-market ownership I do across 50+ markets at DoFreeze.",
        },
        {
            "heading": "Brand that pays back through the full funnel",
            "finding": "This role bridges brand and growth — awareness through to retention — yet brand work is often measured on reach while growth lives on CAC, activation and repeat.",
            "insight": "Brand campaigns that aren't wired to install → activation → retention spend without compounding; the ones that are turn awareness into measurable acquisition.",
            "recommendation": "Build the UAE campaign calendar across the full funnel with clear activation and retention hooks, measured end-to-end — drawing on the Meta/Google performance marketing I run to ROI/ROAS and the marketplace growth (+30% GMV QoQ) behind my track record.",
        },
        {
            "heading": "Experiment-led, with AI doing the heavy lifting",
            "finding": "Revolut prizes analytical rigour, experiments and turning data into compelling conversion stories — at hyper-growth speed.",
            "insight": "The marketers who keep up pair a real test-and-learn cadence with automation, so insight-to-campaign cycle time shrinks instead of bottlenecking on manual work.",
            "recommendation": "Stand up a weekly test-and-learn loop and use AI to accelerate it — I built a generative-AI marketing automation system (Claude) that cut manual campaign-planning and reporting workload ~40%, a rare edge for a fast-moving growth team.",
        },
    ],
    "closing": (
        "These are outside-in observations; with Revolut's UAE customer and performance data I'd pressure-test them "
        "fast. I'm transparent that fintech isn't my home sector — but the brand-and-growth craft here (localised "
        "go-to-market, full-funnel measurement, experiment-led, AI-accelerated) is exactly how I work."
    ),
}

with llm.override({"submit_deliverable": deliverable}):
    path = generate_deliverable(job, analysis, deliverable_type="brand_analysis")

print("\n========== REVOLUT DELIVERABLE ==========")
print("Deliverable:", path)
