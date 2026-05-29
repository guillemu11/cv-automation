---
type: concept
domain: ai
tags: [firecrawl, competitive-intelligence, research, seo, landing-page]
status: active
created: 2026-04-11
updated: 2026-04-11
sources: ["[[jack-roberts-firecrawl-intelligence-websites]]"]
---

# Competitive Intelligence with Firecrawl

Distinct from [[Brand Extraction with Firecrawl]] — this is the **pre-design research step** that answers "what does best-in-class look like for this niche?" before any code or design decisions are made. Firecrawl scrapes the top N competitors in a niche, synthesizes what they have in common, and produces an intelligence report that acts as the blueprint for the subsequent design work.

## Why this is different from brand extraction

| | Brand extraction | Competitive intelligence |
|---|---|---|
| Input | 1 company URL | Niche keyword + location |
| Output | Colors, logo, typography of that company | Comparative report across top 5 competitors |
| Purpose | Make artifact look ON-BRAND for that company | Make artifact meet/exceed NICHE STANDARDS |
| Used when | You have a specific target to mimic | You need to understand what "good" means in this market |

For Paula's campaign-landing skill, both matter:
- Brand extraction grounds the visual style in the target company's real identity.
- **Competitive intelligence grounds the strategy** — what kind of hero section do Brand Managers expect? What trust signals are table stakes in Dubai retail? What content depth does SEO require for the specific vertical?

Without the intelligence layer, you produce a pretty deliverable that doesn't know what "good" means for that particular industry.

## The flow (per [[jack-roberts-firecrawl-intelligence-websites]])

1. **Define niche + geo**. Example: "pool cleaners in East Texas", "luxury retail in Dubai", "SaaS HR tools in MENA". Geo matters because market norms differ.
2. **Invoke Firecrawl with the niche query**. The skill uses Firecrawl's search + scrape to find the top ~5 competitors ranked by:
   - Google rankings (SERP position for the niche keyword)
   - Review count & rating (Google Reviews, Trustpilot)
   - Search visibility
   - "Several other factors" (Jack doesn't fully enumerate — the ranking logic lives inside the skill)
3. **Scrape each competitor**. For each top competitor, Firecrawl extracts: design tokens (colors, typography), content (copy, CTAs, section structure), branding (logo, tone), SEO (meta, keywords, backlinks).
4. **Synthesize**. Claude reads all 5 scrapes and produces a structured report with these sections:
   - Executive summary
   - Target company audit (strengths + critical gaps vs the top 5)
   - Competitor profiles (logos and color palettes side by side)
   - "What winners do exceptionally well" (patterns common to multiple winners)
   - SEO landscape (keywords the top 5 rank for, gaps in target's SEO)
   - Recommended site structure (derived from common winner patterns)
   - Winning blueprint (hero strong headline → service categories → photo gallery → about → blog)
5. **Use the blueprint as scaffolding** for the subsequent design work. Don't invent a structure — copy what's proven to work in the niche.

## What the report itself is worth

Jack notes this is usable as a **standalone deliverable**, not just an internal artifact. For Paula's use case: the intelligence report could be attached to the outreach email as a second piece alongside the landing page. Combined value:

- Landing page = "here's what your brand could do with a campaign like X"
- Intelligence report = "here's what your market is already doing, and here's where you're losing ground"

Two deliverables from one Firecrawl run. Very high perceived value for minimal extra effort.

## Where the data can be unreliable

- **Review scraping** depends on the competitors having real Google/Trustpilot profiles. Luxury/B2B niches often lack this data — some top performers in Dubai retail have no Trustpilot presence at all.
- **SERP ranking** varies by query and geo. Running the skill from a US IP when researching a Dubai niche will pull US-centric results. Use a VPN or explicitly geo-target in the Firecrawl query.
- **"Top 5" is algorithmic**. The skill picks by its own ranking logic, which may not match what Paula as a domain expert would pick. **Always sanity-check** the chosen competitors before consuming the report.

## Related concepts

- [[Brand Extraction with Firecrawl]] — same tool, narrower use case.
- [[Frontend Design Skill Pattern]] — the taste layer that reads this report and converts it into design decisions.
- [[HTML Replication Pattern]] — downstream: pick the best competitor from the report and scaffold from their HTML.
