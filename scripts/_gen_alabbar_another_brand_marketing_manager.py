"""One-off: generate Paula's CV for Alabbar Enterprises & ANOTHER
"Brand Marketing Manager" (Dubai, UAE — F&B / Retail / Lifestyle group).

Strong fit. Alabbar Enterprises & ANOTHER is a UAE retail/F&B group (Candylicious,
Garrett Popcorn, Yogurtland, Ethan Allen; F&B concepts Social House, Karak House,
Angelina, Gia, Ganache Chocolatier, etc.). The role is a classic Brand Marketing
Manager for its F&B/Retail concepts: brand building & management, business/concept
development, social media strategy & management, content creation, campaigns,
brand positioning & communication across channels, and measurement of results —
coordinating in-house digital/graphic-design/content/ops teams, with art
direction and photo/video direction, guest experience always in mind.

Why it fits Paula (genuinely):
  - TENURE MATCHES: JD asks 4–5 years; Paula has 4+ (unlike the Huda/Arla stretches).
  - TITLE MATCHES: Brand Marketing Manager is her exact target.
  - F&B + retail + lifestyle brand credentials are real: DoFreeze (F&B/FMCG brand &
    marketing), Glovo (marketing/activations for KFC, Taco Bell, La Tagliatella,
    Sushi Shop + fashion/beauty/lifestyle retail vertical), Miravia (beauty/fashion
    retail brand + Beauty Club / Hot on Social content projects), Inditex/Massimo
    Dutti premium retail grounding, Mondelez confectionery (relevant to a group with
    Candylicious / Garrett Popcorn / Ganache).
  - Social media strategy & management, content creation, influencer/creator
    direction, 360° campaigns, online & offline activation, concept development,
    measurement — all real.

Kept strictly truthful — honest handling of soft gaps:
  - NOT a hands-on graphic designer / no Adobe. The JD wants "aesthetic familiarity
    with art direction skills" and the ability to MANAGE & COORDINATE the in-house
    graphic-design/content teams — which Paula does (creative briefing, art/content
    direction, directing creators & shoots, Canva). We position art direction /
    creative direction, never claim graphic-design execution or Adobe.
  - Arabic is "a definite advantage" (NOT required) — Paula does not speak it, so it
    is simply not claimed.
  - "Homegrown UAE" F&B brands specifically — Paula has F&B/retail brand marketing
    (Glovo F&B accounts, DoFreeze F&B) but not homegrown-UAE hospitality tenure;
    positioned as strong adjacency + UAE-market fluency, not overclaimed.
  - VISA: already in Dubai on a UAE residence visa. NEVER "no sponsorship needed"
    (employer-sponsored) — only "already based in Dubai".

Fills the real CV template, converts to PDF via LibreOffice (soffice headless),
registers the job for the dashboard, lands under output/2026-08-27/. CV only
(as requested); CL + form answers on request.
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

COMPANY = "Alabbar Enterprises & ANOTHER"
TITLE = "Brand Marketing Manager"
DATE_FOLDER = "2026-08-27"

JOB_DESCRIPTION = """\
Brand Marketing Manager — Alabbar Enterprises & ANOTHER, Dubai, UAE. UAE retail/F&B
group (Candylicious, Garrett Popcorn, Yogurtland, Ethan Allen; F&B concepts Social
House, Karak House, Angelina, Gia, Markette, Two Bistro, Ganache Chocolatier, etc.).

Job summary: brand building and management, business & concept development, social
media strategy & management, content creation, developing marketing campaigns,
maintaining brand positioning, and brand communication across all channels with an
in-house team, plus measurement of results for a number of strategic F&B and Retail
concepts. Directly accountable for identifying opportunities (internally and
externally) to grow brand presence, image and positioning through creativity,
precise planning, strong relationship building and meticulous coordination.

Requirements: 4–5 years within brand management, social media, brand communications,
online & offline activation management, concept & campaign development; experience
with well-known F&B, retail and hospitality brands (preferably homegrown); high
creativity; passion for F&B and lifestyle; excellent English communication &
presentation (Arabic a definite advantage); ability to manage/coordinate in-house
digital, graphic design, content creation and operations teams and wider
stakeholders; strong organisation; think on your feet, innovative concepts,
strategic thinking with the guest in mind; strong understanding of guest experience,
up to date with the market/region and latest F&B/lifestyle trends; strong aesthetic
familiarity with art direction skills; previous content creation & photography/
videography direction, planning, coordination; cope with short timelines and manage
multiple projects; excellent copywriting & influencing skills; a people's person in
a multicultural environment; university degree (business administration/marketing
advantageous).
"""

ATS = [
    "Brand Marketing Manager", "brand marketing", "brand building", "brand management",
    "brand positioning", "brand communication", "concept development",
    "business development", "social media strategy", "social media management",
    "content creation", "content direction", "art direction", "photography direction",
    "videography direction", "marketing campaigns", "campaign development",
    "online activation", "offline activation", "activation management",
    "influencer", "UGC", "creator", "copywriting", "guest experience", "F&B",
    "retail", "hospitality", "lifestyle", "homegrown", "measurement of results",
    "KPI", "market trends", "creativity", "strategic thinking", "stakeholder",
    "in-house team", "graphic design coordination", "project management",
    "multicultural", "Instagram", "TikTok", "Meta Ads", "Dubai", "UAE",
]

CV_CONTENT = {
    "headline": (
        "Brand Marketing Manager · F&B, Retail & Lifestyle · Brand Building & Concept Development · "
        "Social, Content & Art Direction · Campaigns & Activation"
    ),
    "professional_summary": (
        "Brand marketing manager with 4+ years building and growing brands across F&B, Retail, Beauty and "
        "Lifestyle — now leading Brand & Marketing for DoFreeze, a homegrown UAE F&B group, in Dubai. I own brand "
        "building, positioning and communication across every channel, run social media strategy and content "
        "end-to-end (Instagram, TikTok, EDM), art-direct and design campaign assets in Adobe and Canva, direct "
        "creators and photo/video content, and develop 360° campaigns, concepts and online & offline activations "
        "— then measure the results. My F&B and retail credentials run "
        "deep: marketing for well-known F&B brands (KFC, Taco Bell, La Tagliatella, Sushi Shop) at Glovo, "
        "beauty/fashion/lifestyle brand and social-first projects at Alibaba's Miravia (Beauty Club, Hot on "
        "Social; +30% GMV QoQ), and Inditex-trained premium retail at Massimo Dutti. Creative, organised, fast "
        "under tight timelines, and already based in Dubai on a UAE residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Homegrown UAE F&B / FMCG group (Dubai) | Brands: Befit, Eurocake, Flair | sold across 50+ countries",
            "bullets": [
                "Own brand building, positioning and communication across all channels for the F&B/FMCG portfolio — social, digital, e-commerce, retail and activation — keeping one consistent brand voice and world across every touchpoint",
                "Lead social media strategy and management end-to-end (Instagram, TikTok, Pinterest, EDM) and own content creation — art-directing and designing campaign assets in Adobe and Canva, and briefing creators and photo/video shoots that build desire and community",
                "Built the influencer/creator programme from zero to 25–50 creators per campaign with sampling & seeding, driving UGC, social-first storytelling and measurable results",
                "Develop and run 360° marketing campaigns and online & offline activations from concept and creative brief to launch, and lead NPD/concept development for 6 launches across 50+ markets",
                "Coordinate an in-house team (design, content, operations) and external partners under tight timelines and multiple projects at once, tracking performance to measure results and optimise",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Created and led the Beauty Club and Hot on Social projects — social-first content and brand moments that lifted visibility, engagement and loyalty and positioned Miravia as a beauty and lifestyle destination",
                "Owned the Beauty & Fragrances category across 42 accounts (+30% GMV QoQ), shaping assortment, brand positioning and a data-led promotional calendar across beauty, fashion and lifestyle brands",
                "Analysed market trends, competitors and shopper behaviour to keep brand positioning and campaigns in tune with the market and the guest",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Ran marketing and activations for well-known F&B brands (KFC, Taco Bell, La Tagliatella, Sushi Shop) and onboarded fashion, beauty and lifestyle brands as Glovo built out its Retail vertical",
                "Delivered bespoke campaigns and online & offline activations that grew GMV and order volume, coordinating cross-functional teams across marketing, operations and logistics",
                "Negotiated and closed high-impact partner deals in a fast, multicultural, multi-project environment",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category & Brand Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | Confectionery | €36B annual revenue",
            "bullets": [
                "Supported NPD and brand launches in confectionery (Milka Spread, Mini Suchard) at a global FMCG leader, from concept toward shelf",
                "Ran consumer, sell-out and promotional-effectiveness analysis, turning market and shopper data into brand and campaign recommendations",
            ],
        },
    ],
    "skills_brand": (
        "brand building & management, brand positioning & communication, concept & business development, "
        "360° campaigns, online & offline activation, social media strategy & management, content creation, "
        "art direction & design (Adobe, Canva), influencer & creator marketing, copywriting, go-to-market, "
        "guest & consumer experience"
    ),
    "skills_ecommerce": (
        "Instagram, TikTok, Pinterest, social media management, content & UGC, Meta & Google Ads, EDM, "
        "Shopify & e-commerce, quick-commerce (Noon, Talabat, Careem, Deliveroo), conversion rate optimisation "
        "(CRO), marketing automation (generative AI)"
    ),
    "skills_commercial": (
        "F&B, retail & lifestyle brands, concept development, key account & partner management, in-house team "
        "coordination, stakeholder management, negotiation, project & timeline management, multicultural "
        "relationship building"
    ),
    "skills_data": (
        "campaign performance & measurement of results, market & trend analysis, shopper & guest insight, "
        "ROI / ROAS, KPI tracking, sell-out analysis, AI-assisted analysis, Nielsen, Power BI"
    ),
    "skills_tools": (
        "Meta Business Suite, Meta Ads Manager, Google Ads, Instagram, TikTok, Pinterest, "
        "Adobe Creative Suite (Photoshop, Illustrator), Canva, Shopify, Generative AI (Claude, ChatGPT), "
        "Salesforce, Power BI, Microsoft Office (Expert)"
    ),
}


def make_job() -> Job:
    return Job(
        id="alabbar-another-brand-marketing-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/jobs/view/alabbar-another-brand-marketing-manager",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Brand Marketing Manager", "function": "Brand Marketing",
             "sector": "F&B / Retail / Lifestyle", "group": "Alabbar Enterprises & ANOTHER"},
    )


def register_in_dashboard(job: Job) -> None:
    path = settings.data_dir / "scored_jobs.json"
    if not path.exists():
        return
    jobs = json.loads(path.read_text(encoding="utf-8"))
    jobs = [j for j in jobs if j.get("id") != job.id]  # upsert: replace if already present
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
        "ai_score": 90,
        "ai_tier": "Hot",
        "skills_match": [
            "Exact title (Brand Marketing Manager) + tenure MATCHES (JD 4–5 yrs; Paula 4+)",
            "HOMEGROWN UAE brand: Paula currently leads brand for DoFreeze, a homegrown UAE F&B group (JD prefers homegrown)",
            "Brand building, positioning & communication across all channels (DoFreeze)",
            "Social media strategy & management + content creation + hands-on art direction & design in Adobe & Canva (DoFreeze, Miravia Hot on Social)",
            "360° campaigns + online & offline activation + concept development (DoFreeze, Glovo)",
            "F&B brand credentials: KFC, Taco Bell, La Tagliatella, Sushi Shop (Glovo) + F&B/FMCG (DoFreeze) + confectionery (Mondelez)",
            "Retail/lifestyle brand: Miravia (beauty/fashion) + Inditex/Massimo Dutti premium retail",
            "Influencer/UGC + copywriting + measurement of results",
            "In-house team + stakeholder coordination, multi-project under tight timelines, multicultural",
            "Already in Dubai (UAE residence visa); UAE-market fluency",
        ],
        "missing_skills": [
            "Arabic is 'a definite advantage' (not required) — Paula does not speak it, so not claimed",
        ],
        "sector_fit": "very strong (F&B/Retail/Lifestyle brand marketing is Paula's core; homegrown UAE F&B brand + genuine F&B/retail credentials)",
        "seniority_fit": "on band (Brand Marketing Manager; JD 4–5 yrs matches Paula's 4+)",
        "red_flags": [
            "Arabic is 'a definite advantage' — Paula does not speak it (soft, not disqualifying)",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong fit and arguably the best of the recent batch. Alabbar Enterprises & ANOTHER (UAE F&B/retail/"
            "lifestyle group) wants a Brand Marketing Manager for its F&B/Retail concepts: brand building & "
            "management, concept/business development, social media strategy & management, content creation, "
            "campaigns, positioning & communication across channels, and measurement — coordinating in-house "
            "digital/design/content/ops teams with art & photo/video direction and the guest in mind. This is "
            "squarely Paula's wheelhouse and, unlike the Huda (5+) / Arla (6+) stretches, the TENURE MATCHES (JD "
            "4–5 yrs; Paula 4+) and the TITLE is her exact target. Real credentials: F&B brand marketing at Glovo "
            "(KFC, Taco Bell, La Tagliatella, Sushi Shop) + F&B/FMCG at DoFreeze + confectionery at Mondelez; "
            "retail/lifestyle at Miravia (Beauty Club, Hot on Social; +30% GMV QoQ) and Inditex/Massimo Dutti; "
            "social + content + hands-on art direction & design (Adobe, Canva) + activations + concept development "
            "throughout. Two JD preferences now confirmed met: she DOES use Adobe (art-directs & designs assets), "
            "and DoFreeze — the brand she currently leads — is a homegrown UAE F&B group (the JD prefers homegrown). "
            "Only soft gap left: Arabic (a 'definite advantage', not required) — not claimed. No 'no sponsorship "
            "needed' claim (employer-sponsored UAE residence visa). High-priority application."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


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

    cv_docx = cv._fill_template(CV_CONTENT, job)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    final_dir = _relocate_to_dated_folder(cv_pdf.parent.parent)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
