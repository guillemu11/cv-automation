# Deploy

Phase 6 of the campaign-landing skill. Derived from `wiki/concepts/vercel-oneshot-deploy.md`.

## Hard rules

- **Always ask the user before running any deploy command.** Even preview URLs are publicly accessible.
- **Honor `PIPELINE_DRY_RUN`.** If set, print the command that would run and stop.
- **Always private** when pushing to GitHub (`--private`). Real company names + Paula's name = sensitive.
- **Default to preview deploy**, not production. User promotes to prod manually.

## Prereq check

Before attempting deploy, check CLI availability:

```bash
vercel --version 2>/dev/null && echo "vercel ok" || echo "vercel missing"
```

If missing, tell the user to run `npm i -g vercel` and `vercel login`, then stop. Do not attempt a fallback.

## The command

From inside `output/landing_<slug>/`:

```bash
# Preview (default)
vercel deploy --yes

# Production (only if user explicitly confirms)
vercel deploy --prod --yes
```

Dry-run form (when `PIPELINE_DRY_RUN=true`):

```text
[DRY RUN] would execute: vercel deploy --yes  (from output/landing_<slug>/)
```

## GitHub path (alternative, for version history)

Only if the user explicitly wants a git-backed workflow:

```bash
cd output/landing_<slug>
git init
git add .
git commit -m "campaign-landing: <slug>"
gh repo create paula-landing-<slug> --private --source=. --push
```

Then in Vercel dashboard, import the repo (one click if GitHub OAuth is linked). This gives automatic redeploys on every push.

Skip this path for one-shot deliverables where Paula will never iterate on the landing.

## Output format

After a successful preview deploy, report to the user:

```text
Preview URL: https://<project>-<hash>.vercel.app
Status: <live | building>
Folder:  output/landing_<slug>/
Next:    open the URL, verify on mobile, then promote with `vercel deploy --prod --yes` when ready.
```

Never auto-promote to production. Never open the URL in a browser without asking.

## Netlify alternative

If the user prefers Netlify (same outcome, different host):

```bash
netlify deploy --dir=output/landing_<slug>          # preview
netlify deploy --dir=output/landing_<slug> --prod   # production
```

All the same rules apply (ask first, honor dry run, default to preview).

## After deploy

Append a one-line entry to `output/landing_<slug>/DEPLOY_LOG.md`:

```text
2026-04-11  preview  https://paula-landing-lipton-ax71.vercel.app
```

This is the only persistent record of which URL went where. Do not write a bigger log.
