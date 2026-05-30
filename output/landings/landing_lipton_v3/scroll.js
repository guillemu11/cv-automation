(function () {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const isMobile = () => window.matchMedia('(max-width: 860px)').matches;

  // --- reveal on scroll for intro, manifesto, executions, kpis ------------
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

  // --- HORIZONTAL SCROLL HIJACK ------------------------------------------
  // The .journey section is 300vh tall and contains a sticky inner with a
  // horizontal track (300vw). Vertical scroll progress within the journey
  // section maps to translateX of the track. Each panel is 100vw wide, so
  // progress 0 = panel 0, progress 0.5 = panel 1, progress 1 = panel 2.
  //
  // On mobile (≤860px) or reduced-motion, CSS falls back to a vertical stack
  // and we skip the hijack logic.

  const journey = document.querySelector('[data-journey]');
  if (!journey) return;

  const track = journey.querySelector('[data-journey-track]');
  const panels = Array.from(journey.querySelectorAll('.city-panel'));
  const dots = Array.from(journey.querySelectorAll('[data-dot]'));
  const railLabel = journey.querySelector('.journey-rail-label');

  if (!track || panels.length === 0) return;

  let currentActive = -1;

  function setActivePanel(idx) {
    if (idx === currentActive) return;
    currentActive = idx;
    panels.forEach((p, i) => p.classList.toggle('is-active', i === idx));
    dots.forEach((d, i) => d.classList.toggle('is-active', i === idx));
    if (railLabel) {
      railLabel.textContent = `${idx + 1} / ${panels.length} bottlers shown of 17`;
    }
  }

  function updateJourney() {
    if (isMobile() || reduceMotion) {
      track.style.transform = '';
      panels.forEach((p) => p.classList.add('is-active'));
      return;
    }

    const rect = journey.getBoundingClientRect();
    const scrollable = rect.height - window.innerHeight;
    if (scrollable <= 0) return;

    const progress = Math.max(0, Math.min(1, -rect.top / scrollable));
    const maxTranslate = (panels.length - 1) * window.innerWidth;
    const tx = -progress * maxTranslate;
    track.style.transform = `translate3d(${tx}px, 0, 0)`;

    // Determine which panel is "centered" in the viewport.
    // Each panel occupies 1/(n-1) of the progress range for the MAIN position,
    // with equal transition bands between. Simple mapping:
    //   progress ∈ [0,       1/(2*(n-1))]        → panel 0
    //   progress ∈ [1/(2*(n-1)), 3/(2*(n-1))]    → panel 1
    //   ...
    const stepsN = panels.length;
    const slotCenter = 1 / (stepsN - 1);
    let idx = Math.round(progress / slotCenter);
    idx = Math.max(0, Math.min(stepsN - 1, idx));
    setActivePanel(idx);
  }

  let ticking = false;
  function requestUpdate() {
    if (!ticking) {
      requestAnimationFrame(() => { updateJourney(); ticking = false; });
      ticking = true;
    }
  }
  window.addEventListener('scroll', requestUpdate, { passive: true });
  window.addEventListener('resize', requestUpdate);

  // On mobile, activate all panels so the copy is visible on the vertical
  // stacked fallback. On desktop, just run the normal update.
  if (isMobile() || reduceMotion) {
    panels.forEach((p) => p.classList.add('is-active'));
  } else {
    setActivePanel(0);
    updateJourney();
  }
})();
