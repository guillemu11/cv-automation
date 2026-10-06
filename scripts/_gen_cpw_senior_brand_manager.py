"""One-off: CV de una página para **Senior Brand Manager** en **Cereal Partners Worldwide** (joint venture
Nestlé & General Mills: NESQUIK, FITNESS, CHEERIOS, CHOCAPIC). Dubái. Publicada en el portal de carreras de
Nestlé (req. 17327). Es la vacante "Senior" que CPW abrió a la vez que el Brand Manager del 2026-10-01
(`_gen_cpw_brand_manager.py`).

Pide el JD: estrategia, crecimiento y ejecución de las marcas de inversión; bajar la visión global a planes
regionales; **Annual Growth Plans y Brand Long-Term Plan a 3 años**; pipeline de **innovación y renovación** con
Technical / R&D; **líder regional del portafolio Breakfast Cereals** (estrategia de crecimiento de categoría).
Día a día: segmentos prioritarios de consumidor e insights; Brand Essence y posicionamiento; LTPs y planes
anuales con agencias; comunicación **RED** (Relevant, Easy, Distinctive); ejecución de campañas en todos los
touchpoints; cultura de **test, learn & optimise** con equipos de medios y medición; innovación y renovación.
Requisitos: **experiencia extensa en marketing FMCG (esencial)**; **experiencia probada en campañas ATL**;
nivel mercado y/o regional **gestionando varios países de MENA**; agencia (deseable); datos y analítica fuertes;
equipos multifuncionales. No pide árabe.

Ángulo honesto de Paula:
- Test & learn es su punto más fuerte y el que más distingue: SMASH × talabat +165% vs +4,7% del grupo de
  control (Befit); Befit × Noon +31% sobre baseline (+4.176 uds incrementales); auditó el informe de la agencia.
- Innovación: 6 NPD end-to-end (brief, packaging, pricing, go-to-market) en DoFreeze; apoyo a Milka Spread y
  Mini Suchard en Mondelez.
- Calendario anual de activación por ocasiones de consumo (Ramadán, back to school, Fitness Month, New Year)
  para tres marcas de alimentación vendidas en 50+ mercados.
- Briefs creativos para un equipo de dos y cuatro agencias; 103 activaciones de creator en 3 campañas.
- "Emerging capabilities": sistema de IA con Claude (~40% menos trabajo manual).
- Multifuncional: sales, distribuidores, e-commerce y plataformas; lado cliente en Miravia y Glovo.

Guardarraíles de honestidad:
- **ATL**: no ha hecho TV, exterior ni radio. Su media es paid social, search, creators, sampling e in-app.
  No aparece "ATL" ni "through-the-line" en el CV.
- **Gestión regional de varios países MENA con equipos locales**: no. En DoFreeze ella es la central y adapta
  por mercado y canal para exportación. Se dice así.
- **Brand LTP a 3 años / Brand Essence formal / segmentación cuantitativa / brand health tracking**: no consta.
  Se habla de calendario anual y de ocasiones de consumo, no de LTP ni de brand essence.
- **Cereal / desayuno**: no lo ha trabajado. Befit es nutrición better-for-you.
- **Renovación con R&D**: no consta. Se dice "brief, packaging, pricing and go-to-market", sin inventar R&D.
- **Seniority**: ~5 años (ago-2021 → hoy) frente a "extensive". El resumen dice 5.
- **Forecast**: lo cierra la e-commerce manager; no aparece.
- **Deliveroo**: DoFreeze NO está. Plataformas: talabat, Noon, Careem.
- Creators: "103 activaciones en 3 campañas". Equipo: "team of two (designer + social media executive)".
- Visa: "UAE Employment Visa (employer-sponsored)" (cabecera desde profile.yaml); nunca "no sponsorship".
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

COMPANY = "Cereal Partners Worldwide"
TITLE = "Senior Brand Manager"
DATE_FOLDER = "2026-10-06"

JOB_DESCRIPTION = """\
Senior Brand Manager. Cereal Partners Worldwide (Nestlé & General Mills). Dubai, UAE. Requisition 17327.
Position Summary: As Senior Brand Manager, you will lead the strategy, growth, and execution of key investment
brands, translating global vision into impactful regional plans that drive consumer engagement and business
performance. Working across multiple markets, you will develop distinctive brand strategies, lead Annual Growth
Plans and the three-year Brand Long-Term Plan, and build a strong innovation and renovation pipeline in
partnership with cross-functional teams. As the regional lead for the Breakfast Cereals portfolio, you will define
the category growth strategy, unlock new opportunities, and accelerate the performance of existing brands.
Combining consumer insight, commercial acumen, and creative thinking, you will deliver campaigns and initiatives
that strengthen brand equity, drive demand, and create sustainable growth across the region.
A day in the life: Know your consumer deeply (priority segments by attractiveness and business opportunity;
translate consumer and market insights into actionable strategies; consumer needs, behaviours, motivations and
perceived brand value). Build and strengthen brand foundations (shape and refine the Brand Essence and positioning;
partner with cross-functional and regional stakeholders to ensure consistency across markets; incorporate local
perspectives from key markets). Deliver outstanding marketing experiences (lead Long-Term Plans and Annual Brand
Plans with consumer insights, brand strategy, business priorities and agency expertise; translate plans into
short-term execution and a multi-year pipeline of growth opportunities; consumer-centric communication that is
Relevant, Easy and Distinctive (RED) with agencies, regional teams and key markets; excellence in campaign
execution across touchpoints). Drive a culture of testing, learning and optimization (champion innovative
marketing approaches and emerging capabilities; work with media and measurement teams to evaluate campaign
effectiveness and optimize marketing investments; use data, insights and experimentation). Lead innovation and
renovation initiatives with Technical, R&D and cross-functional teams; ensure a robust pipeline.
What will make you successful: extensive experience in Marketing within FMCG is essential; proven expertise in
developing and executing Above-the-Line (ATL) communication campaigns; experience working at a Market and/or
Regional level managing multiple countries across MENA; previous experience with or within a creative, media or
marketing agency would be an advantage; strong data and analytics capabilities, translating insights into business
actions; experience working within Cross-Functional Teams (CFTs) and collaborating across multiple stakeholders.
"""

ATS = [
    "senior brand manager", "brand management", "brand strategy", "brand equity", "brand positioning",
    "FMCG", "food", "breakfast cereals", "category growth", "consumer insights", "consumer segments",
    "consumer occasions", "annual brand plan", "annual growth plan", "long-term plan", "activation calendar",
    "innovation", "renovation", "NPD", "product launches", "pipeline", "go-to-market", "packaging",
    "integrated campaigns", "campaign execution", "consumer touchpoints", "creative briefs", "agencies",
    "agency management", "RED communication", "ATL", "media", "digital media", "Meta Ads", "Google Ads",
    "creators", "sampling", "test and learn", "experimentation", "optimization", "campaign effectiveness",
    "control group", "incrementality", "marketing investment", "ROI", "ROAS", "data and analytics", "Nielsen",
    "sell-in", "sell-out", "cross-functional teams", "stakeholder management", "sales", "distributors",
    "trade marketing", "modern trade", "quick-commerce", "multi-market", "regional", "GCC", "MENA",
    "team leadership", "generative AI", "emerging capabilities",
]

CONTENT = {
    "headline": "Senior Brand Manager · FMCG Food · Activation, Innovation & Test-and-Learn · GCC",
    "professional_summary": (
        "FMCG brand marketer in Dubai with 5 years across food, beauty and e-commerce (Mondelez, Alibaba, Glovo). "
        "Leads brand, activation and 6 NPD launches for three food brands sold in 50+ markets, manages a team of "
        "two, and measures every campaign on sell-out against a control group."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE F&B / FMCG group | Befit (better-for-you nutrition), Eurocake, Flair | GCC + 50+ markets",
            "bullets": [
                "Own the annual activation calendar for three food brands, built on consumer occasions (Ramadan, back to school, Fitness Month, New Year), adapting plans by market and channel with sales and distributors across modern trade and quick-commerce",
                "Lead 6 NPD launches end-to-end (brief, packaging, pricing, go-to-market) across GCC, MENA, Asia, Europe, USA and Africa",
                "Write the creative briefs for a team of two (designer + social media executive) and four agencies: 103 creator activations over three campaigns, 30% negotiated off. Built a Claude AI workflow for planning, content and reporting (~40% less manual work)",
                "Test, learn and reallocate on sell-out: SMASH × talabat lifted daily sales +165% vs +4.7% for a control brand; Befit × Noon added 4,176 incremental units (+31% over baseline). Audited agency reach reports; A/B test Meta & Google creatives on ROI/ROAS",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Grew 42 brand accounts (incl. KIKO Milano) +30% GMV QoQ through assortment, pricing and promotional plans; created the Beauty Club and Hot on Social projects with social, content and commercial teams",
                "Owned the Flash Sales channel for Beauty, Fashion & Home reporting to the CEO, reading promotional ROI, conversion and retention to reallocate investment",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce leader | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Managed XL accounts (KFC, Taco Bell, La Tagliatella) on GMV and joint marketing activations, coordinating marketing, logistics and customer support to deliver campaigns",
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
    "skills_brand": (  # -> "Brand & Innovation"
        "brand strategy, activation calendar, consumer occasions, 6 NPD launches, briefs, team of two"
    ),
    "skills_ecommerce": (  # -> "Communication & Media"
        "integrated campaigns, 4 agencies, creators & sampling, Meta & Google Ads, social, quick-commerce"
    ),
    "skills_commercial": (  # -> "Cross-Functional"
        "sales & distributors, trade & shopper marketing, modern trade, key accounts, A&P budgets"
    ),
    "skills_data": (  # -> "Test & Learn"
        "control groups, incremental sell-out, post-campaign reviews, Nielsen, ROI & ROAS, A/B testing"
    ),
    "skills_tools": (  # -> "Tools"
        "Excel & PowerPoint (Advanced), Power BI, Nielsen, SAP, Salesforce, Canva & Adobe, Claude (AI)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Brand & Innovation",
    "E-Commerce & Digital": "Communication & Media",
    "Commercial": "Cross-Functional",
    "Data & Analytics": "Test & Learn",
}


def make_job() -> Job:
    return Job(
        id="cpw-senior-brand-manager-dubai-2026-10",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE",
        url="https://www.nestle.com/jobs/search-jobs?keyword=Senior%20Brand%20Manager%20Dubai",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "Cereal Partners Worldwide Senior Brand Manager Dubai",
            "note": "Portal de carreras de Nestlé, req. 17327. Líder regional del portafolio Breakfast Cereals. "
                    "Abierta a la vez que el Brand Manager de CPW en Dubái (cpw-brand-manager-dubai-2026-10), "
                    "probablemente el mismo equipo. No pide árabe. Requisitos duros que no cumple: experiencia "
                    "probada en campañas ATL y gestión regional de varios países MENA; FMCG 'extensive' frente a "
                    "~5 años. Encaje fuerte en test & learn con grupo de control, NPD y calendario por ocasiones.",
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
        "ai_score": 60, "ai_tier": "Warm",
        "skills_match": [
            "Test & learn medido con grupo de control: SMASH × talabat +165% vs +4,7%; Befit × Noon +31%",
            "6 lanzamientos NPD end-to-end, que encajan con el pipeline de innovación",
            "FMCG de alimentación hoy: Befit, Eurocake y Flair, vendidas en 50+ mercados",
            "Calendario anual de activación por ocasiones de consumo (Ramadán, back to school, Fitness Month, New Year)",
            "Briefs creativos para su equipo de dos y para cuatro agencias",
            "Datos: Nielsen y sell-in/sell-out en Mondelez; auditoría del informe de la agencia",
            "Trabajo multifuncional con sales, distribuidores y plataformas; lado cliente en Miravia y Glovo",
            "IA como capacidad emergente: sistema con Claude (~40% menos trabajo manual)",
        ],
        "missing_skills": [
            "Campañas ATL (TV, exterior, radio): requisito y no las ha hecho",
            "Gestión regional de varios países MENA con equipos locales",
            "Experiencia FMCG 'extensive': tiene ~5 años en total, 2 de ellos en FMCG",
            "Brand Long-Term Plan a 3 años y Brand Essence formal",
            "Categoría cereal / desayuno",
            "Experiencia en agencia (deseable)",
        ],
        "sector_fit": "muy bueno — FMCG de alimentación, innovación y activación multi-mercado",
        "seniority_fit": "por debajo — Senior BM de multinacional suele pedir 7+ años y ATL; ella tiene ~5",
        "red_flags": [
            "ATL es requisito explícito y su media es digital, creators y sampling",
            "Mismo equipo que el Brand Manager de CPW: conviene aplicar también a ese, que es el encaje realista",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "El trabajo encaja con lo que Paula hace hoy en DoFreeze: calendario anual por ocasiones, seis "
            "lanzamientos NPD y una cultura de test & learn medida con grupo de control, que es justo el pilar "
            "de 'testing, learning and optimization' del JD. El problema es el nivel. Pide experiencia FMCG "
            "extensa, campañas ATL probadas y gestión regional de varios países MENA, y Paula tiene ~5 años, "
            "media digital y exportación desde una central. Vale la pena aplicar, pero el Brand Manager de "
            "CPW abierto a la vez es el encaje más realista."
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
