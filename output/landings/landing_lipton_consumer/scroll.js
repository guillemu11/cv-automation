(function () {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // --- reveal on scroll ----------------------------------------------------
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

  // --- counter animation ---------------------------------------------------
  const counters = document.querySelectorAll('[data-counter]');
  const counterObserved = new WeakSet();
  function animateCounter(el) {
    if (counterObserved.has(el)) return;
    counterObserved.add(el);
    const to = parseInt(el.dataset.counterTo || '0', 10);
    const duration = 1400;
    const start = performance.now();
    const startVal = 0;
    function step(now) {
      const t = Math.min(1, (now - start) / duration);
      const eased = 1 - Math.pow(1 - t, 3);
      const val = Math.floor(startVal + (to - startVal) * eased);
      el.textContent = val.toLocaleString();
      if (t < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  // --- sticky CTA bar: hide when form is on screen ------------------------
  const stickyCta = document.querySelector('[data-sticky-cta]');
  const claimSection = document.getElementById('claim');
  if (stickyCta && claimSection && 'IntersectionObserver' in window) {
    const claimIo = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        stickyCta.classList.toggle('is-hidden', e.isIntersecting);
      });
    }, { threshold: 0.3 });
    claimIo.observe(claimSection);
  }

  // --- form client-side handling ------------------------------------------
  const form = document.querySelector('[data-claim-form]');
  const success = document.querySelector('[data-claim-success]');
  if (form && success) {
    form.addEventListener('submit', (e) => {
      // Let the mailto action proceed but also show success state.
      setTimeout(() => {
        form.hidden = true;
        success.hidden = false;
        success.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }, 100);
    });
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

  function smoothstep(t) {
    t = Math.max(0, Math.min(1, t));
    return t * t * (3 - 2 * t);
  }

  const FADE_WINDOW = 0.05;

  function updateStage() {
    const rect = stage.getBoundingClientRect();
    const total = rect.height - window.innerHeight;
    const progress = total > 0
      ? Math.max(0, Math.min(1, -rect.top / total))
      : 0;

    const idx = Math.min(frameCount - 1, Math.floor(progress * frameCount));
    const target = preloaded[idx];
    if (target && target.complete && target.naturalWidth > 0) {
      if (display.src !== target.src) display.src = target.src;
    }

    for (const ch of chapters) {
      const start = parseFloat(ch.dataset.chapterStart);
      const end = parseFloat(ch.dataset.chapterEnd);

      let opacity = 0;
      let ty = 60;

      if (progress < start - FADE_WINDOW) {
        opacity = 0; ty = 60;
      } else if (progress < start) {
        const t = smoothstep((progress - (start - FADE_WINDOW)) / FADE_WINDOW);
        opacity = t; ty = 60 * (1 - t);
      } else if (progress <= end) {
        opacity = 1; ty = 0;
        // trigger counter animations when a chapter fully enters
        const counter = ch.querySelector('[data-counter]');
        if (counter) animateCounter(counter);
      } else if (progress < end + FADE_WINDOW) {
        const t = smoothstep((progress - end) / FADE_WINDOW);
        opacity = 1 - t; ty = -60 * t;
      } else {
        opacity = 0; ty = -60;
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
