"""One-off: CV de una página para **Marketing Manager** de una **start-up FMCG** (cliente confidencial)
vía **Converge** (consultora de selección de Dubái). Dubái, presencial, jornada completa.
"Promocionado por técnico de selección", publicado hace 2 semanas. **902 solicitudes.** Paula ya
había empezado la solicitud en LinkedIn ("Solicitud modificada justo ahora").

Pide el JD: impulsar el crecimiento de marca y la expansión del negocio en el GCC; rol muy
hands-on, construir desde cero; iniciativas de marketing propias, estrategias de go-to-market,
presencia en varios mercados del GCC; trabajar con la dirección y equipos cross-funcionales.
**Individual contributor, sin reportes directos.** Perfil ideal (el cliente lo llama "esencial"):
**8+ años de FMCG**, con experiencia actual en FMCG Food & Beverage; **3–4 países del GCC**;
GTM y expansión en el GCC demostrados en roles anteriores; entorno start-up; **mezcla de FMCG
multinacional y local**; ritmo rápido y ownership; capacidad comercial, estratégica y de ejecución.

Ángulo honesto de Paula:
- FMCG Food actual: DoFreeze (grupo de alimentación local de los EAU: Befit, Eurocake, Flair),
  vendida en el GCC y 50+ mercados de exportación. Cumple "current F&B FMCG".
- Mezcla multinacional + local: Mondelez (multinacional, trainee de Category Planning) + DoFreeze
  (local). Es literalmente el mix que pide, aunque la parte multinacional es junior.
- GTM: 6 lanzamientos NPD end-to-end (brief, packaging, pricing, go-to-market) e integración de las
  marcas en el quick-commerce de los EAU (Noon, talabat, Careem) desde el onboarding.
- Construir desde cero (start-up): montó el programa de influencers desde cero (103 activaciones en
  3 campañas, con resultados de venta medidos), el programa de afiliación (iniciativa suya, con
  landing hecha con agentes de IA) y el sistema de automatización con IA (~40% menos trabajo manual).
  En Glovo ayudó a montar el vertical de Retail. Encaja con un rol hands-on.
- Puente GCC desde Miravia: onboarding de las casas árabes de oud y perfume (Arabian Oud, Lattafa,
  Swiss Arabian, Ajmal) como PIC de Fragrances.

Guardarraíles de honestidad:
- **8+ años de FMCG: NO.** Tiene ~5 años de carrera en total y ~2 del lado marca en FMCG (DoFreeze +
  Mondelez trainee). No se escribe ningún número de años en el CV. Es la brecha de verdad, y el
  cliente dice que es esencial.
- **3–4 países del GCC con nombre**: no hay dato firme de en qué países del GCC vende DoFreeze (hay
  indicios de KSA y Kuwait en scripts anteriores, sin confirmar). Se dice "GCC" sin nombrar países.
  Si Guille/Paula confirman los países, añadirlos al bullet de GTM.
- **Expansión a nuevos países del GCC liderada por ella**: no consta. Se habla de GTM de lanzamientos
  y de canales, no de "entré en Arabia Saudí".
- **Rol sin reportes**: se mantiene el equipo de dos solo como dato, sin protagonismo; el foco es
  hands-on.
- **Forecast**: la dueña es la e-commerce manager; no aparece.
- **Deliveroo**: DoFreeze NO está en Deliveroo. Plataformas: talabat, Noon, Careem.
- Sin árabe (el JD no lo menciona). Visa solo "UAE Residence Visa"; nunca "no sponsorship".
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

COMPANY = "Converge"
TITLE = "Marketing Manager"
DATE_FOLDER = "2026-10-02"

JOB_DESCRIPTION = """\
Marketing Manager | Dubai, UAE. Recruiter: Converge, on behalf of a confidential client. On-site, full time.
What This Role Is About: Our client, an ambitious FMCG start-up, is looking for a Marketing Manager, based in Dubai,
to drive brand growth and support the expansion of the business across the GCC. This is a highly hands-on role for
someone who is comfortable building from the ground up. As the business continues to grow, you will take ownership
of key marketing initiatives, develop go-to-market strategies, and help strengthen the company's presence across
multiple GCC markets. You will work closely with senior leadership and cross-functional teams to identify growth
opportunities, develop effective market strategies, and turn plans into action. Please note that this is an
individual contributor role at this stage, with no direct reports. The successful candidate must be comfortable
operating independently and taking a hands-on approach to building the marketing function.
The Client's Definition of the Ideal Fit: 8+ years of FMCG experience, with current experience within an FMCG Food &
Beverage business. Experience working across at least 3 to 4 GCC countries is required. Strong hands-on experience in
Go-To-Market strategy and expanding businesses across the GCC; this experience must be clearly demonstrated through
previous roles and responsibilities. Comfortable working in a start-up environment and building marketing
initiatives independently. A strong mix of experience across both multinational and local FMCG businesses. Proven
ability to work in fast-paced and evolving environments with a high level of ownership. Strong commercial,
strategic, and execution capabilities.
We understand this is a highly specific profile and that the combination of requirements significantly narrows the
talent pool. However, these experiences are essential for the stage of growth and ambitions of the business.
"""

ATS = [
    "marketing manager", "FMCG", "food & beverage", "F&B", "food", "start-up", "brand growth", "brand building",
    "go-to-market", "GTM", "go-to-market strategy", "market expansion", "GCC", "UAE", "multi-market",
    "hands-on", "building from the ground up", "marketing function", "ownership", "independent",
    "marketing initiatives", "market strategies", "growth opportunities", "senior leadership",
    "cross-functional", "multinational", "local FMCG", "fast-paced", "commercial", "strategic", "execution",
    "NPD", "product launches", "pricing", "packaging", "distributors", "modern trade", "quick-commerce",
    "Noon", "talabat", "Careem", "Shopify", "D2C", "e-commerce", "influencer marketing", "affiliate",
    "sampling", "trade marketing", "shopper marketing", "key accounts", "A&P budget", "Meta Ads",
    "Google Ads", "sell-in", "sell-out", "Nielsen", "ROI", "ROAS", "AI automation",
]

CONTENT = {
    "headline": "Marketing Manager · FMCG Food & Beverage · Go-to-Market & GCC Growth · Hands-on Builder",
    "professional_summary": (
        "Hands-on FMCG food marketer in Dubai, running brand and go-to-market for a homegrown food group "
        "(Befit, Eurocake, Flair) sold across the GCC and 50+ export markets. Launched six products and built "
        "the influencer, affiliate and AI-automation programmes from zero. Multinational FMCG grounding at "
        "Mondelez; marketplace side at Miravia (Alibaba)."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Homegrown UAE F&B / FMCG group | Befit, Eurocake, Flair | GCC + 50+ export markets",
            "bullets": [
                "Own go-to-market for 6 product launches end-to-end — brief, packaging, pricing, channel plan and launch — across the GCC and export markets, working with senior leadership, sales and distributors",
                "Integrated the brands into UAE quick-commerce from onboarding (Noon, talabat, Careem): listings, promotional mechanics and retail execution, alongside modern trade and our Shopify D2C store",
                "Built the influencer and affiliate programmes from zero — 103 creator activations over three campaigns: Befit × Noon +31% over baseline (+4,176 incremental units); SMASH × talabat daily sales +165% vs +4.7% for the control brand",
                "Built an AI automation system (Claude) for campaign planning, content and reporting, cutting ~40% of manual work; run Meta & Google Ads on ROI and ROAS; lead a designer and a social media executive",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Managed 42 brand accounts on assortment, pricing and promotions, delivering +30% GMV QoQ; owned the Flash Sales channel reporting to the CEO against P&L targets",
                "Launched the Fragrances category as PIC, onboarding 30+ stores in two months, including the official distributors of Arabian Oud, Lattafa, Swiss Arabian and Ajmal",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped build the Retail vertical, onboarding non-food brands beyond food delivery, and grew XL accounts (KFC, Taco Bell, La Tagliatella) through joint marketing activations",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | chocolate category (Milka, Suchard)",
            "bullets": [
                "Ran sell-in/sell-out and promotional-effectiveness analysis with Nielsen and supported NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": (  # -> "Marketing & GTM"
        "go-to-market, NPD launches, brand building, integrated campaigns, influencer & affiliate, sampling"
    ),
    "skills_ecommerce": (  # -> "Channels"
        "distributors, modern trade, quick-commerce (Noon, talabat, Careem), Shopify D2C, paid social"
    ),
    "skills_commercial": (  # -> "Commercial"
        "trade & shopper marketing, key accounts, pricing, A&P budgets, negotiation, P&L targets"
    ),
    "skills_data": (  # -> "Performance"
        "sell-in/sell-out, incremental volume, control groups, ROI & ROAS, Nielsen, automated dashboards"
    ),
    "skills_tools": (  # -> "Tools"
        "Excel & PowerPoint (Advanced), Power BI, Nielsen, SAP, Salesforce, Canva & Adobe, Claude (AI)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Marketing & GTM",
    "E-Commerce & Digital": "Channels",
    "Commercial": "Commercial",
    "Data & Analytics": "Performance",
}


def make_job() -> Job:
    return Job(
        id="converge-fmcg-startup-marketing-manager-2026-10",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE (On-site)",
        url="https://www.linkedin.com/jobs/search/?keywords=Converge%20Marketing%20Manager%20FMCG%20Dubai",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "Converge Marketing Manager FMCG start-up Dubai",
            "note": "Converge es la consultora de selección; el cliente es una start-up FMCG confidencial. Rol "
                    "individual contributor, sin reportes, presencial en Dubái. 902 solicitudes, publicado hace 2 "
                    "semanas. El cliente pide como esencial 8+ años de FMCG (Paula tiene ~5 de carrera, ~2 de "
                    "FMCG brand-side) y 3-4 países del GCC (sin confirmar en cuáles vende DoFreeze). Encaje bueno "
                    "en lo demás: F&B actual, mezcla Mondelez + DoFreeze, GTM de 6 lanzamientos, construir desde "
                    "cero.",
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
        "posted_date": "2026-09-18", "raw": job.raw,
        "ai_score": 55, "ai_tier": "Warm",
        "skills_match": [
            "FMCG Food actual: DoFreeze (Befit, Eurocake, Flair), grupo local de los EAU",
            "Mezcla multinacional + local que pide: Mondelez + DoFreeze",
            "Go-to-market de 6 lanzamientos end-to-end (brief, packaging, pricing, canal)",
            "Integró las marcas en Noon, talabat y Careem desde el onboarding",
            "Construye desde cero: programas de influencers, afiliación y automatización con IA",
            "Hands-on y con ownership, que es lo que pide un rol sin reportes",
            "Resultados de venta medidos: Noon +31% sobre baseline, talabat +165% frente a +4,7% del control",
        ],
        "missing_skills": [
            "8+ años de FMCG: tiene ~5 de carrera y ~2 de FMCG del lado marca (el cliente lo llama esencial)",
            "3-4 países del GCC con nombre: sin confirmar en cuáles vende DoFreeze",
            "Expansión a nuevos países del GCC liderada por ella: no consta",
        ],
        "sector_fit": "muy bueno — FMCG Food & Beverage actual, local y con base multinacional",
        "seniority_fit": "por debajo — piden 8+ años y ella tiene ~5; el rol es individual contributor",
        "red_flags": [
            "El cliente dice que 8+ años y 3-4 países del GCC son esenciales: el filtro del recruiter puede cortarla",
            "902 solicitudes y publicado hace 2 semanas",
            "Individual contributor sin reportes: hoy gestiona a dos personas",
            "Start-up confidencial: verificar banda salarial pronto (suelo 20.000 AED/mes)",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "En contenido encaja bien: FMCG de alimentación actual, la mezcla de multinacional (Mondelez) y local "
            "(DoFreeze), go-to-market de seis lanzamientos y un historial de montar programas desde cero, que es "
            "lo que pide una start-up con un rol hands-on. El problema es de criterios duros: el cliente pide 8+ "
            "años de FMCG y experiencia en 3-4 países del GCC, y dice expresamente que son esenciales. Paula tiene "
            "unos cinco años de carrera y no está confirmado en qué países del GCC vende DoFreeze. Merece la pena "
            "aplicar porque es barato, pero con expectativas bajas salvo que el recruiter de Converge flexibilice "
            "los años."
        ),
        "scored_by": "manual:claude", "freshness": "recent",
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
