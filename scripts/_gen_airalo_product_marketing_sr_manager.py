"""One-off: generate Paula's CV + cover letter for Airalo
"Product Marketing - Senior Manager" — fully remote (Spain / UK / UAE, Deel EOR),
reporting to the Chief Growth Officer.

IMPORTANT — this is a STRETCH / reach application, and the package is built to be
honest about that:
  - The role asks for 8+ years of PRODUCT MARKETING including senior leadership,
    and it "shapes the PMM function" reporting to the CGO. Paula's continuous
    marketing/commercial track is ~5 years and she is a Brand & Marketing Manager,
    NOT a titled Product Marketing lead. That gap is real and is flagged plainly
    (missing_skills, red_flags, and one candid line in the letter). Summary says
    "5+ years" — never 8.

Why it is still worth a strong, honest shot:
  - The SUBSTANCE of PMM is genuinely her day-to-day, and she has the single
    hardest-to-fake requirement: end-to-end GLOBAL, MULTI-COUNTRY product
    go-to-market. At DoFreeze she owns GTM for a multi-brand portfolio across 50+
    countries (GCC, MENA, Asia, Europe, USA, Africa) and has led 6 NPD launches
    end-to-end (brief → positioning → pricing → channel plan). The JD lists
    "multi-country product coverage across multiple regions" and "global
    experience" as key — she has it.
  - MARKETPLACE-NATIVE across both B2C and B2B/partner audiences (Alibaba's
    Miravia — 42 beauty/fragrance/fashion accounts, +30% GMV QoQ; Glovo Retail
    vertical launch). The JD wants high-growth tech/consumer/MARKETPLACE and
    "B2C + B2B/B2C, primary B2C" — direct.
  - Positioning & messaging, customer/market research & competitive analysis
    (voice of customer), lifecycle/adoption (activation, engagement, upsell,
    retention), cross-functional launch coordination (Product, Growth, CRM,
    Partnerships, Support), executive presentation (reported to the CEO at
    Miravia), and data-fluency all map onto real work.

Honest positioning (NO fabrication):
  - No fabricated PMM title, no invented battlecards/formal sales-enablement
    programmes. She builds pitch decks / positioning guides / enablement materials
    (real) — that is what is claimed, not a titled PMM enablement function.
  - No travel/telecom sector claim (not held); marketplace / e-commerce /
    consumer-digital cover the listed "plus".
  - Remote role via Deel EOR — visa not a factor and not surfaced. Per standing
    rule, NO "no sponsorship needed" claim; "already based in the UAE" stated only
    as the factual match to the UAE remote option.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-29/.
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

COMPANY = "Airalo"
TITLE = "Product Marketing - Senior Manager"
DATE_FOLDER = "2026-08-29"

# No hiring manager named on the posting (reports into the CGO) — letter stays
# addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Product Marketing - Senior Manager — Airalo. Location: Remote, anywhere in Spain,
the UK or the UAE. Contract: full-time, permanent (UK local; Spain & UAE via Deel
EOR). Working language: English. Airalo is the world's first eSIM store, used by
millions of travelers across 200+ countries; a fully remote team of 400+ across
60+ countries. Reports into the Chief Growth Officer.

As Senior Manager of Product Marketing you will own how Airalo positions, launches
and grows its product portfolio globally. You are the connective tissue between
Product, Growth, CRM, Partnerships and Customer Support — ensuring every team has
the messaging, information and enablement they need to sell and support the
products. You will shape the PMM function, set strategic direction for how Airalo
brings its connectivity to market, and drive adoption, engagement and monetization
across the lifecycle.

Product Positioning & Messaging: own the product narrative; define clear,
differentiated positioning for each product and customer segment (B2C travelers,
B2B partners, enterprise); develop and maintain a messaging framework that scales
across channels, markets and languages; ensure consistency between product value
and how it is communicated externally.

Go-To-Market Strategy & Customer Insights: lead GTM planning for new products,
features and market expansions — strategy through execution; partner with Growth,
CRM and Partnerships to design integrated launch plans with clear goals, channels
and success metrics; develop partner-specific GTM motions; build a deep
understanding of customers, segments and buying behaviors; commission and
synthesize market research, competitive analysis and customer feedback; serve as
the internal voice of the customer across Product, Marketing and Leadership.

Product Adoption & Lifecycle Marketing: drive strategies to increase activation,
engagement, upsell and retention across the lifecycle; work with CRM, Growth and
Product to design lifecycle campaigns grounded in product value and behavioral
data; identify and close gaps between product capability and customer
awareness/usage.

Product Launch, Planning Support & Enablement: partner with Product Management on
roadmap planning so marketing is integrated early; define launch tiers and
coordinate cross-functional readiness; own launch retrospectives and improve the
launch playbook; equip Growth, CRM, Partnerships and Support with positioning
guides, competitive battlecards, objection-handling materials and product updates;
build training programs and onboarding materials for GTM roles.

What You'll Bring: 8+ years of product marketing experience, including senior
leadership in a high-growth tech, consumer or marketplace company; proven track
record owning end-to-end GTM strategy for complex or global products; strong
ability to distill complex products into clear, compelling messaging for diverse
global audiences; experience working cross-functionally across Product, Growth,
CRM, Sales and Support; data-fluent; excellent written/verbal and executive-level
presentation skills; experience in travel, mobile, fintech or marketplace a plus;
comfortable in a remote-first, globally distributed environment; experience
managing both B2C and B2B/B2C products with a primary focus on B2C; extensive
multi-country product coverage across multiple regions (global experience a plus).

Salary: UK £88,500-£119,500; Spain €65,000-€85,000 (UAE via Deel; tiered by
location).
"""

ATS = [
    "Product Marketing", "PMM", "Senior Manager", "product positioning",
    "positioning & messaging", "messaging framework", "product narrative",
    "value proposition", "go-to-market", "GTM", "GTM strategy", "product launch",
    "launch planning", "launch tiers", "launch playbook", "launch retrospectives",
    "new product", "feature launch", "market expansion", "customer segments",
    "B2C", "B2B", "B2B/B2C", "buying behavior", "customer insights",
    "market research", "competitive analysis", "competitive battlecards",
    "voice of customer", "product adoption", "lifecycle marketing", "activation",
    "engagement", "upsell", "retention", "monetization", "behavioral data",
    "CRM", "Growth", "Partnerships", "Customer Support", "Product Management",
    "roadmap", "cross-functional", "enablement", "sales enablement",
    "positioning guides", "onboarding materials", "training programs",
    "data-fluent", "executive presentation", "multi-country", "global products",
    "multiple regions", "marketplace", "consumer", "e-commerce", "remote",
    "English", "GCC", "MENA", "UAE",
]

CV_CONTENT = {
    "headline": (
        "Product & Brand Marketing · Global Go-To-Market across 50+ Markets · "
        "Positioning, Messaging & Launch · Lifecycle, Adoption & Insights · B2C + B2B Marketplace"
    ),
    "professional_summary": (
        "Product and brand marketing professional with 5+ years across FMCG, Beauty and E-Commerce "
        "marketplaces, currently owning end-to-end go-to-market for a multi-brand portfolio across 50+ countries "
        "(GCC, MENA, Asia, Europe, USA and Africa). I define product positioning and messaging, lead launches "
        "from strategy through execution, and partner cross-functionally with product, growth, CRM and "
        "partnerships to drive adoption, engagement and retention. Marketplace-native across both B2C and "
        "B2B/partner audiences (Alibaba's Miravia, Glovo), data-fluent (activation, conversion, retention, "
        "ROI/ROAS, GMV; +30% GMV QoQ across 42 accounts), and an early adopter of generative AI for messaging, "
        "research and enablement. Fluent English, remote-first, and already based in the UAE."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own end-to-end go-to-market for the brand portfolio across 50+ countries (GCC, MENA, Asia, Europe, USA and Africa), leading 6 NPD launches from strategy through execution — positioning, packaging, pricing and channel plan with clear goals and success metrics",
                "Define product positioning and messaging for each brand, segment and market — building a narrative that scales across channels, markets and languages and keeps product value consistent from pack to campaign",
                "Partner cross-functionally with product/supply, growth, CRM and quick-commerce partners (Noon, Talabat, Careem, Deliveroo) on integrated launch and lifecycle plans — driving activation, engagement, upsell and retention grounded in behavioral and sales data",
                "Commission and synthesize market research, competitive analysis and customer feedback to inform positioning and roadmap, acting as the internal voice of the customer across marketing and leadership",
                "Equip commercial and partner teams with positioning guides, pitch decks and enablement materials, and built AI-powered automation (Claude/GPT) that scales messaging, research and reporting — cutting manual workload ~40%",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Ran marketplace product and category marketing across 42 beauty, fragrance and fashion accounts (B2C shoppers + B2B partners) — owning positioning, assortment and promotion to grow GMV +30% QoQ, ahead of category",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting directly to the CEO — setting go-to-market strategy and presenting performance-driven plans at executive level",
                "Led category expansion as PIC Fragrances, launching 30+ partner brands in two months (incl. the official distributors of Arabian Oud, Lattafa, Swiss Arabian and Ajmal) with partner-specific go-to-market motions",
                "Ran competitive, pricing and customer deep dives, turning research and behavioral data into positioning and lifecycle actions that lifted conversion, retention and engagement",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce marketplace | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped launch Glovo's Retail vertical — taking new categories (fashion, beauty, lifestyle) to market with positioning, launch plans and partner-specific activations",
                "Managed strategic B2B/B2C key accounts and coordinated cross-functional launches across marketing, product, operations and support",
                "Negotiated and closed high-impact partner deals, growing GMV through data-led planning",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Owned sell-in/sell-out and promotional-effectiveness analysis for the chocolate category, turning data into insights and recommendations for launches and business reviews",
                "Supported NPD launches (Milka Spread, Mini Suchard) from concept to shelf with structured go-to-market analysis",
            ],
        },
    ],
    "skills_brand": (
        "product positioning & messaging, go-to-market (GTM) strategy & execution, product launches & NPD "
        "end-to-end, launch planning & readiness, product narrative & value proposition, lifecycle & adoption "
        "marketing, brand strategy, generative-AI messaging & enablement"
    ),
    "skills_ecommerce": (
        "marketplaces (Alibaba/Miravia, Glovo), quick-commerce (Noon, Talabat, Careem, Deliveroo), lifecycle & "
        "CRM campaigns, activation / engagement / retention, Shopify & CRO, EDM, Meta & Google Ads, marketing automation"
    ),
    "skills_commercial": (
        "cross-functional leadership (Product, Growth, CRM, Partnerships, Support), partner / B2B go-to-market, "
        "enablement (positioning guides, decks), stakeholder & project management, negotiation, pricing & "
        "promotion strategy"
    ),
    "skills_data": (
        "customer & market research, competitive analysis, voice of customer, behavioral & performance data, "
        "funnel & KPI analysis (activation, conversion, retention, ROI/ROAS, GMV), dashboards, business reviews, "
        "AI-assisted analysis"
    ),
    "skills_tools": (
        "Generative AI (Claude, ChatGPT), Notion, Looker, Power BI, Tableau, Google Sheets & Excel (Expert), "
        "Salesforce, Meta Ads Manager, Google Ads, Canva, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Airalo turned a genuinely painful travel problem — staying connected abroad — into a product millions "
        "reach for by default, and scaling that across 200+ countries is fundamentally a product-marketing "
        "challenge: sharp positioning, disciplined launches and messaging that travels across markets and "
        "languages. The Senior Manager, Product Marketing role reads like the core of what I do today — I own "
        "end-to-end go-to-market for a multi-brand portfolio across 50+ countries (GCC, MENA, Asia, Europe, USA "
        "and Africa), the kind of multi-country, global-product remit this role is built around."
    ),
    "body_paragraph_1": (
        "At DoFreeze I define positioning and messaging for each brand, segment and market and lead launches "
        "from strategy through execution — six NPD launches end-to-end (positioning, packaging, pricing, channel "
        "plan) with clear goals and success metrics — partnering cross-functionally with product, growth, CRM "
        "and platform partners to drive activation, engagement and retention. I'm also marketplace-native: at "
        "Alibaba's Miravia I ran product and category marketing across 42 beauty, fragrance and fashion accounts "
        "(B2C shoppers and B2B partners), grew GMV +30% QoQ, owned the Flash Sales channel and presented "
        "go-to-market plans directly to the CEO; and at Glovo I helped take a whole new retail vertical to "
        "market. Commissioning research and competitive analysis to act as the voice of the customer, and "
        "turning behavioral data into positioning and lifecycle decisions, is how I already work."
    ),
    "body_paragraph_2": (
        "I'll be transparent, in the spirit of your roaming-free recruitment: I'm earlier in my arc than the "
        "eight-year, senior-PMM-leadership bar — I'm a Brand & Marketing Manager, not yet a titled Product "
        "Marketing lead. What I bring is that I already do the substance of the role at global scale, I'm "
        "marketplace- and consumer-native (a listed plus, in place of direct travel/telecom), I'm data-fluent "
        "and an early adopter of generative AI for messaging, research and enablement, and I'm comfortable in a "
        "remote-first, globally distributed team. I'd join hungry to shape the PMM function and grow into its "
        "leadership fast — and I'm already based in the UAE and set up to work fully remotely."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to show how I'd approach Airalo's product narrative and launch playbook — "
        "differentiated positioning by segment, integrated GTM with Growth, CRM and Partnerships, and a "
        "lifecycle that turns product value into adoption and retention. Thank you for considering my "
        "application — I'd be glad to walk through how I'd spend the first 90 days shaping the PMM function."
    ),
}


def make_job() -> Job:
    return Job(
        id="airalo-product-marketing-sr-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Remote (Spain / UK / UAE)",
        url="https://jobs.lever.co/airalo",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Product Marketing Senior Manager Airalo remote",
             "function": "Product Marketing (PMM)", "reports_to": "Chief Growth Officer",
             "workplace": "Remote — Spain / UK / UAE (UK local; Spain & UAE via Deel EOR)",
             "salary_bands": "UK £88,500-£119,500; Spain €65,000-€85,000 (UAE via Deel)",
             "note": "Airalo (world's first eSIM store). 8+ yrs PMM incl. senior leadership required — stretch application."},
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
        "salary_raw": "UK £88,500-£119,500; Spain €65,000-€85,000 (UAE via Deel)",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 64,
        "ai_tier": "Warm",
        "skills_match": [
            "End-to-end GLOBAL, multi-country product GTM across 50+ markets (DoFreeze) — direct to 'multi-country product coverage / global products'",
            "6 NPD launches end-to-end (positioning → pricing → channel plan)",
            "Product positioning & messaging across brands, segments, markets & languages",
            "Marketplace-native (Alibaba/Miravia, Glovo) — matches 'marketplace company' + a listed plus",
            "B2C + B2B/partner audiences (primary B2C) — matches the B2C+B2B requirement",
            "Lifecycle/adoption: activation, engagement, upsell, retention (CRM/EDM, Shopify CRO, Miravia retention)",
            "Cross-functional with Product, Growth, CRM, Partnerships, Support",
            "Customer/market research, competitive analysis, voice of customer",
            "Executive presentation (reported to CEO at Miravia)",
            "Data-fluent; generative-AI for messaging/research/enablement",
            "Remote-first; fluent English; already in the UAE (remote option)",
        ],
        "missing_skills": [
            "8+ years PMM incl. SENIOR LEADERSHIP — Paula is ~5 years and a Brand & Marketing Manager, not a titled PMM lead (the core gap)",
            "Titled Product Marketing / PMM function ownership — adjacent via brand + GTM, not a PMM title",
            "Formal sales-enablement artefacts (competitive battlecards, objection-handling, structured training/L&D programmes) — builds decks/positioning guides, but not a titled enablement function",
            "Travel / telecom / mobile-app / fintech sector — not held; marketplace / e-commerce / consumer-digital cover the adjacent 'plus'",
        ],
        "sector_fit": "strong (marketplace / consumer-digital; B2C+B2B) — but role seniority sits above current level",
        "seniority_fit": "STRETCH — Senior Manager / 8+ yrs incl. senior leadership vs ~5 yrs at Manager level",
        "red_flags": [
            "8+ years incl. senior leadership is a hard 'What You'll Bring' — Paula is ~5 yrs; the single biggest gap across her recent applications",
            "Role shapes/leads the PMM function reporting to the CGO — a step up in scope and altitude from an IC/Manager remit",
            "No titled Product Marketing experience — strong adjacency (brand + global GTM) but not a PMM track",
            "Fully remote via Deel EOR (UAE) — employment setup differs from a local UAE-sponsored package",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "STRETCH / reach application — built honestly. This is a Senior Product Marketing Manager role that "
            "shapes the PMM function reporting to the Chief Growth Officer and asks for 8+ years of product "
            "marketing including senior leadership; Paula's continuous marketing/commercial track is ~5 years "
            "and she is a Brand & Marketing Manager, not a titled PMM lead — the core, honestly-flagged gap. "
            "The case for shooting anyway is that the SUBSTANCE maps well and she holds the hardest-to-fake "
            "requirement: end-to-end GLOBAL, multi-country product go-to-market across 50+ countries (GCC, MENA, "
            "Asia, Europe, USA, Africa) with 6 NPD launches end-to-end, and she is marketplace-native across "
            "B2C and B2B/partner audiences (Alibaba's Miravia +30% GMV QoQ; Glovo Retail vertical launch) — the "
            "JD prizes marketplace/consumer companies, multi-country/global product coverage, and B2C+B2B. "
            "Positioning & messaging, market research / competitive analysis / voice-of-customer, "
            "lifecycle/adoption (activation, engagement, upsell, retention), cross-functional launch "
            "coordination, executive presentation (CEO at Miravia) and data-fluency are all real. Gaps not "
            "fabricated: the 8-yr senior-leadership bar and PMM title (letter names this outright), formal "
            "sales-enablement artefacts (battlecards/L&D), and travel/telecom sector (marketplace/consumer "
            "covers the 'plus'). Scored Warm to reflect the seniority gap despite strong substance fit. No "
            "'no sponsorship needed' claim (remote via Deel EOR)."
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
