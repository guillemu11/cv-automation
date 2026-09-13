/* Talabat O'Clock — app-banner moment cycler + scroll reveals + count-up.
   No dependencies. Respects prefers-reduced-motion. */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- app banner: cycle through craving-moments (talabat mart) ---- */
  var MOMENTS = [
    { time: "05:41", label: "Suhoor run",      craving: "dates, laban & water" },
    { time: "15:00", label: "3pm karak break", craving: "karak, biscuits, a cold drink" },
    { time: "20:45", label: "Matchday haul",   craving: "chips, dips, cold ones" },
    { time: "45°C",  label: "Heatwave rescue", craving: "ice, water, watermelon" },
    { time: "23:58", label: "One thing short", craving: "milk & eggs in 20 min" },
    { time: "Fri",   label: "Brunch reset",    craving: "eggs, avocado, fresh bread" }
  ];

  var elTime = document.querySelector("[data-clock-time]");
  var elLabel = document.querySelector("[data-clock-label]");
  var elCraving = document.querySelector("[data-clock-craving]");
  var i = 0;

  function paint(m) {
    if (!elTime) return;
    [elTime, elLabel, elCraving].forEach(function (el) { el.style.opacity = "0"; });
    setTimeout(function () {
      elTime.textContent = m.time;
      elLabel.textContent = m.label;
      elCraving.textContent = m.craving;
      [elTime, elLabel, elCraving].forEach(function (el) { el.style.opacity = "1"; });
    }, 340);
  }

  if (elTime && !reduce) {
    setInterval(function () {
      i = (i + 1) % MOMENTS.length;
      paint(MOMENTS[i]);
    }, 2600);
  }

  /* ---- scroll reveals ---- */
  var reveals = document.querySelectorAll("[data-reveal]");
  if (reduce || !("IntersectionObserver" in window)) {
    reveals.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.15 });
    reveals.forEach(function (el) { io.observe(el); });
  }

  /* ---- count-up on the insight stat ---- */
  var counter = document.querySelector("[data-count]");
  if (counter && !reduce && "IntersectionObserver" in window) {
    var target = parseInt(counter.getAttribute("data-count"), 10) || 0;
    var seen = false;
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting && !seen) {
          seen = true;
          var start = null, dur = 1200;
          (function step(ts) {
            if (!start) start = ts;
            var pr = Math.min(1, (ts - start) / dur);
            var eased = 1 - Math.pow(1 - pr, 3);
            counter.textContent = Math.round(eased * target);
            if (pr < 1) requestAnimationFrame(step);
          })(performance.now ? performance.now() : Date.now());
        }
      });
    }, { threshold: 0.6 });
    co.observe(counter);
  }
})();
