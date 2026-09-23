"""One-off: CV de una página para **Brand Executive** en **Frío Sparkling Water**
(Dubai; marca de bebidas con planta propia en EAU — agua con gas, cola y nuevos sabores;
~1.500 tiendas, cafés y restaurantes, e-commerce y tienda online propia; equipo de 2-10,
se trabaja directamente con el fundador).

Pide el JD: rol 100% hands-on — planificar el calendario mensual/trimestral con el fundador
y ejecutarlo; crear y publicar contenido (posts, reels, fotos de producto, material en tienda);
campañas de pago en Meta, TikTok y Google midiendo coste y retorno; apoyar lanzamientos de
producto de la idea al lineal (naming, feedback de packaging, plan de lanzamiento, material
retail); hacer crecer la tienda online (email, ofertas, suscripciones, recurrencia); trabajar
con partners de retail y cafés en activaciones, sampling y displays; briefear y gestionar
freelancers, fotógrafos y agencias; mantener todo dentro de las brand guidelines; reportar
resultados cada mes en números simples.
Requisitos: 2+ años de marketing/marca en EAU; prueba de campañas llevadas de punta a punta;
manos en contenido social, paid ads y herramientas de diseño (Canva, Adobe); buen inglés
(árabe es un plus fuerte); creativa, organizada y dispuesta a ejecutar ella misma; residente
en EAU y presencial en Dubái. Nice to have: FMCG, bebidas, food o retail; Shopify; edición de vídeo.

Ángulo de Paula: encaje casi literal. Hoy en DoFreeze (grupo FMCG de EAU: Befit, Eurocake,
Flair) lleva marca + contenido + Meta/Google Ads + Shopify + lanzamientos + retail y talabat/
Careem, con equipo de dos y 4 agencias. Es exactamente el perfil "lo planeo y lo ejecuto yo".

Guardarraíles de honestidad:
- Paid hands-on: **Meta Ads y Google Ads (Search & Display)**. TikTok e Instagram sólo como
  contenido orgánico — NO se reclama TikTok Ads.
- Árabe: NO lo tiene (el JD lo pide como "strong plus", no como requisito) — nunca insinuarlo.
- Forecast: contribuye con Sales/Finance, no es dueña.
- Visa: sólo "UAE Residence Visa"; nunca "no sponsorship needed".
- Nivel: el puesto es Executive y ella es Manager — el CV se posiciona como operadora
  hands-on, no como jefa de equipo grande.
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

COMPANY = "Frio Sparkling Water"
TITLE = "Brand Executive"
DATE_FOLDER = "2026-09-22"

JOB_DESCRIPTION = """\
Brand Executive — Frio Sparkling Water, Dubai, UAE. On-site, full time.
FRIO is a Dubai beverage brand. We make sparkling water, cola and new flavours in our own plant in the
UAE. We sell in about 1,500 stores, plus cafes and restaurants, e-commerce, and our own online shop.
We are a small team. You will work directly with the founder. This is a hands-on role: you will plan the
marketing and then do it yourself.
Responsibilities: plan the monthly and quarterly marketing calendar with the founder, then run it;
create and publish content — social posts, reels, product photos, in-store material; run paid campaigns
on Meta, TikTok and Google, tracking what each campaign costs and what it brings back; support new
product launches from idea to shelf — naming, packaging feedback, launch plan, retail material; grow the
online shop through email, offers, subscriptions and returning customers; work with retail and cafe
partners on activations, sampling and displays; brief and manage freelancers, photographers and agencies;
keep every piece of work on brand and inside the brand guidelines; report results every month in simple
numbers.
Requirements: at least 2 years of marketing or brand work in the UAE; proof you have run campaigns end to
end, not just one part; hands-on skills in social content, paid ads and design tools (Canva, Adobe or
similar); good writing in English, Arabic is a strong plus; creative, organised and willing to do the work
yourself — small team, no big team underneath; currently in the UAE and able to work on-site in Dubai.
Nice to have: FMCG, beverage, food or retail brand experience; Shopify; video editing.
Hiring process: shortlisted candidates send 2 or 3 examples of campaigns they ran, then a short task, then
one interview.
"""

ATS = [
    "brand", "brand guidelines", "marketing calendar", "content creation", "social media",
    "reels", "product photography", "in-store material", "POSM", "paid media", "paid ads",
    "Meta Ads", "Google Ads", "campaign management", "end to end campaigns", "ROI", "ROAS",
    "cost per acquisition", "product launch", "naming", "packaging", "go-to-market",
    "launch plan", "retail material", "e-commerce", "online shop", "Shopify", "email marketing",
    "EDM", "offers", "promotions", "returning customers", "retention", "retail partners",
    "cafes", "HORECA", "activations", "sampling", "displays", "trade marketing",
    "freelancers", "photographers", "agencies", "creative briefs", "Canva", "Adobe",
    "video editing", "monthly reporting", "KPIs", "FMCG", "beverage", "food", "UAE", "Dubai",
    "hands-on", "start-up", "small team",
]

CONTENT = {
    "headline": "Hands-On Brand & Content · Paid Social · Beverage & FMCG in the UAE · Shopify",
    "professional_summary": (
        "UAE-based brand marketer who plans the calendar and then executes it herself — content, Meta and Google "
        "ads, launches and retail activations for three beverage and food brands in Dubai, plus the Shopify store."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 - Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG manufacturer (Befit drinks, Eurocake, Flair) | retail, HORECA, Shopify D2C, talabat & Careem | 50+ markets",
            "bullets": [
                "Own the monthly and quarterly marketing calendar for three brands and run it myself: social content and reels, product photography and in-store/POSM material, all inside the brand guidelines",
                "Plan and optimise paid campaigns on Meta and Google Ads day to day - budgets, audiences, remarketing and creative testing - tracking what each campaign costs and what it returns in sales",
                "Grow the Shopify store end to end: offers, EDM sends and funnel testing to lift conversion, AOV and repeat purchase",
                "Take new products from idea to shelf - packaging feedback, launch plan and retail material - and run activations, sampling and displays with retail and cafe partners",
                "Brief a designer, a social executive, photographers and 4 agencies, and report results monthly in simple numbers: sales, spend, ROI, reach and conversion",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager - Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 - Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's lifestyle marketplace | 42 consumer brands",
            "bullets": [
                "Built and ran campaign calendars with 42 consumer brands - offers, promo mechanics and always-on content - growing +30% GMV QoQ by putting investment where it paid back",
                "Owned the Flash Sales channel reporting to the CEO: planned each drop end to end and presented results monthly",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager - XL Accounts",
            "dates": "Sep 2022 - Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | food & beverage partners",
            "bullets": [
                "Ran in-app promos and bespoke activations with food and beverage partners (KFC, Taco Bell, Sushi Shop), reading order and conversion data to grow volume profitably",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee - Category Planning",
            "dates": "Aug 2021 - Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | category & shopper analytics",
            "bullets": [
                "Measured promotional effectiveness and sell-in/sell-out with Nielsen across grocery retailers",
            ],
        },
    ],
    "skills_brand": (  # label -> "Brand & Content"
        "marketing calendar, social content & reels, product photography, copywriting (EN/ES), brand guidelines, POSM"
    ),
    "skills_ecommerce": (  # label -> "Paid & Online Shop"
        "Meta Ads, Google Ads (Search & Display), Shopify, EDM & offers, retention & repeat purchase"
    ),
    "skills_commercial": (  # label -> "Launches & Retail"
        "launches idea-to-shelf, packaging feedback, retail & cafe activations, sampling & displays, agency briefing"
    ),
    "skills_data": (  # label -> "Reporting"
        "ROI, ROAS, CPA, conversion rate, AOV, sell-out, monthly performance reporting"
    ),
    "skills_tools": (  # label -> "Tools"
        "Canva, Adobe (Photoshop basics), CapCut, Meta Ads Manager, Google Ads, Shopify, Power BI, Claude (AI)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Brand & Content",
    "E-Commerce & Digital": "Paid & Online Shop",
    "Commercial": "Launches & Retail",
    "Data & Analytics": "Reporting",
}


def make_job() -> Job:
    return Job(
        id="frio-sparkling-water-brand-executive-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE",
        url="https://www.linkedin.com/jobs/search/?keywords=Frio%20Sparkling%20Water%20Brand%20Executive%20Dubai",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "Frio Sparkling Water Brand Executive Dubai",
            "note": "Marca de bebidas de Dubái con planta propia, 2-10 empleados, se trabaja directamente con el "
                    "fundador. Encaje de contenido casi literal con su puesto actual (FMCG bebidas EAU, contenido, "
                    "Meta/Google Ads, Shopify, lanzamientos, retail y cafes). Riesgos: nivel Executive por debajo "
                    "de Manager (probable ajuste de banda salarial), 950 candidatos y +100 solicitudes, arabe como "
                    "'strong plus'. Proceso: 2-3 ejemplos de campanas + prueba corta + una entrevista. "
                    "Paula ya aplico el 2026-09-16 (Solicitud sencilla).",
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
        "salary_raw": "Not disclosed",
        "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": DATE_FOLDER, "raw": job.raw,
        "ai_score": 74, "ai_tier": "Hot",
        "skills_match": [
            "FMCG de bebidas y comida en EAU hoy mismo (Befit, Eurocake, Flair) con planta propia y retail",
            "Hands-on real: contenido social y reels, fotografia de producto, material en tienda dentro de guidelines",
            "Meta Ads y Google Ads a diario, midiendo coste y retorno por campana",
            "Shopify end-to-end: ofertas, EDM, recurrencia, conversion y AOV",
            "Lanzamientos de producto idea-to-shelf y activaciones con retail y cafes; brief a 4 agencias y freelancers",
        ],
        "missing_skills": [
            "TikTok Ads (el JD lo pide) - solo TikTok organico",
            "Arabe (strong plus en el JD)",
            "Edicion de video avanzada (nice to have) - nivel CapCut",
        ],
        "sector_fit": "muy alto - bebidas/FMCG en EAU, exactamente su categoria actual",
        "seniority_fit": "por encima - puesto Executive y ella es Manager; riesgo de banda salarial baja",
        "red_flags": [
            "950 candidatos y +100 solicitudes",
            "Empresa de 2-10 empleados: sueldo y estructura probablemente por debajo de su nivel actual",
            "Proceso exige 2-3 ejemplos de campanas propias y una prueba corta",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Encaje de contenido casi literal: el JD describe lo que Paula hace hoy en DoFreeze - calendario, "
            "contenido y reels, Meta/Google Ads, Shopify, lanzamientos idea-to-shelf, activaciones en retail y "
            "cafes, y reporting mensual simple - dentro de la misma categoria (bebidas FMCG en EAU). El CV se "
            "posiciona como operadora hands-on, no como manager de equipo grande, porque el puesto es Executive "
            "en una empresa de 2-10 personas. Brechas honestas: TikTok Ads (solo organico) y arabe."
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

    short = final_dir / "01_CV_y_Carta" / "Paula De Francisco - CV.pdf"
    final_cv = final_dir / "01_CV_y_Carta" / cv_pdf.name
    if final_cv.exists():
        shutil.copy(str(final_cv), str(short))
        print("OK_SHORT", short)

    try:
        from pypdf import PdfReader
        n = len(PdfReader(str(final_cv)).pages)
        print(f"PAGES {n}", "OK" if n == 1 else "!! SPILLS")
    except Exception as exc:  # noqa: BLE001
        print("page-count check skipped:", exc)

    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
