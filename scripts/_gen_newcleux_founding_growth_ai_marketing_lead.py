"""One-off: generate Paula's application package for the Newcleux
"Founding Growth & AI Marketing Lead" (Abu Dhabi · Remote) role.

Newcleux is an early-stage venture building an "AI operating system", run by a
founding team split between Abu Dhabi and Chicago. The role spans TWO businesses:
  (1) New Wave Car Wash — website, customer journey, membership, messaging, growth
  (2) Newcleux — how the AI OS is experienced, onboarded, positioned and adopted

The JD is explicit that they do NOT want "a traditional marketer": they want
someone who understands human behaviour, spots friction, builds trust, improves
conversion, and uses AI confidently to research, create, test, analyse and
execute — turning ideas into experiments, prototypes and real customer
experiences, building without a rigid playbook. It ends by asking applicants to
"show us something you've built" and what they learned about people.

This is one of Paula's strongest-fitting roles: her signature differentiator is
being an AI-native marketer who BUILDS (at DoFreeze she built a generative-AI
marketing system, Claude/GPT, -40% manual work), paired with hands-on growth,
Shopify CRO / customer-journey ownership, consumer-behaviour reading (Miravia,
42 accounts +30% GMV QoQ) and building things from zero with no playbook
(influencer programme, Glovo's Retail vertical).

Honest gaps (addressed in the cover letter, NOT papered over):
  - very early-stage founding role; her title is Brand & Marketing Manager, not a
    formal "Growth Lead"
  - UI/UX is hands-on instinct (Shopify, landing pages), not pro product design
  - consumer psychology is applied/instinctive, not formally trained

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful — NO invented experience. Fills the real CV + cover-letter templates,
converts DOCX->PDF via LibreOffice (docx2pdf/Word is unreliable on this Mac),
and lands the package under
output/2026-08-18/Newcleux - Founding Growth & AI Marketing Lead/.
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

COMPANY = "Newcleux"
TITLE = "Founding Growth & AI Marketing Lead"
DATE_FOLDER = "2026-08-18"

SOFFICE = "/Applications/LibreOffice.app/Contents/MacOS/soffice"

JOB_DESCRIPTION = """\
Founding Growth & AI Marketing Lead — Newcleux, Abu Dhabi, UAE (Remote, full-time).

We are looking for someone who is fascinated by why people do what they do and
excited about using AI to turn those insights into growth. This role sits at the
intersection of AI, psychology, marketing, brand, and digital experience. You will
work directly with the founders across two businesses:
- New Wave Car Wash, where you will help rethink the website, customer journey,
  membership experience, messaging, and growth strategy.
- Newcleux, where you will help shape how an entirely new AI operating system is
  experienced, understood, and brought to market, from product journeys and
  onboarding to positioning, messaging, and user adoption.

We are not looking for a traditional marketer. We are looking for someone who can
understand human behavior, spot friction, build trust, improve conversion, and use
AI to move faster across research, content, design, testing, prototyping and analysis.

You may be a great fit if you:
- Are deeply curious about psychology, consumer behavior, and decision making
- Understand growth, conversion, retention, and customer journeys
- Have strong instincts around brand, messaging, UI, UX, and digital experiences
- Use AI confidently to research, create, test, analyze, and execute
- Can turn ideas into experiments, prototypes, and real customer experiences
- Are comfortable with data but never lose sight of the human behind it
- Move quickly, think creatively, and are comfortable building without a rigid playbook
- Want meaningful ownership and direct influence on how both businesses grow

Location and how we work: Our founding team is based between Abu Dhabi and Chicago,
but location is not a barrier. For us, the person matters more than the post code.

When you apply, don't just send us a résumé. Show us something you've built,
redesigned, grown, tested, or changed and tell us what you learned about people
along the way.
"""

ATS = [
    "growth", "growth marketing", "AI", "generative AI", "AI marketing",
    "psychology", "consumer behaviour", "consumer behavior", "decision making",
    "conversion", "conversion rate optimisation", "CRO", "retention",
    "customer journey", "customer journeys", "brand", "messaging", "UI", "UX",
    "digital experience", "experiments", "A/B testing", "prototypes",
    "prototyping", "testing", "research", "content", "analysis", "automation",
    "membership", "onboarding", "positioning", "adoption", "funnel",
    "build trust", "friction", "ownership", "Shopify", "landing pages",
    "Meta Ads", "Google Ads", "e-commerce", "remote", "UAE", "Abu Dhabi",
]

CONTENT = {
    "headline": "Growth & AI Marketing · Consumer Behaviour & Conversion · Brand, Messaging & Digital Experience (UX / CRO) · Builds with Generative AI (Claude / GPT)",
    "professional_summary": (
        "AI-native growth marketer who starts from why people do what they do and turns it into conversion. Not a "
        "traditional marketer: I use generative AI (Claude / GPT) across my whole day — research, content, design, "
        "testing, prototyping and analysis — and I built the AI marketing system behind it at DoFreeze, cutting manual "
        "work ~40% and letting me ship an idea as a live landing page or experiment in hours. I own customer journeys "
        "end-to-end on Shopify (UX, messaging, checkout) to lift conversion and retention, read consumer behaviour to "
        "grow accounts (42 accounts, +30% GMV QoQ at Alibaba's Miravia), and I build things from zero with no playbook. "
        "Comfortable with data but never losing sight of the human behind it. Based in Dubai, set up to work remotely."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Use generative AI (Claude / GPT) end-to-end across my day — research, content, design, A/B testing, prototyping and analysis — having built the AI marketing system that automates campaign planning, market research, content and reporting, cutting manual work ~40% and letting me ship ideas as experiments in hours, not days",
                "Own the brand's Shopify store end-to-end — customer journey, UX, catalogue, collections, checkout and messaging — lifting conversion (CRO) and average order value by tuning it to how people actually shop",
                "Build landing pages, prototypes and pitch decks with AI to turn ideas into real, testable customer experiences fast, then iterate on what the data and customer response show",
                "Built and scaled the influencer programme from zero with no playbook — sourcing, briefing and managing 25–50 creators per campaign plus sampling and seeding — to earn awareness, trust and UGC that convert",
                "Run paid media on Meta Ads (Facebook & Instagram) and Google Ads with continuous creative A/B testing, reading ROI/ROAS and funnel data to improve conversion and retention",
                "Lead NPD end-to-end for 6 launches (brief, positioning, pricing, go-to-market) across 50+ markets — translating what customers actually want into products and messaging that land",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Grew 42 key accounts +30% GMV QoQ by reading consumer behaviour and decision-making — pricing, assortment and promotion choices tuned to how shoppers really buy in beauty, fragrance and fashion",
                "Continuously analysed conversion, traffic, retention and ROI/ROAS to optimise channel performance — data-led, but always with the customer behind the number",
                "Created and led the Beauty Club and Hot on Social projects, building brand visibility, loyalty and trust and positioning Miravia as a beauty and lifestyle destination",
                "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months through trend-driven products and promotions on a top-5 global e-commerce platform",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped build Glovo's Retail vertical from scratch — onboarding fashion and lifestyle brands and expanding a quick-commerce marketplace into new categories without a rigid playbook",
                "Drove GMV growth for strategic accounts through data-led planning and bespoke marketing activations, optimising the customer journey across a web + mobile platform",
                "Led cross-functional teams across marketing, logistics and CX to ship campaigns quickly and lift order volume",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category & Consumer Insights",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran sell-in/sell-out and promotional-effectiveness analysis for the chocolate category — early grounding in why people buy and how insight turns into action",
                "Identified consumer-backed growth opportunities that fed NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": "growth marketing, consumer behaviour & decision-making, brand & messaging, building from zero (no playbook), rapid experimentation & prototyping, generative-AI marketing (Claude / GPT), go-to-market, NPD end-to-end, influencer & UGC",
    "skills_ecommerce": "conversion rate optimisation (CRO), customer journey & UX, Shopify e-store, landing pages & prototypes, retention & lifecycle, A/B testing, Meta Ads (Facebook & Instagram), Google Ads, quick-commerce, EDM/CRM",
    "skills_commercial": "growth & GMV, pricing & assortment, key account management, cross-functional leadership, commercial acumen & P&L, ownership mindset",
    "skills_data": "funnel & conversion analysis, ROI / ROAS / retention, KPI dashboards (Power BI, Tableau, Looker), AI-assisted research & analysis, A/B test read-out, sell-in/sell-out, forecasting",
    "skills_tools": "Generative AI (Claude, ChatGPT), Shopify, Meta Ads Manager, Google Ads, Canva, Power BI, Tableau, Looker, Microsoft Office (Expert)",
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "\"We are not looking for a traditional marketer\" is the line that made me want to write. I'm a marketer who "
        "starts from why people do what they do and uses AI to turn that into growth — which is exactly where this role "
        "sits, at the intersection of AI, psychology, brand and digital experience. Doing that across two very different "
        "businesses — rethinking New Wave Car Wash's journey, membership and messaging, and shaping how Newcleux's AI "
        "operating system is experienced, onboarded and adopted — is precisely the founding, build-it-yourself mandate "
        "I've been moving toward."
    ),
    "body_paragraph_1": (
        "You asked to see something built rather than a résumé, so here's what I've built and what it taught me. At "
        "DoFreeze I use generative AI (Claude / GPT) across my whole day — research, content, design, testing, "
        "prototyping and analysis — and I built the AI marketing system behind it, which cut manual work ~40% and lets "
        "me ship an idea as a live landing page or experiment in hours. I own our Shopify store end-to-end — customer "
        "journey, UX, messaging and checkout — and lift conversion and average order value by tuning it to how people "
        "actually shop. I also built our influencer programme from zero with no playbook, scaling to 25–50 creators a "
        "campaign to earn awareness and trust. Earlier, at Alibaba's Miravia, I grew 42 accounts +30% GMV QoQ by reading "
        "consumer behaviour and decision-making, and created loyalty projects (Beauty Club, Hot on Social) that made "
        "people want to come back."
    ),
    "body_paragraph_2": (
        "What I've learned about people is that data points to friction but rarely explains it — the win is watching "
        "where trust breaks in a journey and removing it, whether that's a checkout, an onboarding flow or a first "
        "message. I'm comfortable with data but never lose sight of the human behind it, I move quickly, and I'm at my "
        "best building without a rigid playbook and owning the outcome. I want to be honest about fit too: my title "
        "today is Brand & Marketing Manager rather than a formal growth lead, and my UI/UX and consumer-psychology work "
        "is hands-on instinct — Shopify, landing pages, watching real behaviour — rather than formal training. Given how "
        "I build and how fast I use AI, that's a head start, not a gap. I'm based in Dubai and fully set up to work "
        "remotely with your Abu Dhabi and Chicago team, and I can start immediately."
    ),
    "closing_paragraph": (
        "I'd love to walk you through the AI system and the pages and experiments I've built — and, if useful, put "
        "together a quick concept for New Wave or Newcleux so you can see how I'd think about your customers. Thank you "
        "for reading; I'd be genuinely excited to help build both businesses."
    ),
}


def make_job() -> Job:
    return Job(
        id="newcleux-founding-growth-ai-marketing-lead-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Abu Dhabi, United Arab Emirates (Remote)",
        url="https://www.linkedin.com/company/newcleux/jobs/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Founding Growth & AI Marketing Lead", "via": "LinkedIn (promoted)"},
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
        "ai_score": 84,
        "ai_tier": "Hot",
        "skills_match": [
            "AI-native marketer who BUILDS (DoFreeze generative-AI marketing system, Claude/GPT, -40% manual work)",
            "Uses AI to research, create, test, analyse & execute — ships prototypes/landing pages in hours",
            "Growth, conversion & retention: Shopify CRO + customer-journey ownership end-to-end",
            "Reads consumer behaviour & decision-making (Miravia: 42 accounts, +30% GMV QoQ)",
            "Brand, messaging & digital experience (UX, landing pages, loyalty projects)",
            "Builds from zero with no playbook (influencer programme; Glovo Retail vertical)",
            "Moves fast, ownership mindset; based in Dubai, remote-ready",
        ],
        "missing_skills": [
            "Very early-stage founding role; her title is Brand & Marketing Manager, not a formal Growth Lead",
            "UI/UX is hands-on instinct (Shopify, landing pages), not pro product design",
            "Consumer psychology is applied/instinctive, not formally trained",
        ],
        "sector_fit": "strong (AI-native growth · brand / digital experience · e-commerce & AI-product startup)",
        "seniority_fit": "on-band (founding generalist; 4+ yrs, ownership scope maps)",
        "red_flags": [
            "Very early-stage founding role across a two-business pair (car wash + AI OS) — undefined structure, likely equity-weighted comp",
            "Salary not disclosed — cannot confirm AED 20k/mo floor",
            "Remote founding role (profile prefers on-site/hybrid), though this role is explicitly location-agnostic and UAE-based",
            "Promoted listing, 88 applicants within 24h",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "One of Paula's strongest-fit roles. Newcleux's 'Founding Growth & AI Marketing Lead' explicitly wants a "
            "non-traditional marketer who understands human behaviour, improves conversion, and uses AI confidently to "
            "research, create, test, analyse and execute — turning ideas into experiments and prototypes while building "
            "without a playbook. That is Paula's signature: at DoFreeze she BUILT a generative-AI marketing system "
            "(Claude/GPT, -40% manual work) and uses AI across research, content, design, testing and prototyping; she "
            "owns Shopify customer-journey/CRO end-to-end; she reads consumer behaviour (Miravia, 42 accounts +30% GMV "
            "QoQ) and builds from zero (influencer programme, Glovo Retail vertical). Genuine caveats — early-stage "
            "founding role, hands-on (not pro) UI/UX, applied (not formal) psychology, undisclosed equity-weighted comp "
            "— are handled honestly in the cover letter. The JD's 'show us something you built' ask plays directly to "
            "her AI-built landing pages and experiments."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _to_pdf_soffice(docx_path: Path) -> Path:
    """Convert DOCX->PDF with LibreOffice headless (docx2pdf/Word is unreliable
    on this Mac). Removes the intermediate DOCX on success."""
    outdir = docx_path.parent
    subprocess.run(
        [SOFFICE, "--headless", "--convert-to", "pdf", "--outdir", str(outdir), str(docx_path)],
        check=True,
        capture_output=True,
    )
    pdf_path = docx_path.with_suffix(".pdf")
    if not pdf_path.exists():
        raise RuntimeError(f"LibreOffice did not produce {pdf_path}")
    docx_path.unlink(missing_ok=True)
    return pdf_path


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

    # --- CV ---
    cv_docx = cv._fill_template(CONTENT, job)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    # --- Cover letter ---
    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, contact_name=None)
    cl_pdf = _to_pdf_soffice(cl_docx)
    print("OK_CL", cl_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
