"""One-off: generate Paula's CV (+ cover letter) for Z Gallerie's ("ZG")
Middle East Localization & Marketing Manager role — a China-HQ American premium
home brand expanding into the GCC via a Dubai DTC site.

HONESTY FIRST — this is a STRETCH application (user chose to proceed anyway):
  The role's spine is requirements Paula does NOT meet, and we do not fabricate
  them:
    - "Native/fluent Arabic" is a HARD requirement. Paula is Spanish native,
      English C1, NO Arabic. Not claimed. The cover letter discloses this openly.
    - "Deep expertise in Islamic social customs / religious compliance / deliver
      cultural training to China HQ / build the Arabic website." Paula is not a
      GCC-native cultural or religious authority. NOT claimed. Positioned as the
      COMMERCIAL / DTC-localization half of the bridge, leaning on native-Arabic
      partners for Arabic copy and compliance sign-off.
    - Sector home/furniture is a preference she lacks (e-commerce/beauty/fashion/
      FMCG); bridged honestly via premium lifestyle retail (Inditex/Massimo Dutti)
      and 0-to-1 platform launches.

What is GENUINELY strong and what we lead on (all true):
    - DTC / e-commerce LOCALIZATION: Shopify store end-to-end, website audits,
      user journeys, product display, CRO — the JD's "Dubai DTC Website
      Localization" + "website optimization (CRO, user journeys)".
    - GCC market, Dubai-based: quick-commerce (Noon, Talabat, Careem, Deliveroo),
      payments/logistics; adapts campaigns to the region's religious & commercial
      calendar (Ramadan, Eid, DSF, White Friday).
    - THE distinctive asset for THIS role: worked INSIDE a Chinese-owned group
      (Alibaba's Miravia) — real cross-cultural collaboration with China teams.
    - Market intelligence & competitor monitoring + reporting to leadership/HQ;
      membership/CRM & loyalty (Beauty Club); social/influencer/short-form content.
    - 5+ years met by counting from 2021 (Mondelez -> Glovo -> Miravia -> DoFreeze).

  Per standing rule, NO "own visa / no sponsorship" claim. CV states factual
  "UAE Residence Visa" only. No Arabic added to the languages block.

Fills the real CV + cover-letter templates, converts to PDF via LibreOffice
(soffice headless), registers the job for the dashboard, and lands the package
under output/2026-08-21/.
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

COMPANY = "Z Gallerie"
TITLE = "Middle East Localization & Marketing Manager"
DATE_FOLDER = "2026-08-21"

CONTACT = None  # No hiring manager named — letter addressed to "Hiring Manager".

JOB_DESCRIPTION = """\
Middle East Localization & Marketing Manager — Z Gallerie ("ZG"), an American
premium home / furniture brand operating from a China HQ and expanding into the
GCC via a Dubai DTC website. Bridges ZG China HQ with the local Middle East market.

1. Cultural training & internal enablement: deliver systematic training on Middle
   Eastern culture, religion and lifestyle to ZG China HQ teams; build and maintain
   the "ZG Middle East Cultural Knowledge Base" (cultural insights, consumer
   trends, social highlights); provide religious and cultural compliance reviews
   for product selection, visuals and marketing copy (human imagery, colour
   symbolism, pattern motifs, holiday expressions).
2. Dubai DTC website localization: audit the ZG Dubai DTC website from a local-
   consumer perspective and drive localization (user journey, religious
   adaptation, visuals & content, product display); collaborate with ZG China
   teams (UI/UX, Product, Operations) and external web vendors; drive the Arabic-
   language website version and its content review.
3. Middle East marketing strategy support: support brand positioning, target-
   audience profiling and localized value propositions; plan/review campaigns
   across social, YouTube, search, influencer marketing; contribute a Middle East
   membership programme and CRM strategy.
4. Middle East commercial & marketing calendar: build/maintain the "ZG Middle East
   Annual Commercial Calendar" aligned to religious holidays, commercial events and
   mega events; sync with global product-launch cadence; plan ME-specific
   selection, launch and promotion 3-6 months ahead.
5. Market intelligence & localization insights: monitor ME home-retail dynamics and
   competitors (Home Centre, THE One, Marina Home, West Elm ME); produce monthly ME
   market insight reports for China HQ; maintain localized quality and cultural
   relevance of all content.

Qualifications: deep expertise in GCC culture, Islamic social customs and consumer
psychology; NATIVE/FLUENT ARABIC with professional English. 5+ years in regional
marketing, brand management or e-commerce operations (home/furniture, lifestyle,
fashion retail or DTC localization in ME preferred). Proficient in ME digital
marketing and the GCC e-commerce ecosystem (payments, logistics, regulations),
website optimization (CRO, user journeys) and basic data analysis. Exceptional
cross-cultural communication as a "Cultural Translator" bridging local insight with
Chinese team mindsets. Strong upward management / enablement into guidelines and
strategic reports for China HQ.

Preferred: studied/lived in China, cross-cultural collaboration; launched a home/
furniture brand in the GCC 0-to-1; social content creation (TikTok/Reels/YouTube)
and ME short-form ecosystem; offline retail/showroom operations; familiarity with
Z Gallerie or American premium home brands.
"""

ATS = [
    "Middle East", "GCC", "localization", "DTC", "e-commerce operations",
    "regional marketing", "brand management", "brand positioning",
    "target audience profiling", "value proposition", "website localization",
    "website optimization", "CRO", "conversion rate optimization", "user journey",
    "product display", "visuals & content", "Arabic-language website",
    "cross-cultural communication", "China HQ", "Chinese teams",
    "cross-cultural collaboration", "commercial calendar", "marketing calendar",
    "religious holidays", "Ramadan", "Eid", "mega events", "product launch",
    "membership programme", "CRM", "loyalty", "social media", "YouTube",
    "search engines", "influencer marketing", "TikTok", "Reels", "short-form",
    "market intelligence", "competitor monitoring", "consumer trends",
    "monthly insight reports", "data analysis", "payments", "logistics",
    "quick-commerce", "Noon", "Talabat", "Careem", "Deliveroo", "Shopify",
    "premium home", "lifestyle", "fashion retail", "showroom", "0-to-1",
    "Dubai", "UAE", "upward management", "enablement",
]

CV_CONTENT = {
    "headline": (
        "Middle East / GCC E-Commerce & DTC Localization · Regional Brand & Growth Marketing (Dubai-based) · "
        "Marketing Calendar & Market Intelligence · Cross-Cultural Collaboration with China Teams (ex-Alibaba)"
    ),
    "professional_summary": (
        "Dubai-based brand, e-commerce and DTC-localization marketer with five years of experience (since 2021) "
        "across e-commerce, retail, FMCG, beauty and fashion. I localize brands for the GCC market end-to-end: "
        "I run DTC/e-commerce stores on Shopify, audit and improve user journeys and conversion (CRO) from a "
        "local-consumer perspective, and adapt brand communications, visuals and campaigns to local consumers "
        "and the region's key commercial and religious calendar moments (Ramadan, Eid, DSF, White Friday). I "
        "know the GCC e-commerce ecosystem first-hand — quick-commerce (Noon, Talabat, Careem, Deliveroo), "
        "payments and logistics — and I produce market-intelligence and competitor reporting for leadership. "
        "Distinctively for this role, I've worked inside a Chinese-owned global group (Alibaba's Miravia), so "
        "cross-cultural collaboration with China teams is familiar terrain, and I coordinate Arabic-language "
        "content and creators through native partners in-market. Trained in premium lifestyle retail at Inditex "
        "(Massimo Dutti). Spanish native, English C1; Business Administration graduate (CUNEF)."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Multi-market group | Brands: Befit, Eurocake, Flair | GCC + 50+ countries",
            "bullets": [
                "Run DTC/e-commerce on Shopify end-to-end — auditing and improving the user journey, product display and conversion (CRO) from a local-consumer perspective, lifting conversion and average order value",
                "Localize brand and marketing for the GCC market — adapting brand communications, visuals and campaigns to local consumers and the region's key commercial and religious calendar moments (Ramadan, Eid, DSF, White Friday)",
                "Operate across the GCC e-commerce ecosystem — quick-commerce (Noon, Talabat, Careem, Deliveroo), payments and logistics — managing listings, promo mechanics and retail execution",
                "Build and maintain the marketing/commercial calendar across markets, aligning launches and promotions to regional key dates and synchronising with global product cadence 3–6 months ahead",
                "Plan and review multi-channel campaigns (social, YouTube, search, influencer/UGC) and coordinate Arabic-language content and creators through native partners in-market",
                "Produce market-intelligence and competitor monitoring, present plans and performance to leadership, and coordinate external agencies, vendors and web/dev partners",
                "Built an AI-powered automation system (Claude / generative AI) that scales localized content, market research and reporting, cutting manual workload ~40%",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Chinese-owned global group (Alibaba) | Top-5 e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Worked inside a Chinese-owned global group (Alibaba's Miravia) — day-to-day cross-cultural collaboration with China-based product, operations and commercial teams",
                "Managed 42 beauty, fragrance and fashion accounts (+30% GMV QoQ) — assortment, pricing and localized promotions on a top-5 marketplace",
                "Created and led the 'Beauty Club' loyalty programme and 'Hot on Social' content programme — membership/CRM and social engagement tailored to consumer loyalty dynamics",
                "Analysed conversion, traffic, retention, ROI and ROAS, and tracked category trends and competitors to steer assortment and campaigns",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce super-app | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped build Glovo's Retail vertical — taking new fashion and lifestyle brands to market on the platform (0-to-1 launches)",
                "Drove GMV growth for strategic accounts through data-led campaigns and localized activations",
                "Ran complex cross-functional campaigns from concept to execution across marketing, operations and logistics",
                "Negotiated and closed commercial deals, coordinating external partners and vendors",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Produced category, competitor and consumer-trend analysis and monthly performance reports for the chocolate category",
                "Supported NPD launches (Milka Spread, Mini Suchard) aligned to the commercial calendar",
                "Distilled market data into actionable insight and recommendations for leadership",
            ],
        },
    ],
    "skills_brand": (
        "regional / GCC brand & growth marketing, DTC localization, brand positioning & value-proposition "
        "adaptation, marketing & commercial calendar (religious + commercial key dates), multi-channel "
        "campaigns (social, YouTube, search, influencer), membership / CRM & loyalty, content strategy"
    ),
    "skills_ecommerce": (
        "DTC / e-commerce localization, Shopify, conversion rate optimisation (CRO), user-journey & website "
        "audits, product display, GCC e-commerce ecosystem (payments, logistics), quick-commerce (Noon, "
        "Talabat, Careem, Deliveroo), social & short-form content (TikTok / Reels / YouTube), AI content localization"
    ),
    "skills_commercial": (
        "cross-cultural collaboration with China teams (ex-Alibaba), 0-to-1 brand launches, agency / vendor / "
        "web-developer coordination, upward reporting to HQ & leadership, project management, key account management"
    ),
    "skills_data": (
        "market intelligence & competitor monitoring, monthly insight reports, consumer-trend analysis, "
        "conversion & customer-behaviour analysis, KPI reporting, ROI / ROAS, Power BI, forecasting"
    ),
    "skills_tools": (
        "Generative AI (Claude, ChatGPT), Shopify, Meta Ads Manager, Google Ads, Salesforce (CRM), Power BI, "
        "Canva, Microsoft Office (Expert)"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Z Gallerie entering the GCC through a Dubai DTC site needs someone who can turn a China-built premium "
        "home brand into a store and a calendar that feel native to the local shopper — and who can work fluidly "
        "with your China HQ to get there. I'm a Dubai-based brand and e-commerce marketer who localizes brands "
        "for the GCC market every day: I run DTC stores end-to-end, optimise the user journey and conversion, "
        "and build region-specific calendars around the moments that actually move sales here. I'll be candid "
        "up front about where I fit and where I'd lean on others — because I'd rather be a real fit than a "
        "keyword match."
    ),
    "body_paragraph_1": (
        "On the commercial and localization half of this role I'm strong. At DoFreeze I run Shopify DTC "
        "end-to-end — auditing user journeys, product display and conversion (CRO) from a local-consumer lens — "
        "and adapt brand communications, visuals and campaigns to GCC consumers and the region's religious and "
        "commercial calendar (Ramadan, Eid, DSF, White Friday), synchronising launches with a global product "
        "cadence 3–6 months ahead. I know the GCC e-commerce ecosystem first-hand (quick-commerce, payments, "
        "logistics), plan multi-channel campaigns across social, YouTube, search and influencer, and I built a "
        "membership/loyalty programme ('Beauty Club') and social content engine ('Hot on Social') at Alibaba's "
        "Miravia. I also produce competitor and market-intelligence reporting for leadership — exactly the "
        "monthly ME insight reports this role owes China HQ."
    ),
    "body_paragraph_2": (
        "Two honest notes so you can calibrate the fit. First, I am not a native Arabic speaker — I'm Spanish "
        "(native) with English at C1 — so for Arabic-language copy, religious-compliance sign-off and the "
        "deepest cultural-training work I'd partner with native-Arabic colleagues, creators and agencies, as I "
        "already coordinate Arabic-facing content in-market; where I add the most is the commercial, DTC-"
        "localization and China-collaboration side. And that China side is a genuine edge: I've worked inside "
        "Alibaba's organisation (Miravia), so bridging with your China HQ teams — UI/UX, Product, Operations — "
        "is familiar terrain. Second, my sector is e-commerce, beauty and fashion rather than home/furniture, "
        "but I trained in premium lifestyle retail at Inditex (Massimo Dutti) and have launched new brands "
        "0-to-1 on-platform, so premium-lifestyle merchandising and retail localization are comfortable ground."
    ),
    "closing_paragraph": (
        "If you're looking for the commercial, DTC-localization and China-bridge engine of your GCC launch — "
        "paired with native-Arabic cultural expertise on the team — I'd bring hands-on GCC e-commerce, "
        "market-calendar and localization experience and an AI-powered way of scaling content and insight. I'm "
        "based in Dubai and happy to share e-commerce and localization case studies. Thank you for your "
        "consideration — I look forward to hearing from you."
    ),
}


def make_job() -> Job:
    return Job(
        id="zgallerie-middle-east-localization-manager-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE",
        url="",
        source="job board",
        description=JOB_DESCRIPTION,
        raw={"query": "Middle East Localization Marketing Manager",
             "function": "ME localization / DTC e-commerce / cross-cultural (China HQ <-> GCC)",
             "sector": "Premium home / furniture (American brand, China HQ)",
             "note": "STRETCH application (user opted in). HARD requirement Paula MISSES: native/fluent Arabic "
                     "+ GCC cultural/religious authority + delivering cultural training to China HQ. NOT "
                     "fabricated — disclosed openly in the cover letter. Positioned honestly on her real "
                     "strengths: DTC/e-commerce localization + CRO, GCC market execution, and the distinctive "
                     "China-org collaboration (Alibaba/Miravia). No Arabic added to languages. No 'own visa / "
                     "no sponsorship' claim."},
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
        "ai_score": 48,
        "ai_tier": "Cool",
        "skills_match": [
            "DTC / e-commerce LOCALIZATION — Shopify end-to-end, website/user-journey audits, product display, CRO (JD's core 'Dubai DTC website localization' + 'website optimization')",
            "GCC market, Dubai-based — quick-commerce (Noon/Talabat/Careem/Deliveroo), payments/logistics; adapts campaigns to Ramadan/Eid/DSF/White Friday",
            "DISTINCTIVE for this role: worked INSIDE a Chinese-owned group (Alibaba/Miravia) — real cross-cultural collaboration with China teams",
            "Marketing/commercial calendar aligned to key regional dates, synced to global launch cadence 3-6 months ahead",
            "Market intelligence & competitor monitoring + reporting to leadership/HQ (maps to monthly ME insight reports)",
            "Membership/CRM & loyalty ('Beauty Club'); multi-channel campaigns (social, YouTube, search, influencer); short-form/UGC",
            "Premium lifestyle retail training (Inditex/Massimo Dutti) + 0-to-1 platform launches (Glovo Retail vertical) — home/lifestyle adjacency",
            "5+ years met counting from 2021 (Mondelez -> Glovo -> Miravia -> DoFreeze); English C1; based in Dubai",
        ],
        "missing_skills": [
            "NATIVE/FLUENT ARABIC — HARD requirement Paula does NOT meet (Spanish native, English C1, no Arabic). Disclosed openly in the cover letter; NOT fabricated; no Arabic added to CV languages",
            "Deep GCC cultural / Islamic-customs / religious-compliance AUTHORITY + delivering cultural training to China HQ + building the Arabic website — she is not a region-native cultural/religious authority. Positioned as the commercial/DTC-localization half of the bridge, leaning on native-Arabic partners",
            "Home/furniture sector (preference) — she is e-commerce/beauty/fashion/FMCG; bridged honestly via premium lifestyle retail + 0-to-1 launches",
        ],
        "sector_fit": "weak (home/furniture is new; e-commerce/DTC + premium lifestyle retail are the honest adjacencies)",
        "seniority_fit": "on-band on years, but the role's core identity (Arabic-native 'Cultural Translator') is a fundamental mismatch",
        "red_flags": [
            "LIKELY REJECT on merit: the role's spine is native/fluent Arabic + GCC cultural/religious authority + training China HQ on Middle Eastern culture/religion — none of which Paula has. Generated as a STRETCH at the user's explicit request, positioned honestly on her real DTC-localization + China-collaboration strengths; nothing fabricated.",
            "Arabic gap is disclosed candidly in the cover letter rather than hidden — a deliberate honesty choice to protect credibility.",
            "No 'own visa / no sponsorship' claim (employer-sponsored visa); CV states factual 'UAE Residence Visa' only.",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Honest STRETCH (user opted in after being warned). The role is a China-HQ premium home brand (Z "
            "Gallerie) hiring an Arabic-native 'Cultural Translator' to train China HQ on Middle Eastern culture/"
            "religion, run religious-compliance reviews, build the Arabic DTC website, and own ME localization. "
            "Its #1 qualification — native/fluent Arabic + deep Islamic/GCC cultural authority — is a fundamental "
            "gap for Paula (Spanish native, English C1, not a region-native cultural/religious authority), so on "
            "merit this is a likely reject. We do NOT fabricate any of it: the cover letter discloses the Arabic "
            "gap openly and positions her on the genuine half she can own — DTC/e-commerce localization, CRO/"
            "user-journey work, GCC market execution and calendar, market-intelligence reporting — plus the one "
            "distinctive asset that actually fits this role: real cross-cultural collaboration inside a Chinese-"
            "owned group (Alibaba's Miravia). Sector (home/furniture) bridged via premium lifestyle retail "
            "(Inditex) and 0-to-1 platform launches. 5+ years met from 2021. No Arabic added to languages; no "
            "'own visa / no sponsorship' claim."
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
