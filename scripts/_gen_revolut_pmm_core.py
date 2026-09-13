"""One-off: generate Paula's CV for **Product Marketing Manager** (core financial features)
at **Revolut** — remote, based in the UAE. LinkedIn, posted 2026-09-02 (~18h before capture),
100+ clicks on Apply already, promoted by a recruiter, replies handled outside LinkedIn.

JD ask: elevate Revolut's core financial features, establish Revolut as the MAIN ACCOUNT for
millions globally, and communicate value while building customer trust. Own the product marketing
strategy across channels; data-driven quarterly roadmaps that forecast, prioritise and deliver
projects increasing main-account usage; launch strategies end-to-end; value propositions, clear
messaging, creative briefs and launches orchestrated across channels AND geographies; feedback
loops turned into actionable insight; solid cross-functional relationships in a fast-paced env.
Needs: B2B or B2C product/brand/consumer marketing in a fast-paced environment (preferably a
hyper-growth tech company); knowledge of markets and the competitive landscape in fintech or
payments; GTM project management across cross-functional teams; recognition for highly original
ideas; creative excellence while maintaining BRAND INTEGRITY; a solid consumer-marketing track
record across in-product, digital, PR and OFFLINE ACTIVATIONS; exceptional eye for detail.

Difference vs the Crypto PMM version generated the same day: this one is core banking/usage, so the
CV leans on (a) usage/adoption/retention rather than category education, (b) OFFLINE activations —
retail execution, sampling & seeding, modern trade, in-store — which the crypto JD did not ask for,
and (c) originality: programmes she invented from zero (Beauty Club, Hot on Social, the influencer
programme, the AI reporting system), because "recognised for generating highly original ideas" is
an explicit requirement here.

Paula's honest angle:
- PRODUCT MARKETING IS HER DAY JOB, IN FMCG LANGUAGE: NPD end-to-end for 6 launches — brief,
  positioning, pricing, packaging, go-to-market — across GCC, MENA, Asia, Europe, USA and Africa.
  Launch strategy + value proposition + cross-functional execution across geographies is the spine
  of this role.
- HYPER-GROWTH TECH, TWICE: Miravia was Alibaba's brand-new marketplace launch in Spain (owned
  Flash Sales reporting to the CEO, led category expansion) and Glovo was quick-commerce at €500M+
  scale where she helped build the retail vertical from zero.
- ADOPTION, NOT JUST AWARENESS: her metrics are GMV, conversion, AOV, retention and repeat — the
  same shape as "make Revolut the main account", i.e. usage frequency and share of wallet.
- ORIGINAL IDEAS, SHIPPED: Beauty Club and Hot on Social were her own programmes; so was the
  influencer engine built from zero and the AI reporting/planning system (~40% less manual work).
- ALL FOUR CHANNELS THE JD LISTS: in-product/onsite merchandising, digital (Meta/Google/CRM),
  earned media & creators, and genuine OFFLINE activation (modern trade retail execution,
  sampling & seeding, distributor-led launches).
- PROOF OF WORK: she already built and deployed a full fictional Revolut campaign, "No Borders"
  (https://guillemu11.github.io/revolut-no-borders/) — the single biggest differentiator, and it
  speaks directly to this JD's "creative excellence while maintaining brand integrity".

Honesty guardrails: she has NOT worked in fintech, payments, banking or any regulated financial
product — and this JD asks for knowledge of the fintech/payments competitive landscape as a
requirement, not a nice-to-have. The CV claims consumer/product marketing, GTM and hyper-growth
platform experience only — never fintech, never payments, never financial services. No PR-agency
ownership claim (earned media and creator work, phrased as "communications planning"). No Arabic.
Factual "UAE Residence Visa" only — never "no sponsorship needed". Remote role based in the UAE.

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

COMPANY = "Revolut"
TITLE = "Product Marketing Manager"
DATE_FOLDER = "2026-09-03"

JOB_DESCRIPTION = """\
Product Marketing Manager — Revolut. Full-time. Remote, based in the United Arab Emirates.
About Revolut: 80+ million customers, 13,000+ people, products across spending, saving, investing,
exchanging and travelling. Marketing at Revolut is about clarity, creativity and commercial impact;
the Growth team turns bold ideas into campaigns that connect with millions, working across channels
and teams to build a brand that earns attention and drives results.
About the role: a motivated Product Marketing Manager to elevate our core financial features,
establish Revolut as the main account for millions globally, and communicate our value while
building customer trust and value.
What you'll be doing: understanding customer needs and how our core financial features function
globally; leveraging feedback loops and trends to extract data-driven, actionable insights that
inform product marketing strategy; creating and owning the product marketing strategy across
channels; designing impactful, data-driven quarterly roadmaps to forecast, prioritise and deliver
creative projects that increase usage of Revolut as a main account; leading the development and
execution of effective launch strategies; crafting value propositions, formulating clear messaging,
briefing creatives, and orchestrating launches across marketing channels and geographies;
developing solid cross-functional relationships in a fast-paced environment to effectively bring
new products and campaigns to market.
What you'll need: experience in either B2B or B2C product, brand, or consumer marketing in a
fast-paced environment, preferably in a hyper-growth tech company; a passion for Revolut's
products; knowledge of markets and the competitive landscape in fintech or the payments industry;
experience setting strategic direction and project managing complex go-to-market campaigns that
require input from cross-functional teams; to have been recognised for generating highly original
ideas; the ability to set the standard for creative excellence while maintaining brand integrity;
a solid track record in consumer marketing and understanding of channels, including in-product,
digital, PR, and offline activations; excellent communication and interpersonal skills with the
ability to talk to anyone and work in a high-performance environment; an exceptional eye for
detail and quality.
"""

ATS = [
    "product marketing", "product marketing manager", "PMM", "go-to-market", "GTM",
    "launch strategy", "product launch", "product marketing strategy", "roadmap",
    "quarterly roadmap", "prioritisation", "forecasting",
    "value proposition", "positioning", "messaging", "brand integrity", "brand strategy",
    "consumer marketing", "brand marketing", "B2C", "B2B", "campaign strategy",
    "creative briefing", "creative excellence", "art direction", "content strategy",
    "in-product", "onsite merchandising", "digital", "paid social", "Meta Ads",
    "Google Ads", "CRM", "EDM", "PR", "communications", "earned media",
    "influencer marketing", "UGC", "offline activations", "in-store activation",
    "sampling", "retail execution", "modern trade", "shopper marketing", "trade marketing",
    "cross-functional", "stakeholder management", "project management",
    "multi-market", "international", "geographies", "localisation", "expansion markets",
    "customer needs", "customer insight", "feedback loops", "data-driven",
    "actionable insights", "KPI", "performance analysis", "ROI", "ROAS",
    "conversion", "retention", "adoption", "usage", "GMV", "AOV", "A/B testing",
    "experimentation", "marketplace", "platform", "hyper-growth", "fast-paced",
    "e-commerce", "Shopify", "quick-commerce", "Dubai", "UAE", "remote", "generative AI",
]

CONTENT = {
    "headline": (
        "Product Marketing & Go-to-Market · Launch Strategy · Consumer Adoption & Retention · "
        "Hyper-Growth Platforms"
    ),
    "professional_summary": (
        "Consumer product marketer with 5 years across hyper-growth platforms (Alibaba's Miravia, Glovo) "
        "and global consumer brands. Owns launches end-to-end — insight, positioning, value proposition, "
        "channel plan, cross-functional execution — across 50+ geographies, growing usage and repeat, not "
        "just awareness. Dubai-based, available remote."
    ),
    "experience": [
        {
            "company": "DoFreeze LLC",
            "role": "Brand & Marketing Manager",
            "dates": "Oct 2025 – Present",
            "location": "Dubai, UAE",
            "context": "Consumer brands (Befit, Eurocake, Flair) | 50+ markets | D2C, marketplaces & retail",
            "bullets": [
                "Own product marketing end-to-end for 6 launches — customer insight, positioning and value proposition, pricing, messaging and launch phasing — orchestrated across channels and geographies (GCC, MENA, Asia, Europe, USA, Africa)",
                "Set the quarterly roadmap against commercial KPIs and let the data decide it: ROI/ROAS, conversion, repeat and retention feedback loops determine what scales, gets reworked or is cut",
                "Run every channel end-to-end — in-product/onsite merchandising on Shopify (CRO, AOV), paid social and Google Ads, CRM/EDM, 25–50 creators briefed per campaign, and offline activation via sampling, seeding and retail execution — with one brand story across all of them",
            ],
        },
        {
            "company": "Miravia (Alibaba Group)",
            "role": "Key Account Manager – Beauty, Fragrances & Fashion",
            "dates": "Nov 2023 – Oct 2025",
            "location": "Madrid, Spain",
            "context": "Alibaba Group's marketplace launch in Spain | Hyper-growth global tech | 100K+ employees",
            "bullets": [
                "Joined a brand-new Alibaba marketplace at launch and owned the Flash Sales channel for Beauty, Fashion and Home reporting to the CEO — commercial plan, promotional calendar and the P&L case behind it",
                "Created the Beauty Club and Hot on Social programmes from scratch to drive repeat usage on a young platform, grew 42 accounts +30% GMV QoQ and led category expansion as PIC Fragrances (30+ stores in two months)",
            ],
        },
        {
            "company": "Glovo",
            "role": "Account Manager – XL Accounts",
            "dates": "Sep 2022 – Nov 2023",
            "location": "Madrid, Spain",
            "context": "Quick-commerce platform | €500M+ revenue | 10K+ employees",
            "bullets": [
                "Helped build Glovo's retail vertical from zero — taking a food-delivery app into fashion, beauty and non-food — and ran launch activations with strategic partners (KFC, Taco Bell, Sushi Shop)",
            ],
        },
        {
            "company": "Mondelez International",
            "role": "Trainee – Category Planning",
            "dates": "Aug 2021 – Aug 2022",
            "location": "Madrid, Spain",
            "context": "Global FMCG | €36B revenue | Category planning & analytics",
            "bullets": [
                "Measured launch and promotional performance for the chocolate category and fed the read-outs into NPD decisions (Milka Spread, Mini Suchard)",
            ],
        },
    ],
    "skills_brand": (  # label -> "Product Marketing & GTM"
        "go-to-market strategy, product launches end-to-end, positioning & value propositions, "
        "messaging, quarterly roadmaps, pricing, brand strategy"
    ),
    "skills_ecommerce": (  # label -> "Channels & Creative"
        "in-product & onsite merchandising, paid social (Meta), Google Ads, CRM/EDM, "
        "creator & UGC programmes, communications planning, offline activations"
    ),
    "skills_commercial": (  # label -> "Markets & Stakeholders"
        "50+ markets across 6 regions, cross-functional leadership, partner management, "
        "marketplace & quick-commerce platforms, C-level reporting"
    ),
    "skills_data": (  # label -> "Customer & Data"
        "customer & category insight, feedback loops, KPI forecasting, ROI, ROAS, conversion, "
        "retention, GMV, AOV, A/B testing, launch read-outs"
    ),
    "skills_tools": (  # label -> "Tools"
        "Power BI, Tableau, Looker, Google Analytics, Meta Ads Manager, Salesforce, "
        "Shopify, Adobe, Canva, Generative AI (Claude, ChatGPT)"
    ),
}

ROLE_LABELS = {
    "Brand & Marketing": "Product Marketing & GTM",
    "E-Commerce & Digital": "Channels & Creative",
    "Commercial": "Markets & Stakeholders",
    "Data & Analytics": "Customer & Data",
}

OUTREACH = """\
# Outreach — Revolut · Product Marketing Manager (core)

**Rol:** Product Marketing Manager · Remoto, con base en EAU · publicado 2-sep-2026 (~18h antes de verlo)
**Estado de la oferta:** +100 personas han hecho clic en «Solicitar» en el primer día. Promocionada por
técnico de selección, **respuestas gestionadas fuera de LinkedIn** → hay que aplicar en revolut.com/careers.
**Aplicar:** solo por canales oficiales de Revolut. Nunca por terceros — la propia oferta avisa de estafas.

## Ojo: es la tercera Revolut de la semana

Ya hay paquete hecho para **PMM (Crypto)** (misma carpeta de hoy) y para **Marketing Manager (Brand)**
(20-ago). Esta es la de **core financial features / main account**. Son equipos distintos dentro de
Growth, así que aplicar a varias no penaliza — pero **el CV y el mensaje tienen que ser distintos**,
y este está enfocado a adopción/uso recurrente y activaciones offline, no a categoría nueva.

## El diferenciador: ya existe una campaña Revolut hecha por Paula

**"No Borders"** — landing de campaña completa, desplegada y navegable:
https://guillemu11.github.io/revolut-no-borders/

Esta JD pide literalmente "set the standard for creative excellence while maintaining brand integrity"
y "recognised for generating highly original ideas". El link responde a las dos en 10 segundos.
Va en la primera línea del mensaje, no en un adjunto.

## Contacto

LinkedIn muestra **Alejandro y otros de su red** en «Personas con las que puedes hablar». Antes de
aplicar: abrir la oferta → esa lista → pedir referral. En Revolut el referral pesa mucho más que el
ATS, y con 100+ solicitudes en 24h el CV screen a pelo es una lotería.

## Mensaje sugerido (LinkedIn, <300 caracteres si es nota de Top Choice)

> Hola [nombre], voy a aplicar al Product Marketing Manager de Revolut (main account). Vengo de
> product marketing de consumo en Miravia (Alibaba) y Glovo, lanzando en 50+ mercados. Me hacía
> tanta ilusión que monté una campaña Revolut de cero: [link]. ¿Podrías referirme?

## Ángulo en la aplicación

1. **Product marketing, en idioma FMCG.** 6 lanzamientos end-to-end (insight, posicionamiento,
   propuesta de valor, pricing, messaging, GTM) orquestados por canal **y por geografía** — que es
   exactamente la frase de la JD.
2. **Adopción, no solo awareness.** Sus métricas son GMV, conversión, AOV, repetición y retención:
   la misma forma que "increase usage of Revolut as a main account".
3. **Ideas originales, ejecutadas.** Beauty Club y Hot on Social se los inventó ella en un
   marketplace recién lanzado; también el programa de influencers desde cero y el sistema de
   reporting con IA (~40% menos trabajo manual).
4. **Los cuatro canales que pide la JD.** in-product/onsite, digital, earned media/creadores y
   **offline** (sampling, seeding, ejecución en modern trade) — este último es donde la mayoría de
   PMMs de tech no tienen nada y ella sí.
5. **Hyper-growth tech, dos veces.** Miravia era el marketplace nuevo de Alibaba en España; Glovo
   construyó su vertical retail desde cero.

## Lo que NO se dice

- **Cero fintech, pagos, banca o producto financiero regulado.** Aquí es peor que en la de Crypto:
  "knowledge of markets and the competitive landscape in fintech or the payments industry" está en
  **requisitos**, no en nice-to-have. No se maquilla en el CV. Se compensa preparando 2-3 lecturas
  propias y reales del competitive landscape (Wise, Monzo, N26, y en EAU: Wio, Mashreq Neo, e&
  money, ADCB Hayyak) antes de cualquier entrevista.
- **Ni "orchestrating PR campaigns" a escala Revolut.** Tiene earned media y creadores, no gabinete
  de prensa. En el CV va como "communications planning".
- **Nunca "no necesito sponsorship".** Visado de residencia EAU patrocinado por su empresa actual.
- **Sin árabe.** No aplica en un rol global/remoto, pero no se insinúa lo contrario.

## Riesgos

- 100+ solicitudes en 24 horas. Sin referral, el CV screen es un muro.
- Revolut filtra por pedigrí (ex-consultoría, ex-big-tech) y el proceso es largo: varias rondas +
  case study.
- Es remoto, fuera de su preferencia declarada.
- Sin salario publicado — confirmar contra el suelo de 20.000 AED/mes.
"""


def make_job() -> Job:
    return Job(
        id="revolut-product-marketing-manager-core-uae-remote-2026-09",
        title=TITLE,
        company=COMPANY,
        location="United Arab Emirates (Remote)",
        url="https://www.revolut.com/careers/",
        source="linkedin",
        description=JOB_DESCRIPTION,
        raw={
            "query": "Revolut Product Marketing Manager remote UAE",
            "note": "Posted on LinkedIn 2026-09-02 (~18h before capture); 100+ Apply clicks in the first "
                    "day; promoted by a recruiter with replies handled outside LinkedIn. Remote, based in "
                    "the UAE. Apply ONLY via revolut.com/careers (the JD warns about recruitment scams). "
                    "LinkedIn shows network contacts at Revolut ('Alejandro y otros') — chase a referral "
                    "before applying. Distinct from the PMM (Crypto) and Marketing Manager (Brand) postings "
                    "already packaged: this one is core financial features / main-account usage. Real gap: "
                    "fintech/payments competitive-landscape knowledge is a stated REQUIREMENT here and "
                    "Paula has none. Revolut is a stated priority target for Paula.",
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
        "posted_date": "2026-09-02", "raw": job.raw,
        "ai_score": 72, "ai_tier": "Warm",
        "skills_match": [
            "Product marketing is her actual day job in FMCG language: 6 NPD launches end-to-end (insight, positioning, value proposition, pricing, messaging, GTM) orchestrated across channels AND geographies — the JD's exact phrasing",
            "Adoption-shaped metrics: GMV, conversion, AOV, repeat and retention — the same problem as 'increase usage of Revolut as a main account'",
            "Recognised for original ideas, with receipts: Beauty Club and Hot on Social invented on a newly launched Alibaba marketplace, an influencer engine built from zero, and a self-built AI reporting system (~40% less manual work)",
            "All four channels the JD lists, including the one most tech PMMs lack: in-product/onsite merchandising, digital (Meta/Google/CRM), earned media and creators, and genuine offline activation (sampling, seeding, modern-trade retail execution)",
            "Hyper-growth tech twice over: Miravia was Alibaba's new marketplace launch in Spain (owned Flash Sales, reported to the CEO); Glovo built its retail vertical from zero",
            "Already built and deployed a full fictional Revolut campaign ('No Borders') — speaks directly to 'creative excellence while maintaining brand integrity'",
            "Revolut is a stated priority target — 'a passion for Revolut's products' is credible here",
        ],
        "missing_skills": [
            "No fintech or payments experience, and no knowledge of that competitive landscape — listed here as a REQUIREMENT, not a nice-to-have (harder gap than in the Crypto posting)",
            "No banking or regulated financial-product marketing at all",
            "No formal Product Marketing Manager title — PMM work sits inside brand/e-commerce and KAM roles",
            "PR is her weakest channel: earned media and creator work, not orchestrated PR at Revolut's scale",
            "No experience marketing a product where trust/security is the core message",
        ],
        "sector_fit": "adjacent — consumer product marketing and hyper-growth platforms are a direct hit; fintech and payments are entirely new and are an explicit requirement here",
        "seniority_fit": "good — 5 years consumer/product marketing, and the role is a hands-on IC manager rather than a people-leadership post",
        "red_flags": [
            "100+ Apply clicks within 24 hours of posting — without a referral the CV screen is a wall",
            "Fintech/payments landscape knowledge sits in the requirements list, and she has none",
            "Revolut screens hard on pedigree (ex-consultancy, ex-big-tech); multi-stage process with case study",
            "Remote role, outside Paula's stated preference (remote_ok: false in profile.yaml)",
            "No salary published — confirm against the AED 20K/month floor",
            "Apply only via revolut.com/careers; the JD explicitly warns about recruitment scams, and replies are handled outside LinkedIn",
        ],
        "ats_keywords": ATS,
        "reasoning": (
            "Same asymmetry as the Crypto posting — Paula already has a deployed Revolut campaign "
            "('No Borders') that answers this JD's creative-excellence and original-ideas asks in one link "
            "— but a slightly better substantive fit on two counts. First, the job is about usage and "
            "main-account behaviour, and her metrics are adoption-shaped (GMV, conversion, AOV, repeat, "
            "retention) rather than awareness-shaped. Second, this JD explicitly wants offline activations "
            "alongside in-product, digital and PR, and offline is where her FMCG background (sampling, "
            "seeding, modern-trade retail execution) beats most tech PMMs. The originality requirement is "
            "also answerable with real programmes she invented rather than inherited. The gap is worse "
            "than in the Crypto version, though: fintech/payments competitive-landscape knowledge is a "
            "stated requirement here, not a nice-to-have, and she has zero. The CV therefore claims "
            "consumer/product marketing and hyper-growth platform experience only, and the referral "
            "(network contacts visible on the posting) is what decides whether this gets read at all."
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

    outreach_dir = final_dir / "03_Outreach"
    outreach_dir.mkdir(parents=True, exist_ok=True)
    (outreach_dir / "Outreach.md").write_text(OUTREACH, encoding="utf-8")
    print("OK_OUTREACH", outreach_dir / "Outreach.md")

    try:
        from pypdf import PdfReader
        n = len(PdfReader(str(final_cv)).pages)
        print(f"PAGES {n}", "OK" if n == 1 else "!! SPILLS")
    except Exception as exc:  # noqa: BLE001
        print("page-count check skipped:", exc)

    print("OK_PACKAGE", final_dir)


if __name__ == "__main__":
    main()
