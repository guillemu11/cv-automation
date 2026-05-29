---
type: source
domain: ai
tags: [landing-page, claude-code, nano-banana, kling, scroll-animation, ffmpeg, vercel, skill-design]
status: active
created: 2026-04-11
updated: 2026-04-11
sources: []
---

# Nate Herk — Nano Banana 2 + Claude Code = $10k Websites

**Source**: `raw/ai/nate-herk-nano-banana-2-websites.md`
**URL**: https://www.youtube.com/watch?v=q0TgUtj6vIs
**Author / Publisher**: Nate Herk (YouTube)
**Date published**: 2025 (exact date unknown)

## TL;DR

Walkthrough of a "video-to-website" Claude Code skill that ingests a product video (generated via Nano Banana 2 start/end keyframes + Kling animation) and produces a scroll-driven one-page product landing. Frames are extracted with ffmpeg, each frame tied to a scroll position — this is NOT video playback, it's image sequence animation. Demonstrates end-to-end: image generation → video → Claude Code plan mode → localhost test → GitHub → Vercel deploy. Worked example: "Obsidian Vortex" fictional blender brand built in 30 minutes.

## Key takeaways

- **The skill is a markdown file.** "All of the magic lives in the skill.md. Turn a video into a premium scroll-driven animated website." Contains best practices that make websites feel premium on the first try. Skills are instructions, not code.
- **Two skills needed**: (a) `frontend-design` (modified version of Anthropic's official skill for taste/aesthetics), (b) `video-to-website` (Nate's custom skill for the scroll-driven pipeline).
- **ffmpeg dependency**: The skill extracts frames from the input video (~120 webp frames from a short clip). Each frame is mapped to a scroll position so users control playback by scrolling. Claude Code auto-installs ffmpeg if missing.
- **Dark-mode composition trick**: If the input video is on a black background, prompt: "background of the website should be completely black so it should blend into the background of the image, making it feel like one fluid page." Makes the product feel integrated, not bolted on.
- **Plan mode is mandatory** for quality. Claude asks clarifying questions (product name? brand? sections?) and produces a to-do list. Accept plan → switch to bypass permissions mode so it runs uninterrupted.
- **Two environments mental model**: localhost (for iteration) and the cloud/Vercel (for production). Always iterate locally, then push to GitHub, then Vercel auto-deploys from the repo.
- **Common deploy gotcha**: By default GitHub ignores large binary folders. The frames folder was auto-excluded, so the deployed site had no animation. Fix: explicitly tell Claude "you need the frames in the codebase." Keep this in mind for any scroll-driven site.
- **Skill iteration loop**: After building each site, tell Claude "here's what I told you to fix, here's what worked. Reflect this in the skill.md." Every build makes the skill smarter. This is compounding.
- **Mobile optimization is a second pass.** First build is desktop-first; Nate explicitly says "mobile optimization would be the next step." Don't expect one-shot mobile perfection.

## Quotes

> "All of the animations you're seeing on the site — they're just videos. I had Nano Banana generate two different images for me and then turn it into a video."

> "It basically associates each of these frames with a scroll position. So as you scroll down, it kind of like reveals itself or if you scroll backwards, it goes the other way."

> "Every single time that you build a website with this skill, the skill gets better and better and better."

## Entities mentioned

- [[Nano Banana 2]]
- [[Claude Code]]
- [[Kling 3.0]]
- [[Kie.ai]]
- [[ffmpeg]]
- [[Vercel]]
- [[GitHub]]
- [[Anthropic Frontend Design Skill]]
- [[VS Code]]

## Concepts touched

- [[Scroll-Driven Animation]]
- [[Nano Banana Keyframe Workflow]]
- [[Frontend Design Skill Pattern]]
- [[Vercel One-Shot Deploy]]
- [[Plan Mode Bypass Permissions]]
- [[Skill Compounding Loop]]
