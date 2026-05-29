---
type: concept
domain: ai
tags: [claude-code, skill, frontend, taste, meta]
status: active
created: 2026-04-11
updated: 2026-04-11
sources: ["[[jack-roberts-claude-nano-banana-websites]]", "[[nate-herk-nano-banana-2-websites]]", "[[nate-herk-seedance-2-websites]]", "[[nick-saraev-claude-kling-animated-sites]]", "[[jack-roberts-firecrawl-intelligence-websites]]"]
---

# Frontend Design Skill Pattern

Meta-pattern: Claude Code produces dramatically better landing pages when a **taste-layer skill** is loaded alongside the task. The skill doesn't write code — it's a `.md` file that injects aesthetic judgment, anti-AI-slop rules, and design tokens into Claude's context before it generates anything.

Both Anthropic and the YouTube community have converged on this approach. Anthropic ships `/frontend-design` as an official Claude Code plugin. Community versions (Nate Herk, Jack Roberts) are forks with use-case-specific overrides.

## What's in a frontend design skill

A typical skill.md contains:

- **Anti-slop rules**: forbidden aesthetics (gradients everywhere, centered hero with 3 CTAs, default shadcn purple, lorem ipsum, stock photos, emoji in UI).
- **Preferred aesthetics**: typography scale, spacing rhythm, color discipline (max N colors), asymmetric layouts, editorial feel, calibrated shadows.
- **Framework preferences**: Tailwind utilities vs custom CSS, component libraries to prefer/avoid, animation libraries.
- **Micro-rules**: "Never use border-radius above 12px except on pill buttons", "Headings should use display font at >48px on desktop", "Never place hero text at screen center; offset left or right".
- **Examples** of good vs bad outputs, often pulled from Awwwards or Dribbble.

The skill is loaded into context every time Claude Code starts generating UI code. The effect is like having a senior designer whisper rules into Claude's ear throughout the build.

## Two sources of skill content

1. **Anthropic's official `/frontend-design`**. Install via `/plugins` → search → install globally. Run `/reload plugins` to pick it up. Then `/frontend-design` is available.
2. **Community skills** — Nate Herk's `video-to-website`, Jack Roberts' `scroll-stop-prompter` and `3D-website-builder`, etc. These are markdown files distributed via free school communities or GitHub. Installing them is literally "drag the `.md` into `.claude/skills/` and Claude Code finds it".

## The compounding loop

[[nate-herk-nano-banana-2-websites]] makes an important observation: every time you use the skill and spot a problem in the output, you can **update the skill.md itself** with the fix. Next time, the skill is smarter. Over weeks of use, a heavily-iterated skill produces dramatically better first-pass websites than any one-shot prompt.

For Paula's `campaign-landing` skill, this means:

- Skill starts minimal (the 6-phase workflow from the plan).
- After every "hot" job deliverable, Paula notes what was wrong with the output.
- Before the next use, update the skill's rules to prevent that specific mistake.
- Over 10-20 uses, the skill stabilizes into something very high quality.

This is not optional. It's the only way skills stay useful — they rot if never updated.

## Skill structure for the campaign-landing case

Following Anthropic's progressive disclosure principle, the skill directory should look like:

```text
.claude/skills/campaign-landing/
├── SKILL.md              ← loaded by default (frontmatter + workflow outline)
├── references/           ← loaded on demand
│   ├── workflow.md
│   ├── brand-extraction.md
│   ├── animation-patterns.md
│   └── deploy.md
├── templates/            ← file templates referenced by workflow steps
│   ├── base.html
│   ├── styles.css
│   └── scroll.js
└── examples/             ← reference outputs
```

Only SKILL.md is in context by default. The `references/` files are read only when Claude reaches the relevant workflow phase. This keeps the context window clean on every invocation.

The content of `references/animation-patterns.md` should be derived directly from [[Scroll-Driven Animation]] and [[Seedance Loop Video Hero]] in this wiki — the concept pages are the source of truth, the skill file is just a copy for Claude Code to load quickly without hopping into the wiki vault every time.

## Community taste skills as alternative

[[nick-saraev-claude-kling-animated-sites]] uses a community taste skill from an open GitHub repo (the "cracked 16-year-old" / Leon's skill) instead of Anthropic's official `/frontend-design`. Both work the same way — load via `.claude/skills/` or by pointing Claude Code at the repo URL — but community ones often have stronger opinions on specific aesthetics (high-end luxury, brutalist, editorial) that match narrower use cases better than the general-purpose Anthropic skill.

For Paula's `campaign-landing` skill, the right call is **Anthropic's official `/frontend-design` as the base** (stable, maintained, updated with each Claude release) **plus use-case-specific overrides** in the skill's own `references/` files that layer brand/marketing-campaign aesthetics on top. This avoids depending on a GitHub repo that might disappear but still gets domain-specific taste rules.

## UI/UX post-build audit pattern

[[jack-roberts-firecrawl-intelligence-websites]] introduces a second layer: a dedicated **UI/UX audit skill** that runs *after* the build and does ~15 accessibility checks, ~8 SEO fixes, and improvements on image dimensions, form feedback, and touch interaction. This is distinct from the taste skill — the taste skill shapes the initial generation; the audit skill validates quality before ship.

For Paula's campaign-landing skill, the workflow should be:

1. Plan → build using `frontend-design` + campaign-landing references (the taste layer).
2. Preview locally via `python -m http.server`.
3. **Run the audit skill** as the final phase before deploy. It returns a checklist of what was fixed (alt tags added, skip links inserted, color contrast corrected, meta tags filled, etc.).
4. Only then deploy via [[Vercel One-Shot Deploy]].

This two-stage pattern (creative build → quality audit) catches the accessibility and SEO issues that taste-layer skills don't explicitly check for. It also makes the deliverable more defensible — Paula can tell a recruiter "this landing page passes WCAG AA" because the audit skill verified it.

The audit skill itself can be authored as `.claude/skills/ui-ux-audit/` — another standalone skill installed globally, not part of campaign-landing directly. That way it's reusable for any site Paula builds in the future, not just campaign landings.

## Related concepts

- [[Brand Extraction with Firecrawl]] — phase 1 input to the skill.
- [[Scroll-Driven Animation]] — one of two animation patterns the skill routes between.
- [[Seedance Loop Video Hero]] — the other animation pattern.
- [[HTML Replication Pattern]] — alternative scaffolding source.
- [[Vercel One-Shot Deploy]] — final phase of the skill workflow.
