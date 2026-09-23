"""One-off: CV de una página para **Shopper Marketing (Senior) Account Manager** en una agencia de
marketing de Dubái, vacante publicada por **Xpat Today** (consultora de selección, 2-10 empleados).
Presencial, jornada completa. LinkedIn Easy Apply. 125 solicitudes EN UN SOLO DÍA.

Anunciante del empleo con nombre: **Sarah Melati** (3er grado) — hay a quién escribir.

Pide el JD: agencia de marketing en crecimiento que trabaja para marcas líderes de Oriente Medio.
Reporta al Group Account Director. Responsabilidades: reforzar y ampliar la relación con clientes
clave; tomar briefs de cliente y desarrollar soluciones creativas y estratégicas con el apoyo de
Account Directors y equipo de diseño; investigación de mercado para apoyar la ejecución de briefs;
desarrollo de cuentas clave e input estratégico en el desarrollo de campañas; comunicar objetivos,
plazos y presupuestos a clientes y stakeholders internos y externos; canalizar la comunicación
entre departamentos para el desarrollo de creatividad, estrategia, **PoS, material de marketing y
premiums**; **planificar y ejecutar eventos**, incluidos lanzamientos de producto y activaciones de
marca; liderar y participar en presentaciones a cliente. El titular del anuncio especifica
"Experiential BTL activation and Trade Marketing experience".

Requisitos: experiencia en marketing (preferiblemente Shopper/Trade Marketing) **en un rol de
Account Manager**; experiencia planificando y ejecutando campañas; experiencia extensa en shopper
marketing (estrategia y ejecución); gestión de eventos de principio a fin; comprensión del
comportamiento de compra del shopper; mucha autonomía, organización y atención al detalle.

Ángulo honesto de Paula:
- Shopper y trade marketing REAL: planes por canal en modern trade, general trade y quick-commerce
  para 50+ mercados, con presupuesto de A&P y mecánicas promocionales medidas en sell-out.
- Comportamiento de compra: mide en recompra e incrementalidad con grupo de control, no en alcance.
- Activaciones y lanzamientos: 6 NPD end-to-end, sampling y seeding en punto de venta y
  quick-commerce, sorteo con talabat, 2 campañas de lanzamiento de SMASH con creators.
- **Es la clienta de la agencia, y eso aquí es un activo**: gestiona 4 agencias, redacta los
  briefs, negocia (-30% conseguido), revisa entregables y audita sus informes. Sabe exactamente
  qué espera un cliente de un account manager porque lo vive desde el otro lado de la mesa.
- Gestión de stakeholders, plazos y presupuestos; dirige a un diseñador y una social media exec,
  es decir, ya brifea y revisa producción creativa.
- Miravia y Glovo: relación con cuentas clave, presentaciones comerciales y negociación.

Guardarraíles de honestidad (IMPORTANTES):
- **Nunca ha trabajado en agencia ni ha tenido un rol de Account Manager de agencia.** Es la
  brecha central del puesto. El CV no finge lo contrario: presenta su experiencia de cliente y su
  gestión de agencias como lo que son.
- **Experiential BTL a gran escala**: no ha producido activaciones experienciales ni roadshows con
  equipo de campo. Tiene sampling, seeding y lanzamientos. Se dice eso y solo eso.
- **Eventos**: ha hecho lanzamientos y activaciones de marca, no producción de eventos como
  disciplina. No se infla a "event management end-to-end" de agencia.
- **PoS y premiums**: ejecución en punto de venta sí; no desarrollo de premiums ni producción de
  material PoS con proveedores.
- Sin árabe. Visa solo "UAE Residence Visa"; nunca "no sponsorship needed".
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

COMPANY = "Xpat Today"
TITLE = "Shopper Marketing Account Manager"
DATE_FOLDER = "2026-09-23"

JOB_DESCRIPTION = """\
Shopper Marketing Senior Account Manager — Experiential BTL activation and Trade Marketing experience.
Posted by Xpat Today (recruitment agency) for a fast-growing marketing agency in Dubai, UAE. On-site, full time.
About the company: the client is a dynamic and fast growing marketing agency driving marketing strategies for
some of the Middle East's leading brands — a high-paced, results-driven environment requiring a proactive
individual to manage a portfolio of key accounts and projects with a focus on shopper marketing strategy and
retail trade activations.
Reporting to the Group Account Director. Key responsibilities: strengthen and expand relationships with key
clients and stakeholders; take client briefs and develop creative and strategic solutions with the support of
Account Directors, Account Managers and the design team; research all facets of marketing to support execution
of client briefs; assist the development of key accounts and provide strategic input into campaign development;
communicate project goals, timelines and budgets to clients and internal and external stakeholders; traffic
communication through departments to aid development of creative, strategy, POS, marketing collateral and
premiums; plan and execute events including product launches and brand activations; ensure jobs are completed
to an impeccable standard; lead and participate in client presentations, responding to briefs, concepts and
initiatives; build strong relationships with team members.
Qualifications: experience in marketing, preferably Shopper Marketing / Trade Marketing, in an Account Manager
role; experience planning and executing marketing campaigns; extensive shopper marketing experience including
developing strategies and executing campaigns; managing events from initiation to completion; understanding
consumer purchasing behaviour; highly organised with strong attention to detail, able to prioritise, problem
solve and work autonomously and collaboratively across departments; committed to excellent client service.
"""

ATS = [
    "shopper marketing", "trade marketing", "retail activation", "brand activation", "BTL",
    "experiential", "point of sale", "POS", "marketing collateral", "premiums", "product launch",
    "events", "campaign planning", "campaign execution", "client brief", "briefing", "creative development",
    "strategic input", "account management", "key accounts", "client relationships", "stakeholder management",
    "budgets", "timelines", "project management", "client presentations", "agency management",
    "consumer purchasing behaviour", "shopper insights", "category management", "modern trade",
    "general trade", "quick-commerce", "FMCG", "beauty", "retail", "GCC", "MENA", "UAE", "sell-out",
    "promotional mechanics", "sampling", "seeding", "A&P budget", "ROI", "Dubai", "cross-functional",
    "design team", "negotiation", "attention to detail", "autonomy",
]

CONTENT = {
    "headline": "Shopper & Trade Marketing · Retail Activation · Agency & Key Account Management",
    "professional_summary": (
        "Shopper and trade marketer who has sat on the client side of the desk: writes the briefs, "
        "manages four agencies in Dubai, negotiates the rates and audits what comes back. Builds "
        "channel plans and retail activations across modern trade and quick-commerce in 50+ markets, "
        "and measures them on shopper behaviour and sell-out rather than reach."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG group (Befit, SMASH, Eurocake) | modern trade + quick-commerce | 50+ markets",
            "bullets": [
                "Manage 4 Dubai marketing agencies end-to-end — writing the briefs, setting objectives, timelines and budgets, trafficking creative through to delivery and negotiating −30% on rate, with agencies over-delivering 103 creators against 75 contracted",
                "Build shopper and trade marketing plans by channel across modern trade, general trade and quick-commerce, owning A&P and promotional budgets and driving availability, visibility and conversion at the point of purchase",
                "Plan and execute brand activations and product launches: 6 NPD launches end-to-end, 2 launch campaigns for SMASH, seasonal in-store and in-app sampling and seeding, and a purchase-to-enter cashback activation with talabat",
                "Read shopper behaviour to steer the next campaign — SMASH × talabat lifted daily revenue AED 355 → 940 (+165%) against a control brand (+4.7%); audited an agency's reporting and found reach estimated from followers and double-counted accounts, then rebuilt the KPI definitions",
                "Brief and review all creative and social output, leading a graphic designer and a social media executive and presenting plans and results to commercial leadership",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Managed a portfolio of 42 key accounts — client relationships, promotional calendars, pricing and assortment — delivering +30% GMV QoQ, and created 'Beauty Club' and 'Hot on Social' as brand activation programmes on the platform",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue",
            "bullets": [
                "Managed XL client accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop) with bespoke marketing activations, leading cross-functional teams across marketing, logistics and support and closing commercial deals",
            ],
        },
        {
            "company": "Mondelez International · Massimo Dutti (Inditex)",
            "role": "Trainee, Category Planning · Sales Associate",
            "dates": "Jun 2018 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG (Milka, Suchard) | Premium fashion retail floor",
            "bullets": [
                "Sell-in/sell-out and promotional-effectiveness analysis with Nielsen behind NPD launches; Inditex grounding in store execution and visual merchandising",
            ],
        },
    ],
    "skills_brand": (  # -> "Shopper & Activation"
        "shopper marketing strategy, channel plans, retail & in-store activation, product launches, sampling & seeding, promotional mechanics, visual merchandising"
    ),
    "skills_ecommerce": (  # -> "Account & Agency"
        "client briefing, agency management (4 agencies), creative trafficking, rate negotiation, stakeholder communication, presentations, timelines & budgets"
    ),
    "skills_commercial": (  # -> "Commercial"
        "key account portfolio management, A&P budget ownership, pricing & assortment, distributor and modern trade relationships, deal negotiation"
    ),
    "skills_data": (  # -> "Shopper Insight"
        "consumer purchasing behaviour, sell-in/sell-out, incrementality & control-group measurement, promotional ROI, Nielsen, campaign reporting"
    ),
    "skills_tools": (  # -> "Tools"
        "Adobe Creative Suite, Canva, Excel & PowerPoint (Advanced), Power BI, Tableau, Nielsen, Salesforce, SAP, Meta Ads, Claude (AI agents)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Shopper & Activation",
    "E-Commerce & Digital": "Account & Agency",
    "Commercial": "Commercial",
    "Data & Analytics": "Shopper Insight",
}


def make_job() -> Job:
    return Job(
        id="xpat-today-shopper-marketing-account-manager-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE (On-site)",
        url="https://www.linkedin.com/jobs/search/?keywords=Xpat%20Today%20Shopper%20Marketing%20Account%20Manager%20Dubai",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "Xpat Today Shopper Marketing Senior Account Manager Dubai",
            "note": "Vacante de AGENCIA publicada por Xpat Today (consultora pequeña, 2-10 personas) para "
                    "una agencia de marketing de Dubái sin nombrar. Anunciante del empleo con nombre y "
                    "cara: SARAH MELATI (contacto de 3er grado) — hay a quién escribir directamente, que "
                    "es la mejor baza. El encaje de disciplina (shopper + trade + activación) es bueno; "
                    "el de contexto no: Paula nunca ha trabajado en agencia ni ha sido account manager de "
                    "agencia. Su contraargumento es que gestiona 4 agencias desde el lado cliente y sabe "
                    "qué se espera del otro lado. 125 solicitudes en 24 horas. Empresa cliente sin "
                    "nombrar: no se puede verificar banda ni cultura.",
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
        "ai_score": 66, "ai_tier": "Warm",
        "skills_match": [
            "Shopper y trade marketing real por canal: modern trade, general trade y quick-commerce en 50+ mercados",
            "Gestiona 4 agencias de Dubái desde el lado cliente: briefs, plazos, presupuestos y -30% negociado",
            "Activaciones y lanzamientos: 6 NPD, 2 campañas de lanzamiento de SMASH, sampling y seeding, sorteo con talabat",
            "Comportamiento de compra medido de verdad: incrementalidad con grupo de control, no alcance",
            "Cartera de cuentas clave en Miravia (42) y Glovo (KFC, Taco Bell, Sushi Shop) — client servicing",
            "Brifea y revisa producción creativa a diario; dirige a un diseñador y una social media exec",
            "Presupuestos de A&P y mecánicas promocionales con lectura de ROI",
        ],
        "missing_skills": [
            "NUNCA ha trabajado en agencia ni ha sido Account Manager de agencia — es la brecha central",
            "Experiential BTL a gran escala: roadshows, activaciones experienciales con equipo de campo",
            "Producción de eventos como disciplina (el JD pide gestionar eventos de inicio a fin)",
            "Desarrollo y producción de PoS y premiums con proveedores",
            "Sin árabe",
        ],
        "sector_fit": "alto — la disciplina es exactamente la suya, aunque el contexto (agencia) no lo sea",
        "seniority_fit": "bueno — Senior Account Manager reportando a Group Account Director encaja con su nivel",
        "red_flags": [
            "125 solicitudes en 24 horas",
            "Agencia cliente sin nombrar: no se puede verificar banda salarial, marcas ni cultura antes de aplicar",
            "Salto cliente -> agencia: ritmo, facturación por horas y servicio a cliente son otro oficio; conviene que ella quiera ese cambio, no solo que encaje",
            "Consultora pequeña (2-10 personas) como intermediaria",
            "Presencial",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "La disciplina encaja de forma muy limpia: shopper marketing, activación en retail, lanzamientos "
            "y mecánicas promocionales es lo que Paula hace cada día, y además con una cartera de cuentas "
            "clave gestionada antes en Miravia y Glovo, que es el músculo de client servicing que pide el "
            "rol. El giro que hay que jugar bien es que ella es hoy la CLIENTA de cuatro agencias de Dubái: "
            "escribe los briefs, negocia las tarifas y audita los informes, así que sabe exactamente qué "
            "espera un cliente de su account manager. Eso no borra la brecha real, que es no haber trabajado "
            "nunca dentro de una agencia, ni la de BTL experiencial y producción de eventos. Hay un nombre "
            "concreto publicando la vacante, Sarah Melati, y con 125 solicitudes en un día esa es la vía: "
            "escribirle en vez de sumarse al montón del Easy Apply. Antes de invertir, conviene que Paula "
            "decida si quiere pasarse al lado agencia, porque es otro oficio, no solo otra silla."
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
