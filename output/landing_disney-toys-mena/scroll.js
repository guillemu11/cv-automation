// Home of Heroes — scroll behaviours
// - reveal-on-scroll via IntersectionObserver
// - subtle parallax lift on the hero copy
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

  // --- hero parallax ---
  const parallax = document.querySelector('[data-parallax]');
  if (parallax && !reduceMotion) {
    let ticking = false;
    const update = () => {
      const y = window.scrollY;
      if (y < window.innerHeight) {
        parallax.style.transform = `translateY(${y * 0.18}px)`;
        parallax.style.opacity = String(Math.max(0, 1 - y / (window.innerHeight * 0.85)));
      }
      ticking = false;
    };
    window.addEventListener('scroll', () => {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }
})();
