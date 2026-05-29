---
type: concept
domain: ai
tags: [seedance, hero-video, loop, autoplay, landing-page]
status: active
created: 2026-04-11
updated: 2026-04-11
sources: ["[[nate-herk-seedance-2-websites]]"]
---

# Seedance Loop Video Hero

Alternate hero pattern to [[Scroll-Driven Animation]]: a short (10 second) video plays on autoplay, muted, looping forever in the hero section of a landing page. The user does not control playback — they just see an atmospheric motion-rich background while they read the copy on top of it.

## When to use this vs. scroll-driven

| Goal | Pattern |
|------|---------|
| Show a product coming apart / assembling | [[Scroll-Driven Animation]] |
| Show an atmosphere / mood / setting | **Seedance Loop Video Hero** |
| Reveal features one by one as user scrolls | [[Scroll-Driven Animation]] |
| Luxury feel, desert drive, architecture firm, travel brand | **Seedance Loop Video Hero** |
| Product walkthrough with text over each state | [[Scroll-Driven Animation]] |

For Paula's "campaign for the target company" deliverables, loop video hero is the right pick when the campaign is **lifestyle / brand / aspirational** and scroll-driven is the right pick when the campaign centers on a **product or feature**. The skill should ask which category the campaign falls into and route accordingly.

## The seamless loop trick

The entire pattern rests on one non-obvious detail: in [[Seedance 2.0]] (or any image-to-video model with first/last frame inputs), set **first frame = last frame** (upload the same image into both slots). The model generates motion in the middle that returns to the starting state. When the video reaches its end and the `<video loop>` element restarts from frame 0, there's no visible jump — the loop is invisible.

Without this trick, the loop "pops" every N seconds and completely breaks the atmosphere.

## Worked example from the source

[[nate-herk-seedance-2-websites]] built a site for a fictional architecture firm. Hero input image: a blueprint of a skyscraper 75% sketched. Prompt: "the sketch starts being filled in with more lines, then zooms into a real city where the building is under construction, rising to the top until finished, with text 'Turn your ideas into reality' appearing. Then zoom back out and fade back into the original blueprint."

First frame and last frame are both the same blueprint → the loop returns cleanly.

## Settings that matter

- **10 seconds**, not 15. The 10-second version costs less (~410 Kie credits vs 625) AND feels more fast-paced. 15s drags.
- **720p** is enough for a landing page hero on desktop and mobile. 1080p doubles cost for marginal visual gain.
- **Turn OFF audio generation** — the web video plays muted, audio generation is wasted compute.
- **16×9 aspect ratio** — matches the source image generated earlier, avoids letterboxing.
- **Disable reference images** unless you want Seedance to borrow motion from another clip — usually you don't.

## Embedding in HTML

```html
<section class="hero">
  <video autoplay muted loop playsinline>
    <source src="assets/hero-loop.mp4" type="video/mp4">
  </video>
  <div class="hero-copy">
    <h1>Turn your ideas into reality</h1>
  </div>
</section>
```

Key attributes: `autoplay muted loop playsinline`. Mobile Safari refuses to autoplay without `playsinline` AND `muted`.

## Performance considerations

- Encode the output as **H.264 MP4** (not WebM) for Safari compatibility.
- Keep under **5 MB** if possible — a 10s 720p clip should land around 2-4 MB. Bigger than that and mobile users on 4G wait for the animation.
- Add a `poster="assets/hero-first-frame.jpg"` so the first frame is visible immediately while the video loads.
- Consider a low-power mode detection (`prefers-reduced-motion: reduce` media query) to swap the video for a static poster — some users explicitly opt out of motion.

## Related concepts

- [[Scroll-Driven Animation]] — the other hero pattern.
- [[Nano Banana Keyframe Workflow]] — generates the single input image (here, start AND end).
- [[Frontend Design Skill Pattern]] — routes between patterns based on campaign type.
