# Consumer mode

Structure and copy rules for `mode: consumer` — the live ad-landing variant. Read this instead of `workflow.md` phase 3 when consumer mode is active.

## What this is

The page a real consumer lands on after clicking a paid social ad (Meta, TikTok, X, Google Display). The ONLY thing that matters is **conversion** — the fraction of visitors who submit the lead form. Everything else is supporting material to get them to the form.

## Hard differences vs pitch mode

| Dimension | Pitch mode | Consumer mode |
| --- | --- | --- |
| Audience | CMO / internal decision-maker | End consumer (Gen Z / millennial) |
| Goal | "This person understands strategy" | "How many leads did we capture?" |
| Copy voice | Third person, analytical, data-driven | Second person, benefit-first, conversational |
| Primary KPI | Brand love, reach | Conversion rate, CPL, form completion |
| Length | 6 sections (hero → credits) | 5 sections (hero → form → legal) |
| Credits footer | Paula named as proposer | Paula credited sub-line only; main footer is brand legal |
| Disclaimer | "Fictional concept" pill at top | Standard brand T&C language + fictional disclaimer at the bottom |

## Section structure (in order)

### 1. Hero with the hook (sticky scroll stage, 3-4 chapters)

Same scroll-stage mechanic as pitch mode — reuse the 150 frames from the hero video when the visual matches both campaigns. Chapters are different:

- **Chapter 1 — The Hook** (0.00-0.22). Big tagline + 1-line subhead. Primary CTA button visible even during the animation, floating bottom-right, links to the form anchor below.
- **Chapter 2 — The Offer** (0.26-0.48). What exactly the user gets if they convert. ONE clear line. e.g. "Claim your free Lipton Half-Sugar can, redeemable at any 7-Eleven in the UAE."
- **Chapter 3 — Urgency / social proof** (0.52-0.78). A counter, a countdown, or a claim number. e.g. "2,341 cans already claimed in the last 24 hours" (fake but plausible).
- **Chapter 4 — The ask** (0.82-1.00). One-line CTA repeated with an arrow pointing down toward the form. e.g. "Claim yours in 30 seconds ↓"

### 2. How it works (traditional section, 3 steps)

Three numbered steps. No more. Must fit on one screen on mobile. Example for a sampling funnel:

1. **Tell us where** — pick your nearest store.
2. **Get your code** — we text you a QR in 30 seconds.
3. **Enjoy it cold** — redeem at the counter.

### 3. Lead capture form (the entire point of the page)

Fields — ask the MINIMUM number required to satisfy the mechanic. Every extra field drops conversion ~7%.

Standard sampling funnel form:
- First name (required)
- Mobile (+971 / +966 / etc, required, validates format)
- Email (required)
- City (required, select from AMESA cities)
- Age bracket (optional, one-tap: 18-24 / 25-34 / 35+)
- GDPR/PDPL consent checkbox (required)
- Marketing opt-in checkbox (optional, pre-checked only if legally allowed in the market)
- Primary CTA button — full-width, brand-primary bg, verb-first copy ("Claim my free can")

The form block must be visible without scrolling past any other sections once How-It-Works ends.

### 4. FAQ (optional, 3-5 items, collapsed accordion)

Only include if there's a real question that blocks conversion. Typical:
- "Is this real?" (yes, fictional-concept disclaimer goes at the bottom not here)
- "How soon will I get the code?"
- "What if I don't have a store nearby?"
- "How do you use my data?"

Skip entirely if you don't have genuine objections to handle.

### 5. Legal footer

Not the pitch-mode credits. This is standard brand T&C language:

- Brand name + copyright line
- Privacy policy / Terms links (dummy hrefs fine)
- Cookie notice link
- **At the very bottom, in small muted text**: "Fictional campaign concept created by Paula De Francisco as a job-application deliverable. Not affiliated with or endorsed by \<brand\>." This is the only mention of Paula on the page.

## Copy rules

- **Second person always.** "You" not "they". "Your afternoon" not "the consumer's afternoon".
- **No jargon.** No "AMESA", no "penetration", no "KPI", no "DMP". Those belong in pitch mode.
- **Benefit-first headlines.** Not "Lipton Ice Tea Half-Sugar campaign" but "Half the sugar. Twice as cold."
- **Short paragraphs.** Max 2 sentences. Read on a phone, on the metro, with one thumb.
- **One CTA verb.** Pick it early and repeat it 4+ times. "Claim" or "Get" or "Enter" — never mix.
- **Numbers for credibility.** "2,341 claimed today" beats "many people have claimed".

## Visual rules

- Reuse the same brand tokens from `brand.json`.
- Reuse the same hero frame sequence if the visual works for both audiences — a bottle pouring over ice is universally compelling.
- The form block is ALWAYS the highest-contrast element on the page. Use `--brand-primary` as the CTA button background with `--brand-text` as foreground for maximum pop.
- No execution-card grid (that's pitch mode). No KPI counter grid (that's pitch mode).
- Include a sticky bottom-of-viewport CTA bar on mobile ("Claim in 30s →") that persists below the scroll stage and disappears only when the form itself is on screen.

## Form handling

The skill generates a static HTML form. Submission handling options:

- **Default**: `action="mailto:paulich98@hotmail.com"` — submissions arrive as an email. Zero infra. Works for a demo deliverable sent to a recruiter who will click "Claim" once and see the form work.
- **Optional upgrade** (user asks): Formspree / Getform / Netlify Forms — real lead capture, free tier, 1 line change to the form `action`.
- **Never**: a fake form that does nothing on submit. If the user clicks and nothing happens, the deliverable looks broken. Always wire it to something, even if it's just mailto.

Add a client-side `onsubmit` handler that:
1. Validates required fields
2. Shows a thank-you state in place of the form ("Thanks! We'll text your code within 60 seconds.")
3. For mailto path, still falls through to email; for Formspree path, uses fetch.

## Files produced

```
output/landing_<slug>_consumer/
├── index.html          ← scroll stage + form + legal
├── styles.css          ← reuses brand tokens, adds form styles
├── scroll.js           ← same scroll orchestration as pitch mode
├── brand.json          ← (shared if landing_<slug> already exists, else regenerated)
└── assets/
    ├── frames/         ← symlink or copy from pitch-mode landing
    ├── hero-loop.mp4   ← same
    └── hero-keyframe-*.png
```

The slug gets `_consumer` suffix so pitch and consumer modes for the same brand coexist.