---
type: concept
domain: ai
tags: [vercel, github, deploy, claude-code, mcp]
status: active
created: 2026-04-11
updated: 2026-04-11
sources: ["[[jack-roberts-claude-nano-banana-websites]]", "[[nate-herk-nano-banana-2-websites]]", "[[nate-herk-seedance-2-websites]]", "[[nick-saraev-claude-kling-animated-sites]]"]
---

# Vercel One-Shot Deploy

Pattern for going from "HTML sitting in a local folder" to "live URL shareable in an email" in a single Claude Code prompt, without leaving the IDE. The skill that generates the landing page should be able to deploy it at the end of its workflow.

## The two-tool pipeline

All three sources converge on the same architecture:

- **[[GitHub]]** = code storage. Claude Code creates a repo via the `gh` CLI (Claude handles the auth dance once), pushes all the project files, and returns a repo URL.
- **[[Vercel]]** = deployment target. Once the GitHub repo exists, Vercel either auto-imports it (if the GitHub ↔ Vercel accounts are linked via OAuth) or pulls it via an API call. Vercel builds and serves the site at a `.vercel.app` URL in 30-60 seconds. Every subsequent `git push` triggers an automatic redeploy.

The magic is that a single prompt — _"create a GitHub repo, push this codebase, then create a Vercel project from it and give me the live URL"_ — does the whole thing because Claude Code has the CLIs + MCP servers installed.

## Authentication setup (one-time per machine)

1. **GitHub CLI**: `gh auth login` — pops a browser, user signs in. Claude Code can invoke `gh auth login` and walk the user through it on first use.
2. **Vercel**:
   - Easiest: sign up for Vercel with "Continue with GitHub" so the accounts are linked from day one. Imports are then one-click.
   - MCP path ([[jack-roberts-claude-nano-banana-websites]]): generate an API token at `vercel.com/account/settings/tokens`, add it to Claude Code's MCP config, and the Vercel MCP server handles all operations programmatically from inside Claude Code. Better for automation.
3. **Vercel CLI** (alternative): `npm i -g vercel`, then `vercel login`. Simpler than the MCP server for a local skill that just needs `vercel deploy` and `vercel --prod`.

For Paula's skill, prefer the **Vercel CLI** approach over the MCP server: it's simpler, has fewer moving parts, and matches the "HTML/CSS/JS standalone folder" stack already chosen for the project.

## The frames gotcha

[[nate-herk-nano-banana-2-websites]] hit this live on camera: after pushing the site to GitHub and deploying to Vercel, the hero animation was invisible. Cause: the `frames/` folder with ~120 `.webp` sequence frames had been excluded from the commit (likely by a default `.gitignore` rule ignoring assets). The deployed site had code but no image sequence, so scroll did nothing.

**Fix for the skill**: explicitly verify that the frames folder is tracked in git before pushing. Add a check in the deploy step:

```bash
git status frames/  # must show "new file" entries, not "ignored"
```

Or force-include with `git add -f frames/`. Better: the skill's `.gitignore` template should whitelist `assets/` and `frames/` explicitly.

## Private vs public repos

All three videos note that **private GitHub repos still auto-deploy to Vercel** when linked via OAuth. No need to make the code public. For Paula's use case (personalized job application deliverables with real company names), **always push to private**. The landing gets a shareable Vercel URL; the source code stays hidden.

## Two environments mental model

Borrowed directly from [[nate-herk-nano-banana-2-websites]]: keep a clean distinction between:

1. **Local iteration** — `python -m http.server 8000` in `output/landing_<slug>/`, or `vercel dev`. Fast feedback loop. Try things, break things, no stakes.
2. **Deployed preview** — `vercel deploy` (preview URL, shareable). Used to test on a real phone, send to Paula for review, etc. Redeploys on every push.
3. **Production** — `vercel deploy --prod`. Only when Paula explicitly approves. Gets the primary domain.

For Paula's campaign-landing skill, the default should be **preview deploy** (not prod) — she reviews the preview URL first, then runs `vercel --prod` manually when she's happy. Never auto-promote to prod without confirmation.

## Respect `PIPELINE_DRY_RUN`

Per the root [[CLAUDE.md]] convention, if `PIPELINE_DRY_RUN=true` the skill must NOT actually execute `vercel deploy`. Print the command it would run and stop. This is how all pipeline steps in the project stay testable.

## Domain assignment

[[jack-roberts-claude-nano-banana-websites]] covers the one-click custom-domain flow: inside the Vercel project dashboard, click **Domains**, type the domain you bought (Vercel sells domains too), click assign. Done. For Paula's deliverables this is usually overkill — the auto-generated `<project-name>.vercel.app` URL is enough for an email attachment.

## Netlify as alternative deploy target

[[nick-saraev-claude-kling-animated-sites]] uses **Netlify** instead of Vercel and achieves the same outcome with a near-identical flow. Both are valid; the skill should support either based on Paula's preference. Tradeoffs:

| Dimension | Vercel | Netlify |
| --- | --- | --- |
| Free tier | Generous hobby plan | Free forever, 300 build minutes/month |
| Deploy command | `vercel deploy` / `vercel --prod` | `netlify deploy` / `netlify deploy --prod` |
| CLI install | `npm i -g vercel` | `npm i -g netlify-cli` |
| GitHub auto-sync | Yes, via OAuth link | Yes, via OAuth link |
| Global CDN | Yes (edge nodes) | Yes (edge nodes) |
| Analytics | Built-in (hobby plan limited) | Built-in |
| MCP server | Official Vercel MCP exists | No official MCP at time of writing |

**For Paula's skill**: default to **Vercel** (the plan's chosen stack explicitly says Vercel), but make the deploy step parameterizable so `deploy_target: netlify` is a one-line switch. Both CLIs follow the same `deploy` → preview URL → `deploy --prod` → production URL pattern.

Nick's pragmatic take: "Netlify is free forever on the free plan. You can deploy from AI, Git, or an API. Unlimited deploy previews." The deploy-from-AI angle matters — both platforms accept a programmatic deploy from within a Claude Code skill without any manual browser step.

## Related concepts

- [[Scroll-Driven Animation]] — the thing most likely to break on deploy (via the frames gotcha).
- [[Frontend Design Skill Pattern]] — the parent skill that chains into this deploy step.
