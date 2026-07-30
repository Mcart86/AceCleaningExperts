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
});
