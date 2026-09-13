"""One-off: generate Paula's CV + cover letter for Binance
"Affiliate Relationship Manager - MENA" (Dubai, UAE — remote).

Read honestly: STRETCHIER than the Creator Partnerships role. The role's spine is
relationship/affiliate/partner management — which is Paula's core (KAM: 42 accounts
at Miravia, XL at Glovo; KOL/creator programmes at DoFreeze) and the JD explicitly
accepts "Affiliate Marketing, Key Account Management (KAM), or B2B partnership
management" as qualifying industry experience. BUT the primary industry requirement
is professional experience in "Crypto, FX, CFD, Trading Platforms, or related
financial industries" plus familiarity with exchange affiliate ecosystems,
commission/rebate mechanisms and trading-abuse risk (wash trading, arbitrage,
multi-accounting) — a specialised crypto/FX-trading domain Paula does NOT have
professionally. She is a personal crypto user/investor only. LinkedIn itself flags
the match as low. So: worth a low-effort Easy Apply given the strong transferable
KAM/partnership spine + no Arabic requirement + it's Binance, but with realistic
expectations. Scored Warm.

Honest positioning (NO fabrication):
  - NO professional crypto/FX/CFD/trading-platform experience claimed. Crypto is
    stated only as genuine personal use/investing + following the ecosystem.
  - NO invented knowledge of rebate mechanisms, wash-trading detection or exchange
    affiliate mechanics. Real, transferable work only: KAM, partner relationship
    management, retention, commission/incentive & co-marketing negotiation,
    onboarding/due-diligence, dispute/escalation handling, performance/anomaly
    monitoring, cross-functional collaboration.
  - Spanish (native) surfaced for the "additional languages an advantage" +
    LATAM/cross-cultural preference. NO Arabic claim.
  - Remote role; already in Dubai on a UAE residence visa. NO "no sponsorship
    needed" claim.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice,
registers the job for the dashboard, and lands the package under output/2026-08-30/.
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

COMPANY = "Binance"
TITLE = "Affiliate Relationship Manager - MENA"
DATE_FOLDER = "2026-08-30"

CONTACT = None

JOB_DESCRIPTION = """\
Affiliate Relationship Manager (ARM) - MENA — Binance, Dubai, UAE (Remote,
full-time). Manage and grow long-term relationships with key affiliates and channel
partners across MENA. Not cold acquisition / aggressive BD — a strategic partner
manager responsible for affiliate retention, revenue growth, relationship stability
and risk awareness. Ideal candidate understands the crypto/FX affiliate ecosystem
deeply, is relationship-oriented, commercially sensitive, and balances growth with
compliance and platform interests.

Responsibilities: manage relationships with existing affiliates, KOLs, trading
communities and strategic partners; drive affiliate performance growth (user
acquisition, trading volume, retention, revenue contribution); monitor affiliate
performance metrics and identify abnormal behaviours, risks or opportunities; handle
affiliate concerns professionally (commission disputes, competitor poaching,
operational escalations); collaborate with Marketing, Product, Operations, Risk,
Compliance and Legal; design and execute joint campaigns, incentive programs and
partnership initiatives; analyse affiliate ROI, trading behaviours and lifecycle
performance; identify and prevent risks such as wash trading, arbitrage abuse,
multi-accounting or non-compliant traffic; maintain market awareness of competitor
affiliate programs, commission structures and industry trends; support affiliate
onboarding, due diligence and long-term relationship development.

Requirements — Industry Experience: experience in Crypto, FX, CFD, Trading Platforms
or related financial industries; familiar with exchange affiliate ecosystems,
commission structures and rebate mechanisms; experience in Affiliate Marketing, Key
Account Management (KAM) or B2B partnership management; strong understanding of
affiliate lifecycle management and partner incentive systems.
Core Competencies: strong relationship management and stakeholder communication;
handle sensitive partner situations with maturity; good analytical skills (trading
volume, retention, ROI, behavioural trends); commercial negotiation (exclusive
partnerships, tiered commissions, co-marketing); strong risk awareness (affiliate
abuse, compliance, suspicious activity); cross-cultural communication — experience
managing LATAM, MENA, SEA or global markets preferred.
Personality: patient, stable, long-term relationship oriented; strong service
mindset; high EQ; detects early churn/competitor signals; self-driven, detail-
oriented, fast-paced.
Nice to have: trading/quant background; compliance/risk/due-diligence experience;
managing online communities or affiliate ecosystems. Fluency in English required;
additional languages an advantage.
"""

ATS = [
    "Affiliate Relationship Manager", "affiliate management", "affiliate marketing",
    "Key Account Management", "KAM", "B2B partnership management", "partner management",
    "channel partners", "affiliate retention", "relationship management",
    "stakeholder communication", "revenue growth", "user acquisition", "retention",
    "affiliate lifecycle", "partner incentive systems", "incentive programs",
    "commission structures", "tiered commissions", "co-marketing", "joint campaigns",
    "commercial negotiation", "exclusive partnerships", "onboarding", "due diligence",
    "performance metrics", "ROI", "behavioural trends", "risk awareness",
    "abnormal behaviour", "compliance", "escalations", "commission disputes",
    "competitor", "market awareness", "KOLs", "communities", "cross-cultural",
    "LATAM", "MENA", "SEA", "global markets", "crypto", "Web3", "English", "Spanish",
    "remote", "Dubai", "UAE",
]

CV_CONTENT = {
    "headline": (
        "Key Account & Partnership Management · Affiliate, KOL & Channel-Partner Relationships · "
        "Retention, Incentives & Commercial Negotiation · Crypto User/Investor · Spanish-Native / English C1"
    ),
    "professional_summary": (
        "Relationship-driven Key Account and partnership manager with 5+ years managing portfolios of key "
        "accounts, partners and creators across consumer internet, marketplaces and FMCG. My core is exactly "
        "this role: long-term partner relationship management, retention and revenue growth through tiered "
        "promotions, incentives and co-marketing, plus commercial negotiation, onboarding/due diligence and "
        "professional handling of disputes and escalations. At Alibaba's Miravia I managed a 42-account "
        "portfolio, growing GMV +30% QoQ, and I run creator/KOL and community programmes at DoFreeze. I monitor "
        "partner performance and ROI, flag anomalies and risks, and collaborate cross-functionally with "
        "marketing, product, operations and finance. Native Spanish speaker (a plus for LATAM/cross-cultural) "
        "with C1 English, a personal crypto user and investor who follows the Web3 and exchange ecosystem, "
        "self-driven and comfortable in remote, global teams. Already based in Dubai."
    ),
    "experience": [
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Managed a portfolio of 42 key accounts and partners — long-term relationship management, retention and revenue growth (+30% GMV QoQ) through tiered promotions, pricing and co-marketing initiatives",
                "Negotiated commercial terms and incentive/commission-style promotional support, owning the Flash Sales channel and reporting to the CEO against P&L targets",
                "Recruited and onboarded 30+ new partners in two months with selection and due diligence, and handled partner concerns, escalations and competitor pressure professionally",
                "Monitored partner performance, ROI, conversion, retention and behavioural trends — flagging anomalies, risks and growth opportunities across the partner ecosystem",
            ],
        },
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Homegrown UAE F&B / FMCG group | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Manage long-term relationships with creators, KOLs and channel/retail partners — briefing, negotiation, incentive and collaboration programmes, and ongoing relationship development across 50+ markets",
                "Design and execute joint campaigns and incentive/partnership initiatives, driving partner performance (reach, engagement and sell-out) and retention",
                "Track partner and campaign performance metrics, flag anomalies and opportunities, and handle partner concerns and escalations professionally",
                "Collaborate cross-functionally with marketing, product, supply chain and finance, and use generative-AI automation to scale reporting and market/competitor research",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "High-growth consumer-internet / quick-commerce | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic partner and key accounts at a high-growth consumer-internet platform — relationship management, retention and data-led joint planning",
                "Negotiated and closed commercial deals and incentive structures, maximising profitability for both platform and partners",
                "Coordinated cross-functional execution across marketing, operations and support to grow partner revenue",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Analysed sell-in/sell-out, ROI and promotional effectiveness, turning data into clear insights and recommendations",
                "Built recurring performance reports that fed commercial and partner planning",
            ],
        },
    ],
    "skills_commercial": (
        "key account management (KAM), affiliate & partner relationship management, B2B partnership management, "
        "partner onboarding & due diligence, commission/incentive & tiered-deal negotiation, retention & "
        "lifecycle management, dispute & escalation handling, exclusive partnerships & co-marketing"
    ),
    "skills_data": (
        "partner performance & ROI analysis, retention & behavioural-trend analysis, anomaly / risk flagging, "
        "KPI dashboards & reporting, conversion analysis, competitor & market-trend awareness, AI-assisted analysis"
    ),
    "skills_brand": (
        "KOL / creator & community management, affiliate & partner programmes, joint campaigns & co-marketing, "
        "incentive programme design, cross-channel marketing, go-to-market"
    ),
    "skills_ecommerce": (
        "marketplaces & consumer-internet platforms (Alibaba/Miravia, Glovo), quick-commerce (Noon, Talabat, "
        "Careem, Deliveroo), crypto exchanges (personal user/investor), CRM & lifecycle, social & content platforms"
    ),
    "skills_tools": (
        "Generative AI (Claude, ChatGPT), Salesforce, Power BI, Tableau, Looker, Google Sheets & Excel (Expert), "
        "Notion, Meta Ads Manager, Canva, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "This role is fundamentally about what I do best: managing long-term partner relationships, growing "
        "retention and revenue, and negotiating incentives and co-marketing — as a steady, service-minded "
        "partner rather than a cold-acquisition hunter. I'm also a native Spanish speaker with C1 English (useful "
        "for LATAM and cross-cultural partner work) and a personal crypto user and investor who follows the "
        "exchange and Web3 ecosystem closely."
    ),
    "body_paragraph_1": (
        "Relationship and key account management is the spine of my career. At Alibaba's Miravia I managed a "
        "42-account partner portfolio, growing revenue +30% QoQ through tiered promotions, incentives and "
        "co-marketing, while negotiating commercial terms, onboarding 30+ partners with due diligence, handling "
        "escalations and competitor pressure, and monitoring performance and behavioural trends to flag risks "
        "and opportunities. Today at DoFreeze I manage creator, KOL and channel-partner relationships across 50+ "
        "markets — incentive and collaboration programmes, joint campaigns and cross-functional work with "
        "marketing, product, operations and finance. That maps directly onto affiliate lifecycle management, "
        "partner incentive systems, dispute handling and performance monitoring."
    ),
    "body_paragraph_2": (
        "I'll be straight about fit: my industry background is consumer internet, marketplaces and FMCG rather "
        "than years inside a crypto/FX exchange, so I'd be learning the specific affiliate rebate mechanics and "
        "trading-abuse risk signals rather than arriving with them. What I bring is a very strong, transferable "
        "KAM and B2B partnership foundation, genuine personal crypto experience and enthusiasm for the space, "
        "cross-cultural/Spanish coverage, and the patient, high-EQ, service-oriented style this role calls for — "
        "plus I ramp fast and I'm already based in Dubai and set up to work remotely."
    ),
    "closing_paragraph": (
        "I'd welcome the chance to show how I'd protect and grow a MENA affiliate portfolio — stabilising key "
        "relationships, spotting early churn or competitor signals, and designing incentive and co-marketing "
        "programmes that grow performance responsibly. Thank you for considering my application — I'd be glad to "
        "discuss how my partnership track record would transfer to Binance's affiliate ecosystem."
    ),
}


def make_job() -> Job:
    return Job(
        id="binance-affiliate-relationship-manager-mena-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates (Remote)",
        url="https://www.binance.com/en/careers",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Affiliate Relationship Manager MENA Binance remote",
             "function": "Affiliate / Partner Relationship Management",
             "workplace": "Remote, Dubai UAE",
             "note": "No Arabic required (English required; additional languages a plus). Primary gap: "
                     "professional crypto/FX/trading-platform industry experience. LinkedIn flagged low match."},
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
        "ai_score": 62,
        "ai_tier": "Warm",
        "skills_match": [
            "Key Account Management + B2B partnership management (explicitly accepted by JD) — Miravia 42 accounts, Glovo XL",
            "Long-term partner relationship management, retention & revenue growth (+30% GMV QoQ)",
            "Commission/incentive & tiered-deal negotiation, co-marketing & joint campaigns",
            "Partner onboarding & due diligence; dispute/escalation handling",
            "Performance/ROI monitoring + anomaly/risk flagging",
            "KOL / creator & community management (DoFreeze)",
            "Cross-functional with marketing/product/ops/finance",
            "Native Spanish (LATAM/cross-cultural plus); English C1 — no Arabic needed here",
            "Personal crypto user & investor; follows the exchange/Web3 ecosystem",
            "Self-driven, remote/global, already in Dubai",
        ],
        "missing_skills": [
            "Professional Crypto/FX/CFD/Trading-Platform industry experience — the PRIMARY industry requirement — NOT held (personal crypto use only)",
            "Exchange affiliate ecosystems, commission/rebate mechanisms — crypto/FX-specific, not held",
            "Trading-abuse risk (wash trading, arbitrage abuse, multi-accounting) — specialised, not held",
            "Trading/quant or compliance/risk/due-diligence background (nice-to-have) — not held",
        ],
        "sector_fit": "transferable spine strong (KAM/affiliate/partnerships); crypto/FX-trading domain is the gap",
        "seniority_fit": "on-band experienced (5+ yrs KAM/partnerships)",
        "red_flags": [
            "Primary industry requirement is crypto/FX/trading-platform experience — Paula lacks it professionally",
            "LinkedIn itself flags the match as LOW (resume reads FMCG/e-commerce, not crypto/FX)",
            "Role needs deep exchange-affiliate/rebate + trading-abuse-risk fluency she'd have to learn",
            "Stretchier than the Creator Partnerships role; treat as low-effort Easy Apply with realistic odds",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Honest split verdict, stretchier than the Creator Partnerships role. The role's spine is "
            "relationship/affiliate/partner management, and the JD explicitly accepts 'Affiliate Marketing, Key "
            "Account Management (KAM), or B2B partnership management' — Paula's core (42-account portfolio at "
            "Miravia +30% GMV QoQ, XL accounts at Glovo, KOL/creator & community programmes at DoFreeze), with "
            "genuine retention, commission/incentive & co-marketing negotiation, onboarding/due-diligence, "
            "dispute handling, performance/anomaly monitoring and cross-functional collaboration. It also needs "
            "NO Arabic (English required; Spanish is a plus for LATAM/cross-cultural). BUT the PRIMARY industry "
            "requirement is professional Crypto/FX/CFD/Trading-Platform experience plus exchange affiliate/rebate "
            "mechanics and trading-abuse risk (wash trading, arbitrage, multi-accounting) — a specialised domain "
            "Paula does not have professionally (she is a personal crypto user/investor only), and LinkedIn "
            "flags the match as low. Nothing crypto-professional is fabricated; the cover letter names the "
            "domain gap plainly and leans on the transferable KAM/partnership foundation + personal crypto + "
            "Spanish. Worth a low-effort Easy Apply given company fit and strong transferable spine, but with "
            "realistic expectations. Scored Warm (below the Creator role). No 'no sponsorship needed' claim."
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

    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, CONTACT)
    cl_pdf = _to_pdf_soffice(cl_docx)
    print("OK_CL", cl_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
