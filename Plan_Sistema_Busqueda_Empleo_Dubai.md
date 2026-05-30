# Sistema de Operador de Carrera Profesional - Paula De Francisco (Dubai)

## Context

Paula busca empleo en Dubai. Perfil: Brand & Marketing Manager con 4+ años en FMCG, Beauty, E-Commerce. Actualmente en DoFreeze LLC (Dubai). Experiencia previa en Alibaba Group (Miravia/AliExpress), Glovo y Mondelez. Skills core: brand strategy, NPD, key account management, e-commerce, trade marketing, influencer marketing. Ya tiene visa UAE, LinkedIn activo, CV actualizado. Objetivo: máxima automatización, calidad alta, diferenciación real.

---

## 1. Entorno: Stack Híbrido con Claude Code como Orquestador

```
Claude Code (orquestador central)
├── MCP Indeed        → búsqueda programática de ofertas en Dubai
├── MCP Gmail         → crear drafts de outreach, follow-ups
├── MCP Notion        → CRM de candidaturas, tracking, contactos
├── MCP Chrome        → asistir en formularios, research de empresas
├── SerpAPI           → Google Jobs scraping (ofertas de Google)
├── Apify             → LinkedIn Jobs scraping (datos públicos, sin login)
├── Firecrawl /interact → scraping + interacción con career sites
├── Scripts Python    → generación de CVs (python-docx), orquestación
└── Claude API        → análisis de ofertas, scoring, generación de contenido
```

---

## 2. Fuentes de Ofertas: Triple Pipeline

### A. Indeed (MCP - ya conectado)
- Búsqueda directa via MCP
- Filtros por ubicación (Dubai/UAE), título, sector
- Ideal para ofertas de empresas grandes y medianas

### B. Google Jobs (SerpAPI)
- API dedicada: `engine=google_jobs`, location=Dubai
- Agrega ofertas de múltiples fuentes (career sites, LinkedIn, Indeed, Bayt, GulfTalent)
- 10 resultados por página, paginación con `next_page_token`
- Coste: ~$75/mes por 5,000 búsquedas ($0.015/búsqueda)
- **Ventaja**: captura ofertas que no están en Indeed (career pages directas, portales regionales como Bayt, Naukrigulf)

### C. LinkedIn Jobs (Apify)
- Scrapers de Apify extraen ofertas PÚBLICAS de LinkedIn sin necesitar login
- Legal: precedente hiQ v. LinkedIn confirma que scraping de datos públicos no viola CFAA
- NO se accede con la cuenta de Paula, NO hay riesgo de ban
- Solo se extraen listings públicos de jobs, no datos personales
- Actors recomendados: `cryptosignals/linkedin-jobs-scraper` o `bebity/linkedin-jobs-scraper`
- Coste: Apify Free tier = 30 actor runs/mes, Starter = $49/mes

### D. Career Pages de Empresas Target (Firecrawl /interact)
- Firecrawl /interact permite scraping + interacción (click, navegación, paginación)
- Ideal para career pages de empresas como Chalhoub Group, L'Oréal, Unilever que tienen portales propios
- Browser Sandbox: entorno managed donde AI agents pueden navegar web
- Se puede configurar una lista de 20-30 career pages target y monitorearlas semanalmente
- Coste: Firecrawl Free = 500 credits/mes, Hobby = $16/mes

### Deduplicación cross-source
- Cada oferta se hashea por (título normalizado + empresa + ubicación)
- Se almacena en `seen_jobs.json` local + campo en Notion
- Evita procesar la misma oferta desde Indeed + Google + LinkedIn

---

## 3. CRM: Notion vs Custom — Recomendación

### Análisis comparativo:

| Criterio | Notion | Custom (Supabase + Next.js) |
|----------|--------|-----------------------------|
| Tiempo de setup | 1 hora | 1-2 semanas |
| Paula puede usar | Sí, app móvil incluida | Necesita frontend custom |
| Board/Pipeline visual | Nativo | Hay que construirlo |
| Calendar view | Nativo | Hay que construirlo |
| API/MCP | Ya conectado | Supabase MCP disponible |
| Flexibilidad de datos | Media (propiedades fijas) | Total (SQL) |
| Analytics avanzados | Limitado | Ilimitado |
| Coste | $0 (plan gratuito) | $0 (Supabase free) + hosting |
| Mantenimiento | Cero | Hay que mantener código |

### Recomendación: **Notion para MVP, evaluar custom para V2**

**Razones:**
1. Paula necesita interactuar con el pipeline diariamente (ver ofertas, actualizar estados, añadir notas). Notion tiene app móvil nativa.
2. Las vistas Board + Calendar + Table son exactamente lo que necesitamos y son nativas en Notion.
3. Ya tenemos el MCP conectado, podemos automatizar todo desde Claude Code.
4. Un CRM custom requiere 1-2 semanas de desarrollo de frontend antes de poder usarse. Ese tiempo es mejor invertirlo en buscar empleos.
5. Si más adelante necesitamos analytics avanzados (conversion rates por fuente, A/B testing de cover letters), podemos añadir Supabase como data warehouse sin reemplazar Notion.

### Opción híbrida (V2):
```
Notion (interfaz para Paula) ←→ Supabase (data warehouse para analytics)
                                    ↓
                              Next.js Dashboard (métricas de conversión)
```

---

## 4. Queries de Búsqueda Optimizadas para Paula

**Títulos target:**
- Brand Manager
- Marketing Manager
- E-Commerce Manager
- Key Account Manager
- Trade Marketing Manager
- Digital Marketing Manager
- Commercial Manager
- Category Manager

**Sectores prioritarios:**
- FMCG / Consumer Goods
- Beauty & Fragrances / Personal Care
- E-commerce / Quick-commerce
- Food & Beverage
- Retail / Modern Trade
- Luxury / Fashion

**Empresas target Dubai (career pages a monitorear):**
- Chalhoub Group, LVMH ME, L'Oréal ME, Estée Lauder ME
- Unilever Gulf, P&G Gulf, Nestlé ME, Mars, Reckitt
- Al Futtaim, Majid Al Futtaim, Landmark Group, Apparel Group
- Noon, Talabat, Careem, Deliveroo UAE
- Alshaya Group, Azadea Group
- PepsiCo, Coca-Cola, Mondelez ME
- Amazon UAE, Namshi

**Keywords ATS de alto valor:**
- NPD, brand strategy, influencer marketing, trade marketing
- Key account management, distributor management
- Quick-commerce, Noon, Talabat, e-commerce
- FMCG, GCC, MENA
- P&L, ROI, ROAS, GMV
- Category management, shopper marketing

---

## 5. Arquitectura del Sistema

### Flujo principal:

```
DIARIO (automatizado, scheduled task cada mañana):

  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
  │   Indeed     │   │  Google Jobs │   │  LinkedIn   │
  │   MCP       │   │  (SerpAPI)   │   │  (Apify)    │
  └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
         │                 │                  │
         └────────────┬────┴──────────────────┘
                      ▼
              ┌───────────────┐
              │ Deduplicación │
              │ + Filtrado    │
              └───────┬───────┘
                      ▼
              ┌───────────────┐
              │   Analyzer    │    Claude API analiza cada oferta:
              │  (Score 0-100)│    - Match de skills
              │               │    - Sector fit
              │               │    - Seniority fit
              └───────┬───────┘    - Keywords ATS
                      ▼
              ┌───────────────┐
              │  Notion CRM   │    Inserta con score + clasificación
              │  "Job Pipeline"│    Hot (>80) / Warm (60-80) / Cold (<60)
              └───────┬───────┘
                      ▼
              ┌───────────────┐
              │ Gmail: Resumen│    "Hoy: 3 Hot, 7 Warm, 12 Cold"
              │   diario      │    Con links a las Hot para review rápido
              └───────────────┘


AUTOMÁTICO (para ofertas Hot, >80 score):

  ┌───────────────┐
  │ Oferta Hot    │
  │ detectada     │
  └───────┬───────┘
          ▼
  ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
  │ CV            │   │ Cover Letter  │   │ Company       │
  │ Personalizado │   │ Personalizada │   │ Research      │
  │ (DOCX)        │   │ (DOCX)        │   │ (web/producto)│
  └───────┬───────┘   └───────┬───────┘   └───────┬───────┘
          │                   │                    │
          └────────┬──────────┴────────────────────┘
                   ▼
  ┌─────────────────────────┐
  │ Gmail Draft:            │
  │ - Email outreach listo  │
  │ - CV adjunto            │
  │ - Cover letter adjunta  │
  │ - (Value-add si aplica) │
  └─────────────────────────┘
          ▼
  ┌─────────────────────────┐
  │ Notion: Status →        │
  │ "Ready to Apply"        │
  │ + archivos linked       │
  └─────────────────────────┘


SEMANAL (career pages monitoring):

  ┌───────────────────────────┐
  │ Firecrawl /interact       │
  │ Scrape 20-30 career pages │
  │ de empresas target        │
  └───────────┬───────────────┘
              ▼
        (mismo pipeline de análisis)
```

### Componentes detallados:

#### A. Discovery Agent
- **Indeed MCP**: Búsqueda diaria con queries del perfil
- **SerpAPI**: Google Jobs API, location=Dubai, múltiples queries
- **Apify**: LinkedIn Jobs scraper, datos públicos
- **Firecrawl**: Career pages de empresas target (semanal)
- **Deduplicación**: Hash (título+empresa+ubicación) contra histórico
- **Output**: Ofertas raw → Notion "Inbox"

#### B. Analysis Agent
Cada oferta se analiza con Claude API:
- Responsabilidades clave (lista)
- Requisitos obligatorios vs deseables
- Skills match con Paula (% de match)
- Seniority level
- Sector/industria
- Keywords ATS
- Red flags (si los hay)
- **Score (0-100)**:
  - Match de skills (40%)
  - Match de sector/industria (20%)
  - Seniority fit (15%)
  - Match de ubicación/formato (10%)
  - Calidad de la oferta (15%)
- Clasificación: **Hot (>80)** / **Warm (60-80)** / **Cold (<60)**

#### C. Content Generation Agent
Para cada oferta aprobada:

1. **CV Personalizado** (DOCX):
   - Reordena bullets de experiencia según relevancia
   - Ajusta Professional Summary con keywords del job description
   - Añade/enfatiza skills que matchean
   - Mantiene formato idéntico al CV original de Paula
   - Naming: `CV_Paula_DeFrancisco_[Empresa]_[Puesto].docx`

2. **Cover Letter**:
   - Hook mencionando algo específico de la empresa
   - Conexión entre experiencia de Paula y requisitos
   - Propuesta de valor concreta con métricas
   - Call to action
   - Naming: `CL_Paula_DeFrancisco_[Empresa]_[Puesto].docx`

3. **Mensajes de Outreach**:
   - Email (subject + body personalizado)
   - LinkedIn connection note (300 chars max)
   - LinkedIn follow-up message
   - Respuestas para formularios típicos

4. **Value-Add Deliverable** (solo Hot, >80):
   - Mini auditoría de web/e-commerce/social de la empresa
   - 3-5 observaciones concretas + sugerencias de mejora
   - Adaptado al rol específico
   - 1-2 páginas PDF

#### D. Notion CRM

**Base de datos: Job Pipeline**
| Propiedad | Tipo | Descripción |
|-----------|------|-------------|
| Job Title | Title | Título del puesto |
| Company | Text | Nombre de la empresa |
| Score | Number | Score de match (0-100) |
| Priority | Select | Hot / Warm / Cold |
| Status | Select | Inbox → Analyzed → CV Ready → Applied → Followed Up → Interview → Offer → Rejected |
| Source | Select | Indeed / Google / LinkedIn / Career Page / Referral |
| Link | URL | Link a la oferta |
| Sector | Select | FMCG / Beauty / E-commerce / F&B / Retail / Luxury |
| Seniority | Select | Mid / Senior / Lead / Director |
| CV Version | Files | CV personalizado |
| Cover Letter | Files | Cover letter |
| Applied Date | Date | Fecha de aplicación |
| Follow-up Date | Date | Fecha de follow-up programado |
| Contacts | Relation | Contactos clave |
| Analysis | Rich Text | Análisis detallado de la oferta |
| Key Requirements | Rich Text | Requisitos principales |

**Base de datos: Contacts**
| Propiedad | Tipo |
|-----------|------|
| Name | Title |
| Company | Text |
| Role | Select (Recruiter / Hiring Manager / Team Lead / HR Director) |
| LinkedIn URL | URL |
| Email | Email |
| Notes | Rich Text |
| Related Jobs | Relation → Job Pipeline |

**Vistas:**
- **Board por Status**: Pipeline visual (Kanban)
- **Hot Jobs**: Table filtrada Score > 80
- **Calendar**: Follow-up dates
- **By Company**: Agrupada por empresa

---

## 6. Mapa de Automatización (Máxima Autonomía)

| Tarea | Nivel | Detalle |
|-------|-------|---------|
| Búsqueda de ofertas (3 fuentes) | 100% auto | Scheduled task diaria |
| Análisis y scoring | 100% auto | Claude API |
| Inserción en Notion | 100% auto | MCP Notion |
| Notificación diaria por email | 100% auto | Gmail MCP |
| Generación de CV personalizado | 95% auto | Genera DOCX, Paula revisa |
| Cover letter | 95% auto | Genera draft, Paula revisa tono |
| Mensajes outreach (email) | 90% auto | Drafts en Gmail, Paula revisa y envía |
| Value-add deliverables | 85% auto | Genera propuesta, Paula valida |
| Company research | 90% auto | Chrome MCP + Firecrawl |
| Career page monitoring | 100% auto | Firecrawl semanal |
| Follow-up tracking | 100% auto | Notion + scheduled reminders |
| Rellenar formularios | 70% auto | Chrome MCP asiste, Paula supervisa |
| LinkedIn mensajes | 0% auto | Paula envía manualmente (proteger cuenta) |

---

## 7. Stack Técnico Completo

| Función | Herramienta | Coste/mes |
|---------|-------------|-----------|
| Orquestación | Claude Code + Scheduled Tasks | (incluido) |
| Búsqueda Indeed | Indeed MCP | (incluido) |
| Búsqueda Google Jobs | SerpAPI | ~$75 (5K búsquedas) |
| Búsqueda LinkedIn Jobs | Apify | $0-49 |
| Career pages scraping | Firecrawl /interact | $0-16 |
| Análisis de ofertas | Claude API (Sonnet) | ~$10-20 |
| CRM / Pipeline | Notion MCP | $0 |
| Email / Outreach | Gmail MCP | $0 |
| Generación CV | python-docx + WeasyPrint | $0 |
| Research empresas | Chrome MCP | (incluido) |
| **Total estimado** | | **$85-160/mes** |

**Opción económica (solo herramientas gratuitas):**
- Indeed MCP + Notion MCP + Gmail MCP + Claude API (~$10-20)
- Sin SerpAPI, sin Apify paid, sin Firecrawl paid
- **Total: ~$10-20/mes**

---

## 8. Propuesta de MVP (Semana 1)

### Paso 1: Perfil de candidata (`profile.yaml`)
- Extraer toda la info del CV de Paula en formato estructurado
- Skills, experiencia, keywords, preferencias, empresas target

### Paso 2: Notion CRM
- Crear base de datos "Job Pipeline" con todas las propiedades
- Crear base de datos "Contacts"
- Configurar vistas: Board, Calendar, Hot Jobs, By Company

### Paso 3: Discovery pipeline
- Indeed MCP: búsqueda con 8 queries de títulos
- Deduplicación contra histórico
- Análisis y scoring con Claude API
- Inserción automática en Notion

### Paso 4: Content generation
- CV personalizer: DOCX con formato del CV actual de Paula
- Cover letter generator
- Outreach email templates

### Paso 5: Gmail integration
- Crear drafts de outreach listos para revisar
- Notificación diaria con resumen de ofertas

### Paso 6: Scheduled task
- Pipeline diario automatizado cada mañana

---

## 9. Versión Avanzada (Semana 2-4)

1. **Google Jobs + LinkedIn Jobs**: Añadir SerpAPI y Apify como fuentes
2. **Career pages monitoring**: Firecrawl para 20-30 empresas target
3. **Contact finder**: Research de hiring managers por empresa
4. **Value-add generator**: Mini auditorías y propuestas personalizadas
5. **Smart follow-ups**: Reminders automáticos + drafts de follow-up
6. **Batch CV optimization**: CV por cluster de ofertas similares
7. **Interview prep**: Cuando status = Interview, generar documento de preparación
8. **Analytics** (opcional, Supabase): Métricas de conversión por fuente/sector/score

---

## 10. Maximización de Resultados

1. **Diferenciación**: Los value-add deliverables son el arma secreta. Nadie más envía una mini auditoría de la web de la empresa junto con su CV.
2. **Speed**: Aplicar en las primeras 24-48h. El pipeline diario lo garantiza.
3. **ATS**: Keywords del job description inyectadas naturalmente en el CV.
4. **Network**: Dubai funciona mucho por conexiones. El sistema identifica contactos y prepara outreach personalizado.
5. **Quality > Quantity**: Solo aplicar a Hot (>80) automáticamente. Warm con review. Cold se ignoran.
6. **Superpoder de Paula**: Su experiencia en quick-commerce UAE (Noon, Talabat, Careem, Deliveroo) es rara y valiosa. Destacar en CADA candidatura relevante.
7. **Sector targeting**: FMCG y Beauty en GCC son sus sectores de máximo fit.

---

## 11. Riesgos y Mitigaciones

| Riesgo | Mitigación |
|--------|------------|
| Ban de LinkedIn | NO automatizar envíos. Solo preparar contenido |
| CV mal personalizado | Quick review antes de enviar |
| Email spam | Máximo 5-10 outreach/día, alta personalización |
| Ofertas expiradas | Verificar link antes de aplicar |
| Scraping bloqueado | Rotar IPs (Apify lo maneja), usar proxies |
| Coste de APIs | Empezar con tier gratuito, escalar si funciona |

---

## 12. Sobre End-to-End con Computer Use / Browser Automation

### Lo que SÍ se puede hacer:
- Buscar ofertas en Google, LinkedIn (público), career pages → **Firecrawl + Apify**
- Entrar en ofertas y extraer datos → **Firecrawl /interact**
- Identificar personas clave (nombre + título) → **Chrome MCP + búsqueda web**
- Redactar mensajes personalizados → **Claude API**
- Generar deliverables de valor → **Claude API + templates**
- Crear drafts de email → **Gmail MCP**

### Lo que tiene limitaciones:
- Rellenar formularios complejos → **Chrome MCP puede asistir**, pero CAPTCHAs y verificaciones requieren humano
- Encontrar emails corporativos → **Herramientas como Hunter.io ayudan**, pero no siempre disponible
- Enviar LinkedIn messages → **Paula debe hacerlo manualmente** (ban risk)

### Lo que NO se debería hacer:
- Automatizar login de Paula en LinkedIn/portales de empleo con sus credenciales
- Envío masivo de connection requests
- Submit automático de aplicaciones sin review

---

## 13. Primer Paso de Implementación

1. Crear `profile.yaml` de Paula
2. Crear Notion CRM con el schema definido
3. Ejecutar primera búsqueda en Indeed para validar el pipeline
4. Generar primer CV personalizado para una oferta real
5. Validar el flujo completo end-to-end con 1 oferta
