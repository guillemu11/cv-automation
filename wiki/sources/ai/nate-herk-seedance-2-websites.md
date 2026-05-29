---
type: source
domain: ai
tags: [landing-page, claude-code, seedance, kie-ai, loop-video, hero-video, vercel, dribbble]
status: active
created: 2026-04-11
updated: 2026-04-11
sources: []
---

# Nate Herk — Seedance 2.0 + Claude Code = $10k Websites

**Source**: `raw/ai/nate-herk-seedance-2-websites.md`
**URL**: https://www.youtube.com/watch?v=NvxiSG34mPU
**Author / Publisher**: Nate Herk (YouTube)
**Date published**: 2025 (exact date unknown)

## TL;DR

Companion video to the Nano Banana piece, but for a different kind of hero: a **seamless loop video** playing continuously in the background (architecture firm example) instead of a scroll-driven frame sequence. Introduces ByteDance's Seedance 2.0 video model (via Kie.ai) and the trick of setting first-frame = last-frame so the loop is invisible. Also shows the "design-reference grab" pattern — take a screenshot from Awwwards or Dribbble and tell Claude "make the design feel more like this" to avoid generic AI output.

## Key takeaways

- **Two hero patterns, pick one per site**:
  - *Loop video* (this video): video plays on autoplay forever, user scrolls past it. For mood/atmosphere — car in desert, architecture firm, luxury feel.
  - *Scroll-driven frame sequence* (Nano Banana video): user's scroll controls playback position. For product reveals, exploded diagrams, feature walkthroughs.
- **Seamless loop trick**: In Seedance 2, set the **first frame** and **last frame** to the SAME input image. The AI generates all the in-between motion. When the video loops back, there's no visible seam. Also: turn off audio generation for web use.
- **10s > 15s for hero loops**: Cheaper (410 vs 625 credits on Kie.ai) and feels more fast-paced/engaging on a landing page. 15s drags.
- **Kie.ai as model router**: One API key, hits Seedance, Nano Banana, Qwen, GPT-image, Kling, Gemini 3, etc. Nate uses it daily because of single-auth + pricing. Good for a skill that needs multiple image/video models without maintaining 5 different API clients.
- **Image-prompt symmetry**: Generate hero image at 16×9 aspect ratio so the video output matches without letterboxing. Generic trap to avoid.
- **`/frontend-design` as an official Claude Code plugin**: Nate installs it via `/plugins`, then `/reload plugins`. This is the Anthropic-published version. Makes Claude's design taste significantly better out of the box. Also confirms skill-installation flow via Claude Code's plugin system.
- **Design-reference grab pattern**: Go to Awwwards or Dribbble → find a site in the same vibe as what you want → save the screenshot → drop it in Claude Code → "make the section below the video feel more like this style." This is a fast way to avoid the "AI slop" look without hand-prompting every aesthetic detail.
- **settings.local.json for permissions**: Instead of clicking "yes" on every tool call, drop a `settings.local.json` into `.claude/` that pre-authorizes the tool list. Speeds up iteration massively. Alternative to bypass permissions mode.
- **Private GitHub repos auto-deploy to Vercel too.** No need to make the repo public. Sync once and every push triggers a redeploy in 30-60s.
- **Iteration reality check**: Nate shows that even on a "30-minute site" he added a second small video (engine revving) under the stats section after seeing the first pass. Good sites are built in iterative passes, not one-shot.

## Quotes

> "I want the first frame and the last frame to be the same so that this video is basically just like an endless loop and it feels very seamless to the user on our site."

> "It's basically like an open router for different models when it comes to video, image, and music. One API key and you can hit any model you want."

> "You could go to something like Dribbble or Awwwards, save the image, and say 'make everything feel a little bit more like this style'."

## Entities mentioned

- [[Seedance 2.0]]
- [[Kie.ai]]
- [[Claude Code]]
- [[Nano Banana 2]]
- [[Vercel]]
- [[GitHub]]
- [[Awwwards]]
- [[Dribbble]]
- [[Anthropic Frontend Design Skill]]
- [[ByteDance]]

## Concepts touched

- [[Seedance Loop Video Hero]]
- [[Nano Banana Keyframe Workflow]]
- [[Frontend Design Skill Pattern]]
- [[Vercel One-Shot Deploy]]
- [[Design Reference Grab Pattern]]
- [[Plan Mode Bypass Permissions]]
