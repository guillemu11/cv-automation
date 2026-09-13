"""One-off: generate Paula's CV + cover letter for Jobgether
"eCom Operations Manager" — a full-time, fully REMOTE role based in the UAE,
listed by Jobgether on behalf of an unnamed partner: a fast-growing
direct-to-consumer (DTC) health & wellness business. Operational leadership:
own day-to-day operations, build/document/optimise SOPs and internal systems,
coordinate supply chain, logistics and core e-commerce operations, remove
bottlenecks, and bring structure to a lean, high-growth global team.

Honest read of fit (adjacent / stretch — a pivot from marketing into operations):
  - Paula's core is Brand / Marketing / Commercial, NOT dedicated operations
    management. This is positioned as a genuine but transferable operational
    thread, never as a held "Operations Manager" title.
  - What genuinely transfers:
      * E-commerce operations: at DoFreeze she runs the Shopify store end-to-end
        (catalogue, listings, product info, stock, pricing, promotions, checkout)
        and integrated brands into UAE quick-commerce (Noon, Talabat, Careem,
        Deliveroo) — onboarding, listings, promo mechanics, retail execution:
        real hands-on e-commerce operational coordination.
      * Systems & SOPs rather than maintenance: she built an AI-powered marketing
        automation system (Claude/GPT) that documents and scales campaign
        planning, content, research and KPI reporting, cutting manual workload
        ~40% — building systems and workflows from the ground up.
      * Cross-functional coordination in fast-paced, high-growth environments:
        Glovo (marketing, logistics, customer support), Miravia (42 accounts),
        DoFreeze (50+ markets) — juggling many moving parts with high autonomy.
      * Logistics/supply-chain-ADJACENT exposure: quick-commerce onboarding and
        Glovo's logistics-heavy operating model — adjacent, not owned end-to-end.
      * High autonomy & ownership: effectively runs DoFreeze's marketing function
        solo, identifying gaps and driving solutions to execution.
  - Honest gaps (stated plainly, never papered over):
      * Not a dedicated operations manager — supply-chain / logistics ownership
        is adjacent to her e-commerce and commercial work, not her core title.
      * Formal, documented SOP/operations-systems discipline at scale is framed
        as "builds and documents systems/automation" (true) — not claimed as a
        formal ops-management track record.
      * Sector: DTC health & wellness is new but adjacent (FMCG / beauty /
        e-commerce); not claimed as health-category experience.
      * Recruiting/hiring support is listed as "an advantage" — light exposure at
        most; not overclaimed.
  - The 3+ years operations/e-commerce requirement is met on the e-commerce side
    (2021 → present across e-commerce/commercial roles); the "operations
    management" flavour is the honest stretch.
  - "Excellent communication" — C1 professional English (stated as such).
  - NO "no sponsorship needed" claim — visa is employer-sponsored (standing rule);
    CV header states only "UAE Residence Visa".

NOTE FOR PAULA/GUILLE: this is a bigger stretch than the Digital Marketing &
E-Commerce Growth Manager role — it's a pivot from marketing into operations. The
package is honest about that. Worth applying (Simple Apply, low cost) but expect it
to read as "strong operator with e-commerce ops + systems-building, pivoting from
marketing", not a like-for-like ops match.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-26/.
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

COMPANY = "Jobgether"
TITLE = "eCom Operations Manager"
DATE_FOLDER = "2026-08-26"

# Jobgether posts on behalf of an unnamed DTC partner — no hiring manager named.
CONTACT = None

JOB_DESCRIPTION = """\
eCom Operations Manager — Jobgether (on behalf of a partner company). United Arab
Emirates. Fully remote, full-time. Fast-growing direct-to-consumer (DTC) health &
wellness business.

Own day-to-day operations within a high-performance environment where priorities
move quickly. Bring structure, clarity and accountability. Combines operational
leadership, process improvement, cross-functional coordination and hands-on problem
solving. Build and improve SOPs, workflows and internal systems that let the business
scale efficiently; identify bottlenecks, coordinate core e-commerce operations, and
turn operational challenges into practical solutions. Work with a lean global team
with significant autonomy and visible impact. Ideal for an operator who enjoys
ownership, moves quickly, and builds systems rather than simply maintaining them.

Accountabilities:
- Own and continuously improve day-to-day business operations, ensuring priorities,
  processes and workflows run efficiently.
- Build, document, implement and optimise SOPs, operational workflows and internal
  systems that support scalable growth.
- Coordinate supply chain, logistics and other critical e-commerce operational
  activities to maintain business continuity.
- Identify operational bottlenecks, inefficiencies and gaps, then develop and
  implement practical solutions.
- Introduce greater organisation, accountability and structure across teams and
  processes.
- Coordinate cross-functional initiatives and keep projects, priorities and
  deliverables moving forward.
- Support recruiting activities, including candidate coordination, interviewing and
  team-growth initiatives.
- Continuously evaluate and evolve operational processes as the business grows.
- Take ownership of operational challenges from identification through execution and
  resolution.

Requirements:
- 3+ years of relevant operations management experience within a direct-to-consumer
  or e-commerce business.
- Proven experience creating, implementing, documenting and continuously improving
  SOPs and operational systems.
- Strong organisational and project-coordination skills; manage multiple priorities
  and moving parts simultaneously.
- Experience in fast-paced, high-growth environments where processes and priorities
  evolve quickly.
- Strong problem-solving and a practical, solutions-oriented approach.
- High degree of autonomy and comfort working with limited supervision.
- Strong ownership mentality — identify problems, take initiative, drive solutions
  through execution.
- Excellent communication and cross-functional collaboration.
- Adaptability, attention to detail and a continuous-improvement mindset.
- Experience supporting hiring and team growth is an advantage.

Benefits: meaningful ownership within a fast-growing DTC health & wellness business;
high autonomy and visibility; build systems, processes and SOPs from the ground up;
fast-paced, execution-focused environment; global team of operators; competitive
compensation (details discussed during hiring).

How Jobgether works: AI-powered matching reviews applications against core
requirements and shares a shortlist with the hiring company; interviews and final
decisions are managed by the partner's internal team.
"""

ATS = [
    "eCom Operations Manager", "e-commerce operations", "operations management",
    "direct-to-consumer", "DTC", "day-to-day operations", "process improvement",
    "SOPs", "standard operating procedures", "workflows", "internal systems",
    "operational systems", "documentation", "scalable growth", "scale",
    "supply chain", "logistics", "business continuity", "bottlenecks",
    "efficiency", "operational excellence", "continuous improvement",
    "cross-functional coordination", "project coordination", "prioritisation",
    "problem solving", "solutions-oriented", "ownership", "accountability",
    "autonomy", "high-growth", "fast-paced", "execution", "structure",
    "Shopify", "e-commerce operations coordination", "catalogue management",
    "product listings", "inventory", "stock", "promotions", "checkout",
    "quick-commerce", "onboarding", "retail execution", "marketing automation",
    "AI automation", "generative AI", "systems building", "reporting",
    "KPI tracking", "communication", "recruiting support", "team growth", "remote",
]

CV_CONTENT = {
    "headline": (
        "E-Commerce Operations & Systems · Shopify + Quick-Commerce Ops · SOPs, "
        "Workflows & AI Automation · Cross-Functional Coordination · High-Ownership Operator"
    ),
    "professional_summary": (
        "Hands-on e-commerce operator with 4+ years running the operational side of fast-growing e-commerce and "
        "FMCG businesses. At DoFreeze I own the Shopify store end-to-end — catalogue, product information, stock, "
        "pricing, promotions and checkout — and integrated brands into UAE quick-commerce platforms (Noon, "
        "Talabat, Careem, Deliveroo), coordinating onboarding, listings, promo mechanics and retail execution. I "
        "build systems rather than maintain them: I designed an AI-powered automation system (Claude/GPT) that "
        "documents and scales planning, content, research and reporting, cutting manual workload ~40%. Across "
        "Glovo and Alibaba's Miravia I coordinated cross-functional operations (logistics, support, marketing, "
        "commercial) in high-growth, fast-moving environments, juggling many priorities with high autonomy and a "
        "strong ownership mentality — identifying bottlenecks and driving solutions through to execution. I'll be "
        "clear that my core has been marketing/commercial and e-commerce rather than a dedicated operations title; "
        "the operational craft — systems, SOPs, coordination and problem-solving — is what I do every day. "
        "Excellent communication (English C1), fully set up for autonomous remote work."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager (E-Commerce Operations & Systems)",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "FMCG e-commerce & distribution | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own core e-commerce operations end-to-end on Shopify — catalogue, product information, stock, pricing, promotions and checkout journey — keeping listings accurate and operations running efficiently across a large multi-brand catalogue and 50+ markets",
                "Built and documented an AI-powered automation system (Claude/GPT) that turns manual, ad-hoc work into repeatable workflows/SOPs for planning, content, research and KPI reporting — cutting manual workload ~40% and letting a lean team scale",
                "Coordinated onboarding of brands into UAE quick-commerce platforms (Noon, Talabat, Careem, Deliveroo) — managing listings, promotional mechanics, stock and retail execution across channels to maintain continuity",
                "Identify operational bottlenecks and gaps across the e-commerce and go-to-market process and drive practical solutions through to execution, with high autonomy and limited supervision",
                "Coordinate cross-functional initiatives across supply/distribution partners, creative and commercial teams — keeping projects, priorities and deliverables moving in a fast-changing environment",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts (Operations & Partner Coordination)",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Coordinated cross-functional operations across marketing, logistics and customer support to launch partners and keep order flow running smoothly in a high-growth, fast-paced quick-commerce environment",
                "Managed strategic XL accounts and onboarded new partners end-to-end — juggling multiple moving parts, priorities and deliverables simultaneously with a hands-on, solutions-oriented approach",
                "Part of the team building Glovo's Retail vertical from the ground up — helping stand up new processes and workflows to expand the marketplace beyond food delivery",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Ran operations for 42 accounts across a large multi-SKU catalogue — assortment, pricing, promotions and channel execution — with the organisation and attention to detail to keep many priorities on track",
                "Owned the Flash Sales channel operationally (Beauty, Fashion & Home), coordinating stock, timing and execution, and onboarded 30+ new stores in two months",
                "Continuously analysed performance data to spot inefficiencies and improve channel operations and forecasting accuracy",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built structured performance reports and sell-in/sell-out analysis for the chocolate category, bringing organisation and repeatable process to category data",
                "Supported NPD launches with data-driven analysis, coordinating inputs across planning and commercial stakeholders",
            ],
        },
    ],
    "skills_brand": (
        "operational ownership & accountability, systems & SOP building, workflow documentation, "
        "process improvement, continuous improvement, bottleneck identification, hands-on problem solving, "
        "building systems (not just maintaining), generative-AI automation"
    ),
    "skills_ecommerce": (
        "e-commerce operations (Shopify end-to-end), catalogue / listings / stock / pricing / promotions, "
        "checkout & customer-journey ops, quick-commerce onboarding (Noon, Talabat, Careem, Deliveroo), "
        "retail execution, marketing & ops automation, reporting systems"
    ),
    "skills_commercial": (
        "cross-functional coordination, project & priority management, partner / vendor coordination, "
        "supply-chain & logistics coordination (adjacent), stakeholder communication, "
        "recruiting & team-growth support, negotiation"
    ),
    "skills_data": (
        "KPI tracking & dashboards, performance & efficiency analysis, forecasting, sell-in/sell-out, ROI, ROAS, "
        "Google Analytics, Power BI, Tableau, Looker, advanced Excel"
    ),
    "skills_tools": (
        "Shopify, Generative AI (Claude, ChatGPT) for automation & SOPs, Google Analytics, Power BI, Tableau, "
        "Looker, Salesforce (CRM), Meta Business Suite, Canva, Microsoft Office — Expert (Excel, PowerPoint, Word); "
        "quick to adopt new ops / project-management tooling"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "The eCom Operations Manager brief — own day-to-day e-commerce operations, build SOPs and systems that let "
        "a lean team scale, remove bottlenecks and turn operational challenges into practical solutions with high "
        "autonomy — describes the operational side of what I do every day. I'm an operator who builds systems "
        "rather than just maintaining them, I'm comfortable owning problems end-to-end, and I'm set up for "
        "autonomous remote work with a global team."
    ),
    "body_paragraph_1": (
        "At DoFreeze I run core e-commerce operations end-to-end: I own the Shopify store — catalogue, product "
        "information, stock, pricing, promotions and checkout — and I coordinated onboarding our brands into UAE "
        "quick-commerce platforms (Noon, Talabat, Careem, Deliveroo), managing listings, promo mechanics, stock "
        "and retail execution across channels. Just as importantly, I build systems: I designed an AI-powered "
        "automation system (Claude/GPT) that turned manual, ad-hoc work into documented, repeatable workflows for "
        "planning, content, research and reporting — cutting manual workload by roughly 40% so a lean team can "
        "scale. Across Glovo and Alibaba's Miravia I coordinated cross-functional operations (logistics, support, "
        "commercial), juggling many priorities in fast-moving, high-growth environments while keeping projects and "
        "deliverables on track."
    ),
    "body_paragraph_2": (
        "I want to be straight about fit. My titles have been in marketing and commercial rather than dedicated "
        "operations, and end-to-end supply-chain/logistics ownership is adjacent to my work rather than my core — "
        "I wouldn't overclaim it. What I bring honestly is the operator's craft the role is really about: owning "
        "e-commerce operations hands-on, building and documenting SOPs and systems from the ground up, coordinating "
        "cross-functional work, spotting bottlenecks and driving solutions to execution, all with a high degree of "
        "autonomy and ownership. The DTC health & wellness sector would be new but adjacent to my FMCG, beauty and "
        "e-commerce background, and I ramp quickly. I have excellent communication (English C1) and a "
        "detail-oriented, continuous-improvement mindset."
    ),
    "closing_paragraph": (
        "I'd welcome a conversation about how I'd approach the first 90 days — mapping the current operations, "
        "documenting the highest-leverage SOPs first, and removing the bottlenecks that most slow the business "
        "down — and about where my e-commerce-operations and systems-building experience is the strongest match. "
        "I'm set up for focused, autonomous remote work across time zones. Thank you for considering my "
        "application."
    ),
}


def make_job() -> Job:
    return Job(
        id="jobgether-ecom-operations-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="United Arab Emirates · Fully remote",
        url="https://www.linkedin.com/jobs/search/?keywords=Jobgether%20eCom%20Operations%20Manager",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Jobgether eCom Operations Manager UAE remote DTC health wellness",
             "function": "E-Commerce Operations (SOPs, systems, coordination, supply-chain/logistics)",
             "workplace": "Fully remote (UAE-based)",
             "note": "Jobgether = platform posting on behalf of an unnamed DTC health & wellness partner; AI-shortlist model; no hiring manager named; salary not disclosed. 100+ applicants — competitive. This is an operations pivot from Paula's marketing/commercial core."},
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
        "salary_raw": "Not disclosed (fully remote, UAE)",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 58,
        "ai_tier": "Warm (pivot: marketing → operations)",
        "skills_match": [
            "Owns core e-commerce operations end-to-end today on Shopify (catalogue, listings, stock, pricing, promotions, checkout)",
            "Builds SYSTEMS not just maintenance — designed an AI automation system (Claude/GPT) that documents & scales workflows, -40% manual workload",
            "Quick-commerce onboarding & retail execution (Noon, Talabat, Careem, Deliveroo) — hands-on e-commerce operational coordination",
            "Cross-functional coordination in fast-paced, high-growth environments (Glovo: logistics/support/marketing; Miravia: 42 accounts)",
            "High autonomy & strong ownership mentality — effectively runs DoFreeze's function solo, identifies gaps, drives solutions to execution",
            "Manages multiple priorities / moving parts simultaneously with organisation and attention to detail",
            "Meets 3+ years e-commerce/commercial requirement (2021 → present)",
            "Excellent communication (English C1); set up for autonomous remote work with a global team",
        ],
        "missing_skills": [
            "NOT a dedicated operations manager — her titles are marketing/commercial; supply-chain/logistics OWNERSHIP is adjacent, not core (framed honestly, not claimed)",
            "Formal, documented SOP/operations-systems discipline at scale — she builds & documents systems/automation (true) but not as a formal ops-management track record",
            "DTC health & wellness sector — new but adjacent to FMCG/beauty/e-commerce; not claimed as health-category experience",
            "Recruiting / hiring support ('an advantage') — light exposure at most; not overclaimed",
            "Dedicated supply-chain / inventory-planning tooling & process depth — adjacent via quick-commerce & Shopify ops, not owned",
        ],
        "sector_fit": "adjacent — DTC health & wellness e-commerce is close to her FMCG/beauty/e-commerce background; the ROLE FUNCTION (operations) is the real pivot from her marketing/commercial core",
        "seniority_fit": "on-band on seniority (Manager-level, 3+ yrs met); the stretch is disciplinary (operations vs marketing), handled honestly",
        "red_flags": [
            "PIVOT ROLE — operations, not marketing. Paula's genuine thread is e-commerce ops + systems-building + coordination, but this is a career-adjacent stretch, not a like-for-like match",
            "Supply chain / logistics coordination named as a core accountability — adjacent to her experience, not owned end-to-end",
            "100+ applicants (competitive); AI-shortlist model against 'core requirements' that centre on operations-management experience she frames honestly",
            "Salary not disclosed — cannot confirm against her 20,000 AED/month floor",
            "Unnamed DTC partner — company, product and comp opaque until first call",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Warm but honest PIVOT fit — a career-adjacent stretch from Paula's marketing/commercial core into an "
            "operations role, worth applying (Simple Apply, low cost) with truthful positioning. The role owns "
            "day-to-day e-commerce operations for a DTC health & wellness business: build/document/optimise SOPs, "
            "workflows and internal systems; coordinate supply chain, logistics and core e-commerce ops; remove "
            "bottlenecks; and bring structure with high autonomy. Paula's genuine transferable thread is strong on "
            "the e-commerce-operations and systems-building axis: she owns the Shopify store end-to-end (catalogue, "
            "listings, stock, pricing, promotions, checkout), coordinated quick-commerce onboarding and retail "
            "execution (Noon/Talabat/Careem/Deliveroo), and — crucially for 'builds systems rather than maintains "
            "them' — designed an AI automation system that documents and scales workflows (-40% manual work). Her "
            "cross-functional coordination in high-growth environments (Glovo logistics/support, Miravia 42 "
            "accounts) and high-autonomy ownership fit the operator profile. Honest gaps, stated plainly: she is "
            "not a dedicated operations manager; supply-chain/logistics ownership is adjacent not core; formal "
            "ops-SOP discipline is framed as systems/automation building (true); DTC health & wellness is a new but "
            "adjacent sector; recruiting support is minimal. CV + letter lead with the e-commerce-ops and "
            "systems-building craft, coordination and ownership, and openly name the marketing→operations pivot and "
            "the supply-chain adjacency — no fabricated ops-manager title or logistics ownership, no native-English "
            "or 'no sponsorship needed' claim."
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
