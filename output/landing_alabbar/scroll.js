// House Rules — Alabbar Enterprises & ANOTHER
// (1) reveal-on-scroll  (2) nav turns solid once the hero is scrolled past.
(function () {
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // --- reveal on scroll ---
  var reveals = document.querySelectorAll('[data-reveal]');
  if (reveals.length && 'IntersectionObserver' in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-visible'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-visible'); });
  }

  // --- adaptive nav ---
  var nav = document.querySelector('[data-nav]');
  var hero = document.querySelector('[data-hero]');
  if (nav && hero) {
    var ticking = false;
    var onScroll = function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        var threshold = hero.offsetHeight - 72;
        nav.classList.toggle('is-solid', window.scrollY > threshold);
        ticking = false;
      });
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }
})();
