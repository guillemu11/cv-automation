---
type: concept
domain: ai
tags: [firecrawl, brand-extraction, scraping, landing-page]
status: active
created: 2026-04-11
updated: 2026-04-11
sources: ["[[jack-roberts-claude-nano-banana-websites]]", "[[jack-roberts-firecrawl-intelligence-websites]]"]
---

# Brand Extraction with Firecrawl

Technique for pulling the visual identity of a real company — color palette, logos, typography, tone of voice — directly from its live website, so any generated artifact (landing page, campaign mockup, outreach PDF) grounds itself in the company's real brand instead of generic AI aesthetics.

## How it works

[[Firecrawl]] exposes a `/scrape` endpoint that accepts a URL and returns structured data in multiple formats. One of those formats is `branding`, which extracts:

- Primary and secondary color palette
- Logo assets (as URLs)
- Font families / typography
- Metadata relevant to brand positioning

The Firecrawl playground at `firecrawl.dev` has a UI flow: left sidebar → **Scrape** → **Markdown** → click **Branding**. This returns the same data as the API call.

Because Firecrawl has a REST API, this step can be scripted inside a Claude Code skill. The API key lives in the skill's config; the skill calls it as step 1 of any landing-page-building workflow.

## Why it matters for Paula's pipeline

The whole value of the campaign-landing deliverable rests on **not looking generic**. A landing page that uses anyvan.com's exact green, exact logo, exact typography feels like it was made by someone who spent hours studying the brand. A landing with made-up colors feels like AI slop. Brand extraction is the difference.

For every "hot" job application where Paula wants to ship a landing page as value-add, the flow starts here: `company_url` → Firecrawl → `brand.json` → all downstream generators consume this file.

## Fallback when Firecrawl fails

If Firecrawl returns nothing (some sites block scraping, some have no semantic branding data to extract):

1. Screenshot the homepage with a headless browser / Playwright.
2. Pass the screenshot to Claude with vision and ask it to extract HEX colors, describe fonts, and identify the logo location.
3. Manually download the logo from the site's `/assets/` or via `<link rel="icon">`.

Slower, less reliable, but works on any site.

## Concrete tips from the sources

- [[jack-roberts-claude-nano-banana-websites]]: the full "Branding" format on Firecrawl is one click in the playground — don't write a custom parser, the data is already structured.
- Validate the extracted palette by eye before feeding it to the CSS generator. Firecrawl sometimes picks up accent colors from ads or promotional banners that don't represent the real brand.
- Save the extracted `brand.json` under `output/landing_<slug>/brand.json` so the rest of the skill can read it deterministically.

## Enrichment from competitive intelligence flow

[[jack-roberts-firecrawl-intelligence-websites]] reveals that the same Firecrawl API can also pull **real customer reviews** from the target site (whichever ones are embedded in their Google/Facebook widgets). This is important for Paula's campaign-landing deliverables: if the landing page quotes the company's real reviews in the testimonials section, the deliverable feels researched rather than hallucinated. Add this to the brand extraction output:

- Real review quotes + authors (for use as social proof in the landing)
- Real trust signals present on the site (awards, certifications, logos of past clients)

Note this only works when the target company actually surfaces reviews on their own site. For companies without public reviews, fall back to paraphrasing their brand voice from the About/Mission copy that Firecrawl also extracts.

## Related concepts

- [[Competitive Intelligence with Firecrawl]] — broader use of the same tool for niche-level research.
- [[HTML Replication Pattern]] — complements brand extraction by giving you the full DOM structure.
- [[Frontend Design Skill Pattern]] — consumes the brand tokens to produce taste-aligned output.
