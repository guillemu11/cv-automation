/* Shelf to Story — scroll behaviour.
   1) marks <html> as .js so reveal elements start hidden (no-JS shows everything)
   2) IntersectionObserver fades sections in
   3) drives the shelf->phone morph via a single CSS var --p (0..1) on [data-morph] */

(function () {
  "use strict";
  var root = document.documentElement;
  root.classList.add("js");

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // --- reveals ---
  var reveals = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    reveals.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  }

  // --- shelf -> scroll morph ---
  var stage = document.querySelector("[data-morph]");
  if (stage && !reduce) {
    var ticking = false;
    function update() {
      var rect = stage.getBoundingClientRect();
      var total = rect.height - window.innerHeight;
      var p = total > 0 ? (-rect.top) / total : 0;
      p = Math.max(0, Math.min(1, p));
      // ease so the cross-fade lingers at the extremes
      var eased = p < 0.5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
      stage.style.setProperty("--p", eased.toFixed(4));
      ticking = false;
    }
    function onScroll() {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });
    update();
  }
})();
