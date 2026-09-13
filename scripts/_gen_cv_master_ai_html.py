#!/usr/bin/env python3
"""Generate Paula's MASTER CV (HTML -> PDF): Marketing + E-Commerce + AI.

Not tailored to a single vacancy — this is the general-purpose CV she shares in
Dubai networking / job groups (WhatsApp "Opportunities" style). Positioning:
hybrid marketing-technology profile who runs the commercial stack with AI
(Claude / Claude Code + MCP) on top of Shopify, Meta/Google Ads, Supabase,
Notion, GSC and Canva.

Same red-accent house style as the other packages; rendered via Playwright /
Chromium because weasyprint lacks native libs on this Windows box.

Outputs to: output/<DAY>/CV_Master_Marketing_Ecommerce_AI/01_CV_y_Carta/
"""
from __future__ import annotations

from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
DAY = "2026-08-12"
OUT = ROOT / "output" / DAY / "CV_Master_Marketing_Ecommerce_AI" / "01_CV_y_Carta"
OUT.mkdir(parents=True, exist_ok=True)

RED = "#C8102E"
INK = "#1a1a1a"
MUTE = "#5a6473"

NAME = "Paula De Francisco Pérez"
HEADLINE = "Marketing &amp; E-Commerce Manager · AI-Powered Growth &amp; Automation"
CONTACT = ("Dubai, UAE | +971 50 386 3656 | paulich98@hotmail.com | "
           "linkedin.com/in/paula-de-francisco-perez")
STATUS = ("Nationality: Spanish · UAE Residence Visa — based in Dubai, "
          "no relocation, available immediately")

SUMMARY = (
    "Marketing and e-commerce manager with a hybrid marketing–technology profile and 4+ years "
    "across FMCG, beauty, fashion and quick-commerce in the UAE and Europe. I run brand, "
    "e-commerce and paid media end-to-end — and I use AI (Claude / Claude Code) as an automation "
    "layer over the entire company stack: Shopify, Meta Ads, Google Ads &amp; Search Console, "
    "Supabase, Notion, Gmail, Google Drive and Canva, connected via MCP and APIs. With it I have "
    "built management dashboards, a full affiliate programme, bundle and discount engines, "
    "newsletter automation and an SEO/AEO strategy from scratch. Track record: +30% GMV QoQ across "
    "42 key accounts at Alibaba's Miravia, 6 NPD launches across 50+ markets, and ~40% less manual "
    "workload through AI automation. Business Administration graduate (CUNEF, E-Commerce &amp; "
    "Fashion Industry specialisation)."
)

EXPERIENCE = [
    {
        "role": "Brand &amp; Marketing Manager",
        "dates": "Oct 2025 – Present",
        "context": ("DoFreeze LLC · Multi-brand FMCG: Befit, Eurocake, SMASH, Flair, Delice | "
                    "50+ countries · Dubai, UAE"),
        "bullets": [
            "<b>AI automation across the full stack:</b> run Claude Code with MCP/API connectors to Shopify, Meta Ads, Google Search Console, Supabase, Notion, Gmail, Google Drive and Canva — executing real production changes (products, collections, automatic discounts, campaigns, audiences and catalogues) and cutting manual workload ~40%",
            "<b>Shopify (Admin API / GraphQL):</b> multi-brand catalogue management, smart collections, inventory, automatic discounts and codes, CDN image uploads and sales analysis with ShopifyQL across D2C, B2B draft orders and marketplaces — driving conversion rate (CRO) and average order value",
            "<b>D2C site (dofreeze.ae):</b> build and maintain the headless storefront on Shopify — technical briefs, brand pages, redirects, technical-SEO fixes (canonicals, 404s, indexation) and campaign landing pages",
            "<b>Affiliate programme built from zero (\"Befit Crew\"):</b> designed the full programme — tiered commissions (6/8/10% by monthly volume), personalised discount codes, creator validation criteria, legal T&amp;Cs, content brief, email sequence, video script and landing page — and selected and implemented the affiliate engine (BixGrow) on Shopify",
            "<b>Paid media assisted by AI:</b> create and optimise Meta and Google Ads campaigns via API — budgets, retargeting audiences, dynamic catalogues, Pixel/CAPI, ROAS diagnostics and broken-feed fixes — with automated reporting",
            "<b>Executive dashboards:</b> built an in-house web app (React + Tailwind + Vite) with daily updates on web traffic, revenue by channel, bundles, gifting and every paid campaign, deployed for the management team",
            "<b>SEO + AEO/GEO:</b> implemented structured data (schema), llms.txt, entities in Wikidata / Crunchbase and Google Business Profile to position the brands both in search engines and in AI answers (ChatGPT, Perplexity, Google AI)",
            "<b>Brand &amp; go-to-market:</b> lead 6 NPD launches end-to-end (brief, packaging, pricing, GTM) across GCC, MENA, Asia, Europe, USA and Africa, plus trade and shopper marketing plans by channel",
            "<b>E-retail &amp; quick-commerce:</b> onboarded and manage the brands on Noon, Talabat, Careem and Deliveroo — listings, content, promotional mechanics and retail execution across modern trade",
            "<b>Influencer marketing from zero:</b> sourcing, briefing, negotiation and management of 25–50 creators per campaign, plus sampling and seeding — driving awareness, UGC and measurable sell-out",
        ],
    },
    {
        "role": "Key Account Manager (E-Commerce) – Beauty, Fragrances &amp; Fashion",
        "dates": "Nov 2023 – Oct 2025",
        "context": "Miravia (Alibaba Group) · Top 5 global e-commerce | 100K+ employees · Madrid, Spain",
        "bullets": [
            "Managed 42 key accounts, achieving <b>+30% GMV growth QoQ</b> through pricing strategy, assortment optimisation and conversion-led promotions",
            "Owned the Flash Sales channel for Beauty, Fashion &amp; Home — reporting directly to the CEO and executing commercial plans against P&amp;L targets",
            "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months, including the official distributors of leading Arabian &amp; oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
            "Created and led the Beauty Club and Hot on Social projects, boosting visibility, loyalty and positioning Miravia as a beauty and lifestyle destination",
            "Continuously analysed ROI, ROAS, conversion, traffic and retention to optimise channel performance and forecasting accuracy",
        ],
    },
    {
        "role": "Account Manager – XL Accounts",
        "dates": "Sep 2022 – Nov 2023",
        "context": "Glovo · Quick-commerce leader | EUR 500M+ revenue | 10K+ employees · Madrid, Spain",
        "bullets": [
            "Part of the team that built Glovo's retail vertical — onboarding fashion, beauty and lifestyle brands and expanding the marketplace beyond food delivery",
            "Managed strategic XL accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop), driving GMV growth through data-led planning and bespoke marketing activations",
            "Led cross-functional teams across marketing, logistics and customer support, and negotiated high-impact commercial deals",
        ],
    },
    {
        "role": "Trainee – Category Planning",
        "dates": "Aug 2021 – Aug 2022",
        "context": "Mondelez International · Global FMCG | EUR 36B revenue | 90K+ employees · Madrid, Spain",
        "bullets": [
            "Sell-in / sell-out analysis, promotional effectiveness evaluation and category performance reporting for the chocolate category",
            "Contributed to NPD launches including Milka Spread and Mini Suchard",
        ],
    },
]

SKILLS = [
    ("AI &amp; Automation",
     "Claude / Claude Code, MCP &amp; APIs, prompt engineering, AI agents &amp; scheduled tasks, "
     "AI image &amp; video generation (Higgsfield, Hailuo), AEO/GEO for AI search"),
    ("E-Commerce",
     "Shopify (Admin API, GraphQL, ShopifyQL), headless D2C (Lovable), Supabase, BixGrow (affiliates), "
     "CRO, digital shelf, marketplaces &amp; quick-commerce (Noon, Talabat, Careem, Deliveroo)"),
    ("Paid &amp; Analytics",
     "Meta Ads API, Google Ads, GA4, Google Search Console, Google Merchant Center, Pixel/CAPI, "
     "ROI / ROAS, Looker, Power BI"),
    ("Brand &amp; Marketing",
     "brand strategy, NPD &amp; go-to-market, influencer marketing &amp; UGC, sampling &amp; seeding, "
     "trade &amp; shopper marketing, A&amp;P budgets, SEO/AEO, EDM &amp; newsletters, bilingual copy (EN/ES)"),
    ("Data &amp; Reporting",
     "Python (pandas, openpyxl, python-pptx), advanced Excel, React / Tailwind dashboards, Git &amp; GitHub, "
     "KPI scorecards, forecasting, P&amp;L"),
    ("Commercial",
     "key account management, distributor &amp; modern trade management, negotiation, pricing, "
     "assortment planning, category management"),
    ("Productivity",
     "Notion, Gmail, Google Drive, Canva, Microsoft Office (Expert), Salesforce, SAP"),
]

CSS = """
@page { size: A4; margin: 13mm 14mm 11mm 14mm; }
* { box-sizing: border-box; }
html, body { margin:0; padding:0; font-family:"Helvetica Neue","Arial","Segoe UI",sans-serif;
  font-size:9.3pt; color:__INK__; line-height:1.32; }
h1 { font-size:22pt; font-weight:800; margin:0 0 3px 0; color:__INK__; letter-spacing:.2px; }
.headline { color:__RED__; font-weight:700; font-size:10.5pt; margin:0 0 5px 0; }
.contact { color:__MUTE__; font-size:8.6pt; margin:0; }
.status  { color:__INK__; font-size:8.6pt; margin:2px 0 0 0; }
h2 { color:__RED__; font-size:10pt; font-weight:700; text-transform:uppercase; letter-spacing:1px;
  border-bottom:1px solid #e3c4c7; padding-bottom:3px; margin:13px 0 7px 0; break-after:avoid; }
p.summary { margin:0; text-align:justify; }
.job { margin:0 0 9px 0; break-inside:avoid; }
.job-head { display:flex; justify-content:space-between; align-items:baseline; }
.job-role { font-weight:700; font-size:10pt; color:__INK__; }
.job-dates { font-size:8.6pt; color:__MUTE__; white-space:nowrap; padding-left:10px; }
.job-context { font-size:8.6pt; color:__MUTE__; margin:1px 0 4px 0; }
ul { margin:0; padding-left:15px; }
li { margin:2px 0; }
li::marker { color:__RED__; }
b { color:__INK__; }
table.skills { width:100%; border-collapse:collapse; }
table.skills td { vertical-align:top; padding:3.5px 0; border-bottom:1px solid #eee; }
td.k { width:21%; font-weight:700; color:__RED__; padding-right:10px; }
td.v { color:#333; }
.edu-head { display:flex; justify-content:space-between; align-items:baseline; }
.edu-title { font-weight:700; color:__INK__; }
.edu-dates { font-size:8.6pt; color:__MUTE__; }
.edu-sub { font-size:8.6pt; color:__MUTE__; margin:1px 0 0 0; }
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
    return (f"<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
            f"<style>{CSS}</style></head><body>{body}</body></html>")


def render(html: str, out: Path) -> None:
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.set_content(html, wait_until="networkidle")
        pg.pdf(path=str(out), format="A4", print_background=True,
               margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        b.close()


def main() -> None:
    cv_out = OUT / "CV_Paula_De_Francisco_Marketing_Ecommerce_AI.pdf"
    render(build_cv(), cv_out)
    print("OK_CV", cv_out)


if __name__ == "__main__":
    main()
