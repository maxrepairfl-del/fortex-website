"""/our-work/ (photo proof from real jobs) and the single /areas/ page.

The six city pages were folded into /areas/ on 2026-11-12: they were near
duplicates of each other. Their URLs 301 to /areas/ (vercel.json).
"""
from .components import esc, page, cta_band, trust_strip, coverage_map
from .data import SITE, SERVICES_BY_SLUG
from .icons import icon
from . import media
from . import pages as P

# ---------------------------------------------------------------- areas
# Cities and the neighborhoods / communities inside them. Orange County first,
# then the nearby LA County cities we also take calls from.
AREA_GROUPS = [
    ("Irvine", "Woodbridge, Northwood, Turtle Rock, University Park, Quail Hill, Portola Springs, Great Park, Orchard Hills, Woodbury, Cypress Village, Stonegate, Westpark, Shady Canyon"),
    ("Newport Beach", "Corona del Mar, Newport Coast, Balboa Island, Balboa Peninsula, Lido Isle, Eastbluff, Westcliff, Bayshores"),
    ("Huntington Beach", "Huntington Harbour, Seacliff, Downtown, Sunset Beach"),
    ("Costa Mesa", "Mesa Verde, Eastside, College Park"),
    ("Fountain Valley", "Green Valley, Mile Square"),
    ("Santa Ana", "Floral Park, French Park, Park Santiago, Riverview West"),
    ("Tustin", "Tustin Ranch, Tustin Legacy, North Tustin, Lemon Heights, Cowan Heights"),
    ("Orange", "Old Towne, Orange Park Acres, Villa Park, Orange Hills"),
    ("Anaheim", "Anaheim Hills, Platinum Triangle, West Anaheim"),
    ("Yorba Linda", "Vista del Verde, Bryant Ranch"),
    ("Fullerton", "Sunny Hills, Raymond Hills, Golden Hill"),
    ("Brea, Placentia, La Habra", "Olinda Ranch, Brea Hills"),
    ("Buena Park, Cypress, La Palma", "Lincoln Village"),
    ("Garden Grove, Westminster, Stanton", "Midway City, West Garden Grove"),
    ("Seal Beach, Los Alamitos", "Rossmoor, College Park East, Leisure World"),
    ("Lake Forest", "Foothill Ranch, Portola Hills"),
    ("Mission Viejo", "Lake Mission Viejo, Pacific Hills"),
    ("Laguna Niguel, Laguna Hills, Laguna Woods", "Bear Brand Ranch, Rancho Niguel"),
    ("Aliso Viejo", "Glenwood, Pacific Park"),
    ("Laguna Beach", "Three Arch Bay, Emerald Bay, Top of the World, Arch Beach Heights"),
    ("Rancho Santa Margarita", "Dove Canyon, Robinson Ranch, Rancho Trabuco"),
    ("Ladera Ranch, Coto de Caza, Rancho Mission Viejo", "Las Flores, Trabuco Canyon, Wagon Wheel"),
    ("San Juan Capistrano", "Capistrano Valley, San Juan Hills"),
    ("Dana Point", "Monarch Beach, Capistrano Beach, Lantern Village"),
    ("San Clemente", "Talega, Forster Ranch, Sea Summit"),
    ("Nearby in LA County", "Long Beach, Lakewood, Cerritos, Hawaiian Gardens (call to check the day's schedule)"),
]

ALL_CITY_NAMES = [n.strip() for g, _ in AREA_GROUPS[:-1] for n in g.split(",")]


def area_chips():
    """Short city list for the home page, linking to the full /areas/ page."""
    names = ["Irvine", "Newport Beach", "Huntington Beach", "Costa Mesa", "Santa Ana", "Tustin",
             "Orange", "Anaheim", "Yorba Linda", "Fullerton", "Mission Viejo", "Laguna Niguel",
             "Lake Forest", "Fountain Valley", "Laguna Beach", "San Clemente"]
    chips = "".join(f"<span>{esc(n)}</span>" for n in names)
    return f"""<div class="area-chips">{chips}</div>
  <div class="center" style="margin-top:22px"><a class="btn btn--outline" href="/areas/">Every city and neighborhood we cover {icon('arrow-right', size=16)}</a></div>"""


def render_areas():
    groups = "".join(
        f'<div class="area-group"><h3>{esc(g)}</h3><p>{esc(n)}</p></div>' for g, n in AREA_GROUPS)
    body = f"""
<section class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="/">Home</a> <span>›</span> <span>Service Areas</span></div>
  <h1>Where We Work: Orange County, CA</h1>
  <p class="hero-lead">Our technicians drive to you across all of Orange County, from Seal Beach to San Clemente, with same-day and next-day appointments. The same prices and the same warranty everywhere: $80 service call, free with repair.</p>
  <div class="hero-cta">
    <a class="btn btn--primary btn--lg cta-call" href="{SITE['phone_href']}">{icon('phone', size=20)} {esc(SITE['phone'])}</a>
    <a class="btn btn--outline btn--lg cta-book" href="/book/">{icon('calendar', size=20)} Book a Repair</a>
  </div>
</div></section>
<section class="section"><div class="wrap">
  <div class="map-solo">{coverage_map()}</div>
</div></section>
<section class="section section--surface"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Cities &amp; neighborhoods</p>
    <h2>Every area we cover</h2>
    <p class="lede">Don't see your neighborhood? Call or text. If it's in Orange County, we almost certainly come to you.</p></div>
  <div class="area-groups">{groups}</div>
</div></section>
{trust_strip()}
{cta_band()}
"""
    schema = {"@context": "https://schema.org", "@type": "Service",
              "serviceType": "Appliance repair", "provider": {"@id": SITE["url"] + "/#business"},
              "areaServed": [{"@type": "City", "name": n} for n in ALL_CITY_NAMES]}
    return "/areas/index.html", page(
        f"Appliance Repair Service Areas in Orange County | {SITE['name']}",
        "Same-day appliance repair in every Orange County city: Irvine, Newport Beach, Huntington Beach, Costa Mesa, Santa Ana, Anaheim, Mission Viejo, San Clemente and more. Call (949) 478-0089.",
        "/areas/", body, extra_schema=[schema])


# ---------------------------------------------------------------- our work
WORK_ORDER = ["refrigerator-repair", "freezer-repair", "washing-machine-repair", "dryer-repair",
              "dishwasher-repair", "oven-repair", "stove-cooktop-repair", "microwave-repair",
              "ice-machine-repair", "commercial-freezer-repair", "wine-cellar-cooling-repair"]


def render_our_work():
    groups = ""
    for slug in WORK_ORDER:
        s = SERVICES_BY_SLUG[slug]
        items = s.get("gallery") or []
        if not items:
            continue
        shots = "".join(
            f'<figure class="job-shot reveal">{P.img(ph, sizes="(max-width:700px) 46vw, 280px")}'
            f'<figcaption>{esc(cap)}</figcaption></figure>' for ph, cap in items)
        groups += f"""<div class="work-group">
  <div class="work-group__head"><h2>{esc(s['short'])}</h2>
    <a class="more-link" href="/services/{slug}/">{esc(s['name'])} {icon('arrow-right', size=16)}</a></div>
  <div class="job-gallery">{shots}</div>
</div>"""
    team = "".join(
        f'<figure class="job-shot reveal">{P.img(media.slug(p), sizes="(max-width:700px) 46vw, 280px")}'
        f'<figcaption>{esc(c)}</figcaption></figure>' for p, c in media.TEAM)
    body = f"""
<section class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="/">Home</a> <span>›</span> <span>Our Work</span></div>
  <h1>Our Work: Real Repairs in Orange County Homes</h1>
  <p class="hero-lead">Every photo on this page was taken by our technicians on real service calls. No stock images. Frozen evaporators, burned-out igniters, lint-packed dryers and the fixes that followed.</p>
</div></section>
<section class="section"><div class="wrap">{groups}
<div class="work-group"><div class="work-group__head"><h2>The team</h2>
  <a class="more-link" href="/about/">About Fortex {icon('arrow-right', size=16)}</a></div>
  <div class="job-gallery">{team}</div></div>
</div></section>
{P.steps_section()}
{cta_band()}
"""
    return "/our-work/index.html", page(
        f"Our Work: Real Appliance Repair Photos | {SITE['name']}",
        "Photos from real Fortex service calls across Orange County: refrigerators, washers, dryers, ovens, ranges, ice machines and wine cellars. No stock images.",
        "/our-work/", body, og_image=media.slug(media.TEAM[0][0]))
