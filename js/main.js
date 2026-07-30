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

  // Testimonial carousel.
  var carousel = document.getElementById("testiCarousel");
  if (carousel) {
    var slides = carousel.querySelectorAll(".carousel-slide");
    var dotsWrap = carousel.parentElement.querySelector(".carousel-dots");
    var dots = dotsWrap ? dotsWrap.querySelectorAll(".carousel-dot") : [];
    var idx = 0;

    function goTo(n) {
      idx = (n + slides.length) % slides.length;
      slides.forEach(function (s, i) { s.classList.toggle("is-active", i === idx); });
      dots.forEach(function (d, i) { d.classList.toggle("is-active", i === idx); });
    }

    dots.forEach(function (d) {
      d.addEventListener("click", function () { goTo(Number(d.dataset.goto)); });
    });
    var prevBtn = carousel.querySelector(".carousel-prev");
    var nextBtn = carousel.querySelector(".carousel-next");
    if (prevBtn) prevBtn.addEventListener("click", function () { goTo(idx - 1); });
    if (nextBtn) nextBtn.addEventListener("click", function () { goTo(idx + 1); });
  }

  // Multi-step quote wizard on the contact page.
  var wizard = document.getElementById("quoteWizard");
  if (wizard) {
    wizard.classList.add("js-enabled");
    var steps = wizard.querySelectorAll(".wizard-step");
    var stepNumEl = document.getElementById("wizStepNum");
    var current = 1;

    function showStep(n) {
      current = n;
      steps.forEach(function (el) {
        el.classList.toggle("is-active", Number(el.dataset.step) === n);
      });
      if (stepNumEl) stepNumEl.textContent = String(n);
    }
    showStep(1);

    wizard.querySelectorAll(".wizard-choice").forEach(function (btn) {
      btn.addEventListener("click", function () {
        wizard.querySelectorAll(".wizard-choice").forEach(function (b) { b.classList.remove("selected"); });
        btn.classList.add("selected");
        var input = document.getElementById("wizServiceInput");
        if (input) input.value = btn.dataset.value || "";
        showStep(2);
      });
    });

    wizard.querySelectorAll(".wizard-next").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var town = document.getElementById("town");
        if (town && !town.reportValidity()) return;
        showStep(3);
      });
    });

    wizard.querySelectorAll(".wizard-back").forEach(function (btn) {
      btn.addEventListener("click", function () {
        showStep(Math.max(1, current - 1));
      });
    });

    var form = document.getElementById("quoteForm");
    var success = document.getElementById("wizardSuccess");
    if (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var data = new FormData(form);
        fetch(form.action, { method: "POST", body: data, headers: { Accept: "application/json" } })
          .then(function (res) {
            if (res.ok) {
              form.hidden = true;
              if (success) success.hidden = false;
            } else {
              form.submit();
            }
          })
          .catch(function () {
            form.submit();
          });
      });
    }
  }
});
