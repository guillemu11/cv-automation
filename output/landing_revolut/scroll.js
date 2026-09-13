// No Borders — Revolut campaign landing
// - reveal-on-scroll via IntersectionObserver
// - count-up for [data-count] figures (insight stat + KPIs)
// Respects prefers-reduced-motion.

(function () {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---- count-up helper ----
  function formatValue(value, decimals, prefix, suffix) {
    const n = decimals > 0 ? value.toFixed(decimals) : Math.round(value).toString();
    return `${prefix}${n}${suffix}`;
  }

  function animateCount(el) {
    const target = parseFloat(el.dataset.count);
    const decimals = parseInt(el.dataset.decimals || '0', 10);
    const prefix = el.dataset.prefix || '';
    const suffix = el.dataset.suffix || '';
    if (isNaN(target)) return;

    if (reduceMotion) {
      el.textContent = formatValue(target, decimals, prefix, suffix);
      return;
    }

    const duration = 1400;
    const start = performance.now();
    const easeOut = (t) => 1 - Math.pow(1 - t, 3);

    function tick(now) {
      const p = Math.min(1, (now - start) / duration);
      el.textContent = formatValue(target * easeOut(p), decimals, prefix, suffix);
      if (p < 1) requestAnimationFrame(tick);
      else el.textContent = formatValue(target, decimals, prefix, suffix);
    }
    requestAnimationFrame(tick);
  }

  // ---- reveal on scroll (and trigger counters within a revealed block) ----
  const reveals = document.querySelectorAll('[data-reveal]');
  const counters = document.querySelectorAll('[data-count]');
  const countedFor = new WeakSet();

  function runCountersIn(root) {
    (root.querySelectorAll ? root.querySelectorAll('[data-count]') : []).forEach((c) => {
      if (!countedFor.has(c)) { countedFor.add(c); animateCount(c); }
    });
  }

  if ('IntersectionObserver' in window && !reduceMotion) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          runCountersIn(e.target);
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });
    reveals.forEach((el) => io.observe(el));

    // counters that sit outside any [data-reveal] block
    const soloIo = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting && !countedFor.has(e.target)) {
          countedFor.add(e.target);
          animateCount(e.target);
          soloIo.unobserve(e.target);
        }
      });
    }, { threshold: 0.5 });
    counters.forEach((c) => { if (!c.closest('[data-reveal]')) soloIo.observe(c); });
  } else {
    reveals.forEach((el) => el.classList.add('is-visible'));
    counters.forEach((c) => animateCount(c));
  }
})();
