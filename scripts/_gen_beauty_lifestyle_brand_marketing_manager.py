"""One-off: generate Paula's CV (+ cover letter) for a recruiter-posted
"Brand Marketing Manager" role at a fast-growing beauty / lifestyle brand
entering US retail.

Why this is a genuinely strong fit:
  - The role is a broad, hands-on BRAND MARKETING + campaign-delivery +
    marketing-project-management role for a beauty/lifestyle brand: translate
    strategy into launch plans and campaign timelines, own end-to-end product
    launches, build launch calendars/trackers/briefs/approvals, coordinate
    across brand/design/social/retail/e-commerce, run PR mailers/gifting/events,
    align influencer activity, coordinate consumer research, and compile
    post-campaign reporting on a commercially responsible budget. Paula does
    almost all of this today at DoFreeze.
  - Beauty depth is REAL and on-the-nose: at Alibaba's Miravia she was KAM for
    Beauty, Fragrances & Fashion (42 accounts, +30% GMV QoQ), onboarded leading
    Arabian/oud fragrance houses, and BUILT the "Beauty Club" and "Hot on Social"
    programmes that positioned the platform as a beauty & lifestyle destination.
    The JD "strongly prefers" beauty/skincare/cosmetics — she has it.
  - Tenure lands exactly: JD asks "around four or more years"; Paula has 4+.
  - Launch project management, influencer/UGC/gifting-seeding, e-commerce
    partnership (Shopify + customer journey), agency/vendor coordination and
    post-campaign reporting are all things she owns now.

Honest positioning (NO fabrication):
  - US MARKET is the single real gap. Her markets today span GCC, MENA, Europe,
    Asia and Africa with US EXPORT exposure via DoFreeze's 50+ countries — she
    coordinates brand comms to international retail partners, but she is NOT a
    US-native and does not claim years of US-consumer/US-retail fluency. This is
    disclosed plainly in the cover letter, not hidden.
  - Her beauty grounding is on the commercial/e-commerce side (Miravia) plus
    brand/NPD leadership on the FMCG side (DoFreeze); framed as a legitimate
    composite, never as brand-side beauty tenure she doesn't have.
  - Per standing rule, NO "no sponsorship needed" claim — her UAE residence visa
    is employer-sponsored. States "based in Dubai" only.
  - Company is confidential (recruiter posting: "We're partnering with...").
    Filed under a neutral "Beauty & Lifestyle Brand" label; no hiring manager
    named, so the letter stays addressed to "Hiring Manager".

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-21/.
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

COMPANY = "Beauty & Lifestyle Brand"
TITLE = "Brand Marketing Manager"
DATE_FOLDER = "2026-08-21"

# Recruiter posting ("We're partnering with..."), brand confidential, no hiring
# manager named — letter stays addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Brand Marketing Manager — fast-growing beauty / lifestyle brand (confidential,
via recruiter). Hands-on role to lead brand and project delivery through the next
stage of growth. Significant global customer base already established, with a
major launch with US retailers on the horizon. This person becomes the
operational engine of the marketing function, turning strategy into launch plans,
campaigns and commercially effective execution across product launches, retail,
e-commerce, creative, social, PR and events.

The opportunity: not a narrow, single-channel role. Own the planning,
coordination and delivery of day-to-day brand activity end to end, connecting
internal teams and external partners so every project lands on time, on brand and
to a high standard. Broad scope that grows with the brand and team — real
ownership.

What you'll be doing:
- Translate brand strategy into clear launch plans, campaign timelines and
  channel-specific deliverables.
- Own end-to-end coordination of product launches, retail moments, exclusives and
  promotional campaigns.
- Develop brand communications, product storytelling, launch decks and
  external-facing materials.
- Act as the central point of coordination across brand, design, social, retail
  and e-commerce teams.
- Build and manage project plans, launch calendars, trackers, briefs, approvals
  and delivery milestones.
- Coordinate brand communication with US retail partners, ensuring assets,
  messaging and product information land on time.
- Partner with the e-commerce team to strengthen product storytelling, campaign
  visibility and the customer journey.
- Project-manage PR mailers, gifting initiatives, events and wider brand
  activations.
- Coordinate external agencies, vendors and partners, resolving delivery issues
  quickly.
- Ensure social and influencer activity aligns with wider brand objectives,
  without directly owning talent management.
- Coordinate consumer research, review collection and insight-gathering to inform
  future campaigns.
- Compile post-campaign reporting and keep marketing budgets commercially
  responsible.

What we're looking for:
- Around four or more years in brand marketing, integrated marketing, campaign
  delivery or marketing project management.
- Experience within beauty, skincare or cosmetics strongly preferred.
- Strong understanding of the US consumer, beauty and retail landscape.
- Proven track record managing product launches and multi-channel campaigns from
  planning through to delivery.
- Excellent project-management skills, running multiple timelines and
  stakeholders at once.
- Strong commercial and creative judgement, confidence to bring ideas and see
  them through.
- Comfortable in a small, flat, fast-moving team where responsibilities evolve.
- Highly organised, proactive and accountable, with excellent written and verbal
  communication.

Brand marketing role (not performance marketing); direct ownership of influencer
talent not required, though close coordination with the influencer team. Suits an
established Marketing Manager or a high-performing Senior Marketing Executive
ready for a broader, ownership-driven role, joining at a pivotal point as the
brand expands into US retail.
"""

ATS = [
    "Brand Marketing Manager", "brand marketing", "integrated marketing",
    "campaign delivery", "marketing project management", "project management",
    "beauty", "skincare", "cosmetics", "fragrances", "lifestyle brand",
    "product launch", "product launches", "launch plans", "campaign timelines",
    "channel-specific deliverables", "go-to-market", "GTM", "retail moments",
    "exclusives", "promotional campaigns", "brand communications",
    "product storytelling", "launch decks", "external-facing materials",
    "launch calendars", "trackers", "briefs", "approvals", "delivery milestones",
    "central point of coordination", "cross-functional", "stakeholder management",
    "US retail", "US consumer", "retail partners", "e-commerce", "customer journey",
    "campaign visibility", "PR mailers", "gifting", "seeding", "events",
    "brand activations", "agencies", "vendors", "influencer", "UGC", "social",
    "consumer research", "review collection", "insight-gathering",
    "post-campaign reporting", "marketing budgets", "A&P", "multi-channel",
    "omnichannel", "creative", "highly organised", "commercial judgement",
    "Shopify", "CRO", "Meta Ads", "ROI", "ROAS", "GMV", "NPD",
]

CV_CONTENT = {
    "headline": (
        "Brand Marketing Manager · Beauty, Fragrances & Lifestyle · Product Launches & "
        "Multi-Channel Campaign Delivery · End-to-End Launch Project Management · Influencer, PR & E-Commerce"
    ),
    "professional_summary": (
        "Brand marketing and campaign-delivery manager with 4+ years across beauty, fragrances, fashion, FMCG "
        "and e-commerce, now leading Brand & Marketing for a multi-market FMCG house in Dubai. I turn brand "
        "strategy into launch plans, campaign timelines and on-brand execution: I run product launches "
        "end-to-end (brief, storytelling, packaging, pricing, go-to-market), deliver multi-channel campaigns "
        "across retail, e-commerce, social, influencer, PR/gifting and events, and keep every project on time "
        "and on brand through disciplined project management — launch calendars, trackers, briefs and approvals "
        "across 50+ markets. My beauty & fragrances grounding comes from Alibaba's Miravia, where I managed 42 "
        "beauty, fragrance and fashion accounts (+30% GMV QoQ) and built the 'Beauty Club' and 'Hot on Social' "
        "programmes that positioned the platform as a beauty & lifestyle destination. I coordinate agencies, "
        "vendors and cross-functional teams, scale influencer/UGC and gifting/seeding, partner with e-commerce "
        "on the customer journey, and build the AI-powered playbooks, decks and landing pages that let a small, "
        "fast-moving team punch far above its size. Business Administration graduate (CUNEF), based in Dubai."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Multi-market FMCG house | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Translate brand strategy into launch plans, campaign timelines and channel-specific deliverables — owning end-to-end coordination of 6 product launches (brief, product storytelling, packaging, pricing, go-to-market) across retail, e-commerce, social and PR",
                "Act as the central point of coordination across brand, design, social, retail and e-commerce — building and managing project plans, launch calendars, trackers, briefs, approvals and delivery milestones that keep every activation on time and on brand",
                "Own end-to-end multi-channel campaigns across product launches, retail moments, exclusives and promotions in 50+ markets (GCC, MENA, Europe, USA, Africa) — coordinating brand communication to international retail partners so assets, messaging and product information land on time",
                "Build and scale influencer, UGC and gifting/seeding programmes from zero — sourcing, briefing and managing 25–50 creators per campaign plus PR mailers and product seeding across modern trade and quick-commerce — aligning influencer activity to wider brand objectives without owning talent management",
                "Partner with e-commerce to strengthen product storytelling, campaign visibility and the customer journey — running the brand's Shopify store end-to-end (catalogue, UX, collections, checkout) to lift conversion and average order value",
                "Coordinate external agencies, vendors and partners and resolve delivery issues quickly, while developing brand communications, launch decks and external-facing materials",
                "Compile post-campaign reporting and keep A&P budgets commercially responsible — and built an AI-powered automation system (Claude / generative AI) that turns planning, content, decks and reporting into repeatable playbooks, cutting manual workload ~40%",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top-5 global e-commerce marketplace | Beauty, Fragrances & Fashion | 100K+ employees",
            "bullets": [
                "Owned 42 beauty, fragrance and fashion accounts, driving +30% GMV growth QoQ through assortment, pricing and multi-channel promotional campaigns — a deep grounding in the beauty and lifestyle landscape",
                "Created and led the 'Beauty Club' and 'Hot on Social' programmes end-to-end — brand storytelling, content and activations that boosted visibility and loyalty and positioned the platform as a beauty & lifestyle destination",
                "Led category expansion as PIC Fragrances, onboarding 30+ new beauty/fragrance houses in two months — including leading Arabian & oud brands (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) — via trend-driven assortment and promotions",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting to the CEO — planning and delivering deadline-driven promotional campaigns aligned to commercial targets",
                "Analysed conversion, traffic, retention, ROI and ROAS, and tracked category trends and the competitive landscape to inform assortment, storytelling and campaign decisions",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce super-app | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped build Glovo's Retail vertical — taking new fashion, beauty and lifestyle brands to market on the platform and running bespoke launch activations beyond food",
                "Ran complex, cross-functional campaigns from brief to live — coordinating marketing, design, logistics and support across multiple timelines to deliver launches on schedule",
                "Managed strategic key accounts and drove GMV growth through data-led campaign planning and promotional mechanics",
                "Negotiated and closed high-impact commercial deals, maximising profitability for partners and platform",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran consumer, sell-in/sell-out and promotional-effectiveness analysis for the chocolate category, distilling insight to steer brand and category plans",
                "Supported NPD launches (Milka Spread, Mini Suchard) from concept to shelf — early grounding in product launches and go-to-market",
                "Collected and synthesised category and consumer insight (Nielsen / Kantar) to identify growth opportunities",
            ],
        },
    ],
    "skills_brand": (
        "brand marketing, integrated marketing, campaign delivery, product launches / NPD end-to-end, "
        "go-to-market (GTM), brand communications & product storytelling, launch decks & external-facing "
        "materials, multi-channel campaigns, influencer & UGC, PR mailers & gifting/seeding, events & brand "
        "activations, shopper & trade marketing"
    ),
    "skills_ecommerce": (
        "e-commerce partnership & customer journey, Shopify e-store, conversion rate optimisation (CRO), "
        "campaign visibility, social (Instagram, TikTok, Pinterest), paid media (Meta / Google Ads), CRM & EDM, "
        "quick-commerce (Noon, Talabat, Careem, Deliveroo), marketing automation"
    ),
    "skills_commercial": (
        "end-to-end launch project management, launch calendars, trackers, briefs & approvals, "
        "cross-functional & stakeholder coordination, agency & vendor management, retail & modern-trade "
        "partners, key account management, negotiation"
    ),
    "skills_data": (
        "consumer & review research, insight-gathering, post-campaign reporting, A&P / marketing budget "
        "management, KPI tracking, ROI / ROAS / conversion / retention analysis, Nielsen, Kantar, Power BI"
    ),
    "skills_tools": (
        "Generative AI (Claude, ChatGPT), Shopify, Meta Ads Manager, Meta Business Suite, Google Ads, Canva, "
        "Power BI, Salesforce, SAP, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "A beauty and lifestyle brand with a global customer base stepping into US retail — turning strategy "
        "into launches, campaigns and commercially effective execution across product, retail, e-commerce, "
        "social, PR and events — is exactly the operational-engine role I want. I'm a brand marketing and "
        "campaign-delivery manager with 4+ years across beauty, fragrances, fashion, FMCG and e-commerce, now "
        "leading Brand & Marketing for a multi-market FMCG house in Dubai, and I spend my days doing precisely "
        "what this role asks: making broad, fast-moving brand activity land on time, on brand and to a high "
        "standard."
    ),
    "body_paragraph_1": (
        "Your 'what you'll be doing' list maps closely onto my day job. At DoFreeze I translate brand strategy "
        "into launch plans and campaign timelines and own end-to-end coordination of product launches — brief, "
        "product storytelling, packaging, pricing and go-to-market — across retail, e-commerce, social, "
        "influencer and PR, in 50+ markets. I'm the central coordination point across brand, design, social, "
        "retail and e-commerce, running the project plans, launch calendars, trackers, briefs and approvals "
        "that keep everything moving, and I coordinate external agencies and vendors, resolving delivery issues "
        "fast. My beauty grounding is real: at Alibaba's Miravia I managed 42 beauty, fragrance and fashion "
        "accounts (+30% GMV QoQ), onboarded leading fragrance houses, and built the 'Beauty Club' and 'Hot on "
        "Social' programmes that made the platform a beauty & lifestyle destination. I've scaled influencer, "
        "UGC and gifting/seeding from zero (25–50 creators per campaign), partner daily with e-commerce to "
        "strengthen product storytelling and the customer journey, and I compile post-campaign reporting while "
        "keeping A&P budgets commercially responsible."
    ),
    "body_paragraph_2": (
        "Two things make me a strong fit for a small, flat, fast-moving team. First, disciplined execution at "
        "pace: I'm highly organised and accountable, comfortable running multiple launch timelines and "
        "stakeholders at once, and I've built AI-powered playbooks, decks and landing pages (Claude / "
        "generative AI) that let a lean team deliver like a much bigger one. Second, entrepreneurial ownership "
        "— I bring ideas and see them through. I'll be candid on one point: my markets today span GCC, MENA, "
        "Europe and Africa with US export exposure, so while I coordinate brand communication to international "
        "retail partners, I'd be deepening my US-consumer and US-retail fluency rather than arriving with years "
        "of it — something I'm genuinely excited to do as the brand enters that chapter, and I ramp fast."
    ),
    "closing_paragraph": (
        "I'd love to be the operational engine that turns your US-retail moment and everyday brand activity "
        "into launches and campaigns that land — combining hands-on beauty and lifestyle experience, "
        "end-to-end launch project management and AI-powered ways of scaling a lean team. I'm based in Dubai "
        "and available to talk through how I'd approach the first 90 days. Thank you for your consideration — "
        "I look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="beauty-lifestyle-brand-marketing-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="—",
        url="",
        source="recruiter",
        description=JOB_DESCRIPTION,
        raw={"query": "Brand Marketing Manager",
             "function": "Brand Marketing / Campaign Delivery / Marketing PM",
             "sector": "Beauty / Skincare / Cosmetics / Lifestyle",
             "note": "Confidential brand via recruiter ('We're partnering with...'). "
                     "Location not stated in posting; brand expanding into US retail. "
                     "US-market depth is the single honest gap — disclosed in the cover letter, never inflated."},
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
        "ai_score": 85,
        "ai_tier": "Hot",
        "skills_match": [
            "Brand marketing + campaign delivery + marketing project management — Paula's core at DoFreeze TODAY",
            "Beauty/fragrances depth (JD strongly prefers) — Miravia KAM Beauty, Fragrances & Fashion (42 accounts, +30% GMV QoQ), Beauty Club & Hot on Social programmes, oud/fragrance houses onboarded",
            "Product launches end-to-end (6 NPDs: brief, storytelling, packaging, pricing, GTM) + multi-channel campaigns planning->delivery",
            "End-to-end launch project management — project plans, launch calendars, trackers, briefs, approvals, delivery milestones",
            "Central coordination across brand/design/social/retail/e-commerce + agency & vendor management",
            "Influencer/UGC + PR mailers/gifting/seeding scaled from zero (25-50 creators/campaign); aligns influencer activity without owning talent",
            "E-commerce partnership — Shopify store end-to-end, product storytelling, campaign visibility, customer journey, CRO/AOV",
            "Consumer & review research, post-campaign reporting, A&P/marketing budget responsibility",
            "~4+ years (JD asks 'around four or more') — exact tenure match; small, flat, fast-moving team fit",
            "Highly organised, entrepreneurial, AI-powered playbooks/decks that scale a lean team; Business Admin (CUNEF), English C1, based in Dubai",
        ],
        "missing_skills": [
            "US consumer / US retail landscape depth (real gap — markets are GCC/MENA/Europe/Asia/Africa with US EXPORT exposure via DoFreeze's 50+ countries). Disclosed honestly in the cover letter; coordinates brand comms to international retail partners but NOT claimed as US-native fluency",
            "Beauty tenure is commercial/e-commerce side (Miravia) + brand/NPD on FMCG side (DoFreeze) — a legitimate composite, not brand-side beauty tenure she doesn't have",
        ],
        "sector_fit": "strong (beauty/fragrances/lifestyle real via Miravia + brand/NPD via DoFreeze)",
        "seniority_fit": "on-band (established Marketing Manager; 4+ vs 'around four or more' — exact match)",
        "red_flags": [
            "US-market depth is the single honest gap; positioned truthfully via US export exposure + fast ramp, never fabricated. Everything else (brand marketing, campaign delivery, launch PM, beauty, influencer/PR/gifting, e-commerce, reporting/budget) is a direct, strong match.",
            "Job location not stated in the posting (brand confidential, US-retail expansion). CV keeps Paula's Dubai base; no relocation/sponsorship claims made.",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong fit and one of the most on-profile beauty roles to date. The JD is a broad, hands-on BRAND "
            "MARKETING + campaign-delivery + marketing-project-management role for a beauty/lifestyle brand: "
            "translate strategy into launch plans/timelines, own end-to-end product launches and multi-channel "
            "campaigns, build launch calendars/trackers/briefs/approvals, coordinate across "
            "brand/design/social/retail/e-commerce and external agencies/vendors, run PR mailers/gifting/events, "
            "align influencer activity (no talent ownership), coordinate consumer/review research, and compile "
            "post-campaign reporting on a responsible budget. Paula owns nearly all of this today at DoFreeze, "
            "and her beauty grounding is genuine (Miravia KAM Beauty/Fragrances/Fashion, +30% GMV QoQ, Beauty "
            "Club/Hot on Social, fragrance-house onboarding). Tenure matches exactly (4+ vs 'around four or "
            "more'). The one real gap is US-consumer/US-retail depth — her markets are GCC/MENA/Europe/Asia/"
            "Africa with US EXPORT exposure; disclosed openly in the cover letter and bridged honestly, never "
            "fabricated. No 'no sponsorship needed' claim (employer-sponsored visa) — states 'based in Dubai' "
            "only."
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
