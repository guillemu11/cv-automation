# Brand audit — Opella + sub-brands

## Fuentes verificadas (2026-05-22)

### Opella (parent)

- **Bold green** como primary (`#00A651` inferido vía WebFetch; confirmado por caso de estudio en MOC85 — "a Bold Green that dominates the category").
- Tipografía custom: **Opella Sans** (statements, clarity) + **Opella Serif** (human, truthful tone).
- Wordmark verde sobre blanco, minimalista.
- Tone: modern, direct, health-focused.
- Sistema visual: "Revolutionary Simplicity" — ilustración con wit + warmth.

### Buscopan

- buscopan.com es un site corporativo global con white + azul `#0066CC` accent + Arial. No tiene mucha personalidad visual en web.
- Pero el **packaging real** (lo que el consumidor reconoce) es amarillo pálido + rojo, que es lo que yo usé (`#F4DC59` + `#C2202C`).

### Doliprane

- doliprane.fr bloqueó WebFetch (ECONNREFUSED — protección anti-bot).
- Pero por conocimiento de packaging + búsqueda: la caja icónica es **naranja-amarillo con wordmark rojo**, que es exactamente lo que usé (`#F58220` + `#E2231A`). Es uno de los packaging OTC más reconocibles de Europa francófona.

## Diagnóstico del gap

Lo que hice mal: **me salté la fase 1 de la skill `campaign-landing`** (extracción real de brand desde el sitio del sub-brand vía Firecrawl/WebFetch). Usé palette de memoria, basada en packaging.

Resultado:
- Las paletas de producto que elegí (Buscopan amarillo, Doliprane naranja) **son consumer-correct** — coinciden con el packaging real.
- Pero **falta el endorsement visual del parent** (Opella verde + Opella Sans). Una CMO que abra estas landings ahora ve "una campaña sobre Buscopan" en vez de "una campaña sobre Buscopan **dentro del sistema Opella**".

## Tres opciones para corregir

1. **No tocar nada** — las paletas son correctas a nivel producto. Añadir solo una mención del parent en `ANGLES.md`.
2. **Hybrid (recomendado)** — mantener producto colors en hero/executions, pero envolver toda la landing en **Opella green + Opella Sans en nav/footer/typography**. Da el contexto corporativo sin perder el reconocimiento de packaging.
3. **Full Opella corporate** — sustituir todas las paletas por Opella green/white/black. Más limpio, menos branded por producto. Mejor para "presentation deck" mode, peor para "campaign for consumer".
