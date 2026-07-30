document.addEventListener("DOMContentLoaded", function () {
  var yr = document.getElementById("yr");
  if (yr) yr.textContent = new Date().getFullYear();

  var toggle = document.getElementById("navToggle");
  var nav = document.getElementById("primaryNav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  document.querySelectorAll(".ba-slider").forEach(function (slider) {
    var range = slider.querySelector(".ba-range");
    var after = slider.querySelector(".ba-after");
    var handle = slider.querySelector(".ba-handle");
    if (!range || !after || !handle) return;
    function update() {
      var v = range.value;
      after.style.clipPath = "inset(0 " + (100 - v) + "% 0 0)";
      handle.style.left = v + "%";
    }
    range.addEventListener("input", update);
    update();
  });

  // Header gains a shadow once the page has scrolled past the top.
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      if (window.scrollY > 8) header.classList.add("scrolled");
      else header.classList.remove("scrolled");
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  // Scroll-reveal: fade/rise content into view as it enters the viewport.
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealTargets = document.querySelectorAll(
    ".section-head, .svc-card, .testi-card, .who-card, .county-card, .step, .faq-item, .feature-row"
  );
  if (reduceMotion || !("IntersectionObserver" in window)) {
    revealTargets.forEach(function (el) { el.classList.add("reveal-visible"); });
  } else {
    revealTargets.forEach(function (el) { el.classList.add("reveal"); });
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("reveal-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    revealTargets.forEach(function (el) { io.observe(el); });
  }
});
