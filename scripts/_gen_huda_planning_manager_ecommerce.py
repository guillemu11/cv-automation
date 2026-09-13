"""One-off: generate Paula's CV for **Planning Manager - eCommerce** at **Huda Beauty**
(Dubai, on-site — LinkedIn "evaluando activamente" 2026-09-02; Indeed posting 2026-07-24).

READ THIS FIRST — the title is misleading. Despite "eCommerce" in the name, this is a
**demand planning / supply chain** role, not an e-commerce trading or merchandising role.
The JD asks for 5–8 years in demand planning, business planning or supply chain; forecast
accuracy as the primary KPI; driver-based forecasting models; FuturMaster or equivalent planning
tools; S&OP and monthly demand review cycles; inventory health across markets (stock-outs,
overstock, ageing stock, excess provisions); ERP and Power BI. Paula has never held a demand
planning or supply chain role and has never used FuturMaster. This package is generated because
Paula asked for it, but it is an honest long shot — see 04_Aplicacion/LEEME_ANTES_DE_APLICAR.md.

Paula's honest angle (the real overlap, and it is genuine as far as it goes):
- CATEGORY PLANNING FOUNDATIONS: at Mondelez she did sell-in/sell-out analysis, promotional
  effectiveness measurement and performance reporting for the chocolate category — the exact
  discipline this role industrialises.
- PRODUCT LIFECYCLE PLANNING: she runs NPD end-to-end for 6 launches across 50+ markets — launch
  phasing, assortment decisions, pricing and go-to-market timing, which is the "manage end-to-end
  product lifecycle planning, including new launches, assortment updates and discontinuations"
  line in the JD.
- PROMO / CALENDAR ALIGNMENT: she builds the trade and shopper calendar by channel and aligns
  sampling, seeding and promotional mechanics with it — the JD's "align planning outputs with
  promotional strategy, marketing calendar, GWP/sampling and bundling initiatives".
- EARLY-SIGNAL REFORECASTING: at Miravia she owned Flash Sales for Beauty/Fashion/Home reporting
  to the CEO, sizing uplift events and reacting to early sales signals, and grew 42 accounts
  +30% GMV QoQ through assortment and pricing decisions read off performance data.
- TOOLS AND DATA: Shopify (JD "preferred"), Power BI (JD "preferred"), advanced Excel, large
  dataset analysis, retail mathematics.
- BEAUTY: two years running beauty, fragrance and fashion accounts — the JD's preferred industry.

Honesty guardrails: NO demand planning or supply chain job title is claimed. NO FuturMaster, no
ERP ownership, no S&OP process ownership, no inventory or stock-provision accountability, no
forecast-accuracy KPI ownership. The CV says "commercial and category planning", "forecast inputs"
and "launch phasing" — all true — and never says "demand planner" or "supply chain". No Arabic.
Factual "UAE Residence Visa" only — never "no sponsorship needed".

ONE-PAGE standard: tight summary, 3/2/1/1 bullets, ~6-9 short skills per row.
Fills the real CV template, relabels the skills rows for this role, converts to PDF via
LibreOffice, registers the job, verifies 1 page, lands under output/2026-09-03/.
Also drops a short-named 'Paula De Francisco - CV.pdf' copy for portals / Easy Apply.
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

COMPANY = "Huda Beauty"
TITLE = "Planning Manager - eCommerce"
DATE_FOLDER = "2026-09-03"

JOB_DESCRIPTION = """\
Planning Manager - eCommerce — Huda Beauty. Full-time. Dubai, UAE (on-site).
Summary: the Planning Manager - eCommerce plays a critical role in driving data-led decision-making
across a global ecom business. This role owns forecasting and inventory planning processes while
ensuring strong alignment across commercial, finance, marketing and supply chain teams. You will go
beyond execution — challenging assumptions, identifying risks and opportunities proactively, and
influencing business decisions through robust, driver-based planning.
Responsibilities: own business forecasting across all time horizons (weekly to annual), with
accountability for forecast accuracy as the primary KPI; drive adoption and optimisation of planning
tools (e.g. FuturMaster), phasing out manual processes; develop driver-based forecasting models
incorporating marketing plans, launch phasing, distribution strategy, product typology, benchmarks
and early sales signals; partner cross-functionally (commercial, finance, S&OP, supply chain,
operations); actively challenge assumptions to improve forecast integrity; translate data into
actionable recommendations; own demand inputs into monthly demand review cycles; apply commercial
awareness including stock provisions, excess risk and P&L impact; manage end-to-end product
lifecycle planning including new launches, assortment updates and discontinuations; align planning
outputs with promotional strategy, marketing calendar, GWP/sampling and bundling initiatives;
monitor launch and campaign performance and dynamically reforecast on early signals (within ~4–8
weeks); identify risks early (stock-outs, overstock, slow movers) and drive mitigation; manage
inventory health across markets, minimising excess and ageing stock; identify inefficiencies and
drive automation and process improvements across planning workflows; improve tools, dashboards and
planning frameworks.
Requirements: Bachelor's degree in Business, Supply Chain, Analytics or related; 5–8 years in demand
planning, business planning or supply chain; strong analytical capability including retail
mathematics and large dataset analysis; advanced Excel, experience with ERP, Shopify and Power BI
preferred; proven ownership and independent delivery; critical thinking and solution-oriented
mindset; strong cross-functional collaboration; clear structured communication; comfortable in a
fast-paced international environment; experience in beauty, fashion or lifestyle industries
preferred.
"""

ATS = [
    "planning manager", "business planning", "commercial planning", "category planning",
    "demand inputs", "forecasting", "forecast accuracy", "driver-based forecasting",
    "reforecasting", "early sales signals", "launch phasing", "product lifecycle",
    "new product development", "NPD", "assortment planning", "assortment updates",
    "discontinuations", "range planning", "promotional planning", "promotional effectiveness",
    "marketing calendar", "trade calendar", "GWP", "sampling", "bundling",
    "sell-in", "sell-out", "retail mathematics", "large dataset analysis",
    "inventory", "stock availability", "slow movers", "P&L", "commercial acumen",
    "cross-functional", "S&OP", "supply chain alignment", "finance", "operations",
    "eCommerce", "e-commerce", "Shopify", "marketplace", "quick-commerce", "D2C",
    "GMV", "AOV", "conversion", "ROI", "ROAS", "KPI reporting", "dashboards",
    "advanced Excel", "Power BI", "Tableau", "Looker", "ERP", "automation",
    "beauty", "fragrance", "fashion", "lifestyle", "FMCG",
    "Dubai", "UAE", "international",
]

CONTENT = {
    "headline": (
        "Commercial & Category Planning · E-Commerce Performance · Launch Phasing and Assortment "
        "Across 50+ Markets · Beauty & FMCG"
    ),
    "professional_summary": (
        "Commercial and category planner turned brand owner, with 5 years across FMCG, beauty and "
        "e-commerce. Builds the launch, assortment and promotional plan across 50+ markets, feeds the "
        "sales and stock forecasts behind it, and reforecasts off early sell-out signals. Analytical core "
        "from Mondelez category planning; Shopify and Power BI hands-on. Dubai-based."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Consumer brands (Befit, Eurocake, Flair) | 50+ markets | D2C + modern trade",
            "bullets": [
                "Own end-to-end product lifecycle planning for 6 launches across GCC, MENA, Asia, Europe, USA and Africa — launch phasing, assortment decisions, pricing and go-live dates — feeding the sales and stock forecasts behind each market's plan with commercial, supply and distributor teams",
                "Build the promotional and trade calendar by channel and align it with sampling, seeding and bundling mechanics, then read launch performance back within weeks and adjust the plan on early sell-out signals",
                "Run the Shopify business hands-on (catalogue, assortment, availability, offers, pricing) and report weekly on category and SKU performance in Power BI, automating the reporting itself with an AI system that cut manual workload ~40%",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba Group's marketplace in Spain | Top-5 global e-commerce | 100K+ employees",
            "bullets": [
                "Grew 42 beauty, fragrance and fashion accounts +30% GMV QoQ through assortment optimisation, pricing strategy and targeted promotions, tracking SKU-level performance to decide what to push, reprice or delist",
                "Owned the Flash Sales channel for Beauty, Fashion and Home reporting to the CEO — sizing uplift events against P&L targets, planning the promotional calendar and reforecasting off early trading signals",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | Category planning & analytics",
            "bullets": [
                "Ran sell-in/sell-out analysis and promotional effectiveness measurement for the chocolate category, building the performance reports that informed launch decisions (Milka Spread, Mini Suchard)",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce platform | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed strategic accounts and helped build the retail vertical from zero, planning assortment and activations across marketing, logistics and operations",
            ],
        },
    ],
    "skills_brand": (  # label -> "Planning & Forecasting"
        "commercial & category planning, launch phasing, product lifecycle (NPD to delisting), "
        "assortment planning, promotional & trade calendar, GWP/sampling & bundling, forecast inputs"
    ),
    "skills_ecommerce": (  # label -> "E-Commerce & Trading"
        "Shopify, marketplace & quick-commerce trading, catalogue & availability management, "
        "pricing, offers & promo mechanics, D2C and modern trade"
    ),
    "skills_commercial": (  # label -> "Commercial & Cross-Functional"
        "P&L awareness, cross-functional alignment (commercial, supply, finance, marketing), "
        "distributor & key account management, 50+ markets, C-level reporting"
    ),
    "skills_data": (  # label -> "Analytics & Reporting"
        "sell-in/sell-out analysis, promotional effectiveness, SKU & category performance, "
        "retail mathematics, large dataset analysis, GMV, AOV, conversion, ROI, weekly KPI reporting"
    ),
    "skills_tools": (  # label -> "Tools"
        "Advanced Excel, Power BI, Tableau, Looker, Google Analytics, Shopify, Salesforce, "
        "Generative AI (Claude, ChatGPT) for planning automation"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Planning & Forecasting",
    "E-Commerce & Digital": "E-Commerce & Trading",
    "Commercial": "Commercial & Cross-Functional",
    "Data & Analytics": "Analytics & Reporting",
}

WARNING = """\
# LÉEME ANTES DE APLICAR — Huda Beauty, Planning Manager - eCommerce

## El título engaña: esto es demand planning, no e-commerce

La oferta se llama "Planning Manager - **eCommerce**", pero la JD real (recuperada de Indeed,
publicada el 24-jul-2026) describe un puesto de **demand planning / supply chain**:

- **KPI principal: forecast accuracy.** Literal: "with accountability for forecast accuracy as the
  primary KPI".
- Piden **5–8 años en demand planning, business planning o supply chain**.
- Herramientas: **FuturMaster** (planificación de demanda), ERP, Power BI.
- Responsabilidades: modelos de forecast driver-based, ciclos mensuales de demand review, **S&OP**,
  salud de inventario por mercado, stock-outs, sobrestock, stock obsoleto, provisiones por exceso.
- Titulación preferida: Business, **Supply Chain** o Analytics.

Paula no ha tenido nunca un puesto de demand planning ni de supply chain, y no ha usado
FuturMaster. Esto no es un matiz: es el 60% de la JD.

## Qué sí se sostiene (y está en el CV, sin inflar)

| Lo que pide la JD | Lo que Paula tiene de verdad |
|---|---|
| Product lifecycle planning: lanzamientos, surtido, discontinuaciones | 6 NPD end-to-end en 50+ mercados, con phasing y fechas de go-live |
| Alinear plan con calendario promocional, GWP/sampling, bundling | Construye el calendario de trade y shopper por canal |
| Reforecast por señales tempranas (4–8 semanas) | Flash Sales en Miravia: dimensionar uplift y reaccionar al dato temprano |
| Retail math, análisis de datasets grandes | Mondelez: sell-in/sell-out y efectividad promocional del chocolate |
| Shopify, Power BI (preferido) | Ambos, hands-on |
| Beauty / fashion / lifestyle (preferido) | 42 cuentas de beauty, fragancias y moda en Miravia |

## Qué NO se dice en ningún sitio

- Nunca "demand planner" ni "supply chain" como título ni como responsabilidad.
- Nada de FuturMaster, ni propiedad de ERP, ni de proceso S&OP.
- Ninguna responsabilidad sobre inventario, provisiones de stock ni forecast accuracy como KPI.
- Nunca "no necesito sponsorship" — visado de residencia EAU patrocinado por su empresa actual.

En el CV va como **"commercial & category planning"**, "forecast inputs" y "launch phasing", que es
exactamente lo que ha hecho.

## Recomendación honesta

Aplicar solo como tiro largo y de bajo coste (la oferta es Easy Apply y está "evaluando
activamente"). No invertir tiempo en referral ni en seguimiento: contra candidatos con 5–8 años de
demand planning puro y FuturMaster, el filtro va a doler.

**La alternativa buena dentro de Huda Beauty:** en `data/scored_jobs.json` ya están registradas dos
ofertas suyas que sí encajan con su perfil —
*Senior Global Brand Marketing Manager - Fragrance* y *Assistant Manager, Global Brand Marketing*.
Esas son la vía real para entrar en Huda.
"""


def make_job() -> Job:
    return Job(
        id="huda-beauty-planning-manager-ecommerce-dubai-2026-09",
        title=TITLE,
        company=COMPANY,
        location="Dubai, United Arab Emirates",
        url="https://to.indeed.com/aakpllfqwzx8",
        source="indeed",
        description=JOB_DESCRIPTION,
        raw={
            "query": "Huda Beauty Planning Manager eCommerce Dubai",
            "indeed_url": "https://to.indeed.com/aakpllfqwzx8",
            "note": "TITLE IS MISLEADING — despite 'eCommerce' this is a demand planning / supply chain "
                    "role: forecast accuracy is the primary KPI, FuturMaster is the named tool, and they "
                    "ask for 5-8 years in demand planning, business planning or supply chain. Paula has "
                    "never held a planning or supply chain role. Surfaced on LinkedIn 2026-09-02 as "
                    "'evaluando activamente' with Easy Apply; original Indeed posting 2026-07-24. "
                    "Generated at Paula's explicit request as a low-cost long shot. Better Huda routes "
                    "already in the pipeline: Senior Global Brand Marketing Manager - Fragrance and "
                    "Assistant Manager, Global Brand Marketing.",
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
        "salary_raw": None, "salary_aed_min": None, "salary_aed_max": None,
        "posted_date": "2026-07-24", "raw": job.raw,
        "ai_score": 48, "ai_tier": "Cold",
        "skills_match": [
            "End-to-end product lifecycle planning: 6 NPD launches across 50+ markets with launch phasing, assortment decisions and go-live dates",
            "Aligns planning with the promotional strategy, marketing calendar, sampling/seeding and bundling mechanics — a named JD responsibility",
            "Reforecasting off early signals: owned Flash Sales for Beauty/Fashion/Home at Miravia, sizing uplift events against P&L targets",
            "Category planning foundations at Mondelez — sell-in/sell-out analysis and promotional effectiveness for the chocolate category",
            "Retail mathematics and SKU-level performance analysis: 42 accounts grown +30% GMV QoQ via assortment and pricing decisions",
            "Shopify and Power BI hands-on (both listed as preferred), plus advanced Excel",
            "Beauty, fragrance and fashion background — the JD's preferred industry",
        ],
        "missing_skills": [
            "No demand planning or supply chain role, ever — the JD asks for 5–8 years of exactly that",
            "Never owned forecast accuracy as a KPI, which the JD names as the primary accountability",
            "No FuturMaster or any dedicated demand planning tool; no ERP ownership",
            "No S&OP process ownership and no participation in monthly demand review cycles",
            "No inventory accountability: stock-outs, overstock, ageing stock, excess provisions are all new",
            "No driver-based forecasting model building",
            "5 years total experience vs the 5–8 asked, and none of it in the asked discipline",
        ],
        "sector_fit": "good on industry (beauty/e-commerce), poor on function (demand planning / supply chain)",
        "seniority_fit": "borderline — Manager level matches, but the years asked are in a discipline she has not worked in",
        "red_flags": [
            "Job title says eCommerce but the role is demand planning — easy to misjudge from the LinkedIn listing alone",
            "Primary KPI (forecast accuracy) is something Paula has never owned",
            "Named tool (FuturMaster) is unknown to her",
            "On-site Dubai, no salary published — confirm against the AED 20K/month floor",
            "Posted 2026-07-24 and still open — likely a hard-to-fill specialist brief, i.e. they will hold out for a real planner",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Weak functional fit despite an attractive company and industry. The listing reads like an "
            "e-commerce trading job, but the JD is demand planning: forecast accuracy is the stated primary "
            "KPI, FuturMaster is the named tool, and they want 5–8 years in demand planning, business "
            "planning or supply chain, ideally with a supply chain degree. Paula has never held that role. "
            "The genuine overlap is real but partial — product lifecycle and launch phasing across 50+ "
            "markets, promotional/GWP calendar alignment, reforecasting off early signals at Miravia's "
            "Flash Sales, sell-in/sell-out and promo-effectiveness analysis at Mondelez, plus Shopify, "
            "Power BI and a beauty background. The CV therefore positions her as a commercial and category "
            "planner and never claims a planning or supply chain title, FuturMaster, S&OP or inventory "
            "accountability. Worth a low-cost Easy Apply given the company, not worth referral effort. The "
            "better Huda routes are the two brand marketing roles already in the pipeline."
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

    warn_dir = final_dir / "04_Aplicacion"
    warn_dir.mkdir(parents=True, exist_ok=True)
    (warn_dir / "LEEME_ANTES_DE_APLICAR.md").write_text(WARNING, encoding="utf-8")
    print("OK_WARNING", warn_dir / "LEEME_ANTES_DE_APLICAR.md")

    try:
        from pypdf import PdfReader
        n = len(PdfReader(str(final_cv)).pages)
        print(f"PAGES {n}", "OK" if n == 1 else "!! SPILLS")
    except Exception as exc:  # noqa: BLE001
        print("page-count check skipped:", exc)

    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
