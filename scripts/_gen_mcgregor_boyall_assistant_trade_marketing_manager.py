"""One-off: CV de una página para **Assistant Trade Marketing Manager** publicado por
**McGregor Boyall** (consultora de selección) para una empresa de **food & beverage** en Dubai.

Ojo con el nivel: el título del anuncio dice "Assistant Trade Marketing Manager" pero el cuerpo
del JD dice "to appoint a Trade Marketing Manager". Probable banda por debajo de Manager pleno
— verificar sueldo pronto (suelo de Paula: 20.000 AED/mes).

Pide el JD: planes de trade marketing por canal (modern trade, general trade y foodservice) para
disponibilidad, visibilidad y conversión; ownership del trade spend y los presupuestos
promocionales con ROI medible; activación en tienda, PoS y campañas promocionales en cuentas
clave; trabajo con equipos de ventas y distribuidores para reforzar el route-to-market; insights
de categoría y shopper para planes de canal y negociaciones con clientes; seguimiento de
distribución, ventas y performance promocional con acciones correctoras; soporte a lanzamientos
con planes, listings y activación channel-ready; y trabajo cross-funcional con brand, ventas,
supply chain y finance. Pide 5+ años en trade marketing / category management / comercial en F&B
o FMCG, experiencia **principal side** con distribuidores y cuentas clave en GCC, Excel y
PowerPoint avanzados, y track record de activación en tienda.

Ángulo honesto de Paula:
- DoFreeze (F&B puro, principal side): planes de trade y shopper por canal en 50+ mercados,
  red de distribuidores, modern trade y quick-commerce, presupuestos de A&P, 6 lanzamientos NPD
  channel-ready y ejecución en punto de venta con sampling y seeding.
- Mondelez: category planning en FMCG con Nielsen — sell-in/sell-out y efectividad promocional.
  Es el pedigrí más "trade" de su CV.
- Miravia: pricing, surtido y promociones con P&L, 42 cuentas clave.

Guardarraíles de honestidad:
- **Foodservice**: NO lo ha trabajado como canal. No se menciona. Es la brecha real.
- **Activación en tienda / PoS**: tiene ejecución en punto de venta, sampling y seeding en modern
  trade, pero NO programas grandes de display/PoS con agencia de campo. Se dice lo que hay.
- **5+ años en trade marketing**: Paula tiene ~5 años de carrera comercial, con trade marketing
  como parte de su rol actual, no como tenencia dedicada. No se infla ninguna fecha.
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

COMPANY = "McGregor Boyall"
TITLE = "Assistant Trade Marketing Manager"
DATE_FOLDER = "2026-09-23"

JOB_DESCRIPTION = """\
Assistant Trade Marketing Manager — McGregor Boyall (recruitment consultancy) for a leading food and
beverage business. Dubai, UAE. On-site, full time.
The role sits at the intersection of brand and sales, translating category strategy into in-market
execution across modern trade, general trade and foodservice channels.
Key responsibilities: develop and execute channel-specific trade marketing plans to drive availability,
visibility and sales conversion; own trade spend and promotional budgets, ensuring investment is aligned
to growth priorities and delivers measurable ROI; design and deliver in-store activation, point-of-sale and
promotional campaigns across key accounts; partner with sales teams and distributors to strengthen
route-to-market and improve execution standards; build and maintain category and shopper insights to inform
channel plans and customer negotiations; track distribution, sales and promotional performance, identifying
gaps and driving corrective action; support new product launches with channel-ready plans, listings and
activation; work cross-functionally with brand, sales, supply chain and finance to embed trade priorities
into commercial plans.
What you'll bring: 5+ years in trade marketing, category management or commercial roles within food and
beverage or wider FMCG; experience working principal side with distributors and key accounts in the GCC;
strong commercial acumen, with the ability to link trade investment to revenue and margin outcomes;
advanced Excel and PowerPoint, with confidence handling sales and market data; proven track record of
in-store activation and promotional execution; Bachelor's degree in Business, Marketing or a related
discipline.
"""

ATS = [
    "trade marketing", "shopper marketing", "category management", "FMCG", "food and beverage", "F&B",
    "modern trade", "general trade", "channel plans", "availability", "visibility", "sales conversion",
    "trade spend", "promotional budgets", "A&P budget", "ROI", "in-store activation", "point of sale",
    "POS", "promotional campaigns", "key accounts", "distributors", "route-to-market", "principal side",
    "GCC", "MENA", "category insights", "shopper insights", "customer negotiations", "distribution",
    "sell-in", "sell-out", "promotional effectiveness", "corrective action", "new product launch", "NPD",
    "listings", "channel-ready", "cross-functional", "brand", "sales", "supply chain", "finance",
    "Nielsen", "Excel", "PowerPoint", "commercial acumen", "margin", "revenue", "pricing", "assortment",
]

CONTENT = {
    "headline": "Trade & Shopper Marketing · Modern Trade, Distributors & Key Accounts · GCC",
    "professional_summary": (
        "Trade and commercial marketer in F&B, principal side — building channel plans, promotional "
        "budgets and in-market execution across modern trade and distributors in 50+ markets. FMCG "
        "category planning at Mondelez; 42 key accounts and +30% GMV QoQ at Miravia (Alibaba)."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE food & beverage group (Eurocake, Befit, SMASH, Flair) | principal side | 50+ markets",
            "bullets": [
                "Build channel-specific trade and shopper marketing plans across modern trade, general trade and quick-commerce, driving availability, visibility and sell-out in GCC, MENA and 50+ export markets",
                "Own A&P and promotional budgets — setting mechanics, tracking spend against sell-out and reporting ROI — and partner with the distributor network and sales teams to improve route-to-market and execution standards",
                "Lead 6 NPD launches end-to-end with channel-ready plans: listings, pricing, promotional mechanics, in-store execution and sampling and seeding across modern trade and quick-commerce accounts",
                "Track distribution, promotional performance and competitor activity, flag gaps and drive corrective action, working cross-functionally with sales, supply chain and finance",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Managed 42 key accounts — assortment, pricing strategy and promotional calendars — delivering +30% GMV growth QoQ and leading customer negotiations on investment and visibility",
                "Owned the Flash Sales channel for Beauty, Fashion & Home reporting to the CEO, building commercial plans aligned to P&L targets and reading promotional ROI to steer the next cycle",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed XL F&B accounts (KFC, Taco Bell, La Tagliatella, Sushi Shop) on catalogue, promotional mechanics and GMV, negotiating joint investment with partners",
            ],
        },
        {
            "company": "Mondelez International · Massimo Dutti (Inditex)",
            "role": "Trainee, Category Planning · Sales Associate",
            "dates": "Jun 2018 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG, chocolate category (Milka, Suchard) | Premium fashion retail floor",
            "bullets": [
                "Ran sell-in/sell-out and promotional-effectiveness analysis with Nielsen, built category performance reports and supported NPD launches (Milka Spread, Mini Suchard); Inditex grounding in store execution and visual merchandising",
            ],
        },
    ],
    "skills_brand": (  # -> "Trade & Shopper"
        "channel plans, in-store activation, PoS & promotional mechanics, sampling & seeding, visibility & availability, NPD channel plans"
    ),
    "skills_ecommerce": (  # -> "Channels & RTM"
        "modern trade, general trade, distributor management, route-to-market, key accounts, quick-commerce (Noon, talabat, Careem)"
    ),
    "skills_commercial": (  # -> "Commercial & Budgets"
        "trade spend & A&P budgets, promotional ROI, pricing strategy, assortment, customer negotiations, margin awareness"
    ),
    "skills_data": (  # -> "Data & Insights"
        "sell-in/sell-out, distribution tracking, promotional effectiveness, category & shopper insights, Nielsen, AI-automated reporting"
    ),
    "skills_tools": (  # -> "Tools"
        "Excel (Advanced), PowerPoint (Advanced), Nielsen, Planorama, Power BI, Tableau, SAP, Salesforce, Claude (AI)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Trade & Shopper",
    "E-Commerce & Digital": "Channels & RTM",
    "Commercial": "Commercial & Budgets",
    "Data & Analytics": "Data & Insights",
}


def make_job() -> Job:
    return Job(
        id="mcgregor-boyall-assistant-trade-marketing-manager-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE (On-site)",
        url="https://www.linkedin.com/jobs/search/?keywords=McGregor%20Boyall%20Assistant%20Trade%20Marketing%20Manager%20Dubai",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "McGregor Boyall Assistant Trade Marketing Manager Dubai",
            "note": "Vacante a través de consultora (McGregor Boyall) para una empresa de F&B sin nombrar. "
                    "Encaje muy directo con DoFreeze (F&B, principal side, distribuidores, modern trade, "
                    "presupuestos de A&P) y con Mondelez (category planning FMCG con Nielsen). Brecha real: "
                    "foodservice como canal y programas grandes de PoS con agencia de campo. OJO CON EL NIVEL: "
                    "el título dice 'Assistant' pero el cuerpo del JD dice 'to appoint a Trade Marketing "
                    "Manager' — verificar banda salarial pronto (suelo 20K AED). 213 solicitudes en un día.",
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
        "ai_score": 78, "ai_tier": "Hot",
        "skills_match": [
            "F&B principal side hoy mismo: DoFreeze, con planes de trade y shopper por canal en 50+ mercados",
            "Red de distribuidores y modern trade en GCC/MENA — justo el 'principal side with distributors' del JD",
            "Presupuestos de A&P y mecánicas promocionales con seguimiento de ROI contra sell-out",
            "6 lanzamientos NPD channel-ready: listings, pricing, mecánica promocional y ejecución en punto de venta",
            "Mondelez: category planning FMCG con Nielsen, sell-in/sell-out y efectividad promocional",
            "Miravia: 42 cuentas clave, negociación de inversión y visibilidad, +30% GMV QoQ",
            "Excel y PowerPoint avanzados, que el JD pide explícitamente",
        ],
        "missing_skills": [
            "Foodservice como canal (no lo ha trabajado)",
            "Programas grandes de PoS/display con agencia de campo",
            "5+ años de trade marketing DEDICADO (tiene ~5 de carrera comercial, con trade como parte del rol actual)",
        ],
        "sector_fit": "alto — F&B es exactamente su sector actual",
        "seniority_fit": "ambiguo — el anuncio dice 'Assistant' pero el JD dice 'Trade Marketing Manager'; verificar banda",
        "red_flags": [
            "213 solicitudes en un solo día",
            "Empresa sin nombrar: no se puede investigar cultura, marca ni banda salarial antes de aplicar",
            "'Assistant' en el título puede significar banda por debajo del suelo de 20K AED — preguntar pronto",
            "Presencial, no híbrido",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Encaje de sector y de función muy limpio: el puesto es trade marketing en F&B con distribuidores y "
            "cuentas clave en GCC, y eso es literalmente lo que Paula hace hoy en DoFreeze desde el lado del "
            "principal, con el respaldo de category planning en Mondelez. Las brechas son foodservice y PoS a gran "
            "escala con agencia de campo. El punto a aclarar antes de invertir tiempo no es el encaje sino el "
            "nivel: 'Assistant' en el título frente a 'Trade Marketing Manager' en el cuerpo del anuncio. Al ir por "
            "consultora, la vía es responder al recruiter y preguntar banda y cliente."
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
