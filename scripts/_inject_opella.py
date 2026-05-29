"""One-shot: inject the Opella Brand Manager (Dubai) LinkedIn posting into the
pipeline as if discovery had picked it up.

Paula saw this job on LinkedIn but the daily discovery missed it. We construct
a normalized Job, score it with the configured LLM provider, and append it to
``data/scored_jobs.json`` so the rest of the system (dashboard, generators,
contact finder) treats it as a regular job.

Run once. Idempotent — if the job_id already exists in scored_jobs.json, it
is left untouched.
"""
from __future__ import annotations

import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.analyzer import JobAnalysis
from career_ops.config import settings
from career_ops.discovery.normalize import Job

OPELLA_URL = (
    "https://www.linkedin.com/jobs/search-results/?currentJobId=4417095540"
)

OPELLA_DESCRIPTION = """Opella is the self-care challenger with the purest and third-largest portfolio in the Over-The-Counter (OTC) & Vitamins, Minerals & Supplements (VMS) market globally.

Our mission: to bring health in people's hands by making self-care as simple as it should be for over half a billion consumers worldwide.

At the core of this mission is our 100+ loved brands, our 11,000-strong global team, our 13 best-in-class manufacturing sites and four specialized science and innovation development centers.

Headquartered in France, Opella is the proud maker of many of the world's most loved brands, including Allegra, Buscopan, Doliprane, Dulcolax, Enterogermina, Essentiale and Mucosolvan.

B Corp certified in multiple markets, we are active players in the journey towards healthier people and planet.

About The Job

You'll be driving a global brand and our team is committed to driving its growth through bold ideas, data-driven strategies, and consumer-centric thinking. We work cross-functionally with medical, digital, commercial, and regional teams to ensure our brand not only leads in market share but also in relevance and trust.

You'll be part of a collaborative, agile, and forward-thinking environment where creativity meets executional excellence. We challenge conventions, celebrate innovation, and support each other to deliver impactful brand experiences that improve lives.

Main Responsibilities
- Provide strategic leadership for the brand and manage resource allocation across brand strategies and tactics.
- Identify profitable and relevant brand growth opportunities and allocate budgets accordingly.
- Sign-off on brand ATL and BTL investments.
- Lead, evaluate, and ensure implementation of strategic growth plans to achieve above-market growth and sales/profitability objectives.
- Drive brand analytics, market and competition understanding, and integrated planning processes.
- Execute key initiatives driving brand growth.
- Identify high ROI initiatives to drive best-performing brand activations.

About You
- University degree in business, marketing, or a scientific discipline.
- Proven experience as a Brand Manager in creating and developing brand strategy.
- Experience in Consumer Healthcare or FMCG companies with a proven track record in marketing positions.
- Strong leadership and project management skills, with a focus on executional excellence.
- Strategic, integrative, and analytical thinking.
- Autonomy and ability to balance long-term strategic priorities with short-term business needs.
- Creative problem-solver who thrives in agile, collaborative environments.
- Fluent in English and Arabic.
- Experience in UAE market.
"""


def main() -> str:
    job = Job.build(
        title="Brand Manager",
        company="Opella",
        location="Dubai, United Arab Emirates",
        url=OPELLA_URL,
        source="linkedin",
        description=OPELLA_DESCRIPTION,
        posted_date=date.today(),
        raw={
            "linkedin_job_id": "4417095540",
            "applicants": "215+",
            "promoted": True,
            "manually_injected": True,
        },
    )
    print(f"Built job: id={job.id}  title={job.title}  company={job.company}")

    path = settings.data_dir / "scored_jobs.json"
    existing: list[dict] = []
    if path.exists():
        existing = json.loads(path.read_text(encoding="utf-8"))

    if any(r.get("id") == job.id for r in existing):
        print(f"Job {job.id} already in scored_jobs.json — skipping injection.")
        return job.id

    # Manual JobAnalysis — Paula already decided to apply; no need to spend
    # an LLM call. Values reflect that this is a near-perfect fit for her
    # profile (FMCG + Consumer Healthcare + Brand Manager + Dubai), with the
    # Arabic language requirement noted as a gap.
    analysis = JobAnalysis(
        score=88,
        tier="Hot",
        skills_match=[
            "Brand management (4+ years FMCG/Beauty)",
            "Brand P&L ownership",
            "ATL & BTL investment sign-off",
            "Integrated campaign management",
            "Brand analytics & competition understanding",
            "Strategic & analytical thinking",
            "Project management (cross-functional)",
            "UAE market experience (already living in Dubai)",
            "Fluent English",
            "FMCG track record (Mondelez, Inditex)",
            "Quick-commerce + e-commerce execution (Noon, Talabat, Careem, Deliveroo)",
            "Consumer-centric thinking",
            "Agile, collaborative environment fit",
        ],
        missing_skills=[
            "Fluent Arabic",
            "Direct Consumer Healthcare / OTC / VMS category experience",
        ],
        sector_fit="adjacent",
        seniority_fit="exact",
        red_flags=[
            "Arabic fluency listed as a requirement — Paula is Spanish/English only",
            "215+ applicants in first 24h — very competitive funnel",
        ],
        ats_keywords=[
            "Brand Manager",
            "OTC",
            "VMS",
            "Vitamins Minerals Supplements",
            "Consumer Healthcare",
            "Self-care",
            "FMCG",
            "ATL",
            "BTL",
            "Brand P&L",
            "Brand strategy",
            "Brand growth",
            "Resource allocation",
            "Budget allocation",
            "Brand analytics",
            "Integrated planning",
            "Market share",
            "ROI",
            "Cross-functional",
            "UAE market",
            "Dubai",
            "Above-market growth",
        ],
        reasoning=(
            "Near-perfect role+seniority+geography match. Brand Manager in UAE with FMCG "
            "background is exactly Paula's track. Two gaps: (1) Arabic — non-negotiable on "
            "the JD; (2) Consumer Healthcare/OTC vs. her FMCG/Beauty/Quick-commerce base. "
            "Pitch must over-index on UAE quick-commerce expertise + brand P&L delivery to "
            "compensate."
        ),
        scored_by="manual:paula-decision",
    )
    print(f"  -> score={analysis.score} tier={analysis.tier} (manual scoring)")

    rec = job.to_dict()
    a = analysis.to_dict()
    rec["ai_score"] = a.pop("score", 0)
    rec["ai_tier"] = a.pop("tier", "Warm")
    rec.update(a)
    rec["freshness"] = "fresh"
    rec["discovered_at"] = datetime.now(timezone.utc).isoformat()

    existing.append(rec)
    path.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Appended to {path.name}. Total jobs now: {len(existing)}")
    print(f"\nJOB_ID={job.id}")
    return job.id


if __name__ == "__main__":
    main()
