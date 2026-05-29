# Career Ops — Paula (Dubai)

Sistema automatizado de búsqueda de empleo para Paula De Francisco en Dubai.
Pipeline diario: discovery multi-fuente → filtrado → scoring con Claude → Notion CRM → drafts de email y CV personalizados.

**Nunca envía nada automáticamente.** Todo termina en drafts listos para revisar.

---

## Quickstart

```bash
# 1. Clonar e instalar
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt

# 2. Configurar credenciales
cp .env.example .env
# editar .env con las API keys (ver sección Credenciales)

# 3. Crear las bases de datos de Notion (one-shot)
python scripts/setup_notion_db.py
# copiar los IDs devueltos a .env (NOTION_DB_JOBS, NOTION_DB_CONTACTS)

# 4. Calibrar el scorer (Paula etiqueta 30 ofertas)
python scripts/calibrate_scorer.py

# 5. Dry-run del pipeline
PIPELINE_DRY_RUN=true python -m career_ops.pipeline

# 6. Primer run real
python -m career_ops.pipeline
```

---

## Arquitectura

```
discovery/  →  filters/  →  analyzer  →  contact_finder  →  notion_sync  →  daily_digest
  jobspy       dedupe       Claude       Apollo.io           Notion API      Outlook/Gmail
  serpapi      salary       SQLite
  apify        blacklist    cache
  firecrawl
```

Ver `plan/lucky-booping-ullman.md` para el diseño completo.

---

## Credenciales necesarias

| Variable | Dónde obtenerla |
|----------|-----------------|
| `ANTHROPIC_API_KEY` | https://console.anthropic.com |
| `NOTION_TOKEN` | https://notion.so/my-integrations |
| `SERPAPI_KEY` | https://serpapi.com |
| `APIFY_TOKEN` | https://apify.com → settings |
| `FIRECRAWL_API_KEY` | https://firecrawl.dev |
| `APOLLO_API_KEY` | https://apollo.io → settings → integrations |
| `MS_GRAPH_*` (Outlook) | https://portal.azure.com → App registrations |

---

## Runbook

### Disparar un run manual
```bash
python -m career_ops.pipeline
```

### Generar CV + cover letter + draft para una oferta concreta
```bash
python scripts/generate_for_job.py --job-id <id>
```
Sale en `output/CV_Paula_<Company>_<Role>.docx` y crea el draft en el email de Paula.

### Resetear el estado (empezar de cero)
```bash
rm data/seen_jobs.json data/analysis_cache.sqlite
```

### Añadir una empresa a la lista de career pages
Editar `career_ops/discovery/firecrawl_careers.py` → `TARGET_COMPANIES`.

### Recalibrar el scorer
```bash
python scripts/calibrate_scorer.py --recalibrate
```

---

## Estructura

```
career_ops/
├── pipeline.py              # orquestador principal
├── config.py                # carga .env + profile.yaml
├── discovery/               # fuentes de ofertas
├── filters/                 # dedupe, salary, hard filters
├── analyzer.py              # scoring con Claude
├── contact_finder.py        # Apollo.io
├── notion_sync.py
├── gmail_client.py / outlook_client.py
├── daily_digest.py
└── generators/              # CV, cover letter, outreach
scripts/
├── setup_notion_db.py
├── calibrate_scorer.py
└── generate_for_job.py
templates/
├── cv_paula_template.docx
└── cover_letter_template.docx
data/
├── seen_jobs.json
├── golden_set.yaml
└── analysis_cache.sqlite
```

---

## Costes estimados

| Servicio | Plan | Coste/mes |
|---------|------|-----------|
| Claude API (Sonnet) | pay-as-you-go | $10-25 |
| SerpAPI | Free → Starter | $0-75 |
| Apify | Free → Starter | $0-49 |
| Firecrawl | Hobby | $0-16 |
| Apollo.io | Free → Basic | $0-49 |
| **Total** | **Min → Max** | **$10 → $230** |

Empezar en tiers gratuitos y subir solo cuando cada fuente demuestre valor.
