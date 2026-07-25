/* Fortex — light progressive enhancement (no dependencies). */
(function () {
  "use strict";

  /* ---------- mobile nav ---------- */
  var nav = document.querySelector(".mobile-nav");
  var scrim = document.querySelector(".scrim");
  function setNav(open) {
    if (!nav) return;
    nav.classList.toggle("open", open);
    scrim.classList.toggle("open", open);
    document.body.style.overflow = open ? "hidden" : "";
    var toggle = document.querySelector("[data-nav-open]");
    if (toggle) toggle.setAttribute("aria-expanded", open ? "true" : "false");
  }
  document.querySelectorAll("[data-nav-open]").forEach(function (b) {
    b.addEventListener("click", function () { setNav(true); });
  });
  document.querySelectorAll("[data-nav-close]").forEach(function (b) {
    b.addEventListener("click", function () { setNav(false); });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") setNav(false);
  });

  /* Reveal animation is now pure CSS (see .reveal in styles.css) so content
     is never dependent on JS to become visible. */

  /* ---------- shrink header on scroll ---------- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.style.boxShadow = window.scrollY > 8
        ? "0 6px 24px -12px rgba(20,30,45,.25)" : "none";
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ---------- YouTube facade → opens a large lightbox on click ---------- */
  var ve = document.querySelector(".video-embed");
  if (ve) {
    var openVideo = function () {
      var id = ve.getAttribute("data-yt");
      if (!id) return; // no video id set yet
      var box = document.createElement("div");
      box.className = "video-lightbox";
      box.innerHTML =
        '<div class="video-lightbox__inner">' +
          '<button class="video-lightbox__close" aria-label="Close video">✕</button>' +
          '<iframe src="https://www.youtube-nocookie.com/embed/' + id +
            '?autoplay=1&rel=0&modestbranding=1" title="Fortex Appliance Repair video" ' +
            'allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>' +
        '</div>';
      document.body.appendChild(box);
      document.body.style.overflow = "hidden";
      var close = function () {
        box.remove();
        document.body.style.overflow = "";
        document.removeEventListener("keydown", onKey);
      };
      box.addEventListener("click", function (e) {
        if (e.target === box || e.target.closest(".video-lightbox__close")) close();
      });
      var onKey = function (e) { if (e.key === "Escape") close(); };
      document.addEventListener("keydown", onKey);
    };
    ve.addEventListener("click", openVideo);
    ve.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); openVideo(); }
    });
  }

  /* ---------- booking form: light validation + UX ---------- */
  var form = document.querySelector("[data-booking]");
  if (form) {
    // require an appliance choice (only for the radio-button form)
    form.addEventListener("submit", function (e) {
      var radios = form.querySelectorAll('input[name="appliance"]');
      if (radios.length && !form.querySelector('input[name="appliance"]:checked')) {
        e.preventDefault();
        var grid = form.querySelector(".choice-grid");
        if (grid) {
          grid.style.outline = "2px solid var(--red)";
          grid.style.outlineOffset = "6px";
          grid.scrollIntoView({ behavior: "smooth", block: "center" });
        }
        return;
      }
      var btn = form.querySelector('button[type="submit"]');
      if (btn) { btn.disabled = true; btn.style.opacity = ".7"; btn.textContent = "Sending…"; }
    });
    // light phone formatting
    var phone = form.querySelector('input[name="phone"]');
    if (phone) {
      phone.addEventListener("input", function () {
        var d = phone.value.replace(/\D/g, "").slice(0, 10);
        if (d.length > 6) phone.value = "(" + d.slice(0, 3) + ") " + d.slice(3, 6) + "-" + d.slice(6);
        else if (d.length > 3) phone.value = "(" + d.slice(0, 3) + ") " + d.slice(3);
        else if (d.length > 0) phone.value = "(" + d;
      });
    }
  }
})();
