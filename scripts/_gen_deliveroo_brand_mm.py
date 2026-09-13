"""One-off: generate Paula's application package for the Deliveroo
"Marketing Manager, Brand, Middle East" (Dubai) role.

Strong-fit application. The JD is a brand / integrated-campaign / project-
management role inside Deliveroo's Middle East Brand & Experience team,
covering UAE + Kuwait. Paula's current work (Brand & Marketing Manager at
DoFreeze) is squarely this: owning campaigns end-to-end from brief to
delivery, briefing creative/agencies, running paid + influencer + social,
managing A&P budgets and reporting on KPIs — across 50+ GCC/MENA markets.
The killer hook: Deliveroo is one of the very quick-commerce platforms she
already merchandises brands onto, so she knows the platform from the inside.

Content is authored directly (no LLM API key in this repo) and kept strictly
truthful — NO invented experience. The one genuine gap (JD asks 6–8 yrs, Paula
has 4+) is addressed head-on in the cover letter rather than papered over.

Fills the real CV + cover-letter templates, converts to PDF, and lands the
package under output/2026-08-12/Deliveroo - Marketing Manager, Brand, Middle East/.
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cover_letter as cl
from career_ops.generators import cv_generator as cv

COMPANY = "Deliveroo"
TITLE = "Marketing Manager, Brand, Middle East"
DATE_FOLDER = "2026-08-18"

JOB_DESCRIPTION = """\
Marketing Manager, Brand, Middle East — Deliveroo, Dubai, UAE.

Deliveroo's Brand & Experience team builds the emotional connection between
Deliveroo and its customers, riders and partners, bringing the brand to life
across every touchpoint. We are looking for an experienced Marketing Manager for
the Middle East Marketing team, based in the UAE, covering marketing projects and
campaign management across the Middle East with a focus on the UAE and Kuwait.
Reporting into the Marketing team lead, you will coordinate and execute integrated
marketing campaigns and projects that connect emotionally with customers and
strengthen Deliveroo's position as a loved, trusted brand. You own projects
end-to-end, set the pace, align contributors and make sure delivery happens across
a full breadth of marketing initiatives — balancing creative sensibility, strong
project management and a data-driven mindset.

What you'll be doing: Own end-to-end delivery of marketing projects and campaigns
as the project lead — timelines, contributors, accountability — landing on time, on
budget and to the highest creative standard. Work cross-functionally with media,
CRM, social, PR/comms and central vertical and marketing teams to plan and execute
local brand campaigns across the UAE and Middle East, ensuring consistent activation
across all channels (ATL, OOH, digital, social, in-app). Write clear, insight-led
creative briefs and manage the feedback and approval process with internal creative
teams and external agencies. Track campaign KPIs, compile post-campaign reports and
translate learnings into recommendations. Own and track campaign budgets and delivery
timelines, flagging risks proactively. Stay informed on market trends, competitor
campaigns and cultural moments to inform creative strategy. Act as the connective
tissue across workstreams, building strong relationships with local and central teams,
agencies and partners.

What you'll need: 6–8 years of experience in brand marketing, campaign and project
management or a related discipline, ideally in tech. Proven experience managing
integrated brand campaigns end-to-end across multiple channels and markets. A strong
eye for creative quality with the ability to give clear feedback to agencies and
internal teams. Excellent project management skills — highly organised, detail-oriented,
managing multiple workstreams simultaneously. Analytically minded, comfortable pulling
and interpreting campaign performance data. Strong interpersonal and communication
skills across cross-functional teams and senior stakeholders. A self-starter who takes
ownership and moves quickly in a fast-paced, matrixed environment. Familiarity with the
UAE and Kuwait markets, including local consumer behaviour and cultural moments
(Ramadan, Eid, National Days) and the competitive landscape.
"""

ATS = [
    "brand marketing", "integrated brand campaigns", "campaign management",
    "project management", "end-to-end delivery", "creative brief", "briefing",
    "agency management", "stakeholder management", "cross-functional", "ATL",
    "OOH", "digital", "social", "in-app", "CRM", "PR", "comms", "media",
    "go-to-market", "budget management", "A&P", "campaign KPIs",
    "post-campaign report", "performance data", "market intelligence",
    "competitor campaigns", "cultural moments", "Ramadan", "Eid", "UAE",
    "Kuwait", "Middle East", "MENA", "brand building", "self-starter", "tech",
    "quick-commerce", "Deliveroo",
]

CONTENT = {
    "headline": "Brand & Marketing Manager · Integrated Campaigns End-to-End · Quick-Commerce & Delivery · UAE / MENA",
    "professional_summary": (
        "Brand and marketing manager who owns integrated campaigns end-to-end — from insight-led brief to "
        "on-time, on-budget delivery — across paid, social, influencer, CRM/EDM and in-store, and across 50+ "
        "GCC/MENA markets including the UAE and Kuwait. Currently lead Brand & Marketing at DoFreeze in Dubai: "
        "campaign and project management, creative briefing and agency/creator direction, A&P budget ownership "
        "and KPI reporting. Deep hands-on with UAE quick-commerce and delivery — Deliveroo, talabat, Noon and "
        "Careem — so I know the platform, the shopper and the local cultural calendar (Ramadan, Eid, National "
        "Days) from the inside. Data-driven, AI-native, and already in Dubai on a residence visa."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
            "bullets": [
                "Own integrated brand campaigns end-to-end across the UAE and 50+ GCC/MENA markets — from insight-led brief through creative, activation and delivery — as project lead setting timelines, aligning contributors and driving accountability so work lands on time, on budget and on brand across every channel (paid, social, influencer, CRM/EDM, in-store)",
                "Write clear creative briefs and run the feedback-and-approval process with creative teams, agencies and 25–50 influencers per campaign — championing the work while holding it to brand guidelines and the highest creative standard",
                "Own campaign A&P budgets and delivery timelines, flag risks early, and track KPIs into post-campaign reporting (ROI, ROAS, sell-out) that sharpens the next brief — with an AI (Claude/GPT) system automating that reporting and cutting manual workload ~40%",
                "Run the UAE quick-commerce and delivery shelf across Deliveroo, talabat, Noon and Careem — assortment, content and promotional mechanics — timing activations to local cultural moments (Ramadan, Eid, National Days)",
                "Act as the connective tissue across commercial, brand, trade, creative and central/local teams, keeping every contributor clear on priorities and timelines to move campaigns forward",
            ],
        },
        {
            "company": "Miravia / AliExpress (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Top 5 global e-commerce | 100K+ employees",
            "bullets": [
                "Created and led integrated brand campaigns — Beauty Club and Hot on Social — from concept to activation, working cross-functionally with social, content and commercial teams to build brand love and loyalty on platform",
                "Grew 42 key accounts +30% GMV QoQ through campaign-led promotions, assortment and pricing — reporting the Flash Sales channel directly to the CEO",
                "Pulled and interpreted campaign performance data (conversion, traffic, retention, ROI) to shape creative and commercial decisions and improve forecasting",
                "Coordinated multiple workstreams at once — 30+ store onboardings in two months as PIC Fragrances — without dropping the ball",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Delivered bespoke marketing activations for strategic partners on a quick-commerce delivery platform — the same brand-meets-delivery world Deliveroo operates in — driving order volume and GMV through data-led planning",
                "Led cross-functional teams across marketing, logistics and CX to deliver seamless campaigns end-to-end",
                "Helped build Glovo's Retail vertical from the ground up — a fast-paced, matrixed environment that rewarded ownership and pace",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category & Brand Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B annual revenue | 90K+ employees",
            "bullets": [
                "Built performance reports and promotional-effectiveness analysis for the chocolate category — early grounding in the measure-and-learn mindset this role needs",
                "Contributed to brand NPD launches (Milka Spread, Mini Suchard) from concept to shelf",
            ],
        },
    ],
    "skills_brand": "integrated brand campaigns end-to-end, campaign & project management, creative briefing & agency direction, brand strategy & building, go-to-market, NPD end-to-end, influencer & UGC, cultural-moment activations (Ramadan / Eid / National Days), shopper & trade marketing, omnichannel (ATL, OOH, digital, social, in-app)",
    "skills_ecommerce": "quick-commerce & delivery (Deliveroo, talabat, Noon, Careem), Meta Ads (Facebook & Instagram), Google Ads, CRM & EDM, social & content, Shopify e-store, marketing automation, generative-AI content",
    "skills_commercial": "cross-functional & senior-stakeholder management, key account management, negotiation, pricing strategy, category management, modern trade & distributor management",
    "skills_data": "campaign KPI tracking & post-campaign reporting, ROI / ROAS, A&P budget & timeline management, performance & sell-out analysis, AI-assisted analysis & forecasting, Looker, Power BI, Nielsen, Kantar, Salesforce",
    "skills_tools": "Meta Ads Manager, Google Ads, Generative AI (Claude / ChatGPT), Shopify, Salesforce, Power BI, Tableau, Looker, Canva, Microsoft Office (Expert)",
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "Deliveroo's brand is one I already work with every week — from the other side of the marketplace, "
        "merchandising and activating FMCG brands on your quick-commerce shelf in the UAE. So the Marketing "
        "Manager, Brand role in the Middle East team is the exact intersection I've been building toward: the "
        "craft of building a loved, trusted brand, on a delivery platform I know from the inside, in the UAE and "
        "Kuwait markets I live and work in."
    ),
    "body_paragraph_1": (
        "What this role asks for is what I do now. As Brand & Marketing Manager at DoFreeze I own integrated "
        "campaigns end-to-end across the UAE and 50+ GCC/MENA markets — from insight-led brief to on-time, "
        "on-budget delivery — as the project lead who sets timelines, aligns contributors and holds accountability. "
        "I write the creative briefs and run feedback and approvals with agencies, creative teams and 25–50 "
        "influencers per campaign; I own the A&P budget; and I track KPIs into post-campaign reporting (ROI, ROAS, "
        "sell-out) that shapes the next brief. Before this, at Alibaba's Miravia I built integrated brand campaigns "
        "like Beauty Club and Hot on Social from scratch and grew 42 accounts +30% GMV QoQ, reporting to the CEO — "
        "and at Glovo I ran bespoke activations on a delivery platform much like Deliveroo's."
    ),
    "body_paragraph_2": (
        "Two things make me a strong fit beyond the checklist. First, I'm genuinely native to this world — Deliveroo, "
        "talabat, Noon and Careem on the delivery side, and the UAE/Kuwait cultural calendar (Ramadan, Eid, National "
        "Days) that shapes when and how campaigns land — plus I'm AI-native, building generative-AI tooling that makes "
        "briefing, research and reporting faster. Second, I'm already in Dubai on a residence visa, so I can start with "
        "zero relocation. I'll be candid about one thing: I have 4+ years of experience rather than the 6–8 in the "
        "posting — but those years are unusually broad and delivery-dense, spanning exactly the brand-meets-quick-"
        "commerce space this role lives in, and I'd back my campaign portfolio against that gap any day."
    ),
    "closing_paragraph": (
        "I'd love to show the Middle East Marketing team how I'd approach an integrated campaign for the UAE and "
        "Kuwait — from brief to the post-campaign read. I'm based in Dubai and available immediately. Thank you for "
        "considering my application."
    ),
}


def make_job() -> Job:
    return Job(
        id="deliveroo-brand-mm-me-2026-08",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://careers.deliveroo.co.uk/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={"query": "Marketing Manager Brand Middle East", "via": "LinkedIn / Deliveroo Careers"},
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
            "Integrated brand campaigns end-to-end (DoFreeze)",
            "Campaign & project management, timelines & accountability",
            "Creative briefing & agency/creator direction",
            "A&P budget ownership + KPI / post-campaign reporting",
            "Cross-functional & senior-stakeholder management (Miravia → CEO)",
            "Quick-commerce & delivery native (Deliveroo, talabat, Noon, Careem)",
            "UAE + GCC/MENA markets & cultural moments (Ramadan, Eid)",
            "AI-native builder; already in Dubai (residence visa)",
        ],
        "missing_skills": [
            "6–8 yrs tenure (Paula has 4+)",
            "Deep Kuwait-specific market depth",
        ],
        "sector_fit": "strong (brand marketing · quick-commerce/delivery · tech)",
        "seniority_fit": "good (slight tenure gap vs 6–8 yrs ask)",
        "red_flags": ["Tenure below the 6–8 yr band — addressed head-on in the cover letter"],
        "ats_keywords": ATS,
        "reasoning": (
            "Strong fit. Deliveroo 'Marketing Manager, Brand, Middle East' is a brand / integrated-campaign / "
            "project-management role covering UAE + Kuwait — the substance of Paula's current DoFreeze remit "
            "(campaigns end-to-end from brief to delivery, creative briefing, agency/creator direction, A&P "
            "budgets, KPI/post-campaign reporting) across 50+ GCC/MENA markets. Standout hook: Deliveroo is one "
            "of the quick-commerce/delivery platforms she already merchandises brands onto, so she knows the "
            "platform and the local cultural calendar from the inside. Only real gap is tenure (JD asks 6–8 yrs, "
            "Paula has 4+), handled honestly in the cover letter."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


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
    cv_pdf = cv._to_pdf(cv_docx)
    print("OK_CV", cv_pdf)

    # --- Cover letter ---
    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, contact_name=None)
    cl_pdf = cl._to_pdf(cl_docx)
    print("OK_CL", cl_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
