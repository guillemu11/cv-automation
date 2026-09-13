"""One-off: generate Paula's CV for the Beiersdorf / Eucerin
"Assistant Brand Manager" (Dubai) role.

This is a *strong, honest* fit: an FMCG brand role in Skin Care (Eucerin) asking
for 1-3 yrs in Brand / Consumer / Shopper Marketing, Nielsen category deep dives,
innovation & relaunch project management, artwork & packaging, integrated
omnichannel comms, budget control and cross-functional stakeholder management —
almost all of which Paula genuinely has (NPD end-to-end incl. packaging, beauty &
fragrances category depth at Miravia, FMCG brand ownership at DoFreeze, Nielsen,
A&P budgets, shopper & trade, e-commerce/quick-commerce, influencers).

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful — NO invented skincare titles, NO invented Arabic, NO invented S&OP
ownership. It is re-angled to the JD's pillars. Genuine gaps (Arabic language,
skincare-specific brand) are simply not over-claimed.

Fills the real CV template, converts to PDF, registers the job for the dashboard,
and lands the package under output/2026-08-15/.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

COMPANY = "Beiersdorf"
TITLE = "Assistant Brand Manager - Eucerin"
DATE_FOLDER = "2026-08-15"

JOB_DESCRIPTION = """\
Assistant Brand Manager - Eucerin — Beiersdorf, Dubai, UAE.

Innovation Management & Readiness: lead and coordinate innovation and relaunch
projects to ensure timely, successful market implementation; track innovation
milestones and readiness across functions (timelines, risks, key deliverables);
support launch planning, execution and post-launch evaluation.

Marketing & Communications: analyze category trends and develop a deep
understanding of consumers and competitors to create best-in-class communication
and activation strategies; support execution of integrated marketing campaigns
across digital, influencers, e-commerce and in-store; lead coordination with
Digital, E-commerce and Shopper & Customer Marketing (S&CM) teams and with
international and local Beiersdorf agencies to develop and adapt campaigns per
local market.

Market Analysis, Insights & Competition Tracking: monthly category deep dives
using Nielsen; monitor brand and category performance and identify growth
opportunities and corrective actions; track competitor activity, launches,
pricing, promotions and market share; develop clear recommendations and action
plans from market and consumer insights.

Artwork & Packaging Management: manage artwork development and approval for new
launches, relaunches and renovation projects; coordinate internal and external
stakeholders to ensure timely delivery while maintaining compliance with local
regulations and brand guidelines; track timelines and proactively resolve issues.

Cross-Functional Project Management: support the S&OP process and align
commercial and supply planning requirements.

Budget Management & Control: raise purchase orders and process invoices; monitor
and track brand budgets with Senior Brand Managers and Finance; manage accruals,
provisions and year-end budget closing.

In-Market Execution (Offline & Online): ensure strong brand visibility through
promotional materials, POS displays, eCommerce visibility and shopper journey
optimization; maintain strong relationships with sales; partner with Media &
E-commerce to maximize visibility and sales online; drive synergies with Finance
and Supply Chain to deliver KPIs.

Profile: Bachelor's in Business Administration, Marketing or related; 1-3 years in
Brand Management, Consumer Marketing or Shopper Marketing in FMCG (skin care
preferred); advanced Excel, PowerPoint, Nielsen; data analysis, performance
reporting and translating insights into action; excellent project and stakeholder
management; thrives in a fast-paced, multi-priority environment; strong English
and Arabic communication and presentation skills; digital and consumer-centric
mindset with a passion for brands and innovation; self-motivated, proactive team
player.
"""

ATS = [
    "Brand Management", "Assistant Brand Manager", "Consumer Marketing",
    "Shopper Marketing", "FMCG", "Skin Care", "Beauty", "innovation management",
    "relaunch", "launch planning", "post-launch evaluation", "NPD",
    "category trends", "consumer insights", "competitor tracking", "market share",
    "Nielsen", "category deep dives", "integrated marketing campaigns", "digital",
    "influencers", "e-commerce", "in-store", "Shopper & Customer Marketing",
    "S&CM", "artwork", "packaging", "brand guidelines", "S&OP",
    "budget management", "A&P", "purchase orders", "invoices", "accruals",
    "POS displays", "eCommerce visibility", "shopper journey", "stakeholder management",
    "project management", "Excel", "PowerPoint", "performance reporting", "GCC", "MENA",
]

CONTENT = {
    "headline": "Brand & Marketing Manager · FMCG & Beauty · NPD & Innovation · Nielsen Insights · Shopper & E-Commerce",
    "professional_summary": (
        "Brand and marketing professional with 4+ years across FMCG and Beauty, building brands the way this "
        "role is scoped: leading innovation and NPD end-to-end (brief, packaging, pricing, go-to-market), turning "
        "category, consumer and competitor insight into integrated omnichannel campaigns, and executing across "
        "digital, influencers, e-commerce and in-store. Currently own Brand & Marketing for DoFreeze (Befit, "
        "Eurocake, Flair) in Dubai across 50+ markets; previously owned the Beauty & Fragrances category at "
        "Alibaba's Miravia (42 accounts, +30% GMV QoQ) and ran category planning at Mondelez with sell-in/sell-out "
        "and Nielsen-style analysis. Advanced Excel & PowerPoint, hands-on with Nielsen, A&P budgets and "
        "cross-functional stakeholder management. Business Administration graduate (CUNEF, 9.5/10 thesis), already "
        "based in Dubai on a residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Lead innovation, NPD and relaunch projects end-to-end for 6 launches — brief, packaging and artwork, pricing and go-to-market — coordinating cross-functional readiness and tracking milestones, risks and deliverables to hit market-launch deadlines across GCC, MENA and beyond",
                "Manage artwork development and approval with internal teams and external agencies, keeping packaging compliant with local regulations and brand guidelines while protecting launch timelines",
                "Turn category, consumer and competitor insight into integrated marketing campaigns spanning digital, influencers, e-commerce and in-store — briefing and coordinating local and international agencies to adapt creative per market",
                "Own A&P budget planning, tracking and reconciliation, and partner with Finance and Supply Chain to align demand, availability and KPI delivery",
                "Run in-market execution across modern trade and UAE quick-commerce (Noon, Talabat, Careem, Deliveroo) — POS visibility, eCommerce content and shopper-journey optimisation — working hand-in-hand with the sales team on brand plans",
                "Built a generative-AI system (Claude/GPT) automating campaign planning, market research and KPI reporting — cutting manual workload ~40% and speeding go-to-market",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Owned the Beauty & Fragrances category across 42 key accounts, growing GMV +30% QoQ through assortment, pricing, promotions and best-in-class activation — a content- and discovery-led category adjacent to skin care",
                "Ran monthly category and competitor deep dives — pricing, launches, promotions and share — turning insight into clear recommendations and action plans for brands and buyers",
                "Created and led the Beauty Club and Hot on Social activation programmes, lifting brand visibility, consumer loyalty and category positioning",
                "Led category expansion as PIC Fragrances, onboarding 30+ beauty & fragrance houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) in two months via trend-driven assortment",
                "Analysed conversion, traffic, retention, ROI and ROAS to steer performance and forecasting accuracy",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran monthly category deep dives for chocolate — sell-in/sell-out, promotional effectiveness and Nielsen-style performance reporting — to surface growth opportunities and corrective actions",
                "Contributed to NPD launches (Milka Spread, Mini Suchard) from concept to shelf, supporting innovation readiness across functions",
                "Built management-ready analyses in advanced Excel and PowerPoint, translating data into actionable brand recommendations",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic key accounts and helped build Glovo's Retail vertical, driving GMV through data-led planning and bespoke marketing activations",
                "Led cross-functional squads across marketing, logistics and CX to ship campaigns and grow order volume",
                "Negotiated high-impact commercial deals maximising profitability for platform and partners",
            ],
        },
    ],
    "skills_brand": "brand management, innovation & NPD end-to-end, launch & relaunch planning, artwork & packaging management, integrated omnichannel campaigns, shopper & trade marketing, influencer marketing, A&P budget management, go-to-market, activation strategy",
    "skills_ecommerce": "e-commerce & eCommerce visibility, Shopify e-store management, quick-commerce (Noon, Talabat, Careem, Deliveroo), shopper-journey optimisation, conversion rate optimisation (CRO), Meta Ads, Google Ads, influencers & UGC, marketing automation",
    "skills_commercial": "category management, assortment planning, pricing strategy, key account management, competitor & market-share tracking, negotiation, modern trade, distributor management, forecasting",
    "skills_data": "Nielsen, category deep dives, sell-in/sell-out, performance reporting, KPI tracking, consumer & competitor insight, ROI/ROAS, AI-assisted analysis, Power BI, Tableau, Kantar, SAP",
    "skills_tools": "Nielsen, Microsoft Excel (Advanced), PowerPoint (Advanced), Generative AI (Claude, ChatGPT), Shopify, Meta Ads Manager, Google Ads, Power BI, Tableau, SAP, Canva, Microsoft Office (Expert)",
}


def make_job() -> Job:
    return Job(
        id="beiersdorf-eucerin-abm-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.beiersdorf.com/careers",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Assistant Brand Manager - Eucerin", "brand": "Eucerin",
             "recruiter": "Akash Sharma", "apply_by": "2026-08-12"},
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
        "ai_score": 82,
        "ai_tier": "Hot",
        "skills_match": [
            "FMCG + Beauty brand management", "NPD / innovation & relaunch end-to-end",
            "Artwork & packaging management", "Nielsen category deep dives",
            "Integrated omnichannel campaigns (digital/influencers/e-com/in-store)",
            "Shopper & trade marketing", "A&P budget management",
            "Competitor & market-share tracking", "Advanced Excel & PowerPoint",
            "Already in Dubai (residence visa)",
        ],
        "missing_skills": [
            "Arabic language (JD asks EN + Arabic — Paula is ES native / EN C1)",
            "Skin-care-specific brand experience (has FMCG + beauty/fragrance, adjacent)",
            "Formal S&OP process ownership",
        ],
        "sector_fit": "strong (FMCG + beauty, skin-care adjacent)",
        "seniority_fit": "strong (4+ yrs vs 1-3 asked — slightly above, title is a step)",
        "red_flags": ["Arabic listed as a requirement", "Application deadline was 12 Aug 2026 (passed)"],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, honest fit. Eucerin Assistant Brand Manager is a core FMCG brand role (innovation/NPD "
            "readiness, Nielsen category deep dives, integrated omnichannel comms, artwork & packaging, A&P "
            "budget control, shopper & in-market execution) — nearly all of which Paula genuinely has: NPD "
            "end-to-end incl. packaging at DoFreeze, Beauty & Fragrances category depth at Miravia, "
            "Nielsen-style category planning at Mondelez, and hands-on shopper/e-commerce execution. Genuine "
            "gaps: Arabic (JD asks EN+Arabic; Paula is ES native/EN C1) and skin-care-specific brand tenure "
            "(has adjacent beauty/fragrance + FMCG). Tenure is slightly above the 1-3 yr band. Positioned "
            "truthfully as an FMCG/beauty brand builder; no invented skincare/Arabic/S&OP claims."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
    """Convert DOCX -> PDF headlessly via LibreOffice (no Word automation prompts).

    Falls back to cv._to_pdf (docx2pdf/Word) if soffice is unavailable or fails.
    Removes the intermediate DOCX on success, mirroring cv._to_pdf.
    """
    soffice = shutil.which("soffice") or "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    pdf_path = docx_path.with_suffix(".pdf")
    if Path(soffice).exists():
        try:
            subprocess.run(
                [soffice, "--headless", "--convert-to", "pdf", "--outdir",
                 str(docx_path.parent), str(docx_path)],
                check=True, capture_output=True, timeout=180,
            )
            if pdf_path.exists():
                docx_path.unlink(missing_ok=True)
                return pdf_path
        except Exception as exc:  # noqa: BLE001
            print("soffice conversion failed, falling back to docx2pdf:", exc)
    return cv._to_pdf(docx_path)


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
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
