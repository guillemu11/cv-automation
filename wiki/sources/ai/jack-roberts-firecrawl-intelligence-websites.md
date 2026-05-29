---
type: source
domain: ai
tags: [landing-page, firecrawl, competitive-intelligence, claude-code, nano-banana, ui-ux-audit, client-feedback]
status: active
created: 2026-04-11
updated: 2026-04-11
sources: []
---

# Jack Roberts — Claude Code + Nano Banana 2 + Firecrawl = Epic $12k Websites

**Source**: `raw/ai/jack-roberts-firecrawl-intelligence-websites.md`
**URL**: https://www.youtube.com/watch?v=2gvFLFl4xw8
**Author / Publisher**: Jack Roberts (YouTube)
**Date published**: 2025 (exact date unknown)

## TL;DR

Jack's second video goes beyond "pretty pixels" and introduces **competitive intelligence** as the missing ingredient. Uses Firecrawl not just for brand extraction but to scrape the top 5 competitors in a niche, synthesize a market intelligence report (competitor profiles, color palettes, SEO landscape, keyword gaps, content patterns), and use that as a blueprint before any code is written. Also adds a **UI/UX Pro audit skill** for accessibility + SEO checks after the build, and a **client feedback portal pattern** using Notion for post-delivery change management.

## Key takeaways

- **Intelligence layer before design layer.** The most important conceptual leap: don't start with "make a beautiful site for X company." Start with "what are the top 5 performers in X's niche doing, what do they have in common, and what are X's gaps against them." The intelligence report IS the deliverable's foundation.
- **Firecrawl for competitive scraping.** Extends the [[Brand Extraction with Firecrawl]] concept. Same API, different flow: feed it a niche keyword + location ("pool cleaners in East Texas"), it finds top 5 by Google reviews + Trustpilot + search visibility, scrapes each for design, content, branding, logos, SEO. Output is a structured market intelligence report.
- **Ranking algorithm.** The skill uses Google rankings + review counts + Trustpilot + "several other factors" to pick the top 5. Not just Google SERP.
- **Print-ready intelligence report.** The report includes: executive summary, current website audit (strengths + critical gaps), 5 competitor profiles with logos and color palettes side by side, SEO landscape, keyword gaps, "what winners do exceptionally well", recommended site structure, winning blueprint. This report itself is a valuable deliverable — Jack notes "I get people reaching out saying 'here's a deep dive on your business' and it never looks this good."
- **Real review pull-through.** When building the site, Firecrawl pulls the target company's ACTUAL Google/Facebook reviews and inserts them into the testimonials section. Trust signals are real, not fabricated.
- **Reference image flow in Higgsfield / Nano Banana 2.** For the scroll-driven "dirty pool → clean pool" animation: (1) generate dirty pool image with Nano Banana 2 (4 iterations, 16×9, 2K, white background), (2) pick the best one, (3) click "reference" on it in Higgsfield, (4) paste the clean pool prompt — now the clean version shares the exact same pool structure/angle/composition as the dirty one. Solves the keyframe consistency problem.
- **UI/UX Pro audit skill** — a public skill that runs ~15 accessibility checks, ~8 SEO fixes, improvements on image dimensions, form feedback, touch and interaction. Run as a post-build quality pass. Output is a checklist of what was changed.
- **Mobile vs desktop hero swap**: for scroll-driven animations, you can generate a **separate hero asset for mobile** (square aspect ratio) and swap based on breakpoint. One-prompt change: "use this asset below the mobile breakpoint."
- **Client feedback portal via Notion** (not applicable to Paula's use case but worth noting for completeness): a Notion database connected to a form on the deployed site. Clients submit tweaks through the form → Notion → Claude reviews them nightly. Three-tier: trivial copy changes auto-approved, structural changes flagged for human review.
- **Glido** for speech-to-text when prompting Claude Code. Jack uses it to dictate prompts instead of typing. Nick Saraev uses a similar tool. Paula could consider this if the skill workflow involves a lot of back-and-forth.

## Quotes

> "It isn't just a gorgeous website, it's got substance."

> "This has a really intelligent algorithm about how it determines what the top websites are. We do that based on Google rankings, reviews, and several other factors."

> "These should be actual reviews that exist on Google."

## Entities mentioned

- [[Firecrawl]]
- [[Anti-Gravity]]
- [[Claude Code]]
- [[Nano Banana 2]]
- [[Higgsfield]]
- [[Kling 3.0]]
- [[Notion]]
- [[Google Reviews]]
- [[Trustpilot]]
- [[Glido]]

## Concepts touched

- [[Competitive Intelligence with Firecrawl]] (new concept from this source)
- [[Brand Extraction with Firecrawl]]
- [[Nano Banana Keyframe Workflow]] — reference-image trick for keyframe consistency
- [[HTML Replication Pattern]]
- [[Frontend Design Skill Pattern]] — UI/UX Pro audit as a post-build skill
- [[Scroll-Driven Animation]]
