"""One-off: generate Paula's CV for a **generic Marketing Manager** role.

Role-agnostic but Marketing-Manager-shaped: it leads with brand strategy,
integrated campaigns, NPD/go-to-market, digital & e-commerce and people/agency
management, instead of the key-account angle used in her commercial CVs. Meant
to be sent to any UAE "Marketing Manager" posting where there is no JD to tailor
against (recruiter groups, referrals, speculative applications).

Content is drawn from profile.yaml — nothing invented. Honesty guardrails:
no Arabic claimed, factual "UAE Residence Visa", no fabricated ownership.

Includes the standing **AI & Automation** skills row (memory rule).

ONE-PAGE standard: 4/2/1/2 bullets, ~6 skills per row, short row labels.
Lands under output/2026-09-16/Generico - Marketing Manager/01_CV_y_Carta/,
plus a short-named 'Paula De Francisco - CV.pdf' copy for portals.
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from docx import Document

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

COMPANY = "Generico"
TITLE = "Marketing Manager"
DATE_FOLDER = "2026-09-16"

JOB_DESCRIPTION = """\
Marketing Manager (generic, UAE). Own the brand and marketing plan end-to-end:
brand strategy and positioning, annual and seasonal marketing calendar, integrated
360 campaigns across digital, social, influencer, retail and in-store; product
launches and go-to-market; content and creative direction with agencies and
in-house designers; e-commerce and quick-commerce activation; paid media planning
and optimisation; A&P budget ownership; campaign KPI tracking and reporting;
partnering with Sales and Trade Marketing on promotions and sell-out; managing and
developing a small team. 4+ years in marketing, ideally FMCG / retail / e-commerce,
with a data-driven, hands-on approach. English fluent; UAE experience preferred.
"""

CONTENT = {
    "headline": (
        "Marketing Manager · Brand Strategy & 360 Campaigns · Digital & E-Commerce · FMCG · Dubai"
    ),
    "professional_summary": (
        "Marketing manager with 5 years across FMCG, beauty and e-commerce, now leading brand and marketing for a "
        "UAE snacking group: full marketing calendar, 6 launches, 4 agencies, paid media and a team of two — with "
        "AI automation built into how plans, content and reporting get done."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG snacking group (Befit, Eurocake, Flair) | GCC + 50+ markets",
            "bullets": [
                "Own brand positioning and the full marketing calendar across digital, social, influencer, shopper and in-store; delivered 6 launches end-to-end (brief, packaging, pricing, go-to-market) with Sales, Supply Chain and Finance across 50+ markets",
                "Built the influencer and UGC programme from zero to 25–50 creators per campaign, plus sampling and seeding across modern trade and quick-commerce; brief and manage 4 agencies (negotiated −30%) and audit their KPI reporting",
                "Run paid media and owned channels: Meta and Google Ads (audiences, creative A/B testing, ROAS), social, EDM and the Shopify store end-to-end (catalogue, UX, promotions), lifting conversion rate and average order value",
                "Manage the A&P budget against campaign KPIs and lead a team of two (graphic designer + social media executive); built an AI automation layer (Claude) for campaign planning, content and reporting that cut manual workload ~40%",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's lifestyle marketplace | Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Grew 42 brand accounts +30% GMV QoQ through promotional campaigns, pricing and assortment, and owned the Flash Sales channel reporting to the CEO",
                "Launched the Fragrances category (30+ brands in two months) off consumer and competitor trends, and created the Beauty Club and Hot on Social marketing projects that drove visibility and loyalty",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Built bespoke marketing activations and data-led promotional plans for XL accounts (KFC, Taco Bell, Sushi Shop), coordinating marketing, operations and support to grow order volume",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | Chocolate category (Milka, Suchard) | €36B revenue",
            "bullets": [
                "Analysed the chocolate category with Nielsen data — sell-in/sell-out, market share and promotional effectiveness — turning it into growth recommendations for the brand teams",
                "Supported the Milka Spread and Mini Suchard launches from category rationale to shelf",
            ],
        },
    ],
    "skills_brand": (  # label -> "Brand & Campaigns"
        "brand strategy & positioning, 360 integrated campaigns, NPD & go-to-market, seasonal calendar, "
        "influencer & UGC, team leadership (2)"
    ),
    "skills_ecommerce": (  # label -> "Digital & E-Commerce"
        "Meta & Google Ads, social & EDM, Shopify e-store & CRO, quick-commerce (Noon, Talabat, Careem, Deliveroo), "
        "content & art direction"
    ),
    "skills_commercial": (  # label -> "Commercial & Insights"
        "A&P budget & P&L, shopper & trade marketing, modern trade & distributors, pricing & assortment, "
        "sell-in / sell-out, ROI / ROAS / GMV"
    ),
    "skills_data": (  # label -> "AI & Automation"
        "Claude / Claude Code agents, generative AI for content & campaigns, AI video (Higgsfield, Hailuo), "
        "MCP integrations, AEO / GEO, Python reporting"
    ),
    "skills_tools": (  # label -> "Tools"
        "Excel & PowerPoint (expert), Power BI, Tableau, Nielsen & Kantar, Salesforce, SAP, Shopify, "
        "Meta Ads Manager, Adobe & Canva"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Brand & Campaigns",
    "E-Commerce & Digital": "Digital & E-Commerce",
    "Commercial": "Commercial & Insights",
    "Data & Analytics": "AI & Automation",
}


def make_job() -> Job:
    return Job(
        id="generic-marketing-manager-2026-09-16",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE",
        url="",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={"note": "Generic Marketing Manager CV — no specific posting, not registered in the dashboard."},
    )


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

    cv_docx = cv._fill_template(CONTENT, job)
    _relabel_for_role(cv_docx)
    cv_pdf = cv._to_pdf(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)

    final_cv = final_dir / "01_CV_y_Carta" / cv_pdf.name
    short = final_dir / "01_CV_y_Carta" / "Paula De Francisco - CV.pdf"
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
