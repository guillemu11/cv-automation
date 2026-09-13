"""1-page CV tailored to a Sr. Specialist INFLUENCER MARKETING role (Talabat via
Álvaro referral): leads on influencer/brand building + paid creator programmes,
keeps AI-first prominent, and still shows KAM + e-commerce/quick-commerce range.
Saved to output/CV_general/CV_Paula_Influencer.pdf (1 page)."""
from __future__ import annotations
import shutil, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent; sys.path.insert(0, str(ROOT))
from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

CONTENT = {
 "headline": ("Influencer & Brand Marketing · Paid Creator Programmes (25–50 creators/campaign) · AI-First Marketer "
              "(Claude/GPT) · E-Commerce & Quick-Commerce · Key Account Management · Dubai-based"),
 "professional_summary": (
   "Brand & influencer marketer in Dubai who builds brands through creator programmes end-to-end — I built "
   "DoFreeze's influencer programme from zero, managing 25–50 creators per campaign (paid + organic) with briefing, "
   "negotiation and sampling/seeding for UGC and sell-out. AI-first (Claude/GPT automation), with strong "
   "e-commerce, quick-commerce and key-account experience (+30% GMV QoQ)."),
 "experience": [
   {"company":"DoFreeze LLC","role":"Brand & Marketing Manager","dates":"Oct 2025 – Present","location":"Dubai, UAE",
    "context":"Multi-brand FMCG group | Befit, Eurocake, Flair | 50+ countries","bullets":[
      "Built and scaled the influencer programme from zero — sourcing, briefing, negotiating and managing 25–50 creators per campaign across paid and organic, plus sampling & seeding — building brand awareness, generating UGC and driving measurable sell-out",
      "Lead brand building and NPD end-to-end across 50+ markets, integrating brands into UAE quick-commerce (Talabat, Noon, Careem, Deliveroo) and running paid media on Meta & Google Ads",
      "AI-first: built a generative-AI system (Claude/GPT) that automates creator research, brief writing, content and reporting — cutting ~40% of manual work"]},
   {"company":"Miravia (Alibaba Group)","role":"Key Account Manager – Beauty, Fragrances & Fashion","dates":"Nov 2023 – Oct 2025","location":"Madrid, Spain",
    "context":"Top-5 global e-commerce marketplace (Alibaba) | 100K+ employees","bullets":[
      "Owned 42 brand accounts end-to-end (+30% GMV QoQ) and created the 'Hot on Social' and Beauty Club projects to boost brand visibility, social buzz and loyalty",
      "Led category expansion — 30+ brands onboarded in two months — and owned the Flash Sales channel, reporting to the CEO"]},
   {"company":"Glovo","role":"Account Manager – XL Accounts","dates":"Sep 2022 – Nov 2023","location":"Madrid, Spain",
    "context":"Quick-commerce super-app | €500M+ revenue","bullets":[
      "Managed strategic key accounts and partner marketing activations on a quick-commerce super-app, driving GMV growth"]},
   {"company":"Mondelez International","role":"Trainee – Category Planning","dates":"Aug 2021 – Aug 2022","location":"Madrid, Spain",
    "context":"Global FMCG multinational | €36B revenue","bullets":[
      "Category planning at a global FMCG — sell-in/sell-out analysis and NPD support (Milka Spread, Mini Suchard)"]},
 ],
 "skills_brand":"influencer marketing (paid + organic), creator sourcing/briefing/negotiation, brand building & strategy, UGC, sampling & seeding, social & content, NPD",
 "skills_ecommerce":"quick-commerce (Talabat, Noon, Careem, Deliveroo), campaigns & promotions, Meta & Google Ads, Shopify & CRO, marketplace management, EDM",
 "skills_commercial":"key account management, negotiation, pricing & assortment, category management, budget management",
 "skills_data":"campaign & influencer KPIs, ROI/ROAS, sell-in/sell-out, AI-assisted analysis, Power BI",
 "skills_tools":"Generative AI (Claude, ChatGPT), Meta Ads, Google Ads, Shopify, Power BI, MS Office (Expert)",
}

job = Job(id="paula-influencer-cv", title="Influencer", company="Paula De Francisco",
          location="Dubai, UAE", url="", source="manual", description="", raw={})
docx = cv._fill_template(CONTENT, job)
dest_dir = settings.output_dir / "2026-08-27"; dest_dir.mkdir(parents=True, exist_ok=True)
dest_docx = dest_dir / "CV_Paula_De_Francisco.docx"
shutil.move(str(docx), str(dest_docx))
shutil.rmtree(settings.output_dir / "Paula De Francisco - Influencer", ignore_errors=True)
soffice = shutil.which("soffice") or "/Applications/LibreOffice.app/Contents/MacOS/soffice"
subprocess.run([soffice,"--headless","--convert-to","pdf","--outdir",str(dest_dir),str(dest_docx)],check=True,capture_output=True,timeout=180)
dest_docx.unlink(missing_ok=True)
pdf = dest_dir / "CV_Paula_De_Francisco.pdf"
import pypdf
print("PAGES:", len(pypdf.PdfReader(str(pdf)).pages), "->", pdf)
