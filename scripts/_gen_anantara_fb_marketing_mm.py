"""One-off: generate Paula's CV for the Anantara (Minor Hotels)
"F&B Marketing Manager" role at Anantara The Palm Dubai Resort.

Honest re-angle. This is a hospitality Food & Beverage marketing role centred on
exactly the muscles Paula uses every day: integrated marketing strategy to grow
brand awareness and revenue; owning and growing social media across Instagram,
Facebook, TikTok and LinkedIn (planning, scheduling, publishing, optimising);
content calendars and engaging digital content; an influencer / blogger / media
partner programme; paid advertising, email marketing and content marketing;
campaign / social / traffic analytics and reporting; brand-guideline consistency;
market research and competitor analysis; partnership development; and
cross-functional collaboration to promote launches, seasonal campaigns and
special events.

Paula genuinely has the marketing engine — she owns brand social, built and
scaled a 25–50-creator influencer programme from zero, runs seasonal campaigns,
product launches and promotions across 50+ markets, plans/optimises Meta &
Google paid media plus EDM, and reports on campaign/social/traffic KPIs. A
real, useful F&B tie-in: at Glovo she managed marquee restaurant accounts (KFC,
Taco Bell, La Tagliatella, Sushi Shop) with bespoke marketing activations.

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful — NO invented hospitality/hotel tenure, NO invented restaurant-outlet
ownership, NO overclaimed SEO or in-house photography/videography craft (she
directs/produces content with creators & agencies, she is not a
photographer/videographer). Genuine gaps (hospitality/hotel sector tenure,
classic PR/press-office and SEO depth, Arabic) are simply not over-claimed and
are logged honestly in the dashboard.

Fills the real CV template, converts to PDF, registers the job for the dashboard,
and lands the package under output/2026-08-16/.
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

COMPANY = "Anantara Hotels & Resorts"
TITLE = "F&B Marketing Manager"
DATE_FOLDER = "2026-08-16"

JOB_DESCRIPTION = """\
F&B Marketing Manager — Anantara The Palm Dubai Resort (Minor Hotels), Dubai, UAE.

Anantara Hotels & Resorts is a global luxury hotel and resort brand rooted in
Thai culture, part of Minor International, one of the largest hospitality and
leisure companies in Asia Pacific.

Key Responsibilities:
Develop and execute integrated marketing strategies to increase brand awareness,
drive revenue, and promote Food & Beverage outlets, special events, seasonal
campaigns, and promotions.
Create engaging digital content, including photography, videography, graphics,
email campaigns, and promotional materials, ensuring consistency with brand
guidelines.
Manage and grow the company's social media presence across platforms such as
Instagram, Facebook, TikTok, and LinkedIn by planning, scheduling, publishing,
and optimizing content.
Develop and maintain content calendars aligned with marketing objectives,
seasonal initiatives, and business priorities.
Monitor social media channels, engage with guests, respond to comments,
messages, and online reviews, and build a strong online community.
Analyse campaign performance, website traffic, social media insights, and
customer engagement, providing regular reports and recommendations for
continuous improvement.
Plan, execute, and optimise digital marketing campaigns, including paid
advertising, email marketing, SEO, and content marketing initiatives.
Build and maintain relationships with influencers, bloggers, media partners, and
external stakeholders to enhance brand visibility, generate high-quality content,
and increase online reach.
Develop strategic partnerships with local businesses, tourism organisations, and
commercial partners to support marketing and promotional activities.
Conduct market research and competitor analysis to identify industry trends,
customer preferences, and new marketing opportunities.
Ensure all marketing communications and promotional materials reflect the
company's brand identity, tone of voice, and visual standards.
Collaborate closely with Food & Beverage, Operations, Sales, and Revenue teams
to deliver integrated marketing campaigns that support commercial objectives.
Coordinate the promotion of restaurant launches, menu updates, signature
experiences, and special events across all marketing channels.
Support public relations initiatives by liaising with media, journalists,
influencers, and content creators to secure positive brand exposure.
Manage multiple projects simultaneously while ensuring timely delivery, budget
compliance, and high-quality execution.
Stay informed of emerging digital marketing trends, technologies, and best
practices to continuously enhance marketing performance and guest engagement.
"""

ATS = [
    "F&B Marketing Manager", "Food & Beverage marketing", "integrated marketing strategy",
    "brand awareness", "revenue", "seasonal campaigns", "promotions", "special events",
    "restaurant launches", "menu updates", "signature experiences",
    "social media", "Instagram", "Facebook", "TikTok", "LinkedIn",
    "social media management", "content calendar", "content creation", "digital content",
    "photography", "videography", "graphics", "email campaigns", "promotional materials",
    "community management", "online reviews", "engagement",
    "campaign performance", "social media insights", "website traffic", "reporting",
    "digital marketing campaigns", "paid advertising", "paid media", "email marketing",
    "content marketing", "SEO", "influencers", "bloggers", "media partners", "UGC",
    "strategic partnerships", "tourism", "market research", "competitor analysis",
    "brand guidelines", "tone of voice", "visual standards", "public relations", "PR",
    "budget compliance", "project management", "Meta Ads", "Google Ads", "EDM",
    "ROI", "ROAS", "go-to-market", "Dubai", "UAE", "luxury", "lifestyle",
]

CONTENT = {
    "headline": "Brand & Marketing Manager · Social Media, Content & Influencer Marketing · Integrated Campaigns · Paid Media, EDM & Analytics",
    "professional_summary": (
        "Brand and marketing manager with 4+ years building integrated, social-first campaigns that grow brand "
        "awareness and drive revenue — scoped closely to this role: developing and executing marketing strategies "
        "across seasonal campaigns, launches, promotions and events, and owning brand social media across Instagram, "
        "Facebook, TikTok and LinkedIn. Currently lead Brand & Marketing for DoFreeze in Dubai, running content "
        "calendars and engaging content, planning/optimising Meta and Google paid media plus email/EDM, and reporting "
        "on campaign, social and traffic KPIs. Built and scaled an influencer / creator programme from zero to 25–50 "
        "creators per campaign — sourcing, briefing, negotiating and managing creators, bloggers and media partners to "
        "generate high-quality content, UGC and reach. Genuine Food & Beverage exposure from Glovo, managing marquee "
        "restaurant accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop) with bespoke marketing activations. "
        "Data-driven and brand-guideline-disciplined, an early adopter of generative AI for content and campaign "
        "planning, and already based in Dubai on a residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Develop and execute integrated marketing strategies to grow brand awareness and drive revenue — seasonal campaigns, product launches, promotions and events — coordinating go-to-market across 50+ markets on budget and on time",
                "Own and grow brand social media across Instagram, Facebook, TikTok and LinkedIn — planning, scheduling, publishing and optimising content, maintaining content calendars aligned to seasonal initiatives, and managing community engagement and responses",
                "Built and scaled the influencer / creator programme from zero — sourcing, briefing, negotiating and managing 25–50 creators, bloggers and media partners per campaign, plus product sampling and seeding — generating high-quality content, UGC and measurable reach",
                "Direct engaging digital content (photography, video, graphics, email campaigns and promotional materials) with creators and agencies, ensuring every asset reflects brand guidelines, tone of voice and visual standards",
                "Plan, execute and optimise digital campaigns — paid advertising on Meta (Facebook & Instagram) and Google Ads, plus email marketing/EDM and content — analysing performance, social insights, traffic and ROI/ROAS and reporting recommendations for continuous improvement",
                "Run market research and competitor analysis, develop partnerships, and collaborate cross-functionally with commercial, trade and operations teams to deliver integrated campaigns that support commercial objectives",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Grew brand visibility and engagement across a content- and discovery-led lifestyle category (beauty, fragrances, fashion), managing 42 accounts and driving +30% GMV QoQ through campaigns, promotions and social activation",
                "Created and led the Beauty Club and Hot on Social programmes — social-first content and creator activations that built community, loyalty and repeat engagement",
                "Led category expansion as PIC Fragrances, onboarding 30+ houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) in two months via trend-driven, seasonal campaigns",
                "Analysed campaign performance, conversion, traffic, retention, ROI and ROAS to steer content and promotional decisions and report results to leadership",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed marquee Food & Beverage / restaurant accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop), building bespoke marketing activations, promotions and seasonal campaigns that grew order volume",
                "Coordinated the promotion of new launches and menu/offer updates across marketing channels, driving visibility and demand for partner outlets",
                "Led cross-functional squads across marketing, logistics and customer support to ship campaigns end-to-end, and negotiated high-impact commercial deals for platform and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran category and promotional-effectiveness analysis (sell-in/sell-out, Nielsen) and built management-ready performance reports and recommendations",
                "Contributed to NPD launches (Milka Spread, Mini Suchard) from concept to shelf, supporting go-to-market and activation",
            ],
        },
    ],
    "skills_brand": "integrated marketing strategy, social media marketing, content creation & content calendars, influencer & creator marketing, media & blogger partnerships, UGC, seasonal campaigns / promotions / events, brand & product launches, brand guidelines / tone of voice / visual identity, go-to-market, A&P budget management",
    "skills_ecommerce": "social media management (Instagram, Facebook, TikTok, LinkedIn), community management, paid advertising (Meta Ads, Google Ads), email marketing / EDM, content marketing, marketing automation, Shopify / web content, UX optimisation",
    "skills_commercial": "partnership development, stakeholder & partner management, key account management, negotiation, project management, budget & timeline compliance, cross-functional collaboration",
    "skills_data": "campaign performance analysis, social media insights, website traffic analytics, KPI tracking & reporting, market research & competitor analysis, consumer insight, ROI, ROAS, GMV, AI-assisted analysis, Power BI, Tableau",
    "skills_tools": "Meta Business Suite, Meta Ads Manager, Google Ads, Canva, Generative AI (Claude, ChatGPT), email/EDM tools, Power BI, Tableau, Salesforce, Microsoft Office (Expert)",
}


def make_job() -> Job:
    return Job(
        id="anantara-fb-marketing-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://careers.minor.com/",
        source="careers",
        description=JOB_DESCRIPTION,
        raw={"query": "F&B Marketing Manager Anantara", "brand": "Anantara The Palm Dubai Resort",
             "division": "Minor Hotels — Anantara Hotels & Resorts", "req_id": "JR109589"},
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
        "ai_score": 77,
        "ai_tier": "Warm",
        "skills_match": [
            "Integrated marketing strategy (campaigns, launches, promotions, events)",
            "Social media ownership & growth (Instagram, Facebook, TikTok, LinkedIn)",
            "Content calendars & digital content direction (brand-guideline consistent)",
            "Influencer / creator / blogger & media-partner programme (zero → 25–50 per campaign)",
            "Paid advertising (Meta, Google), email/EDM & content marketing with ROI/ROAS",
            "Campaign / social / traffic analytics & reporting",
            "Genuine F&B tie-in: managed KFC, Taco Bell, La Tagliatella, Sushi Shop at Glovo",
            "Market research, competitor analysis & partnership development",
            "Already in Dubai (residence visa, no sponsorship)",
        ],
        "missing_skills": [
            "Hospitality / hotel / F&B-outlet sector tenure (background is FMCG, Beauty & marketplace, not hotels)",
            "Classic PR / press-office & media-relations depth (has influencer & media-partner work, not a dedicated PR role)",
            "SEO depth (strong on paid + content/social; SEO is not a core strength)",
            "In-house photography / videography craft (directs & produces content with creators/agencies)",
            "Arabic (Paula is Spanish native / English C1)",
        ],
        "sector_fit": "moderate (luxury lifestyle brand-building & social/influencer marketing is a strong match; hospitality/F&B sector tenure is the gap)",
        "seniority_fit": "strong (4+ yrs brand/marketing management; Manager scope fits)",
        "red_flags": [
            "Hospitality/hotel F&B sector experience is the main gap — role sits in a luxury resort's F&B outlets",
            "JD lists SEO and photography/videography; Paula's strengths are paid/social/content direction, not SEO or hands-on production",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong marketing-skill fit with an honest sector gap. The Anantara F&B Marketing Manager role is a "
            "social-first, integrated brand-marketing job — grow brand awareness and revenue via seasonal campaigns, "
            "launches, promotions and events; own and grow Instagram/Facebook/TikTok/LinkedIn with content calendars "
            "and engaging content; run an influencer / blogger / media-partner programme; execute paid advertising, "
            "email and content marketing; and report on campaign/social/traffic analytics — nearly all of which Paula "
            "does today at DoFreeze (brand social, 25–50-creator influencer programme built from zero, seasonal "
            "campaigns and launches across 50+ markets, Meta/Google paid media + EDM, KPI reporting) and did at "
            "Miravia (content-led beauty/lifestyle category, Beauty Club & Hot on Social, +30% GMV QoQ). A real F&B "
            "tie-in: at Glovo she managed marquee restaurant accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop) "
            "with bespoke marketing activations. Genuine gaps, positioned truthfully and not over-claimed: "
            "hospitality/hotel sector tenure, classic PR/press-office depth, SEO, hands-on photo/video production, and "
            "Arabic."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
    """Convert DOCX -> PDF headlessly via LibreOffice (no Word automation prompts).

    Falls back to cv._to_pdf (docx2pdf/Word) if soffice is unavailable or fails.
    Removes the intermediate DOCX on success, mirroring cv._to_pdf.
    """
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

    cv_docx = cv._fill_template(CONTENT, job)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
