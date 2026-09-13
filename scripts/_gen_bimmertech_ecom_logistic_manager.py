"""One-off: generate Paula's CV + cover letter for BimmerTech
"E-commerce Logistic Manager" (Dubai, Hybrid — Operations/Logistics function).

HONEST FIT NOTE (read before editing):
  This is a LOGISTICS / OPERATIONS role, not a brand/marketing one. The core is
  warehouse operations, WMS (Unleashed), international shipment & courier
  coordination, order fulfillment, procurement, inventory management and leading
  a distributed 5-person logistics team (Orlando, Dubai, Warsaw). Paula's core is
  brand/commercial/e-commerce. This is a genuine STRETCH, positioned truthfully
  as adjacent.

Honest overlaps we lean on (all real, in profile.yaml):
  - E-commerce operations run end-to-end: owns a Shopify store (catalogue,
    availability, listings, checkout) and integrates brands into UAE
    quick-commerce (Noon, Talabat, Careem, Deliveroo) — listings, availability,
    promo mechanics and retail execution.
  - Procurement / vendor management: negotiates pricing, terms and distribution
    with distributor networks across 50+ markets; closed high-impact commercial
    deals at Glovo.
  - Cross-functional coordination WITH logistics: at Glovo led cross-functional
    teams across marketing, LOGISTICS and customer support to keep orders flowing
    and volume growing — a direct, honest touchpoint.
  - Data & KPIs: KPI tracking, sell-in/sell-out, forecasting, operational-data
    analysis, Power BI; process improvement (AI automation cut manual workload
    ~40%).
  - Team leadership across geographies: manages/coordinates cross-functional
    teams and 25-50 creators per campaign across an international footprint.

What we DO NOT claim (real gaps — no fabrication):
  - Direct warehouse operations / inventory-in-a-warehouse management.
  - WMS (Unleashed) or any dedicated logistics/order-management system ownership.
  - International shipment / courier-carrier coordination as a core function.
  - Managing a dedicated logistics team. (Framed as cross-functional team +
    creator-team leadership, and as coordinating WITH logistics.)
  Systems gap is handled honestly: "systems-fluent, ramps fast on new platforms"
  backed by Shopify/SAP/Salesforce/Power BI — never a false Unleashed/WMS claim.

Per standing rule: NO "no sponsorship needed" claim — her UAE residence visa is
employer-sponsored. States "already based in Dubai" only.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-18/.
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
from career_ops.generators import cover_letter as cl
from career_ops.generators import cv_generator as cv

COMPANY = "BimmerTech"
TITLE = "E-commerce Logistic Manager"
DATE_FOLDER = "2026-08-18"

# Posting says "Respuestas gestionadas fuera de LinkedIn" and names no hiring
# manager, so the letter stays addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
E-commerce Logistic Manager — BimmerTech, Dubai (UAE). Hybrid, full-time.
BimmerTech is an international e-commerce company selling electronic automotive
upgrades (B2C), with a distributed team across Orlando, Dubai and Warsaw.

Your Responsibilities:
- Manage logistics processes in e-commerce (B2C).
- Coordinate international shipments and collaborate with courier companies and
  logistics providers.
- Oversee the order fulfillment process, including managing the warehouse
  fulfillment team (electronic automotive upgrades).
- Optimize shipping costs and order fulfillment times.
- Supervise warehouse operations and inventory management.
- Coordinate and develop the Warehouse Management System (WMS) – Unleashed.
- Monitor and analyze key performance indicators (KPIs), including on-time
  delivery, product availability, inventory levels, etc.
- Coordinate procurement activities related to logistics, including negotiating
  pricing, terms, and delivery schedules with suppliers.
- Manage a distributed logistics team of five employees located in Orlando,
  Dubai, and Warsaw.
- Analyze operational data and implement improvements to enhance logistics
  efficiency.
- Work closely with the Sales and Technical Support teams.

Requirements:
- At least 3 years of experience in a managerial role in logistics, order
  management, and procurement, preferably within the e-commerce industry.
- Proven experience in team management.
- A proactive mindset with a strong focus on process improvement.
- Ability to work independently, take ownership, and effectively organize both
  personal and team workflows.
- English proficiency at a minimum B2 level (international team).

What We Offer: No dress code, no bureaucracy; lunch at the office twice a week;
an international team of great people.
"""

ATS = [
    "E-commerce", "e-commerce logistics", "logistics", "B2C", "order management",
    "order fulfillment", "fulfillment", "procurement", "supplier negotiation",
    "negotiating pricing", "terms", "delivery schedules", "suppliers",
    "international shipments", "courier", "logistics providers", "shipping costs",
    "warehouse operations", "inventory management", "inventory levels",
    "product availability", "WMS", "warehouse management system",
    "KPIs", "on-time delivery", "operational data", "process improvement",
    "logistics efficiency", "team management", "distributed team",
    "cross-functional", "Sales", "Technical Support", "managerial",
    "ownership", "workflow organization", "Dubai", "UAE", "hybrid", "English",
]

CV_CONTENT = {
    "headline": (
        "E-Commerce Operations & Commercial Manager · Order & Quick-Commerce Ops · "
        "Procurement & Supplier Negotiation · KPIs & Process Improvement"
    ),
    "professional_summary": (
        "E-commerce and commercial manager with 4+ years running online operations end-to-end across "
        "FMCG, Beauty and Quick-Commerce in Dubai and Europe. At DoFreeze I own a Shopify store end-to-end "
        "(catalogue, availability, listings, checkout) and integrate brands into UAE quick-commerce platforms "
        "(Noon, Talabat, Careem, Deliveroo) — managing listings, product availability and retail execution — "
        "while negotiating pricing, terms and delivery with a distributor network across 50+ markets. At Glovo "
        "I led cross-functional teams across marketing, logistics and customer support to keep orders flowing "
        "and volume growing. A data-led operator (KPI tracking, forecasting, operational-data analysis, Power BI) "
        "with a strong process-improvement mindset — I built AI automation that cut manual workload ~40%. "
        "Systems-fluent and quick to ramp on new platforms; comfortable owning workflows and coordinating "
        "distributed international teams. Business Administration graduate, fluent English, already based in Dubai."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Run e-commerce operations end-to-end — own a Shopify store (catalogue, product availability, listings, checkout) and integrate brands into UAE quick-commerce platforms (Noon, Talabat, Careem, Deliveroo), managing listings, availability and retail execution so orders flow reliably across channels",
                "Coordinate procurement and distribution across a 50+ country distributor network — negotiating pricing, terms and delivery schedules with suppliers and partners to keep cost and availability on target",
                "Track operational KPIs (product availability, sell-through, conversion, order performance) and turn the data into concrete process improvements — including AI automation that cut manual workload ~40%",
                "Work independently and own the workflow — organising personal and cross-functional pipelines across marketing, commercial, supply and platform teams to hit go-to-market and availability targets",
                "Coordinate an international, distributed set of partners and teams across GCC, MENA, Asia, Europe, USA and Africa — briefing, aligning and following through across time zones",
                "Lead 6 new-product launches end-to-end (brief, sourcing, pricing, go-to-market), coordinating cross-functional teams from concept through in-market execution",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Led cross-functional teams across marketing, LOGISTICS and customer support to deliver campaigns and increase order volume — a direct, hands-on touchpoint with last-mile delivery operations and fulfillment flow",
                "Managed strategic XL key accounts, using data-led joint planning to grow order volume and keep operations running smoothly at scale on a quick-commerce platform",
                "Negotiated and closed high-impact commercial deals — pricing and terms — maximising profitability for both platform and partners",
                "Helped build Glovo's Retail vertical, onboarding new partners onto the marketplace and standing up the operational setup (listings, availability, order flow) behind them",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Owned 42 key accounts on a major e-commerce platform, coordinating assortment, availability, pricing and promotions to grow GMV +30% QoQ — end-to-end responsibility for catalogue and order performance",
                "Led the Fragrances category as PIC, onboarding 30+ accounts in two months and managing listings, stock availability and go-live operations across the portfolio",
                "Continuously analysed operational and commercial KPIs (conversion, availability, ROI, retention) to sharpen forecasting accuracy and channel performance",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting to the CEO and executing time-critical commercial and availability plans",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out and stock-flow analysis for the chocolate category — early grounding in inventory availability, demand and supply planning",
                "Evaluated promotional effectiveness and built performance reports, translating operational data into actionable improvements",
                "Built management-ready analyses in advanced Excel, feeding forecasting and category planning",
            ],
        },
    ],
    "skills_ecommerce": (
        "e-commerce operations (end-to-end), Shopify store management, order & checkout flow, "
        "product availability & listings, quick-commerce (Noon, Talabat, Careem, Deliveroo), "
        "marketplace operations, retail execution, conversion rate optimisation (CRO), omnichannel"
    ),
    "skills_commercial": (
        "procurement & vendor management, supplier & terms negotiation, pricing & delivery-schedule "
        "negotiation, distributor & partner management, cost optimisation, key account management, "
        "assortment & availability planning, commercial deal negotiation"
    ),
    "skills_data": (
        "operational KPI tracking (availability, on-time, conversion), operational-data analysis, "
        "sell-in/sell-out, demand & supply planning, forecasting, process improvement, "
        "P&L awareness, Power BI, SAP, Salesforce"
    ),
    "skills_brand": (
        "process improvement & workflow ownership, cross-functional team coordination, distributed / "
        "international team leadership, project management (end-to-end launches), stakeholder alignment, "
        "AI-driven automation, proactive problem-solving"
    ),
    "skills_tools": (
        "Shopify, SAP, Salesforce, Power BI, Microsoft Excel (Advanced), Microsoft Office (Expert), "
        "Generative AI (Claude, ChatGPT) for ops automation, Tableau — systems-fluent, fast to ramp on "
        "new platforms incl. WMS/order-management tools"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "I'm writing about your E-commerce Logistic Manager role. What drew me is that it sits exactly at the "
        "intersection I work at every day: running e-commerce operations across an international, distributed "
        "setup — in BimmerTech's case Orlando, Dubai and Warsaw — where availability, procurement and order flow "
        "have to stay tight for a B2C business to keep its promise to customers. I'm already based in Dubai and "
        "immediately available."
    ),
    "body_paragraph_1": (
        "The operational spine of this role maps onto my track. As Brand & Marketing Manager at DoFreeze I run "
        "e-commerce operations end-to-end — owning a Shopify store (catalogue, availability, listings, checkout) "
        "and integrating brands into UAE quick-commerce platforms (Noon, Talabat, Careem, Deliveroo) so orders "
        "flow reliably — while coordinating procurement across a 50+ country distributor network, negotiating "
        "pricing, terms and delivery schedules with suppliers. I track operational KPIs like product availability "
        "and order performance and turn them into process improvements, including AI automation that cut manual "
        "workload ~40%. Earlier, at Glovo, I led cross-functional teams across marketing, logistics and customer "
        "support to keep orders flowing and volume growing on a quick-commerce platform."
    ),
    "body_paragraph_2": (
        "Let me be straight about fit so your time isn't wasted. My strengths for this role are procurement and "
        "supplier negotiation, e-commerce and quick-commerce order operations, operational-data/KPI work, "
        "process improvement and coordinating distributed international teams. What I have not done is run a "
        "physical warehouse or own a WMS such as Unleashed day-to-day — my logistics exposure has been "
        "coordinating with fulfillment and last-mile partners rather than managing a warehouse floor. That said, "
        "I'm systems-fluent (Shopify, SAP, Salesforce, Power BI), I ramp fast on new platforms, and I take "
        "ownership of a workflow end-to-end — so I'd close that gap quickly while contributing on procurement, "
        "KPIs and process from week one."
    ),
    "closing_paragraph": (
        "I'd be glad to bring this blend of e-commerce operations, procurement negotiation and data-led process "
        "improvement to BimmerTech's logistics function, and to lead your distributed Orlando–Dubai–Warsaw team "
        "with the ownership the role asks for. I'm based in Dubai and available to start immediately — I'd welcome "
        "a conversation about how I'd approach tightening fulfillment times, costs and availability. Thank you for "
        "your consideration."
    ),
}


def make_job() -> Job:
    return Job(
        id="bimmertech-ecom-logistic-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/jobs/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "ecommerce remoto últimas 24 horas",
             "function": "Logistics / Operations", "workplace": "Hybrid",
             "note": "Responses managed off-LinkedIn; apply via LinkedIn. No hiring manager named."},
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
        "ai_score": 61,
        "ai_tier": "Warm",
        "skills_match": [
            "E-commerce operations end-to-end (Shopify + UAE quick-commerce)",
            "Order/availability/listing operations across channels",
            "Procurement & supplier negotiation (pricing, terms, delivery — 50+ market distributor network)",
            "Cross-functional coordination WITH logistics (Glovo: marketing/logistics/customer support)",
            "Operational KPI tracking & data analysis (availability, on-time, conversion)",
            "Process improvement (AI automation cut manual workload ~40%)",
            "Distributed / international team coordination",
            "Workflow ownership & independent operation",
            "Systems-fluent (Shopify, SAP, Salesforce, Power BI); fast to ramp",
            "English (C1, well above the B2 asked)",
            "Already based in Dubai; hybrid-ready",
        ],
        "missing_skills": [
            "Direct warehouse operations / physical inventory management (not held — coordinated WITH fulfillment, did not run a warehouse floor)",
            "WMS (Unleashed) or dedicated order-management-system ownership (not held — positioned as fast-to-learn, backed by Shopify/SAP/Salesforce)",
            "International shipment / courier-carrier coordination as a core function (adjacent via quick-commerce order flow, not owned)",
            "Managing a dedicated logistics team (framed as cross-functional + creator-team leadership)",
        ],
        "sector_fit": "adjacent (e-commerce — yes; logistics/warehouse operations — stretch)",
        "seniority_fit": "on-band (4+ yrs vs 3 asked; managerial/ownership scope present)",
        "red_flags": [
            "Role is a LOGISTICS/OPERATIONS manager (warehouse, WMS, shipping, fulfillment team) — outside Paula's brand/commercial core; positioned truthfully as adjacent with an explicit warehouse/WMS gap, no fabrication",
            "Niche B2C vertical (electronic automotive upgrades) — no direct category experience",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Stretch application, positioned honestly. BimmerTech's E-commerce Logistic Manager is an "
            "operations/logistics role — warehouse operations, WMS (Unleashed), international shipment & courier "
            "coordination, order fulfillment, inventory management and leading a distributed 5-person logistics "
            "team — which sits outside Paula's brand/commercial core. The honest overlaps are real and worth "
            "playing: end-to-end e-commerce and quick-commerce operations (Shopify + Noon/Talabat/Careem/"
            "Deliveroo listings, availability, order flow), procurement and supplier negotiation across a 50+ "
            "market distributor network, cross-functional coordination WITH logistics at Glovo, operational-KPI/"
            "data analysis, process improvement (AI automation cut workload ~40%), and distributed international "
            "team coordination — all against a modest 3-yr / B2-English bar she clears. The CV and letter are "
            "upfront about the gaps: she has not run a physical warehouse or owned a WMS such as Unleashed, and "
            "her logistics exposure is coordination with fulfillment/last-mile partners rather than warehouse-floor "
            "management. No warehouse/WMS/shipping-ownership experience is invented; the systems gap is framed as "
            "fast-to-ramp, backed by Shopify/SAP/Salesforce/Power BI. Scored Warm, not Hot, to reflect the genuine "
            "function mismatch."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
    """Convert DOCX -> PDF headlessly via LibreOffice (docx2pdf/Word fails on this Mac)."""
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

    cv_docx = cv._fill_template(CV_CONTENT, job)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, CONTACT)
    cl_pdf = _to_pdf_soffice(cl_docx)
    print("OK_CL", cl_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
