# Log

Append-only chronological record of wiki operations. Each entry starts with `## [YYYY-MM-DD] <op> | <short label>` so it can be grepped.

## [2026-04-11] init | vault created

Schema, directory structure, and base files created by Claude Code.
Domains: `jobs` + `ai`.
Integrated inside `CV_Automation/` project. Pattern: LLM Wiki (Karpathy).

## [2026-04-11] ingest | landing-page techniques (3 YouTube transcripts)

Created raw:

- `raw/ai/jack-roberts-claude-nano-banana-websites.md`
- `raw/ai/nate-herk-nano-banana-2-websites.md`
- `raw/ai/nate-herk-seedance-2-websites.md`

Created sources:

- `sources/ai/jack-roberts-claude-nano-banana-websites.md`
- `sources/ai/nate-herk-nano-banana-2-websites.md`
- `sources/ai/nate-herk-seedance-2-websites.md`

Created concepts (born compounded — multiple sources from day one where applicable):

- [[Brand Extraction with Firecrawl]] — 1 source
- [[Scroll-Driven Animation]] — 2 sources
- [[Nano Banana Keyframe Workflow]] — 3 sources
- [[HTML Replication Pattern]] — 1 source
- [[Vercel One-Shot Deploy]] — 3 sources
- [[Seedance Loop Video Hero]] — 1 source
- [[Frontend Design Skill Pattern]] — 3 sources

Updated: `index.md`.

Purpose: feeds the planned `.claude/skills/campaign-landing/` skill for generating jaw-dropping animated campaign landing pages as job-application deliverables. See plan at `C:\Users\gmunoz02\.claude\plans\composed-swimming-badger.md`.

## [2026-04-11] ingest | landing-page techniques (2 more YouTube transcripts)

Added sources:

- `raw/ai/nick-saraev-claude-kling-animated-sites.md` + `sources/ai/nick-saraev-claude-kling-animated-sites.md`
- `raw/ai/jack-roberts-firecrawl-intelligence-websites.md` + `sources/ai/jack-roberts-firecrawl-intelligence-websites.md`

New concept:

- [[Competitive Intelligence with Firecrawl]] — distinct from brand extraction; scrapes top N competitors in a niche and synthesizes a market intelligence report.

Enriched existing concepts (compounding pattern — added new sources + new sections, did not duplicate):

- [[Brand Extraction with Firecrawl]] — now 2 sources. Added enrichment section on pulling real customer reviews.
- [[Scroll-Driven Animation]] — now 4 sources. Added sections on locomotive-scroll library, "make it faster" iterative optimization loop, reference-image → scroll animation bridge.
- [[Nano Banana Keyframe Workflow]] — now 5 sources. Added Higgsfield reference-image chain for before/after animations, parallel generation tip.
- [[Vercel One-Shot Deploy]] — now 4 sources. Added Netlify as alternative deploy target with tradeoff table.
- [[Frontend Design Skill Pattern]] — now 5 sources. Added community taste skill alternative, UI/UX post-build audit pattern.

Updated: `index.md`.

Compounding validated: 3 of 7 concepts now cite 4+ sources. Zero duplicate concepts created. Dangling wikilink to `[[Notion]]`, `[[Google Reviews]]`, `[[Trustpilot]]`, `[[Glido]]`, `[[Locomotive Scroll]]`, `[[Anti-Gravity]]`, `[[Higgsfield]]`, `[[Netlify]]`, `[[Kling 3.0]]`, `[[Nano Banana 2]]`, `[[Seedance 2.0]]`, `[[Kie.ai]]`, `[[ByteDance]]`, `[[VS Code]]`, `[[Awwwards]]`, `[[Dribbble]]`, `[[Anthropic Frontend Design Skill]]`, `[[GitHub]]`, `[[Vercel]]`, `[[Firecrawl]]`, `[[Hixelon]]`, `[[AnyVan]]`, `[[Claude Code]]`, `[[ffmpeg]]` — deferred to next ingest pass (see wiki/CLAUDE.md lint workflow for when to materialize stubs).
