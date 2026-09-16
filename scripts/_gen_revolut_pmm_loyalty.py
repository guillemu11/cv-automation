"""One-off: Paula's CV for **Product Marketing Manager (Loyalty)** at **Revolut** —
full-time, remote, based in the United Arab Emirates. Indeed listing; the header says
"Product Marketing Manager (Loyalty)" while the body asks for a *Senior* PMM. Comp is
published for Poland only (PLN 24,700-29,100 gross/month); other locations "discussed
during the interview process".

The brief: drive PROFITABILITY through loyalty product adoption and engagement — own
upgrade strategies and build a marketing strategy focused on customer lifetime value.
Positioning-to-launch across channels and markets, value propositions and narratives,
cross-functional work with Product/Design/Comms, and segmentation + conversion
optimisation off customer-behaviour analysis.

This is the fourth Revolut package (after PMM core, PMM Crypto and Marketing Manager
Brand). Different team within Growth, so applying to several does not penalise — but
the angle here is deliberately distinct: LOYALTY, REPEAT and TRADING UP, not
category education (Crypto) or main-account usage (core).

Paula's honest angle:
- SHE HAS ACTUALLY BUILT A LOYALTY PROGRAMME. Beauty Club at Miravia was hers, created
  from scratch on a newly launched Alibaba marketplace explicitly to drive customer
  loyalty and repeat purchase — alongside Hot on Social. That is the single most
  on-brief thing in her CV for this role, and it is real.
- ENGAGEMENT AND REPEAT ARE HER METRICS. GMV, conversion, AOV, repeat and retention
  across 42 accounts (+30% GMV QoQ) — the shape of an LTV problem, expressed in
  commercial rather than fintech language.
- PRODUCT MARKETING IS HER DAY JOB IN FMCG LANGUAGE: 6 launches end-to-end — insight,
  positioning, value proposition, pricing, messaging, launch phasing — orchestrated
  across channels AND geographies (GCC, MENA, Asia, Europe, USA, Africa), which is the
  JD's "orchestrating product launches across markets... highlighting what sets each
  country apart".
- TRADING UP IS FAMILIAR, IN RETAIL FORM: premium assortment and pricing work in
  beauty and fragrances (onboarding the official distributors of Arabian Oud, Lattafa,
  Swiss Arabian, Ajmal), promotional mechanics designed to lift AOV and basket value.
- SEGMENTATION AND CUSTOMER BEHAVIOUR: category and customer analysis feeding
  assortment, promo and channel decisions; feedback loops turned into launch read-outs.
- CROSS-FUNCTIONAL AND CHANNEL BREADTH: in-product/onsite merchandising, digital
  (Meta/Google/CRM-EDM), creators and earned media, and genuine offline activation.
- PROOF OF WORK: she already built and deployed a full fictional Revolut campaign,
  "No Borders" (https://guillemu11.github.io/revolut-no-borders/) — answers the
  originality/creative-excellence bar in one link.

Honesty guardrails (NO fabrication):
- ZERO fintech, payments, banking or regulated financial product. The JD asks for
  "knowledge of loyalty markets and the competitive landscape in fintech or payments"
  as a REQUIREMENT. Not claimed anywhere.
- She has NOT driven premium/subscription tier upgrades (Revolut Premium/Metal-style
  paid-plan adoption). Her "trading up" is retail assortment and basket value, not
  subscription upgrade funnels. Never phrased as premium-plan adoption.
- LTV/CLV is not a metric she has formally owned — the CV says repeat and retention,
  which is what she genuinely measures.
- PR is her weakest channel: earned media and creator work, phrased as
  "communications planning", never orchestrated PR at Revolut's scale.
- No formal PMM title; PMM work sits inside brand/e-commerce/KAM roles. Years stated
  honestly.
- NO "no sponsorship needed" claim (standing rule). NO Arabic claim.

ONE-PAGE standard: 3/2/1/1 bullets, compact skills rows, verified page count.
Relabels the skills rows for this role, converts via LibreOffice, registers the job,
drops a short-named portal copy and an outreach note, lands under output/2026-09-16/.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from docx import Document

from career_ops.config import settings
from career_ops.discovery.normalize import Job
from career_ops.generators import cv_generator as cv

COMPANY = "Revolut"
TITLE = "Product Marketing Manager (Loyalty)"
DATE_FOLDER = "2026-09-16"

JOB_DESCRIPTION = """\
Product Marketing Manager (Loyalty) — Revolut. Full-time. Remote, based in the United Arab
Emirates. (Listing header says Product Marketing Manager; the body asks for a Senior Product
Marketing Manager.)

About Revolut: 80+ million customers, 13,000+ people, products across spending, saving,
investing, exchanging and travelling. Marketing at Revolut is about clarity, creativity and
commercial impact; the Growth team turns bold ideas into campaigns that connect with millions.

About the role: a Senior Product Marketing Manager to drive profitability through loyalty
product adoption and engagement. You'll lead upgrade strategies and build a high-performing
marketing strategy focused on providing customer lifetime value.

What you'll be doing:
- Immersing yourself in understanding customers' needs and how loyalty products work globally,
  using data-driven insights to shape strategy.
- Designing the loyalty product marketing strategy across channels, from positioning to launch
  campaigns.
- Crafting compelling value propositions and narratives that showcase benefits, working with
  creative teams to bring them to life.
- Orchestrating product launches across markets, ensuring consistent messaging and positioning
  whilst highlighting what sets each country apart.
- Fostering solid cross-functional partnerships with Product, Design and Communications to
  maximise product awareness and adoption.
- Analysing customer behaviour and market trends to identify segmentation opportunities and
  optimise conversion strategies.

What you'll need:
- Experience in either B2B or B2C product, brand or consumer marketing in a fast-paced
  environment (preferably in a hyper-growth tech company).
- Experience driving premium product adoption.
- Knowledge of loyalty markets and the competitive landscape in fintech or payments.
- Expertise in setting strategic direction and project managing complex go-to-market campaigns
  requiring input and execution from various teams.
- Experience generating highly original ideas and setting the standard for creative excellence
  while maintaining brand integrity.
- A track record in consumer marketing and an understanding of channels such as in-product,
  digital, PR and offline activations.
- Excellent communication and interpersonal skills; a charismatic people-person able to work in
  a dynamic, international environment.
- An exceptional eye for detail and quality.

Compensation: Poland PLN 24,700-29,100 gross monthly; other locations discussed during the
interview process. Apply only through official Revolut channels (@revolut.com domains).
"""

ATS = [
    "product marketing", "product marketing manager", "senior product marketing manager", "PMM",
    "loyalty", "loyalty programme", "loyalty program", "rewards", "membership",
    "premium product adoption", "upgrade strategy", "trading up", "subscription",
    "customer lifetime value", "LTV", "CLV", "profitability", "engagement", "adoption",
    "repeat purchase", "retention", "churn", "segmentation", "customer behaviour",
    "conversion optimisation", "conversion strategies", "cohort analysis",
    "go-to-market", "GTM", "launch strategy", "product launch", "positioning", "messaging",
    "value proposition", "narrative", "creative brief", "creative excellence", "brand integrity",
    "consumer marketing", "brand marketing", "B2C", "B2B", "campaign strategy",
    "multi-market", "international", "geographies", "localisation", "market trends",
    "cross-functional", "Product", "Design", "Communications", "stakeholder management",
    "project management", "in-product", "onsite merchandising", "digital", "paid social",
    "Meta Ads", "Google Ads", "CRM", "EDM", "PR", "earned media", "influencer marketing",
    "UGC", "offline activations", "sampling", "retail execution", "modern trade",
    "data-driven", "customer insight", "KPI", "ROI", "ROAS", "GMV", "AOV", "A/B testing",
    "hyper-growth", "fast-paced", "marketplace", "platform", "e-commerce", "Shopify",
    "UAE", "Dubai", "remote", "generative AI",
]

CONTENT = {
    "headline": (
        "Product Marketing & Go-to-Market · Loyalty and Repeat Purchase · "
        "Multi-Market Launches · Hyper-Growth Platforms"
    ),
    "professional_summary": (
        "Consumer product marketer with 5 years across hyper-growth platforms (Alibaba's Miravia, Glovo) "
        "and global consumer brands. Built a loyalty programme from scratch to drive repeat purchase, and "
        "owns launches end-to-end — insight, positioning, value proposition, channel plan — across 50+ "
        "markets. Dubai-based, available remote."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Consumer brands (Befit, Eurocake, Flair) | 50+ markets | D2C, marketplaces & retail",
            "bullets": [
                "Own product marketing end-to-end for 6 launches — customer insight, positioning and value proposition, pricing, messaging and launch phasing — orchestrated across channels and geographies, adapting the story to what makes each market different",
                "Run every channel against one narrative: in-product/onsite merchandising on Shopify (CRO, AOV), paid social and Google Ads, CRM/EDM, 25–50 creators briefed per campaign, and offline activation via sampling, seeding and retail execution",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba Group's marketplace launch in Spain | Hyper-growth global tech | 100K+ employees",
            "bullets": [
                "Created the Beauty Club loyalty programme and Hot on Social from scratch on a newly launched marketplace — designing the proposition, benefits narrative and channel plan to lift customer loyalty, repeat purchase and engagement",
                "Grew 42 accounts +30% GMV QoQ through pricing, premium assortment and promotional mechanics built to raise basket value, analysing customer behaviour and conversion to decide where to push",
                "Owned the Flash Sales channel for Beauty, Fashion and Home reporting to the CEO, and led premium category expansion as PIC Fragrances (30+ stores in two months, including the official Arabian Oud, Lattafa, Swiss Arabian and Ajmal distributors)",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce platform | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped build Glovo's retail vertical from zero — taking a food-delivery app into fashion, beauty and non-food — and ran launch activations with strategic partners (KFC, Taco Bell, Sushi Shop)",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | Category planning & analytics",
            "bullets": [
                "Measured launch and promotional performance for the chocolate category and fed the read-outs into NPD decisions (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": (  # label -> "Product Marketing & GTM"
        "go-to-market strategy, product launches end-to-end, positioning & value propositions, "
        "benefit narratives, loyalty & engagement programmes, pricing"
    ),
    "skills_ecommerce": (  # label -> "Channels & Creative"
        "in-product & onsite merchandising, paid social (Meta), Google Ads, CRM/EDM, "
        "creator & UGC programmes, communications planning, offline activations"
    ),
    "skills_commercial": (  # label -> "Markets & Stakeholders"
        "50+ markets across 6 regions, cross-functional leadership (product, design, comms), "
        "partner management, marketplace & quick-commerce platforms, C-level reporting"
    ),
    "skills_data": (  # label -> "Customer & Data"
        "customer behaviour & segmentation, repeat and retention analysis, conversion optimisation, "
        "ROI, ROAS, GMV, AOV, A/B testing, launch read-outs"
    ),
    "skills_tools": (  # label -> "Tools"
        "Power BI, Tableau, Looker, Google Analytics, Meta Ads Manager, Salesforce, Shopify, "
        "Adobe, Canva, Generative AI (Claude, ChatGPT)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Product Marketing & GTM",
    "E-Commerce & Digital": "Channels & Creative",
    "Commercial": "Markets & Stakeholders",
    "Data & Analytics": "Customer & Data",
}

OUTREACH = """\
# Outreach — Revolut · Product Marketing Manager (Loyalty)

**Rol:** PMM (Loyalty) · Remoto **con base en EAU** · Indeed. El encabezado dice "Product Marketing
Manager"; el cuerpo pide un **Senior** PMM — conviene asumir vara de senior.
**Salario:** solo publicado para Polonia (PLN 24.700–29.100 brutos/mes). Para EAU se negocia en
proceso → **confirmar contra el suelo de 20.000 AED/mes antes de invertir tiempo**.
**Aplicar:** únicamente por canales oficiales de Revolut (@revolut.com). La propia oferta avisa de
estafas de reclutamiento.

## Es la cuarta de Revolut — y la mejor de las cuatro

Ya hay paquete de **PMM (core)** y **PMM (Crypto)** (3-sep) y de **Marketing Manager (Brand)**
(20-ago). Equipos distintos dentro de Growth, así que no penaliza. Pero esta es **la que mejor
encaja de verdad**, por una razón concreta: **Paula ha construido un programa de fidelización de
cero**. El Beauty Club de Miravia era suyo, inventado en un marketplace recién lanzado, con el
objetivo explícito de repetición y lealtad. Eso no es un paralelismo forzado: es literalmente el
producto que este rol comercializa.

## El diferenciador que ya existe

**"No Borders"** — campaña Revolut completa, desplegada y navegable:
https://guillemu11.github.io/revolut-no-borders/
La JD pide "generating highly original ideas" y "creative excellence while maintaining brand
integrity". El link responde a ambas en 10 segundos. Va en la primera línea del mensaje, nunca como
adjunto.

## Referral, otra vez

En Revolut el referral pesa más que el ATS. Antes de aplicar: abrir la oferta en LinkedIn → lista de
"Personas con las que puedes hablar" (en las anteriores aparecía Alejandro y otros de su red) →
pedir referencia.

## Ángulo en la aplicación

1. **Loyalty, con receta propia.** Beauty Club + Hot on Social, creados desde cero para subir
   repetición y engagement en una plataforma joven.
2. **Lanzamientos multi-mercado.** 6 lanzamientos end-to-end orquestados por canal **y por
   geografía**, adaptando la historia a lo que diferencia cada mercado — frase casi literal de la JD.
3. **Subir el ticket.** Surtido premium, pricing y mecánicas promocionales para levantar AOV y
   valor de cesta; expansión de categoría premium en fragancias.
4. **Los cuatro canales que pide.** in-product/onsite, digital, earned media/creadores y **offline**
   — este último es donde casi ningún PMM de tech tiene nada y ella sí.
5. **Cross-functional.** Trabajo con producto, diseño y comunicación; reporting a CEO en Miravia.

## Lo que NO se dice

- **Cero fintech, pagos o banca.** "Knowledge of loyalty markets and the competitive landscape in
  fintech or payments" está en **requisitos**. No se maquilla. Se compensa llegando a la entrevista
  con lectura propia de Revolut Premium/Metal/RevPoints frente a Wise, Monzo, N26 y, en EAU, Wio,
  Mashreq Neo y e& money.
- **No ha llevado adopción de planes premium de suscripción.** Su "trading up" es surtido y cesta
  en retail, no funnels de upgrade a un tier de pago. El CV no lo insinúa.
- **LTV/CLV no es una métrica que haya poseído formalmente** — el CV dice repetición y retención,
  que es lo que sí mide.
- **PR de gabinete a escala Revolut, no.** Earned media y creadores; en el CV va como
  "communications planning".
- **Nunca "no necesito sponsorship".** Visado de residencia EAU pagado por su empresa actual.
- **Sin árabe.**

## Riesgos

- Vara de **senior** en el cuerpo de la oferta, con 5 años de experiencia.
- El requisito de landscape de loyalty en fintech/pagos es real y no lo tiene.
- Revolut filtra por pedigrí y el proceso es largo (varias rondas + case study).
- Salario sin publicar para EAU.
- Remoto, fuera de su preferencia declarada — aunque con base en EAU, que es lo que quiere.
"""


def make_job() -> Job:
    return Job(
        id="revolut-product-marketing-manager-loyalty-uae-remote-2026-09",
        title=TITLE,
        company=COMPANY,
        location="United Arab Emirates (Remote)",
        url="https://www.revolut.com/careers/",
        source="indeed",
        description=JOB_DESCRIPTION,
        raw={
            "query": "Revolut Product Marketing Manager Loyalty remote UAE",
            "note": (
                "Indeed listing; header says PMM, body asks for a Senior PMM. Remote, based in the UAE. "
                "Comp published for Poland only (PLN 24,700-29,100 gross/month); UAE discussed in process "
                "— confirm against the AED 20K/month floor. Apply ONLY via revolut.com/careers (the JD "
                "warns about recruitment scams). Fourth Revolut package after PMM core, PMM Crypto and "
                "Marketing Manager Brand — different Growth team, and the best substantive fit of the four "
                "because Paula actually built a loyalty programme (Beauty Club at Miravia) from scratch. "
                "Real gap: loyalty/fintech/payments competitive-landscape knowledge is a stated requirement "
                "and she has none; she has also never driven premium subscription-tier adoption. Revolut is "
                "a stated priority target for Paula. Deployed Revolut campaign 'No Borders' available as "
                "proof of work."
            ),
        },
    )


def register_in_dashboard(job: Job) -> None:
    path = settings.data_dir / "scored_jobs.json"
    if not path.exists():
        return
    jobs = json.loads(path.read_text(encoding="utf-8"))
    if any(j.get("id") == job.id for j in jobs):
        return
    jobs.insert(0, {
        "id": job.id, "title": job.title, "company": job.company, "location": job.location,
        "url": job.url, "source": job.source, "description": job.description,
        "salary_raw": "PLN 24,700-29,100 gross/month (Poland); UAE not published",
        "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 75, "ai_tier": "Warm",
        "skills_match": [
            "She has genuinely built a loyalty programme: Beauty Club (plus Hot on Social) created from scratch on Alibaba's newly launched Miravia marketplace to drive repeat purchase, loyalty and engagement — the most on-brief item in her CV and entirely real",
            "Engagement/repeat metrics rather than awareness metrics: GMV, conversion, AOV, repeat and retention across 42 accounts (+30% GMV QoQ) — an LTV-shaped problem in commercial language",
            "Product marketing end-to-end in FMCG language: 6 launches (insight, positioning, value proposition, pricing, messaging, phasing) orchestrated across channels AND geographies, adapted per market — the JD's exact phrasing",
            "Trading up in retail form: premium assortment, pricing and promo mechanics to lift basket value; led premium fragrance category expansion (Arabian Oud, Lattafa, Swiss Arabian, Ajmal distributors)",
            "Segmentation and customer-behaviour analysis feeding assortment, promo and channel decisions; launch read-outs as feedback loops",
            "All four channels the JD lists, including the one most tech PMMs lack: in-product/onsite, digital (Meta/Google/CRM-EDM), creators and earned media, and real offline activation",
            "Hyper-growth tech twice: Miravia was Alibaba's new marketplace launch in Spain; Glovo built its retail vertical from zero",
            "Already built and deployed a full fictional Revolut campaign ('No Borders') — answers the originality and creative-excellence bar in one link",
            "Revolut is a stated priority target, so 'a passion for Revolut's products' is credible here",
        ],
        "missing_skills": [
            "No knowledge of loyalty markets or the fintech/payments competitive landscape — listed as a REQUIREMENT, not a nice-to-have",
            "Has never driven premium subscription-tier adoption (Revolut Premium/Metal-style upgrades); her trading-up experience is retail assortment and basket value, not paid-plan upgrade funnels",
            "LTV/CLV has not been a formally owned metric — she measures repeat and retention",
            "No fintech, payments, banking or regulated financial product experience at all",
            "No formal PMM title; product-marketing work sits inside brand, e-commerce and KAM roles",
            "PR is her weakest listed channel — earned media and creators, not orchestrated PR at Revolut's scale",
        ],
        "sector_fit": "adjacent — consumer product marketing, loyalty-programme building and hyper-growth platforms hit directly; fintech/payments and the loyalty competitive landscape are entirely new and explicitly required",
        "seniority_fit": "stretch-to-on-band — the body of the ad asks for a SENIOR PMM and she has 5 years with no formal PMM title, though the work itself matches",
        "red_flags": [
            "Body of the ad asks for a Senior Product Marketing Manager while the header says PMM — assume a senior bar",
            "Loyalty + fintech/payments landscape knowledge sits in the requirements list and she has none",
            "Premium subscription-tier adoption is an explicit requirement she cannot claim",
            "No salary published for the UAE — confirm against the AED 20K/month floor before investing time",
            "Revolut screens hard on pedigree and runs a long multi-stage process with a case study",
            "Apply only via revolut.com/careers; the JD explicitly warns about recruitment scams",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "The best substantive fit of the four Revolut packages so far, for one concrete reason: Paula has "
            "actually built a loyalty programme. Beauty Club at Alibaba's Miravia was hers, created from "
            "scratch on a newly launched marketplace to drive repeat purchase and engagement — this role "
            "markets exactly that kind of product. Around it sits the rest of the brief in real form: launches "
            "owned end-to-end from insight through positioning, value proposition and channel plan, "
            "orchestrated across 50+ geographies with the story adapted per market; repeat/retention/AOV as "
            "her working metrics rather than awareness; premium assortment and promo mechanics that raise "
            "basket value; customer-behaviour analysis driving segmentation and conversion decisions; and all "
            "four channels the JD names, including offline activation, where FMCG beats most tech PMMs. The "
            "deployed 'No Borders' Revolut campaign answers the originality bar directly. The gaps are real "
            "and stated: no fintech or payments exposure and no read on the loyalty competitive landscape "
            "(both explicit requirements), no premium subscription-tier upgrade experience, and LTV is not a "
            "metric she has formally owned. The body of the ad also asks for a Senior PMM. A referral is what "
            "decides whether this gets read."
        ),
        "scored_by": "manual:claude", "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00", "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


def _relabel_for_role(docx_path: Path) -> None:
    doc = Document(str(docx_path))
    for table in doc.tables:
        for row in table.rows:
            first = row.cells[0]
            new = ROLE_LABELS.get(first.text.strip())
            if not new:
                continue
            para = first.paragraphs[0]
            if para.runs:
                para.runs[0].text = new
                for r in para.runs[1:]:
                    r.text = ""
            else:
                para.add_run(new)
    doc.save(str(docx_path))


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

    cv_docx = cv._fill_template(CONTENT, job)
    _relabel_for_role(cv_docx)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    pos_dir = cv_pdf.parent.parent
    final_dir = _relocate_to_dated_folder(pos_dir)

    final_cv = final_dir / "01_CV_y_Carta" / cv_pdf.name
    short = final_dir / "01_CV_y_Carta" / "Paula De Francisco - CV.pdf"
    if final_cv.exists():
        shutil.copy(str(final_cv), str(short))
        print("OK_SHORT", short)

    outreach_dir = final_dir / "03_Outreach"
    outreach_dir.mkdir(parents=True, exist_ok=True)
    (outreach_dir / "Outreach.md").write_text(OUTREACH, encoding="utf-8")
    print("OK_OUTREACH", outreach_dir / "Outreach.md")

    try:
        from pypdf import PdfReader
        n = len(PdfReader(str(final_cv)).pages)
        print(f"PAGES {n}", "OK" if n == 1 else "!! SPILLS")
    except Exception as exc:  # noqa: BLE001
        print("page-count check skipped:", exc)

    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
