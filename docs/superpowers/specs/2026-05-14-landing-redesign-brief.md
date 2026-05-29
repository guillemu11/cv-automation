# Landing-page deliverable — Design Brief

> Companion to `.impeccable.md` → section "Landings (external deliverables)".
> This brief makes block-by-block decisions concrete so implementation needs
> zero design judgment. If the implementer feels they need to "decide" some-
> thing, the brief is incomplete — escalate, don't improvise.

---

## 1. Feature Summary

Two cold-outreach landings, one per target: **Azadea** (Dubai multibrand
fashion retailer) and **Gloria Jeans** (Russian retailer launching MENA).
Both produced by the same generator, both follow the same 8-block structure,
both render to `output/<Company_Role>/landing/index.html` as a self-contained
HTML+CSS+JS bundle that gets attached to an outreach email. The landing is
the candidate's **taste sample** — substance lives in the CV; the landing's
job is to make a hiring manager say *"who made this, let's talk."*

## 2. Primary User Action

A first-time reader, three seconds in, should keep scrolling. That's the
single user action — keep going. Everything else (reading the manifesto,
absorbing the stats, hitting the closing CTA) follows from that one win.

The CTA at the end is *secondary*. If the scroll-through happens, the CTA
converts on its own; if it doesn't, no CTA copy will save it.

## 3. Design Direction

**Editorial fashion-magazine, restrained.** AnOther Magazine for the
asymmetric layouts and whitespace discipline; SSENSE for the photographic
rhythm and tight captions; one Off-White-style typographic moment in the
pull-quote block to hand the page a personality signature. Light surface
throughout except one inverted closing.

Italiana (display) + Geist (body) is locked. OKLCH palette is locked
(ink / paper / paper-deep / burnt sienna accent / muted). No gradients,
no border-left accents, no centered hero/subtitle, no gradient text.

The mood is *editorial*, not *consultancy*. If a block could appear in a
McKinsey deck, it's wrong. If it could appear in an AnOther feature on
"the future of MENA retail," it's right.

## 4. Layout Strategy

A single 12-column grid governs every block. The grid is a CONTRACT for
asymmetry, not for tidy 6-6 splits. Within that grid:

- Hero, pull-quote, full-bleed image, stats, and closing all break the grid
  in different ways (overlay, single-cell, full-bleed, three-rows-one-column,
  inverted-surface respectively).
- Diptych, manifesto, and triptych use the grid but in asymmetric splits —
  never 6/6, never centered.
- Spacing rhythm is **wide-wide-narrow-wide-narrow-wide-wide-narrow** vertical
  beats across the 8 blocks. Wide blocks get `clamp(96px, 12vw, 192px)` top
  and bottom; narrow get half that. This rhythm is what stops the page
  feeling like a list.

The reader moves down through alternating densities: heavy image → quiet
type → paired image → text island → loud image → image grid → numeric
intervention → inverted statement. Every block is a different shape from
the one before and the one after.

## 5. The 8 Blocks (the heart of this brief)

### Block 1 — Hero

**Responsibility:** make the reader want to scroll. That's all. No promises,
no claims, no scroll-hint clutter.

**Content budget:**
- 1 full-bleed image (21:9, ~100vh on desktop, ~80vh on mobile)
- 1 headline, 4-8 words, broken across 2 lines
- 1 supporting line, max 12 words
- 1 author tag (name + role + city), small, bottom-right or bottom-left

**Layout in plain words:** photograph fills the whole viewport. Headline sits
in the bottom-left third over the photo, never centered. The supporting line
sits directly under the headline with a thin rule between. Author tag is
diagonally opposite (bottom-right) in small tracked uppercase. **No top nav,
no scroll arrow, no logo.** The page introduces itself only by the photograph.

**Reference to look at:** the cover spread of any AnOther Magazine print
issue (e.g. A/W 2023 cover). Or SSENSE editorials homepage hero:
https://www.ssense.com/en-us/editorial

### Block 2 — Pull-quote

**Responsibility:** the page's personality signature. One sentence that the
reader will quote back to themselves while closing the tab.

**Content budget:**
- 1 sentence, **strictly max 14 words**
- 1 attribution line in tiny tracked uppercase ("— a thesis", "— a working
  principle", etc.) — Off-White typographic register

**Layout in plain words:** paper surface, no photo. The sentence sits on
columns 3-10 of the 12-col grid (asymmetric, slightly left-of-center).
Italiana italic at very large size. Vertical padding generous — block height
should feel like half a viewport on desktop, the page should *breathe* here.
Attribution sits below-right of the quote, small.

**Reference to look at:** any Off-White Spring/Summer campaign typography
spread, particularly the "FOR DISPLAY PURPOSES ONLY" lockup style. Or the
opening spread of a Gentlewoman magazine feature.

### Block 3 — Diptych

**Responsibility:** establish visual range. Two photos that argue with each
other or complement each other — never two of the same kind.

**Content budget:**
- 2 photographs (one 4:5 vertical, one 3:4 horizontal — visibly different
  aspect ratios)
- 1 single caption, max 5 words, set between them in tiny tracked uppercase

**Layout in plain words:** the two images sit side by side on columns 1-6 and
7-12, but **with different vertical sizes** — the vertical image is full
column height, the horizontal one is shorter and sits aligned to the top,
leaving deliberate dead space below it. The caption sits in that dead
space, tiny, left-aligned to the horizontal image.

**Reference to look at:** any inside spread of AnOther Magazine where two
images are paired across a fold — they're almost never the same size.

### Block 4 — Manifesto

**Responsibility:** the only block where the candidate gets to make an
argument with prose. One paragraph, no more.

**Content budget:**
- 1 paragraph, max 50 words
- 1 portrait-orientation photograph (3:4)
- Optional: 1 tracked-uppercase eyebrow above the paragraph ("a thesis",
  "what we'd build", etc.)

**Layout in plain words:** 12-col grid split 5/3/4 — text on columns 1-5,
intentional empty gutter on columns 6-8, photo on columns 9-12. The empty
gutter is the design move; it's what differentiates this from a generic
"text-left, image-right" pattern. Text top-aligned with the photo. Paragraph
set at 56ch max (will wrap inside its 5-col band).

**Reference to look at:** a Highsnobiety long-read article structure on
desktop, where text columns and images are separated by deliberate dead space.

### Block 5 — Full-bleed image

**Responsibility:** respiration. The page stops talking for a moment.

**Content budget:**
- 1 photograph, 21:9 or 16:9, full viewport width
- ZERO text. No caption. No overlay. No nothing.

**Layout in plain words:** image edge-to-edge of the viewport. Vertical
height matches the image's natural ratio (~50-60vh). No padding, no margin,
no chrome. The block is a single horizontal band of pure photograph between
two other blocks.

**Reference to look at:** Apple product page "image break" sections, or the
full-page non-text spreads inside an AnOther feature.

### Block 6 — Triptych

**Responsibility:** show breadth. Three images that together cover more
ground than one could.

**Content budget:**
- 3 photographs (all 4:5 vertical, same aspect for grid coherence)
- 3 captions, each max 3 words, each underneath its image

**Layout in plain words:** three columns of equal width, columns 1-4, 5-8,
9-12. Each image is 4:5 vertical. Captions immediately below each image,
left-aligned, tiny tracked uppercase. The captions read as a triptych in
themselves — three short phrases that hint at three different facets.

**Reference to look at:** a Net-A-Porter editorial "shop the story" 3-up
grid, but with the product chrome removed.

### Block 7 — Stats

**Responsibility:** the candidate's numeric track record, said once and well.

**Content budget:**
- Exactly 3 stats
- Each: 1 number (large, accent color) + 1 label (small, tracked uppercase)
- Optional: each stat gets 1 sub-label of max 5 words

**Layout in plain words:** three rows, one stat per row. Each row spans
columns 2-11. Number is left-aligned in Italiana display weight at a very
large size; label sits below the number, tiny, in tracked uppercase. Sub-
label, if present, sits one line below the label. **No box, no card, no
border.** Just three numbers stacked vertically with generous vertical space
between them. The accent color appears here for the first and only time in
the body of the page.

**Reference to look at:** Stripe Press book product pages
(https://press.stripe.com) — the way they handle simple numeric facts with
zero decoration.

### Block 8 — Closing

**Responsibility:** make the meeting easy to say yes to.

**Content budget:**
- 1 short paragraph, max 25 words
- 1 CTA line ("30 minutes, by phone or coffee.")
- 1 contact strip (email · phone · linkedin)

**Layout in plain words:** **inverted block** — ink background, paper text.
Single column, content sits on columns 3-10 of the 12-col grid (slightly
narrower than the body to feel "set apart"). Closing paragraph in Geist
body weight, lede size. CTA line directly below in Italiana italic, slightly
larger. Contact strip below the CTA in tiny tracked uppercase, dots between
fields, accent color on hover only. No button. The CTA is text.

**Reference to look at:** the closing colophon of a printed art catalogue —
small, dense, set on dark paper, no decoration.

## 6. Key States

- **Default (rendered with all 8 images present):** all blocks render as designed.
- **Partial-image (some `secN.png` missing):** the missing image's block
  gracefully degrades — a textured paper-deep surface fills the image slot
  with the caption sitting under it. The hero block degrades by losing the
  full-bleed background and falling back to the paper surface with the
  headline shifted up and the typography taking over the role the photo had.
- **No images at all (Higgsfield unavailable):** generator should still
  produce a valid landing. Every image block falls back to the paper-deep
  surface. The landing reads as a pure-typographic editorial, which is also
  a legitimate AnOther aesthetic.
- **Mobile (<768px viewport):** asymmetric splits collapse to single column
  with explicit ordering. Pull-quote and stats lose nothing. Triptych
  stacks vertically. Manifesto: photo above paragraph. Hero: photo with
  headline overlaid bottom-left, smaller scale.
- **`prefers-reduced-motion: reduce`:** all reveal animations disabled,
  content appears with `opacity:1, transform:none`.

## 7. Interaction Model

This is a **read-only artifact**. There are no forms, no menus, no buttons
that change state. The only interactions are:

- **Scroll** — drives all reveals via IntersectionObserver. Each block
  fades in once, in place, and stays.
- **Hover on links** — only on the contact strip (mailto:, tel:, linkedin
  URL). Color shift to accent on hover, 200ms ease. Underline appears on
  hover too, replacing the default no-underline state.
- **Hover on images** — none. Images do not respond to cursor.
- **Click anywhere else** — does nothing. There are no clickable areas
  outside the contact strip.

This is intentional. A read-only artifact respects the reader's time.

## 8. Content Requirements (per landing)

Each landing's content is produced by Claude through a tool_use schema. The
schema must enforce the budget constraints in section 5. Suggested field
shape:

```
hero:        headline (4-8 words, will be split into 2 lines by render)
             support  (max 12 words)
quote:       text       (max 14 words)
             attribution (Off-White-style short label, max 4 words)
diptych:     caption (max 5 words)
manifesto:   eyebrow   (max 3 words, optional)
             paragraph (max 50 words)
triptych:    captions × 3 (each max 3 words)
stats:       items × 3
               number (number, formatted by render with K/M suffixes)
               label  (max 5 words)
               sublabel (max 5 words, optional)
closing:     paragraph (max 25 words)
             cta_line  (max 10 words)
```

**Image labels** are no longer in the content — image placement is
positional (block 1 = hero, block 3 image 1 = `dip1`, block 3 image 2 =
`dip2`, block 5 = `bleed`, block 6 images = `tri1/tri2/tri3`, block 4 = `man`).
That's **8 images per landing**: `hero`, `dip1`, `dip2`, `man`, `bleed`,
`tri1`, `tri2`, `tri3`. The Higgsfield prompts are constructed by the
generator using the candidate's positioning angle and the target company.

**Hard constraint:** total word count, summing all text fields, must be
≤ 120. Target 80. Claude's prompt enforces this at tool_use schema level
(maxLength per field). Generator validates after the call and fails loudly
if exceeded.

### Per-landing content seeds (for the implementer)

**Azadea (angle: fashion_commerce_bridge):**
- Hero direction: photography of luxury multibrand retail concourse
- Pull-quote direction: a one-liner about portfolio thinking — *"Fifty brands.
  One season. One conversation."* or similar
- Manifesto direction: from silos to orchestration
- Stats: real metrics from Paula's CV (42 multibrand key accounts, +30% GMV
  QoQ, 50+ countries managed)
- Closing: ask for 30 minutes to walk through a specific portfolio activation
  idea

**Gloria Jeans (angle: inditex_insider, brand-name-suppressed):**
- Hero direction: photography of premium retail floor operations
- Pull-quote direction: a one-liner about operational rhythm — *"Premium
  retail isn't products. It's cadence."* or similar
- Manifesto direction: an operating system for MENA premium retail
- Stats: same three real metrics from Paula's CV, framed for retail-ops fit
- Closing: ask for 30 minutes to walk through a first-quarter roadmap
- **Strict rule:** the words "Inditex" and "Massimo Dutti" must not appear
  in the rendered HTML. The implementer must verify with a `grep -i` test.

## 9. What to Keep from the Existing Template

Very little:

- **`IntersectionObserver` reveal logic** in `scroll.js` — keep as-is, it's
  the right primitive and has good `prefers-reduced-motion` handling
- **HTML-escape via `html.escape`** in `_paragraphs_to_html` and the field
  injectors — that pattern is right, preserve it everywhere
- **`job_output_dir(job)` + `landing/` subfolder convention** — the FastAPI
  static mount and the dashboard `_files.landing` key both depend on this
- **The `_DEFAULT_BRAND` dict pattern** in `landing_generator.py`, but with
  new OKLCH values per the .impeccable.md palette
- **Test fixtures** in `tests/test_landing_generator.py` — keep the test
  file shape, rewrite the assertions to match the new block names

## 10. What to Throw Away

Everything else:

- The current `HTML_TEMPLATE`, `SECTION_TEMPLATE`, `CSS_TEMPLATE`, `JS_TEMPLATE`
  string constants — all replaced
- The 6-section iterator — replaced by 8 named block renderers
- The `figure-placeholder` gradient — replaced by paper-deep surface fallback
- The 1.6vw `clamp` body sizing — replaced by Italiana/Geist scale
- The `accent: #C8A876` champagne gold — replaced by burnt-sienna OKLCH
- The hero radial-gradient background — replaced by full-bleed photo
- The `submit_landing_content` tool_use schema in `landing_generator.py` —
  replaced by the new schema in section 8
- The `_SYSTEM` prompt — rewritten to enforce the 80-word brutalist budget
- The HTML escape edge cases around `<` and `>` are correct but the function
  surface needs to extend to new fields (`stats.number` should NOT be
  escaped if it includes decimal points; everything else escapes)

## 11. Recommended References

For the implementer (read these before coding):

- **`reference/spatial-design.md`** — for the 12-col asymmetric grid and the
  vertical rhythm of the 8 blocks
- **`reference/typography.md`** — for the Italiana/Geist scale calibration
  and the OpenType features available on each
- **`reference/motion-design.md`** — for the IntersectionObserver reveal
  timing and the `prefers-reduced-motion` handling
- **`reference/color-and-contrast.md`** — for verifying the OKLCH burnt-
  sienna passes WCAG AA against the paper and ink surfaces

External references (look at while building):
- SSENSE editorial section: https://www.ssense.com/en-us/editorial
- AnOther Magazine "fashion" section: https://www.anothermag.com/fashion
- Stripe Press book pages: https://press.stripe.com
- Off-White SS spreads on archive.org or runway photography aggregators

## 12. Open Questions for the Implementer

- **Image fallback aesthetic when only `paper-deep` shows:** does it just
  hold the space, or does it get a tiny center-bottom caption explaining
  what would've been there? My recommendation: just hold the space. Empty
  paper IS the editorial fallback. Captions on empty surfaces feel like
  apologies.
- **Should the page have a `<title>` for browser tabs that mentions both
  Paula and the target company?** Yes — `"For {Company} — {Paula's Name}"`.
- **Should the landing emit OpenGraph tags?** Skip. The landing is sent as
  a direct link in private email; it does not need to be socially shareable.
  Adding OG tags is YAGNI here.
- **Per-landing image generation cost:** 8 images × Soul Cinematic 2k at
  0.12 credits each = 0.96 credits per landing. Two landings = 1.92 credits.
  Acceptable given the 1199-credit budget. The generator should NOT
  auto-regenerate images on every Claude call — image generation is
  expensive enough that a "regenerate landing copy" should reuse existing
  images by default, with an explicit flag to also regenerate visuals.
