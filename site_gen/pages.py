"""Page renderers. Each returns (path, html)."""
from .components import (
    page, esc, stars, icon, img, trust_strip, cta_band, brand_strip,
    review_card, faq_block, faq_schema, areas_grid,
)
from .data import (
    SITE, SERVICES, SERVICES_BY_SLUG, CITIES, NEARBY, STEPS, WHY, STATS,
    REVIEWS, HOME_FAQ, BRANDS, BOOKING_APPLIANCES,
)


# ----------------------------------------------------------- shared fragments
def steps_section(heading="How it works", sub="Three simple steps from broken to fixed — usually in a single visit."):
    cards = ""
    for i, (ic, title, body) in enumerate(STEPS, 1):
        cards += f"""<div class="step reveal">
  <div class="n">{i}</div><div class="ic">{icon(ic, size=24)}</div>
  <h3>{esc(title)}</h3><p>{esc(body)}</p>
</div>"""
    return f"""<section class="section section--surface"><div class="wrap">
  <div class="section-head center"><p class="eyebrow">{esc(heading)}</p>
    <h2>From first call to fixed, fast</h2><p class="lede">{esc(sub)}</p></div>
  <div class="steps">{cards}</div>
</div></section>"""


def video_section(poster="fridge-branded"):
    vid = SITE.get("video_id", "")
    play = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
    points = [
        ("clock", "On time, every time — we respect your schedule"),
        ("dollar", "An upfront price before any work begins"),
        ("leaf", "Tidy, booties-on service that leaves no mess"),
    ]
    plist = "".join(
        f'<li>{icon(ic, size=20)}<span>{esc(t)}</span></li>' for ic, t in points
    )
    return f"""<section class="section section--surface" id="video"><div class="wrap">
  <div class="split">
    <div>
      <p class="eyebrow">Watch · 60 seconds</p>
      <h2>See a real Fortex repair, start to finish</h2>
      <p class="lede" style="margin-top:14px">No mystery and no upsell. Watch exactly how a visit goes — the diagnosis, the fix, and the clean-up — so you know what to expect before we knock on your door.</p>
      <ul class="aside-list" style="margin-top:22px;gap:14px">{plist}</ul>
      <a class="btn btn--primary" style="margin-top:26px" href="/book/">{icon('calendar', size=18)} Book Your Repair</a>
    </div>
    <div class="video-embed reveal" data-yt="{esc(vid)}" role="button" tabindex="0" aria-label="Play video">
      <span class="video-tag"><span class="yt">YouTube</span> Our process</span>
      <button class="video-play" aria-label="Play video">{play}</button>
      {img(poster, sizes='(max-width:1000px) 92vw, 560px')}
    </div>
  </div>
</div></section>"""


def home_quote_form():
    opts = "".join(f"<option>{esc(label)}</option>" for label, _ic in BOOKING_APPLIANCES)
    bullets = [
        ("bolt", "Same-day &amp; next-day appointments"),
        ("dollar", "Free service call with your repair"),
        ("award", "12-month parts / 90-day labor warranty"),
    ]
    blist = "".join(f'<li>{icon(ic, size=20)}<span>{t}</span></li>' for ic, t in bullets)
    return f"""<section class="section section--surface" id="quote"><div class="wrap">
  <div class="quote-grid">
    <div>
      <p class="eyebrow">Free quote</p>
      <h2>Book your repair in under a minute</h2>
      <p class="lede" style="margin-top:12px">Tell us what's wrong and we'll text or call right back to confirm your same-day or next-day appointment.</p>
      <ul class="aside-list" style="margin-top:20px;gap:13px">{blist}</ul>
    </div>
    <form class="form-card" name="quote" method="POST" action="{esc(SITE['form_endpoint'])}" data-booking>
      <input type="hidden" name="_next" value="{esc(SITE['url'])}/book/thank-you/">
      <input type="hidden" name="_subject" value="New quote request — fortexappliancerepair.com">
      <p class="hp"><label>Don't fill this out: <input name="_gotcha" tabindex="-1" autocomplete="off"></label></p>
      <div class="field-row">
        <div class="field"><label for="q-appl">Appliance <span class="req">*</span></label>
          <select id="q-appl" name="appliance" required><option value="" disabled selected>Choose…</option>{opts}</select></div>
        <div class="field"><label for="q-name">Your name <span class="req">*</span></label>
          <input id="q-name" name="name" autocomplete="name" required></div>
      </div>
      <div class="field-row">
        <div class="field"><label for="q-phone">Phone <span class="req">*</span></label>
          <input id="q-phone" name="phone" type="tel" autocomplete="tel" required></div>
        <div class="field"><label for="q-zip">ZIP code</label>
          <input id="q-zip" name="zip" inputmode="numeric" autocomplete="postal-code" placeholder="92602"></div>
      </div>
      <div class="field"><label for="q-issue">What's wrong? <span class="req">*</span></label>
        <input id="q-issue" name="issue" placeholder="e.g. Fridge not cooling and making noise" required></div>
      <button class="btn btn--primary btn--lg btn--block" type="submit">{icon('calendar', size=20)} Get My Free Quote</button>
      <p class="form-note">No obligation. We'll never share your information.</p>
    </form>
  </div>
</div></section>"""


def why_split(photo="tech-portrait", heading="Orange County trusts Fortex"):
    feats = ""
    for ic, t, b in WHY:
        feats += f"""<div class="feature">
  <div class="fic">{icon(ic, size=24)}</div>
  <div><h3>{esc(t)}</h3><p>{esc(b)}</p></div>
</div>"""
    return f"""<section class="section"><div class="wrap">
  <div class="split">
    <div class="media reveal">{img(photo, sizes='(max-width:1000px) 90vw, 520px')}</div>
    <div>
      <p class="eyebrow">Why Fortex</p><h2>{esc(heading)}</h2>
      <div class="feature-list">{feats}</div>
    </div>
  </div>
</div></section>"""


def services_tiles(heading="What we fix", title="Repair for every major appliance",
                   sub="From refrigerators to ice machines — tap your appliance to see common problems we fix."):
    tiles = ""
    for s in SERVICES:
        tiles += f"""<a class="svc-tile reveal" href="/services/{s['slug']}/">
  <span class="svc-tile__ic">{icon(s['icon'], size=26)}</span>
  <span class="svc-tile__name">{esc(s['short'])}</span>
</a>"""
    return f"""<section class="section section--surface" id="services"><div class="wrap">
  <div class="section-head center"><p class="eyebrow">{esc(heading)}</p>
    <h2>{esc(title)}</h2><p class="lede">{esc(sub)}</p></div>
  <div class="svc-tiles">{tiles}</div>
  <div class="center" style="margin-top:30px"><a class="btn btn--outline" href="/services/">See all services &amp; details {icon('arrow-right', size=16)}</a></div>
</div></section>"""


def services_grid(heading="What we fix", title="Repair for every major appliance",
                  sub="From refrigerators to ice machines, our licensed technicians repair all major brands across Orange County."):
    cards = ""
    for s in SERVICES:
        cards += f"""<a class="svc-card reveal" href="/services/{s['slug']}/">
  <div class="ic">{icon(s['icon'], size=28)}</div>
  <h3>{esc(s['short'])}</h3><p>{esc(s['card'])}</p>
  <span class="more">Learn more {icon('arrow-right', size=16)}</span>
</a>"""
    return f"""<section class="section section--surface" id="services"><div class="wrap">
  <div class="section-head center"><p class="eyebrow">{esc(heading)}</p>
    <h2>{esc(title)}</h2><p class="lede">{esc(sub)}</p></div>
  <div class="cards grid-4">{cards}</div>
</div></section>"""


def stats_band():
    cells = "".join(f'<div class="stat"><b>{esc(v)}</b><span>{esc(l)}</span></div>' for v, l in STATS)
    return f'<section class="section section--tight section--slate"><div class="wrap"><div class="stats">{cells}</div></div></section>'


def reviews_section(items=None, heading="Reviews"):
    items = items or REVIEWS[:3]
    cards = "".join(review_card(r) for r in items)
    return f"""<section class="section section--surface" id="reviews"><div class="wrap">
  <div class="section-head center"><p class="eyebrow">{esc(heading)}</p>
    <h2>Loved by 2,000+ Orange County homeowners</h2>
    <p class="lede">Don't take our word for it — here's what neighbors across OC say about Fortex.</p></div>
  <div class="reviews">{cards}</div>
  <div class="rating-summary">
    <span class="rating-pill">{stars()} <b>5.0</b> on Yelp · 101 reviews</span>
    <span class="rating-pill">{stars()} <b>5.0</b> on Google</span>
  </div>
  <div class="center" style="margin-top:26px"><a class="btn btn--outline" href="/reviews/">Read more reviews {icon('arrow-right', size=16)}</a></div>
</div></section>"""


def areas_section():
    return f"""<section class="section"><div class="wrap">
  <div class="section-head center"><p class="eyebrow">Service area</p>
    <h2>Same-day appliance repair across Orange County</h2>
    <p class="lede">Local technicians serving Irvine, Huntington Beach, Anaheim, Santa Ana, Yorba Linda and surrounding cities.</p></div>
  {areas_grid()}
</div></section>"""


def home_faq_section(faqs=None):
    faqs = faqs or HOME_FAQ
    return f"""<section class="section section--surface"><div class="wrap">
  <div class="section-head center"><p class="eyebrow">FAQ</p><h2>Questions, answered</h2></div>
  <div style="display:flex;justify-content:center">{faq_block(faqs)}</div>
</div></section>"""


# ----------------------------------------------------------------- home
def render_home():
    body = f"""
<section class="hero">
  <span class="hero-glow"></span>
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow"><span style="color:var(--yellow)">{icon('star', size=15)}</span> Orange County's 5-star appliance repair</p>
      <h1>Same-Day <span class="accent">Appliance Repair</span> in Orange County</h1>
      <p class="hero-sub">Licensed &amp; insured. Trusted by 2,000+ homeowners across Irvine, Huntington Beach, Anaheim and surrounding cities. Free service call with any repair.</p>
      <div class="hero-cta">
        <a class="btn btn--primary btn--lg" href="/book/">{icon('calendar', size=20)} Book Online</a>
        <a class="btn btn--outline btn--lg" href="{SITE['phone_href']}">{icon('phone', size=20)} {esc(SITE['phone'])}</a>
      </div>
      <ul class="hero-points">
        <li>{icon('check-circle', size=20)}<span>Free service call with repair</span></li>
        <li>{icon('check-circle', size=20)}<span>Certified, insured technicians</span></li>
        <li>{icon('check-circle', size=20)}<span>12-month warranty</span></li>
      </ul>
    </div>
    <div class="hero-media reveal">
      <div class="photo">{img('tech-arrival', sizes='(max-width:1000px) 92vw, 560px', loading='eager', fetchpriority='high')}</div>
      <div class="hero-badge">{icon('shield', size=34, cls='', stroke=1.6)}<div><span class="stars">★★★★★</span><b>Licensed &amp; Insured</b><span>CA Lic #{SITE['license']}</span></div></div>
    </div>
  </div>
</section>
{trust_strip()}
{services_tiles()}
{video_section()}
{home_quote_form()}
{steps_section()}
{why_split('fridge-wide')}
{stats_band()}
{reviews_section()}
{brand_strip()}
{areas_section()}
{home_faq_section()}
{cta_band()}
"""
    desc = ("Same-day appliance repair in Orange County, CA. Licensed & insured Fortex technicians "
            "repair refrigerators, washers, dryers, dishwashers, ovens and more. Free service call with repair. "
            "Call (949) 479-0089.")
    return "/index.html", page(
        f"{SITE['name']} | Same-Day Appliance Repair in Orange County, CA",
        desc, "/", body, extra_schema=faq_schema(HOME_FAQ),
    )


# ----------------------------------------------------------------- services
def render_services_index():
    body = f"""
<section class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="/">Home</a> <span>›</span> <span>Services</span></div>
  <h1>Appliance Repair Services</h1>
  <p>Licensed, insured, same-day repair for every major appliance and brand across Orange County. Pick your appliance to learn more, or book online in under a minute.</p>
</div></section>
{services_grid(heading='Our services', title='What we repair', sub='Select an appliance for common problems we fix, brands we service, and answers to frequent questions.')}
{steps_section()}
{trust_strip()}
{cta_band()}
"""
    return "/services/index.html", page(
        f"Appliance Repair Services in Orange County | {SITE['name']}",
        "Refrigerator, washer, dryer, dishwasher, oven, microwave and more — same-day appliance repair across Orange County, CA. Licensed & insured. Call (949) 479-0089.",
        "/services/", body,
    )


def render_service(s):
    symptoms = "".join(
        f'<li>{icon("check", size=20)}<span>{esc(x)}</span></li>' for x in s["symptoms"]
    )
    related = [x for x in SERVICES if x["slug"] != s["slug"]][:4]
    rel_cards = "".join(
        f"""<a class="svc-card reveal" href="/services/{r['slug']}/">
  <div class="ic">{icon(r['icon'], size=28)}</div><h3>{esc(r['short'])}</h3>
  <p>{esc(r['card'])}</p><span class="more">Learn more {icon('arrow-right', size=16)}</span></a>"""
        for r in related
    )
    faqs = s["faqs"]
    body = f"""
<section class="page-hero"><div class="wrap page-hero-grid">
  <div>
    <div class="breadcrumb"><a href="/">Home</a> <span>›</span> <a href="/services/">Services</a> <span>›</span> <span>{esc(s['short'])}</span></div>
    <h1>{esc(s['name'])} in Orange County</h1>
    <p>{esc(s['intro'])}</p>
    <div class="hero-cta">
      <a class="btn btn--primary btn--lg" href="/book/">{icon('calendar', size=20)} Book This Repair</a>
      <a class="btn btn--outline btn--lg" href="{SITE['phone_href']}">{icon('phone', size=20)} {esc(SITE['phone'])}</a>
    </div>
  </div>
  <div class="media reveal">{img(s['photo'], sizes='(max-width:1000px) 90vw, 460px', loading='eager')}</div>
</div></section>
{trust_strip()}
<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Common problems</p>
    <h2>{esc(s['noun'])} problems we fix</h2>
    <p class="lede">Seeing one of these? We diagnose the real cause and fix it right — usually the same or next day.</p></div>
  <ul class="checks">{symptoms}</ul>
</div></section>
{steps_section()}
{why_split(s['photo'], heading='Why choose Fortex for your repair')}
<section class="section section--surface"><div class="wrap">
  <div class="section-head center"><p class="eyebrow">FAQ</p><h2>{esc(s['noun'])} repair FAQs</h2></div>
  <div style="display:flex;justify-content:center">{faq_block(faqs)}</div>
</div></section>
<section class="section"><div class="wrap">
  <div class="section-head center"><p class="eyebrow">More services</p><h2>We fix these too</h2></div>
  <div class="cards grid-4">{rel_cards}</div>
</div></section>
{cta_band(heading=f"Need your {s['noun'].lower()} repaired today?")}
"""
    svc_schema = {
        "@context": "https://schema.org", "@type": "Service",
        "serviceType": s["name"], "provider": {"@id": SITE["url"] + "/#business"},
        "areaServed": SITE["region"],
        "name": f"{s['name']} in Orange County",
    }
    return f"/services/{s['slug']}/index.html", page(
        f"{s['name']} in Orange County, CA | {SITE['name']}",
        f"Same-day {s['noun'].lower()} repair in Orange County. Licensed & insured Fortex technicians, upfront pricing, 12-month warranty. Call (949) 479-0089.",
        f"/services/{s['slug']}/", body,
        extra_schema=[svc_schema, faq_schema(faqs)], og_image=s["photo"],
    )


# ----------------------------------------------------------------- areas
def render_areas_index():
    cards = ""
    for c in CITIES:
        cards += f"""<a class="photo-card reveal" href="/areas/{c['slug']}/">
  <div class="ph">{img(c['photo'], sizes='(max-width:860px) 90vw, 360px')}</div>
  <div class="bd"><h3>{esc(c['name'])}</h3><p>{esc(c['blurb'])}</p></div></a>"""
    near = "".join(f'<a href="/book/">{icon("pin", size=18)}{esc(n)}</a>' for n in NEARBY)
    body = f"""
<section class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="/">Home</a> <span>›</span> <span>Service Areas</span></div>
  <h1>Appliance Repair Across Orange County</h1>
  <p>Local, licensed technicians serving cities throughout Orange County with same-day and next-day appointments. Find your city below.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="cards grid-3">{cards}</div>
  <div class="section-head center" style="margin-top:48px"><h3>Also serving nearby</h3></div>
  <div class="area-list">{near}</div>
</div></section>
{trust_strip()}
{cta_band()}
"""
    return "/areas/index.html", page(
        f"Appliance Repair Service Areas in Orange County | {SITE['name']}",
        "Fortex provides same-day appliance repair across Orange County — Irvine, Huntington Beach, Anaheim, Santa Ana, Yorba Linda and nearby cities. Call (949) 479-0089.",
        "/areas/", body,
    )


def render_city(c):
    svc = ""
    for s in SERVICES:
        svc += f"""<a class="svc-card reveal" href="/services/{s['slug']}/">
  <div class="ic">{icon(s['icon'], size=28)}</div><h3>{esc(s['short'])}</h3>
  <p>{esc(s['card'])}</p><span class="more">Learn more {icon('arrow-right', size=16)}</span></a>"""
    faqs = [
        (f"Do you offer same-day appliance repair in {c['name']}?",
         f"Yes — we schedule same-day and next-day appointments throughout {c['name']} and the surrounding area whenever possible. Call or text early for the best availability."),
        HOME_FAQ[1], HOME_FAQ[3], HOME_FAQ[4],
    ]
    body = f"""
<section class="page-hero"><div class="wrap page-hero-grid">
  <div>
    <div class="breadcrumb"><a href="/">Home</a> <span>›</span> <a href="/areas/">Service Areas</a> <span>›</span> <span>{esc(c['name'])}</span></div>
    <h1>Appliance Repair in {esc(c['name'])}, CA</h1>
    <p>{esc(c['blurb'])} Licensed, insured, and backed by a 12-month warranty.</p>
    <div class="hero-cta">
      <a class="btn btn--primary btn--lg" href="/book/">{icon('calendar', size=20)} Book Online</a>
      <a class="btn btn--outline btn--lg" href="{SITE['phone_href']}">{icon('phone', size=20)} {esc(SITE['phone'])}</a>
    </div>
  </div>
  <div class="media reveal">{img(c['photo'], sizes='(max-width:1000px) 90vw, 460px', loading='eager')}</div>
</div></section>
{trust_strip()}
<section class="section"><div class="wrap">
  <div class="prose">
    <h2>Your local {esc(c['name'])} appliance repair team</h2>
    <p>When an appliance breaks down in {esc(c['name'])}, you need a technician who can get there fast and fix it right the first time. Fortex Appliance Repair serves homeowners across {esc(c['name'])} — including {esc(c['areas'])} — with same-day and next-day service on every major brand.</p>
    <p>Every repair includes an honest diagnostic and an upfront, all-in price before any work begins. The service call is free when you approve the repair, and we back our work with a 12-month parts and 90-day labor warranty. Licensed (CA #{SITE['license']}) and fully insured.</p>
  </div>
</div></section>
<section class="section section--surface"><div class="wrap">
  <div class="section-head center"><p class="eyebrow">Services in {esc(c['name'])}</p>
    <h2>Every major appliance, repaired</h2></div>
  <div class="cards grid-4">{svc}</div>
</div></section>
{steps_section()}
{reviews_section(REVIEWS[:3], heading=f'{c["name"]} reviews')}
<section class="section"><div class="wrap">
  <div class="section-head center"><p class="eyebrow">FAQ</p><h2>{esc(c['name'])} appliance repair FAQs</h2></div>
  <div style="display:flex;justify-content:center">{faq_block(faqs)}</div>
</div></section>
{cta_band(heading=f"Appliance trouble in {c['name']}?")}
"""
    return f"/areas/{c['slug']}/index.html", page(
        f"Appliance Repair in {c['name']}, CA | {SITE['name']}",
        f"Same-day appliance repair in {c['name']}, CA. Licensed & insured Fortex technicians repair refrigerators, washers, dryers, ovens and more. Free service call with repair. Call (949) 479-0089.",
        f"/areas/{c['slug']}/", body,
        extra_schema=faq_schema(faqs), og_image=c["photo"],
    )


# ----------------------------------------------------------------- how it works
def render_how():
    body = f"""
<section class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="/">Home</a> <span>›</span> <span>How It Works</span></div>
  <h1>How Fortex Works</h1>
  <p>Getting a broken appliance fixed should be simple. Here's exactly what to expect from your first call to a fully working appliance — with no surprises along the way.</p>
</div></section>
{steps_section(sub='No call-center runaround and no surprise fees. Just a fast, honest, warrantied repair.')}
{video_section()}
{why_split('toolbag-shoecovers', heading='What makes a Fortex visit different')}
<section class="section section--surface"><div class="wrap">
  <div class="split">
    <div>
      <p class="eyebrow">The diagnostic</p>
      <h2>Free service call with your repair</h2>
      <div class="prose" style="margin-top:18px">
        <p>Every visit starts with a thorough diagnostic. Your technician inspects the appliance, identifies the true root cause, and explains it in plain language — then gives you a clear, all-in price.</p>
        <p>If you approve the repair, the service call is free. There are no hidden fees and no pressure. Most parts are already on the van, so the majority of repairs are completed in that same visit.</p>
      </div>
    </div>
    <div class="media reveal">{img('diagnostic-meter', sizes='(max-width:1000px) 90vw, 520px')}</div>
  </div>
</div></section>
{stats_band()}
{home_faq_section()}
{cta_band()}
"""
    return "/how-it-works/index.html", page(
        f"How It Works | {SITE['name']}",
        "Easy scheduling, a free diagnostic with your repair, and a 12-month warranty. See exactly how Fortex Appliance Repair works in Orange County. Call (949) 479-0089.",
        "/how-it-works/", body, og_image="diagnostic-meter",
    )


# ----------------------------------------------------------------- about
def render_about():
    body = f"""
<section class="page-hero"><div class="wrap page-hero-grid">
  <div>
    <div class="breadcrumb"><a href="/">Home</a> <span>›</span> <span>About</span></div>
    <h1>Your trusted Orange County appliance experts</h1>
    <p>Fortex Appliance Repair is a local, licensed, family-minded company built on one idea: fix it right, charge fairly, and treat every home with respect.</p>
    <div class="hero-cta">
      <a class="btn btn--primary btn--lg" href="/book/">{icon('calendar', size=20)} Book a Repair</a>
      <a class="btn btn--outline btn--lg" href="{SITE['phone_href']}">{icon('phone', size=20)} {esc(SITE['phone'])}</a>
    </div>
  </div>
  <div class="media reveal">{img('tech-portrait', sizes='(max-width:1000px) 90vw, 460px', loading='eager')}</div>
</div></section>
{trust_strip()}
<section class="section"><div class="wrap">
  <div class="prose" style="max-width:760px;margin-inline:auto">
    <p class="eyebrow">Our story</p>
    <h2>Built on honest, reliable service</h2>
    <p>We started Fortex Appliance Repair to do appliance service the way it should be done. No call-center runaround, no inflated quotes, no mystery fees — just experienced technicians who show up on time, diagnose honestly, and stand behind their work.</p>
    <p>Today we've completed more than 2,000 repairs across Orange County and earned a 5.0-star reputation on Yelp and Google. We repair every major brand, from everyday Whirlpool and Samsung units to high-end Sub-Zero and Viking built-ins.</p>
    <p>Whether it's a fridge that quit on a Saturday or a dryer that's been slow for weeks, our goal is the same: get your home running again quickly, and earn a customer for life.</p>
  </div>
</div></section>
{why_split('tech-arrival', heading='What we stand for')}
{stats_band()}
{reviews_section()}
{cta_band()}
"""
    return "/about/index.html", page(
        f"About Us | {SITE['name']}",
        "Fortex Appliance Repair is a licensed, insured, 5-star appliance repair company serving Orange County, CA with 2,000+ completed repairs. Honest pricing, warrantied work.",
        "/about/", body, og_image="tech-portrait",
    )


# ----------------------------------------------------------------- reviews
def render_reviews():
    cards = "".join(review_card(r) for r in REVIEWS)
    body = f"""
<section class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="/">Home</a> <span>›</span> <span>Reviews</span></div>
  <h1>5.0 Stars Across Orange County</h1>
  <p>We've earned 101 five-star reviews on Yelp and a 5.0 rating on Google by doing right by our customers — every visit, every time.</p>
  <div class="rating-summary" style="justify-content:flex-start">
    <span class="rating-pill">{stars()} <b>5.0</b> on Yelp · 101 reviews</span>
    <span class="rating-pill">{stars()} <b>5.0</b> on Google</span>
  </div>
</div></section>
<section class="section"><div class="wrap">
  <div class="reviews">{cards}</div>
  <div class="center" style="margin-top:32px;display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
    <a class="btn btn--outline" href="{SITE['yelp_url']}" target="_blank" rel="noopener nofollow">{stars()} Read all 101 on Yelp</a>
    <a class="btn btn--outline" href="{SITE['google_url']}" target="_blank" rel="noopener nofollow">{stars()} See our Google reviews</a>
  </div>
</div></section>
{brand_strip()}
{cta_band()}
"""
    review_schema = {
        "@context": "https://schema.org", "@type": "HVACBusiness",
        "name": SITE["name"], "@id": SITE["url"] + "/#business",
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "5.0", "reviewCount": "100"},
        # No "review" array on purpose. These are Yelp reviews, and Google's
        # structured-data policy forbids marking up reviews sourced from
        # third-party sites; the entries also have no author name, which makes
        # Review markup invalid. The reviews still render as normal HTML.
    }
    return "/reviews/index.html", page(
        f"Reviews | {SITE['name']}",
        "Read 5-star reviews for Fortex Appliance Repair from homeowners across Orange County. 101 five-star Yelp reviews and a 5.0 Google rating.",
        "/reviews/", body, extra_schema=review_schema,
    )


# ----------------------------------------------------------------- booking
def render_book():
    appls = ""
    for label, ic in BOOKING_APPLIANCES:
        appls += f"""<label class="choice">{icon(ic, size=26)}<span>{esc(label)}</span>
  <input type="radio" name="appliance" value="{esc(label)}" required></label>"""
    body = f"""
<section class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="/">Home</a> <span>›</span> <span>Book Online</span></div>
  <h1>Book Your Repair</h1>
  <p>Tell us what's going on and we'll confirm your same-day or next-day appointment. Takes about 60 seconds — or call <a href="{SITE['phone_href']}" style="color:var(--red);font-weight:700">{esc(SITE['phone'])}</a>.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="booking">
    <form class="form-card" name="booking" method="POST"
          action="{esc(SITE['form_endpoint'])}" data-booking>
      <input type="hidden" name="_next" value="{esc(SITE['url'])}/book/thank-you/">
      <input type="hidden" name="_subject" value="New booking request — fortexappliancerepair.com">
      <p class="hp"><label>Don't fill this out: <input name="_gotcha" tabindex="-1" autocomplete="off"></label></p>

      <div class="field">
        <label>Which appliance needs repair? <span class="req">*</span></label>
        <div class="choice-grid">{appls}</div>
      </div>
      <div class="field">
        <label for="issue">What's the problem? <span class="req">*</span></label>
        <textarea id="issue" name="issue" placeholder="e.g. Refrigerator isn't cooling and is making a buzzing noise" required></textarea>
      </div>
      <div class="field-row">
        <div class="field"><label for="name">Your name <span class="req">*</span></label>
          <input id="name" name="name" autocomplete="name" required></div>
        <div class="field"><label for="phone">Phone <span class="req">*</span></label>
          <input id="phone" name="phone" type="tel" autocomplete="tel" required></div>
      </div>
      <div class="field-row">
        <div class="field"><label for="city">City</label>
          <input id="city" name="city" autocomplete="address-level2" placeholder="Irvine"></div>
        <div class="field"><label for="zip">ZIP code</label>
          <input id="zip" name="zip" inputmode="numeric" autocomplete="postal-code" placeholder="92602"></div>
      </div>
      <div class="field-row">
        <div class="field"><label for="day">Preferred day</label>
          <select id="day" name="preferred_day">
            <option>As soon as possible</option><option>Today</option><option>Tomorrow</option>
            <option>This week</option><option>Specific date (note below)</option></select></div>
        <div class="field"><label for="time">Preferred time</label>
          <select id="time" name="preferred_time">
            <option>Anytime</option><option>Morning (8am–12pm)</option>
            <option>Afternoon (12–4pm)</option><option>Evening (4–8pm)</option></select></div>
      </div>
      <button class="btn btn--primary btn--lg btn--block" type="submit">{icon('calendar', size=20)} Request My Appointment</button>
      <p class="form-note">By submitting you agree to be contacted about your repair. We never share your info.</p>
    </form>

    <aside class="form-aside">
      <div class="aside-card">
        <h3>Why book with Fortex</h3>
        <ul class="aside-list">
          <li>{icon('check-circle', size=20)}<span><strong>Same-day &amp; next-day</strong> appointments across Orange County</span></li>
          <li>{icon('check-circle', size=20)}<span><strong>Free service call</strong> with any completed repair</span></li>
          <li>{icon('check-circle', size=20)}<span><strong>Upfront pricing</strong> — approved before any work begins</span></li>
          <li>{icon('check-circle', size=20)}<span><strong>12-month parts</strong> / 90-day labor warranty</span></li>
          <li>{icon('check-circle', size=20)}<span>Licensed CA #{SITE['license']} &amp; fully insured</span></li>
        </ul>
      </div>
      <div class="aside-card" style="background:#fff;border:1.5px solid var(--line);box-shadow:var(--shadow-sm)">
        <h3>Prefer to call or text?</h3>
        <p style="margin-bottom:16px;font-size:.95rem;color:var(--muted)">We're happy to help and answer your questions.</p>
        <a class="btn btn--primary btn--block" href="{SITE['phone_href']}">{icon('phone', size=18)} {esc(SITE['phone'])}</a>
        <a class="btn btn--outline btn--block" style="margin-top:10px" href="{SITE['sms_href']}">{icon('chat', size=18)} Text Us</a>
      </div>
    </aside>
  </div>
</div></section>
"""
    return "/book/index.html", page(
        f"Book Online | {SITE['name']}",
        "Book your Orange County appliance repair online in 60 seconds. Same-day & next-day appointments, free service call with repair. Or call (949) 479-0089.",
        "/book/", body,
    )


def render_thankyou():
    body = f"""
<section class="section" style="padding-block:clamp(60px,10vw,120px)"><div class="wrap center">
  <div class="ic" style="width:84px;height:84px;border-radius:50%;background:var(--red-tint);color:var(--green);display:grid;place-items:center;margin:0 auto 24px">{icon('check-circle', size=48, stroke=2)}</div>
  <h1>Thank you — request received!</h1>
  <p class="lede" style="margin:16px auto 0">A Fortex team member will call or text you shortly to confirm your appointment. Need immediate help? Call us now.</p>
  <div class="hero-cta" style="justify-content:center;margin-top:30px">
    <a class="btn btn--primary btn--lg" href="{SITE['phone_href']}">{icon('phone', size=20)} {esc(SITE['phone'])}</a>
    <a class="btn btn--outline btn--lg" href="/">Back to Home</a>
  </div>
</div></section>
{reviews_section()}
"""
    return "/book/thank-you/index.html", page(
        f"Thank You | {SITE['name']}",
        "Thanks for your appliance repair request. Fortex will confirm your Orange County appointment shortly.",
        "/book/thank-you/", body,
    )


# NOTE: standard boilerplate — owner should have these reviewed by counsel.
def _legal_page(slug, title, eyebrow, blocks, desc):
    body_blocks = "".join(blocks)
    body = f"""
<section class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="/">Home</a> <span>›</span> <span>{esc(eyebrow)}</span></div>
  <h1>{esc(title)}</h1>
  <p>Last updated: June 2026</p>
</div></section>
<section class="section"><div class="wrap"><div class="prose">{body_blocks}</div></div></section>
"""
    return f"/{slug}/index.html", page(f"{title} | {SITE['name']}", desc, f"/{slug}/", body)


def render_privacy():
    p = SITE["phone"]
    e = SITE["email"]
    blocks = [
        f"<p>Fortex Appliance Repair (“Fortex,” “we,” “us”) respects your privacy. This policy explains what information we collect when you contact us or use this website, and how we use it.</p>",
        "<h2>Information we collect</h2>",
        "<p>We collect the information you provide when you book a repair, request a quote, call, or text us — such as your name, phone number, email address, service address, and details about your appliance and the problem. We also collect basic, non-identifying website analytics (such as pages visited).</p>",
        "<h2>How we use your information</h2>",
        "<ul><li>To schedule, perform, and follow up on your appliance repair</li><li>To contact you about your request, appointment, or estimate</li><li>To improve our services and website</li></ul>",
        "<h2>Text messages</h2>",
        f"<p>If you provide your phone number, we may text you appointment confirmations and arrival updates. Message and data rates may apply. Reply STOP to opt out at any time, or HELP for help. You can also call us at {esc(p)}.</p>",
        "<h2>How we share information</h2>",
        "<p>We do not sell your personal information. We share it only as needed to perform your service (for example, with parts suppliers) or when required by law.</p>",
        "<h2>Your choices</h2>",
        f"<p>You may ask us to review, update, or delete the information we hold about you by emailing <a href=\"mailto:{esc(e)}\">{esc(e)}</a> or calling {esc(p)}.</p>",
        "<h2>Contact us</h2>",
        f"<p>Fortex Appliance Repair · Huntington Beach, CA · {esc(p)} · <a href=\"mailto:{esc(e)}\">{esc(e)}</a></p>",
    ]
    return _legal_page("privacy", "Privacy Policy", "Privacy", blocks,
                       "Fortex Appliance Repair privacy policy — what information we collect and how we use it.")


def render_terms():
    p = SITE["phone"]
    blocks = [
        "<p>These terms govern your use of the Fortex Appliance Repair website and our repair services. By booking a service, you agree to these terms.</p>",
        "<h2>Our services</h2>",
        "<p>Fortex provides residential and commercial appliance repair across Orange County, CA. Every visit begins with a diagnostic to identify the problem and provide a price.</p>",
        "<h2>Estimates &amp; pricing</h2>",
        "<p>We provide an upfront, all-in price before any repair work begins. The service-call fee is waived when you approve and complete the repair. You are responsible for the quoted price only after you approve the work.</p>",
        "<h2>Warranty</h2>",
        "<p>Completed repairs are backed by a 12-month warranty on parts and a 90-day warranty on labor, using original manufacturer parts. The warranty covers the specific repair performed and does not cover new, unrelated faults or damage caused by misuse.</p>",
        "<h2>Payment</h2>",
        "<p>Payment is due upon completion of the repair. We accept major credit cards (Visa, Mastercard, American Express, Discover) and other methods as agreed.</p>",
        "<h2>Scheduling &amp; cancellations</h2>",
        f"<p>Appointment windows are estimates and may shift due to earlier jobs; we'll keep you updated by call or text. To reschedule or cancel, please contact us at {esc(p)} as early as possible.</p>",
        "<h2>Limitation of liability</h2>",
        "<p>To the fullest extent permitted by law, Fortex's liability for any claim related to our services is limited to the amount paid for the specific repair. We are not liable for indirect or consequential damages.</p>",
        "<h2>Governing law</h2>",
        "<p>These terms are governed by the laws of the State of California.</p>",
        "<h2>Contact us</h2>",
        f"<p>Questions about these terms? Call {esc(p)}.</p>",
    ]
    return _legal_page("terms", "Terms of Use", "Terms", blocks,
                       "Fortex Appliance Repair terms of use, pricing, and warranty terms.")


def render_404():
    body = f"""
<section class="section" style="padding-block:clamp(60px,10vw,120px)"><div class="wrap center">
  <p class="eyebrow">404</p>
  <h1>We couldn't find that page</h1>
  <p class="lede" style="margin:16px auto 0">The page may have moved. Let's get you back on track — or book a repair in 60 seconds.</p>
  <div class="hero-cta" style="justify-content:center;margin-top:30px">
    <a class="btn btn--primary btn--lg" href="/">Back to Home</a>
    <a class="btn btn--outline btn--lg" href="/services/">Browse Services</a>
  </div>
</div></section>
"""
    return "/404.html", page(f"Page Not Found | {SITE['name']}", "Page not found.", "/404.html", body)


# ----------------------------------------------------------------- all pages
def all_pages():
    pages = [
        render_home(), render_services_index(), render_areas_index(),
        render_how(), render_about(), render_reviews(),
        render_book(), render_thankyou(), render_404(),
        render_privacy(), render_terms(),
    ]
    pages += [render_service(s) for s in SERVICES]
    pages += [render_city(c) for c in CITIES]
    return pages
