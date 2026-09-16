"""One-off: paquete de candidatura para E-Commerce Manager en un grupo multimarca de
moda con oficina en Jebel Ali Free Zone (Dubái). Vacante publicada en LinkedIn por
Sonalli Abraham (perfil de RRHH/TA que publica vacantes de varias funciones del grupo).

NOTA DE FIT (bueno — es de los encajes más limpios hasta ahora, ~68/100):
  - Lo que el JD pide y Paula TIENE de verdad:
      * Ownership de DTC: lleva la tienda Shopify de DoFreeze end-to-end (catálogo,
        UX, colecciones, descuentos, checkout) con CRO y AOV como KPIs.
      * Marketplaces desde DENTRO: en Miravia (Alibaba) fue KAM de 42 cuentas de
        beauty/fragancia/moda — pricing, surtido, calidad de listing, participación
        en promociones, campañas de Flash Sales contra objetivos de P&L de canal.
        Conoce las mecánicas de marketplace desde el lado de la plataforma.
      * Marketplaces desde FUERA: en DoFreeze mete marcas en Noon, Talabat, Careem y
        Deliveroo — onboarding, listings, contenido, mecánicas promocionales.
      * Merchandising digital, contenido de producto y calendario promocional.
      * Paid media contra ROAS/CAC (Meta Ads, Google Ads).
      * Stakeholders cross-funcionales: marca/categoría, supply chain y logística,
        y equipo técnico/plataforma.
      * Gestión de equipo real (designer + social media executive).
      * IA aplicada al día a día — el JD lo pide explícitamente y es SU diferencial
        más fuerte: sistema de automatización con Claude para contenido, planificación
        y reporting.
      * Moda: Miravia (cuentas de moda), Glovo (montó el vertical retail onboarding
        marcas de moda y lifestyle) y Massimo Dutti / Inditex al inicio.
  - GAPS que se dejan por escrito y NO se maquillan:
      * Pide 6-10 años; Paula tiene ~5.
      * Pide ownership de P&L completo de las webs DTC. Ella ha trabajado un canal
        contra objetivos de P&L (Miravia Flash Sales) y es dueña del presupuesto
        A&P/trade en DoFreeze — NO se escribe "owned the DTC P&L".
      * Equipo de 4 reportes vs 2 que lleva hoy.
      * Sin experiencia hands-on de Seller/Vendor Central de Amazon, buy-box,
        supresiones de listing ni Namshi/Centrepoint/Ounass/Firstcry. Conoce
        marketplaces, pero no ESOS marketplaces.
      * Forecast: en DoFreeze la e-commerce manager es la dueña del forecast, Paula
        aporta (ver memoria dofreeze-ecommerce-forecast-ownership). Nunca "own forecast".
  - Árabe: no lo tiene y el JD no lo pide. No se menciona.
  - Visa: reside en Dubái con residencia patrocinada por su empresa actual. NUNCA se
    dice "no necesita sponsorship".

Genera CV + carta (plantillas reales, PDF vía LibreOffice) y la guía de outreach a
Sonalli en output/2026-09-16/.
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

COMPANY = "Multi-Brand Fashion Group (JAFZA)"
TITLE = "E-Commerce Manager"
DATE_FOLDER = "2026-09-16"
JOB_ID = "fashion-group-jafza-ecommerce-manager-2026-09"
CONTACT = "Sonalli Abraham"

JOB_DESCRIPTION = """\
E-Commerce Manager — Dubai (office in Jebel Ali Free Zone). Experience: 6-10 years.
Purpose: acquire, convert and retain customers, build the brand, and define and execute
the annual marketing plan across all channels.

Role purpose: own the end-to-end digital commercial performance of 4-5 fashion brands
across marketplaces and the group's DTC websites — driving revenue, profitability and
brand-right online positioning. Acts as business owner for the online channel: full P&L
accountability for the DTC websites, commercial and content stewardship of each brand's
marketplace presence (Centrepoint, Amazon, Namshi, Ounass, Firstcry and similar), and
leadership of a 4-person team covering marketplace operations, digital merchandising,
website performance and fulfilment coordination.

AI-driven approach: embed AI and automation into everyday ecommerce decision-making —
AI-powered demand forecasting, dynamic pricing, listing/content optimisation, personalised
on-site merchandising, AI-driven analytics to flag underperforming listings, pricing gaps
and CX issues early, and automated reporting across marketplaces and DTC.

Key responsibilities:
1. DTC website P&L ownership — revenue, gross margin, digital marketing spend (CAC, ROAS),
   fulfilment/logistics cost, net channel profitability; budgets, forecasts and monthly/
   quarterly business reviews; conversion rate, AOV, repeat purchase rate and CLV;
   promotional calendars, discounting and pricing strategy to protect margin; partner with
   performance marketing on paid and organic acquisition against ROAS and CAC targets.
2. Multi-brand marketplace management — commercial performance across all marketplace
   accounts per brand; pricing strategy, buy-box/visibility health, listing quality,
   catalogue expansion, promotional participation; price parity and brand-right positioning
   to avoid channel conflict; marketplace KPIs (sales, conversion, ratings/reviews, return
   rate, account health) and platform issues (listing suppressions, policy violations);
   evaluate and onboard new marketplace opportunities.
3. Team leadership — lead and develop 4 direct reports across marketplace operations, DTC
   website/trading, digital merchandising & content, and ecommerce fulfilment; set KPIs,
   run performance reviews, allocate workload across 4-5 brands and multiple platforms.
4. Stakeholder and cross-functional management — 3-4 core stakeholder relationships across
   brand/category, marketing, supply chain & warehouse/logistics and IT/tech platform teams;
   align on assortment, pricing architecture and seasonal launches; ensure stock availability,
   delivery SLAs, returns handling and fulfilment cost efficiency; partner with IT on website
   performance, integrations, catalogue feeds and marketplace APIs; represent ecommerce in
   senior leadership and principal/brand-partner reviews with data-led reporting.
5. Digital merchandising, content and customer experience — homepage, category and product-page
   layout, cross-sell/upsell, seasonal campaign execution; product content (imagery, copy,
   sizing, attributes) to brand and platform standards; monitor reviews and service feedback;
   use analytics to identify range gaps, pricing opportunities and CX improvements.
6. Operations, fulfilment and compliance — order management, fulfilment, returns and reverse
   logistics; on-time delivery, cancellation rate, return rate, platform compliance scores;
   marketplace and consumer/ecommerce regulatory compliance; inventory allocation and
   stock-sync accuracy to avoid overselling and stockouts.
"""

ATS = [
    "E-Commerce Manager", "ecommerce manager", "digital commerce", "online business strategy",
    "DTC", "direct-to-consumer", "DTC website", "marketplace management", "multi-brand",
    "fashion", "fashion retail", "apparel", "Amazon", "Namshi", "Ounass", "Centrepoint",
    "Firstcry", "marketplace operations", "seller account", "listing quality", "catalogue expansion",
    "buy-box", "visibility", "listing optimisation", "product content", "price parity",
    "channel conflict", "pricing strategy", "dynamic pricing", "promotional calendar",
    "discounting", "gross margin", "profitability", "P&L", "revenue growth", "budgets",
    "forecasting", "demand planning", "business reviews", "conversion rate", "CRO", "AOV",
    "average order value", "repeat purchase", "customer lifetime value", "CLV", "retention",
    "customer acquisition", "CAC", "ROAS", "performance marketing", "paid media", "Meta Ads",
    "Google Ads", "SEO", "organic acquisition", "digital merchandising", "on-site merchandising",
    "cross-sell", "upsell", "category page", "product detail page", "customer experience",
    "reviews and ratings", "return rate", "account health", "platform compliance",
    "order management", "fulfilment", "reverse logistics", "returns", "delivery SLA",
    "inventory allocation", "stock sync", "stockouts", "overselling", "supply chain",
    "warehouse", "logistics", "catalogue feeds", "integrations", "marketplace API",
    "Shopify", "quick-commerce", "Noon", "Talabat", "Careem", "Deliveroo",
    "team leadership", "people management", "KPIs", "performance reviews",
    "stakeholder management", "cross-functional", "seasonal launches", "assortment",
    "AI", "artificial intelligence", "automation", "AI-driven analytics", "generative AI",
    "automated reporting", "data-led reporting", "GMV", "sell-out", "UAE", "Dubai", "GCC",
]

CV_CONTENT = {
    "headline": "E-Commerce Manager · DTC & Marketplaces · Digital Merchandising · AI-Driven Ecommerce",
    "professional_summary": (
        "E-commerce manager with 5 years running online channels in the UAE and Europe: owns a DTC Shopify store "
        "end-to-end and multi-brand marketplace presence, after managing 42 beauty and fashion accounts inside "
        "Miravia (Alibaba). Leads a team of two and runs ecommerce reporting on AI automation."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & E-Commerce Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG group (Befit, Eurocake, Flair) | Shopify DTC + Noon, talabat, Careem, Deliveroo",
            "bullets": [
                "Own the DTC Shopify store end-to-end — catalogue, product content, collections, cross-sell, discounting and checkout — lifting conversion rate and AOV through data-led digital merchandising",
                "Run multi-brand marketplace presence across Noon, talabat, Careem and Deliveroo: onboarding, listing quality, pricing, promo mechanics and price parity platform by platform",
                "Govern the A&P and trade budget by channel on ROI data, steering Meta and Google Ads against ROAS and acquisition-cost targets, and work with supply chain on availability across channels",
                "Lead a team of two (designer + social media executive); built a Claude-based system automating listing and content optimisation, campaign planning and KPI reporting (-40% manual workload)",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's eCommerce marketplace | 100K+ employees",
            "bullets": [
                "Managed the online commercial performance of 42 beauty, fragrance and fashion accounts: pricing, assortment, listing quality, promotional participation and account health (+30% GMV QoQ)",
                "Owned the Flash Sales channel for Beauty, Fashion & Home against P&L targets, reporting revenue and margin to the CEO; led catalogue expansion with 30+ new stores in two months",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed XL partners (KFC, Taco Bell, Sushi Shop) on assortment, promotions and GMV; helped build the Retail vertical, onboarding fashion and lifestyle brands",
            ],
        },
        {
            "company": "Mondelez International · Massimo Dutti (Inditex)",
            "role": "Trainee, Category Planning · Sales Associate",
            "dates": "2018 – 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG (€36B) | Premium fashion retail",
            "bullets": [
                "Sell-in/sell-out and promotional-effectiveness reporting with Nielsen; fashion retail floor and visual merchandising at Inditex",
            ],
        },
    ],
    "skills_ecommerce": (
        "DTC ownership (Shopify), digital merchandising, CRO & AOV, product content, listings, marketplaces"
    ),
    "skills_brand": (
        "brand strategy, team leadership, stakeholder management (brand, supply chain, IT), launches & GTM"
    ),
    "skills_commercial": (
        "pricing & discounting, price parity, assortment & catalogue expansion, key accounts, negotiation"
    ),
    "skills_data": (
        "P&L targets & margin, conversion & retention, GMV, ROI/ROAS, budget governance, AI-driven reporting"
    ),
    "skills_tools": (
        "Shopify, Meta & Google Ads, Excel, PowerPoint, Power BI, Looker, Salesforce, SAP, Claude (AI), Canva"
    ),
}

CL_PARAGRAPHS = {
    "opening_paragraph": (
        "I am writing about the E-Commerce Manager opening for your fashion portfolio in Dubai. "
        "It reads like the role I have been building towards: owning an online channel end-to-end, "
        "across both a DTC store and a set of marketplaces, for more than one brand at a time."
    ),
    "body_paragraph_1": (
        "At DoFreeze in Dubai I own the DTC Shopify store end-to-end — catalogue and product content, "
        "collections and category pages, cross-sell, discounting and checkout — with conversion rate and "
        "average order value as my KPIs, and I run the brands' presence across Noon, Talabat, Careem and "
        "Deliveroo, managing listings, pricing, promotional mechanics and price parity platform by platform. "
        "I govern the A&P and trade budget, steer Meta and Google Ads against ROAS and acquisition-cost "
        "targets, and work with supply chain and logistics on stock availability and allocation so the "
        "channels do not run dry. I also lead a team of two and am used to being the person who has to "
        "prioritise across brands and platforms when everything is urgent."
    ),
    "body_paragraph_2": (
        "Before Dubai I spent two years inside a marketplace rather than selling on one: as Key Account "
        "Manager at Miravia (Alibaba Group) I managed the commercial performance of 42 beauty, fragrance and "
        "fashion accounts — pricing, assortment, listing quality, promotional participation and account "
        "health — growing GMV +30% quarter on quarter, and I owned the Flash Sales channel for Beauty, "
        "Fashion & Home against P&L targets, reporting to the CEO. That perspective is useful on the other "
        "side of the table: I know what makes a listing win visibility and what gets it suppressed. On the AI "
        "point in your brief, this is genuinely how I work — I built a Claude-based system that automates "
        "listing and content optimisation, campaign planning and KPI reporting across markets, cutting manual "
        "workload by around 40%."
    ),
    "closing_paragraph": (
        "To be straightforward: I have five years of experience rather than six to ten, my team today is two "
        "people rather than four, and my P&L accountability has been at channel and budget level rather than "
        "full DTC P&L ownership. What I bring instead is an unusually complete hands-on span — DTC trading, "
        "marketplace operations, digital merchandising, paid media and stock coordination — in this market, "
        "already living in Dubai. I would welcome the chance to talk it through."
    ),
}


def make_job() -> Job:
    return Job(
        id=JOB_ID,
        title=TITLE,
        company=COMPANY,
        location="Jebel Ali Free Zone, Dubai, United Arab Emirates",
        url="https://www.linkedin.com/in/sonalli-abraham-5343391a3/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={
            "query": "E-Commerce Manager Dubai fashion multi-brand",
            "posted_by": f"{CONTACT} (LinkedIn hiring post)",
            "portfolio": "4-5 fashion brands, DTC websites + marketplaces",
            "team": "4 direct reports",
            "experience_required": "6-10 years",
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
        "ai_score": 68,
        "ai_tier": "Good fit",
        "skills_match": [
            "Ownership real de una tienda DTC (Shopify end-to-end: catálogo, colecciones, UX, descuentos, checkout) con CRO y AOV",
            "Merchandising digital y contenido de producto — el corazón del bloque 5 del JD",
            "Marketplaces desde dentro: 42 cuentas en Miravia (Alibaba) — pricing, surtido, calidad de listing, promociones, account health",
            "Marketplaces desde fuera: onboarding y gestión de Noon, Talabat, Careem y Deliveroo en DoFreeze",
            "Paid media contra ROAS y coste de adquisición (Meta Ads, Google Ads)",
            "Canal contra objetivos de P&L reportando a CEO (Miravia Flash Sales) + gobierno de presupuesto A&P y trade",
            "Gestión de equipo (designer + social media executive) y de prioridades entre marcas y plataformas",
            "Stakeholders cross-funcionales: marca/categoría, supply chain y logística, equipo de plataforma",
            "IA en el día a día — el JD lo pide explícitamente y es su diferencial más fuerte (sistema con Claude para contenido, planificación y reporting)",
            "Moda: cuentas de moda en Miravia, vertical retail de Glovo (onboarding de marcas de moda) y Massimo Dutti / Inditex",
        ],
        "missing_skills": [
            "Piden 6-10 años; Paula tiene ~5",
            "Ownership de P&L completo de las webs DTC (revenue, margen, coste logístico, beneficio neto de canal) — su P&L ha sido de canal y de presupuesto A&P, no de marca/web completa",
            "Equipo de 4 reportes vs 2 que lleva hoy",
            "Sin hands-on de Amazon Seller/Vendor Central, buy-box, supresiones de listing ni de Namshi / Centrepoint / Ounass / Firstcry en concreto",
            "Sin ownership de fulfilment, devoluciones y logística inversa (coordina con supply chain, no lo dirige)",
            "Sin experiencia específica en compliance regulatorio de e-commerce por plataforma",
        ],
        "sector_fit": "bueno (moda multimarca + marketplaces; ella viene de beauty/moda en Miravia, retail en Glovo/Inditex y FMCG en DoFreeze, siempre con canal online)",
        "seniority_fit": "ligeramente por debajo (5 años vs 6-10; equipo de 2 vs 4) pero el título de Manager y el scope de canal sí coinciden",
        "red_flags": [
            "Jebel Ali Free Zone — commute largo desde la mayoría de zonas residenciales de Dubái; conviene confirmar ubicación y horario",
            "Anuncio publicado por RRHH sin nombre de empresa; hay que identificar el grupo antes de comprometerse",
            "'Full P&L accountability' puede ser un filtro duro en entrevista — preparar la respuesta honesta de canal vs marca",
            "Rango salarial no publicado; verificar que supera el suelo de 20.000 AED/mes",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Uno de los encajes más limpios del pipeline. El JD es un rol de dueño del canal online para 4-5 "
            "marcas de moda: P&L de las webs DTC, gestión comercial y de contenido en marketplaces (Amazon, "
            "Namshi, Centrepoint, Ounass, Firstcry), equipo de 4 y stakeholders de supply chain e IT, con una "
            "insistencia explícita en usar IA en la toma de decisiones diaria. Paula cubre de verdad el bloque "
            "de DTC (Shopify end-to-end, CRO, AOV, merchandising, contenido, descuentos), el de marketplaces "
            "(42 cuentas gestionadas desde dentro de Miravia + onboarding de Noon/Talabat/Careem/Deliveroo "
            "desde el lado marca), el de paid media contra ROAS/CAC, el de stakeholders y el de equipo. El "
            "punto de IA es donde saca ventaja frente a un candidato de e-commerce clásico. Los gaps se "
            "escriben tal cual y se declaran también en la carta: 5 años vs 6-10, equipo de 2 vs 4 y P&L de "
            "canal/presupuesto en vez de P&L completo de las webs. No se dice 'owned the DTC P&L', ni se "
            "atribuye ownership del forecast de DoFreeze (es de la e-commerce manager; Paula aporta), ni se "
            "inventa Amazon Seller Central, Namshi, Ounass, Centrepoint ni Firstcry. Árabe no aparece: no lo "
            "tiene y el JD no lo pide. Visa: se indica residencia en Dubái, nunca 'no necesita sponsorship'."
        ),
        "scored_by": "manual:claude",
        "freshness": "fresh",
        "discovered_at": f"{DATE_FOLDER}T00:00:00+00:00",
        "status": "Reviewing",
    })
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")


OUTREACH_MD = f"""# Outreach — {CONTACT} (publica la vacante en LinkedIn)

**Rol:** E-Commerce Manager — grupo multimarca de moda, oficina en Jebel Ali Free Zone, Dubái
**Origen:** post de LinkedIn de {CONTACT} ("HIRING | E-commerce Manager | Dubai")
**Perfil:** https://www.linkedin.com/in/sonalli-abraham-5343391a3/
**Gancho central:** Paula ha gestionado marketplaces **desde los dos lados** — dentro de Miravia (Alibaba), llevando 42 cuentas de beauty y moda, y desde la marca, metiendo productos en Noon, Talabat, Careem y Deliveroo — y hoy es dueña de una tienda DTC en Shopify end-to-end. Más el punto de IA, que el JD pide explícitamente.

---

## Orden recomendado

1. **Aplicar por el link del post** (el JD dice "apply directly through the link below"). El CV está listo.
2. **Nota de conexión a {CONTACT}** el mismo día, mencionando que ya ha aplicado.
3. Si acepta, **mensaje largo**.
4. Comentario en el post solo si quieres visibilidad extra (opcional).

---

## 1) Nota de conexión de LinkedIn
*286 caracteres · cabe en el límite de 300*

> Hi Sonalli — I've just applied to the E-Commerce Manager role you posted. Quick context: I run a DTC Shopify store end-to-end in Dubai and previously managed 42 beauty and fashion accounts inside Miravia (Alibaba), so I know marketplaces from both sides. Would love to connect.

---

## 2) Mensaje largo (tras aceptar la conexión)

> Hi Sonalli, thanks for connecting — and thanks for putting the E-Commerce Manager role out there with so much detail on the scope.
>
> I applied through the link, but wanted to give you the short version directly.
>
> Today I lead Brand & E-Commerce at DoFreeze here in Dubai: I own the DTC Shopify store end-to-end — catalogue, product content, collections, cross-sell, discounting, checkout — with conversion rate and AOV as my KPIs, and I run the brands' presence across Noon, Talabat, Careem and Deliveroo, managing listings, pricing, promo mechanics and price parity platform by platform. I also steer Meta and Google Ads against ROAS and acquisition-cost targets, and I lead a team of two.
>
> Before Dubai I was on the other side of the marketplace: at Miravia (Alibaba Group) I managed the commercial performance of 42 beauty, fragrance and fashion accounts — pricing, assortment, listing quality, promotional participation, account health — growing GMV +30% quarter on quarter, and owned the Flash Sales channel for Beauty, Fashion & Home against P&L targets, reporting to the CEO.
>
> One thing that caught my eye is the AI part of the brief, because that's genuinely how I work: I built a Claude-based system that automates listing and content optimisation, campaign planning and KPI reporting across markets, and it cut our manual workload by around 40%.
>
> Where I'm honest: I have five years rather than six to ten, and my team today is two rather than four. What I'd bring is an unusually complete hands-on span across DTC trading, marketplace operations, merchandising and paid media — in this market.
>
> Happy to send my CV or jump on a quick call whenever suits you. Also, if you can share which group this is and the salary range, that would help me make sure I'm the right fit before taking your time.
>
> Best,
> Paula De Francisco
> +971 50 386 3656 · paulich98@hotmail.com

---

## 3) Comentario público en el post (opcional)

> Great scope on this one — DTC and marketplaces under the same owner is where the interesting work is. Applied, and sent you a message, Sonalli 🙌

---

## Preguntas que conviene resolver pronto (no en el primer mensaje)

- **¿Qué grupo es?** El post no nombra la empresa. Marketplaces citados (Centrepoint, Namshi, Ounass, Firstcry) apuntan a un distribuidor/agente de marcas de moda y kids con oficina en JAFZA. Confirmar antes de invertir en entrevistas.
- **Rango salarial:** no publicado. Suelo de Paula: 20.000 AED/mes.
- **Jebel Ali Free Zone:** confirmar días de oficina y commute.
- **Los 4 reportes:** entender si ya existen o hay que construir el equipo.

---

## Cómo responder al hueco de "full P&L accountability" (prepárarlo)

> "I've carried channel P&L targets rather than a full website P&L: at Miravia I ran the Flash Sales channel for Beauty, Fashion & Home against revenue and margin targets, reporting contribution to the CEO, and at DoFreeze I govern the A&P and trade budget and track channel profitability by platform. Owning the full DTC P&L line by line — including fulfilment cost and net channel profit — would be a step up, and it's the step I'm looking for."

Nunca decir "I owned the DTC P&L".

---

## Notas operativas

- **Email:** no lo tenemos y no se conoce la empresa — **no inventar dominio**. Canal: LinkedIn + el link de aplicación del post.
- **Árabe:** el JD no lo pide. No mencionarlo.
- **Visado:** reside en Dubái con residencia patrocinada por su empresa actual. No decir "no sponsorship needed".
- **Entregables:** `01_CV_y_Carta/` (CV + carta en PDF).
"""


def _to_pdf_soffice(docx_path: Path) -> Path:
    """DOCX -> PDF headless con LibreOffice (docx2pdf/Word falla en este Mac)."""
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

    cv_docx = cv._fill_template(CV_CONTENT, job)
    cv_pdf = _to_pdf_soffice(cv_docx)
    print("OK_CV", cv_pdf)

    cl_docx = cl._fill_template(CL_PARAGRAPHS, job, CONTACT)
    cl_pdf = _to_pdf_soffice(cl_docx)
    print("OK_CL", cl_pdf)

    final_dir = _relocate_to_dated_folder(cv_pdf.parent.parent)
    outreach_dir = final_dir / "02_Outreach"
    outreach_dir.mkdir(parents=True, exist_ok=True)
    (outreach_dir / f"Outreach_{CONTACT.replace(' ', '_')}.md").write_text(
        OUTREACH_MD, encoding="utf-8"
    )
    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
