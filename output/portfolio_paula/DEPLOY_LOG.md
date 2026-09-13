# Deploy log — Paula De Francisco portfolio

Personal single-page portfolio. Editorial warm-paper system (Italiana + Geist).
Vercel project: `paula-de-francisco` (permanent — do NOT reuse the rotating paula-pitch-a/b slots).

| Date | Env | URL | Notes |
|---|---|---|---|
| 2026-08-22 | prod | https://paula-de-francisco.vercel.app | initial launch · CLI (authed guillemu11) · deploy dpl_4xM1QHqCg1JokMfySuNYEzR3Wfie · clean domain public (200); *-projects.vercel.app URL is SSO-protected (302) |
| 2026-08-23 | prod | https://paula-de-francisco.vercel.app | deploy dpl_4JramLvrRB3vXDCuALmaY8NLmE7G · (1) ONE photo only — removed about-section portrait (`portrait_about.*` deleted), kept hero headshot; hero img hardened `aspect-ratio:1/1; object-fit:cover` so it can never stretch. (2) Work section restructured: **Live work — DoFreeze** (dofreeze.ae e-commerce built in Lovable · Befit Crew affiliates dofreeze.ae/affiliates · Email/CRM) leads; concept campaigns demoted to a secondary row (Revolut, Colgate, +Lipton `landingliptonv2`). CSS bumped v3→v4 |
| 2026-08-23 | prod | https://paula-de-francisco.vercel.app | deploy dpl paula-de-francisco-rgkazxlug · **PHOTO FIX (real bug):** the `aspect-ratio:1/1` set on the `<img>` inside `<picture>` was ignored → hero photo rendered as a tall, super-zoomed portrait crop. Fixed by moving `aspect-ratio:1/1` + `overflow:hidden` to the **`.hero-portrait` figure** (block element) and making `picture`/`img` fill it 100%×100% with `object-fit:cover`. Verified via Chrome headless screenshot of the live URL. Added 3 concept campaigns (each deployed to its own Vercel project, all public 200): Byredo `landingbyredo.vercel.app` (fragrance · "Known by Name"), Huda Beauty `landinghuda-beauty.vercel.app` (makeup · "360° Launch"), Schwarzkopf/Henkel `landingschwarzkopf.vercel.app` ("Shelf to Story"). Concept row now: Revolut, Colgate, Lipton, Byredo, Huda Beauty, Schwarzkopf. CSS v4→v5 |
