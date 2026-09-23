"""One-off: CV de una página para **Sr. Specialist Retail Media Insight** en **talabat**
(Delivery Hero), Dubái, presencial. Rol REGIONAL de analítica dentro de la función de retail media.
LinkedIn Easy Apply. 1.208 solicitudes, 71 en un día — la más competida de todas.

Pide el JD: análisis profundo de performance y traducción a recomendaciones accionables para la
función de retail media en todos los mercados; insights regionales a los Retail Media Leads
locales y a partnerships; detección temprana de riesgo de under-delivery sobre objetivos de
ingresos y estrategias de optimización; iniciativas de test-and-learn con Product y Tech;
post-campaign reviews regionales para anunciantes y stakeholders internos; troubleshooting de
campañas cross-market; identificación de gaps de monetización, revenue leakage, problemas de
pacing e infrautilización de inventario; diagnósticos deep-dive con planes de acción priorizados;
estandarización de frameworks de medición; modelado predictivo y análisis de segmentación para
forecast y cohortes de crecimiento; dashboards regionales de revenue, delivery health y partner
performance; resúmenes ejecutivos; alineación de definiciones de KPI; roadmaps de ejecución.

Requiere: grado en Estadística, Business Analytics, Ingeniería, Economía o afín; 4-5 años en data
analytics, retail media, publicidad digital o e-commerce; **expertise en plataformas de retail
media, compra programática, modelos de atribución y palancas de optimización de campaña**;
exposición comercial; FMCG y/o entornos multi-mercado preferidos; Tableau, Power BI o Looker
avanzado; modelado en Excel/Sheets; comunicación persuasiva a stakeholders senior; inglés fluido,
**árabe preferido**.

Ángulo honesto de Paula:
- Es ANUNCIANTE en retail media en EAU: invierte y optimiza en talabat, Noon y Careem como marca,
  además de Meta y Google Ads. Conoce el producto desde el lado del partner que paga.
- Multi-mercado real: 50+ países en GCC, MENA, Asia, Europa, USA y África.
- FMCG puro: DoFreeze hoy y Mondelez al principio (category planning con Nielsen).
- Rigor de medición: mide con GRUPO DE CONTROL e incrementalidad (SMASH x talabat vs Befit), que
  es exactamente el debate de atribución del retail media.
- Auditó el informe de una agencia y encontró reach estimado desde seguidores, doble conteo de
  unique accounts y un mismo creador con 5x de diferencia entre oleadas — historia perfecta para
  "estandarizar frameworks de medición" y "alinear definiciones de KPI".
- Miravia (Alibaba): analizaba ROI, ROAS, conversión, tráfico y retención; dueña de Flash Sales
  reportando al CEO con planes atados a P&L. Ahí sí estuvo del lado de la plataforma.
- Reporting automatizado con IA y stack de BI (Power BI, Tableau, Looker) y Excel avanzado.

Guardarraíles de honestidad (IMPORTANTES):
- **Compra programática: NO.** No aparece en el CV.
- **Modelos de atribución formales / modelado predictivo: NO** como disciplina. Lo que sí tiene es
  medición con grupo de control e incrementalidad, y así se dice, sin llamarlo "attribution modeling".
- **Lado plataforma del retail media** (revenue leakage, pacing, inventario publicitario,
  monetización): NO lo ha hecho. Su experiencia de retail media es de anunciante. No se disfraza.
- **No ha gestionado performance de equipos locales** en varios países.
- Grado: BBA en CUNEF, no Estadística ni Business Analytics. No se reetiqueta.
- **Sin árabe** (el JD lo marca como preferido, no obligatorio) — ver [[paula-no-arabic-hard-filter]].
- Visa solo "UAE Residence Visa"; nunca "no sponsorship needed".
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

COMPANY = "talabat"
TITLE = "Sr. Specialist Retail Media Insight"
DATE_FOLDER = "2026-09-23"

JOB_DESCRIPTION = """\
Sr. Specialist Retail Media Insight — talabat (Delivery Hero). Dubai, UAE. On-site, full time. Regional role.
Drives performance excellence and revenue optimization across all markets by conducting deep performance
analysis and translating insights into clear, actionable recommendations for the retail media function.
Responsibilities: provide regional insights to local Retail Media Leads and regional partnerships teams;
detect early risks of under-delivery on revenue targets and recommend optimization strategies; drive
test-and-learn initiatives with Product and Tech; produce regional post-campaign reviews and insights for
advertisers and internal stakeholders; troubleshoot cross-market campaign issues; identify monetization gaps,
revenue leakage, pacing issues and inventory underutilization; develop structured deep-dive diagnostics with
prioritized action plans; standardize measurement frameworks across markets; use predictive modeling and
segmentation analysis to forecast performance and identify growth cohorts; build and maintain regional
dashboards tracking revenue, delivery health and partner performance; create executive-ready summaries;
ensure KPI definitions and reporting standards are aligned regionally; build execution roadmaps; drive
prioritization and accountability across stakeholders.
Requirements: Bachelor's in Statistics, Business Analytics, Engineering, Economics or related; 4-5 years in
data analytics, retail media, digital advertising or e-commerce; expertise in retail media platforms,
programmatic buying, attribution models and campaign optimization levers; strong commercial exposure and
understanding of revenue drivers; FMCG and/or multi-market environments preferred; advanced Tableau, Power BI
or Looker; strong Excel/Google Sheets modeling; persuasive communication to senior stakeholders; stakeholder
management and prioritization; fluent English required, Arabic proficiency preferred.
"""

ATS = [
    "retail media", "digital advertising", "data analytics", "performance analysis", "insights",
    "revenue optimization", "revenue drivers", "monetization", "pacing", "under-delivery",
    "campaign optimization", "post-campaign review", "measurement framework", "incrementality",
    "control group", "test-and-learn", "A/B testing", "segmentation", "cohorts", "forecasting",
    "dashboards", "KPI definitions", "reporting standards", "executive summaries", "deep-dive diagnostics",
    "action plans", "prioritization", "stakeholder management", "cross-functional", "cross-market",
    "multi-market", "regional", "GCC", "MENA", "FMCG", "e-commerce", "quick-commerce", "marketplace",
    "talabat", "Noon", "Careem", "Meta Ads", "Google Ads", "ROAS", "ROI", "GMV", "conversion",
    "sell-in", "sell-out", "Tableau", "Power BI", "Looker", "Excel modeling", "Nielsen", "SQL-free analytics",
    "advertiser", "partner performance", "commercial acumen", "P&L",
]

CONTENT = {
    "headline": "Commercial Analytics & Retail Media Performance · Multi-Market · GCC & MENA",
    "professional_summary": (
        "Commercial marketer who runs on measurement: buys and optimises retail media on talabat, "
        "Noon and Careem as an advertiser across 50+ markets, proves campaign impact with control "
        "groups and incrementality rather than platform-reported reach, and has audited agency "
        "reporting down to double-counted metrics. FMCG background, BI stack and AI-automated reporting."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE FMCG group (Befit, SMASH, Eurocake) | advertiser on talabat, Noon & Careem | 50+ markets",
            "bullets": [
                "Plan, buy and optimise retail media and paid media across talabat, Noon, Careem, Meta and Google Ads, reading ROAS, conversion and incremental sell-out to reallocate budget mid-flight and flag under-delivering activity early",
                "Built the team's measurement standard: SMASH × talabat measured against Befit as a control brand on the same platform and window — +165% daily revenue vs +4.7% control, ~AED 32K incremental on ~AED 8.7K spend; Befit × Noon, +4,176 incremental units, +31% over baseline",
                "Audited an agency's campaign reporting — reach estimated from follower counts, the same creator double-counted across waves at 5× variance, 'unique accounts' summed from estimates — then rebuilt the KPI definitions and moved spend to cohorts outperforming campaign average 10–40×",
                "Built AI-automated dashboards and reporting for campaign performance and KPI tracking across 50+ markets, cutting manual reporting ~40% and producing executive-ready summaries for leadership",
                "Run post-campaign reviews and deep-dives with commercial, sales and platform partners, turning findings into prioritised action plans; lead a designer and a social media executive",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's e-commerce marketplace | 100K+ employees | platform side",
            "bullets": [
                "Owned the Flash Sales channel for Beauty, Fashion & Home reporting to the CEO — plans tied to P&L targets, revenue pacing and corrective action on shortfalls; analysed ROI, ROAS, conversion, traffic and retention across 42 accounts, +30% GMV QoQ",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce platform | €500M+ revenue",
            "bullets": [
                "Drove GMV on XL accounts through data-led planning and in-app promotional mechanics across functions",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | Nielsen",
            "bullets": [
                "Ran sell-in/sell-out and promotional-effectiveness analysis with Nielsen, building category performance reports behind NPD launches",
            ],
        },
    ],
    "skills_brand": (  # -> "Analysis & Insight"
        "performance deep-dives, post-campaign reviews, incrementality & control-group measurement, KPI definition, measurement frameworks, executive summaries"
    ),
    "skills_ecommerce": (  # -> "Retail Media & Channels"
        "retail media as advertiser (talabat, Noon, Careem), Meta Ads, Google Ads, campaign optimisation levers, budget pacing, marketplace & q-commerce mechanics"
    ),
    "skills_commercial": (  # -> "Commercial"
        "revenue drivers, P&L exposure, forecasting, pricing & promotional ROI, partner and stakeholder management across markets"
    ),
    "skills_data": (  # -> "Data & BI"
        "Power BI, Tableau, Looker, Excel modeling (Advanced), Nielsen, segmentation & cohort analysis, AI-automated analysis and dashboards"
    ),
    "skills_tools": (  # -> "Tools"
        "Power BI, Tableau, Looker, Excel & Google Sheets, Nielsen, Kantar, Salesforce, SAP, Meta Ads Manager, Google Ads, Claude (AI agents)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Analysis & Insight",
    "E-Commerce & Digital": "Retail Media & Channels",
    "Commercial": "Commercial",
    "Data & Analytics": "Data & BI",
}


def make_job() -> Job:
    return Job(
        id="talabat-sr-specialist-retail-media-insight-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE (On-site)",
        url="https://www.linkedin.com/jobs/search/?keywords=talabat%20Sr%20Specialist%20Retail%20Media%20Insight%20Dubai",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "talabat Sr. Specialist Retail Media Insight Dubai",
            "note": "Rol REGIONAL de analítica dentro de retail media en talabat (Delivery Hero). Paula "
                    "conoce el retail media de talabat desde el lado del anunciante, no desde el de la "
                    "plataforma, y ese es el eje del puesto (revenue leakage, pacing, inventario, "
                    "monetización). Su mejor baza es el rigor de medición: grupo de control e "
                    "incrementalidad, y la auditoría del reporting de la agencia. Brechas duras: compra "
                    "programática, modelos de atribución formales, modelado predictivo y experiencia "
                    "platform-side de monetización. Árabe preferido y no lo tiene. 1.208 solicitudes.",
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
        "ai_score": 58, "ai_tier": "Warm",
        "skills_match": [
            "Anunciante real en el retail media de talabat, Noon y Careem — conoce el producto desde quien paga",
            "Medición con grupo de control e incrementalidad: justo el debate de atribución del retail media",
            "Auditoría del reporting de agencia (reach estimado, doble conteo) — encaja con 'estandarizar frameworks de medición' y 'alinear definiciones de KPI'",
            "Multi-mercado de verdad: 50+ países en GCC, MENA, Asia, Europa, USA y África",
            "FMCG puro, que el JD marca como preferido: DoFreeze hoy, Mondelez con Nielsen al principio",
            "Miravia platform-side: Flash Sales con P&L reportando al CEO, pacing contra objetivo",
            "Stack de BI (Power BI, Tableau, Looker) y Excel avanzado; dashboards automatizados con IA",
        ],
        "missing_skills": [
            "Compra programática — no la ha hecho",
            "Modelos de atribución formales y modelado predictivo como disciplina",
            "Lado plataforma del retail media: revenue leakage, pacing de inventario, gaps de monetización",
            "Gestión del performance de equipos locales en varios países",
            "Grado en Estadística / Business Analytics (tiene BBA en CUNEF)",
            "Árabe (preferido en el JD)",
        ],
        "sector_fit": "muy alto — q-commerce y FMCG en EAU es su terreno",
        "seniority_fit": "ajustado — Sr. Specialist regional con perfil muy analítico; ella viene del lado comercial/marca",
        "red_flags": [
            "1.208 solicitudes, 71 en un día — la más competida de todas las vistas",
            "El JD pide perfil cuantitativo puro (Estadística/Analytics/Ingeniería) y programática; ella es comercial con buena analítica",
            "Árabe preferido",
            "Presencial",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "El encaje aquí es de mentalidad, no de currículum. Lo que el puesto premia — desconfiar de la "
            "métrica que te da la plataforma, medir incrementalidad contra un control, reconstruir las "
            "definiciones de KPI cuando no cuadran — Paula lo ha hecho de verdad y tiene la historia de la "
            "auditoría de agencia para demostrarlo, que es mejor material que el de la mayoría de "
            "candidatos comerciales. Lo que no tiene es el perfil técnico que el JD describe: programática, "
            "atribución formal, modelado predictivo y el lado plataforma de la monetización. Con 1.208 "
            "solicitudes y un filtro académico cuantitativo, la probabilidad por Easy Apply es baja. Si "
            "quiere invertir aquí, la vía es el contacto dentro de talabat y un mensaje que lidere con el "
            "caso de incrementalidad de SMASH, no el envío en frío. Entre las tres de hoy, esta es la "
            "tercera en prioridad."
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
