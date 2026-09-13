#!/usr/bin/env python3
"""Rebuild Paula's Colgate-Palmolive CV + Cover Letter as clean HTML -> PDF.

The original red-styled generator was created in another session and never
committed, so this reconstructs it faithfully from the last rendered package
(output/Colgate/) with three agreed corrections:

  1. Header: drops the false "no sponsorship" claim -> "Based in Dubai, UAE -
     no relocation, available immediately".
  2. Professional summary: adds the generative-AI (Claude) clause.
  3. Cover letter date -> 8 July 2026 (re-application line kept; Paula did
     apply in June).

Renders via Playwright (Chromium headless) because weasyprint lacks its native
libs on this Windows box. Output overwrites the PDFs in output/Colgate/.
"""
from __future__ import annotations

from pathlib import Path
from html import escape

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "output" / "Colgate" / "01_CV_y_Carta"
OUT.mkdir(parents=True, exist_ok=True)

RED = "#D6001C"       # Colgate-brand red accent
INK = "#1a1a1a"       # near-black body
MUTE = "#5a6473"      # muted gray

# --------------------------------------------------------------------------
# Content
# --------------------------------------------------------------------------
NAME = "Paula De Francisco Pérez"
HEADLINE = "E-Commerce Manager · Digital Commerce · FMCG · Digital Shelf & Key Accounts"
CONTACT = "Dubai, UAE | +971 50 386 3656 | paulich98@hotmail.com | linkedin.com/in/paula-de-francisco-perez"
STATUS = "Nationality: Spanish · Based in Dubai, UAE — no relocation, available immediately"

SUMMARY = (
    "E-commerce professional with 4+ years scaling digital commerce across FMCG, beauty and "
    "quick-commerce. Owns the DoFreeze e-store and digital-shelf execution across UAE retailers "
    "(Noon, Talabat, Careem, Deliveroo), and grew 42 key accounts +30% GMV QoQ at Alibaba's Miravia. "
    "Runs weekly digital-shelf scorecards, content that converts and full-funnel media to net-sales "
    "and P&amp;L targets — and builds generative-AI (Claude) automation for content, campaign planning "
    "and KPI reporting. FMCG category-planning foundations from Mondelez; a direct fit for "
    "multinational FMCG digital commerce."
)

EXPERIENCE = [
    {
        "role": "Brand &amp; Marketing Manager",
        "dates": "Oct 2025 – Present",
        "context": "DoFreeze LLC · Global FMCG distributor | Brands: Befit, Eurocake, Flair | 50+ countries · Dubai, UAE",
        "bullets": [
            "Own digital-shelf execution across UAE e-commerce retailers (Noon, Talabat, Careem, Deliveroo) — listings, rich content, imagery, pricing and promotional mechanics that lift click &amp; conversion rates",
            "Manage the Shopify e-store end-to-end (catalogue, UX, collections, checkout), lifting conversion rate (CRO) and average order value through data-led merchandising",
            "Plan and optimise full-funnel digital marketing (Meta Ads, Google Ads, social, EDM), tracking traffic, spend, ROI and ROAS by channel on a weekly KPI scorecard and recommending corrective actions",
            "Drive category growth and promotion strategy across sub-channels, owning A&amp;P budget allocation to net-sales and P&amp;L targets",
            "Led 6 NPD launches end-to-end (brief, packaging, pricing, go-to-market) across GCC, MENA, Asia, Europe, USA and Africa — differentiated innovation with best-in-class execution",
            "Coordinate agencies and built AI-powered automation (Claude) for content, campaign planning and KPI reporting, cutting manual workload ~40%",
        ],
    },
    {
        "role": "Key Account Manager (E-Commerce) – Beauty, Fragrances &amp; Fashion",
        "dates": "Nov 2023 – Oct 2025",
        "context": "Miravia (Alibaba Group) · Top 5 global e-commerce | 100K+ employees · Madrid, Spain",
        "bullets": [
            "Grew 42 key accounts +30% GMV QoQ on a top-5 global e-commerce platform through pricing, assortment and conversion-led promotions",
            "Owned the digital shelf for Beauty, Fashion &amp; Home — content, assortment and promotional execution — and ran the Flash Sales channel to P&amp;L targets, reporting directly to the CEO",
            "Continuously analysed conversion, traffic, retention, ROI and ROAS to optimise channel performance and forecasting",
            "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months via data-led assortment",
        ],
    },
    {
        "role": "Account Manager – XL Accounts",
        "dates": "Sep 2022 – Nov 2023",
        "context": "Glovo · Quick-commerce leader | EUR 500M+ revenue | 10K+ employees · Madrid, Spain",
        "bullets": [
            "Helped build Glovo's retail vertical — onboarding fashion, beauty and lifestyle brands and expanding the marketplace beyond food delivery",
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
    ("Brand &amp; Marketing", "digital commerce strategy, digital shelf excellence, content that converts, 360 marketing communications, promotion strategy, go-to-market, NPD / innovation launches"),
    ("E-Commerce &amp; Digital", "e-store management, Shopify, conversion rate optimisation (CRO), full-funnel, digital merchandising, product content &amp; digital-asset (DAM) workflows, online marketplaces, quick-commerce, Noon, Talabat, Careem, Deliveroo, Meta Ads, Google Ads, EDM"),
    ("Commercial", "key account management, category growth, assortment planning, pricing strategy, customer prioritization, supply-chain coordination, distributor management"),
    ("Data &amp; Analytics", "digital-shelf scorecards, conversion &amp; click-through, P&amp;L management, Net Sales, ROI, ROAS, traffic &amp; channel analytics, KPI tracking, Looker"),
    ("Tools", "Shopify, Meta Ads Manager, Google Ads, Looker, Salesforce, SAP, Generative AI (Claude), Microsoft Office / Google Suite (Expert)"),
]

# --------------------------------------------------------------------------
# Styles
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


def build_cv() -> str:
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
  <p class="headline">{HEADLINE}</p>
  <p class="contact">{CONTACT}</p>
  <p class="status">{STATUS}</p>
</header>

<h2>Professional Summary</h2>
<p class="summary">{SUMMARY}</p>

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


# --------------------------------------------------------------------------
# Cover letter
# --------------------------------------------------------------------------
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
a { color:__RED__; text-decoration:none; }
""".replace("__RED__", RED).replace("__INK__", INK).replace("__MUTE__", MUTE)

CL_BODY = f"""
<h1>{NAME}</h1>
<p class="contact">Dubai, UAE · +971 50 386 3656 · paulich98@hotmail.com · linkedin.com/in/paula-de-francisco-perez</p>
<hr class="rule">
<p class="to">Colgate-Palmolive — Talent Acquisition</p>
<p class="meta">Re: Ecommerce Manager, Dubai (Job #174114)</p>
<p class="date">Dubai, 8 July 2026</p>

<p>Dear Hiring Team,</p>

<p>I am re-applying for the Ecommerce Manager role in Dubai (Job #174114), now that the position has
been reposted — I first applied in June, and the weeks since have only strengthened my conviction that
this is the role I am built for. Colgate-Palmolive's products are trusted in more households than any
other brand in the world, and the chance to translate that trust into digital-shelf excellence — turning
rich content and data into measurable conversion across Oral, Personal, Home and Pet Care — is exactly
the challenge I am looking for. I already build this every day in Dubai's FMCG and quick-commerce market.</p>

<p>As Brand &amp; Marketing Manager at DoFreeze (Befit, Eurocake, Flair), I own the Shopify e-store
end-to-end and run digital-shelf execution across UAE e-commerce retailers — listings, content,
promotions and net-sales delivery — using ROI/ROAS analytics and weekly scorecards to drive conversion
and corrective action. Earlier, at Alibaba's Miravia, I managed 42 key accounts to +30% GMV growth QoQ
through pricing, assortment and promotion strategy, running the Flash Sales channel to P&amp;L targets and
reporting directly to the CEO. That blend of digital commerce strategy, customer alignment and full-funnel
execution maps directly to this role's remit.</p>

<p>What sets me apart for a UAE FMCG mandate: hands-on experience across the key e-retailers and
quick-commerce platforms in this market — Noon, Talabat, Careem and Deliveroo — plus FMCG
category-planning foundations from Mondelez and an AI-first approach (I built generative-AI automation for
content, campaign planning and KPI reporting that cut manual workload ~40%). I am already based in Dubai
on a UAE residence visa, so there is zero relocation cost or delay, and I work fluently in English and Spanish.</p>

<p>To show rather than tell, I prepared a concept of how I would approach Colgate's digital shelf in the
UAE — <strong>"Always Shelf-Ready"</strong> (<a href="https://landingcolgate.vercel.app">landingcolgate.vercel.app</a>),
with a supporting deck covering the perfect page, search-share dominance, retail media, quick-commerce and
one weekly scorecard. I would welcome the chance to walk you through it and discuss how I can accelerate
Colgate-Palmolive's digital commerce growth in the region. I am available to start at short notice. Thank
you for your consideration.</p>

<div class="sign">
  <p class="n">Paula De Francisco Pérez</p>
  <p class="c">+971 50 386 3656 · paulich98@hotmail.com</p>
</div>
"""
CL_HTML = f"<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><style>{CL_CSS}</style></head><body>{CL_BODY}</body></html>"


def render(html: str, out: Path) -> None:
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.set_content(html, wait_until="networkidle")
        pg.pdf(path=str(out), format="A4", print_background=True,
               margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        b.close()


def main() -> None:
    cv_out = OUT / "CV_Paula_Colgate-Palmolive_Ecommerce_Manager.pdf"
    cl_out = OUT / "CL_Paula_Colgate-Palmolive_Ecommerce_Manager.pdf"
    render(build_cv(), cv_out)
    render(CL_HTML, cl_out)
    print("OK_CV", cv_out)
    print("OK_CL", cl_out)


if __name__ == "__main__":
    main()
