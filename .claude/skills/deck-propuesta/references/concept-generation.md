# Generating 3 distinct trade-shopper concepts

The opening idea is the deck's differentiator, so don't free-hand a single concept. Fan out
several concepts from different strategic angles, score them with an adversarial judge panel,
and surface the **3 strongest that are mutually distinct** (different hero KPIs, not three
flavours of one idea). Then present those 3 to Paula and let her pick — per her standing
"always exactly three options" preference.

This needs the `Workflow` tool (multi-agent). It is the right place for one: independent
perspectives plus an adversarial check before committing. Run it in the background and read the
returned `concepts` array.

## How to parameterise

Fill `BRIEF` with the specific role + brand + market, keeping the **hard constraint** intact:
the idea must be unmistakably Trade & Shopper (lives at the shelf, runs on shopper mechanics,
moves measurable trade KPIs) — never a brand-ATL film, celebrity, or fashion stunt. Adapt the
six `LENSES` to the category if needed, but keep them genuinely different territories so the
final three don't collapse into one.

## The workflow script

```javascript
export const meta = {
  name: 'deck-concepts',
  description: 'Generate & judge trade-shopper creative concepts for a candidate pitch deck',
  phases: [
    { title: 'Generate', detail: '6 concept generators, distinct strategic lenses' },
    { title: 'Judge', detail: '3-judge adversarial panel scores each concept' },
    { title: 'Synthesize', detail: 'pick the 3 strongest, mutually distinct' },
  ],
}

// === EDIT THIS for the target role/brand/market ===
const BRIEF = `CONTEXT — you are a senior Trade & Shopper Marketing strategist helping a candidate win a job.

THE JOB: <ROLE> at <COMPANY>. Brand: <BRAND>.
THE DELIVERABLE: a visual pitch deck that opens with ONE flagship creative "key visual / big idea", then backs it with a rigorous trade & shopper plan. We are designing that ONE opening big idea here.

HARD CONSTRAINT — this is a TRADE & SHOPPER role, NOT a Brand Manager role. The idea MUST live at retail and be measurable:
- It plays out at the shelf / Perfect Store, pharmacy advice fixtures, the e-tail digital shelf (A+, search, reviews), quick-commerce, retail media, and shopper mechanics (GWP, sampling, secondary displays, price-pack bundles, creator codes).
- It moves trade KPIs: distribution, Perfect Store compliance, sell-out uplift, promo ROI/ROAS, e-tail search share, premium mix %, basket size.
- It must NOT be a pure ATL brand film, a celebrity endorsement, or a fashion co-branding stunt. A Trade & Shopper hiring manager must read it and think "she understands how to WIN THE SHELF."

BRAND: <one line on brand personality + palette + tagline>.
MARKET: <the category truth + channels + seasonal peaks for the market, e.g. GCC heat/humidity year-round; Carrefour/Lulu/Spinneys, BinSina/Aster, Noon/Amazon.ae, Talabat/Noon Minutes; Ramadan/Eid/DSF>.
HERO PRODUCTS: <the ranges to feature>.

Produce ONE concept. Make it specific, ownable, and obviously executable at retail. Avoid generic "summer activation" filler. Name it with a punchy, memorable line.`

const CONCEPT_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    name: { type: 'string' },
    tagline: { type: 'string' },
    big_idea: { type: 'string', description: '2-4 sentences: the core idea and the shopper insight it is built on' },
    key_visual: { type: 'string', description: 'Vivid description of the hero KEY VISUAL — what the opening slide looks like' },
    channel_activation: { type: 'array', items: { type: 'object', additionalProperties: false,
      properties: { channel: { type: 'string' }, how: { type: 'string' } }, required: ['channel', 'how'] } },
    why_trade_shopper: { type: 'string' },
    hero_kpi: { type: 'string' },
  },
  required: ['name', 'tagline', 'big_idea', 'key_visual', 'channel_activation', 'why_trade_shopper', 'hero_kpi'],
}

const VERDICT_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    fit_to_role: { type: 'number', description: '1-10: unmistakably Trade & Shopper, not brand-ATL' },
    wow: { type: 'number', description: '1-10: memorable on a pitch-deck cover' },
    feasibility: { type: 'number', description: '1-10: realistically executable in-market' },
    distinctiveness: { type: 'number', description: '1-10: ownable, non-generic' },
    total: { type: 'number' }, note: { type: 'string', description: 'one-sentence biggest weakness' },
  },
  required: ['fit_to_role', 'wow', 'feasibility', 'distinctiveness', 'total', 'note'],
}

// Six genuinely different territories. Adapt to the category, keep them distinct.
const LENSES = [
  { key: 'instore-theatre', title: 'In-store theatre / Perfect Store hero',
    brief: 'Turn the Modern Trade aisle into a branded experience — a flagship secondary display/endcap that becomes the signature Perfect Store picture.' },
  { key: 'climate-hook', title: 'Own the seasonal/category truth',
    brief: 'Build on the market’s #1 category truth (e.g. heat & humidity) and turn it into a recurring retail ownable that anchors the calendar.' },
  { key: 'qcommerce-first', title: 'Quick-commerce & digital-shelf first',
    brief: 'Lead with the new discovery channel for young shoppers: creator-led tiles, impulse bundles, search-share capture, A+ content as the hero stage.' },
  { key: 'premium-ritual', title: 'Premium gifting / occasion',
    brief: 'Premiumise via a gifting/occasion culture (Ramadan/Eid/DSF): premium endcaps, GWP, gift architecture — built to lift premium mix %, not volume.' },
  { key: 'personalization', title: 'Find-your-match diagnostic journey',
    brief: 'A shopper diagnostic that converts the confusing fixture into a guided choice, routed across pharmacy advice, a q-commerce/e-tail quiz, and an on-shelf benefit block.' },
  { key: 'win-the-shelf', title: 'Win the shelf (KAM / JBP operating system)',
    brief: 'The most trade-pure idea: dramatize a customer-led, data-driven Perfect Store + Joint Business Plan engine as the BIG idea itself. Make rigor the wow.' },
]

const scored = await pipeline(
  LENSES,
  (lens) => agent(`${BRIEF}\n\nYOUR STRATEGIC LENS: ${lens.title}\n${lens.brief}\n\nProduce ONE concept through this lens. Be concrete and ownable.`,
    { label: `gen:${lens.key}`, phase: 'Generate', schema: CONCEPT_SCHEMA }),
  (concept, lens) => parallel([0, 1, 2].map((j) => () =>
    agent(`${BRIEF}\n\nYou are an adversarial judge (#${j + 1}). Score this candidate HARSHLY. Default low if it drifts toward brand-ATL or generic activation.\n\nCONCEPT:\n${JSON.stringify(concept, null, 2)}`,
      { label: `judge:${lens.key}:${j}`, phase: 'Judge', schema: VERDICT_SCHEMA })
  )).then((vs) => {
    const v = vs.filter(Boolean)
    const avg = v.length ? v.reduce((a, b) => a + b.total, 0) / v.length : 0
    return { lens: lens.key, concept, avg_score: Math.round(avg * 10) / 10, verdicts: v }
  })
)

const valid = scored.filter(Boolean).sort((a, b) => b.avg_score - a.avg_score)
log(`Scored ${valid.length}. Top: ${valid.slice(0, 3).map((c) => `${c.concept.name} (${c.avg_score})`).join(', ')}`)

const FINAL_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    concepts: { type: 'array', description: 'Exactly 3, ranked best-first, mutually distinct',
      items: { type: 'object', additionalProperties: false,
        properties: {
          name: { type: 'string' }, tagline: { type: 'string' }, big_idea: { type: 'string' },
          key_visual: { type: 'string' },
          channel_activation: { type: 'array', items: { type: 'object', additionalProperties: false,
            properties: { channel: { type: 'string' }, how: { type: 'string' } }, required: ['channel', 'how'] } },
          why_trade_shopper: { type: 'string' }, hero_kpi: { type: 'string' },
          why_chosen: { type: 'string' }, score: { type: 'number' },
        },
        required: ['name', 'tagline', 'big_idea', 'key_visual', 'channel_activation', 'why_trade_shopper', 'hero_kpi', 'why_chosen', 'score'] } },
    rationale: { type: 'string' },
  },
  required: ['concepts', 'rationale'],
}

const synth = await agent(
  `${BRIEF}\n\nScored candidates (best-first):\n${JSON.stringify(valid.map((v) => ({ name: v.concept.name, avg_score: v.avg_score, concept: v.concept, top_critique: v.verdicts[0] && v.verdicts[0].note })), null, 2)}\n\nSelect and refine the 3 STRONGEST concepts that are MUTUALLY DISTINCT (span different strategic territory; do not pick three variations of one idea). Sharpen names/taglines/copy. Keep each unmistakably Trade & Shopper. Return exactly 3, ranked best-first.`,
  { phase: 'Synthesize', schema: FINAL_SCHEMA })

return synth
```

## Presenting the result

Show all three with a **mockup of each key visual** (the brainstorming visual companion is ideal —
render small 16:9 cards). For each: tagline, big idea, channel activation, and hero KPI. Recommend
one (usually the top-scored, most ownable consumer-truth hook), but let Paula choose — and note that
the three have *different* hero KPIs on purpose so she can match the angle to the interview's emphasis
(demand creation vs. account rigor vs. premium growth).

The judge panel earns its keep by killing each idea's weakness before Paula sees it — e.g. a "live
index" that can't run across physical retailers gets split into a KAM-sellable weekly swap + a truly
live online layer. Carry those fixes into the chosen concept's deck copy.
