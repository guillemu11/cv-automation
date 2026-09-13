"""One-off: generate Paula's CV for **Brand Manager - Better For You, Raffaello & Tablets**
at **Ferrero** (Job ID 77585), Dubai (Hybrid), Gulf region. Reports to the Regional Marketing
Manager; manages one Assistant Brand Manager.

JD ask: brand strategy & portfolio development (positioning, media planning, innovation);
integrated marketing plans with creative/media/digital agencies; commercialisation of
innovation, seasonal and portfolio expansion; consumer & shopper insights with CSU;
digital/social/shopper/in-store activation vs KPIs; partner Sales & Trade Marketing on
sales planning, forecasting, promotions; packaging (innovation, seasonal, promo); budget &
P&L tracking; manage one ABM. 4-5 yrs FMCG incl. 2-3 in marketing; GCC a plus; Arabic preferred.

Paula's honest angle:
- Better For You = Befit (sugar-free / fitness baked snacks) at DoFreeze: seasonal
  campaigns (Fitness Month, New Year New Me) with sell-out proof — Befit x Noon +4,176
  incremental units (+31% vs baseline); SMASH x talabat +165% daily sales vs +4.7% control.
- Seasonal gifting moments (Ramadan for Eurocake) — maps to Raffaello.
- 6 NPD launches end-to-end incl. packaging, pricing, go-to-market across 50+ markets.
- Agencies: 4 influencer/UGC agencies, negotiated -30%, audited reach reporting.
- People: leads a team of two (designer + social media executive) -> the ABM ask.
- Confectionery: Mondelez chocolate category planning (promo effectiveness, sell-in/out,
  Milka Spread, Mini Suchard launches).

Honesty guardrails:
- No Arabic (JD: "preferred", not required) — flagged, not fabricated.
- Forecast: "contribute to the monthly sell-in forecast", never "own".
- Nielsen used at Mondelez (confirmed by Guille 2026-09-13); no TV/ATL media buying claimed.
- Factual "UAE Residence Visa" only.

ONE-PAGE standard. Lands under output/2026-09-13/.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from docx import Document

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

COMPANY = "Ferrero"
TITLE = "Brand Manager BFY Raffaello Tablets"
DATE_FOLDER = "2026-09-13"

JOB_DESCRIPTION = """\
Brand Manager - Better For You, Raffaello & Tablets — Ferrero, Dubai (Hybrid), Job ID 77585.
Reports to the Regional Marketing Manager. Manages and develops the Better For You (BFY),
Raffaello and Tablets portfolio across the Gulf region: brand strategy, innovation,
commercialization and integrated marketing execution. Manages one Assistant Brand Manager.

Brand strategy & portfolio development: positioning, portfolio development, consumer
engagement, media planning, innovation priorities, consumer and market insights, brand equity.
Marketing planning & project management: integrated marketing plans and campaigns with
creative, media and digital agencies; ownership, autonomy, project leadership.
Innovation & commercialization: innovation projects, seasonal initiatives, portfolio expansion,
cross-functional market launches, local vs regional alignment.
Consumer & market insights: market performance, consumer behavior, shopper trends, competitive
activity, category developments; with Consumer & Shopper Understanding (CSU).
Digital & media activation: digital, social media, media, shopper marketing, in-store
activations; agency campaign assets and content; track KPIs and optimize investments.
Commercial & sales performance: partner Sales and Trade Marketing on sales planning,
forecasting, promotional activities, portfolio performance; corrective actions.
Packaging: innovation, seasonal and promotional packaging projects; brand guidelines.
Budget & performance: marketing budgets, financial KPIs, investment effectiveness, forecasting.
People: manage, coach and develop one Assistant Brand Manager; work with Marketing, Sales,
Trade Marketing, Finance, Supply Chain, Quality, CSU.

About you: bachelor's in Marketing/Business; 4-5 years FMCG incl. 2-3 in Marketing; brand
management, integrated campaigns, product launches, consumer insights, agency management;
GCC and multinational exposure an advantage; Excel & PowerPoint, digital & social media,
market analysis, sales forecasting, budget management, P&L understanding. English fluent,
Arabic preferred.
"""

ATS = [
    "Brand Manager", "brand management", "brand strategy", "brand positioning", "brand equity",
    "portfolio development", "Better For You", "confectionery", "chocolate", "innovation",
    "commercialization", "product launches", "seasonal initiatives", "packaging",
    "integrated marketing campaigns", "marketing plans", "media planning", "creative agencies",
    "media agencies", "digital agencies", "agency management", "consumer insights",
    "shopper trends", "competitive activity", "category", "digital", "social media",
    "shopper marketing", "in-store activations", "KPIs", "Sales", "Trade Marketing",
    "sales forecasting", "promotional activities", "budget management", "P&L",
    "project management", "cross-functional", "stakeholder management", "people management",
    "coaching", "Excel", "PowerPoint", "FMCG", "GCC", "Gulf", "UAE", "multinational",
]

CONTENT = {
    "headline": (
        "Brand Manager · Snacking & Chocolate · Better-For-You · Launches & Seasonal Campaigns"
    ),
    "professional_summary": (
        "FMCG brand marketer with 5 years, starting in Mondelez's chocolate category (Milka, Suchard) and now running "
        "brand strategy for a UAE snacking portfolio incl. better-for-you Befit: 6 launches, 4 agencies, a team of two."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG snacking group (Befit better-for-you, Eurocake, Smash) | GCC + 50+ markets",
            "bullets": [
                "Lead brand positioning and integrated marketing plans for the portfolio across digital, social, influencer, shopper and in-store; delivered 6 launches end-to-end (brief, packaging, pricing, go-to-market) with Sales, Supply Chain and Finance",
                "Built the seasonal calendar (Ramadan, Back to School, Fitness Month, New Year): Befit x Noon 'New Year, New Me' added 4,176 incremental units (+31% vs baseline); SMASH x talabat lifted daily sales +165% vs +4.7% for a control brand",
                "Brief and manage 4 agencies on campaign assets and content (negotiated -30%, audited their KPI reporting); track A&P spend vs results and contribute promo and campaign input to the monthly sell-in forecast",
                "Lead and coach a team of two (graphic designer + social media executive), setting priorities and reviewing all creative against brand guidelines",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's lifestyle marketplace | Multinational, 100K+ employees",
            "bullets": [
                "Managed 42 brand accounts and delivered +30% GMV QoQ through promotions, pricing and assortment; owned the Flash Sales channel reporting to the CEO",
                "Launched the Fragrances category (30+ brands in two months) by reading consumer and competitor trends; created the Beauty Club loyalty project",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Grew XL accounts (KFC, Taco Bell, Sushi Shop) with data-led promotional plans, coordinating marketing, operations and support teams",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | Chocolate category (Milka, Suchard) | €36B revenue",
            "bullets": [
                "Planned the chocolate category with Nielsen market data: sell-in/sell-out, market share and promotional-effectiveness reports that identified growth opportunities for the brand teams",
                "Supported chocolate innovation launches Milka Spread and Mini Suchard, from category rationale to shelf",
            ],
        },
    ],
    "skills_brand": (  # label -> "Brand Management"
        "brand positioning & strategy, integrated campaigns, innovation & launches, packaging, seasonal "
        "activations, influencer & social"
    ),
    "skills_ecommerce": (  # label -> "Shopper & Channels"
        "shopper & in-store activation, sampling, modern trade, Noon / talabat / Careem, Meta & Google Ads"
    ),
    "skills_commercial": (  # label -> "Leadership"
        "people management (team of two), agency management (4), Sales & Trade Marketing, Finance, Supply Chain"
    ),
    "skills_data": (  # label -> "Insights & Budget"
        "Nielsen market data, consumer & market insights, promo effectiveness, sell-in / sell-out, A&P budget tracking, KPIs"
    ),
    "skills_tools": (  # label -> "Tools"
        "Excel & PowerPoint (advanced), Power BI, Nielsen, Meta Ads Manager, Adobe & Canva, Generative AI (Claude)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Brand Management",
    "E-Commerce & Digital": "Shopper & Channels",
    "Commercial": "Leadership",
    "Data & Analytics": "Insights & Budget",
}


def make_job() -> Job:
    return Job(
        id="ferrero-77585-brand-manager-bfy-raffaello-tablets",
        title="Brand Manager - Better For You, Raffaello & Tablets",
        company=COMPANY,
        location="Dubai, UAE (Hybrid)",
        url="https://www.ferrerocareers.com/",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "Ferrero Brand Manager Better For You Raffaello Tablets Dubai 77585",
            "note": "Strong fit: FMCG snacking brand manager with a better-for-you brand (Befit), 6 launches incl. "
                    "packaging, seasonal campaigns with sell-out proof, 4 agencies, team of two, Mondelez chocolate. "
                    "Gaps: no Arabic (preferred), no ATL/TV media, no formal CSU/Nielsen ownership.",
        },
    )


def register_in_dashboard(job: Job) -> None:
    path = settings.data_dir / "scored_jobs.json"
    if not path.exists():
        return
    jobs = json.loads(path.read_text(encoding="utf-8"))
    if any(j.get("id") == job.id for j in jobs):
        return
    jobs.insert(0, {
        "id": job.id, "title": job.title, "company": job.company, "location": job.location,
        "url": job.url, "source": job.source, "description": job.description,
        "salary_raw": "Not disclosed (Brand Manager at a multinational — likely at/above 20k AED floor)",
        "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 84, "ai_tier": "Strong",
        "skills_match": [
            "Better For You: runs Befit (sugar-free / fitness snacks) with Befit x Noon +4,176 incremental units (+31%)",
            "6 launches end-to-end incl. packaging, pricing and go-to-market; seasonal initiatives (Ramadan, New Year)",
            "Agency management (4 agencies, -30% negotiated) + people management (team of two) -> ABM",
            "Confectionery grounding at Mondelez chocolate (promo effectiveness, sell-in/out, Milka/Suchard launches)",
        ],
        "missing_skills": [
            "Arabic preferred — Paula has no Arabic",
            "No ATL / TV media planning",
            "Premium gifting (Raffaello) and chocolate tablets brand-side experience is adjacent, not direct",
        ],
        "sector_fit": "strong — FMCG snacking & confectionery in the GCC",
        "seniority_fit": "on level — 4-5 yrs FMCG, Brand Manager with one report",
        "red_flags": [
            "Arabic listed as preferred",
            "Brand-management tenure is ~1 year (DoFreeze); earlier roles are KAM / category",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Very good fit: the portfolio includes a better-for-you line, which is exactly what Paula runs with Befit, "
            "and the JD's core asks — launches with packaging, seasonal initiatives, agency management, shopper and "
            "digital activation, partnering Sales on forecasting, managing one junior — all map to real, evidenced "
            "work. Gaps are Arabic (preferred only), ATL media and a short formal brand-manager tenure."
        ),
        "scored_by": "manual:claude", "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00", "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _relabel_for_role(docx_path: Path) -> None:
    doc = Document(str(docx_path))
    for table in doc.tables:
        for row in table.rows:
            first = row.cells[0]
            new = ROLE_LABELS.get(first.text.strip())
            if not new:
                continue
            para = first.paragraphs[0]
            if para.runs:
                para.runs[0].text = new
                for r in para.runs[1:]:
                    r.text = ""
            else:
                para.add_run(new)
    doc.save(str(docx_path))


def _to_pdf_soffice(docx_path: Path) -> Path:
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
    _relabel_for_role(cv_docx)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)

    short = final_dir / "01_CV_y_Carta" / "Paula De Francisco - CV.pdf"
    final_cv = final_dir / "01_CV_y_Carta" / cv_pdf.name
    if final_cv.exists():
        shutil.copy(str(final_cv), str(short))
        print("OK_SHORT", short)

    try:
        from pypdf import PdfReader
        n = len(PdfReader(str(final_cv)).pages)
        print(f"PAGES {n}", "OK" if n == 1 else "!! SPILLS")
    except Exception as exc:  # noqa: BLE001
        print("page-count check skipped:", exc)

    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
