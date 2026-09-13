"""One-off: generate Paula's CV + cover letter for Rayfitout Contracting LLC
"Growth Marketing Manager" (Dubai) — a hands-on digital-marketing & client-
acquisition role for an interior fit-out / construction contractor.

Why this is a strong, honest fit:
  - The spine of the role is exactly Paula's day-to-day craft: set up and manage
    Google Ads and Meta Ads campaigns; own Instagram strategy end-to-end (content
    planning, Reels/carousels, posting, growth, engagement); develop original
    campaign/content ideas independently; guide content, design, videography and
    UI teams; improve landing pages and website UX for conversion (CRO); and
    report on marketing performance. At DoFreeze she does all of this today.
  - The lead-acquisition side — contacting new leads, qualifying them, arranging
    meetings, and keeping CRM follow-ups — maps honestly to her Key Account /
    Account Manager years at Alibaba's Miravia (42 accounts, +30% GMV QoQ,
    onboarded 30+ stores) and Glovo (prospecting, qualifying, closing deals): she
    handles clients directly, negotiates and sets meetings.
  - Analytical + creative + hands-on, working independently — the profile the JD
    explicitly asks for — plus generative-AI automation for content and reporting.

Honest positioning (NO fabrication):
  - Sector: her background is FMCG / Beauty / Fashion / E-Commerce, NOT interior
    design / construction / real estate (those are "preferred", not required).
    Her premium/luxury adjacency comes from beauty, fragrances and fashion
    (Miravia, Massimo Dutti) — stated truthfully; no interiors/fit-out experience
    is claimed.
  - The role has a heavy direct outbound lead-handling / calling component. Paula
    is comfortable qualifying leads, negotiating and arranging meetings from KAM /
    AM work, but she has not been a pure outbound SDR — framed as transferable
    client-handling, not overclaimed.
  - "Excellent English" — she is C1 professional (stated as such), not native.
  - Already based in Dubai (genuine advantage; JD wants someone willing to
    relocate). NO "no sponsorship needed" claim — the visa is employer-sponsored
    (standing rule); the CV header only states "UAE Residence Visa".

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-25/.
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

COMPANY = "Rayfitout Contracting LLC"
TITLE = "Growth Marketing Manager"
DATE_FOLDER = "2026-08-25"

# No hiring manager named in the posting — letter stays addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Growth Marketing Manager — Rayfitout Contracting LLC, Dubai (in person).

Rayfitout is looking for a creative, analytical, and hands-on Digital Marketing &
Client Acquisition Manager who can think beyond standard marketing methods and
develop original ideas that generate qualified leads and strengthen the brand.

Responsibilities:
- Set up and manage Google Ads and Meta Ads campaigns.
- Analyse campaign performance, lead quality, cost per lead, and conversions.
- Manage Instagram strategy, content planning, posting, growth, and engagement.
- Develop original campaign, Reel, carousel, and content ideas.
- Identify new and unconventional ways to attract high-value clients.
- Guide the content, design, videography, and UI teams.
- Improve website pages and landing pages from a marketing and conversion perspective.
- Contact new leads, understand their requirements, qualify them, and arrange meetings.
- Maintain lead follow-ups and CRM records.
- Prepare clear marketing performance reports.

Requirements:
- Proven experience with Google Ads, Meta Ads, and Instagram management.
- Strong creative thinking and the ability to develop ideas independently.
- Ability to think outside the box, test new approaches, and solve problems proactively.
- Strong understanding of lead generation, content strategy, branding, and analytics.
- Confident communication and client-handling skills.
- Excellent English.
- Experience in interior design, construction, real estate, or luxury services is preferred.
- Willing to relocate to Dubai.

Package: competitive tax-free salary, housing allowance, annual flight allowance,
health insurance. Work location: in person, Dubai.
"""

ATS = [
    "Growth Marketing Manager", "digital marketing", "client acquisition",
    "Google Ads", "Meta Ads", "Meta Ads Manager", "Meta Business Suite",
    "Facebook Ads", "Instagram Ads", "Instagram management", "Instagram strategy",
    "content strategy", "content planning", "Reels", "carousel", "content ideas",
    "campaign performance", "lead quality", "cost per lead", "CPL", "conversions",
    "conversion rate", "lead generation", "qualified leads", "high-value clients",
    "CRM", "lead follow-up", "arrange meetings", "client-handling",
    "website pages", "landing pages", "conversion", "CRO", "branding",
    "creative thinking", "outside the box", "content team", "design", "videography",
    "UI", "marketing performance reports", "ROI", "ROAS", "analytics",
    "A/B testing", "audience targeting", "budgets", "reporting", "Dubai", "UAE",
    "English", "interior design", "construction", "real estate", "luxury services",
]

CV_CONTENT = {
    "headline": (
        "Growth & Digital Marketing Manager · Paid Media (Google & Meta Ads) · "
        "Instagram & Content · Lead Generation & CRO"
    ),
    "professional_summary": (
        "Creative, analytical and hands-on growth & digital marketing manager with 4+ years across "
        "E-Commerce, FMCG, Beauty and Fashion who turns paid media, social and content into qualified leads "
        "and revenue. At DoFreeze I set up and optimise Google Ads and Meta Ads (Facebook & Instagram), own "
        "Instagram strategy end-to-end — content planning, Reels and carousels, posting, growth and engagement "
        "— develop original campaign ideas independently, and guide content, design and creator teams, while "
        "improving landing pages and store UX for conversion (CRO) and reporting on performance, lead quality "
        "and cost per lead. Earlier, as a Key Account / Account Manager at Alibaba's Miravia and Glovo, I "
        "handled clients directly — qualifying, negotiating, arranging meetings and following up in the CRM — "
        "growing GMV +30% QoQ across 42 accounts and onboarding 30+ new stores in two months. Early adopter of "
        "generative AI (Claude/GPT) to scale content, campaign planning and analytics. Excellent English (C1), "
        "already based in Dubai."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "FMCG e-commerce & distribution | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Set up, manage and optimise Google Ads and Meta Ads (Facebook & Instagram) campaigns — audience building, creative A/B testing, budget and bid management — analysing campaign performance, lead/traffic quality, cost per result and conversions to continuously improve ROI and ROAS",
                "Own Instagram strategy end-to-end — content planning, posting cadence, growth and engagement — developing original Reel, carousel and campaign ideas, and scaling an influencer/UGC programme from zero (25–50 creators per campaign) to attract attention and demand from high-value audiences",
                "Guide content, design and videography workflows — briefing and directing creators and designers, setting the creative direction, and turning original ideas into on-brand assets that perform across paid and organic channels",
                "Improve landing pages and website/store UX from a conversion perspective — own the Shopify store end-to-end (catalogue, UX, checkout) and build campaign landing pages, lifting conversion rate (CRO) and average order value through data-led testing",
                "Prepare clear marketing performance reports (spend, cost per lead, conversions, ROI/ROAS) and built AI-powered automation (Claude/GPT) that scales campaign planning, content and reporting — cutting manual workload ~40%",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Handled 42 key accounts directly — qualifying opportunities, negotiating, arranging meetings and following up through the CRM/pipeline — achieving +30% GMV growth QoQ through pricing, assortment and targeted promotions",
                "Led category expansion as PIC Fragrances, identifying and pursuing high-value prospects and onboarding 30+ new stores in two months with tailored commercial proposals",
                "Continuously analysed ROI, ROAS, conversion, traffic and retention to optimise performance and prioritise the highest-value opportunities, and created the Beauty Club and Hot on Social projects to lift brand visibility and engagement",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Grew strategic accounts and closed high-impact commercial deals — prospecting, qualifying, negotiating and arranging meetings to grow order volume and profitability for both partners and Glovo",
                "Supported building Glovo's Retail vertical — onboarding new brand partners with tailored launch campaigns, promotions and data-led joint planning",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out and promotional-effectiveness analysis for the chocolate category, building performance reports in advanced Excel that informed spend and commercial planning",
                "Supported NPD launches (Milka Spread, Mini Suchard) with data-driven analysis, turning category data into actionable recommendations",
            ],
        },
    ],
    "skills_brand": (
        "growth & digital marketing, paid media (Google & Meta Ads), Instagram strategy & management, content "
        "planning (Reels, carousels), influencer & UGC, creative direction & team leadership, original campaign "
        "ideation, lead generation, branding, go-to-market"
    ),
    "skills_ecommerce": (
        "Google Ads, Meta Ads Manager, Meta Business Suite, Facebook & Instagram Ads, Instagram management, "
        "content planning & scheduling, landing-page & website CRO, Shopify, A/B testing, UX optimisation, "
        "marketing automation, EDM, TikTok"
    ),
    "skills_commercial": (
        "lead generation & qualification, client acquisition, arranging meetings, CRM & pipeline management, "
        "lead follow-ups, negotiation, client-handling, key account management, prospecting, pricing & "
        "promotion strategy"
    ),
    "skills_data": (
        "campaign performance analysis, cost per lead (CPL), lead-quality & conversion analysis, ROI, ROAS, "
        "CTR / CPC / CPM, KPI tracking & reporting, forecasting, Looker, Tableau, Power BI"
    ),
    "skills_tools": (
        "Google Ads, Meta Ads Manager, Meta Business Suite, Instagram, Shopify, Generative AI (Claude, "
        "ChatGPT), Canva, CRM, Looker, Tableau, Power BI, Microsoft Office — Expert (Excel, PowerPoint, Word)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Rayfitout's brief — a marketer who can think beyond standard methods and invent original ways to "
        "generate qualified leads and strengthen the brand — is exactly the kind of hands-on, creative-plus-"
        "analytical role I look for, so the Growth Marketing Manager position caught my eye. Running Google and "
        "Meta Ads, owning Instagram end-to-end, developing original content ideas and turning all of it into "
        "high-value client leads is genuinely my day-to-day, and I'm already based in Dubai and ready to work "
        "on-site."
    ),
    "body_paragraph_1": (
        "As Brand & Marketing Manager at DoFreeze I set up and optimise Google Ads and Meta Ads (Facebook & "
        "Instagram) — audiences, creative A/B tests, budgets and bids — and track campaign performance, lead "
        "quality, cost per lead and conversions to keep improving ROI and ROAS. I own Instagram strategy end-to-"
        "end (content planning, Reels and carousels, posting, growth and engagement), develop original campaign "
        "ideas independently, and guide content, design and videography teams to turn those ideas into on-brand "
        "assets. I also improve landing pages and store UX for conversion (CRO) and prepare clear performance "
        "reports — so the full loop from ad click to qualified lead is what I run every day."
    ),
    "body_paragraph_2": (
        "The client-acquisition side fits just as naturally: as a Key Account / Account Manager at Alibaba's "
        "Miravia and at Glovo I handled clients directly — qualifying opportunities, negotiating, arranging "
        "meetings and following up in the CRM — growing GMV +30% QoQ across 42 accounts and onboarding 30+ new "
        "stores in two months. I'll be straightforward that my background is FMCG, beauty, fashion and "
        "e-commerce rather than interior design or construction, but the premium/luxury client work at Miravia "
        "and Massimo Dutti, plus my performance-marketing and content craft, transfer directly — and I bring "
        "generative-AI automation (Claude/GPT) that scales content, campaign planning and reporting, which is "
        "genuinely useful for testing unconventional lead-generation ideas fast."
    ),
    "closing_paragraph": (
        "I'd love to show how I'd approach Rayfitout's first 90 days of lead generation — from Google/Meta "
        "campaign structures and Instagram content through landing-page conversion to a clean lead-qualification "
        "and follow-up flow. I have excellent English (C1), I'm already based in Dubai and available to start "
        "quickly, and I'd welcome the chance to share a few original ideas for attracting high-value clients. "
        "Thank you for considering my application."
    ),
}


def make_job() -> Job:
    return Job(
        id="rayfitout-growth-marketing-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://ae.indeed.com/jobs?q=Rayfitout+Growth+Marketing+Manager&l=Dubai",
        source="indeed",
        description=JOB_DESCRIPTION,
        raw={"query": "Rayfitout Growth Marketing Manager Dubai",
             "function": "Growth / Digital Marketing & Client Acquisition",
             "workplace": "On-site, Dubai",
             "note": "Fit-out / interior-design contractor; hands-on performance + Instagram + lead-gen role; no hiring manager named in posting"},
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
        "salary_raw": "Competitive tax-free + housing + flights + health insurance (no figure disclosed)",
        "salary_aed_min": None,
        "salary_aed_max": None,
        "posted_date": DATE_FOLDER,
        "raw": job.raw,
        "ai_score": 72,
        "ai_tier": "Warm",
        "skills_match": [
            "Hands-on Google Ads + Meta Ads (Facebook & Instagram) — setup, optimisation, A/B testing, budgets/bids",
            "Instagram strategy end-to-end: content planning, Reels/carousels, posting, growth, engagement",
            "Develops original campaign/content ideas independently — creative + analytical, works proactively",
            "Guides content, design, videography teams — briefs and directs creators/designers",
            "Improves landing pages & website/store UX for conversion (CRO); owns Shopify end-to-end",
            "Campaign performance analysis: lead quality, cost per lead, conversions, ROI, ROAS + clear reporting",
            "Client acquisition / lead handling: qualifying, negotiating, arranging meetings, CRM follow-ups (KAM/AM)",
            "+30% GMV QoQ across 42 accounts; onboarded 30+ new stores in two months (Alibaba's Miravia)",
            "Generative-AI automation (Claude/GPT) for content, campaign planning and reporting",
            "Excellent English (C1); already based in Dubai, available to work on-site immediately",
        ],
        "missing_skills": [
            "Interior design / construction / real estate sector experience (preferred, not required) — her sectors are FMCG/Beauty/Fashion/E-Commerce; premium/luxury adjacency via beauty/fragrances/fashion, positioned honestly",
            "Pure outbound SDR / cold-calling of inbound leads — she qualifies, negotiates and sets meetings from KAM/AM work but has not been a dedicated outbound caller (framed as transferable, not overclaimed)",
            "'Excellent English' is required — she is C1 professional (stated as such), not native",
        ],
        "sector_fit": "adjacent (performance/digital marketing craft is a direct match; interiors/fit-out sector is new — her premium adjacency is beauty/fragrances/fashion)",
        "seniority_fit": "on-band — Manager-level role matches Paula's current Brand & Marketing Manager seniority (lateral, not a step down)",
        "red_flags": [
            "Interior design / construction / real estate / luxury-services experience is 'preferred' and Paula has none in fit-out/interiors — soft gap, framed truthfully",
            "Heavy direct lead-calling / client-acquisition component (contact leads, qualify, arrange meetings, CRM) leans more sales-development than strategic marketing — she covers the client-handling honestly via KAM/AM but is not a pure SDR",
            "Small fit-out contractor (3 open roles, few reviews) vs her large-brand FMCG/e-commerce background — different company scale",
            "In-person, on-site role in Dubai — fine (she's already based in Dubai), but not hybrid/remote",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong, honest fit on the core craft. The role is a hands-on digital-marketing & client-"
            "acquisition manager: set up and manage Google Ads and Meta Ads, own Instagram strategy and content "
            "(Reels/carousels, growth, engagement), invent original lead-generation ideas independently, guide "
            "content/design/videography teams, improve landing pages for conversion (CRO), and report on "
            "campaign performance, lead quality and cost per lead — all of which Paula does today at DoFreeze. "
            "The lead-handling side (contact, qualify, arrange meetings, CRM follow-up) maps honestly to her "
            "Key Account / Account Manager years at Alibaba's Miravia (42 accounts, +30% GMV QoQ, 30+ stores "
            "onboarded) and Glovo (prospecting, qualifying, closing). Honest gaps: no interior-design / "
            "construction / real-estate sector experience (preferred, not required — premium adjacency via "
            "beauty/fragrances/fashion); she is not a pure outbound SDR; and 'excellent English' is met at C1 "
            "professional, not native. Seniority is on-band (Manager). CV + letter lead with the genuine "
            "Google/Meta/Instagram/content/CRO craft and the KAM client-handling, and state the sector and "
            "outbound-calling nuances plainly; no interiors experience or native-English claims. No 'no "
            "sponsorship needed' claim — the visa is employer-sponsored."
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
