---
type: source
domain: ai
tags: [landing-page, claude-code, nano-banana, kling, higgsfield, netlify, locomotive-scroll, performance]
status: active
created: 2026-04-11
updated: 2026-04-11
sources: []
---

# Nick Saraev — Claude Code + Nano Banana 2 + Kling = $15K Animated Sites

**Source**: `raw/ai/nick-saraev-claude-kling-animated-sites.md`
**URL**: https://www.youtube.com/watch?v=ZfYvv-0l9NA
**Author / Publisher**: Nick Saraev (YouTube)
**Date published**: 2025 (exact date unknown)

## TL;DR

Most pragmatic of the five transcripts: Nick built 4 different animated websites in 15 minutes using the **Anti-Gravity IDE** (not VS Code), a community "taste skill" from an open GitHub repo (the "cracked 16-year-old" skill), Kling 3.0 via Higgsfield for video, and **Netlify** (not Vercel) for deploy. Emphasizes a "make it faster" iterative optimization loop where Claude auto-extracts video frames as JPEGs and ties them to scroll position via **locomotive-scroll**. Total cost per site: ~$2-5 in model tokens.

## Key takeaways

- **Two-tool stack is enough.** Anti-Gravity (IDE) + Higgsfield (for Kling 3.0 video) is the minimum viable set. No need for 30 platforms. Three steps: prompt Claude → generate video with Kling → integrate and push live.
- **"Leon's skill" — community taste skill.** Nick references a public GitHub repo by "a cracked 16-year-old" that instills high-end design principles as a taste layer. Install by sending the repo URL to Claude Code with "use this skill." This is the same pattern as Anthropic's official `/frontend-design` but maintained by the community.
- **Inward masking gradient trick.** For hero videos that have a colored background that clashes with the site: apply an inward masking gradient around the video element so it fades into the site background. Prevents the jarring color-seam that otherwise breaks hero sections.
- **Mouse-position parallax as bonus.** Claude sometimes ties the hero element to mouse position unprompted, creating a subtle parallax. Nice-to-have, not a requirement.
- **"Generate 2-3 simultaneously"**. For any video generation step, kick off 2-3 parallel jobs in Kling/Higgsfield. Increases probability that at least one hits the desired output. Cost: ~$1 extra per alternative. Worth it to avoid regenerating.
- **Locomotive-scroll library.** When Claude builds the scroll-driven animation, it imports `locomotive-scroll` under the hood. This is the JS library that makes scroll-hijacking smooth instead of janky.
- **The "make it faster" meta-prompt.** Most powerful pattern in the video: after initial build, say "make it faster" to Claude. It extracts video frames as optimized JPEGs, ties each to a scroll position, adds frame preloading, compresses the hero image (5.3 MB → 252 KB in one prompt). You can run this 3-4 times, assessing quality regression, to find the fast/quality sweet spot.
- **Netlify as free deploy alternative.** "Make it live on Netlify" — one prompt deploy. Free forever plan with global CDN edge nodes, unlimited preview deploys. Alternative to Vercel for Paula's skill; same outcome different vendor.
- **Mobile optimization is a one-prompt fix.** "Mobile optimize the site 3 or 4 times" — Claude handles the breakpoints. Don't over-engineer mobile in the first pass.
- **15 minutes, $2-5 per site, ~$1 in Claude usage.** The economics are no longer a barrier. Iteration and generation count is limited by taste, not cost.

## Quotes

> "Isn't that wild how you could literally just say 'make it load significantly faster' in 2025."

> "You don't have to hop around like 30 different platforms. There's really just three steps."

> "As a former web developer, some of the stuff that this thing does blows my mind. It would have taken me like 3 days to do what this just did in 30 seconds."

## Entities mentioned

- [[Claude Code]]
- [[Anti-Gravity]]
- [[Nano Banana 2]]
- [[Kling 3.0]]
- [[Higgsfield]]
- [[Netlify]]
- [[Locomotive Scroll]]
- [[Glido]]

## Concepts touched

- [[Scroll-Driven Animation]] — specifically the frame-extraction + preloading optimization path
- [[Nano Banana Keyframe Workflow]] — generate multiple simultaneously for selection
- [[Frontend Design Skill Pattern]] — community taste skill alternative to Anthropic's `/frontend-design`
- [[Vercel One-Shot Deploy]] — Netlify as alternative deploy target
- [[Make It Faster Meta Prompt]]
