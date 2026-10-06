"""One-off: CV de una página para **Brand Manager** (LinkedIn lo titula "Manager Brand") en **talabat**
(Delivery Hero), equipo de **Regional Brand**, Dubái, presencial. 8 mercados. Viajes a mercados.
LinkedIn Easy Apply, "Promocionado por técnico de selección". Publicada el 2026-10-06 (hace 4 h al pegarla):
2.640 solicitantes según el panel de insights, 65 en el último día. Paula la tiene guardada.

Pide el JD: plataforma de marca con una idea creativa unificadora y un **sistema operativo por ocasiones** que
ordene campañas, partnerships y canales; presencia en canales emergentes y de alto impacto, con un modelo
**test-and-learn** para social propio que construya brand love más allá de lo promocional; pipeline regional de
**partnerships y patrocinios** puntuados por encaje con la marca y la audiencia; conectar inversión de marca con
resultado comercial (**brand-to-performance**, funnel alto medido hasta conversión); **herramientas de marca con
IA** (guías, precedentes y gobierno de assets accesibles al instante para mercados y agencias); la IA como práctica
diaria del equipo; guías de marca interactivas para los mercados; priorización; monitorización ligera de marca por
mercado; cartera compleja de iniciativas largas.
Requisitos: **8 años** en brand marketing; varias categorías e industrias; creativa y buena comunicadora visual;
IA como multiplicador diario; organización matricial y comunicación virtual; stakeholders; **agencia deseable**;
**inglés y árabe fluidos**.

Ángulo honesto de Paula:
- Ocasiones: el calendario de marca de DoFreeze ya funciona por ocasiones (Fitness Month, New Year New Me,
  Ramadán, back to school) y cada campaña, oleada de creators, sampling y partnership cuelga de él.
- Brand-to-performance, su punto más fuerte: todo el trabajo de marca termina en compra en talabat, Noon, Careem o
  la Shopify propia, y lo mide con grupo de control (SMASH × talabat +165% vs +4,7%; Befit × Noon +31%).
- Conoce talabat desde el lado de la marca: sorteo in-app con tarjetas de cashback de talabat y samplings
  estacionales. Y desde dentro del grupo: Glovo pertenece a Delivery Hero desde jul-2022 (ella entró en sep-2022).
- Partnerships por encaje con la audiencia: comunidades de running, pádel y yoga; programa de creators desde cero
  (103 activaciones en 3 campañas, 4 agencias evaluadas por objetivo).
- IA: sistema de automatización de marketing con Claude (~40% menos trabajo manual), avatar de IA que explica el
  brief de contenido en varios idiomas, landing de afiliación hecha con agentes de IA. Encaja con "AI-powered
  brand tools" y "champion AI as a working practice".
- Varias categorías: alimentación FMCG, chocolate (Mondelez), beauty/fragancia/moda (Miravia), delivery (Glovo).
- Comunicadora visual: dirige a un diseñador y a una social media executive; portfolio en la cabecera.

Guardarraíles de honestidad:
- **8 años**: tiene ~5 (ago-2021 → hoy). El resumen dice 5, no se maquilla.
- **Árabe**: requisito explícito y no lo habla. No se pone, ni "learning". Ver [[paula-no-arabic-hard-filter]].
- **Patrocinios**: no ha llevado ninguno. Se habla de partnerships, nunca de "sponsorship".
- **Agencia**: es lado cliente; gestiona agencias, no ha trabajado en una.
- **Plataforma de marca regional / brand guidelines formales / brand tracking**: no consta. Se habla de calendario
  por ocasiones y de briefs, no de "brand platform" como algo que ya hizo.
- **8 mercados con equipos locales**: no ha coordinado equipos de marca país por país. Sus 50+ mercados son de
  exportación de producto.
- **Forecast**: lo cierra la e-commerce manager; no aparece.
- **Deliveroo**: DoFreeze NO está. Plataformas: talabat, Noon, Careem.
- Creators: "103 activaciones en 3 campañas", nunca "una campaña con 103".
- Equipo: "team of two (designer + social media executive)", sin inflar.
- Visa: "UAE Employment Visa (employer-sponsored)", nunca "no sponsorship".
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
TITLE = "Brand Manager"
DATE_FOLDER = "2026-10-06"

JOB_DESCRIPTION = """\
Brand Manager ("Manager Brand" on LinkedIn) — talabat (Delivery Hero Group). Regional Brand team, Dubai, UAE. On-site,
full time. Covers talabat's 8 markets; travel to markets expected.
We are looking for a passionate Brand Manager to become part of our Regional Brand team located in the Dubai talabat
office. This role is pivotal in bringing to life the brand identity & vision and in building brand love for talabat
across our 8 markets and amongst our employees, vendors and customers. You will help in guiding and shaping initiatives
for these main stakeholders from a brand perspective. You will deep dive into our brand love audience and ensure our
brand communications and activations are well catered to them.
What's on your plate? Build and own a brand platform; develop a unifying creative idea and occasion-led operating
system that every campaign, partnership, and channel expression is built around. Drive brand presence on emerging and
high-impact channels; develop a repeatable test-and-learn model for owned social that builds brand love and engagement
beyond promotional content. Own the regional partnership and sponsorship pipeline; proactively scan culture, score
opportunities against brand identity and audience fit, and drive partnerships that build regional brand equity, not
just commercial deals. Connect brand investment to commercial outcomes; co-develop the brand-to-performance consumer
journey with cross-functional teams, ensuring upper-funnel brand work is measurably linked to conversion. Develop
AI-powered brand tools and intelligence; build or commission AI-assisted systems that give markets and agencies
instant access to brand guidelines, precedents, and asset governance. Champion AI as a working practice; embed AI
tools into team workflows. Evolve how strategy reaches our markets; transform brand guidance into interactive,
searchable, decision-ready tools. Prioritise for strategic impact. Maintain visibility across market-level brand
activity; build a lightweight system for monitoring our brand across markets. Deliver across a complex, high-ambition
portfolio of long-horizon initiatives.
Qualifications: 8 years' experience in brand marketing; experience with a number of categories and industries; highly
creative, change excites you; strong visual communicator; uses AI as a daily force multiplier; complex problem solver;
collaborative team player in a matrix organization across locations, communicating virtually; excellent relationship
and stakeholder management; persuasive and confident communicator; agency background desirable; fluent in English and
Arabic.
"""

ATS = [
    "brand manager", "brand marketing", "brand platform", "brand identity", "brand love", "creative idea",
    "occasion-led", "cultural moments", "Ramadan", "campaigns", "partnerships", "community partnerships",
    "audience fit", "brand equity", "emerging channels", "owned social", "test-and-learn", "engagement",
    "creators", "influencer marketing", "brand-to-performance", "upper funnel", "conversion", "commercial outcomes",
    "control group", "incrementality", "AI-powered tools", "AI", "generative AI", "Claude", "AI agents",
    "brand guidelines", "creative briefs", "visual communication", "art direction", "agency management",
    "matrix organization", "stakeholder management", "cross-functional", "multiple categories", "FMCG", "beauty",
    "fashion", "food delivery", "quick-commerce", "talabat", "Delivery Hero", "Glovo", "GCC", "MENA", "regional",
    "team leadership", "portfolio",
]

CONTENT = {
    "headline": "Brand Manager · Occasion-led Campaigns, Partnerships & Brand-to-Performance · AI-first",
    "professional_summary": (
        "Brand marketer with 5 years across food FMCG, beauty, fashion and food delivery (Glovo, Alibaba). Runs an "
        "occasion-led calendar for three brands in Dubai, ties creator and partnership work to sell-out on talabat "
        "and Noon, and builds the AI tools a team of two uses daily."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "UAE F&B / FMCG group | Befit, Eurocake, Flair | GCC + 50+ markets",
            "bullets": [
                "Run an occasion-led brand calendar for three brands (Fitness Month, New Year New Me, Ramadan, Back to School) that every campaign, creator wave, sampling and partnership is planned around",
                "Link brand work to conversion: creators and partners send shoppers to talabat, Noon, Careem and the brand's Shopify store. SMASH × talabat lifted daily sales +165% vs +4.7% for a control brand; Befit × Noon added 4,176 incremental units (+31%)",
                "Chose partners on audience fit: talabat (in-app giveaway, seasonal samplings), running, padel and yoga communities, and a creator programme built from zero with 4 agencies (103 activations in 3 campaigns, fees negotiated -30%)",
                "Lead a team of two (designer + social media executive) with AI in the daily workflow: built a Claude-based system for planning, content, research and reporting (~40% less manual work) and an AI avatar that briefs creators in several languages",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba's lifestyle marketplace | 100K+ employees",
            "bullets": [
                "Created and led the Beauty Club and Hot on Social projects with social, content and commercial teams, positioning Miravia as a beauty and lifestyle destination; owned the Flash Sales channel, reporting to the CEO",
                "Grew 42 brand accounts (incl. KIKO Milano) +30% GMV QoQ across beauty, fragrance and fashion; onboarded 30+ fragrance stores in two months",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Delivery Hero Group | food delivery & quick-commerce | 10K+ employees",
            "bullets": [
                "Delivered joint marketing activations for XL partners (KFC, Taco Bell, Sushi Shop) with marketing, ops and CX teams; helped build the Retail vertical beyond food",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | chocolate category (Milka, Suchard) | €36B revenue",
            "bullets": [
                "Analysed sell-in/sell-out and promotional effectiveness with Nielsen; supported the Milka Spread and Mini Suchard launches",
            ],
        },
    ],
    "skills_brand": (  # -> "Brand & Creative"
        "occasion-led planning, creative briefs, art direction, brand launches (6 NPD), team of two"
    ),
    "skills_ecommerce": (  # -> "Channels & Partners"
        "owned social, creators & communities, in-app (talabat, Noon, Careem), 4 agencies, Meta Ads"
    ),
    "skills_commercial": (  # -> "AI Practice"
        "Claude & Claude Code, AI agents, AI avatars & video, AI-built landing pages, MCP integrations"
    ),
    "skills_data": (  # -> "Performance"
        "brand-to-conversion, control groups, incremental sell-out, ROI & ROAS, agency report audits"
    ),
    "skills_tools": (  # -> "Tools"
        "Canva, Adobe (Photoshop, Illustrator), Shopify, Meta Ads Manager, Power BI, Notion, Excel"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Brand & Creative",
    "E-Commerce & Digital": "Channels & Partners",
    "Commercial": "AI Practice",
    "Data & Analytics": "Performance",
}


def make_job() -> Job:
    return Job(
        id="talabat-brand-manager-regional-2026-10",
        title=TITLE,
        company=COMPANY,
        location="Dubai, UAE (On-site)",
        url="https://www.linkedin.com/jobs/search/?keywords=talabat%20Manager%20Brand%20Dubai",
        source="manual",
        description=JOB_DESCRIPTION,
        salary_raw=None,
        salary_aed_min=None,
        salary_aed_max=None,
        raw={
            "query": "talabat Manager Brand Dubai",
            "note": "Equipo Regional Brand, 8 mercados, presencial en Dubái, con viajes. LinkedIn Easy Apply, "
                    "promocionado por técnico de selección; 2.640 solicitantes (65 en un día) a las 4 h de publicarse. "
                    "Pide 8 años de brand marketing y árabe fluido (requisito). Advocate interno: Álvaro Martínez "
                    "(Regional Sr. Director). Paula ya pasó RRHH en talabat el 2026-09-09 para Influencer Marketing.",
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
        "ai_score": 62, "ai_tier": "Warm",
        "skills_match": [
            "Calendario de marca por ocasiones ya en marcha (Fitness Month, New Year, Ramadán, back to school)",
            "Brand-to-performance medido con grupo de control: SMASH × talabat +165% vs +4,7%; Befit × Noon +31%",
            "Conoce talabat como marca anunciante (sorteo in-app, samplings) y el grupo desde Glovo (Delivery Hero)",
            "Partnerships por encaje con la audiencia: comunidades de running, pádel y yoga; creators desde cero",
            "IA como práctica diaria: sistema con Claude, avatar de IA que da el brief, landings con agentes",
            "Varias categorías: alimentación, chocolate, beauty, fragancia, moda y delivery",
            "Dirige a un diseñador y a una social media executive; portfolio visual propio",
        ],
        "missing_skills": [
            "Árabe fluido: requisito explícito y no lo habla",
            "8 años de brand marketing: tiene ~5",
            "Patrocinios: no ha llevado ninguno",
            "Plataforma de marca regional y brand guidelines formales para 8 mercados",
            "Experiencia en agencia (deseable)",
        ],
        "sector_fit": "muy bueno — delivery y quick-commerce desde dentro (Glovo) y como marca en talabat",
        "seniority_fit": "por debajo — piden 8 años y ella tiene ~5",
        "red_flags": [
            "Árabe como requisito: probablemente el filtro decisivo",
            "2.640 solicitantes en horas: sin referral la solicitud se pierde",
            "Ya está en proceso con talabat (Influencer Marketing): conviene que Álvaro Martínez sepa que aplica a ambas",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "El contenido del puesto encaja con lo que Paula hace hoy: calendario de marca por ocasiones, "
            "partnerships elegidas por audiencia, trabajo de marca medido hasta la venta con grupo de control "
            "(y precisamente en talabat) e IA metida en el día a día del equipo. Además conoce el grupo desde "
            "Glovo. Le restan dos requisitos duros: árabe fluido, que no habla, y 8 años de brand marketing "
            "frente a ~5. Tampoco ha llevado patrocinios ni una plataforma de marca regional. Con 2.640 "
            "solicitantes, solo tiene sentido si entra referida por Álvaro Martínez."
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
