/* Fortex — light progressive enhancement (no dependencies). */
(function () {
  "use strict";


  /* ---------- business hours: never push an unanswered phone ----------
     Mon-Fri 9:00-18:00, Sat 9:00-16:00, Sun closed, Pacific — computed in the
     shop's timezone, not the visitor's, so someone browsing from another state
     still sees the right thing. Fails open: if anything throws, the page keeps
     its default (phone-first) layout rather than telling everyone we're shut. */
  try {
    var la = new Date(new Date().toLocaleString("en-US", { timeZone: "America/Los_Angeles" }));
    var day = la.getDay(), hour = la.getHours() + la.getMinutes() / 60;
    var open = day >= 1 && day <= 5 ? hour >= 9 && hour < 18
             : day === 6 ? hour >= 9 && hour < 16
             : false;
    if (!open) document.body.classList.add("is-closed");
  } catch (e) { /* leave the default layout */ }


  /* ---------- work out where the lead actually came from ----------
     Classified from the tracking parameters on the click, never from the
     landing page or the appliance: someone who lands on the oven page from an
     organic search is not a Google Ads lead, and saying so would make paid
     spend look better than it is. With no parameters and no referrer the
     answer is Direct, and anything unrecognised stays Unknown rather than
     being attributed to a campaign.

     Stashed for the session because the click that paid for the visit happens
     on the landing page, while the form may be submitted several pages later. */
  try {
    var KEY = "fx_lead_origin";
    var qs = new URLSearchParams(window.location.search);
    var AD_KEYS = ["utm_source","utm_medium","utm_campaign","utm_term","utm_content",
                   "gclid","gbraid","wbraid","gad_source","msclkid"];
    var params = {};
    AD_KEYS.forEach(function (k) { if (qs.get(k)) params[k] = qs.get(k); });

    function classify(p, referrer) {
      var src = (p.utm_source || "").toLowerCase();
      var med = (p.utm_medium || "").toLowerCase();
      if (p.gclid || p.gbraid || p.wbraid || (src === "google" && /cpc|ppc|paid/.test(med))) return "Google Ads";
      if (/chatgpt|openai/.test(src)) return "ChatGPT Ads";
      if (p.msclkid || (src === "bing" && /cpc|ppc|paid/.test(med))) return "Bing Ads";
      if (/cpc|ppc|paid/.test(med) && src) return "Paid - " + src;
      if (src) return "Campaign - " + src;
      if (!referrer) return "Direct";
      if (/google\.|bing\.|duckduckgo\.|search\.yahoo\./.test(referrer)) return "Organic Search";
      if (/yelp\./.test(referrer)) return "Yelp";
      if (/facebook\.|instagram\./.test(referrer)) return "Social";
      return "Referral - " + referrer.replace(/^https?:\/\//, "").split("/")[0];
    }

    var ref = document.referrer && !/fortexappliancerepair\.com/.test(document.referrer)
      ? document.referrer : "";
    var stored = null;
    try { stored = JSON.parse(sessionStorage.getItem(KEY) || "null"); } catch (e) {}

    // the first touch of the session wins; a later internal page must not
    // overwrite a paid click with "Direct"
    if (!stored || Object.keys(params).length) {
      stored = {
        lead_source: classify(params, ref),
        landing_page: window.location.pathname,
        ad_params: Object.keys(params).length ? JSON.stringify(params) : ""
      };
      try { sessionStorage.setItem(KEY, JSON.stringify(stored)); } catch (e) {}
    }

    var fill = function (sel, val) {
      Array.prototype.forEach.call(document.querySelectorAll(sel), function (el) { el.value = val; });
    };
    fill("[data-lead-source]", stored.lead_source);
    fill("[data-landing-page]", stored.landing_page);
    fill("[data-ad-params]", stored.ad_params);
  } catch (e) { /* attribution must never block a submission */ }


  /* ---------- name the appliance back on the confirmation page ----------
     Carried on the query string by the form's redirect. Falls back to the
     generic word rather than printing an empty sentence, and the value is
     written as text so a crafted URL cannot inject markup. */
  try {
    var tyEl = document.querySelector("[data-ty-appliance]");
    if (tyEl) {
      var forWhat = new URLSearchParams(window.location.search).get("for");
      if (forWhat) {
        tyEl.textContent = forWhat.replace(/[^\w &'/-]/g, "").slice(0, 40).toLowerCase();
      }
    }
  } catch (e) {}

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

  /* ---------- booking forms: validation, resilient submit, UX ----------

     Submitted with fetch rather than a native POST navigation. Formspree sits
     behind Cloudflare and does go down (a 502 there used to replace our page
     with Cloudflare's error screen, losing the lead and the visitor). Keeping
     the visitor on our page lets us offer the phone number instead.

     The native action/method are left intact, so with JS disabled the form
     still submits the old way.
  */
  var TEL = (document.querySelector('a[href^="tel:"]') || {}).href || "";
  var SMS = (document.querySelector('a[href^="sms:"]') || {}).href || "";
  var TEL_TEXT = (document.querySelector(".nav-phone") || {}).textContent || "call us";

  function submitFailed(form, btn, btnHtml) {
    if (btn) { btn.disabled = false; btn.style.opacity = ""; btn.innerHTML = btnHtml; }
    var box = form.querySelector(".form-error");
    if (!box) {
      box = document.createElement("div");
      box.className = "form-error";
      box.setAttribute("role", "alert");
      box.innerHTML =
        "<strong>We couldn't send that just now.</strong>" +
        "<span>Our form provider isn't responding. Your request was not submitted — " +
        "please call or text and we'll get you booked right away.</span>" +
        '<span class="form-error__cta">' +
          (TEL ? '<a class="btn btn--primary" href="' + TEL + '">' + TEL_TEXT.trim() + "</a>" : "") +
          (SMS ? '<a class="btn btn--outline" href="' + SMS + '">Text us</a>' : "") +
        "</span>";
      (btn && btn.parentNode ? btn.parentNode.insertBefore(box, btn) : form.appendChild(box));
    }
    box.scrollIntoView({ behavior: "smooth", block: "center" });
  }

  Array.prototype.forEach.call(document.querySelectorAll("[data-booking]"), function (form) {
    form.addEventListener("submit", function (e) {
      // the radio-button form must have an appliance picked
      // Must match radios only. The service pages carry the appliance in a
      // hidden input of the same name, which is never :checked, so a looser
      // selector silently cancelled every submission from those pages.
      var radios = form.querySelectorAll('input[type="radio"][name="appliance"]');
      if (radios.length && !form.querySelector('input[type="radio"][name="appliance"]:checked')) {
        e.preventDefault();
        var grid = form.querySelector(".choice-grid");
        if (grid) {
          grid.style.outline = "2px solid var(--red)";
          grid.style.outlineOffset = "6px";
          grid.scrollIntoView({ behavior: "smooth", block: "center" });
        }
        return;
      }
      if (!window.fetch || !form.action) return; // fall back to a native POST

      e.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      var btnHtml = btn ? btn.innerHTML : "";
      if (btn) { btn.disabled = true; btn.style.opacity = ".7"; btn.textContent = "Sending…"; }
      var err = form.querySelector(".form-error");
      if (err) err.remove();

      var done = false;
      var giveUp = setTimeout(function () {
        if (!done) { done = true; submitFailed(form, btn, btnHtml); }
      }, 15000);

      fetch(form.action, {
        method: "POST",
        body: new FormData(form),
        headers: { Accept: "application/json" },
      }).then(function (res) {
        if (done) return;
        done = true; clearTimeout(giveUp);
        if (!res.ok) return submitFailed(form, btn, btnHtml);
        var next = form.querySelector('input[name="_next"]');
        window.location.href = next && next.value ? next.value : "/book/thank-you/";
      }).catch(function () {
        if (done) return;
        done = true; clearTimeout(giveUp);
        submitFailed(form, btn, btnHtml);
      });
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
  });
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

    // Leaflet's default attribution prefix carries a Ukrainian flag emoji, added
    // upstream in 2022. It is a political statement on a Californian repair
    // company's coverage map, so the prefix is set explicitly instead.
    map.attributionControl.setPrefix(
      '<a href="https://leafletjs.com/">Leaflet</a>'
    );

    // CARTO's basemap started demanding an API key and began stamping
    // "API KEY REQUIRED" across every tile. OpenStreetMap's own tiles need no
    // key; this site's traffic is far below the level their usage policy cares
    // about, and the required attribution is right here.
    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
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
