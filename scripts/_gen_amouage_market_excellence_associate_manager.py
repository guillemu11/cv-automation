"""One-off: CV de una página + carta para **Market Excellence Associate Manager** en
**AMOUAGE** (alta perfumería omaní, Dubai). Publicada 2026-09-22, +100 solicitudes en 9h.

Pide el JD: desplegar la estrategia de Market Excellence en el canal wholesale/distribuidores;
toolkits de lanzamiento T2 con evaluaciones pre y post-mortem; definir la estrategia wholesale
de todos los lanzamientos de producto; mantener guidelines wholesale para consistencia de marca
en todos los mercados; validaciones de trade marketing y activaciones 360 para distribuidores
clave y no clave; programas de fidelidad efímeros; categorías/iniciativas efímeras; eventos.
Piden 3-5 años en trade marketing, ventas o marketing de lujo; experiencia con distribuidores
y redes wholesale; sector fragancia de lujo, beauty o moda; inglés fluido; máster.

Ángulo honesto de Paula: Miravia (Alibaba) — KAM de Beauty, Fragancias y Fashion, PIC
Fragrances, onboarding de los distribuidores oficiales de Arabian Oud, Lattafa, Swiss Arabian
y Ajmal (30+ tiendas en dos meses) con surtido, pricing y planes promocionales; DoFreeze —
distributor management en 50+ mercados, 6 NPD end-to-end con go-to-market 360, trade y shopper
marketing por canal, brand guidelines y revisión de todo el output creativo.

Guardarraíles de honestidad:
- NO tiene máster (Grado en ADE por CUNEF, TFG 9.5/10). No se insinúa lo contrario.
- NO habla árabe. El JD no lo pide — no se menciona.
- Visa: solo "UAE Residence Visa" (patrocinada por el empleador); nunca "no sponsorship needed".
- No ha trabajado en una maison de alta perfumería por dentro: el ángulo es el lado
  distribuidor/retailer de las casas de oud y beauty, que es real y verificable.
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

COMPANY = "AMOUAGE"
TITLE = "Market Excellence Associate Manager"
DATE_FOLDER = "2026-09-22"

JOB_DESCRIPTION = """\
Market Excellence Associate Manager — AMOUAGE, Dubai, UAE. On-site, full time.
Drive wholesale excellence, trade marketing execution, product launches and brand consistency across
AMOUAGE's global distributor network. Working closely with Market Excellence, Sales, distributors and
wholesale partners, support the deployment of AMOUAGE's Market Excellence strategy across key markets.
Manage wholesale launch strategies, trade marketing activations, distributor toolkits, brand guidelines,
loyalty initiatives and product-focused projects, ensuring strong execution and consistent brand standards
across all wholesale channels.
Impact: lead the wholesale deployment of the Market Excellence strategy across key distributors and
wholesale partners; develop and manage toolkits for T2 launches including pre- and post-mortem wholesale
evaluations; define and implement wholesale strategies for all product launches; develop and maintain
wholesale guidelines to ensure brand consistency across all markets; oversee trade marketing validations
and 360 activations for key distributors; manage trade marketing validations for non-key distributors;
support and execute ephemeral loyalty program initiatives; drive focus and execution on ephemeral product
categories and initiatives; support innovative events in collaboration with the Market Excellence Manager.
Expertise: minimum 3-5 years in trade marketing, sales or luxury brand marketing; experience working with
distributors and wholesale networks; strong coordination and project execution skills; experience within
the luxury fragrance, beauty or fashion industry; knowledge of trade marketing best practices and retail
activations; Master's degree in Business, Marketing or related field; fluent in English.
"""

ATS = [
    "trade marketing", "wholesale", "distributors", "distributor network", "distributor management",
    "market excellence", "luxury", "fragrance", "beauty", "fashion", "product launches", "launch strategy",
    "go-to-market", "NPD", "toolkits", "brand guidelines", "brand consistency", "brand standards",
    "360 activations", "retail activations", "trade marketing validations", "loyalty programmes",
    "sell-in", "sell-out", "assortment", "pricing strategy", "promotional planning", "A&P budget",
    "key accounts", "modern trade", "travel retail", "GCC", "MENA", "multi-market", "project execution",
    "post-mortem evaluation", "events", "visual merchandising", "POS", "ROI",
]

CONTENT = {
    "headline": "Trade Marketing · Wholesale & Distributors · Luxury Fragrance, Beauty & Fashion",
    "professional_summary": (
        "Trade marketing and commercial professional with 4+ years across luxury fragrance, beauty and fashion "
        "— PIC Fragrances at Alibaba's Miravia (onboarded the official distributors of Arabian Oud, Lattafa, "
        "Swiss Arabian and Ajmal) and today running brand, trade and distributor execution across 50+ markets "
        "from Dubai."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG house (Befit, Eurocake, Flair) | distributor-led wholesale across 50+ countries",
            "bullets": [
                "Deploy brand and trade marketing plans through the distributor and wholesale network across GCC, MENA, Asia, Europe, USA and Africa — validating local activations, POS execution and adaptations against brand guidelines",
                "Lead 6 product launches end-to-end (brief, packaging, pricing, 360° go-to-market), building the launch toolkits distributors execute with and reviewing performance after each launch to sharpen the next",
                "Own brand guidelines and all creative output for three brands, leading a team of two and four agencies to keep standards consistent across every market and channel",
                "Build channel-by-channel trade and shopper marketing plans, manage A&P budgets and track sell-out and ROI to decide where the next investment goes",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba Group e-commerce | Beauty, Fragrance & Fashion verticals | 100K+ employees",
            "bullets": [
                "PIC Fragrances: led category expansion by onboarding 30+ stores in two months, including the official distributors of Arabian Oud, Lattafa, Swiss Arabian and Ajmal — owning their assortment, pricing and promotional calendar",
                "Managed 42 key accounts across beauty, fragrances and fashion, delivering +30% GMV growth QoQ through assortment, pricing strategy and targeted trade activations",
                "Owned the Flash Sales channel for Beauty, Fashion & Home reporting to the CEO — event calendar, brand selection and P&L-aligned commercial plans",
                "Created the Beauty Club and Hot on Social programmes, building brand visibility and customer loyalty across the beauty portfolio",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic partners and helped build the Retail vertical, onboarding fashion and lifestyle brands and negotiating joint commercial and marketing plans",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | 90K+ employees",
            "bullets": [
                "Built sell-in/sell-out and promotional-effectiveness analysis with Nielsen and supported NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": (  # -> "Trade & Wholesale"
        "trade marketing plans, distributor & wholesale management, 360° activations, POS & retail execution, A&P budgets"
    ),
    "skills_ecommerce": (  # -> "Launches & Brand"
        "NPD end-to-end, launch toolkits, go-to-market, brand guidelines & consistency, loyalty & events"
    ),
    "skills_commercial": (  # -> "Commercial"
        "key account management, assortment & range, pricing strategy, promotional planning, negotiation"
    ),
    "skills_data": (  # -> "Analytics"
        "sell-in/sell-out, post-launch evaluation, ROI & ROAS, KPI dashboards, Nielsen, forecasting support"
    ),
    "skills_tools": (  # -> "Tools & Languages"
        "Excel (Expert), PowerPoint, Power BI, Tableau, SAP, Salesforce, Claude (AI) | Spanish (native), English (C1)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Trade & Wholesale",
    "E-Commerce & Digital": "Launches & Brand",
    "Commercial": "Commercial",
    "Data & Analytics": "Analytics",
}


def make_job() -> Job:
    return Job(
        id="amouage-market-excellence-associate-manager-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE",
        url="https://www.linkedin.com/jobs/search/?keywords=AMOUAGE%20Market%20Excellence%20Associate%20Manager",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "AMOUAGE Market Excellence Associate Manager Dubai",
            "note": "Alta perfumeria omani. Encaje muy alto: trade marketing + distribuidores + fragancia de lujo. "
                    "Brecha: piden master (Paula tiene Grado). 235 solicitudes en 9h, Easy Apply.",
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
        "ai_score": 86, "ai_tier": "Hot",
        "skills_match": [
            "PIC Fragrances en Miravia: onboarding de los distribuidores oficiales de Arabian Oud, Lattafa, Swiss Arabian y Ajmal (30+ tiendas en 2 meses)",
            "Distributor y wholesale management en 50+ mercados desde Dubai (DoFreeze)",
            "Trade y shopper marketing por canal, activaciones 360 y validacion de ejecucion en POS",
            "6 NPD end-to-end con toolkits de lanzamiento y go-to-market 360",
            "Brand guidelines y consistencia de marca en multi-mercado, liderando equipo de 2 y 4 agencias",
            "Beauty, fragancias y fashion: 42 key accounts, +30% GMV QoQ",
        ],
        "missing_skills": [
            "Master's degree (Paula tiene Grado en ADE por CUNEF, TFG 9.5/10)",
            "Experiencia dentro de una maison de alta perfumeria (su angulo es el lado distribuidor/retailer)",
            "Travel retail como canal formal",
        ],
        "sector_fit": "alto — fragancia de lujo, beauty y fashion es exactamente su vertical en Miravia",
        "seniority_fit": "encaje — Associate Manager con 3-5 anos pedidos; ella tiene 4+ y ya es Manager",
        "red_flags": [
            "235 solicitudes en 9 horas y Easy Apply: hay que complementar con contacto directo",
            "Piden master; 60% de los solicitantes lo tiene",
            "Titulo Associate Manager, medio escalon por debajo de su titulo actual — confirmar banda salarial >= 20k AED",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "El JD es despliegue wholesale de trade marketing en red de distribuidores para una casa de alta "
            "perfumeria: toolkits de lanzamiento, validaciones de trade, activaciones 360, guidelines de marca. "
            "Paula ha hecho las dos mitades: el lado distribuidor de las casas de oud arabes en Miravia (PIC "
            "Fragrances) y hoy el despliegue de marca y trade via distribuidores en 50+ mercados desde Dubai. "
            "La brecha real es el master y no haber estado dentro de una maison; se compensa con encaje sectorial "
            "y geografico poco comun en la pila de candidatos."
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
