#!/usr/bin/env python3
"""Generate Paula's BROAD Careem CV (HTML -> PDF) — the "where do I fit?" version.

Companion to _gen_careem_cv_html.py (which is tuned to the Growth Manager
vacancy). This one is for the referral message that says "I'm not sure I fit
this specific role — if you see anything else, flag it". So it must NOT read as
a specialist CV: every capability stays visible and the ordering is deliberately
broad.

Positioning fix vs. the first draft: AI-first leads. Careem is a tech company,
and "marketer who automates the whole commercial stack with Claude Code via
MCP/APIs and built the management dashboard in React" is the most memorable,
most forwardable thing about her — so it is the headline and the first bullet,
the way the Aug-2026 master CV had it. Quick-commerce (she already operates ON
Careem) comes straight after.

Same red-accent house style; rendered via Playwright / Chromium because
weasyprint lacks native libs on this Windows box.

Outputs to: output/<DAY>/Careem - Marketing & E-Commerce (Referral)/01_CV_y_Carta/
"""
from __future__ import annotations

from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
DAY = "2026-09-01"
OUT = ROOT / "output" / DAY / "Careem - Marketing & E-Commerce (Referral)" / "01_CV_y_Carta"
OUT.mkdir(parents=True, exist_ok=True)

RED = "#C8102E"
INK = "#1a1a1a"
MUTE = "#5a6473"

NAME = "Paula De Francisco Pérez"
HEADLINE = ("AI-First Marketing &amp; E-Commerce Manager · Automation &amp; Growth Analytics · "
            "Quick-Commerce &amp; Super-App · Brand &amp; Key Accounts")
CONTACT = ("Dubai, UAE | +971 50 386 3656 | paulich98@hotmail.com | "
           "linkedin.com/in/paula-de-francisco-perez-92a13119a | "
           "paula-de-francisco.vercel.app")
STATUS = ("Nationality: Spanish · UAE Residence Visa — based in Dubai, "
          "no relocation, available immediately")

SUMMARY = (
    "Marketing and e-commerce manager with a hybrid marketing–technology profile and 4+ years "
    "across quick-commerce, FMCG, beauty and fashion in the UAE and Europe. <b>I am AI-first:</b> "
    "I use Claude / Claude Code as an automation layer over the entire commercial stack — Shopify, "
    "Meta Ads, Google Ads &amp; Search Console, Supabase, Notion, Gmail and Canva, connected via "
    "MCP and APIs — and with it I have built management dashboards, a full affiliate programme, "
    "bundle and discount engines, newsletter automation and an SEO/AEO strategy from scratch, "
    "cutting manual workload ~40%. On top of that I run the classic remit end-to-end: brand and "
    "NPD, paid media, e-commerce and CRO, key accounts and trade marketing. Quick-commerce is my "
    "home turf — I was part of the team that built Glovo's retail vertical, and today I grow brands "
    "<b>on Careem, Talabat, Noon and Deliveroo</b> for a multi-brand FMCG group selling in 50+ "
    "countries. Track record: <b>+30% GMV QoQ</b> across 42 key accounts at Alibaba's Miravia and "
    "6 NPD launches across 50+ markets. Business Administration graduate (CUNEF, E-Commerce &amp; "
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
            "<b>Growth analytics &amp; executive dashboards:</b> built an in-house web app (React + Tailwind + Vite) with daily reporting on traffic, revenue by channel, bundles, gifting and every paid campaign, deployed for the management team; sales analysis in ShopifyQL and GA4",
            "<b>Quick-commerce &amp; e-retail:</b> onboarded and grow the brands on <b>Careem, Talabat, Noon and Deliveroo</b> — listings and content, digital-shelf optimisation, in-app promotional mechanics, basket building and retail execution across modern trade; day-to-day owner of the platform relationships",
            "<b>Paid media, AI-assisted:</b> create and optimise Meta and Google Ads campaigns via API — budgets, retargeting audiences, dynamic catalogues, Pixel/CAPI, creative A/B testing and ROAS diagnostics — with automated reporting",
            "<b>E-commerce ownership (Shopify Admin API / GraphQL):</b> multi-brand catalogue, smart collections, inventory, automatic discounts and codes, ShopifyQL analysis across D2C, B2B draft orders and marketplaces; build and maintain the headless dofreeze.ae storefront — brand pages, redirects, technical SEO and campaign landing pages — driving CRO and average order value",
            "<b>Affiliate programme built from zero (\"Befit Crew\"):</b> designed the full programme — tiered commissions (6/8/10% by monthly volume), personalised discount codes, creator validation criteria, legal T&amp;Cs, content brief, email sequence, video script and landing page — and selected and implemented the affiliate engine (BixGrow) on Shopify",
            "<b>Brand &amp; go-to-market:</b> lead 6 NPD launches end-to-end (brief, packaging, pricing, GTM) across GCC, MENA, Asia, Europe, USA and Africa, plus trade and shopper marketing plans by channel",
            "<b>Influencer marketing from zero:</b> sourcing, briefing, negotiation and management of 25–50 creators per campaign, plus sampling and seeding — driving awareness, UGC and measurable sell-out",
            "<b>SEO + AEO/GEO:</b> implemented structured data (schema), llms.txt and entities in Wikidata / Crunchbase / Google Business Profile to position the brands both in search engines and in AI answers (ChatGPT, Perplexity, Google AI)",
        ],
    },
    {
        "role": "Key Account Manager (E-Commerce) – Beauty, Fragrances &amp; Fashion",
        "dates": "Nov 2023 – Oct 2025",
        "context": "Miravia (Alibaba Group) · Top 5 global e-commerce | 100K+ employees · Madrid, Spain",
        "bullets": [
            "Managed 42 key accounts on a top-5 marketplace, achieving <b>+30% GMV growth QoQ</b> through pricing strategy, assortment optimisation and conversion-led promotions",
            "Owned the Flash Sales channel for Beauty, Fashion &amp; Home — reporting directly to the CEO and executing commercial plans against P&amp;L targets",
            "Led category expansion as PIC Fragrances, onboarding 30+ new stores in two months, including the official distributors of leading Arabian &amp; oud houses (Arabian Oud, Lattafa, Swiss Arabian, Ajmal)",
            "Created and led the Beauty Club and Hot on Social projects, boosting visibility, loyalty and positioning Miravia as a beauty and lifestyle destination",
            "Continuously analysed ROI, ROAS, conversion, traffic and retention to optimise channel performance and forecasting accuracy",
        ],
    },
    {
        "role": "Account Manager – XL Accounts",
        "dates": "Sep 2022 – Nov 2023",
        "context": "Glovo · Quick-commerce super-app | EUR 500M+ revenue | 10K+ employees · Madrid, Spain",
        "bullets": [
            "Part of the team that <b>built Glovo's retail vertical</b> — onboarding fashion, beauty and lifestyle brands and expanding the super-app marketplace beyond food delivery into new categories",
            "Managed strategic XL accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop), driving GMV growth through data-led planning, in-app visibility and bespoke marketing activations",
            "Led cross-functional teams across marketing, operations, logistics and customer support to launch campaigns end-to-end, and negotiated high-impact commercial deals",
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
     "workflow automation across Shopify / Meta Ads / GSC / Supabase / Notion, AI image &amp; video "
     "generation (Higgsfield, Hailuo), AEO/GEO for AI search"),
    ("Analytics &amp; Reporting",
     "GA4, Google Search Console, ShopifyQL, Looker, Power BI, React / Tailwind dashboards, "
     "Python (pandas, openpyxl, python-pptx), advanced Excel, Git &amp; GitHub, KPI scorecards, "
     "forecasting, P&amp;L"),
    ("E-Commerce &amp; CRO",
     "Shopify (Admin API, GraphQL), headless D2C, Supabase, BixGrow (affiliates), automatic discounts "
     "&amp; bundle engines, checkout &amp; UX optimisation, digital shelf, technical SEO"),
    ("Quick-Commerce &amp; Marketplaces",
     "Careem, Talabat, Noon, Deliveroo, Glovo · platform onboarding &amp; partner management, "
     "in-app visibility, promotional mechanics, category expansion, retail execution"),
    ("Paid Media",
     "Meta Ads API, Google Ads, Google Merchant Center, Pixel/CAPI, retargeting &amp; dynamic "
     "catalogues, creative A/B testing, ROI / ROAS, EDM &amp; newsletters"),
    ("Brand &amp; Marketing",
     "brand strategy, NPD &amp; go-to-market, influencer marketing &amp; UGC, sampling &amp; seeding, "
     "trade &amp; shopper marketing, A&amp;P budgets, bilingual copy (EN/ES)"),
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
  font-size:9.1pt; color:__INK__; line-height:1.3; }
h1 { font-size:22pt; font-weight:800; margin:0 0 3px 0; color:__INK__; letter-spacing:.2px; }
.headline { color:__RED__; font-weight:700; font-size:10.2pt; margin:0 0 5px 0; }
.contact { color:__MUTE__; font-size:8.4pt; margin:0; }
.status  { color:__INK__; font-size:8.4pt; margin:2px 0 0 0; }
h2 { color:__RED__; font-size:10pt; font-weight:700; text-transform:uppercase; letter-spacing:1px;
  border-bottom:1px solid #e3c4c7; padding-bottom:3px; margin:12px 0 7px 0; break-after:avoid; }
p.summary { margin:0; text-align:justify; }
.job { margin:0 0 9px 0; break-inside:avoid; }
.job-head { display:flex; justify-content:space-between; align-items:baseline; }
.job-role { font-weight:700; font-size:10pt; color:__INK__; }
.job-dates { font-size:8.4pt; color:__MUTE__; white-space:nowrap; padding-left:10px; }
.job-context { font-size:8.4pt; color:__MUTE__; margin:1px 0 4px 0; }
ul { margin:0; padding-left:15px; }
li { margin:2px 0; }
li::marker { color:__RED__; }
b { color:__INK__; }
table.skills { width:100%; border-collapse:collapse; }
table.skills td { vertical-align:top; padding:3.2px 0; border-bottom:1px solid #eee; }
td.k { width:23%; font-weight:700; color:__RED__; padding-right:10px; }
td.v { color:#333; }
.edu-head { display:flex; justify-content:space-between; align-items:baseline; }
.edu-title { font-weight:700; color:__INK__; }
.edu-dates { font-size:8.4pt; color:__MUTE__; }
.edu-sub { font-size:8.4pt; color:__MUTE__; margin:1px 0 0 0; }
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
    cv_out = OUT / "CV_Paula_De_Francisco_Careem.pdf"
    render(build_cv(), cv_out)
    print("OK_CV", cv_out)


if __name__ == "__main__":
    main()
