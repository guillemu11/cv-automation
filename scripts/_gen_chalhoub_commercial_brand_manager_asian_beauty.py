"""One-off: Paula's CV for Chalhoub Group — "Commercial Brand Manager, Asian Beauty" (GCC).

Honest, strong fit. The JD is a commercial brand-ownership role over a regional
Asian Beauty portfolio (skincare + haircare) across the GCC: own commercial
planning and sell-in/sell-out, build annual business plans, targets and budgets
with local teams, retailers and brand principals, localise global brand strategy,
manage A&P, lead regional launches/novelties/activations/BTL, monitor KPIs and
close gaps, partner with KAMs across retail, e-commerce and marketplaces, and
keep operational excellence (in-store execution, VM, GWP).

Paula genuinely has: beauty category ownership at Alibaba's Miravia (42 accounts,
+30% GMV QoQ, PIC Fragrances, Flash Sales P&L to the CEO), FMCG commercial and
trade/shopper planning at DoFreeze across GCC/MENA with A&P budgets and NPD
launches end-to-end, multi-channel execution across retail, e-commerce and
marketplaces (Noon, Talabat, Careem, Deliveroo + Shopify), sell-in/sell-out and
promo-effectiveness analysis from Mondelez, and shop-floor/VM grounding at
Inditex (Massimo Dutti).

Kept strictly truthful — NO invented K-Beauty/J-Beauty/C-Beauty tenure, NO
invented Arabic (this JD does not ask for it), NO inflated years. She has ~5
years post-graduate (2021→2026) against a 6–8 year ask; that is stated plainly
in the dashboard, never padded in the CV. Asian Beauty exposure is listed by the
JD as "a strong advantage, but not essential" and is honestly absent.

One page (house standard since 2026-08-27): tight summary, 2–4 bullets per role.
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

COMPANY = "Chalhoub Group"
TITLE = "Commercial Brand Manager - Asian Beauty"
DATE_FOLDER = "2026-09-16"

JOB_DESCRIPTION = """\
Commercial Brand Manager — Asian Beauty | Chalhoub Group (LVMH joint venture), GCC.

Lead the growth and development of a portfolio of Asian Beauty brands across the GCC,
spanning skincare and haircare. Own commercial performance and brand execution across
multiple markets and channels. Highly commercial, hands-on role combining strong
analytical thinking with creativity, agility and a real passion for beauty.

Responsibilities: own commercial planning and performance of the portfolio, driving
sell-in and sell-out across the region; develop localised go-to-market strategies aligned
with global brand direction and market dynamics; build annual business plans, sales targets
and budgets with local teams, retailers and brand principals; monitor commercial KPIs and
market performance, identify gaps and implement corrective action plans; lead regional
execution of new launches, novelties, activations and BTL campaigns; manage A&P and
marketing budgets focused on commercial impact; analyse sales trends, consumer behaviour,
shopper insights and retail performance; partner with Key Account Managers and retail
partners across stores, e-commerce and marketplaces; ensure operational excellence
including in-store execution, VM initiatives and GWP activities; build strong relationships
with global and local stakeholders across multiple markets; bring new ideas and scale
established and high-potential brands.

Requirements: 6-8 years within Beauty, FMCG or similarly fast-paced consumer environment;
strong Beauty category knowledge, skincare and/or haircare advantageous; Asian Beauty,
K-Beauty, J-Beauty or C-Beauty exposure a strong advantage but not essential; strong
commercial acumen across sales planning, forecasting, budgeting and performance management;
experience managing brands across retail, e-commerce and marketplaces; GCC or regional
market exposure highly advantageous; strong analytical capabilities; excellent stakeholder
management and influencing; proactive, entrepreneurial, resourceful; commercial discipline
with creative flair.
"""

ATS = [
    "Commercial Brand Manager", "brand management", "commercial planning", "sell-in", "sell-out",
    "go-to-market", "localised go-to-market", "annual business plan", "sales targets", "budgets",
    "brand principals", "retail partners", "commercial KPIs", "market performance", "gap analysis",
    "corrective action plans", "new launches", "novelties", "activations", "BTL", "A&P",
    "marketing budget", "sales trends", "consumer behaviour", "shopper insights",
    "retail performance", "Key Account Managers", "key account management", "retail",
    "e-commerce", "marketplaces", "operational excellence", "in-store execution",
    "visual merchandising", "VM", "GWP", "stakeholder management", "influencing",
    "Beauty", "skincare", "haircare", "FMCG", "category management", "assortment",
    "pricing strategy", "promotions", "forecasting", "performance management", "P&L",
    "GCC", "MENA", "Middle East", "GMV", "ROI", "ROAS", "Nielsen", "Power BI",
]

CV_CONTENT = {
    "headline": "Commercial Brand Management · Beauty & FMCG · Sell-In / Sell-Out · GCC",
    "professional_summary": (
        "Commercial and brand professional with 5 years in Beauty and FMCG, owning portfolio performance end-to-end: "
        "business plans, sell-in and sell-out, A&P budgets and launches across retail, e-commerce and marketplaces in the GCC."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG group (Befit, Eurocake, Flair) | modern trade, Shopify D2C, talabat, Noon, Careem | GCC & 50+ markets",
            "bullets": [
                "Own annual business plans, sales targets and A&P budgets with distributors, local teams and retail partners; track sell-in, sell-out and commercial KPIs, closing gaps with corrective plans",
                "Lead regional execution of launches, novelties and BTL activations — 6 NPD end-to-end — localising global brand direction market by market",
                "Drive the portfolio across modern trade, e-commerce and marketplaces: listings, assortment, promotions and in-store execution; lead a team of two (design + social)",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's eCommerce marketplace | 100K+ employees",
            "bullets": [
                "Owned commercial performance of 42 beauty, fragrance and fashion brands — incl. global makeup and skincare houses — through pricing, assortment and promotions (+30% GMV QoQ)",
                "Ran the Flash Sales channel P&L reporting to the CEO; as PIC Fragrances onboarded 30+ houses in two months (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
                "Analysed sales trends, shopper behaviour and retail performance to steer forecasting; created the Beauty Club and Hot on Social programmes",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Delivery & quick-commerce app | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed XL partners on joint business plans, promotions and GMV; helped build the Retail vertical incl. beauty and fashion brands",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | Chocolate category (Milka, Suchard) | €36B revenue",
            "bullets": [
                "Built sell-in/sell-out and promotional-effectiveness reports with Nielsen; contributed to NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": (  # label -> "Brand & Commercial"
        "brand & portfolio management, commercial planning, localised go-to-market, annual business plans, A&P budgets"
    ),
    "skills_commercial": (  # label -> "Sales & Category"
        "sell-in & sell-out, sales targets, forecasting, pricing, assortment, category management, key accounts, principals"
    ),
    "skills_ecommerce": (  # label -> "Channels & Activation"
        "retail, e-commerce & marketplaces, launches & novelties, BTL activations, in-store execution & VM, Noon, talabat, Careem, Shopify"
    ),
    "skills_data": (  # label -> "KPIs & Insight"
        "commercial KPIs & gap analysis, sales trends, shopper insight, P&L, ROI, ROAS, GMV, Nielsen"
    ),
    "skills_tools": (  # label -> "Tools"
        "Excel, PowerPoint, Nielsen, Power BI, Tableau, Salesforce, SAP, Shopify, Meta & Google Ads, Claude (AI)"
    ),
}


def make_job() -> Job:
    return Job(
        id="chalhoub-commercial-brand-manager-asian-beauty-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates (GCC)",
        url="https://www.chalhoubgroup.com/en/careers",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Chalhoub Commercial Brand Manager Asian Beauty",
             "portfolio": "Asian Beauty — skincare & haircare, regional GCC",
             "group": "Chalhoub Group (LVMH joint venture)"},
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
        "salary_raw": None, "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 82, "ai_tier": "Hot",
        "skills_match": [
            "Beauty category ownership at scale — 42 beauty/fragrance/fashion accounts, +30% GMV QoQ (Miravia, Alibaba)",
            "Sell-in AND sell-out ownership across channels; sell-in/sell-out analysis since Mondelez",
            "Annual business plans, sales targets and budgets built with distributors, retailers and principals",
            "A&P and marketing budget management steered to commercial impact",
            "Regional launch execution — 6 NPD end-to-end, novelties, activations, BTL",
            "Multi-channel: modern trade + e-commerce + marketplaces (Noon, Talabat, Careem, Deliveroo, Shopify)",
            "Commercial KPI monitoring, gap analysis and corrective plans (ROI, ROAS, conversion, sell-out)",
            "GCC/MENA market exposure, hands-on and current, based in Dubai",
            "Shopper insight and retail performance analysis; Nielsen from Mondelez",
            "In-store execution & VM grounding from Inditex (Massimo Dutti)",
            "Stakeholder management across global principals and local market teams",
            "Fragrance/beauty principal onboarding — 30+ houses in two months as PIC Fragrances",
        ],
        "missing_skills": [
            "6-8 years asked; Paula has ~5 post-graduate years (2021-2026) plus earlier Inditex retail — a genuine, modest shortfall",
            "Asian Beauty / K-Beauty / J-Beauty / C-Beauty tenure — absent (JD calls it 'a strong advantage, but not essential')",
            "Haircare category specifically — her beauty depth is colour cosmetics, skincare and fragrance",
            "GWP mechanics by name — she runs sampling and seeding, which is adjacent but not identical",
        ],
        "sector_fit": "very strong — beauty portfolio commercial management, her exact category",
        "seniority_fit": "on-band on title (Brand Manager = her current level); slightly light on the 6-8 year ask",
        "red_flags": [
            "Years of experience sits just below the stated 6-8 year band",
            "No Asian Beauty/K-Beauty exposure — explicitly non-essential in the JD but a differentiator she lacks",
            "Chalhoub asks that assessments and interviews be completed WITHOUT generative AI assistance — CV prep is fine, but she must do any test or interview unaided",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "One of the cleanest fits in the pipeline. The role is commercial brand ownership over a regional "
            "beauty portfolio: sell-in/sell-out, annual plans and budgets with principals and retailers, A&P, "
            "launches and BTL, KPI gap-closing, and execution across retail, e-commerce and marketplaces — which "
            "maps almost line-for-line onto what Paula does now at DoFreeze and did at Miravia, where she owned "
            "42 beauty and fragrance accounts at +30% GMV QoQ and ran a channel P&L to the CEO. Beauty is her "
            "category, GCC is her market, and multi-channel is her daily reality. Honest gaps: ~5 years against "
            "a 6-8 year ask, no Asian Beauty tenure (non-essential per the JD), and haircare is outside her depth. "
            "No invented K-Beauty, no invented Arabic (this JD does not ask for it), no padded years."
        ),
        "scored_by": "manual:claude", "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00", "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
    soffice = shutil.which("soffice") or "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    pdf_path = docx_path.with_suffix(".pdf")
    if Path(soffice).exists():
        try:
            subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir",
                            str(docx_path.parent), str(docx_path)],
                           check=True, capture_output=True, timeout=180)
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
    cv_docx = cv._fill_template(CV_CONTENT, job)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)
    final_dir = _relocate_to_dated_folder(cv_pdf.parent.parent)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
