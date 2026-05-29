---
type: source
domain: ai
tags: [landing-page, claude-code, nano-banana, firecrawl, vercel, scroll-animation, seo]
status: active
created: 2026-04-11
updated: 2026-04-11
sources: []
---

# Jack Roberts — Claude Code + Nano Banana 2 = $10k Websites

**Source**: `raw/ai/jack-roberts-claude-nano-banana-websites.md`
**URL**: https://www.youtube.com/watch?v=TZUTe7s11-I
**Author / Publisher**: Jack Roberts (YouTube)
**Date published**: 2025 (exact date unknown)

## TL;DR

End-to-end recipe for one-shotting responsive, branded, SEO-optimized multi-page websites using Claude Code skills + Firecrawl for brand extraction + Nano Banana 2 for keyframe images + Kling/Hixelon for video transitions + Vercel for deploy. Emphasizes that the "wow factor" lives in scroll-driven animations whose quality depends entirely on the start/end keyframes. Also introduces the "HTML replication" trick — download a target site's raw HTML and use it as structural scaffolding.

## Key takeaways

- **Brand extraction first.** Use Firecrawl's `/scrape` endpoint with the `branding` format to pull paleta, logos, typography, and tone from a real company URL before writing any code. This grounds the subsequent work in reality instead of generic AI look.
- **Scroll animations = two good keyframes.** The whole scroll-stopper trick is: generate image A (assembled state) and image B (deconstructed/exploded state) with Nano Banana 2. Feed both as start/end frames to Kling 3.0 via Hixelon (or equivalent) to get a 7s transition video. Everything else is just playback tied to scroll position.
- **Nano Banana tips**: 16×9 aspect ratio, minimum 2K resolution (1K "looks like a kid in PowerPoint"), 4 iterations minimum, clean white background specified explicitly so subjects don't touch edges.
- **HTML replication pattern.** For pitching to real companies: grab their live site via an HTML extractor tool, download it, drop it in the project and tell Claude "I want to recreate this with new copy and the scroll animation added." You inherit their typography, logo, exact structure — only the wow-element is new.
- **Deploy flow**: Claude Code with the Vercel MCP server installed + a Vercel API token → tell it "create a GitHub repo, push it, then create a new Vercel project from it." Two links come back: GitHub repo + live website. Entire flow stays inside Claude.
- **SEO at scale**: A dedicated `/seo-strategy` skill crawls the site, audits robots.txt/sitemap, scores pages, and produces an HTML report with action plan (high-impact items, internal linking suggestions, keywords). Run after the content exists, not before.
- **Multi-page expansion prompt pattern**: "I have an existing website. Look at the current site, understand the design language. Ask me which pages I want to create. For each, match the existing design exactly, add full SEO, structured data, make it fully responsive, update navigation across all pages. Then run a full SEO audit![[hf_20260423_205454_97238098-552e-407b-90f8-17b968b31cc7.mp4]]."
- **Plan-mode + edit-automatically**: Jack recommends plan mode but with "edit automatically" (not "ask before edits") to keep iteration fast. Counterpoint to Nate Herk, who defaults to bypass permissions after plan approval — same outcome different path.

## Quotes

> "The actual scroll is only as good as the start and finish image."

> "1K is like some kid in the garden has had access to PowerPoint or something. Got to be at least 2K."

> "One of the cool techniques I want to show you here, HTML reference. If you like the look of a website, one of the things we can do is grab it — type in HTML website extractor — and download it as HTML because every website is essentially just HTML."

## Entities mentioned

- [[Firecrawl]]
- [[Nano Banana 2]]
- [[Claude Code]]
- [[Vercel]]
- [[GitHub]]
- [[Hixelon]]
- [[Kling 3.0]]
- [[AnyVan]]

## Concepts touched

- [[Brand Extraction with Firecrawl]]
- [[Scroll-Driven Animation]]
- [[Nano Banana Keyframe Workflow]]
- [[HTML Replication Pattern]]
- [[Vercel One-Shot Deploy]]
- [[Frontend Design Skill Pattern]]
