"""One-off: generate Paula's CV + cover letter for Fluke Corporation (Fortive)
"Channel Marketing Manager MEAT (Middle East, Africa, Turkey)" — Dubai, UAE.

Honest fit: MODERATE STRETCH. This is a B2B **channel / distribution marketing**
role in industrial test & measurement — lead partner-led go-to-market across
VARs, electrical wholesalers and distributors: co-op/MDF plans, POS reach, roll
out central campaigns + NPIs at partners, ABM with key distributors, AI-driven
marketing, and pipeline/lead/ROI ownership in close alignment with channel &
field sales. Paula is a B2C/FMCG/Beauty/E-Commerce marketer, NOT a B2B tech
marketer — but there are real, truthful bridges:

  - Channel / TRADE marketing through DISTRIBUTORS is exactly what she does at
    DoFreeze (a *global FMCG distributor*): channel/trade plans across 50+
    markets incl. MEA + Africa, co-op activations, promo mechanics, A&P budgets,
    and NPI roll-out at modern-trade + quick-commerce partners. In FMCG this is
    called "trade marketing"; in tech it's called "channel marketing" — same
    mechanics (partner go-to-market, POS reach, co-op, sell-out).
  - Key Account / partner management: 42 key accounts at Alibaba's Miravia
    (+30% GMV QoQ) via joint business plans, targeted promotions and
    assortment/pricing with strategic partners — *including official
    distributors* of Arabian oud houses. That is partner/channel work and
    account-based (ABM-style) targeting of high-value partners.
  - AI-DRIVEN MARKETING is Paula's standout differentiator and the JD asks for
    it explicitly ("leverage AI-powered tools ... segmentation, personalization,
    campaign performance"). She built a Claude/GPT automation engine for exactly
    this. Rare, genuine, strong match.
  - Digital demand gen + ROI: Meta/Google Ads, funnel/lead generation, CRO,
    ROI/ROAS — genuine performance-marketing track.
  - Already in Dubai on a UAE residence visa (role is Dubai-based).

Truthful gaps — positioned as adjacent, NEVER invented:
  - B2B / industrial / test & measurement vertical: she is B2C FMCG/Beauty/
    E-Commerce. Positioned as transferable channel skill + fast vertical ramp,
    never claimed as owned B2B-tech tenure.
  - VARs / electrical wholesalers channel: she runs distributors, modern trade
    and quick-commerce — adjacent partner types, positioned as such.
  - Formal ABM martech programs: she runs KAM + targeted high-value-account
    plans (ABM in spirit) + digital demand gen — positioned as ABM-style, not as
    named enterprise ABM software.
  - Turkey specifically: covers 50+ countries incl. MEA + Africa; Turkey market
    not owned — the wider MEAT remit is largely covered by her multi-market work.
  - VISA: already in Dubai on an *employer-sponsored* UAE residence visa. Per the
    standing rule we NEVER claim "no sponsorship needed" — only that she is
    already based in Dubai (zero relocation timeline).

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful. Fills the real CV + cover-letter templates, converts to PDF via
LibreOffice (soffice headless — docx2pdf/Word silently fails on this Mac),
registers the job for the dashboard, and lands the package under
output/2026-08-26/.
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

COMPANY = "Fluke Corporation"
TITLE = "Channel Marketing Manager MEAT"
DATE_FOLDER = "2026-08-26"

# Promoted by a recruiter ("Respuestas gestionadas fuera de LinkedIn"); no named
# hiring manager in the post, so the letter stays addressed to "Hiring Manager".
CONTACT = None

JOB_DESCRIPTION = """\
Channel Marketing Manager MEAT (Middle East, Africa, Turkey) — Fluke Corporation
(a Fortive company), Dubai, UAE. Full-time, on-site.

Fluke is seeking a Channel Marketing Manager MEAT to lead and scale channel and
field marketing across Value Added Resellers (VARs), Electrical Wholesalers and
other distribution partners towards end users. Based in Dubai, the role drives
marketing strategy, accelerates growth through partners, and strengthens
alignment with Fluke channel and field sales teams. Pivotal in driving revenue
growth through indirect sales channels by aligning marketing, sales and channel
partners around a common growth strategy.

Key Responsibilities:
- Channel Strategy & Growth: define and execute channel marketing strategies that
  drive demand, increase product visibility and accelerate revenue through
  partners; focus on Co-op marketing with Premium Partners to boost Point of Sale
  (POS) reach, grow mindshare, strengthen partner loyalty, ensure brand
  consistency and support market expansion.
- Annual Planning & Optimization: work with strategic channel partners on annual
  marketing plans, budgets and joint campaigns while ensuring marketing
  development funds / co-op budgets deliver measurable returns.
- Commercial Channel Marketing Execution: roll out Fluke central marketing
  campaigns, promotions and NPIs at key partners; expand reach in digital
  marketing; drive leads and funnel inflow from co-op events; ensure distribution
  partners have the marketing assets, sales tools, campaigns, training and
  incentives to sell effectively (channel readiness).
- Customer Journey Ownership: own and improve the end-user buying experience
  across distributor digital platforms, physical outlets, events/webinars and
  sales interactions.
- Account-Based Marketing (ABM): develop and execute ABM programs with key
  distributors and strategic accounts, targeting high-value customers with
  tailored campaigns.
- AI-Driven Marketing: leverage AI-powered tools and insights to optimize
  segmentation, personalization, campaign performance and efficiency across the
  channel.
- Commercial Alignment: partner closely with channel sales and field sales teams
  so marketing programs directly contribute to pipeline and revenue.
- Performance & ROI Management: manage co-op budgets and track campaign
  effectiveness, partner engagement, ROI/ROAS, pipeline growth, revenue
  contribution, market opportunities and customer behavior.
- Innovation & Experimentation: continuously test, learn and scale new approaches
  across digital, AI and partner-driven marketing.

KPIs: pipeline growth, lead generation, revenue contribution, return on marketing
investment (ROI/ROAS).

Experience & Qualifications:
- 5+ years of B2B marketing, ideally within channel or distribution environments;
  test and measurement industry a plus.
- Digital marketing experience and familiarity with latest tools.
- Track record in pipeline growth and lead/funnel generation programs.
- Familiarity with AI-driven marketing tools and data-led campaign optimization.
- Experience with account-based marketing (ABM) and targeted demand generation.
- Proven experience working closely with sales teams (channel and/or field).
- Strong analytical skills; ability to translate data into strategic actions.
- Demonstrated success in budget ownership and ROI-driven decision-making.
- Bachelor's degree or equivalent experience.
- Excellent communication skills in English (additional languages a plus).
"""

ATS = [
    "Channel Marketing Manager", "channel marketing", "channel strategy",
    "channel & field marketing", "distribution partners", "distributors",
    "distributor management", "VARs", "value added resellers",
    "electrical wholesalers", "indirect sales channels", "partner marketing",
    "partner go-to-market", "premium partners", "co-op marketing", "co-op budgets",
    "marketing development funds", "MDF", "point of sale", "POS reach",
    "partner loyalty", "brand consistency", "market expansion",
    "annual marketing plans", "joint campaigns", "joint business planning",
    "NPI", "new product introduction", "campaign rollout", "channel readiness",
    "sales tools", "marketing assets", "customer journey", "end-user experience",
    "events", "webinars", "account-based marketing", "ABM",
    "targeted demand generation", "demand generation", "AI-driven marketing",
    "AI-powered tools", "segmentation", "personalization",
    "campaign optimization", "digital marketing", "lead generation",
    "funnel generation", "pipeline growth", "revenue contribution",
    "commercial alignment", "channel sales", "field sales", "sales alignment",
    "ROI", "ROAS", "return on marketing investment", "budget ownership",
    "data-driven decision making", "analytics", "B2B marketing",
    "Middle East", "Africa", "Turkey", "MEA", "MENA", "GCC", "UAE", "Dubai",
]

CV_CONTENT = {
    "headline": (
        "Channel & Trade Marketing · Distributor / Partner Go-To-Market · MEA Multi-Market · "
        "AI-Driven Marketing · Digital Demand Gen, Co-op Budgets & ROI"
    ),
    "professional_summary": (
        "Channel, trade and brand marketing professional with ~5 years across FMCG, Beauty and "
        "E-Commerce, running partner- and distributor-led go-to-market across 50+ markets (GCC, MENA, "
        "Africa, Asia, Europe, USA). Currently at DoFreeze — a global FMCG distributor — building "
        "channel/trade plans, co-op activations, promo mechanics and NPI roll-outs through modern-trade "
        "and quick-commerce partners, with hands-on A&P/co-op budget ownership tracked on ROI. Previously "
        "owned 42 key accounts at Alibaba's Miravia (+30% GMV QoQ) via joint business plans, targeted "
        "promotions and assortment/pricing with strategic partners, including official distributors. Early "
        "adopter of AI-driven marketing — built a Claude/GPT automation engine for segmentation, campaign "
        "planning, content and KPI reporting. Strong on digital demand generation (Meta/Google Ads), "
        "lead/funnel and ROI/ROAS. Already based in Dubai on a UAE residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Build and execute channel & trade marketing plans across 50+ markets (GCC, MENA, Africa, Asia, Europe, USA), working with distributor and modern-trade partners on annual joint plans, co-op activations and A&P budgets to grow point-of-sale reach, mindshare and sell-out",
                "Roll out central brand campaigns, promotions and 6 end-to-end NPI launches at key partners — brief, packaging, pricing, go-to-market and channel readiness (marketing assets, promo mechanics and retail execution so partners can sell effectively)",
                "Integrated brands into UAE modern-trade and quick-commerce partners (Noon, Talabat, Careem, Deliveroo) — partner onboarding, listings, promotional mechanics and in-store/online execution to expand distribution reach",
                "Built an AI-driven marketing engine (Claude / generative AI) automating segmentation, campaign planning, content, market research and KPI reporting — cutting manual workload ~40% and accelerating partner go-to-market across markets",
                "Own paid digital demand generation (Meta Ads, Google Ads) and the brand's Shopify store — audience building, creative A/B testing and CRO — tracking ROI/ROAS to drive leads, funnel inflow and measurable channel performance",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Managed 42 key accounts, delivering +30% GMV growth QoQ through joint business plans, targeted promotions and assortment/pricing strategy with strategic partners",
                "Ran account-based, tailored plans for high-value partners — onboarding 30+ partner stores in two months as PIC Fragrances, including the official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) via co-op promotions and trend-led assortment",
                "Owned the Flash Sales channel for Beauty, Fashion & Home (reporting directly to the CEO), executing commercial plans aligned with P&L targets",
                "Continuously analysed ROI, ROAS, conversion, traffic and retention to optimise channel performance and forecasting accuracy",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic XL key accounts and helped build Glovo's Retail vertical — onboarding brand partners and expanding the marketplace beyond food, growing GMV through data-led joint planning and bespoke activations",
                "Partnered closely with sales, marketing, logistics and operations (cross-functional) to deliver campaigns and grow order volume",
                "Negotiated and closed high-impact commercial deals, maximising profitability for both platform and partners",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Ran category deep dives for chocolate — sell-in/sell-out, Nielsen and promotional-effectiveness analysis — turning data into clear commercial and trade recommendations",
                "Supported NPD/NPI launches (Milka Spread, Mini Suchard) from concept to shelf, coordinating listings and go-to-market with head office",
            ],
        },
    ],
    "skills_brand": (
        "channel marketing, trade marketing, co-op / MDF activation, partner go-to-market, "
        "NPI / NPD launch & rollout, account-based marketing (targeted key-account plans), "
        "shopper marketing, A&P & co-op budget management, omnichannel campaigns, AI-driven marketing"
    ),
    "skills_ecommerce": (
        "digital demand generation, Meta Ads (Facebook & Instagram), Google Ads, lead & funnel generation, "
        "conversion rate optimisation (CRO), Shopify & e-store management, quick-commerce (Noon, Talabat, "
        "Careem, Deliveroo), marketing automation, EDM"
    ),
    "skills_commercial": (
        "key account management, distributor & partner management, modern trade, joint business planning (JBP), "
        "commercial negotiation, pricing strategy, assortment planning, category management, "
        "sales & channel alignment"
    ),
    "skills_data": (
        "ROI / ROAS, pipeline & funnel metrics, KPI tracking, sell-in/sell-out, P&L management, "
        "AI-assisted analysis & forecasting, segmentation & personalization, Power BI, Nielsen, Salesforce"
    ),
    "skills_tools": (
        "Generative AI (Claude, ChatGPT), Meta Ads Manager, Meta Business Suite, Google Ads, Shopify, "
        "Salesforce, SAP, Power BI, Looker, Microsoft Office (Expert), Canva"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Fluke's channel program — partner-led growth, co-op with premium partners, POS reach and channel "
        "readiness that lets distributors sell effectively — is exactly the kind of channel marketing I run "
        "every week, just in FMCG and retail distribution rather than test & measurement. The Channel "
        "Marketing Manager MEAT role caught my attention because it asks for what I already do: build annual "
        "partner plans and co-op activations, roll out central campaigns and NPIs at key partners, and drive "
        "demand and ROI through the channel — now supercharged with AI-driven marketing, which happens to be "
        "my sharpest edge."
    ),
    "body_paragraph_1": (
        "Channel and trade marketing through distributors is the spine of my career. Today, as Brand & "
        "Marketing Manager at DoFreeze — a global FMCG distributor — I build channel and trade plans across "
        "50+ markets, including the Middle East and Africa, working with distributor and modern-trade partners "
        "on annual joint plans, co-op activations, promo mechanics and NPI roll-outs, while owning A&P and "
        "co-op budgets tracked on ROI. Before Dubai, I owned 42 key accounts at Alibaba's Miravia and grew "
        "GMV +30% QoQ through joint business plans, targeted promotions and assortment/pricing with strategic "
        "partners — including official distributors of leading Arabian and oud houses. In FMCG we call it "
        "trade marketing; the mechanics — partner go-to-market, POS reach, co-op budgets and sell-out — are "
        "the same ones this role runs."
    ),
    "body_paragraph_2": (
        "Two things set me apart. First, AI-driven marketing: I built a Claude/GPT automation engine for "
        "segmentation, campaign planning, content and KPI reporting — precisely the AI-powered optimization "
        "the role calls for, and a capability I can bring on day one. Second, digital demand generation and "
        "ROI discipline: I run Meta and Google Ads, lead and funnel generation and CRO, always measured on "
        "ROI/ROAS. I'll be candid that my channel experience sits in FMCG and retail distribution "
        "(distributors, modern trade, quick-commerce) rather than VARs and electrical wholesalers in test & "
        "measurement — but the partner mechanics transfer directly, and I ramp fast on a new vertical and "
        "product set. I'm also already in Dubai on a UAE residence visa, so I can start without a relocation "
        "timeline."
    ),
    "closing_paragraph": (
        "I would be excited to bring this blend of channel and trade marketing, AI-driven demand generation "
        "and ROI discipline to Fluke's partner ecosystem across the Middle East, Africa and Turkey. I am "
        "available to start immediately and would welcome the chance to discuss how I would approach partner "
        "co-op plans, NPI roll-out and pipeline growth across the MEAT channel. Thank you for your "
        "consideration — I look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="fluke-channel-marketing-manager-meat-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://www.linkedin.com/jobs/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Channel Marketing Manager MEAT",
             "parent": "Fortive Corporation (NYSE: FTV)",
             "function": "Channel / Field Marketing (B2B)",
             "region": "Middle East, Africa, Turkey (MEAT)",
             "industry": "Test & Measurement / Industrial technology"},
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
        "ai_score": 72,
        "ai_tier": "Warm",
        "skills_match": [
            "Channel / trade marketing through distributors + modern trade (DoFreeze, 50+ markets incl. MEA/Africa)",
            "Co-op / MDF activations + A&P/co-op budget ownership tracked on ROI",
            "Roll out central campaigns + NPI launches at partners (channel readiness)",
            "Key Account / partner management (Miravia 42 accounts +30% GMV QoQ; Glovo XL)",
            "Account-based, tailored plans for high-value partners incl. official distributors (ABM-style)",
            "AI-driven marketing — Claude/GPT engine for segmentation, campaigns, content, KPI reporting",
            "Digital demand generation (Meta/Google Ads), lead & funnel generation, CRO",
            "ROI/ROAS, P&L, KPI tracking, sell-in/sell-out analytics",
            "Sales & channel alignment (cross-functional KAM roles)",
            "Already in Dubai (UAE residence visa) — role is Dubai-based",
        ],
        "missing_skills": [
            "B2B / industrial / test & measurement vertical — has B2C FMCG/Beauty/E-Commerce, adjacent channel skills",
            "VARs / electrical wholesalers channel — has distributors, modern trade, quick-commerce (adjacent partner types)",
            "Formal enterprise ABM martech programs — has KAM + targeted high-value-account plans + digital demand gen (ABM in spirit)",
            "Turkey market specifically — covers 50+ countries incl. MEA + Africa; Turkey not owned",
            "5+ yrs B2B specifically — ~5 yrs total but B2C/FMCG, not B2B",
        ],
        "sector_fit": "stretch (channel/trade marketing transfers; vertical is B2B industrial vs. B2C FMCG)",
        "seniority_fit": "on band (~5 yrs vs. 5+; channel/partner + KAM track)",
        "red_flags": [
            "Core JD is B2B channel marketing in test & measurement (VARs/electrical wholesalers). Paula's channel work is FMCG/retail distribution — mechanics transfer but the vertical and partner types differ; positioned truthfully as adjacent + fast ramp.",
            "'ABM programs' expected — Paula has KAM + targeted high-value-account plans (ABM in spirit), not named enterprise ABM software.",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Moderate-stretch fit anchored on channel/trade marketing and AI. The role leads partner-led "
            "go-to-market across VARs, electrical wholesalers and distributors: co-op/MDF plans, POS reach, "
            "roll out central campaigns + NPIs at partners, ABM with key distributors, AI-driven marketing "
            "and pipeline/lead/ROI ownership aligned with channel & field sales. Paula's DoFreeze work is "
            "genuine channel/trade marketing through a *global FMCG distributor* — channel plans across 50+ "
            "markets incl. MEA + Africa, co-op activations, promo mechanics, A&P/co-op budgets and NPI "
            "roll-out at modern-trade + quick-commerce partners (FMCG calls it 'trade marketing'; same "
            "mechanics as B2B 'channel marketing'). Her 42-account KAM track at Miravia (+30% GMV QoQ, incl. "
            "official distributors) is partner/channel + ABM-style targeting. Her standout edge is AI-driven "
            "marketing (Claude/GPT automation for segmentation/campaigns/content/KPIs) — which the JD asks "
            "for explicitly — plus digital demand gen (Meta/Google Ads, funnel/lead) and ROI/ROAS. Honest "
            "gaps: B2B/industrial/test-&-measurement vertical (she is B2C FMCG/Beauty/E-Commerce), VARs & "
            "electrical wholesalers specifically (has distributors/modern trade/quick-commerce), formal "
            "enterprise ABM martech, and the Turkey market. Positioned truthfully as adjacent channel skill "
            "with fast vertical ramp; no invented B2B-tech, VAR, ABM-software or product tenure, and no 'no "
            "sponsorship needed' claim (she is on an employer-sponsored UAE residence visa)."
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
