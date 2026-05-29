# Animation patterns

Derived from `wiki/concepts/scroll-driven-animation.md` and `wiki/concepts/seedance-loop-video-hero.md`. Two animation archetypes the skill routes between.

## Archetype A — Scroll-driven frame sequence (hero)

Best for campaigns where the product or a key visual transforms (assembled → exploded, empty → full, closed → open).

**Assets needed**: 80-120 sequential frames as `.webp` (or `.jpg` if webp unsupported) at 1920×1080, named `frame_0000.webp` ... `frame_0119.webp`, placed in `assets/frames/`.

**HTML hook**:

```html
<section class="hero" data-scroll-animation>
  <img class="hero-frame" src="assets/frames/frame_0000.webp" alt="">
  <div class="hero-copy">
    <h1 class="hero-tagline">{{tagline}}</h1>
  </div>
</section>
```

**JS** (already in `templates/scroll.js`):

```js
const FRAME_COUNT = 120;
const frames = Array.from({length: FRAME_COUNT}, (_, i) =>
  `assets/frames/frame_${String(i).padStart(4, '0')}.webp`
);
const preloaded = frames.map(src => { const img = new Image(); img.src = src; return img; });

const container = document.querySelector('[data-scroll-animation]');
const display = container.querySelector('.hero-frame');

window.addEventListener('scroll', () => {
  const rect = container.getBoundingClientRect();
  const total = rect.height - window.innerHeight;
  const progress = Math.max(0, Math.min(1, -rect.top / total));
  const idx = Math.floor(progress * (FRAME_COUNT - 1));
  display.src = preloaded[idx].src;
}, { passive: true });
```

**Critical**: the section must be tall (e.g. `height: 300vh`) so there's actual scroll distance to map frames to. If the section is only `100vh`, nothing animates.

**`.gitignore` gotcha**: assets must be tracked. Add `!assets/frames/**` to the ignore rules or Vercel deploys with no images.

## Archetype B — Seamless loop video hero

Best for "mood" campaigns without a transformation — beverages, fashion, lifestyle. Cheaper and simpler than frame sequences.

**Asset**: single `.mp4` (H.264), 7-10 seconds, 1920×1080, ≤5 MB. First frame must equal last frame (generate in Seedance 2.0 or Kling by passing the same image as both keyframes).

**HTML**:

```html
<section class="hero hero--video">
  <video autoplay muted loop playsinline preload="auto">
    <source src="assets/hero-loop.mp4" type="video/mp4">
  </video>
  <div class="hero-copy">
    <h1 class="hero-tagline">{{tagline}}</h1>
  </div>
</section>
```

No JS required. `autoplay muted loop playsinline` is mandatory on mobile Safari.

## Choosing between A and B

| Campaign angle | Archetype |
| --- | --- |
| Product transformation (assembled → exploded) | A (frame sequence) |
| Before/after (dirty → clean) | A (frame sequence) |
| Mood/atmosphere (lifestyle, movement) | B (loop video) |
| Abstract/typographic only | B or CSS-only |

Default if the angle is ambiguous: **B** (video loop). Cheaper, faster, less risk of the frames gotcha on deploy.

## Anti-slop rules (taste layer)

Loaded into phase 5 whenever generating HTML:

- **Never** center-align the hero tagline with 3 CTA buttons below. Asymmetric is better — left-aligned tagline with a single primary CTA offset bottom-right.
- **Never** use `linear-gradient(135deg, purple, pink)`. Ever.
- **Never** emoji in UI copy. Never.
- **Never** `border-radius: 9999px` on non-pill elements. Cards get 8-12px max.
- **Never** default shadcn shadows. Use a calibrated 2-layer shadow: `0 1px 2px rgba(0,0,0,.06), 0 8px 24px rgba(0,0,0,.08)`.
- **Max 2 fonts**: one display, one body. Both from Google Fonts or system.
- **Spacing rhythm**: use a 4/8/16/32/64/128 scale. No arbitrary values.
- **Heading scale**: `clamp(2.5rem, 6vw, 6rem)` for hero, `clamp(1.75rem, 3vw, 3rem)` for section headings.
- **Color discipline**: at most 3 brand colors used on the page. Text stays near-black or near-white, not mid-gray slop.
- **No placeholder lorem ipsum** ever reaches the final output. If copy is missing, the skill stops and asks.

## Reduced motion

Respect `prefers-reduced-motion: reduce`. In `styles.css`:

```css
@media (prefers-reduced-motion: reduce) {
  .hero-frame { transition: none; }
  .hero--video video { display: none; }
  .hero--video { background: var(--brand-primary); }
}
```

The scroll-frame JS also checks the media query and skips the scroll listener if reduce is set.
