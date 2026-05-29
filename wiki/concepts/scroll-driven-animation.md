---
type: concept
domain: ai
tags: [scroll-animation, frontend, css, ffmpeg, landing-page]
status: active
created: 2026-04-11
updated: 2026-04-11
sources: ["[[jack-roberts-claude-nano-banana-websites]]", "[[nate-herk-nano-banana-2-websites]]", "[[nick-saraev-claude-kling-animated-sites]]", "[[jack-roberts-firecrawl-intelligence-websites]]"]
---

# Scroll-Driven Animation

The core "wow factor" trick behind premium-feeling AI-generated landing pages: a sequence of frames tied to scroll position, so the user controls playback by scrolling. As they scroll down, the product rotates, explodes, or reveals its internals. As they scroll up, it reverses. This is NOT a playing video — it's an image sequence animated by scroll.

## The canonical pipeline

1. **Generate two keyframes** (start + end) — see [[Nano Banana Keyframe Workflow]]. These define what the animation "means": assembled→exploded, closed→open, blueprint→finished, etc.
2. **Animate between them** with an image-to-video model (Kling 3.0, Seedance 2.0). Output is a 7-10 second clip.
3. **Extract frames** from the clip with ffmpeg — typically ~120 `.webp` frames. Each frame is tiny (~5-20kb) and together they form a stop-motion-style sequence.
4. **Tie each frame to a scroll position** in JavaScript. As the user scrolls, the active frame changes. The simplest implementation swaps `<img src>` based on `window.scrollY` normalized to the animation's scroll range.

[[nate-herk-nano-banana-2-websites]] notes this is why the "frames" folder is critical — **if frames aren't deployed to GitHub, the animation silently disappears** because the site has nothing to render. Make sure `.gitignore` doesn't exclude image sequences.

## Two DOM-level patterns

Both sources mention two UI patterns for scroll-driven animation:

- **Pinned hero**: the animation container has `position: sticky` while scrolling through its range, and the frame index increments. Classic Apple product-page feel.
- **Full-page unfurl**: background stays mostly static, but a central element (camera, watch, blender) rotates/opens as the user scrolls. Allows copy to layer over the animation.

Paula's campaign-landing skill should prefer **pinned hero** for maximum impact on the first viewport, then transition into normal scrolling for the rest of the page.

## Why not use native CSS `animation-timeline: scroll()`?

CSS Scroll-Driven Animations (2024+ spec) let you do this with pure CSS: `animation-timeline: scroll()` + `@keyframes`. No JS required. BUT:

- Browser support is still partial (Chrome/Edge yes, Safari/Firefox limited as of Q1 2026). For a deliverable Paula is sending to recruiters, inconsistent rendering on Safari is unacceptable.
- The two source videos both use the JS-based frame-sequence approach, which works everywhere.

**Default for the skill**: JS frame-sequence with ~100-140 frames. Fallback to CSS if the landing is static enough that a keyframe animation is cleaner.

## Performance notes

- Preload all frames before the animation enters the viewport (otherwise the first scroll is janky).
- Use `.webp` at ~70-80% quality. `.jpg` is fine but heavier. Never `.png` for sequences.
- Lazy-decode with `<img decoding="async" loading="eager">` on the set that's about to be used.
- If the total frame folder exceeds ~3-4 MB, reduce to 80 frames — diminishing returns beyond that.

## Minimum viable JS

```js
const frames = Array.from({length: 120}, (_, i) =>
  `assets/frame_${String(i).padStart(4, '0')}.webp`
);
const imgs = frames.map(src => { const i = new Image(); i.src = src; return i; });

const container = document.querySelector('.hero-animation');
const display = container.querySelector('img');

window.addEventListener('scroll', () => {
  const rect = container.getBoundingClientRect();
  const progress = Math.max(0, Math.min(1,
    -rect.top / (rect.height - window.innerHeight)
  ));
  const idx = Math.floor(progress * (frames.length - 1));
  display.src = imgs[idx].src;
});
```

## Locomotive-scroll as the smoothness layer

[[nick-saraev-claude-kling-animated-sites]] surfaces that when Claude Code builds these animations unprompted, it tends to pull in **locomotive-scroll** (the popular JS library for smooth scroll-hijacking). This is what makes the frame-progression feel buttery instead of the stuttering native-scroll experience. If the skill's output isn't using locomotive-scroll, add it explicitly — either via CDN script tag or npm (but the skill's no-build philosophy favors CDN).

```html
<link href="https://cdn.jsdelivr.net/npm/locomotive-scroll@4/dist/locomotive-scroll.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/locomotive-scroll@4/dist/locomotive-scroll.min.js"></script>
```

Then initialize with `data-scroll-container` on the root and the library handles the rest.

## The "make it faster" iterative optimization loop

Nick's most actionable pattern: after the first build, the scroll-driven animation will feel laggy. Instead of optimizing by hand, just say **"make it faster"** to Claude. It will:

1. Extract video frames as optimized JPEGs (ffmpeg with quality controls).
2. Tie each image file to a scroll position (replacing the `<video>` playback approach).
3. Add frame preloading (`<link rel="preload">` for the first 30-40 frames, lazy for the rest).
4. Compress the hero/poster image aggressively (Nick's went from 5.3 MB → 252 KB in one prompt).

Run this **3-4 times in sequence**, each time checking whether quality regressed. Stop when quality stops degrading or speed stops improving. This is cheaper than a-priori optimization because Claude can assess both sides — unlike a human, it'll revert overcompression automatically if asked.

## Reference image → scroll animation bridge

[[jack-roberts-firecrawl-intelligence-websites]] (the pool-cleaning example) shows a clean 3-step pipeline for scroll-driven "before/after" style animations: dirty pool keyframe → clean pool keyframe (with the dirty pool used as Higgsfield reference for composition consistency) → Kling 3.0 video transition → ffmpeg frame extraction → scroll binding. The reference-image step is critical — without it, the two keyframes drift in composition and the scroll animation looks wrong. See [[Nano Banana Keyframe Workflow]] for the reference-image details.

## Plan-mode discipline

[[jack-roberts-claude-nano-banana-websites]] recommends building this in plan mode with "edit automatically" (not "ask before edits"). [[nate-herk-nano-banana-2-websites]] flips to bypass-permissions after plan approval. Either way: plan first, then let it run uninterrupted. Scroll animation code has too many small files to babysit every edit.

## Related concepts

- [[Nano Banana Keyframe Workflow]] — upstream: where the two keyframes come from.
- [[Seedance Loop Video Hero]] — alternate pattern (autoplay loop instead of scroll-driven).
- [[Frontend Design Skill Pattern]] — the meta-skill that knows when to use scroll-driven vs loop.
