"""One-off: generate Paula's CV + cover letter for Ounass
"Creative Operations Manager" (Dubai, Hybrid — Al Tayer Group luxury e-commerce).

Why this is a real (if stretch) fit:
  - The gravitational centre of this JD is *leading the AI & automation agenda*
    of the Creative department plus *workflow / process design, SOPs, SLAs and
    project/resource management* — which is precisely Paula's sharpest, rarest
    edge. At DoFreeze she BUILT and owns an AI-powered marketing-automation
    system (Claude / generative AI) that turned planning, content, research and
    reporting into repeatable workflows, cutting manual workload ~40% and scaling
    output across 50+ markets without adding headcount.
  - She designs/documents briefing formats, templates and approval flows, runs
    end-to-end project management (6 NPD launches), plans resourcing across
    always-on + seasonal peaks, and briefs/coordinates 25-50 creators plus
    cross-functional teams per campaign — the operational backbone this role asks
    for.
  - She grew up inside luxury/fashion e-commerce (Inditex/Massimo Dutti, Alibaba's
    Miravia beauty/fashion/fragrance marketplace) and runs a Shopify store
    end-to-end (catalogue, collections, asset structuring) — DAM-adjacent.

Honest positioning (NO fabrication):
  - Paula is NOT a hands-on creative/designer and has NOT run a formal creative-
    production department or owned a DAM platform. Framed truthfully as the
    *operating system around creative* (workflow, SOPs, resourcing, PM, KPIs, AI
    tooling), never as a designer or creative-ops department head.
  - NO invented Adobe Creative Suite command — her hands-on design is Canva +
    generative-AI tools. NO invented DAM platform ownership; catalogue/asset
    structuring on Shopify is positioned as adjacent, not as DAM administration.
  - Tenure gap is real (4+ yrs vs 7+ asked) — acknowledged in the cover letter,
    not hidden.
  - Per standing rule, NO "no sponsorship needed" claim — her UAE residence visa
    is employer-sponsored. States "already based in Dubai" only.

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

COMPANY = "Ounass"
TITLE = "Creative Operations Manager"
DATE_FOLDER = "2026-08-18"

# Responses managed outside LinkedIn (Al Tayer / Ounass career portal); no hiring
# manager named in the posting, so the letter stays addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Creative Operations Manager — Ounass (Al Tayer Group), Dubai, UAE. Hybrid,
full-time. Luxury e-commerce (fashion, beauty, watches, home, jewelry); 500+
team; digital-first, high-AOV GCC platform.

Lead the operational engine behind the Creative department — driving scale,
efficiency and workflow excellence. In partnership with the Head of Creative and
Editorial, own end-to-end creative operations: resourcing, workflow design,
process improvement, and the adoption of AI and automation — enabling the team to
produce more, move faster and work smarter without compromising creative
standards. Think in systems as well as projects.

Strategic:
- Strategic and operational right hand to the Head of Creative; translate strategy
  into scalable systems, workflows and resourcing models.
- Lead the department's AI and automation agenda; position Creative at the
  forefront of technology-enabled production.
- Prioritise process improvement across the creative lifecycle; scale output
  without scaling headcount at the same rate.
- Own the Digital Asset Management (DAM) platform as a strategic asset.

Creative Operations & Workflow:
- Own and optimise end-to-end workflow (brief intake -> production -> review ->
  approval -> asset delivery); make every stage efficient, trackable, scalable.
- Design, document and maintain standardised processes, templates, briefing
  formats and approval flows.
- Implement SOPs and define/monitor SLAs for turnaround and delivery.
- Translate creative/content priorities into resourcing plans and delivery
  timelines; act as operational backbone of the department.

AI & Automation:
- Identify, evaluate and implement AI-driven tools and automation across the
  creative pipeline (generative design, automated resizing/localisation, asset
  tagging, briefing and review tools).
- Build and own the AI tooling roadmap with Technology and Product.
- Train and upskill the creative team on AI-enabled workflows; establish
  guardrails, quality checks and brand-safety processes for AI-assisted output.

DAM Ownership:
- Own the DAM system end-to-end (governance, taxonomy, metadata, permissions,
  administration) as single source of truth.
- Define/enforce metadata, tagging and naming conventions; drive adoption across
  Creative, Editorial, Marketing.
- Evaluate AI-powered DAM capabilities (auto-tagging, visual search); own vendor
  relationships and the DAM roadmap.

Resource, Capacity & Project Management:
- Manage resource planning and capacity across design/content production
  (always-on BAU vs campaign/seasonal peaks); flag bottlenecks and delivery risk.
- Implement project/workflow management systems giving full visibility of status,
  workload and throughput.

Process Improvement & Performance:
- Define/track operational KPIs (turnaround time, throughput, cost per asset,
  rework rate, tool adoption); audit processes; lead change.

Cross-Functional & People:
- Partner with Editorial, Brand/Digital Marketing, Product/UX and Technology.
- Lead the Creative Operations function; conduct reviews; build a culture of
  accountability, efficiency and continuous improvement; champion AI fluency.

What we're looking for:
- Bachelor's/Master's in Operations, Business, Design, Marketing or related.
- 7+ years in creative operations, production management, project management or
  similar operational leadership, ideally luxury/fashion/retail/e-commerce.
- Proven design/implementation of workflow, process and automation improvements
  at scale.
- Strong hands-on experience with AI and automation tools for creative production
  (generative design/image tools, automated workflow platforms, AI-assisted
  content/asset management).
- Experience managing resources, budgets, timelines and concurrent projects.
- Strong knowledge of project/workflow platforms (Asana, Monday.com, Wrike,
  Airtable) and DAM systems.
- Background in design/hands-on creative production with practical Adobe Creative
  Suite knowledge, to credibly guide creative teams.
- SOPs, SLAs, operational standards; analytical/problem-solving; stakeholder
  management, communication, people leadership; change management.
- Highly organised, detail-oriented, comfortable in a fast-paced creative
  environment.
"""

ATS = [
    "Creative Operations", "Creative Operations Manager", "creative operations",
    "production management", "project management", "workflow", "workflow design",
    "workflow excellence", "process improvement", "process design",
    "standardised processes", "templates", "briefing formats", "approval flows",
    "SOPs", "Standard Operating Procedures", "SLAs", "brief intake",
    "asset delivery", "AI", "automation", "AI and automation", "AI agenda",
    "AI tooling roadmap", "generative design", "generative AI", "automated workflow",
    "AI-assisted content", "upskilling", "guardrails", "brand safety",
    "Digital Asset Management", "DAM", "taxonomy", "metadata", "tagging",
    "naming conventions", "asset management", "resource planning", "capacity planning",
    "resourcing", "seasonal peaks", "bottlenecks", "delivery risk",
    "project/workflow management systems", "Asana", "Monday.com", "Wrike", "Airtable",
    "operational KPIs", "turnaround time", "throughput", "cost per asset",
    "rework rate", "tool adoption", "change management", "stakeholder management",
    "cross-functional", "people leadership", "continuous improvement",
    "luxury", "fashion", "e-commerce", "retail", "budgets", "timelines",
    "concurrent projects", "Adobe Creative Suite", "Canva", "Dubai", "GCC", "UAE",
]

CV_CONTENT = {
    "headline": (
        "Creative & Content Operations · AI & Automation Lead · Workflow, Process & SOP Design · "
        "Project & Resource Management · Luxury / Fashion E-Commerce"
    ),
    "professional_summary": (
        "Systems-minded marketing and operations professional with 4+ years across E-Commerce, Beauty, "
        "Fashion and FMCG, specialising in AI-enabled ways of working and scalable content and campaign "
        "production. At DoFreeze I built and own an AI-powered marketing-automation system (Claude / "
        "generative AI) that turned campaign planning, content, research and reporting into standardised, "
        "repeatable workflows — cutting manual workload ~40% and letting a lean team produce more, faster, "
        "without adding headcount. I design and document processes, briefing formats and approval flows, run "
        "content and campaign production end-to-end (brief to delivery), and plan resourcing across always-on "
        "and seasonal peaks — coordinating 25–50 creators plus cross-functional teams against tight, "
        "concurrent deadlines. Trained inside luxury/fashion e-commerce (Alibaba's Miravia; Inditex / Massimo "
        "Dutti) and fluent in catalogue, collections and asset workflows. Business Administration graduate, "
        "already based in Dubai."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Built and own an AI-powered marketing-automation system (Claude / generative AI) that turned campaign planning, content creation, market research and KPI reporting into standardised, repeatable workflows — cutting manual workload ~40% and scaling output across 50+ markets without adding headcount at the same rate",
                "Designed, documented and maintain the content and campaign production process end-to-end — brief intake, templates, briefing formats, review and approval flows — reducing rework and keeping delivery trackable, on-time and scalable",
                "Evaluate, pilot and roll out generative-AI and automation tools (generative design, content generation, automated reporting), training the team to embed them into day-to-day ways of working rather than treat them as side projects",
                "Lead end-to-end project management for 6 NPD launches (brief → packaging → go-to-market), coordinating cross-functional design, product and commercial teams against tight, concurrent timelines",
                "Plan resourcing and capacity across always-on demand and campaign/seasonal peaks — briefing and managing 25–50 external creators per campaign plus content, sampling and production schedules across channels",
                "Own the Shopify e-store's catalogue, collections and content — structuring, tagging and reusing product assets across campaigns and channels for fast, consistent go-to-market",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global luxury/fashion & beauty e-commerce | 100K+ employees",
            "bullets": [
                "Ran high-volume campaign and content production across 42 beauty, fragrance and fashion accounts on a luxury/fashion marketplace — coordinating merchandising, creative and content output against a demanding calendar",
                "Created and led the Beauty Club and 'Hot on Social' content projects end-to-end — briefing, production and delivery — boosting brand visibility and positioning the platform as a beauty and lifestyle destination",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, running deadline-driven campaign production and asset delivery across many concurrent brand activations",
                "Partnered cross-functionally with marketing, design and commercial teams to align creative and content output with campaign calendars and business priorities",
                "Tracked conversion, traffic, retention and ROI to prioritise work and continuously improve how campaigns and content were planned and delivered",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Coordinated cross-functional teams across marketing, design, logistics and support to deliver campaigns and activations on time in a fast-moving marketplace",
                "Ran multiple concurrent projects from brief to live — bespoke marketing activations and content for strategic XL accounts",
                "Helped build Glovo's Retail vertical — standing up new partner-onboarding and content workflows to bring fashion and lifestyle brands onto the platform at scale",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built performance reports and sell-in/sell-out analysis for the chocolate category, turning data into KPIs and recommendations for planning",
                "Supported NPD launches (Milka Spread, Mini Suchard) from concept to shelf — early grounding in end-to-end project coordination",
                "Produced management-ready analyses in advanced Excel, translating category and market data into clear, actionable outputs",
            ],
        },
    ],
    "skills_brand": (
        "creative & content operations, content production workflows, brief / template / approval-flow design, "
        "SOPs & process documentation, SLAs & turnaround standards, resource & capacity planning, campaign & "
        "production project management, go-to-market, A&P budget management"
    ),
    "skills_ecommerce": (
        "luxury & fashion e-commerce, Shopify catalogue & collections, digital asset & catalogue structuring "
        "(taxonomy, tagging, reuse), UAE quick-commerce (Noon, Talabat, Careem, Deliveroo), omnichannel "
        "content, conversion rate optimisation (CRO)"
    ),
    "skills_commercial": (
        "cross-functional stakeholder management, vendor & partner management, change management, "
        "people & team leadership, key account management, negotiation"
    ),
    "skills_data": (
        "operational KPIs (turnaround time, throughput, rework rate, tool adoption), process & bottleneck "
        "analysis, performance reporting, forecasting, P&L management, ROI / ROAS, Power BI"
    ),
    "skills_tools": (
        "Generative AI (Claude, ChatGPT), Shopify, Canva, project & workflow management platforms "
        "(Asana / Monday.com / Trello-style), Meta Business Suite, Power BI, Salesforce, SAP, "
        "Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Ounass is building a creative operation that produces more, moves faster and works smarter by putting "
        "AI and automation at its core — and that is exactly the problem I spend my days solving. As the "
        "definitive home of luxury in the Middle East and part of the Al Tayer Group, you pair a digital-first, "
        "high-AOV e-commerce engine with genuinely high creative standards, and the Creative Operations Manager "
        "role — owning workflow, process, resourcing and the AI agenda behind the Creative team — maps directly "
        "onto how I already work."
    ),
    "body_paragraph_1": (
        "At DoFreeze I built and own an AI-powered marketing-automation system (Claude / generative AI) that "
        "turned campaign planning, content, research and reporting into standardised, repeatable workflows — "
        "cutting manual workload by around 40% and letting a lean team scale output across 50+ markets without "
        "adding headcount at the same rate. I design and document the briefing formats, templates and approval "
        "flows behind our content and campaign production, run end-to-end project management on six NPD "
        "launches, and plan resourcing across always-on and seasonal peaks — briefing and coordinating 25–50 "
        "creators and cross-functional teams against tight, concurrent deadlines. Before that, at Alibaba's "
        "Miravia, I ran high-volume campaign and content production across 42 beauty, fashion and fragrance "
        "accounts on a luxury/fashion marketplace."
    ),
    "body_paragraph_2": (
        "Two things make me a strong fit for how you want this role to work. First, I am genuinely AI-first — "
        "not someone who will 'explore' automation, but someone who has already built it, embedded it in a "
        "team's daily workflow and trained others on it, which is precisely the AI-and-automation agenda this "
        "role is built around. Second, I grew up inside fashion and e-commerce — Inditex/Massimo Dutti, "
        "Alibaba's Miravia and a Shopify store I run end-to-end — so luxury standards, catalogue, collections "
        "and asset workflows are native to me. I'll be candid on two points: my background is in brand, content "
        "and e-commerce operations rather than a formal creative-production department, and my hands-on design "
        "is in Canva and generative-AI tools rather than deep Adobe craft. What I bring is the operating system "
        "around creative — the workflows, SOPs, resourcing, project management, KPIs and AI tooling that free "
        "creative talent to focus on the work — and I ramp fast."
    ),
    "closing_paragraph": (
        "I would be excited to bring this blend of AI-and-automation fluency, systems thinking and luxury "
        "e-commerce experience to the Creative Operations function at Ounass, and to help the team produce more "
        "and move faster without compromising the standards that define the brand. I am already based in Dubai "
        "and available immediately, and I would welcome the chance to discuss how I would approach your creative "
        "workflows, DAM and AI roadmap. Thank you for your consideration — I look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="ounass-creative-operations-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.altayer.com/careers",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Creative Operations Manager",
             "function": "Creative Operations", "workplace": "Hybrid",
             "group": "Al Tayer Group",
             "note": "Responses managed outside LinkedIn — apply via Al Tayer / Ounass career portal"},
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
        "ai_score": 66,
        "ai_tier": "Warm",
        "skills_match": [
            "AI & automation agenda — BUILT and owns an AI marketing-automation system (Claude), embedded in team workflow, trained others (rare, direct, central to this JD)",
            "Workflow / process / SOP design — briefing formats, templates, approval flows, ~40% manual-workload cut",
            "End-to-end project management (6 NPD launches) + concurrent deadlines",
            "Resource & capacity planning across always-on + seasonal peaks (25–50 creators/campaign)",
            "Content & campaign production coordination (Miravia Beauty Club, Hot on Social, Flash Sales)",
            "Luxury / fashion e-commerce fluency (Miravia, Inditex/Massimo Dutti)",
            "Catalogue / collections / asset structuring on Shopify (DAM-adjacent)",
            "Cross-functional stakeholder management + people/team coordination",
            "Operational KPIs, performance reporting, process/bottleneck analysis",
            "Bachelor's in Business Administration; fluent English; already based in Dubai",
        ],
        "missing_skills": [
            "7+ years asked; Paula has 4+ (real seniority gap)",
            "Formal creative-operations / creative-production DEPARTMENT tenure (her ops experience is brand/content/e-commerce, not running a creative dept) — positioned truthfully as adjacent",
            "Hands-on Adobe Creative Suite / design craft to 'credibly guide designers' (she uses Canva + generative-AI tools, not deep Adobe) — not claimed",
            "End-to-end DAM platform ownership/administration (catalogue/asset structuring on Shopify is adjacent, not DAM admin) — not claimed",
        ],
        "sector_fit": "strong (luxury/fashion e-commerce — direct environment match)",
        "seniority_fit": "stretch (4+ yrs vs 7+ asked; ops-leadership title above current band)",
        "red_flags": [
            "Role is a specialised creative-operations function with a design/production + Adobe + DAM expectation; Paula's edge is the AI/automation + workflow/process side. Genuine gaps on design craft, DAM ownership and tenure — all disclosed openly in the cover letter, nothing fabricated.",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Medium fit (LinkedIn itself flags 'idoneidad media'), pursued because the JD's gravitational centre "
            "— leading the AI & automation agenda plus workflow/process/SOP design, resourcing and project "
            "management for a creative team — is Paula's sharpest and rarest edge. She BUILT and owns an "
            "AI-powered marketing-automation system (Claude/generative AI) that turned planning, content, "
            "research and reporting into repeatable workflows (~40% manual-workload cut across 50+ markets), "
            "designs briefing/approval flows, runs 6 NPD launches end-to-end, plans resourcing across peaks "
            "(25–50 creators/campaign) and comes from luxury/fashion e-commerce (Miravia, Inditex/Massimo "
            "Dutti) with Shopify catalogue/asset structuring that is DAM-adjacent. Real gaps — 7+ vs 4+ years, "
            "no formal creative-production-department tenure, no deep Adobe design craft, no DAM-platform "
            "ownership — are acknowledged openly in the cover letter and never papered over; the CV leans on "
            "the 'operating system around creative' (AI, workflow, SOPs, resourcing, PM, KPIs) rather than "
            "claiming she is a designer. No 'no sponsorship needed' claim (employer-sponsored visa)."
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
