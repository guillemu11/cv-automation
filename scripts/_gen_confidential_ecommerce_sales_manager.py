"""One-off: generate Paula's ONE-PAGE CV for **eCommerce Sales Manager** at a **confidential multi-brand
FMCG company** (UAE; LinkedIn posting, company not disclosed).

JD ask: commercial ownership of the eCommerce channel across multiple brands and platforms (Net Sales,
Front Margin, growth); manage eCommerce + Quick Commerce partners, JBPs, annual negotiations; multi-brand
stakeholder reporting; category/assortment (SKUs, pack sizes, bundles); forecast accuracy and availability
with Supply Chain; digital shelf (content, images, SEO); dashboards; promo calendar + platform media ROI;
Customer Marketing / Supply Chain / Finance collaboration. 5+ yrs eCommerce / KAM / FMCG commercial.

Paula's honest angle: Miravia (Alibaba) KAM for 42 brands (+30% GMV QoQ) on pricing, assortment, promotions
and Flash Sales P&L; Glovo XL accounts incl. commercial negotiations; DoFreeze multi-brand (Befit, Eurocake,
Smash) across talabat/Noon/Careem + own Shopify; weekly dark-store stock-risk review; MSL per channel reviewed
with e-commerce sales; Mondelez sell-in/sell-out and promo effectiveness (Nielsen).

Honesty guardrails:
- Forecast NOT owned at DoFreeze ("contribute to the monthly sell-in forecast"); platform assortment reviewed
  jointly with e-commerce sales. No formal JBP signed by her; no Front Margin P&L ownership claimed.
- Negotiation evidence: Glovo deals + Miravia brand promo/pricing plans (platform side).
- ~5 yrs incl. Mondelez trainee year. Factual "UAE Residence Visa" only.

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

COMPANY = "Confidential - Multi-brand FMCG"
TITLE = "eCommerce Sales Manager"
DATE_FOLDER = "2026-09-13"

JOB_DESCRIPTION = """\
eCommerce Sales Manager — lead, manage and grow the eCommerce channel across multiple brands and platforms;
deliver sales targets, expand market share, optimise profitability, manage key customer relationships.

1. Commercial ownership: deliver Net Sales, Front Margin and growth targets; eCommerce growth strategy;
optimise promotional investment and ROI; growth via assortment expansion, pricing, activations, exclusive
partnerships; monitor channel performance and corrective actions.
2. Customer & platform management: key eCommerce and Quick Commerce partners; Joint Business Plans (JBPs);
commercial negotiations and annual business discussions; platform-specific traffic/conversion growth.
3. Multi-brand management: multiple brands across platforms; reporting and feedback to brand stakeholders.
4. Category development & assortment: category trends, shopper behaviour, traffic, conversion, profitability,
competitors; new SKUs, pack sizes, seasonal offers, platform-specific bundles.
5. Inventory & demand planning: with Supply Chain on forecast accuracy; reduce stock-outs/overstock; NPD
launch availability; service levels.
6. Digital shelf & content: content, images, SEO, keywords; product pages; ratings, reviews, visibility.
7. Data & analytics: sales, market share, availability, pricing, conversion; dashboards; insights.
8. Promotion & media: eCommerce promo calendar and platform activations; pricing/promo plans balancing growth
and profitability; media investments and platform marketing tools; campaign ROI.
9. Cross-functional: Customer Marketing, Supply Chain, Finance, central teams.

Qualifications: Bachelor's in Business/Marketing/Commerce; 5+ years eCommerce, Digital Sales, KAM or FMCG
commercial; major eCommerce and Quick Commerce platforms; online sales growth; analytical, negotiation,
stakeholder management; advanced Excel (2+ yrs) and reporting; communication and presentation.
KPIs: Net Sales growth, margin, market share, conversion, forecast accuracy, availability, promo/media ROI.
"""

ATS = [
    "eCommerce sales", "Quick Commerce", "key account management", "Joint Business Plan", "JBP",
    "commercial negotiations", "Net Sales", "Front Margin", "profitability", "market share", "growth strategy",
    "multi-brand", "assortment", "pricing", "promotions", "promotional calendar", "ROI", "platform activations",
    "retail media", "digital shelf", "content", "SEO", "keywords", "conversion rate", "ratings and reviews",
    "category development", "SKU", "bundles", "forecast accuracy", "availability", "stock-outs",
    "demand planning", "supply chain", "dashboards", "Excel", "reporting", "stakeholder management",
    "talabat", "Noon", "Careem", "Amazon", "FMCG",
]

CONTENT = {
    "headline": "eCommerce Sales & Key Account Management · Quick Commerce · FMCG",
    "professional_summary": (
        "eCommerce commercial professional with 5 years across FMCG (Mondelez), marketplaces (Alibaba's Miravia) and quick "
        "commerce (Glovo), now growing a multi-brand FMCG portfolio on talabat, Noon, Careem and Shopify in Dubai."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG food group (Befit, Eurocake, Smash) | talabat, Noon, Careem + Shopify D2C | 50+ markets",
            "bullets": [
                "Drive eCommerce growth for three brands on talabat, Noon and Careem: promo calendar, platform activations, listings and content; review assortment and must-stock lists per channel with e-commerce sales",
                "Run a weekly stock-risk review by dark store with an AI-built dashboard, checking POs against demand to prevent stock-outs; contribute to the monthly sell-in forecast with Sales and Finance",
                "Own the Shopify store end-to-end (catalogue, pricing, bundles, discounts, checkout), lifting conversion rate and AOV; 6 NPD launches, incl. pricing and go-to-market",
                "Plan Meta and Google Ads spend against ROI/ROAS; align campaigns with 4 agencies and lead a team of two (designer + social media executive)",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's eCommerce marketplace | 100K+ employees",
            "bullets": [
                "Managed 42 brand accounts, +30% GMV QoQ through pricing, assortment and promotional plans agreed with each brand; tracked conversion, traffic and ROI",
                "Owned the Flash Sales channel P&L (selection, pricing, timing), reporting to the CEO; onboarded 30+ fragrance stores in two months",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Delivery & quick-commerce app | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Negotiated commercial deals and activations with XL partners (KFC, Taco Bell, Sushi Shop) to grow GMV; helped build the Retail vertical",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | Chocolate category (Milka, Suchard) | €36B revenue",
            "bullets": [
                "Built sell-in/sell-out and promotional-effectiveness reports with Nielsen; supported the Milka Spread and Mini Suchard launches",
            ],
        },
    ],
    "skills_brand": (  # label -> "Commercial"
        "key accounts, negotiations, pricing, promo calendar & ROI, multi-brand growth plans"
    ),
    "skills_ecommerce": (  # label -> "eCom & Q-Commerce"
        "talabat, Noon, Careem, Shopify, digital shelf & content, listings, conversion"
    ),
    "skills_commercial": (  # label -> "Category & Supply"
        "assortment & must-stock lists, NPD, bundles, stock-outs, sell-in forecast input"
    ),
    "skills_data": (  # label -> "Data & Reporting"
        "sales & availability dashboards, sell-in/sell-out, Nielsen, ROI/ROAS, GMV"
    ),
    "skills_tools": (  # label -> "Tools"
        "Advanced Excel, Power BI, Looker, SAP, Salesforce, Meta & Google Ads, Claude"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Commercial",
    "E-Commerce & Digital": "eCom & Q-Commerce",
    "Commercial": "Category & Supply",
    "Data & Analytics": "Data & Reporting",
}


def make_job() -> Job:
    return Job(
        id="confidential-ecommerce-sales-manager-2026-09",
        title=TITLE,
        company=COMPANY,
        location="UAE",
        url="https://www.linkedin.com/jobs/search/?keywords=eCommerce%20Sales%20Manager%20Dubai",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "eCommerce Sales Manager (confidential, multi-brand FMCG)",
            "note": "Strong fit: KAM 42 brands at Miravia, Glovo XL negotiations, multi-brand FMCG on talabat/Noon/Careem, "
                    "dark-store stock-risk review. Gaps: formal JBPs, Front Margin ownership, forecast owned by e-com manager.",
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
        "salary_raw": "Not disclosed",
        "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 76, "ai_tier": "Hot",
        "skills_match": [
            "KAM for 42 brands at Miravia (+30% GMV QoQ) on pricing, assortment and promotions",
            "Quick-commerce: Glovo XL accounts + DoFreeze on talabat, Noon and Careem",
            "Multi-brand FMCG portfolio (Befit, Eurocake, Smash) in the UAE",
            "Weekly dark-store stock-risk review against POs; must-stock lists per channel",
            "FMCG sell-in/sell-out and promo effectiveness (Mondelez, Nielsen)",
        ],
        "missing_skills": [
            "Formal JBPs and annual platform negotiations as supplier-side lead",
            "Front Margin / Net Sales P&L ownership",
            "Forecast ownership (she contributes; e-commerce manager owns)",
        ],
        "sector_fit": "strong — FMCG eCommerce + quick commerce in UAE",
        "seniority_fit": "good — Manager level, 5 yrs vs 5+ asked",
        "red_flags": ["Company confidential", "Sales-heavy role, less brand"],
        "ats_keywords": ATS,
        "reasoning": (
            "Very close to her Miravia/Glovo KAM plus current UAE quick-commerce work; no Arabic listed. Gaps are "
            "supplier-side JBPs and margin ownership. Check salary vs AED 20k floor early."
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
