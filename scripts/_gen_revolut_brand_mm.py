"""One-off: generate Paula's CV + cover letter for Revolut
"Marketing Manager (Brand)" — Dubai / UAE (remote-friendly), Growth team.

Why this is a genuinely strong fit:
  - The role is B2C brand + growth marketing: lead local brand/growth in the UAE,
    own go-to-market product launches (audience strategy, messaging, comms), build
    full-funnel campaign calendars (acquisition -> retention), create data-driven
    stories and content that drive conversion, run experiments with analytical
    rigour, own tone of voice / style guides, adapt global campaigns to local
    nuance, and SCALE creative via playbooks for regional teams. Every one of those
    is squarely in Paula's wheelhouse.
  - Hyper-growth global tech pedigree: Alibaba's Miravia and Glovo are exactly the
    "hyper-growth global tech company" the JD prefers — B2C, fast-paced, data-led.
    At DoFreeze she runs brand + GTM (6 NPD launches end-to-end with messaging and
    positioning), full-funnel paid media on Meta/Google (A/B testing, ROAS = the
    experimentation + analytical rigour the JD asks for), and content/influencer
    programmes that drive conversion.
  - UAE growth execution: she is based in Dubai and executes growth in-market today
    (quick-commerce + modern-trade activation, local campaigns), which maps to
    "experience leading and executing growth strategies in the UAE".
  - Rare, on-the-nose edge: the JD explicitly wants someone to "scale creative
    marketing efforts globally by operationalising resources, such as playbooks for
    regional marketing teams". Paula BUILT an AI-powered marketing-automation system
    (Claude / generative AI) that turned planning, content and reporting into
    repeatable playbooks scaled across 50+ markets — a direct, differentiated match.

Honest positioning (NO fabrication):
  - Paula does NOT have fintech/payments sector experience — she is FMCG / beauty /
    fashion / e-commerce. This is disclosed in the cover letter, not hidden. The
    honest bridge is legitimate: she has worked inside consumer super-app / QC
    platforms (Glovo, Careem, Talabat, Deliveroo, Noon) and owns Shopify checkout /
    payment flows, so consumer-app and payment-adjacent context is real — but she
    is NOT claimed as a fintech expert.
  - Tenure: JD asks 5+ years B2C marketing; Paula has 4+ (with ~4 years across
    Glovo, Miravia and DoFreeze that is genuinely B2C/commercial). Framed as "4+"
    honestly; the hyper-growth-tech pedigree compensates. Not inflated to 5.
  - Per standing rule, NO "no sponsorship needed" claim — her UAE residence visa is
    employer-sponsored. States "already based in Dubai" only.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless — docx2pdf/Word silently fails on this Mac), registers the job
for the dashboard, and lands the package under output/2026-08-20/.
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

COMPANY = "Revolut"
TITLE = "Marketing Manager (Brand)"
DATE_FOLDER = "2026-08-20"

# Applied via Revolut's official careers portal — no hiring manager named in the
# posting, so the letter stays addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Marketing Manager (Brand) — Revolut. Office: Dubai. Remote: UAE. Growth team,
global fintech / financial super app (75M+ customers, 13,000+ people).

About the role: Marketing at Revolut is about clarity, creativity and commercial
impact. The Growth team turns bold ideas into campaigns that connect with
millions, working across channels and teams to build a brand that earns attention
and drives results. We're looking for a Marketing Manager to lead our brand and
growth efforts in the UAE — overseeing local campaign development, refining market
positioning, and launching initiatives that bring our features to life, while
partnering with regional leadership and global marketing.

What you'll be doing:
- Identifying customer needs by deeply understanding their behaviour and how our
  features work globally to create data-driven stories and content to drive
  conversion.
- Driving impactful go-to-market product launches by developing audience strategy,
  messaging and communication strategies.
- Developing research plans to uncover customer insights, steer and validate
  product and marketing roadmaps, and stay on top of the competitive landscape.
- Working with the global Growth team to develop market-leading campaign calendars
  designed to drive engagement across the entire funnel, from acquisition to
  retention.
- Owning tone of voice and style guides, adapting global campaigns aligned to
  local nuances.
- Running experiments to test hypotheses and bring analytical rigour to campaigns
  to inform the go-to-market strategy.
- Delivering campaigns with a solid bias for growth and business impact.
- Scaling creative marketing efforts globally by operationalising resources, such
  as playbooks for regional marketing teams.

What you'll need:
- 5+ years of experience in B2C marketing in a fast-paced environment (preferably a
  hyper-growth global tech company).
- Experience leading and executing growth strategies in the UAE.
- Excellent communication and interpersonal skills.
- Knowledge of markets and the competitive landscape in fintech or payments.
- Experience developing stories and compelling content to drive conversion.
- Expertise in setting strategic direction and project managing complex campaigns
  that require input and execution from cross-functional teams.
- A track record of planning and creating editorial and commercial content.
- The ability to analyse and distil data into actionable insights to inform
  campaign strategy and product development.
"""

ATS = [
    "Marketing Manager", "Brand", "brand marketing", "growth marketing",
    "B2C marketing", "go-to-market", "GTM", "product launch", "product launches",
    "audience strategy", "messaging", "communication strategy", "positioning",
    "market positioning", "campaign development", "campaign calendars",
    "full-funnel", "acquisition", "retention", "engagement", "conversion",
    "drive conversion", "data-driven stories", "storytelling", "content",
    "editorial content", "commercial content", "tone of voice", "style guides",
    "brand guidelines", "customer insights", "customer behaviour", "research plans",
    "competitive landscape", "experimentation", "A/B testing", "test hypotheses",
    "analytical rigour", "actionable insights", "business impact",
    "cross-functional", "project management", "complex campaigns",
    "operationalising", "playbooks", "regional marketing teams", "scale",
    "hyper-growth", "global tech", "fast-paced", "fintech", "payments",
    "super app", "quick-commerce", "paid media", "Meta Ads", "Google Ads", "ROAS",
    "ROI", "CRM", "EDM", "influencer marketing", "UGC", "omnichannel",
    "UAE", "Dubai", "GCC", "MENA", "growth strategy",
]

CV_CONTENT = {
    "headline": (
        "Brand & Growth Marketing Manager · B2C · Go-To-Market & Product Launches · "
        "Full-Funnel Campaigns · Data-Driven Content · Hyper-Growth Global Tech (Alibaba · Glovo)"
    ),
    "professional_summary": (
        "B2C brand and growth marketer with 4+ years across hyper-growth global tech, e-commerce and FMCG, "
        "now leading Brand & Marketing in Dubai. I build brands that earn attention and drive results: I run "
        "go-to-market product launches end-to-end (audience strategy, messaging, positioning), design "
        "full-funnel campaign calendars from acquisition to retention, and turn customer behaviour into "
        "data-driven stories and content that convert. I bring analytical rigour to everything — running paid-"
        "media experiments (Meta / Google, A/B testing, ROAS) and distilling data into actionable insights — "
        "and I scale creative through repeatable playbooks: at DoFreeze I built an AI-powered marketing-"
        "automation system (Claude / generative AI) that operationalised planning, content and reporting "
        "across 50+ markets. Trained inside hyper-growth global tech (Alibaba's Miravia, Glovo) and executing "
        "growth in the UAE today. Business Administration graduate (CUNEF), already based in Dubai."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Lead brand and growth in-market from Dubai — owning local campaign development, market positioning and go-to-market launches that bring products to life across the UAE and 50+ markets",
                "Drive go-to-market product launches end-to-end for 6 NPDs — defining audience strategy, messaging and communication plans, then landing them across paid, owned and earned channels",
                "Design full-funnel campaign calendars from acquisition to retention — paid media (Meta / Google Ads), influencer/UGC, social, EDM and e-store — balancing brand-building with a bias for growth and business impact",
                "Create data-driven stories and content that drive conversion — turning customer behaviour and product features into messaging, creative and content that lift CRO and average order value",
                "Bring analytical rigour to campaigns — running paid-media experiments and A/B tests, then distilling ROI, ROAS, conversion and retention data into actionable insights that inform strategy",
                "Scale creative by operationalising resources — built an AI-powered marketing-automation system (Claude / generative AI) that turned planning, content and reporting into repeatable playbooks used across regional markets, cutting manual workload ~40%",
                "Own tone of voice and brand consistency while adapting global assets to local nuance across GCC, MENA, Asia, Europe, USA and Africa",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Hyper-growth global tech | Top-5 e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Operated inside a hyper-growth global tech company (Alibaba), managing 42 B2C accounts and achieving +30% GMV growth QoQ through pricing, assortment and targeted, data-led campaigns",
                "Created and led the Beauty Club and 'Hot on Social' content projects end-to-end — planning editorial and commercial content that boosted engagement, loyalty (retention) and brand visibility",
                "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting to the CEO — running deadline-driven, full-funnel campaigns to drive conversion and business impact",
                "Continuously analysed conversion, traffic, retention, ROI and ROAS to test hypotheses and distil data into actionable insights that steered the commercial roadmap",
                "Tracked the competitive landscape and category trends to refine positioning and stay ahead in a fast-moving B2C market",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Hyper-growth quick-commerce super-app | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Worked inside a hyper-growth global tech super-app (Glovo), driving GMV growth for strategic B2C accounts through data-led planning and bespoke marketing activations",
                "Ran complex, cross-functional campaigns from brief to live — coordinating marketing, logistics and support to deliver engagement and order growth on tight timelines",
                "Helped build Glovo's Retail vertical — taking new fashion and lifestyle brands to market on the platform and expanding beyond food into new categories",
                "Negotiated and closed high-impact commercial deals, maximising profitability for both Glovo and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built sell-in/sell-out analysis and performance reports for the chocolate category, distilling data into actionable insights for brand and category planning",
                "Supported NPD launches (Milka Spread, Mini Suchard) from concept to shelf — early grounding in go-to-market and product marketing",
                "Evaluated promotional effectiveness and identified growth opportunities across the category",
            ],
        },
    ],
    "skills_brand": (
        "brand strategy & positioning, B2C brand marketing, growth marketing, go-to-market (GTM), "
        "product launch / NPD, audience strategy & messaging, full-funnel campaigns (acquisition to retention), "
        "editorial & commercial content, storytelling, tone of voice & style guides, influencer marketing, "
        "omnichannel campaigns, generative-AI marketing playbooks"
    ),
    "skills_ecommerce": (
        "paid media (Meta / Facebook / Instagram Ads, Google Ads), A/B testing & experimentation, "
        "conversion rate optimisation (CRO), CRM & EDM, social & UGC, Shopify e-store, "
        "quick-commerce & consumer super-apps (Noon, Talabat, Careem, Deliveroo), marketing automation"
    ),
    "skills_commercial": (
        "cross-functional project management, complex campaign delivery, stakeholder management, "
        "regional & global marketing partnership, key account management, negotiation, go-to-market execution"
    ),
    "skills_data": (
        "data-driven insight generation, customer & behavioural research, competitive-landscape analysis, "
        "A/B testing, ROI / ROAS / conversion / retention analysis, KPI tracking, forecasting, P&L, Power BI"
    ),
    "skills_tools": (
        "Generative AI (Claude, ChatGPT), Meta Ads Manager, Meta Business Suite, Google Ads, Shopify, "
        "Power BI, Salesforce, Canva, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Revolut is building a brand that earns attention and drives results at the scale of 75 million "
        "customers — and the Marketing Manager (Brand) role, leading brand and growth in the UAE, is exactly "
        "the kind of build I want to be part of. I am a B2C brand and growth marketer who came up inside "
        "hyper-growth global tech (Alibaba's Miravia and Glovo), and I now lead Brand & Marketing from Dubai, "
        "running go-to-market launches, full-funnel campaigns and data-driven content in-market every day. "
        "Bringing your global brand to life for a UAE audience — and operationalising it so regional teams can "
        "scale it — is the work I do best."
    ),
    "body_paragraph_1": (
        "The 'what you'll be doing' list maps almost line for line onto my day job. At DoFreeze I lead "
        "go-to-market product launches end-to-end — audience strategy, messaging and communication plans across "
        "six NPDs — and design full-funnel campaign calendars that move people from acquisition to retention "
        "through paid media, influencer/UGC, social, CRM/EDM and e-commerce. I turn customer behaviour and "
        "product features into data-driven stories and content that convert, and I bring genuine analytical "
        "rigour: I run paid-media experiments and A/B tests on Meta and Google, then distil ROI, ROAS, "
        "conversion and retention data into actionable insights that steer the strategy. Before Dubai, I did "
        "this inside two hyper-growth global tech companies — at Alibaba's Miravia I grew 42 B2C accounts +30% "
        "GMV QoQ and built the 'Beauty Club' and 'Hot on Social' content programmes; at Glovo I ran complex, "
        "cross-functional campaigns on a quick-commerce super-app."
    ),
    "body_paragraph_2": (
        "Two things make me a differentiated fit. First, your JD explicitly wants someone to 'scale creative "
        "marketing globally by operationalising resources, such as playbooks for regional teams' — that is "
        "precisely what I built: an AI-powered marketing-automation system (Claude / generative AI) that turned "
        "planning, content and reporting into repeatable playbooks running across 50+ markets, which is exactly "
        "how you turn one strong idea into engagement at Revolut's scale. Second, I am already executing growth "
        "in the UAE, so I know the market, the channels and the local nuance first-hand. I'll be candid about "
        "one gap: my sector background is e-commerce, consumer tech and FMCG rather than fintech — though I have "
        "worked inside consumer super-apps (Glovo, Careem, Talabat) and own Shopify checkout and payment flows, "
        "so app-based, payment-adjacent products are familiar terrain. I ramp fast, I'm obsessive about the "
        "competitive landscape, and I'd get up to speed on fintech quickly."
    ),
    "closing_paragraph": (
        "I would love to bring this blend of hyper-growth-tech pedigree, hands-on UAE growth execution and "
        "AI-powered ways of scaling creative to Revolut's Growth team, and to help make every move the brand "
        "makes in the UAE resonate and perform. I am already based in Dubai and available immediately, and I'd "
        "welcome the chance to talk through how I'd approach brand and growth for Revolut in-market. Thank you "
        "for your consideration — I look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="revolut-marketing-manager-brand-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.revolut.com/careers/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Marketing Manager Brand",
             "function": "Brand / Growth Marketing", "workplace": "Office (Dubai) / Remote (UAE)",
             "team": "Growth",
             "note": "Apply only via official Revolut careers channel (@revolut.com) — Revolut warns of recruitment scams"},
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
        "ai_score": 82,
        "ai_tier": "Hot",
        "skills_match": [
            "B2C brand + growth marketing — leads brand/growth in-market (DoFreeze Dubai) TODAY, core of the JD",
            "Go-to-market product launches end-to-end (6 NPDs: audience strategy, messaging, comms)",
            "Full-funnel campaign calendars, acquisition -> retention (paid, influencer, CRM/EDM, social, e-store)",
            "Data-driven stories & content that drive conversion (CRO, AOV, content programmes)",
            "Analytical rigour / experimentation — Meta & Google paid-media A/B testing, ROAS/ROI/conversion/retention",
            "Scaling creative via playbooks — BUILT an AI marketing-automation system (Claude) scaled across 50+ markets (on-the-nose match to the JD's 'playbooks for regional teams')",
            "Hyper-growth global tech pedigree — Alibaba's Miravia + Glovo (exactly the 'hyper-growth global tech company' preferred)",
            "UAE growth execution — based in Dubai, executes local growth now",
            "Cross-functional project management of complex campaigns",
            "Tone of voice / brand consistency, adapting global assets to local nuance",
            "Bachelor's in Business Administration; fluent English (C1); already based in Dubai",
        ],
        "missing_skills": [
            "Fintech / payments sector knowledge (real gap — she is e-commerce / consumer tech / FMCG). Honest bridge: consumer super-apps (Glovo, Careem, Talabat) + Shopify checkout/payment flows; disclosed in cover letter, NOT claimed as fintech expertise",
            "5+ years B2C marketing asked; Paula has 4+ (with ~4 genuinely B2C across Glovo, Miravia, DoFreeze) — framed honestly, not inflated",
        ],
        "sector_fit": "adjacent (B2C consumer tech / e-commerce; fintech is new — disclosed honestly)",
        "seniority_fit": "on-band (Marketing Manager; 4+ vs 5+ yrs — hyper-growth-tech pedigree compensates)",
        "red_flags": [
            "No fintech/payments experience — the single real gap. Positioned truthfully via super-app + payment-adjacent context and fast ramp; never fabricated. Everything else (brand, growth, GTM, full-funnel, content, experimentation, playbooks, UAE, hyper-growth tech) is a direct, strong match.",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong fit. The role is B2C brand + growth marketing in the UAE — leading local campaign "
            "development, GTM product launches (audience strategy, messaging, positioning), full-funnel campaign "
            "calendars (acquisition -> retention), data-driven stories/content that convert, experimentation "
            "with analytical rigour, tone-of-voice ownership, adapting global campaigns to local nuance, and "
            "scaling creative via playbooks for regional teams. Paula does all of this today at DoFreeze in "
            "Dubai and did it inside two hyper-growth global tech companies (Alibaba's Miravia, Glovo) — the "
            "exact profile the JD prefers. Her rarest edge lands on-the-nose: she BUILT an AI-powered "
            "marketing-automation system (Claude/generative AI) that operationalised planning/content/reporting "
            "into repeatable playbooks across 50+ markets, which is precisely the JD's 'scale creative by "
            "operationalising playbooks for regional teams'. The one real gap is fintech/payments sector "
            "knowledge (she is e-commerce/consumer-tech/FMCG); disclosed openly in the cover letter and bridged "
            "honestly via consumer super-apps (Glovo/Careem/Talabat) and Shopify checkout/payment flows, never "
            "fabricated. Tenure 4+ vs 5+ asked, framed honestly. No 'no sponsorship needed' claim "
            "(employer-sponsored visa) — states 'already based in Dubai' only."
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
