---
type: concept
domain: ai
tags: [html, scaffolding, landing-page, scraping, pattern]
status: active
created: 2026-04-11
updated: 2026-04-11
sources: ["[[jack-roberts-claude-nano-banana-websites]]"]
---

# HTML Replication Pattern

Technique for generating a landing page that feels **structurally identical** to a target company's real website — same sections, same copy blocks, same visual rhythm — but with new content (e.g., Paula's fictional campaign) inserted into that scaffolding. This makes the deliverable feel like a native extension of the company's existing site rather than a third-party mockup.

## Core idea

Every website is ultimately HTML + CSS + JS in the browser. If you can download the rendered HTML, you have a perfect scaffold: the exact div structure, the exact class names, the exact Tailwind/Bootstrap utility stack they use, the exact nav layout, the exact footer. You then hand that scaffold to Claude Code and say: "Rebuild this site from the existing HTML. Keep the structure and typography. Replace the copy with this new campaign. Add a scroll-driven hero animation where the Jumbotron currently lives."

## The flow

1. Go to the company's real website (e.g., `anyvan.com`).
2. Use an online HTML extractor tool (Google "HTML website extractor" — there are several free ones that return a downloadable .html file including inlined assets). [[jack-roberts-claude-nano-banana-websites]] uses one without naming it specifically — any that returns the full DOM works.
3. Download as a `.html` file.
4. Drop it into the Claude Code project folder.
5. Prompt: _"I've just downloaded the HTML from the original website. I want you to use that HTML to recreate it with new copy and the scroll-stopping animation included. Keep their logo, typography, color tokens. Only swap the copy and add the new hero."_

Claude Code reads the file, understands the design language (because it's literally in the markup), and produces a new site that inherits the structural DNA.

## Why this works better than "inspired by"

Asking Claude to "build me a landing page that looks like anyvan.com" produces something that vaguely resembles it. Asking Claude to "use this exact HTML as scaffolding" produces something that **is** it structurally. The difference is enormous in perceived polish:

- Fonts match exactly because they're loaded from the same CDN URLs
- Color tokens match because they're in the inlined CSS
- Section rhythm matches because the flex/grid structure is copied
- Nav/footer are pixel-identical

The only thing that's new is the hero animation and the content blocks Paula explicitly replaces.

## When to use this vs. from-scratch

- **Use HTML replication** when pitching to an established company that already has a recognizable site. The goal is "here's what your site could look like with this campaign layered on top."
- **Use from-scratch generation** when the company has no web presence, a terrible site that would hurt the deliverable, or when Paula wants to show independent creative direction. In those cases, [[Brand Extraction with Firecrawl]] + [[Frontend Design Skill Pattern]] is the cleaner path.

## Legal / ethical note

This produces a derivative work of the company's HTML. For a private deliverable sent directly to a hiring manager at that same company as part of a job application, this is fine (they own the original). **Do not publish** replicated sites to public URLs without permission — just host for sharing, password-protect, or send as a zipped folder.

## Related concepts

- [[Brand Extraction with Firecrawl]] — alternative path when you want brand tokens without the full DOM.
- [[Frontend Design Skill Pattern]] — the decision layer that picks between these two approaches.
- [[Scroll-Driven Animation]] — what gets inserted into the replicated scaffold.
