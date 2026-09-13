"""One-off: generate Paula's CV for **Global Performance Marketing & Retail Media**
at **Beiersdorf** (NIVEA, Eucerin, La Prairie, Hansaplast, Labello). Recruiter: Akash
Sharma. Apply via the Beiersdorf Career Site until 11 Sep 2026. Location not stated in
the pasted JD — a *global capability* role is most likely Hamburg HQ (flagged).

JD ask: build and scale Beiersdorf's GLOBAL Performance Marketing capability across
Retail Media (marketplaces, pure players, omnichannel retailers), Social Commerce
(TikTok Shop) and emerging channels — frameworks, operating models, measurement
standards (KPIs, benchmarks, attribution, incrementality), playbooks / tools / learning
programmes adopted by regions and markets, test-and-learn, JBP linkage with Commercial
and eCommerce, partnerships with retailers / platforms / agencies, and applying AI to
campaign quality, diagnostics and efficiency. Profile: performance marketing / retail
media / eCommerce in FMCG, beauty, retail, marketplace, agency or platform; experience
building multi-market frameworks and driving adoption across global/regional/local.

Paula's honest angle:
- BOTH SIDES OF RETAIL MEDIA: two years INSIDE a marketplace (Miravia / Alibaba) running
  onsite visibility, Flash Sales and promotions for 42 beauty/fragrance/fashion brands
  (+30% GMV QoQ, reporting to the CEO) — then the BRAND side at DoFreeze, activating
  three FMCG brands on UAE marketplaces / quick-commerce retailers (Noon, Talabat,
  Careem, Deliveroo) plus Meta and Google Ads, tied to sell-out and ROAS.
- FRAMEWORKS & ENABLEMENT: built an AI-powered marketing operating system (Claude /
  generative AI) standardising campaign planning, KPI reporting, research and decks
  (~40% less manual work) and channel-level trade/shopper plans used across 50+
  distributor markets — the closest real analogue to "playbooks adopted by markets".
- SOCIAL COMMERCE FOUNDATIONS: creator programme from zero to 25–50 creators per
  campaign, UGC pipeline, sampling/seeding, paid amplification, measured on sell-out.
- MEASUREMENT: ROI/ROAS/conversion/retention reporting to pace investment against P&L;
  promo effectiveness and sell-in/sell-out analysis at Mondelez.
- AI: the JD explicitly asks for AI applied to campaign quality and efficiency — her
  signature edge.
- FMCG + BEAUTY: Mondelez (FMCG), Miravia (beauty & fragrances KAM), DoFreeze (FMCG).
- People: leads a team of two (designer + social media exec) — keep in Manager CVs.

Honesty guardrails (do NOT overstate):
- NO TikTok Shop and NO TikTok Ads campaign management — TikTok appears as a content /
  creator channel only. Social commerce is framed as creator-led + paid amplification.
- NO Amazon Ads / Criteo / Walmart Connect / retailer media networks. Retail media is
  the UAE marketplace + quick-commerce set she actually works on ("sponsored placements
  & promotional mechanics") — Paula should confirm she has run PAID placements on
  Noon/Talabat before submitting; otherwise soften to "promotional activation".
- Attribution / incrementality: working knowledge, not MMM or geo-lift tests run.
- Never held a global / regional HQ role at a multinational; her multi-market work is a
  UAE group's distributor markets. CV says "50+ distributor markets", not "global lead".
- No Arabic. Factual "UAE Residence Visa" only — never "no sponsorship needed".
- Title in the pasted JD is not explicit; using "Global Performance Marketing & Retail
  Media Manager" as the working title (rename if the career site shows another).

ONE-PAGE standard: tight summary, 3/2/1/1 bullets, ~6-9 short skills per row.
Fills the real CV template, relabels the skills rows for this role, converts to PDF via
LibreOffice, registers the job, verifies 1 page, lands under output/2026-09-04/.
Also drops a short-named 'Paula De Francisco - CV.pdf' copy for portals.
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

COMPANY = "Beiersdorf"
TITLE = "Global Performance Marketing & Retail Media Manager"
DATE_FOLDER = "2026-09-04"

JOB_DESCRIPTION = """\
Global Performance Marketing & Retail Media — Beiersdorf (NIVEA, Eucerin, La Prairie,
Hansaplast, Labello). Recruiter: Akash Sharma. Apply online via the Beiersdorf Career
Site until 11 September 2026. Location not stated (global role — likely Hamburg HQ).

Job Purpose: Drive the development and scaling of Beiersdorf's global Performance
Marketing capabilities across Retail Media, marketplaces, omnichannel retailers and
Social Commerce. Build scalable frameworks, operating models, measurement standards and
capability programmes that help regions and markets improve media effectiveness,
investment quality and business performance. Combines strategic capability building
with practical market acceleration.

Performance Marketing & Retail Media Excellence: shape global Performance Marketing and
Retail Media frameworks, standards and best practices across marketplaces, pure players
and omnichannel retailers. Improve media effectiveness, investment quality and
performance transparency, connecting media activity with sales and wider eCommerce
outcomes. Partner with Commercial and eCommerce teams to link Retail Media priorities
with customer planning and joint business planning. Identify recurring performance gaps
and develop practical solutions regions and markets can adopt and scale.

Social Commerce & Emerging Growth Channels: build the Performance Marketing and
paid-media capability required to accelerate Social Commerce growth. Define activation
principles, audience approaches, campaign standards and measurement for platforms such
as TikTok Shop. Lead selected test-and-learn initiatives, convert market learning into
scalable guidance, recommend where to test, scale or deprioritise. Partner with
eCommerce, Commercial, Marketing, Content and regional teams.

Measurement, Intelligence & Innovation: define global KPIs, benchmarks and reporting
standards connecting media performance with business outcomes. Advance practical
approaches to attribution, incrementality and investment effectiveness. Work with Data,
Analytics and Technology teams on performance visibility, automation and decision
support. Apply AI and technology solutions to improve campaign quality, diagnostics,
optimisation and operational efficiency.

Capability Building & Market Enablement: develop playbooks, tools and learning
programmes that make global standards practical and easy to adopt. Work through
regional teams to build market capability and share proven practices across countries.
Provide expert guidance on complex topics without replacing local execution ownership.
Build partnerships with retailers, platforms, agencies and technology providers;
influence stakeholders across a global matrix.

Profile: relevant experience in Performance Marketing, Retail Media, digital media,
eCommerce or commerce growth, ideally in FMCG, beauty, consumer goods, retail,
marketplace, agency or platform environments. Strong understanding of Retail Media
across marketplaces, pure players and omnichannel retailers (sponsored search, display,
off-site media, retailer audiences, performance measurement). Understanding of Social
Commerce and paid media within platforms such as TikTok Shop. Experience building
multi-market frameworks, tools, playbooks or capability programmes and driving adoption
across global, regional and local teams.
"""

ATS = [
    "performance marketing", "retail media", "marketplaces", "pure players",
    "omnichannel retailers", "sponsored search", "sponsored products", "display",
    "off-site media", "retailer audiences", "social commerce", "TikTok Shop",
    "paid media", "paid social", "paid search", "Meta Ads", "Google Ads",
    "media effectiveness", "investment quality", "performance transparency",
    "eCommerce", "e-commerce", "commerce growth", "joint business planning", "JBP",
    "customer planning", "frameworks", "operating model", "standards", "best practices",
    "playbooks", "tools", "capability building", "learning programmes", "enablement",
    "multi-market", "global", "regional", "local", "adoption", "test-and-learn",
    "activation principles", "audience strategy", "campaign standards", "KPIs",
    "benchmarks", "reporting standards", "attribution", "incrementality",
    "measurement", "ROAS", "ROI", "conversion", "AOV", "GMV", "sell-out",
    "sell-in/sell-out", "promotional effectiveness", "AI", "generative AI",
    "automation", "diagnostics", "optimisation", "creators", "UGC", "influencer",
    "FMCG", "beauty", "consumer goods", "retailers", "platforms", "agencies",
    "stakeholder management", "global matrix", "Noon", "Talabat", "Careem",
    "Deliveroo", "Alibaba", "Miravia", "Shopify", "Power BI", "Looker",
]

CONTENT = {
    "headline": (
        "Performance Marketing & Retail Media · Social Commerce · "
        "Measurement, Playbooks & AI"
    ),
    "professional_summary": (
        "Performance and retail-media marketer with 5 years across FMCG, beauty and marketplace "
        "e-commerce: two years inside Alibaba's Miravia marketplace running onsite visibility and promotions "
        "for 42 beauty brands, now leading paid media and retail-media activation for an FMCG group in 50+ "
        "markets, with the AI tooling and KPI standards that let markets execute to one playbook."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG group (Befit, Eurocake, Flair) | 50+ markets | Noon, Talabat, Careem, Deliveroo + Shopify D2C",
            "bullets": [
                "Plan and optimise retail-media and promotional activation for three brands on UAE marketplaces and quick-commerce retailers (Noon, Talabat, Careem, Deliveroo) — sponsored placements, promo mechanics, listings — plus Meta and Google Ads, tying spend to sell-out, ROAS and e-commerce outcomes",
                "Built an AI-powered marketing operating system (Claude / generative AI) standardising campaign planning, KPI reporting, research and pitch decks — cutting manual work ~40% and giving distributor markets in 50+ countries a single playbook",
                "Built the creator programme from zero to 25–50 creators per campaign — briefing, UGC pipeline, sampling and seeding, paid amplification — measured on awareness, UGC and sell-out; lead a team of two (design + social)",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's lifestyle marketplace (pure player) | Top-5 global e-commerce | 100K+ employees",
            "bullets": [
                "Marketplace-side view of retail media: managed 42 beauty, fragrance and fashion accounts, planning onsite visibility, promotions, pricing and assortment with brands as joint business plans — +30% GMV QoQ",
                "Owned the Flash Sales channel for Beauty, Fashion & Home reporting directly to the CEO — pacing investment against P&L targets on traffic, conversion, ROI, ROAS and retention",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped build Glovo's Retail vertical — onboarding fashion, beauty and lifestyle brands to the marketplace — and grew XL accounts (KFC, Taco Bell, Sushi Shop) through in-app promo mechanics and data-led activation plans",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | Category planning & analytics",
            "bullets": [
                "Measured promotional effectiveness and sell-in/sell-out for the chocolate category — the retailer-outcome lens for judging what media and trade investment actually returns",
            ],
        },
    ],
    "skills_brand": (  # label -> "Retail Media & Performance"
        "retail media on marketplaces & quick-commerce (sponsored placements, promo mechanics, listings), "
        "paid social & search (Meta, Google Ads), budget allocation, creative testing, ROAS / ROI, JBP"
    ),
    "skills_ecommerce": (  # label -> "Channels & Platforms"
        "Noon, Talabat, Careem, Deliveroo, Miravia (Alibaba), Shopify D2C, Meta Ads, Google Ads, "
        "TikTok & Instagram content, EDM / CRM"
    ),
    "skills_commercial": (  # label -> "Social Commerce & Creators"
        "creator programmes (25–50 per campaign), UGC pipelines, sampling & seeding, paid amplification, "
        "test-and-learn, influencer briefing & negotiation"
    ),
    "skills_data": (  # label -> "Measurement & Enablement"
        "KPI frameworks & benchmarks, ROAS, ROI, conversion, AOV, GMV, sell-in / sell-out, promo effectiveness, "
        "attribution & incrementality (working knowledge), playbooks & reporting standards"
    ),
    "skills_tools": (  # label -> "Tools"
        "Generative AI (Claude, ChatGPT), Meta Ads Manager, Google Ads, Google Analytics, Shopify, "
        "Power BI, Looker, Tableau, Nielsen, Canva, Adobe"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Retail Media & Performance",
    "E-Commerce & Digital": "Channels & Platforms",
    "Commercial": "Social Commerce & Creators",
    "Data & Analytics": "Measurement & Enablement",
}


def make_job() -> Job:
    return Job(
        id="beiersdorf-global-performance-marketing-retail-media-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Not stated (global role — likely Hamburg HQ; confirm on career site)",
        url="https://www.beiersdorf.com/careers",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "Beiersdorf Global Performance Marketing Retail Media Social Commerce",
            "recruiter": "Akash Sharma",
            "deadline": "2026-09-11",
            "note": "Global HQ-level capability role: frameworks, measurement standards, playbooks and "
                    "market enablement across Retail Media, marketplaces, omnichannel retailers and "
                    "Social Commerce (TikTok Shop). Stretch on seniority and scope (never a global / "
                    "regional HQ role), real gaps on TikTok Shop / TikTok Ads and retailer media "
                    "networks (Amazon Ads, Criteo). Strong bridges: marketplace-side (Miravia) + "
                    "brand-side (DoFreeze) retail media, AI-built frameworks/reporting, creator-led "
                    "social commerce, FMCG + beauty background. Location not in JD — likely Hamburg; "
                    "Paula is not open to relocation, so confirm before investing in outreach.",
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
        "salary_raw": None, "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 62, "ai_tier": "Warm",
        "skills_match": [
            "Retail media from both sides: 2 years inside Alibaba's Miravia marketplace (onsite visibility, Flash Sales, promotions for 42 beauty brands, +30% GMV QoQ) and brand-side activation on Noon/Talabat/Careem/Deliveroo at DoFreeze",
            "Built an AI-powered marketing operating system standardising campaign planning, KPI reporting and research across 50+ distributor markets — the closest real analogue to 'frameworks, playbooks and tools adopted by markets'",
            "JD explicitly asks for AI applied to campaign quality, diagnostics and efficiency — Paula's signature edge",
            "Creator-led social commerce foundations: programme from zero to 25–50 creators per campaign, UGC pipeline, seeding, paid amplification measured on sell-out",
            "Measurement discipline: ROI/ROAS/conversion/retention reporting to the CEO against P&L; promo effectiveness and sell-in/sell-out at Mondelez",
            "FMCG + beauty background (Mondelez, Miravia beauty & fragrances, DoFreeze FMCG) matches the 'ideally FMCG / beauty' ask",
            "Hands-on paid media on Meta and Google Ads (structure, budgets, creative testing, daily ROAS optimisation)",
        ],
        "missing_skills": [
            "No TikTok Shop and no TikTok Ads campaign management — Social Commerce is a named pillar of the role",
            "No retailer media networks (Amazon Ads, Criteo, Walmart Connect, Carrefour/Instacart) — retail media experience is UAE marketplace + quick-commerce promotional/sponsored activation",
            "Attribution / incrementality at working-knowledge level — has not run MMM, geo-lift or incrementality tests",
            "Never held a global or regional HQ role at a multinational; multi-market experience is a UAE group's distributor markets, not a regional/local matrix",
            "Seniority: a global capability lead typically carries 7–10+ years; Paula has 5 at Manager level",
        ],
        "sector_fit": "strong — FMCG / beauty with marketplace and quick-commerce retail media is exactly her ground",
        "seniority_fit": "stretch — global HQ capability-building role vs. her market-level Manager profile",
        "red_flags": [
            "Location not stated: a global Beiersdorf role is most likely Hamburg HQ — Paula is not open to relocation",
            "TikTok Shop / Social Commerce paid capability is a named pillar and is absent from her CV",
            "Scope is capability-building across a global matrix, a level above her current remit",
            "Deadline 11 Sep 2026 via Beiersdorf Career Site (recruiter: Akash Sharma)",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Honest stretch with a genuinely good story. Paula has done retail media from the marketplace "
            "side (Miravia / Alibaba: onsite visibility, Flash Sales and promotions for 42 beauty brands) and "
            "the brand side (DoFreeze: three FMCG brands on Noon, Talabat, Careem and Deliveroo plus Meta and "
            "Google Ads tied to sell-out and ROAS), and she has built the kind of thing this role exists to "
            "build — a standardised, AI-powered planning and reporting system that distributor markets execute "
            "against. The JD's explicit AI ask is her strongest hook. Three gaps are real: no TikTok Shop / "
            "TikTok Ads, no retailer media networks such as Amazon Ads or Criteo, and no global or regional "
            "HQ role — this is a capability lead across a global matrix, likely a level above her. The "
            "practical blocker is location: the pasted JD does not state it and a global role is most "
            "likely Hamburg, which Paula has ruled out. Worth applying only if the career site shows Dubai "
            "or a remote/regional option; otherwise treat as a networking application with Akash Sharma."
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
