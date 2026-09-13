"""Master/general 1-page CV for Paula — showcases AI-first working + brand/
marketing + key account management + e-commerce/quick-commerce ("un poco todo").
Not tailored to one JD; for warm intros/referrals (e.g. Álvaro @ Talabat).
Saved to output/CV_general/CV_Paula_DeFrancisco.pdf (1 page)."""
from __future__ import annotations
import shutil, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent; sys.path.insert(0, str(ROOT))
from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

CONTENT = {
 "headline": ("AI-First Brand & Marketing Manager · E-Commerce & Quick-Commerce · Key Account Management · "
              "Influencer & Trade Marketing · Multi-Market FMCG · Dubai-based"),
 "professional_summary": (
   "Brand, marketing and commercial professional (4+ yrs, multinational FMCG & e-commerce) based in Dubai. "
   "AI-first — I build Claude/GPT automation for content, campaigns and analytics — with hands-on brand building, "
   "influencer marketing, key account management and quick-commerce growth across 50+ markets (+30% GMV QoQ)."),
 "experience": [
   {"company":"DoFreeze LLC","role":"Brand & Marketing Manager","dates":"Oct 2025 – Present","location":"Dubai, UAE",
    "context":"Multi-brand FMCG group | Befit, Eurocake, Flair | 50+ countries","bullets":[
      "AI-first: built a generative-AI system (Claude/GPT) automating campaign planning, content, research and reporting — cutting ~40% of manual work across 50+ markets",
      "Built and scaled the influencer programme from zero — sourcing, briefing, negotiating and managing 25–50 creators per campaign (paid + organic), plus sampling & seeding to build brand and drive sell-out",
      "Lead brand & NPD end-to-end and grow brands across UAE quick-commerce (Talabat, Noon, Careem, Deliveroo); run paid media on Meta & Google Ads and own the Shopify e-store (CRO)"]},
   {"company":"Miravia (Alibaba Group)","role":"Key Account Manager – Beauty, Fragrances & Fashion","dates":"Nov 2023 – Oct 2025","location":"Madrid, Spain",
    "context":"Top-5 global e-commerce marketplace (Alibaba) | 100K+ employees","bullets":[
      "Owned 42 brand accounts end-to-end on a top-5 marketplace — grew GMV +30% QoQ via pricing, assortment and promotions",
      "Led category expansion (PIC Fragrances) onboarding 30+ brands in two months; owned the Flash Sales channel, reporting to the CEO"]},
   {"company":"Glovo","role":"Account Manager – XL Accounts","dates":"Sep 2022 – Nov 2023","location":"Madrid, Spain",
    "context":"Quick-commerce super-app | €500M+ revenue","bullets":[
      "Managed strategic key accounts and partner activations on a quick-commerce super-app, driving GMV growth and helping build the retail vertical"]},
   {"company":"Mondelez International","role":"Trainee – Category Planning","dates":"Aug 2021 – Aug 2022","location":"Madrid, Spain",
    "context":"Global FMCG multinational | €36B revenue","bullets":[
      "Category planning at a global FMCG — sell-in/sell-out analysis, promo effectiveness and NPD support (Milka Spread, Mini Suchard)"]},
 ],
 "skills_brand":"brand strategy & building, influencer marketing (paid + organic), NPD end-to-end, trade & shopper marketing, sampling & seeding, generative-AI campaigns",
 "skills_ecommerce":"e-commerce & quick-commerce (Talabat, Noon, Careem, Deliveroo), Shopify & CRO, Meta & Google Ads, marketplace management, EDM",
 "skills_commercial":"key account management, distributor & modern trade, negotiation, pricing & assortment, category management",
 "skills_data":"P&L & KPI tracking, ROI/ROAS, sell-in/sell-out, AI-assisted analysis & forecasting, Power BI",
 "skills_tools":"Generative AI (Claude, ChatGPT), Shopify, Meta Ads, Google Ads, Power BI, Salesforce, SAP, MS Office (Expert)",
}

job = Job(id="paula-general-cv", title="General", company="Paula De Francisco",
          location="Dubai, UAE", url="", source="manual", description="", raw={})
docx = cv._fill_template(CONTENT, job)
dest_dir = settings.output_dir / "CV_general"; dest_dir.mkdir(parents=True, exist_ok=True)
dest_docx = dest_dir / "CV_Paula_DeFrancisco.docx"
shutil.move(str(docx), str(dest_docx))
# clean the auto-created job folder
shutil.rmtree(settings.output_dir / "Paula De Francisco - General", ignore_errors=True)
soffice = shutil.which("soffice") or "/Applications/LibreOffice.app/Contents/MacOS/soffice"
subprocess.run([soffice,"--headless","--convert-to","pdf","--outdir",str(dest_dir),str(dest_docx)],check=True,capture_output=True,timeout=180)
dest_docx.unlink(missing_ok=True)
pdf = dest_dir / "CV_Paula_DeFrancisco.pdf"
import pypdf
print("PAGES:", len(pypdf.PdfReader(str(pdf)).pages))
print("PATH:", pdf)
