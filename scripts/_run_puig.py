#!/usr/bin/env python3
"""One-off: full kit (CV + CL + deliverable + outreach) for Puig — Byredo Retail
Manager (2026-06-17). Override pattern; content authored from profile.yaml.

HONEST POSITIONING: this is a physical multi-site RETAIL management role. Paula
has NOT managed store teams / Store Managers. We DO NOT claim she has. We lean on
genuine transferable strengths: fragrance-category expertise (PIC Fragrances),
commercial/P&L, clienteling/CRM (Beauty Club), and the Inditex luxury-retail
foundation — and the cover letter is transparent about the function shift.
"""
from __future__ import annotations

import html
import logging
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from career_ops import llm
from career_ops.analyzer import JobAnalysis
from career_ops.config import settings
from career_ops.discovery.normalize import Job, job_hash
from career_ops.generators import generate_cover_letter, generate_cv, generate_deliverable
from career_ops.generators._paths import job_subdir
from career_ops.generators.outreach import generate_outreach

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)-5s  %(message)s", datefmt="%H:%M:%S")

settings.output_dir = ROOT / "output" / "2026-06-17"
settings.output_dir.mkdir(parents=True, exist_ok=True)


def _html_to_paragraphs(html_str: str) -> list[str]:
    s = re.sub(r"<br\s*/?>", "\n", html_str, flags=re.I)
    out = []
    for p in re.split(r"</p\s*>", s, flags=re.I):
        t = re.sub(r"<[^>]+>", "", p)
        t = html.unescape(re.sub(r"[ \t]+", " ", t)).strip()
        if t:
            out.append(t)
    return out


def build_outreach_pack(job: Job, content) -> Path:
    from docx import Document
    from docx.shared import Pt, RGBColor
    slug = re.sub(r"[^A-Za-z0-9]+", "_", job.company).strip("_")
    out_path = job_subdir(job, "outreach") / f"{slug}_Outreach_Pack.docx"
    doc = Document()
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(11)
    doc.add_heading(f"{job.company} — Outreach Pack", level=0)
    sub = doc.add_paragraph(); r = sub.add_run(f"Outreach copy for an application to {job.title} at {job.company}.")
    r.italic = True; r.font.size = Pt(10); r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    doc.add_heading("Email", level=2)
    s = doc.add_paragraph(); s.add_run("Subject:  ").bold = True; s.add_run(content.email_subject)
    for para in _html_to_paragraphs(content.email_body):
        doc.add_paragraph(para)
    doc.add_heading("LinkedIn connection note (≤300 chars)", level=2)
    doc.add_paragraph(content.linkedin_connection)
    doc.add_heading("LinkedIn InMail", level=2)
    doc.add_paragraph(content.linkedin_inmail)
    doc.save(str(out_path))
    return out_path


CTX = {
    "DoFreeze": "Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries",
    "Miravia": "Top 5 global e-commerce | Alibaba Group | 100K+ employees",
    "Glovo": "Quick-commerce leader | EUR 500M+ revenue | 10K+ employees",
    "Massimo Dutti": "Inditex Group flagship premium fashion brand | Hands-on retail floor",
}

job = Job(
    id=job_hash("Retail Manager - Byredo", "Puig", "Dubai, UAE"),
    title="Retail Manager - Byredo",
    company="Puig",
    location="Dubai, UAE",
    url="https://career2.successfactors.eu/careers?company=Puig",
    source="company_site",
    description=(
        "Retail Manager – Byredo (Puig). Overall management of the retail business with full "
        "accountability for commercial performance and brand value across retail and wholesale doors "
        "in the UAE. Deliver sales, profitability (gross margin, EBITDA), KPI goals. Analyse sales "
        "data and set opportunity-driven strategies. Drive clienteling and CRM to build a segmented "
        "client database for loyalty and long-term value. Collaborate with Marketing on traffic, "
        "conversion and engagement. Lead and develop high-performing store teams and Store Managers; "
        "succession pipeline. Deliver best-in-class luxury client experience with active sales-floor "
        "presence and fragrance profiling. Merchandising and visual standards. Operations (stock, "
        "scheduling, loss prevention, compliance). Requires luxury retail experience and previous "
        "Retail/Area Manager experience leading a team in a multi-site store environment. Puig "
        "welcomes applicants with transferable skills."
    ),
)

analysis = JobAnalysis(
    score=70, tier="Warm",
    skills_match=["luxury beauty & fragrances", "commercial / P&L", "fragrance profiling", "clienteling / CRM", "visual merchandising", "KPI management", "sales generation"],
    missing_skills=["multi-site store-team / Store Manager people management (function shift from brand/e-commerce to physical retail ops)"],
    sector_fit="Luxury Beauty & Fragrances (Puig / Byredo) — exact",
    seniority_fit="Manager-level commercial fit; retail-operations leadership is a transferable stretch",
    red_flags=["role centres on multi-site physical-retail team management, which Paula has not done"],
    ats_keywords=["retail manager", "luxury", "fragrance", "clienteling", "CRM", "P&L", "EBITDA", "KPI", "visual merchandising", "sales", "profitability"],
    reasoning="Dream-sector fit (Puig/Byredo luxury fragrance) with strong commercial, fragrance and clienteling overlap; the retail-ops team-leadership requirement is a transferable stretch, applied transparently per Puig's open invite.",
)

cv = {
    "headline": "Commercial & Brand Manager · Luxury Beauty & Fragrances · Clienteling & P&L",
    "professional_summary": (
        "Commercial and brand professional with 4+ years in beauty, fragrances and luxury-adjacent "
        "retail. Led the fragrance category as PIC Fragrances at Alibaba's Miravia (42 accounts, +30% "
        "GMV QoQ, full P&L on the Flash Sales channel), with deep Arabian & oud expertise (Arabian Oud, "
        "Lattafa, Swiss Arabian, Ajmal), and built the Beauty Club clienteling/CRM programme. "
        "Inditex-trained at Massimo Dutti with hands-on luxury-retail floor and visual "
        "merchandising standards — combining commercial rigour, fragrance expertise and a genuine "
        "luxury-service mindset."
    ),
    "experience": [
        {"company": "DoFreeze LLC", "role": "Brand & Marketing Manager", "dates": "Oct 2025 – Present",
         "location": "Dubai, UAE", "context": CTX["DoFreeze"], "bullets": [
            "Own commercial performance, A&P budget and profitability for a multi-brand portfolio, analysing sales data to set forward-looking, opportunity-driven strategies",
            "Drive retail execution and merchandising across modern trade and quick-commerce, with market and competitor insight feeding commercial plans",
            "Lead fragrance and beauty NPD go-to-market end-to-end, partnering with sales to drive traffic, conversion and growth",
            "Manage distributor and retail-partner relationships across 50+ markets",
        ]},
        {"company": "Miravia (Alibaba Group)", "role": "Key Account Manager & PIC Fragrances – Beauty, Fragrances & Fashion",
         "dates": "Nov 2023 – Oct 2025", "location": "Madrid, Spain", "context": CTX["Miravia"], "bullets": [
            "Owned commercial performance and profitability for 42 beauty & fragrance accounts, growing GMV +30% QoQ through pricing, assortment and targeted promotions to P&L targets",
            "Led the fragrance category as PIC Fragrances — fragrance profiling, assortment and onboarding 30+ doors in two months, including the official distributors of leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
            "Created the Beauty Club and Hot on Social clienteling/CRM projects, building a quality, segmented client base to grow loyalty and long-term client value",
            "Owned the Flash Sales channel for Beauty, Fashion & Home, reporting to the CEO and executing commercial plans aligned to P&L targets",
        ]},
        {"company": "Glovo", "role": "Account Manager – XL Accounts", "dates": "Sep 2022 – Nov 2023",
         "location": "Madrid, Spain", "context": CTX["Glovo"], "bullets": [
            "Managed strategic accounts and led cross-functional teams across marketing, operations and logistics to deliver commercial performance",
            "Negotiated and closed commercial terms, maximising profitability for partners and platform",
        ]},
        {"company": "Massimo Dutti (Inditex)", "role": "Sales Associate – Las Rozas Village", "dates": "Jun 2018 – Jun 2019",
         "location": "Madrid, Spain", "context": CTX["Massimo Dutti"], "bullets": [
            "Inditex luxury-retail foundation: hands-on sales floor, visual merchandising standards and store cadence at a flagship premium outlet",
            "Delivered elevated, personalised customer service and styling — the service DNA that underpins luxury retail and clienteling",
        ]},
    ],
    "skills_brand": "commercial strategy, brand value & positioning, clienteling & CRM, luxury client experience, fragrance profiling, visual merchandising, retail execution, business development",
    "skills_ecommerce": "omnichannel retail, CRM segmentation, e-store & retail merchandising, traffic & conversion, promotions",
    "skills_commercial": "sales generation, P&L & profitability (gross margin, EBITDA), KPI management, key account management, pricing strategy, assortment planning, negotiation, market & competitor analysis",
    "skills_data": "sales analytics, P&L management, KPI tracking, CRM/client segmentation, ROI, Power BI, Tableau, Looker",
    "skills_tools": "Salesforce (CRM), SAP, Power BI, Tableau, Looker, Microsoft Office (Expert), Canva",
}

cl = {
    "opening_paragraph": (
        "Byredo is one of the fragrance houses I most admire, and the chance to grow it in the UAE under "
        "Puig brings together the two threads of my career: a genuine fragrance specialism and a love of "
        "luxury retail. As PIC Fragrances at Alibaba's Miravia and Inditex-trained at Massimo Dutti, I'd be "
        "excited to bring commercial and brand rigour to Byredo's retail business."
    ),
    "body_paragraph_1": (
        "On the commercial side I'd hit the ground running. At Miravia I owned profitability for 42 beauty "
        "and fragrance accounts, growing GMV +30% QoQ and running the Flash Sales channel to P&L targets, "
        "while leading the fragrance category and building the Beauty Club — a segmented clienteling/CRM "
        "programme to grow loyalty and lifetime value. Having managed leading Arabian and oud houses "
        "(Arabian Oud, Lattafa, Swiss Arabian, Ajmal) through their official distributors, I understand the "
        "Gulf fragrance consumer that Byredo's oud lines speak to — fragrance profiling, assortment and "
        "luxury storytelling are second nature to me."
    ),
    "body_paragraph_2": (
        "In full honesty, my background is brand, commercial and key-account leadership rather than "
        "multi-site store management — I have not yet led a network of Store Managers. What I bring instead "
        "is sharp commercial and P&L ownership, deep fragrance and clienteling expertise, and an "
        "Inditex-trained luxury-service foundation, plus the cross-functional team leadership I built at "
        "Glovo. I'm Dubai-based on a UAE residence visa, bilingual in Spanish and English, and motivated to "
        "grow into full retail leadership with Byredo."
    ),
    "closing_paragraph": (
        "Given Puig's openness to candidates with transferable skills, I'd welcome the chance to discuss how "
        "my commercial, fragrance and luxury-service strengths can drive Byredo's retail growth in the UAE. "
        "I'm available to interview at your convenience and can start immediately. Thank you for your consideration."
    ),
}

deliverable = {
    "title": "Byredo UAE — Retail & Clienteling Lens",
    "subtitle": "Three observations on growing a niche luxury fragrance house across UAE doors, from a fragrance-category specialist.",
    "sections": [
        {"heading": "Clienteling as the growth engine, not a nicety",
         "finding": "Niche luxury fragrance lives on a small base of high-value, repeat clients — yet store-level clienteling is often inconsistent across doors.",
         "insight": "A segmented, CRM-led client base compounds: it lifts repeat purchase, average spend and lifetime value far more than footfall alone.",
         "recommendation": "Standardise a clienteling playbook across doors (segmented database, follow-up cadence, fragrance-profiling rituals) — exactly the approach behind the Beauty Club clienteling programme I built at Miravia."},
        {"heading": "Fragrance profiling as the service differentiator",
         "finding": "In niche fragrance, the in-store scent-discovery experience is the brand — but service consistency varies by associate and door.",
         "insight": "Elevating and standardising fragrance profiling turns a browse into an emotional, high-conversion experience that justifies the premium.",
         "recommendation": "Codify a fragrance-profiling service standard and coach teams to it, with flagships as the benchmark — drawing on my fragrance-category expertise as PIC Fragrances — including leading Arabian & oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal) — and Inditex luxury-service training."},
        {"heading": "Retail + wholesale doors as one commercial P&L",
         "finding": "Performance across retail and wholesale doors is easier to manage when read as one commercial picture against margin and EBITDA, not door-by-door in isolation.",
         "insight": "A single opportunity-driven view surfaces where assortment, pricing and activation should shift to protect profitability and growth.",
         "recommendation": "Run a unified KPI scorecard across doors (sell-through, conversion, basket, margin) and re-cut activation by opportunity — the commercial/P&L discipline I applied owning the Flash Sales channel and 42 accounts at Miravia."},
    ],
    "closing": (
        "These are outside-in observations from a fragrance specialist who admires the brand; with Byredo's "
        "door-level data I'd sharpen them quickly. They reflect how I'd approach the role — clienteling-led "
        "growth, elevated fragrance service, and one commercial view across doors."
    ),
}

outreach = {
    "email_subject": "Byredo Retail Manager — fragrance + clienteling",
    "email_body": (
        "<p>Hello,</p>"
        "<p>I'm applying for the Retail Manager – Byredo role. Byredo is one of the fragrance houses I most "
        "admire, and fragrance is my specialism: I led the category as <strong>PIC Fragrances</strong> at "
        "Alibaba's Miravia, onboarding 30+ doors in two months and growing 42 beauty &amp; fragrance accounts "
        "<strong>+30% GMV QoQ</strong> to P&amp;L targets.</p>"
        "<p>I also built the Beauty Club — a segmented clienteling/CRM programme to grow loyalty and lifetime "
        "value — and I'm Inditex-trained at Massimo Dutti, so luxury service and visual merchandising are in my "
        "DNA. I'm candid that my background is commercial and brand rather than multi-site store management, but "
        "I bring the commercial, fragrance and clienteling depth to grow Byredo's doors.</p>"
        "<p>I'm Dubai-based on a residence visa and can start immediately. I'd welcome a short conversation.</p>"
        "<p>Best regards,<br>Paula De Francisco</p>"
    ),
    "linkedin_connection": (
        "Hi — I've applied for your Retail Manager – Byredo role. Fragrance is my specialism (PIC Fragrances at "
        "Miravia, +30% GMV QoQ across 42 beauty/fragrance accounts) plus Beauty Club clienteling and Inditex "
        "luxury-retail training. Dubai-based. I'd love to connect."
    ),
    "linkedin_inmail": (
        "Hi — I've applied for the Retail Manager – Byredo position at Puig. Fragrance is my specialism: I led "
        "the category as PIC Fragrances at Alibaba's Miravia (30+ doors onboarded, 42 accounts at +30% GMV QoQ "
        "to P&L targets), built the Beauty Club clienteling/CRM programme, and trained in luxury retail at "
        "Inditex's Massimo Dutti. I'm Dubai-based on a residence visa and would value a short conversation about "
        "growing Byredo's UAE doors."
    ),
}

with llm.override({"submit_cv_content": cv}):
    cv_path = generate_cv(job, analysis)
with llm.override({"submit_cover_letter": cl}):
    cl_path = generate_cover_letter(job, analysis)
with llm.override({"submit_deliverable": deliverable}):
    dv_path = generate_deliverable(job, analysis, deliverable_type="brand_analysis")
ou_path = None
with llm.override({"submit_outreach": outreach}):
    content = generate_outreach(job, analysis)
if content:
    ou_path = build_outreach_pack(job, content)

print("\n========== PUIG / BYREDO ==========")
print("CV:", cv_path)
print("CL:", cl_path)
print("Deliverable:", dv_path)
print("Outreach:", ou_path)
