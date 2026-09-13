"""One-off: CV + cover letter for Nestlé MENA — NesTalent Marketing Graduate
Trainee (2026-08-15), Dubai.

Honest positioning (same playbook as the Puig Marketing Graduate one-off):
Paula is OVER-qualified — this programme targets fresh graduates with "limited
work experience". We do NOT pretend she is a fresh grad. We lead on her degree
(CUNEF Business Administration, Marketing-heavy, 9.5/10 thesis = the "very good
GPA, BBA with Marketing concentration" ask), her genuine FMCG passion, and the
fact that every rotation theme (brand innovation, brand experiences, consumer
insights) maps to real work she already does. Mondelez is the strongest hook —
global food FMCG, a structured Trainee programme, NPD (Milka) — i.e. a direct
Nestlé analogue. The cover letter addresses the over-experience head-on.

Content is authored directly (no LLM key in this repo) and kept strictly
truthful — NO invented experience. Fills the real CV + cover-letter templates,
converts to PDF, and lands the package under
output/2026-08-15/Nestle MENA - NesTalent Marketing Graduate Trainee/.
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cover_letter as cl
from career_ops.generators import cv_generator as cv

COMPANY = "Nestle MENA"
TITLE = "NesTalent Marketing Graduate Trainee"
DATE_FOLDER = "2026-08-15"

JOB_DESCRIPTION = """\
NesTalent Marketing Graduate Trainee — Nestlé Middle East and North Africa (MENA), Dubai.

NesTalent is a fast-track development programme that nurtures future leaders across the
key business areas of Nestlé MENA. As a Marketing Graduate Trainee you begin an immersive
journey into Nestlé's categories: with guidance from experienced professionals you gain
exposure to diverse marketing streams and make an impact in brand innovation, engaging brand
experiences, consumer insights and more.

Profile we look for:
- Ability to work in a multi-functional environment, interacting effectively with your team
  and business partners.
- Ability to operate in a fast-moving environment and manage time effectively.
- Curious, enthusiastic, a fast learner with strong interpersonal skills.
- Fresh graduate with limited work experience but a strong passion for Marketing.
- Fluency in English.
- Very good GPA and a bachelor's degree in Business Administration with a concentration in
  Marketing.

What we offer:
- A permanent position as a Nestlé employee, starting with a 24-month programme of several
  rotations in different teams.
- Access to Nestlé's comprehensive training programme (soft and hard skills).
- Responsibilities developing your knowledge in Marketing, brand building, consumer insights
  and the core business.
- Mentoring from senior leaders; attractive package, flexible/hybrid working.
- Post-programme assignment based on opportunities and business needs.
"""

ATS = [
    "marketing", "brand innovation", "brand building", "brand experiences",
    "consumer insights", "FMCG", "food & beverage", "NPD", "new product development",
    "brand strategy", "go-to-market", "campaign", "multi-functional", "cross-functional",
    "business partners", "fast-moving environment", "time management", "curious",
    "fast learner", "interpersonal skills", "passion for marketing", "English",
    "Business Administration", "GPA", "consumer trends", "market research",
    "sell-in/sell-out", "category", "trade marketing", "shopper marketing",
    "MENA", "GCC", "UAE", "Dubai", "rotations", "graduate programme", "Nestlé",
]

CONTENT = {
    "headline": (
        "Marketing · FMCG & Consumer Brands · Brand Building, Innovation & Consumer Insights"
    ),
    "professional_summary": (
        "Marketing professional with a Business Administration degree from CUNEF (E-Commerce & "
        "Fashion specialisation, 9.5/10 thesis) and a genuine passion for building consumer brands, "
        "who has spent the last four years in fast-moving FMCG and consumer environments — including "
        "a structured trainee programme at Mondelez (global food FMCG). Hands-on across the themes at "
        "the heart of NesTalent: brand innovation and NPD, engaging brand experiences, and consumer "
        "insights, always working multi-functionally with commercial, creative and trade partners. "
        "Curious, quick to learn and Dubai-based on a UAE residence visa — I'd bring that energy and "
        "rigour, with open eyes, to a 24-month journey across Nestlé MENA's categories."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Work end-to-end on brand innovation — leading 6 NPD launches (brief, packaging, pricing, go-to-market) across food and consumer categories in GCC, MENA and beyond, exactly the brand-building remit NesTalent rotates through",
                "Create engaging brand experiences — 360 campaigns spanning social, influencer (25–50 creators per campaign), sampling/seeding and in-store activations that bring the brands to life for shoppers",
                "Turn consumer insights into action — track consumer and category trends, competitor moves and campaign performance to shape brand plans, using an AI (Claude/GPT) reporting system that speeds decisions",
                "Operate in a genuinely multi-functional, fast-moving environment — coordinating commercial, creative, distributor and trade partners across 50+ markets to launch on time and on budget",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | Alibaba Group | 100K+ employees",
            "bullets": [
                "Created and led consumer-facing brand projects (Beauty Club, Hot on Social) that built brand affinity and positioned Miravia as a beauty and lifestyle destination — brand experiences from concept to activation",
                "Grew a portfolio of 42 brand accounts +30% GMV QoQ through assortment, pricing and promotions, working shoulder-to-shoulder with commercial, marketing and content teams",
                "Analysed consumer behaviour, conversion, traffic and retention to sharpen brand and category decisions — consumer-insight-led planning at scale",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Led cross-functional teams across marketing, logistics and customer support to deliver campaigns and activations end-to-end in a high-tempo environment",
                "Managed strategic key accounts and bespoke marketing activations that drove order volume and brand presence — interpersonal, partner-facing work every day",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global food FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Thrived in a structured graduate-style trainee programme inside a global food FMCG — the closest analogue to NesTalent — rotating through category and brand planning",
                "Contributed to brand innovation / NPD launches including Milka Spread and Mini Suchard, from insight to shelf",
                "Built sell-in/sell-out and promotional-effectiveness analysis for the chocolate category — consumer and category insight turned into commercial recommendations",
            ],
        },
    ],
    "skills_brand": (
        "brand building, brand innovation & NPD (end-to-end), engaging brand experiences, "
        "brand strategy, go-to-market, 360 campaigns, influencer & creator marketing, "
        "sampling & seeding, trade & shopper marketing"
    ),
    "skills_ecommerce": (
        "consumer & digital marketing, social & content (Instagram, TikTok), Meta Ads, "
        "Google Ads, e-commerce & quick-commerce (Noon, Talabat, Careem, Deliveroo), "
        "Shopify, generative-AI content & automation"
    ),
    "skills_commercial": (
        "multi-functional / cross-functional teamwork, business-partner & stakeholder management, "
        "key account management, category management, assortment & pricing, negotiation, modern trade"
    ),
    "skills_data": (
        "consumer insights & market research, consumer & category trends, competitor analysis, "
        "sell-in/sell-out, campaign KPI tracking, ROI / ROAS, AI-assisted analysis, "
        "Power BI, Tableau, Looker, Nielsen, Kantar"
    ),
    "skills_tools": (
        "Microsoft Office (Expert), Generative AI (Claude / ChatGPT), Canva, Meta Business Suite, "
        "Google Ads, Power BI, Tableau, Looker, Salesforce, SAP"
    ),
}

COVER_LETTER = {
    "opening_paragraph": (
        "Nestlé is the brand-building school I most admire in FMCG, so the NesTalent Marketing "
        "Graduate Trainee programme genuinely excites me. Marketing is my passion, food and consumer "
        "brands are where I started my career (a trainee programme at Mondelez), and the idea of a "
        "24-month journey across Nestlé MENA's categories — learning brand innovation, brand "
        "experiences and consumer insights the Nestlé way — is exactly the kind of foundation I want "
        "to build on."
    ),
    "body_paragraph_1": (
        "Every theme the programme rotates through is work I already love doing hands-on. At DoFreeze "
        "I lead brand innovation end-to-end (6 NPD launches: brief, packaging, pricing, go-to-market), "
        "create engaging brand experiences through 360 campaigns and activations, and turn consumer and "
        "category insight into brand plans — all in a fast-moving, multi-functional setting with "
        "commercial, creative and trade partners. Before that, my Mondelez trainee year in a global food "
        "FMCG (category planning, NPD like Milka, sell-in/sell-out analysis) is the closest thing to "
        "NesTalent I've experienced, and it's why I know I'd thrive in it."
    ),
    "body_paragraph_2": (
        "In full honesty, I bring more hands-on experience than a typical fresh graduate — and I'm "
        "applying with open eyes and real enthusiasm. I'm not looking to skip the learning; I want to "
        "learn Nestlé's craft across its portfolio and grow with the business. I'm a CUNEF Business "
        "Administration graduate with a Marketing-heavy specialisation and a 9.5/10 thesis, fluent in "
        "English and Spanish, curious and a fast learner, already based in Dubai on a UAE residence "
        "visa — so I can start contributing from day one with zero relocation."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to talk about how my passion for marketing, FMCG grounding and genuine "
        "eagerness to learn fit the NesTalent programme. I'm based in Dubai and available to interview "
        "at your convenience. Thank you for considering my application."
    ),
}


def make_job() -> Job:
    return Job(
        id="nestle-mena-nestalent-marketing-graduate-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.nestle.com/jobs",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "NesTalent Marketing Graduate Trainee Nestle MENA", "via": "LinkedIn"},
    )


def register_in_dashboard(job: Job) -> None:
    path = settings.data_dir / "scored_jobs.json"
    if not path.exists():
        return
    jobs = json.loads(path.read_text(encoding="utf-8"))
    if any(j.get("id") == job.id for j in jobs):
        return
    jobs.insert(0, {
        "id": job.id,
        "title": job.title,
        "company": job.company,
        "location": job.location,
        "url": job.url,
        "source": job.source,
        "description": job.description,
        "salary_raw": None,
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 58,
        "ai_tier": "Warm",
        "skills_match": [
            "BBA with Marketing focus + very good GPA (CUNEF, 9.5/10 thesis) — meets the education ask exactly",
            "Genuine FMCG grounding: Mondelez (global food FMCG trainee) + DoFreeze (FMCG distributor)",
            "Brand innovation / NPD, brand experiences, consumer insights — the three programme themes, done hands-on",
            "Multi-functional, fast-moving environment; strong interpersonal / partner-facing track record",
            "Fluent English; already in Dubai on UAE residence visa (Nestlé MENA HQ)",
        ],
        "missing_skills": [
            "'Fresh graduate with limited work experience' — Paula has 4+ yrs; she is OVER-qualified for a grad programme",
            "Programme may hard-screen for recent graduates / graduation year",
        ],
        "sector_fit": "excellent (FMCG / food & consumer brands — Nestlé MENA)",
        "seniority_fit": "OVER-qualified — targets fresh grads; positioned transparently as a foot-in-the-door to Nestlé",
        "red_flags": [
            "Graduate programmes frequently filter out candidates with several years of full-time experience; honest application, real chance of an eligibility screen-out",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Dream FMCG employer and a clean thematic match — brand innovation, brand experiences and "
            "consumer insights are exactly what Paula does, and her Mondelez trainee year is a direct "
            "Nestlé-style analogue. The real risk is eligibility: NesTalent explicitly targets fresh "
            "graduates with limited experience, and Paula has 4+ years, so this is applied with open "
            "eyes and honest framing (degree-led, passion-led) rather than pretending she's a new grad."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _relocate_to_dated_folder(pos_dir: Path) -> Path:
    """Move output/<Company> - <Role>/ under output/<DATE_FOLDER>/."""
    dated_parent = settings.output_dir / DATE_FOLDER
    dated_parent.mkdir(parents=True, exist_ok=True)
    dest = dated_parent / pos_dir.name
    if pos_dir.resolve() == dest.resolve():
        return dest
    if dest.exists():
        for sub in pos_dir.iterdir():
            target = dest / sub.name
            if sub.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                for f in sub.iterdir():
                    shutil.move(str(f), str(target / f.name))
            else:
                shutil.move(str(sub), str(target))
        shutil.rmtree(pos_dir, ignore_errors=True)
    else:
        shutil.move(str(pos_dir), str(dest))
    return dest


def main() -> None:
    job = make_job()
    register_in_dashboard(job)

    cv_docx = cv._fill_template(CONTENT, job)
    cv_pdf = cv._to_pdf(cv_docx)
    print("OK_CV", cv_pdf)

    cl_docx = cl._fill_template(COVER_LETTER, job, contact_name=None)
    cl_pdf = cl._to_pdf(cl_docx)
    print("OK_CL", cl_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
