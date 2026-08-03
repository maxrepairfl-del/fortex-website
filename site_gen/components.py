"""Reusable HTML components and the document shell."""
import html
import json

import hashlib
import os

from .data import (SITE, SERVICES, CITIES, NEARBY, BRANDS, CITY_COORDS,
                   SERVICE_AREA_POLYGON)
from .icons import icon, logo_mark
from .images import img


def esc(s):
    return html.escape(str(s), quote=True)


_STATIC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static")


def asset(path):
    """Return an asset URL with a content hash appended.

    /css/styles.css and /js/main.js are served with max-age=604800 under fixed
    names, so without this a returning visitor keeps a week-old stylesheet after
    a deploy. That is not just cosmetic: an SVG element whose fill only exists in
    the new CSS falls back to the SVG default of solid black.
    """
    local = os.path.join(_STATIC, path.lstrip("/"))
    try:
        with open(local, "rb") as fh:
            digest = hashlib.md5(fh.read()).hexdigest()[:8]
    except OSError:
        return path
    return f"{path}?v={digest}"


def stars(n=5):
    return '<span class="stars" aria-label="' + str(n) + ' out of 5 stars">' + ("★" * n) + "</span>"


# ----------------------------------------------------------------- doc shell
GOOGLE_FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&'
    'family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">'
)


def base_schema():
    return {
        "@context": "https://schema.org",
        "@type": "HVACBusiness",
        "@id": SITE["url"] + "/#business",
        "name": SITE["name"],
        "image": SITE["url"] + "/images/fridge-branded-1200.jpg",
        "url": SITE["url"],
        "telephone": SITE["phone"],
        "priceRange": "$$",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Huntington Beach",
            "addressRegion": "CA",
            "addressCountry": "US",
        },
        "areaServed": [{"@type": "City", "name": c["name"]} for c in CITIES]
        + [{"@type": "City", "name": n} for n in NEARBY],
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "5.0",
            "reviewCount": "101",
            "bestRating": "5",
        },
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification",
             "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
             "opens": "09:00", "closes": "18:00"},
            {"@type": "OpeningHoursSpecification",
             "dayOfWeek": "Saturday", "opens": "09:00", "closes": "13:00"},
        ],
        "sameAs": [u for u in [SITE["yelp_url"], SITE.get("google_url")] if u and u != "#"],
    }


def page(title, desc, path, body, extra_schema=None, og_image="fridge-branded"):
    canonical = SITE["url"] + path
    og = f'{SITE["url"]}/images/{og_image}-1200.jpg'
    schema = [base_schema()]
    if extra_schema:
        schema += extra_schema if isinstance(extra_schema, list) else [extra_schema]
    schema_tag = "".join(
        f'<script type="application/ld+json">{json.dumps(s)}</script>' for s in schema
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#E11B22">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og}">
<meta property="og:site_name" content="{esc(SITE['name'])}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
{GOOGLE_FONTS}
<link rel="stylesheet" href="{asset("/css/styles.css")}">
{schema_tag}
</head>
<body>
{promobar()}
{header(path)}
{mobile_nav()}
<main id="main">
{body}
</main>
{footer()}
{mobilebar()}
<script src="{asset("/js/main.js")}" defer></script>
</body>
</html>"""


# ----------------------------------------------------------------- brand/logo
def brand(href="/", light=False):
    return (
        f'<a class="brand" href="{href}" aria-label="{esc(SITE["name"])} home">'
        f'{logo_mark()}'
        f'<span class="word"><b>FORTEX</b><span>Appliance Repair</span></span></a>'
    )


# ----------------------------------------------------------------- promobar
def promobar():
    return (
        '<div class="promobar">'
        f'{icon("shield-plain", size=15)}<span><b>Licensed &amp; Insured</b> · CA Lic #{SITE["license"]}</span>'
        '<span class="dot hide-sm">•</span>'
        f'<span class="hide-sm">{esc(SITE["promo"])}</span>'
        '<span class="dot">•</span>'
        f'<a href="{SITE["phone_href"]}">Call {esc(SITE["phone"])}</a>'
        '</div>'
    )


# ----------------------------------------------------------------- header/nav
def _services_menu():
    items = "".join(
        f'<a href="/services/{s["slug"]}/">{esc(s["short"])}</a>' for s in SERVICES
    )
    return (
        '<div class="menu" style="min-width:460px;display:grid;'
        'grid-template-columns:1fr 1fr;gap:2px">'
        f'{items}</div>'
    )


def _areas_menu():
    items = "".join(f'<a href="/areas/{c["slug"]}/">{esc(c["name"])}</a>' for c in CITIES)
    items += '<a href="/areas/"><strong>All areas →</strong></a>'
    return f'<div class="menu">{items}</div>'


def _cur(path, target):
    if target == "/":
        return ' aria-current="page"' if path == "/" else ""
    return ' aria-current="page"' if path.startswith(target) else ""


def header(path="/"):
    return f"""<header class="site-header">
<div class="wrap nav">
{brand()}
<nav class="nav-links" aria-label="Primary">
  <a href="/"{_cur(path,'/')}>Home</a>
  <span class="has-menu"><a href="/services/"{_cur(path,'/services')}>Services ▾</a>{_services_menu()}</span>
  <span class="has-menu"><a href="/areas/"{_cur(path,'/areas')}>Areas ▾</a>{_areas_menu()}</span>
  <a href="/how-it-works/"{_cur(path,'/how-it-works')}>How It Works</a>
  <a href="/about/"{_cur(path,'/about')}>About</a>
  <a href="/reviews/"{_cur(path,'/reviews')}>Reviews</a>
</nav>
<div class="nav-cta">
  <a class="nav-phone" href="{SITE['phone_href']}">{icon('phone', size=18)}{esc(SITE['phone'])}</a>
  <a class="btn btn--primary" href="/book/">Book Online</a>
</div>
<button class="nav-toggle" aria-label="Open menu" aria-expanded="false" data-nav-open>{icon('menu', size=26)}</button>
</div>
</header>"""


def mobile_nav():
    links = "".join(
        f'<a href="{href}">{label}</a>'
        for href, label in [
            ("/", "Home"), ("/services/", "Services"), ("/areas/", "Service Areas"),
            ("/how-it-works/", "How It Works"), ("/about/", "About"), ("/reviews/", "Reviews"),
        ]
    )
    return f"""<div class="scrim" data-nav-close></div>
<aside class="mobile-nav" aria-label="Mobile menu">
  <div class="m-head">{brand()}<button class="nav-toggle" aria-label="Close menu" data-nav-close>{icon('close', size=26)}</button></div>
  {links}
  <a class="btn btn--primary btn--block" href="/book/" style="margin-top:14px">Book Online</a>
  <a class="btn btn--outline btn--block" href="{SITE['phone_href']}" style="margin-top:10px">{icon('phone', size=18)} {esc(SITE['phone'])}</a>
</aside>"""


def mobilebar():
    return f"""<div class="mobilebar">
  <a class="call" href="{SITE['phone_href']}">{icon('phone', size=19)} Call Now</a>
  <a class="book" href="/book/">{icon('calendar', size=19)} Book Online</a>
</div>"""


# ----------------------------------------------------------------- footer
def footer():
    svc = "".join(
        f'<li><a href="/services/{s["slug"]}/">{esc(s["short"])}</a></li>' for s in SERVICES[:8]
    )
    areas = "".join(
        f'<li><a href="/areas/{c["slug"]}/">{esc(c["name"])}</a></li>' for c in CITIES
    )
    return f"""<footer class="site-footer">
<div class="wrap">
  <div class="footer-grid">
    <div>
      {brand(light=True)}
      <p class="footer-about">Licensed, insured, same-day appliance repair across Orange County. Honest pricing and warrantied work on every major brand.</p>
      <div class="footer-badges">
        <a href="{SITE['yelp_url']}" aria-label="Fortex on Yelp">{img('yelp-badge', sizes='64px')}</a>
      </div>
    </div>
    <div class="footer-col">
      <h4>Services</h4>
      <ul>{svc}<li><a href="/services/"><strong>All services →</strong></a></li></ul>
    </div>
    <div class="footer-col">
      <h4>Service Areas</h4>
      <ul>{areas}<li><a href="/areas/"><strong>All areas →</strong></a></li></ul>
    </div>
    <div class="footer-col">
      <h4>Contact</h4>
      <ul class="footer-contact">
        <li>{icon('phone', size=18)}<a href="{SITE['phone_href']}">{esc(SITE['phone'])}</a></li>
        <li>{icon('mail', size=18)}<a href="mailto:{SITE['email']}">{esc(SITE['email'])}</a></li>
        <li>{icon('pin', size=18)}<span>Serving {esc(SITE['region'])}</span></li>
        <li>{icon('clock', size=18)}<span>{esc(SITE['hours'])}</span></li>
      </ul>
      <a class="btn btn--primary" href="/book/" style="margin-top:6px">Book a Repair</a>
    </div>
  </div>
  <div class="footer-bottom">
    <span>© {{year}} {esc(SITE['name'])} · CA License #{SITE['license']} · <a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a></span>
    <div class="pay-badges" aria-label="Accepted payment methods">
      <span class="pay">VISA</span><span class="pay">Mastercard</span><span class="pay">Amex</span><span class="pay">Discover</span>
    </div>
  </div>
</div>
</footer>"""


# ----------------------------------------------------------------- sections
def trust_strip():
    # The two rating items link out to the actual profiles — a rating a visitor
    # can go and check beats one they have to take our word for.
    items = [
        (stars() + " <span>5.0 on Yelp</span>", None, SITE["yelp_url"]),
        (stars() + " <span>5.0 on Google</span>", None, SITE.get("google_url")),
        ("2,000+ repairs completed", "wrench", None),
        (f"Licensed &amp; insured · #{SITE['license']}", "shield-plain", None),
        ("Same-day service", "bolt", None),
        ("12-month warranty", "award", None),
    ]
    out = []
    for label, ic, href in items:
        lead = icon(ic, size=22) if ic else ""
        if href:
            out.append(f'<a class="trust-item trust-item--link" href="{href}" '
                       f'target="_blank" rel="noopener nofollow">{lead}<span>{label}</span></a>')
        else:
            out.append(f'<div class="trust-item">{lead}<span>{label}</span></div>')
    return f'<section class="trust-strip"><div class="wrap">{"".join(out)}</div></section>'


def cta_band(heading="Ready to get your appliance fixed?",
             sub="Call now or book online and a licensed Fortex technician will be at your door — often the same day."):
    return f"""<section class="section"><div class="wrap">
  <div class="cta-band reveal">
    <h2>{esc(heading)}</h2>
    <p>{esc(sub)}</p>
    <div class="hero-cta">
      <a class="btn btn--primary btn--lg" href="/book/">{icon('calendar', size=20)} Book Online</a>
      <a class="btn btn--ghost btn--lg" href="{SITE['phone_href']}">{icon('phone', size=20)} {esc(SITE['phone'])}</a>
    </div>
  </div>
</div></section>"""


def brand_strip():
    spans = "".join(f"<span>{esc(b)}</span>" for b in BRANDS)
    spans += '<span class="more-brands">&amp; many more</span>'
    return f"""<section class="section section--tight section--surface"><div class="wrap center">
  <p class="eyebrow">We repair all major brands</p>
  <h2 style="margin-bottom:8px">From everyday to high-end &amp; built-in</h2>
  <p class="lede center" style="margin-bottom:26px">Hands-on experience with every major appliance brand sold in the U.S.</p>
  <div class="brandstrip">{spans}</div>
</div></section>"""


# Bump this string whenever the consent wording below changes. It is submitted
# with every form, so a stored lead always records which version the customer
# actually saw — RingCentral asks for this if consent is ever challenged.
SMS_CONSENT_VERSION = "2026-08-02"

SMS_CONSENT_TEXT = (
    "By checking this box, I consent to receive conversational and customer-care SMS messages from Fortex Appliance Repair LLC regarding my service request, pricing, scheduling, appointment confirmations, repair updates, parts updates, and return visits. Messaging frequency may vary. Message and data rates may apply. Reply STOP to opt out or HELP for support. Consent is not a condition of purchase. View our "
)


def sms_consent(prefix, source_page):
    """Optional, unchecked-by-default SMS consent checkbox (A2P 10DLC / RingCentral).

    Must never be `required` and must never carry `checked` — the form has to
    submit fine without it, and a pre-ticked box is not valid consent.
    """
    cid = f"{prefix}sms-consent"
    return f"""<div class="consent">
  <input type="checkbox" id="{cid}" name="sms_consent" value="yes">
  <label for="{cid}">{esc(SMS_CONSENT_TEXT)}<a href="/privacy/">Privacy Policy</a> and <a href="/terms/">Terms &amp; Conditions</a>.</label>
</div>
<input type="hidden" name="sms_consent_version" value="{esc(SMS_CONSENT_VERSION)}">
<input type="hidden" name="consent_source" value="{esc(source_page)}">"""


# --- coverage map -----------------------------------------------------------
def coverage_map():
    """Real slippy map with the service area shaded, built on Leaflet.

    Tiles come from CARTO's light basemap (OpenStreetMap data) — free, no API
    key and no developer account. Apple's MapKit needs a paid Apple Developer
    membership, and screenshotting Apple or Google Maps onto a commercial site
    breaks their terms, so neither of those is an option here.

    The map only initialises once it scrolls near the viewport, so the library
    and tiles cost nothing on pages the visitor never scrolls to the bottom of.
    """
    main = [
        {"name": c["name"], "lat": CITY_COORDS[c["name"]][0],
         "lon": CITY_COORDS[c["name"]][1], "url": f"/areas/{c['slug']}/"}
        for c in CITIES if c["name"] in CITY_COORDS
    ]
    near = [
        {"name": n, "lat": CITY_COORDS[n][0], "lon": CITY_COORDS[n][1]}
        for n in NEARBY if n in CITY_COORDS
    ]
    payload = json.dumps({
        "main": main, "near": near,
        "area": [[la, lo] for la, lo in SERVICE_AREA_POLYGON],
    }, separators=(",", ":"))

    # Plain-text fallback for no-JS and for crawlers.
    names = ", ".join([c["name"] for c in CITIES] + list(NEARBY))
    return f"""<div class="map-wrap reveal">
  <div id="fx-map" class="fx-map" data-map='{esc(payload)}'
       role="img" aria-label="Map of the Orange County area served by Fortex Appliance Repair">
    <noscript><p class="map-fallback">We serve {esc(names)}.</p></noscript>
  </div>
  <p class="map-legend">
    <span><i class="dot dot--main"></i>Cities we cover in depth — tap a pin for details</span>
    <span><i class="dot dot--near"></i>Also serving nearby</span>
  </p>
</div>"""


def source_url(source):
    """Profile URL for a review's source, so customers can verify it themselves."""
    return {"Yelp": SITE["yelp_url"], "Google": SITE.get("google_url")}.get(source) or ""


def review_card(r):
    name = (r.get("name") or "").strip()
    src, url = esc(r["source"]), source_url(r["source"])
    # Link the source back to the profile — a review the reader can go and
    # check is worth more than one they have to take on faith.
    src_link = (f'<a href="{url}" target="_blank" rel="noopener nofollow" '
                f'class="src">{src}</a>') if url else f'<span class="src">{src}</span>'
    if name:
        initials = "".join(p[0] for p in name.split()[:2]).upper()
        who = (f'<span class="av">{initials}</span>'
               f'<span><b>{esc(name)}</b><span>{esc(r["city"])} · '
               f'{src_link}</span></span>')
    else:
        who = (f'<span class="av av--verified">{icon("check", size=20)}</span>'
               f'<span><b>Verified {src_link} review</b>'
               f'<span>{esc(r["city"])}</span></span>')
    return f"""<article class="review reveal">
  {stars(r['rating'])}
  <p>“{esc(r['text'])}”</p>
  <div class="who">{who}</div>
</article>"""


def faq_block(faqs):
    items = "".join(
        f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faqs
    )
    return f'<div class="faq">{items}</div>'


def faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }


def areas_grid():
    """Clean area cards (no photos) with descriptions."""
    cards = ""
    for c in CITIES:
        desc = c.get("card", "Appliance repair across " + c["name"])
        cards += f"""<a class="area-card reveal" href="/areas/{c['slug']}/">
  <div class="area-ic">{icon("pin", size=20)}</div>
  <h3>{esc(c["name"])}</h3>
  <p>{esc(desc)}</p>
</a>"""
    return f'<div class="area-cards">{cards}</div>'
