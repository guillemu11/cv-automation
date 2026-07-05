(function () {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // --- reveal on scroll (for sections AFTER the stage) ---------------------
  const reveals = document.querySelectorAll('[data-reveal]');
  if (reveals.length && 'IntersectionObserver' in window && !reduceMotion) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add('is-visible'));
  }

  // --- Scroll stage: sticky frame sequence + orchestrated chapters ---------
  const stage = document.querySelector('[data-scrollstage]');
  if (!stage || reduceMotion) return;

  const frameCount = parseInt(stage.dataset.frameCount || '150', 10);
  const frameDir = stage.dataset.frameDir || 'assets/frames';
  const frameExt = stage.dataset.frameExt || 'jpg';
  const display = stage.querySelector('.hero-frame');
  const chapters = Array.from(stage.querySelectorAll('[data-chapter]'));
  const progressEl = stage.querySelector('[data-frame-progress]');

  if (!display) return;

  // Preload every frame before enabling scroll binding.
  const urls = Array.from({ length: frameCount }, (_, i) =>
    `${frameDir}/frame_${String(i + 1).padStart(4, '0')}.${frameExt}`
  );
  const preloaded = new Array(frameCount);
  let loaded = 0;

  urls.forEach((src, i) => {
    const img = new Image();
    img.onload = img.onerror = () => {
      loaded++;
      if (progressEl) {
        progressEl.textContent = `Loading ${Math.round((loaded / frameCount) * 100)}%`;
      }
      if (loaded === frameCount && progressEl) {
        progressEl.classList.add('is-done');
      }
    };
    img.src = src;
    preloaded[i] = img;
  });
  display.src = urls[0];

  // Smoothstep easing so chapters don't pop in linearly.
  function smoothstep(t) {
    t = Math.max(0, Math.min(1, t));
    return t * t * (3 - 2 * t);
  }

  const FADE_WINDOW = 0.05; // ±5% progress for chapter fade in/out

  function updateStage() {
    const rect = stage.getBoundingClientRect();
    const total = rect.height - window.innerHeight;
    const progress = total > 0
      ? Math.max(0, Math.min(1, -rect.top / total))
      : 0;

    // Frame index binding
    const idx = Math.min(frameCount - 1, Math.floor(progress * frameCount));
    const target = preloaded[idx];
    if (target && target.complete && target.naturalWidth > 0) {
      if (display.src !== target.src) display.src = target.src;
    }

    // Chapter orchestration
    for (const ch of chapters) {
      const start = parseFloat(ch.dataset.chapterStart);
      const end = parseFloat(ch.dataset.chapterEnd);

      let opacity = 0;
      let ty = 60; // translateY in px while hidden

      if (progress < start - FADE_WINDOW) {
        opacity = 0;
        ty = 60;
      } else if (progress < start) {
        const t = smoothstep((progress - (start - FADE_WINDOW)) / FADE_WINDOW);
        opacity = t;
        ty = 60 * (1 - t);
      } else if (progress <= end) {
        opacity = 1;
        ty = 0;
      } else if (progress < end + FADE_WINDOW) {
        const t = smoothstep((progress - end) / FADE_WINDOW);
        opacity = 1 - t;
        ty = -60 * t;
      } else {
        opacity = 0;
        ty = -60;
      }

      ch.style.opacity = String(opacity);
      ch.style.transform = `translate3d(0, ${ty.toFixed(1)}px, 0)`;
      ch.style.pointerEvents = opacity > 0.5 ? 'auto' : 'none';
    }
  }

  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => { updateStage(); ticking = false; });
      ticking = true;
    }
  }, { passive: true });
  window.addEventListener('resize', updateStage, { passive: true });
  updateStage();
})();
