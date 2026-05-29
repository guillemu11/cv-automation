# Wiki — LLM-maintained knowledge base

Un vault de Obsidian que Claude Code mantiene automáticamente. Tú curas fuentes y haces preguntas; Claude se encarga de resumir, enlazar y mantener la consistencia.

Basado en el patrón **LLM Wiki** de Andrej Karpathy.

## Dominios

- **Jobs** — Investigación del mercado de empleo en Dubai: empresas, recruiters, industrias, JDs, salarios.
- **AI** — Papers, técnicas y patrones de IA aplicables al pipeline `career_ops/`.

## Estructura

- `raw/` — Fuentes en bruto (artículos, PDFs, clippings). **Inmutable**. Git-ignored.
- `entities/` — Páginas de cosas con identidad (empresas, personas, productos).
- `concepts/` — Páginas de ideas (industrias, tipos de rol, técnicas).
- `sources/` — Una página por fuente ingerida, con resumen + takeaways.
- `synthesis/` — Análisis cross-cutting y tesis en evolución.
- `index.md` — Catálogo vivo de todas las páginas.
- `log.md` — Log cronológico de operaciones.
- `CLAUDE.md` — Schema que gobierna cómo Claude opera en la wiki.

## Cómo usarlo

**1. Abre el vault en Obsidian.** El vault ya está registrado como `wiki`.

**2. Para ingerir una fuente**:
   - Descarga/clippea el archivo a `raw/jobs/` o `raw/ai/` (usa Obsidian Web Clipper para páginas web).
   - Pide a Claude: *"Ingesta `raw/jobs/<archivo>`"*.
   - Claude te resume los takeaways, te pide confirmación y luego crea/actualiza las páginas pertinentes.

**3. Para hacer una pregunta**:
   - *"¿Qué sé sobre Emirates Group?"* — Claude lee `index.md` y las páginas relevantes, y responde con citas.
   - *"Compara Landmark Group con Majid Al Futtaim"* — Claude puede guardar la comparación en `synthesis/` si tú quieres.

**4. Para un health check**:
   - *"Haz un lint de la wiki"* — Claude busca páginas huérfanas, stubs sin rellenar, contradicciones no resueltas, etc.

## Reglas importantes

- `raw/` es inmutable. Claude nunca lo edita.
- Todas las páginas tienen frontmatter YAML (ver `CLAUDE.md`).
- Todo claim factual cita la fuente vía `[[wikilink]]`.
- Las contradicciones se marcan, no se sobrescriben.

## Extensiones recomendadas (opcional)

- **Obsidian Web Clipper** — clippea páginas web a `raw/`.
- **Dataview** — tablas dinámicas filtrando por frontmatter.
- **Marp** — slide decks desde markdown.
- **Graph view** (built-in) — visualiza conexiones.

## Cosas que NO van aquí

- Código del pipeline (`career_ops/`). Eso vive en el root del proyecto.
- Notas personales rápidas. Usa un scratchpad aparte.
- Fuentes pesadas que no vayas a consultar más (ocupan espacio en `raw/`).
