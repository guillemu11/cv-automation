"""One-off: CV de una página para **VP, Growth Content & Creator Commerce** — búsqueda de **Drayton**
(headhunter de consumo) para un cliente confidencial. Dubái, híbrido. LinkedIn Easy Apply, 345 solicitudes,
33% nivel Director y 8% nivel VP.

Pide el JD: construir desde cero el motor de Growth Content & Creator Commerce que impulse la **adquisición de
clientes** en un **portafolio multimarca** de un e-commerce disruptivo ($0→400M de facturación en 3 años, ahora
en expansión internacional). Perfil ideal: **rigor comercial + instinto creativo** y conocimiento del
consumidor digital; entornos **rápidos y emprendedores**; **influencia y gestión de stakeholders** alineando
creatividad y negocio; **fluidez práctica en IA con ejemplos de workflows que haya implantado personalmente**;
líder low ego / high EQ que responde por resultados. No pide árabe.

Ángulo honesto de Paula (el contenido del puesto es casi exactamente lo que hace en DoFreeze):
- Creó el programa de creators **desde cero** (antes no había nada) en Befit y Eurocake (lanzamiento de SMASH),
  con campañas todo el año en picos estacionales y siempre dirigidas a venta (talabat, Noon, Careem, Shopify).
- Rigor comercial: SMASH × talabat +165% vs +4,7% del grupo de control (Befit); Befit × Noon +4.176 uds
  incrementales (+31% sobre baseline); AED 81 por pieza de contenido; auditó el informe de la agencia.
- IA hecha por ella: sistema con Claude (~40% menos trabajo manual); programa de afiliación con landing hecha con
  agentes de IA y avatar de IA que explica el brief en varios idiomas.
- Partnerships más allá del creator individual: sorteo con talabat (cada compra = participación), samplings,
  comunidades de running, pádel y yoga.
- Equipo de dos; negoció -30% con la agencia y le entregaron 103 creators frente a 75 contratados.

Guardarraíles de honestidad:
- **Seniority**: es un VP y ella es Brand & Marketing Manager con ~5 años y un equipo de dos. No se pone "VP" ni
  "Head" en ningún sitio; el titular describe la función, no el cargo.
- **Agencias**: alist (3 campañas), Yamammi (cerrando), Amplify (en evaluación), Terrier (evaluada). Se dice
  "ran selection across four creator agencies", no "managed four agencies".
- **Afiliación**: no hay cifras de resultados; se describe sin inventar números.
- Creators: "103 activaciones en 3 campañas", nunca "una campaña con 103". Flair no tuvo campañas de creators.
- **Forecast**: lo cierra la e-commerce manager; no aparece. **Shopify**: suyo de principio a fin.
- **Deliveroo**: DoFreeze NO está. Plataformas: talabat, Noon, Careem.
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

COMPANY = "Drayton (confidential client)"
TITLE = "VP Growth Content & Creator Commerce"
DATE_FOLDER = "2026-10-06"

JOB_DESCRIPTION = """\
VP, Growth Content & Creator Commerce. Drayton (executive search) for a confidential client. Dubai, UAE. Hybrid,
full-time. We are currently working with a really exciting brand, a business that is one of the most exciting
growth stories in their industry. The business has grown from $0-400m turnover in the last 3 years and is now
entering into a key stage of their journey: international expansion and the best in class people to help lead the
business on this exciting journey. One of the key roles that we are supporting them with is a VP of Growth Content
and Creator Commerce. This role will be responsible for building their Growth Content & Creator Commerce engine
that will power customer acquisition across a multi brand portfolio. This is a genuine growth opportunity for an
individual excited by creating scalable capability from the ground up for an industry disruptive ecommerce
business.
The Ideal Profile: An individual who combines commercial rigour with strong creative instincts and a deep
understanding of digital consumers. Thrives in fast paced, entrepreneurial environments where ambiguity, pace and
change are constants. Possesses strong influencing and stakeholder management skills, with the ability to align
creative and commercial objectives. Brings hands on AI fluency and can demonstrate practical examples of AI enabled
workflows they have personally implemented. A low ego, high EQ leader who brings energy, curiosity and a
collaborative approach whilst maintaining accountability for results.
"""

ATS = [
    "growth content", "creator commerce", "creator marketing", "influencer marketing", "creator programme",
    "affiliate marketing", "affiliates", "UGC", "usage rights", "content strategy", "social commerce",
    "customer acquisition", "growth marketing", "performance marketing", "Meta Ads", "Google Ads",
    "e-commerce", "D2C", "Shopify", "marketplaces", "quick-commerce", "talabat", "Noon", "Careem",
    "multi-brand portfolio", "brand portfolio", "product launches", "seasonal campaigns", "communities",
    "platform partnerships", "sampling", "seeding", "agency management", "agency selection", "negotiation",
    "commercial rigour", "incrementality", "control group", "incremental sales", "cost per content",
    "ROI", "ROAS", "A/B testing", "measurement", "reporting", "AI fluency", "AI-enabled workflows",
    "generative AI", "AI agents", "Claude", "AI avatar", "AI video", "automation", "build from zero",
    "scalable capability", "entrepreneurial", "fast-paced", "stakeholder management", "team leadership",
    "digital consumer", "GCC", "UAE", "international expansion",
]

CONTENT = {
    "headline": "Growth Content & Creator Commerce · Hands-on AI",
    "professional_summary": (
        "Consumer marketer in Dubai with 5 years across FMCG, marketplaces and quick-commerce (Mondelez, Alibaba, "
        "Glovo). Built a creator-commerce engine from zero for a multi-brand food group, measures it on "
        "incremental sales against control groups, and runs it on AI workflows built hands-on."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE F&B / FMCG group | Befit, Eurocake (incl. SMASH), Flair | sold in 50+ markets",
            "bullets": [
                "Built the creator programme from zero: year-round campaigns on seasonal peaks (Fitness Month, New Year, Ramadan, back to school) for Befit and the SMASH launch, each driving purchase on talabat, Noon, Careem or our Shopify store, at AED 81 per content piece",
                "Measure on incremental sales, not reach: SMASH × talabat lifted daily sales +165% vs +4.7% for a no-creator control brand; Befit × Noon added 4,176 incremental units (+31% over baseline). Audited agency reports (follower-based reach, double counting)",
                "Hands-on AI: built a Claude system for planning, content and reporting (~40% less manual work), and launched Befit's affiliate programme (commission on sales, no agency) on an AI-agent-built landing page and a multilingual AI avatar briefing creators",
                "Lead a team of two (designer + social media executive); ran selection across four creator agencies, negotiated 30% off (103 creators delivered vs 75 contracted); added a talabat purchase-to-win giveaway and running, padel and yoga communities",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's e-commerce marketplace | 100K+ employees",
            "bullets": [
                "Grew 42 brand accounts (incl. KIKO Milano) +30% GMV QoQ; created the Beauty Club and Hot on Social projects to turn social content into marketplace demand",
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
                "Managed XL accounts (KFC, Taco Bell, La Tagliatella) on GMV and joint marketing activations in a high-growth business, coordinating marketing, logistics and customer support",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | chocolate category (Milka, Suchard)",
            "bullets": [
                "Ran sell-in/sell-out and promo-effectiveness analysis with Nielsen; supported NPD launches (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": (  # -> "Creator Commerce"
        "creator programmes from zero, affiliates, UGC with usage rights, communities, sampling"
    ),
    "skills_ecommerce": (  # -> "AI Workflows"
        "Claude / Claude Code agents, AI landing pages, multilingual AI avatars, AI video, automated reporting"
    ),
    "skills_commercial": (  # -> "Growth & Acquisition"
        "Meta & Google Ads, Shopify D2C, talabat, Noon & Careem, marketplaces, 6 NPD launches"
    ),
    "skills_data": (  # -> "Commercial Rigour"
        "control groups, incremental units, cost per content, agency audits, ROI & ROAS, A/B tests, Nielsen"
    ),
    "skills_tools": (  # -> "Tools"
        "Excel & PowerPoint (Advanced), Power BI, Shopify, Meta Business Suite, Canva & Adobe, Higgsfield"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Creator Commerce",
    "E-Commerce & Digital": "AI Workflows",
    "Commercial": "Growth & Acquisition",
    "Data & Analytics": "Commercial Rigour",
}


def make_job() -> Job:
    return Job(
        id="drayton-vp-growth-content-creator-commerce-dubai-2026-10",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE (Hybrid)",
        url="https://www.linkedin.com/jobs/search/?keywords=VP%20Growth%20Content%20Creator%20Commerce%20Drayton",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "Drayton VP Growth Content & Creator Commerce Dubai",
            "note": "LinkedIn, Easy Apply, publicada hace ~3 semanas por un recruiter de Drayton. 345 solicitudes "
                    "(33% nivel Director, 8% VP). Cliente confidencial: e-commerce multimarca de $0 a $400M en "
                    "3 años, en expansión internacional. No pide árabe. El contenido del puesto encaja casi "
                    "punto por punto; el problema es el nivel VP.",
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
        "ai_score": 50, "ai_tier": "Stretch",
        "skills_match": [
            "Creó el programa de creators desde cero en DoFreeze: exactamente 'build from the ground up'",
            "Creator commerce real: todas las campañas mandan a comprar a talabat, Noon, Careem o Shopify",
            "Rigor comercial: SMASH × talabat +165% vs +4,7% del grupo de control; Befit × Noon +31%",
            "IA implantada por ella: sistema con Claude (~40%), landing de afiliación con agentes, avatar multilingüe",
            "Portafolio multimarca (Befit, Eurocake/SMASH, Flair) y lanzamiento de marca nueva con creators",
            "Programa de afiliación sin agencia, comunidades y partnership de plataforma con talabat",
            "Coste por pieza AED 81 y auditoría del informe de la agencia",
            "Entornos rápidos: Glovo, Miravia (Alibaba) y una PYME de FMCG en Dubái",
        ],
        "missing_skills": [
            "Nivel VP: tiene ~5 años y lidera un equipo de dos",
            "Escala: el cliente factura $400M; DoFreeze es mucho más pequeña",
            "Expansión internacional liderando equipos en varios países",
            "Adquisición de clientes D2C a gran escala (CAC, LTV, cohortes)",
            "Experiencia en e-commerce nativo digital / D2C puro (DoFreeze vende sobre todo por plataformas)",
        ],
        "sector_fit": "bueno — consumo y e-commerce; creator commerce y contenido de crecimiento es su terreno",
        "seniority_fit": "muy por debajo — es un VP; 41% de los candidatos son Director o VP",
        "red_flags": [
            "Nivel VP con 345 candidatos, un tercio de ellos Director",
            "Pasa por headhunter: el filtro de nivel lo hará Drayton antes que el cliente",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Lo que el puesto pide hacer es casi exactamente lo que Paula ha hecho en DoFreeze este año: montar "
            "desde cero un programa de creators orientado a venta, medirlo con grupo de control y apoyarlo en "
            "workflows de IA que ha construido ella. Pocas candidatas pueden enseñar ejemplos de IA tan concretos. "
            "El problema es el nivel: es un VP para un negocio de $400M y ella tiene ~5 años y un equipo de dos. "
            "Merece la pena aplicar porque es Easy Apply y el contenido es muy suyo, pero lo más probable es que "
            "Drayton la descarte por nivel. Escribir al recruiter puede servir para otras búsquedas de Drayton "
            "en consumo en Dubái."
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
