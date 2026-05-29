// campaign-landing scroll behaviors
// - reveal-on-scroll via IntersectionObserver
// - optional frame-sequence hero (Archetype A) if a [data-frame-sequence] hero is present

(function () {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // --- reveal on scroll ---
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

  // --- archetype A: frame-sequence hero ---
  const frameHero = document.querySelector('[data-frame-sequence]');
  if (frameHero && !reduceMotion) {
    const FRAME_COUNT = parseInt(frameHero.dataset.frameCount || '120', 10);
    const FRAME_DIR = frameHero.dataset.frameDir || 'assets/frames';
    const EXT = frameHero.dataset.frameExt || 'webp';
    const display = frameHero.querySelector('.hero-frame');
    if (display) {
      const urls = Array.from({ length: FRAME_COUNT }, (_, i) =>
        `${FRAME_DIR}/frame_${String(i).padStart(4, '0')}.${EXT}`
      );
      const preloaded = urls.map((src) => { const img = new Image(); img.src = src; return img; });

      let ticking = false;
      const update = () => {
        const rect = frameHero.getBoundingClientRect();
        const total = rect.height - window.innerHeight;
        const progress = Math.max(0, Math.min(1, -rect.top / total));
        const idx = Math.floor(progress * (FRAME_COUNT - 1));
        display.src = preloaded[idx].src;
        ticking = false;
      };
      window.addEventListener('scroll', () => {
        if (!ticking) { requestAnimationFrame(update); ticking = true; }
      }, { passive: true });
      update();
    }
  }
})();