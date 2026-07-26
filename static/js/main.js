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

/* ---------------------------------------------------------------- service map
   Leaflet loads from the CDN only on pages that contain a map, and only once
   the map is near the viewport. Trigger is proximity-checked on scroll rather
   than IntersectionObserver alone: IO does not fire in every environment (a
   backgrounded or non-painting tab, for one), and a map stuck on "Loading…"
   forever is worse than one that loads a little eagerly. */
(function () {
  var el = document.getElementById("fx-map");
  if (!el) return;

  var LEAFLET_CSS = "https://unpkg.com/leaflet@1.9.4/dist/leaflet.css";
  var LEAFLET_JS = "https://unpkg.com/leaflet@1.9.4/dist/leaflet.js";
  var started = false;

  function fail() { el.classList.add("fx-map--failed"); }

  function load(cb) {
    var link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = LEAFLET_CSS;
    document.head.appendChild(link);
    var s = document.createElement("script");
    s.src = LEAFLET_JS;
    s.onload = cb;
    s.onerror = fail;
    document.head.appendChild(s);
    // If the CDN hangs rather than erroring, stop showing "Loading map…".
    setTimeout(function () {
      if (!el.classList.contains("fx-map--ready")) fail();
    }, 12000);
  }

  function init() {
    if (typeof L === "undefined") { fail(); return; }
    var data;
    try { data = JSON.parse(el.getAttribute("data-map")); }
    catch (e) { fail(); return; }

    var map = L.map(el, { scrollWheelZoom: false });

    L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png", {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
      subdomains: "abcd",
      maxZoom: 19
    }).addTo(map);

    var area = L.polygon(data.area, {
      color: "#e5231c", weight: 2, opacity: .85,
      fillColor: "#e5231c", fillOpacity: .10
    }).addTo(map);

    data.near.forEach(function (c) {
      L.circleMarker([c.lat, c.lon], {
        radius: 5, color: "#fff", weight: 2, fillColor: "#64748b", fillOpacity: 1
      }).addTo(map).bindTooltip(c.name, { direction: "top" });
    });

    data.main.forEach(function (c) {
      L.circleMarker([c.lat, c.lon], {
        radius: 9, color: "#fff", weight: 3, fillColor: "#e5231c", fillOpacity: 1
      }).addTo(map)
        .bindTooltip(c.name, { direction: "top" })
        .bindPopup('<strong>' + c.name + '</strong><br><a href="' + c.url + '">Appliance repair in ' + c.name + ' &rarr;</a>');
    });

    map.fitBounds(area.getBounds(), { padding: [24, 24] });
    el.classList.add("fx-map--ready");
  }

  function start() {
    if (started) return;
    started = true;
    window.removeEventListener("scroll", maybeStart);
    window.removeEventListener("resize", maybeStart);
    load(init);
  }

  function maybeStart() {
    var r = el.getBoundingClientRect();
    // Within one viewport of the fold, in either direction.
    if (r.top < window.innerHeight * 2 && r.bottom > -window.innerHeight) start();
  }

  window.addEventListener("scroll", maybeStart, { passive: true });
  window.addEventListener("resize", maybeStart);
  maybeStart();
  // Last resort: if nothing above triggered it, load once the page settles.
  window.addEventListener("load", function () { setTimeout(maybeStart, 1200); });
})();
