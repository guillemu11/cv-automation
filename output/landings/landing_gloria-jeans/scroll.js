(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ── Reveal on scroll ──────────────────────────────────────────
  var reveals = document.querySelectorAll('[data-reveal]');

  if (reveals.length && 'IntersectionObserver' in window && !reduceMotion) {
    var revealIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          revealIO.unobserve(e.target);

          // Trigger count-up for stat numbers inside this element
          var counters = e.target.querySelectorAll('[data-count]');
          counters.forEach(function (el) { animateCounter(el); });

          // Also check if this element itself is a counter
          if (e.target.hasAttribute('data-count')) {
            animateCounter(e.target);
          }
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

    reveals.forEach(function (el) { revealIO.observe(el); });
  } else {
    // No IO or reduced motion — show everything immediately
    reveals.forEach(function (el) {
      el.classList.add('is-visible');
      var counters = el.querySelectorAll('[data-count]');
      counters.forEach(function (c) {
        c.textContent = c.getAttribute('data-count');
      });
    });
  }

  // ── Counter animation ─────────────────────────────────────────
  function animateCounter(el) {
    if (el.classList.contains('is-counted')) return;
    el.classList.add('is-counted');

    var target = parseFloat(el.getAttribute('data-count'));
    var isDecimal = target % 1 !== 0;
    var duration = 1400; // ms
    var startTime = null;

    function step(timestamp) {
      if (!startTime) startTime = timestamp;
      var progress = Math.min((timestamp - startTime) / duration, 1);
      // Ease out cubic
      var eased = 1 - Math.pow(1 - progress, 3);
      var current = eased * target;

      el.textContent = isDecimal ? current.toFixed(1) : Math.floor(current);

      if (progress < 1) {
        requestAnimationFrame(step);
      } else {
        el.textContent = isDecimal ? target.toFixed(1) : target;
      }
    }

    requestAnimationFrame(step);
  }

  // ── Smooth nav opacity on scroll ──────────────────────────────
  var nav = document.querySelector('.top-nav');
  if (nav) {
    var lastScroll = 0;
    var ticking = false;

    window.addEventListener('scroll', function () {
      lastScroll = window.scrollY;
      if (!ticking) {
        requestAnimationFrame(function () {
          nav.style.opacity = lastScroll > 100 ? '1' : '1';
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }

  // ── Parallax-lite on hero ─────────────────────────────────────
  if (!reduceMotion) {
    var hero = document.querySelector('.hero-inner');
    if (hero) {
      var heroTicking = false;
      window.addEventListener('scroll', function () {
        if (!heroTicking) {
          requestAnimationFrame(function () {
            var scrolled = window.scrollY;
            if (scrolled < window.innerHeight) {
              hero.style.transform = 'translateY(' + (scrolled * 0.15) + 'px)';
              hero.style.opacity = Math.max(0, 1 - scrolled / (window.innerHeight * 0.8));
            }
            heroTicking = false;
          });
          heroTicking = true;
        }
      }, { passive: true });
    }
  }
})();
