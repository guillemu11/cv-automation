#!/usr/bin/env python3
"""Generate Paula's tailored CV + Cover Letter (HTML -> PDF) for a batch of jobs.

Same red-accent house style as the Colgate package
(scripts/_gen_colgate_cv_cl_html.py), rendered via Playwright/Chromium because
weasyprint lacks native libs on this Windows box.

Each job gets its own tailored headline, professional summary and cover letter,
sharing one strong experience/skills core. The skills table now always includes
an "AI & Automation" row (per the cv-ai-automation-tools preference).

Outputs to: output/<DAY>/<Company> - <Role>/01_CV_y_Carta/
"""
from __future__ import annotations

from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
DAY = "2026-07-08"

RED = "#C8102E"       # neutral professional red accent
INK = "#1a1a1a"
MUTE = "#5a6473"

# --------------------------------------------------------------------------
# Shared identity
# --------------------------------------------------------------------------
NAME = "Paula De Francisco Pérez"
CONTACT = ("Dubai, UAE | +971 50 386 3656 | paulich98@hotmail.com | "
           "linkedin.com/in/paula-de-francisco-perez")
STATUS = ("Nationality: Spanish · UAE Residence Visa — based in Dubai, "
          "no relocation, available immediately")

EXPERIENCE = [
    {
        "role": "Brand &amp; Marketing Manager",
        "dates": "Oct 2025 – Present",
        "context": "DoFreeze LLC · Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries · Dubai, UAE",
        "bullets": [
            "Lead brand &amp; marketing across 50+ markets (GCC, MENA, Asia, Europe, USA, Africa) — brand strategy, 360 campaigns, go-to-market and A&amp;P budget to net-sales and P&amp;L targets",
            "Own digital-shelf execution across UAE e-commerce &amp; quick-commerce (Noon, Talabat, Careem, Deliveroo) — listings, rich content, pricing and promotions that lift click &amp; conversion",
            "Manage the Shopify e-store end-to-end (catalogue, UX, collections, checkout), lifting conversion rate (CRO) and average order value through data-led merchandising",
            "Led 6 NPD launches end-to-end (brief, packaging, pricing, go-to-market) and built the influencer programme from zero — 25–50 creators per campaign, sampling &amp; seeding driving UGC and sell-out",
            "Plan and optimise full-funnel media (Meta Ads, Google Ads, social, EDM) on a weekly KPI scorecard tracking traffic, spend, ROI and ROAS",
            "Built AI-powered automation (Claude / Claude Code) for content, campaign planning and KPI reporting, cutting manual workload ~40%",
        ],
    },
    {
        "role": "Key Account Manager (E-Commerce) – Beauty, Fragrances &amp; Fashion",
        "dates": "Nov 2023 – Oct 2025",
        "context": "Miravia (Alibaba Group) · Top 5 global e-commerce | 100K+ employees · Madrid, Spain",
        "bullets": [
            "Grew 42 key accounts +30% GMV QoQ on a top-5 global e-commerce platform through pricing, assortment and conversion-led promotions",
            "Owned the digital shelf for Beauty, Fashion &amp; Home and ran the Flash Sales channel to P&amp;L targets, reporting directly to the CEO",
            "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months — including Arabian Oud, Lattafa, Swiss Arabian and Ajmal",
            "Analysed conversion, traffic, retention, ROI and ROAS to optimise channel performance and forecasting",
        ],
    },
    {
        "role": "Account Manager – XL Accounts",
        "dates": "Sep 2022 – Nov 2023",
        "context": "Glovo · Quick-commerce leader | EUR 500M+ revenue | 10K+ employees · Madrid, Spain",
        "bullets": [
            "Helped build Glovo's retail vertical — onboarding fashion, beauty and lifestyle brands beyond food delivery",
            "Managed strategic XL accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop), driving GMV growth through data-led planning and full-funnel activations",
            "Led cross-functional teams across marketing, operations and logistics to grow order volume",
        ],
    },
    {
        "role": "Trainee – Category Planning",
        "dates": "Aug 2021 – Aug 2022",
        "context": "Mondelez International · Global FMCG | EUR 36B annual revenue | 90K+ employees · Madrid, Spain",
        "bullets": [
            "Conducted sell-in/sell-out analysis and evaluated promotional effectiveness for the chocolate category",
            "Built category performance reports informing assortment and trade decisions in a multinational FMCG",
            "Contributed to NPD launches including Milka Spread and Mini Suchard",
        ],
    },
]

SKILLS = [
    ("Brand &amp; Marketing", "brand strategy, 360 marketing communications, go-to-market, NPD / innovation launches, promotion strategy, influencer marketing, shopper &amp; trade marketing, content that converts"),
    ("E-Commerce &amp; Digital", "e-store management, Shopify, conversion rate optimisation (CRO), digital shelf, full-funnel, digital merchandising, online marketplaces, quick-commerce (Noon, Talabat, Careem, Deliveroo), Meta Ads, Google Ads, EDM"),
    ("AI &amp; Automation", "Claude / Claude Code (AI agents for marketing, analytics &amp; content automation), generative-AI campaigns (copywriting, creatives, content calendars), AI video (Higgsfield, Hailuo AI / MiniMax), AI–business integrations via MCP (Shopify, Meta Ads, Notion, Gmail, Canva), AEO / GEO (schema, Wikidata, llms.txt), Python reporting automation"),
    ("Commercial", "key account management, category growth, assortment planning, pricing strategy, distributor management, modern trade, negotiation, forecasting"),
    ("Data &amp; Analytics", "digital-shelf scorecards, P&amp;L management, Net Sales, ROI, ROAS, GMV, traffic &amp; channel analytics, KPI tracking, Power BI, Looker, Tableau, Nielsen, Kantar"),
    ("Tools", "Shopify, Meta Ads Manager, Google Ads, Salesforce, SAP, Canva, Notion, Generative AI (Claude / Claude Code, ChatGPT), Higgsfield, Hailuo AI, Microsoft Office (Expert)"),
]

# --------------------------------------------------------------------------
# Per-job tailoring
# --------------------------------------------------------------------------
JOBS = [
    {
        "company": "Deliveroo",
        "role": "Marketing Manager Brand",
        "cv_key": "Deliveroo_Marketing_Manager_Brand",
        "headline": "Brand &amp; Marketing Manager · 360 Campaigns · Quick-Commerce · FMCG",
        "summary": (
            "Brand and marketing leader with 4+ years building brands across FMCG, beauty and "
            "quick-commerce. Currently leads brand &amp; marketing for DoFreeze across 50+ markets — "
            "brand strategy, 360 campaigns, NPD and go-to-market — with hands-on execution across the "
            "UAE quick-commerce platforms I know first-hand, Deliveroo included (Noon, Talabat, Careem). "
            "Scaled an influencer programme from zero to 25–50 creators per campaign and grew 42 key "
            "accounts +30% GMV QoQ at Alibaba's Miravia. AI-first marketer building generative-AI (Claude) "
            "automation for content and campaign planning. A direct fit for a consumer brand marketing "
            "mandate in this market."
        ),
        "cl_to": "Deliveroo — Talent Acquisition",
        "cl_re": "Re: Marketing Manager, Brand — Dubai",
        "cl_paras": [
            "I am applying for the Marketing Manager, Brand role in Dubai, and few briefs have felt more like a natural fit. I work with Deliveroo every week from the brand side — integrating products, promotions and content across UAE quick-commerce — so I understand both the platform and the consumer behaviour behind it. The chance to build the Deliveroo brand itself, turning a beloved service into consistently great campaigns, is exactly the challenge I want.",
            "As Brand &amp; Marketing Manager at DoFreeze (Befit, Eurocake, Flair), I lead brand strategy, 360 campaigns and go-to-market across 50+ markets, own full-funnel media (Meta, Google, social, EDM) to ROI/ROAS targets, and scaled an influencer programme from zero to 25–50 creators per campaign driving real UGC and sell-out. Earlier, at Alibaba's Miravia, I grew 42 key accounts to +30% GMV QoQ and ran the Flash Sales channel to P&amp;L targets, reporting to the CEO.",
            "What sets me apart for this market: first-hand experience across Deliveroo, Noon, Talabat and Careem, FMCG foundations from Mondelez, and an AI-first way of working — I build generative-AI (Claude / Claude Code) automation for content, campaign planning and reporting that cut my manual workload ~40%. I am already in Dubai on a residence visa (zero relocation) and work fluently in English and Spanish.",
            "I would welcome the chance to discuss how I can help grow the Deliveroo brand across the UAE. Thank you for your consideration.",
        ],
    },
    {
        "company": "Philips",
        "role": "Key Account Manager Personal Health E-Commerce",
        "cv_key": "Philips_Key_Account_Manager_Ecommerce",
        "headline": "Key Account Manager · E-Commerce · Digital Shelf · Key Accounts",
        "summary": (
            "Key Account and e-commerce professional with 4+ years growing accounts and digital shelf "
            "across FMCG, beauty and marketplaces. Grew 42 key accounts +30% GMV QoQ at Alibaba's Miravia "
            "through pricing, assortment and conversion-led promotions, and currently owns digital-shelf "
            "execution across UAE e-retailers (Noon, Talabat, Careem, Deliveroo) at DoFreeze. Runs weekly "
            "scorecards on conversion, ROI and ROAS, and builds generative-AI (Claude) automation for "
            "reporting and planning. FMCG category-planning foundations from Mondelez — a strong fit for "
            "an e-commerce key-account mandate in Personal Health."
        ),
        "cl_to": "Philips — Talent Acquisition",
        "cl_re": "Re: Key Account Manager (Personal Health) – E-Commerce, Dubai",
        "cl_paras": [
            "I am applying for the Key Account Manager (Personal Health) – E-Commerce role in Dubai. The combination in this brief — owning e-retailer relationships while driving digital-shelf and conversion performance — is precisely the work I do today and did at scale at Alibaba's Miravia, and Philips' quality-led Personal Health portfolio is a category I would be proud to grow online.",
            "At Miravia (Alibaba Group) I managed 42 key accounts to +30% GMV QoQ, owning pricing, assortment and promotion strategy and running the Flash Sales channel to P&amp;L targets, reporting directly to the CEO. Now, as Brand &amp; Marketing Manager at DoFreeze, I own digital-shelf execution across the UAE's key e-commerce and quick-commerce retailers — Noon, Talabat, Careem and Deliveroo — plus the Shopify e-store, using weekly scorecards on conversion, ROI and ROAS to drive corrective action and net-sales delivery.",
            "What I add for this mandate: hands-on UAE e-retailer and quick-commerce experience, FMCG category-planning foundations from Mondelez, and an AI-first approach — I build generative-AI (Claude / Claude Code) automation for content, campaign planning and KPI reporting that cut manual workload ~40%. I am already based in Dubai on a residence visa (no relocation) and work fluently in English and Spanish.",
            "I would welcome the opportunity to discuss how I can accelerate Philips' e-commerce growth in Personal Health across the region. Thank you for your consideration.",
        ],
    },
    {
        "company": "MTM Groups Trading",
        "role": "E-Commerce Manager",
        "cv_key": "MTM_Groups_Trading_E-Commerce_Manager",
        "headline": "E-Commerce Manager · Digital Commerce · Digital Shelf · Marketplaces",
        "summary": (
            "E-commerce professional with 4+ years scaling digital commerce across FMCG, beauty and "
            "quick-commerce. Owns the DoFreeze e-store and digital-shelf execution across UAE retailers "
            "(Noon, Talabat, Careem, Deliveroo), and grew 42 key accounts +30% GMV QoQ on Alibaba's "
            "Miravia marketplace. Runs the Shopify store end-to-end (catalogue, UX, CRO), weekly "
            "digital-shelf scorecards, content that converts and full-funnel media to ROI/ROAS targets — "
            "and builds generative-AI (Claude) automation for content, campaigns and reporting. A "
            "hands-on, data-led fit for an end-to-end e-commerce mandate."
        ),
        "cl_to": "MTM Groups Trading — Talent Acquisition",
        "cl_re": "Re: E-Commerce Manager, Dubai",
        "cl_paras": [
            "I am applying for the E-Commerce Manager role in Dubai. Running an online business end-to-end — store, digital shelf, content, media and the numbers behind them — is exactly what I do today, and I would relish the chance to own and grow that for MTM Groups.",
            "As Brand &amp; Marketing Manager at DoFreeze (Befit, Eurocake, Flair), I manage the Shopify e-store end-to-end (catalogue, UX, collections, checkout) and own digital-shelf execution across the UAE's key e-commerce and quick-commerce retailers — Noon, Talabat, Careem and Deliveroo — lifting conversion and average order value through data-led merchandising. I plan full-funnel media (Meta, Google, social, EDM) on a weekly scorecard tracking traffic, ROI and ROAS. Earlier, at Alibaba's Miravia, I grew 42 key accounts to +30% GMV QoQ, giving me deep marketplace mechanics on one of the world's top-5 platforms.",
            "What I add: FMCG foundations from Mondelez and an AI-first way of working — I build generative-AI (Claude / Claude Code) automation for content, campaign planning and KPI reporting that cut manual workload ~40%. I am already in Dubai on a residence visa (no relocation) and work fluently in English and Spanish.",
            "I would welcome the chance to discuss how I can grow MTM Groups' online sales. Thank you for your consideration.",
        ],
    },
    {
        "company": "FIJI Water International",
        "role": "Marketing Manager",
        "cv_key": "FIJI_Water_International_Marketing_Manager",
        "headline": "Marketing Manager · Brand · FMCG · Go-to-Market",
        "summary": (
            "Brand and marketing professional with 4+ years across FMCG, beverages, beauty and "
            "quick-commerce. Leads brand &amp; marketing for DoFreeze across 50+ markets — brand strategy, "
            "360 campaigns, NPD, go-to-market and A&amp;P to P&amp;L targets — with full-funnel media and "
            "trade/shopper execution across modern trade and UAE quick-commerce (Noon, Talabat, Careem, "
            "Deliveroo). Grew 42 key accounts +30% GMV QoQ at Alibaba's Miravia. AI-first marketer building "
            "generative-AI (Claude) automation. A strong fit to build a premium FMCG beverage brand in the region."
        ),
        "cl_to": "FIJI Water International — Talent Acquisition",
        "cl_re": "Re: Marketing Manager, Dubai",
        "cl_paras": [
            "I am applying for the Marketing Manager role in Dubai. Building a premium FMCG brand — protecting its equity while driving visibility, distribution and sell-out — is the work I love, and FIJI Water is exactly the kind of aspirational, quality-led brand I would be proud to grow across the region.",
            "As Brand &amp; Marketing Manager at DoFreeze (Befit, Eurocake, Flair), I lead brand strategy, 360 campaigns and go-to-market across 50+ markets, own A&amp;P allocation to net-sales and P&amp;L targets, and drive trade &amp; shopper plans across modern trade and quick-commerce. I run full-funnel media (Meta, Google, social, EDM) to ROI/ROAS and led 6 NPD launches end-to-end. Earlier, at Alibaba's Miravia, I grew 42 key accounts to +30% GMV QoQ, and my career began in FMCG category planning at Mondelez.",
            "What I add: hands-on UAE market experience across the key retailers and quick-commerce platforms, a premium-brand sensibility (Inditex-trained early on), and an AI-first approach — I build generative-AI (Claude / Claude Code) automation for content and campaign planning that cut manual workload ~40%. I am already in Dubai on a residence visa (no relocation) and work fluently in English and Spanish.",
            "I would welcome the chance to discuss how I can grow FIJI Water across the UAE and wider region. Thank you for your consideration.",
        ],
    },
    {
        "company": "Delivery Hero",
        "role": "Manager Marketing Campaign",
        "cv_key": "Delivery_Hero_Manager_Marketing_Campaign",
        "headline": "Marketing Campaign Manager · Quick-Commerce · Full-Funnel · FMCG",
        "summary": (
            "Marketing manager with 4+ years running campaigns across FMCG, beauty and quick-commerce. "
            "Plans and optimises 360 and full-funnel campaigns (Meta Ads, Google Ads, social, EDM) on "
            "weekly scorecards to ROI/ROAS, with hands-on execution across the UAE quick-commerce platforms "
            "in Delivery Hero's world — Talabat, Careem, Noon, Deliveroo. Scaled an influencer programme from "
            "zero to 25–50 creators per campaign and grew 42 key accounts +30% GMV QoQ at Alibaba's Miravia. "
            "AI-first marketer building generative-AI (Claude) automation for campaign planning and content. "
            "A direct fit for a campaign management mandate in quick-commerce."
        ),
        "cl_to": "Delivery Hero — Talent Acquisition",
        "cl_re": "Re: Manager, Marketing Campaign — Dubai",
        "cl_paras": [
            "I am applying for the Manager, Marketing Campaign role in Dubai. Quick-commerce is the world I work in every day — I integrate brands into and market across Talabat, Careem, Noon and Deliveroo — so both the pace and the mechanics of campaigns in this space are second nature to me.",
            "As Brand &amp; Marketing Manager at DoFreeze (Befit, Eurocake, Flair), I plan and run 360 and full-funnel campaigns (Meta, Google, social, EDM) across 50+ markets, tracking traffic, spend, ROI and ROAS on a weekly scorecard and acting on the numbers. I scaled an influencer programme from zero to 25–50 creators per campaign driving UGC and sell-out, and led 6 NPD go-to-market launches. Earlier, at Alibaba's Miravia, I grew 42 key accounts to +30% GMV QoQ and ran the Flash Sales channel to P&amp;L targets.",
            "What I add: first-hand quick-commerce experience across the region's platforms, FMCG foundations from Mondelez, and an AI-first approach — I build generative-AI (Claude / Claude Code) automation for campaign planning, content and reporting that cut manual workload ~40%. I am already in Dubai on a residence visa (no relocation) and work fluently in English and Spanish.",
            "I would welcome the chance to discuss how I can drive high-performing campaigns for Delivery Hero across the region. Thank you for your consideration.",
        ],
    },
    {
        "company": "Sunberry Fresh",
        "role": "Performance Marketing Growth Manager",
        "cv_key": "Sunberry_Fresh_Performance_Marketing_Growth_Manager",
        "headline": "Performance &amp; Growth Marketing Manager · Paid Media · E-Commerce · CRO",
        "summary": (
            "Performance and growth marketer with 4+ years across FMCG, food &amp; beverage, beauty and "
            "quick-commerce. Plans and optimises full-funnel paid media (Meta Ads, Google Ads, social, EDM) "
            "to ROI/ROAS on weekly scorecards, and owns the DoFreeze Shopify store end-to-end — lifting "
            "conversion rate (CRO) and average order value through data-led merchandising and A/B testing. "
            "Grew 42 key accounts +30% GMV QoQ at Alibaba's Miravia. AI-first marketer building generative-AI "
            "(Claude) automation for creatives, campaign planning and analytics. A data-led fit for a growth "
            "mandate."
        ),
        "cl_to": "Sunberry Fresh — Talent Acquisition",
        "cl_re": "Re: Performance Marketing &amp; Growth Manager — Dubai",
        "cl_paras": [
            "I am applying for the Performance Marketing &amp; Growth Manager role in Dubai. Growth marketing that is genuinely accountable to the numbers — spend, conversion, ROAS, CAC — is exactly how I work, and I would enjoy driving that engine for Sunberry Fresh.",
            "As Brand &amp; Marketing Manager at DoFreeze (Befit, Eurocake, Flair), I plan and optimise full-funnel paid media (Meta Ads, Google Ads, social, EDM) on a weekly KPI scorecard tracking traffic, spend, ROI and ROAS, and I own the Shopify e-store end-to-end — lifting conversion rate (CRO) and average order value through data-led merchandising and A/B testing. Earlier, at Alibaba's Miravia, I grew 42 key accounts to +30% GMV QoQ through conversion-led promotions and assortment.",
            "What I add: hands-on UAE e-commerce and quick-commerce experience (Noon, Talabat, Careem, Deliveroo), and an AI-first approach that multiplies output — I build generative-AI (Claude / Claude Code) automation for creatives, campaign planning and analytics, plus AI video (Higgsfield, Hailuo) for social, cutting manual workload ~40%. I am already in Dubai on a residence visa (no relocation) and work fluently in English and Spanish.",
            "I would welcome the chance to discuss how I can accelerate Sunberry Fresh's growth. Thank you for your consideration.",
        ],
    },
]

# --------------------------------------------------------------------------
# Styles (shared)
# --------------------------------------------------------------------------
CSS = """
@page { size: A4; margin: 14mm 15mm 12mm 15mm; }
* { box-sizing: border-box; }
html, body { margin:0; padding:0; font-family:"Helvetica Neue","Arial","Segoe UI",sans-serif;
  font-size:10pt; color:__INK__; line-height:1.34; }
h1 { font-size:23pt; font-weight:800; margin:0 0 3px 0; color:__INK__; letter-spacing:.2px; }
.headline { color:__RED__; font-weight:700; font-size:10.5pt; margin:0 0 5px 0; }
.contact { color:__MUTE__; font-size:9pt; margin:0; }
.status  { color:__INK__; font-size:9pt; margin:2px 0 0 0; }
h2 { color:__RED__; font-size:10.5pt; font-weight:700; text-transform:uppercase; letter-spacing:1px;
  border-bottom:1px solid #e3c4c7; padding-bottom:3px; margin:15px 0 8px 0; break-after:avoid; }
p.summary { margin:0; text-align:justify; }
.job { margin:0 0 10px 0; break-inside:avoid; }
.job-head { display:flex; justify-content:space-between; align-items:baseline; }
.job-role { font-weight:700; font-size:10.5pt; color:__INK__; }
.job-dates { font-size:9pt; color:__MUTE__; white-space:nowrap; padding-left:10px; }
.job-context { font-size:9pt; color:__MUTE__; margin:1px 0 4px 0; }
ul { margin:0; padding-left:16px; }
li { margin:2px 0; }
li::marker { color:__RED__; }
table.skills { width:100%; border-collapse:collapse; }
table.skills td { vertical-align:top; padding:4px 0; border-bottom:1px solid #eee; }
td.k { width:22%; font-weight:700; color:__INK__; padding-right:10px; }
td.v { color:#333; }
.edu-head { display:flex; justify-content:space-between; align-items:baseline; }
.edu-title { font-weight:700; color:__INK__; }
.edu-dates { font-size:9pt; color:__MUTE__; }
.edu-sub { font-size:9pt; color:__MUTE__; margin:1px 0 0 0; }
.langs { display:flex; gap:60px; }
.langs .l-name { font-weight:700; color:__INK__; }
.langs .l-lvl { color:#333; }
""".replace("__RED__", RED).replace("__INK__", INK).replace("__MUTE__", MUTE)

CL_CSS = """
@page { size:A4; margin:20mm 20mm 18mm 20mm; }
* { box-sizing:border-box; }
html,body { margin:0; padding:0; font-family:"Helvetica Neue","Arial","Segoe UI",sans-serif;
  font-size:10.5pt; color:__INK__; line-height:1.5; }
h1 { font-size:19pt; font-weight:800; margin:0 0 2px 0; color:__INK__; }
.contact { color:__MUTE__; font-size:9.5pt; margin:0 0 8px 0; }
.rule { border:0; border-top:2px solid __RED__; margin:0 0 16px 0; }
.to { font-weight:700; color:__INK__; margin:0; }
.meta { color:__MUTE__; font-size:9.5pt; margin:0; }
.date { color:__MUTE__; font-size:9.5pt; margin:2px 0 16px 0; }
p { margin:0 0 12px 0; text-align:justify; }
.sign { margin-top:18px; }
.sign .n { font-weight:700; color:__INK__; }
.sign .c { color:__MUTE__; font-size:9.5pt; }
""".replace("__RED__", RED).replace("__INK__", INK).replace("__MUTE__", MUTE)


def build_cv(job: dict) -> str:
    jobs = ""
    for e in EXPERIENCE:
        lis = "".join(f"<li>{b}</li>" for b in e["bullets"])
        jobs += f"""
<div class="job">
  <div class="job-head">
    <span class="job-role">{e['role']}</span>
    <span class="job-dates">{e['dates']}</span>
  </div>
  <div class="job-context">{e['context']}</div>
  <ul>{lis}</ul>
</div>"""
    skills_rows = "".join(
        f'<tr><td class="k">{k}</td><td class="v">{v}</td></tr>' for k, v in SKILLS
    )
    body = f"""
<header>
  <h1>{NAME}</h1>
  <p class="headline">{job['headline']}</p>
  <p class="contact">{CONTACT}</p>
  <p class="status">{STATUS}</p>
</header>

<h2>Professional Summary</h2>
<p class="summary">{job['summary']}</p>

<h2>Work Experience</h2>
{jobs}

<h2>Core Skills &amp; Tools</h2>
<table class="skills">{skills_rows}</table>

<h2>Education</h2>
<div class="edu-head">
  <span class="edu-title">Bachelor's in Business Administration — CUNEF Universidad, Madrid</span>
  <span class="edu-dates">2016 – 2020</span>
</div>
<p class="edu-sub">Specialisation: E-Commerce · Fashion Industry · Thesis grade: 9.5/10</p>
<p class="edu-sub">Google E-Commerce Certificate · Google Digital Marketing Certificate</p>

<h2>Languages</h2>
<div class="langs">
  <span><span class="l-name">Spanish</span> &nbsp; <span class="l-lvl">Native</span></span>
  <span><span class="l-name">English</span> &nbsp; <span class="l-lvl">Professional (C1)</span></span>
</div>
"""
    return f"<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"


def build_cl(job: dict) -> str:
    paras = "".join(f"<p>{p}</p>" for p in job["cl_paras"])
    body = f"""
<h1>{NAME}</h1>
<p class="contact">Dubai, UAE · +971 50 386 3656 · paulich98@hotmail.com · linkedin.com/in/paula-de-francisco-perez</p>
<hr class="rule">
<p class="to">{job['cl_to']}</p>
<p class="meta">{job['cl_re']}</p>
<p class="date">Dubai, 8 July 2026</p>

<p>Dear Hiring Team,</p>
{paras}

<div class="sign">
  <p class="n">Paula De Francisco Pérez</p>
  <p class="c">+971 50 386 3656 · paulich98@hotmail.com</p>
</div>
"""
    return f"<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><style>{CL_CSS}</style></head><body>{body}</body></html>"


def render(page, html: str, out: Path) -> None:
    page.set_content(html, wait_until="networkidle")
    page.pdf(path=str(out), format="A4", print_background=True,
             margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})


def main() -> None:
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        for job in JOBS:
            folder = ROOT / "output" / DAY / f"{job['company']} - {job['role']}" / "01_CV_y_Carta"
            folder.mkdir(parents=True, exist_ok=True)
            cv_out = folder / f"CV_Paula_{job['cv_key']}.pdf"
            cl_out = folder / f"CL_Paula_{job['cv_key']}.pdf"
            render(pg, build_cv(job), cv_out)
            render(pg, build_cl(job), cl_out)
            print("OK", job["company"], "->", folder)
        b.close()


if __name__ == "__main__":
    main()
