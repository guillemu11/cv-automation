"""One-off: generate Paula's CV + cover letter for The Body Shop
"Franchise Coordinator" (Dubai, Hybrid — Retail / Franchise Operations).

HONEST FIT NOTE (read before editing):
  This is a franchise-OPERATIONS / COORDINATION role: acting as the point of
  coordination between international franchise partners and internal teams
  (Supply Chain, Finance, Retail, Business Management), maintaining high-quality
  data and reporting, and keeping multi-market day-to-day operations running.
  Tools named explicitly: Excel, SAP, Power BI. Sector: retail / wholesale /
  FMCG / fashion / beauty. Paula's core is brand/commercial/e-commerce, but the
  overlap here is genuinely strong on SECTOR and on DATA + MULTI-MARKET PARTNER
  COORDINATION. Two honest caveats, handled in the letter without over-apology:
    1. She has coordinated DISTRIBUTOR and KEY-ACCOUNT partners across markets,
       not a formal franchisor–franchisee franchise network. Framed as the
       direct, adjacent analog — never claimed as literal franchise experience.
    2. The title is a Coordinator; she is currently a Manager. She OVER-indexes
       on seniority (an asset, not a gap) — the letter frames it as bringing
       manager-level rigour to a coordination remit.

Honest overlaps we lean on (all real, in profile.yaml):
  - Multi-market coordination: distributor + partner network across 50+ countries
    (GCC, MENA, Asia, Europe, USA, Africa) at DoFreeze.
  - Point-of-contact partner management: single POC for 42 key accounts at
    Miravia (Alibaba) — beauty, fragrances, fashion — GMV +30% QoQ.
  - Cross-functional coordination WITH Supply/Finance/Commercial/Retail: led
    cross-functional teams across marketing, logistics and customer support at
    Glovo; aligns commercial/supply/finance at DoFreeze.
  - Data accuracy & reporting: sell-in/sell-out analysis + performance reports at
    Mondelez; KPI/ROI/conversion reporting at Miravia; Power BI.
  - Named systems held for real: Microsoft Excel (Expert), SAP, Power BI.
  - Sector: FMCG (Mondelez, DoFreeze), Beauty & Fragrances (Miravia PIC
    Fragrances, DoFreeze), Fashion retail (Inditex / Massimo Dutti, Miravia
    Fashion). The Body Shop = beauty/retail — a real, strong sector match.
  - Retail-floor grounding: Inditex (Massimo Dutti) — retail operations & visual
    merchandising (woven into the summary).

What we DO NOT claim (real gaps — no fabrication):
  - Formal franchise (franchisor–franchisee) operations ownership — framed as
    adjacent distributor/key-account partner coordination.
  - No invented SAP/Power BI depth beyond what profile.yaml holds.

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

COMPANY = "The Body Shop"
TITLE = "Franchise Coordinator"
DATE_FOLDER = "2026-08-18"

# Posting is recruiter-promoted, "responses managed off LinkedIn", no hiring
# manager named -> letter stays addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Franchise Coordinator — The Body Shop, Dubai (UAE). Hybrid, full-time.

For over 50 years, The Body Shop has challenged convention — proving that
business can be a force for good. As we continue to evolve and grow globally, our
Dubai hub plays a key role in connecting markets, strengthening operations and
supporting our international franchise network.

We're now hiring a Franchise Co-ordinator to join the team in Dubai and support
franchise operations across multiple international markets. This is an exciting
opportunity for someone with experience in retail, wholesale, FMCG, fashion or
beauty environments who enjoys working with data, systems and stakeholders in a
fast-paced, global business.

You'll act as a key point of coordination between franchise partners and internal
teams, supporting day-to-day operations, maintaining high-quality data and
reporting, and helping ensure our markets receive the support they need to
succeed. Working closely with teams across Supply Chain, Finance, Retail and
Business Management, you'll build strong relationships across multiple functions
and geographies while contributing to the smooth operation of our franchise
network.

We're looking for someone who is highly organised, detail-oriented and confident
using tools such as Excel, SAP and Power BI, with the ability to manage data
accurately while communicating effectively with a wide range of stakeholders.

If you're looking to develop your career in an international retail business and
play a key role in supporting global franchise operations, we'd love to hear from
you. Be part of a new chapter — helping to connect markets, support partners and
drive operational excellence across our franchise network.
"""

ATS = [
    "franchise operations", "franchise coordinator", "franchise network",
    "franchise partners", "retail operations", "retail", "wholesale", "FMCG",
    "fashion", "beauty", "international markets", "multi-market", "coordination",
    "point of coordination", "day-to-day operations", "operational excellence",
    "data", "reporting", "high-quality data", "data accuracy", "data management",
    "Excel", "SAP", "Power BI", "systems", "stakeholder management", "stakeholders",
    "Supply Chain", "Finance", "Business Management", "cross-functional",
    "highly organised", "detail-oriented", "relationship building",
    "Dubai", "UAE", "hybrid", "English",
]

CV_CONTENT = {
    "headline": (
        "Commercial & Retail Operations Coordinator · Multi-Market Partner Management · "
        "Data & Reporting (Excel · SAP · Power BI) · FMCG · Beauty · Fashion"
    ),
    "professional_summary": (
        "Highly organised commercial and retail professional with 4+ years across FMCG, Beauty and Fashion, "
        "coordinating partners, data and stakeholders across fast-paced multi-market operations. At DoFreeze I "
        "coordinate a distributor and partner network across 50+ countries (GCC, MENA, Asia, Europe, USA, Africa), "
        "acting as the link between partners and internal commercial, supply and finance teams while keeping "
        "listings, pricing and reporting accurate. At Miravia (Alibaba) I was the single point of contact for 42 "
        "key accounts across beauty, fragrances and fashion, growing GMV +30% QoQ while owning assortment, data and "
        "performance reporting. Confident with Excel (Expert), SAP and Power BI and detail-obsessed on data quality; "
        "Inditex-trained in retail operations and visual merchandising from the shop floor up. Bilingual "
        "Spanish/English (C1), already based in Dubai."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Act as the point of coordination between a distributor and partner network across 50+ countries (GCC, MENA, Asia, Europe, USA, Africa) and internal teams — commercial, supply and finance — keeping day-to-day operations running smoothly across markets",
                "Maintain high-quality data and reporting across the portfolio — product listings, pricing, availability and KPI dashboards — with a detail-first approach to data accuracy that leadership relies on to steer the business",
                "Work cross-functionally with supply, finance and commercial teams to align forecasts, pricing and go-to-market across a 50+ market footprint, ensuring each market gets the support it needs",
                "Manage listings and retail execution across UAE retail and quick-commerce channels (modern trade, Noon, Talabat, Careem, Deliveroo), keeping catalogue, availability and promotional data accurate",
                "Built AI-powered automation for reporting and market research that cut manual workload ~40% — improving data turnaround, consistency and accuracy",
                "Coordinate 6 new-product launches end-to-end, aligning briefs, pricing and timelines across international markets and functions",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Single point of contact for 42 key-account partners across beauty, fragrances and fashion — coordinating partners and internal teams to grow GMV +30% QoQ through assortment, pricing and promotions",
                "Led the Fragrances category as PIC, onboarding 30+ partners in two months — coordinating listings, data quality and go-live across the portfolio, including leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
                "Built and maintained performance reporting (conversion, ROI, retention, availability) that steered commercial decisions and sharpened forecasting accuracy",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting directly to the CEO and coordinating time-critical commercial and stock plans across functions",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Coordinated cross-functional teams across marketing, logistics and customer support to keep operations running and order volume growing at scale",
                "Managed strategic XL key-account partners (KFC, Taco Bell, La Tagliatella, Sushi Shop), using data-led joint planning to grow volume and keep day-to-day operations smooth",
                "Helped build Glovo's Retail vertical — onboarding fashion and lifestyle partners and standing up the operational setup (listings, availability, order flow) behind them",
                "Negotiated and closed commercial deals — pricing and terms — maximising profitability for both platform and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out analysis and built performance reports for the chocolate category — grounding in data accuracy, reporting and category operations",
                "Evaluated promotional effectiveness and produced management-ready analyses in advanced Excel, feeding forecasting and category planning",
                "Identified growth opportunities that fed successful NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    # Skills reoriented for a franchise-coordination remit; systems the JD names
    # (Excel, SAP, Power BI) pushed to the front of tools.
    "skills_commercial": (
        "multi-market partner coordination, distributor & key-account management, franchise/partner network "
        "support, stakeholder management, relationship building across functions & geographies, "
        "assortment & availability planning, pricing, negotiation, category management"
    ),
    "skills_data": (
        "high-quality data management & data accuracy, reporting & dashboards, KPI tracking, sell-in/sell-out, "
        "performance & commercial reporting, forecasting, P&L awareness, Power BI, SAP, advanced Excel"
    ),
    "skills_brand": (
        "highly organised & detail-oriented operations coordination, cross-functional coordination "
        "(Supply Chain, Finance, Retail, Commercial), project management (end-to-end launches), "
        "process improvement & AI-driven automation, retail operations & visual merchandising (Inditex-trained)"
    ),
    "skills_ecommerce": (
        "retail & e-commerce operations, listings & catalogue management, retail execution, "
        "quick-commerce (Noon, Talabat, Careem, Deliveroo), omnichannel, Shopify store management"
    ),
    "skills_tools": (
        "Microsoft Excel (Expert), SAP, Power BI, Microsoft Office (Expert), Salesforce, Tableau, "
        "Generative AI (Claude, ChatGPT) for reporting automation — systems-fluent, fast to ramp on new tools"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "I'm writing about your Franchise Coordinator role. What draws me is that The Body Shop's Dubai hub sits "
        "exactly where I like to work — the point that connects international markets and keeps a global partner "
        "network supported day to day — for a brand that has spent 50 years proving business can be a force for "
        "good. I coordinate multi-market partners, data and stakeholders for a living, I'm already based in Dubai, "
        "and I'm immediately available."
    ),
    "body_paragraph_1": (
        "The core of this role maps directly onto my track. As Brand & Marketing Manager at DoFreeze I act as the "
        "link between a distributor and partner network across 50+ countries (GCC, MENA, Asia, Europe, USA, Africa) "
        "and internal commercial, supply and finance teams — keeping listings, pricing and reporting accurate so "
        "each market gets what it needs to run. Before that, at Miravia (Alibaba Group) I was the single point of "
        "contact for 42 key-account partners across beauty, fragrances and fashion, growing GMV +30% QoQ while "
        "owning assortment, data quality and performance reporting. Maintaining high-quality data is second nature: "
        "I built performance reports at Mondelez and Miravia, work in Power BI and SAP, and I'm an expert-level "
        "Excel user — the three tools your brief calls out."
    ),
    "body_paragraph_2": (
        "Two things worth being straight about. First, my partner coordination has been with distributor and "
        "key-account partners rather than a formal franchisor–franchisee network — a close, honest analog, and I'd "
        "pick up the franchise specifics quickly given how similar the coordination, data and stakeholder work is. "
        "Second, I currently sit at manager level, so I'd bring that rigour and ownership to a coordination remit "
        "rather than needing to grow into it. What I add on top: a genuine beauty, FMCG and fashion-retail "
        "background (including Inditex retail training at Massimo Dutti), hands-on UAE market experience, and "
        "bilingual Spanish/English — useful across an international franchise footprint."
    ),
    "closing_paragraph": (
        "I'd love to help The Body Shop's Dubai hub connect markets, support partners and keep franchise operations "
        "running cleanly — with the organised, detail-first, data-accurate approach the role asks for. I'm based in "
        "Dubai and available to start immediately, and I'd welcome a conversation about how I'd support your "
        "international markets from day one. Thank you for your consideration."
    ),
}


def make_job() -> Job:
    return Job(
        id="thebodyshop-franchise-coordinator-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/jobs/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "ecommerce remoto últimas 24 horas",
             "function": "Retail / Franchise Operations", "workplace": "Hybrid",
             "note": "Recruiter-promoted; responses managed off-LinkedIn; apply via LinkedIn. No hiring manager named."},
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
        "ai_score": 68,
        "ai_tier": "Warm",
        "skills_match": [
            "Multi-market partner coordination (distributor/partner network across 50+ countries at DoFreeze)",
            "Point-of-contact partner management (42 key accounts at Miravia — beauty/fragrances/fashion)",
            "Cross-functional coordination WITH Supply/Finance/Commercial/Retail (Glovo + DoFreeze)",
            "High-quality data & reporting; data-accuracy focus (Mondelez sell-in/out, Miravia KPI reporting)",
            "Named systems held: Microsoft Excel (Expert), SAP, Power BI",
            "Strong sector fit: FMCG + Beauty & Fragrances + Fashion retail (Mondelez/DoFreeze/Miravia/Inditex)",
            "Retail-floor operations & visual merchandising grounding (Inditex / Massimo Dutti)",
            "Highly organised, detail-oriented, stakeholder communication across geographies",
            "English (C1) + native Spanish; already based in Dubai; hybrid-ready",
        ],
        "missing_skills": [
            "Formal franchise (franchisor–franchisee) operations ownership (not held — positioned honestly as adjacent distributor/key-account partner coordination, fast to learn)",
            "SAP/Power BI depth is working-level, not specialist (held for real, not overstated)",
        ],
        "sector_fit": "strong (beauty/retail/FMCG/fashion all present — direct match to The Body Shop)",
        "seniority_fit": "over-qualified on level (currently Manager applying to a Coordinator title) — framed as bringing manager-level rigour",
        "red_flags": [
            "Title is a Coordinator while Paula is a Manager — down-level on paper; framed as an asset (rigour/ownership), not hidden",
            "Franchise-specific operating model is adjacent, not identical, to her distributor/key-account coordination — stated plainly in the letter, no fabrication",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Solid, honest fit. The Body Shop's Franchise Coordinator is a retail/franchise-operations coordination "
            "role — point of contact between international franchise partners and internal teams (Supply Chain, "
            "Finance, Retail, Business Management), maintaining high-quality data and reporting, confident with "
            "Excel, SAP and Power BI, in a retail/wholesale/FMCG/fashion/beauty environment. Paula matches strongly "
            "on sector (FMCG via Mondelez/DoFreeze, Beauty & Fragrances via Miravia PIC Fragrances, Fashion retail "
            "via Inditex/Massimo Dutti and Miravia) and on the substance of the work: multi-market partner "
            "coordination across a 50+ country network, single-POC key-account management for 42 partners, "
            "cross-functional coordination with supply/finance/commercial, and data-accuracy-first reporting — with "
            "the exact tools named (Excel Expert, SAP, Power BI). Two honest caveats are stated in the letter rather "
            "than papered over: her partner coordination has been distributor/key-account rather than a formal "
            "franchise network (a close adjacent), and she over-indexes on seniority (Manager applying to a "
            "Coordinator title), framed as bringing manager-level rigour. No franchise experience is fabricated and "
            "no systems depth is overstated. Scored Warm for the level mismatch and franchise-model adjacency, but "
            "high within Warm given the strong sector and skills overlap."
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
