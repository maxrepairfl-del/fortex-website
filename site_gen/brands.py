"""Brand hub, brand pages and brand x appliance pages.

Prices are typical parts + labor ranges in Orange County (see
docs/цены-unit-brand-2026-11-11.md in fortex-ops-bot). Every page states that
Fortex is an independent service, not affiliated with the manufacturer.
"""
import datetime
import re

from .components import esc, page, faq_block, faq_schema, cta_band, BREADCRUMB_NAMES
from .data import SITE
from .icons import icon
from .images import img
from . import pages as P

INDEPENDENT = ("Fortex Appliance Repair is an independent repair company. We are not "
               "affiliated with, authorized by or endorsed by {maker}. Brand names are "
               "used only to describe the appliances we repair.")

PRICE_NOTE = ("Typical parts + labor in Orange County. You get the exact price after "
              "diagnosis, before any work starts. Service call $80, free with repair.")

# ---------------------------------------------------------------- data
BRAND_PAGES = {
    "sub-zero": {
        "name": "Sub-Zero",
        "maker": "Sub-Zero Group, Inc.",
        "title": "Sub-Zero Repair in Orange County",
        "meta": "Sub-Zero refrigerator, freezer and wine storage repair in Orange County. Built-in, integrated and PRO models. OEM parts, price before work, $80 service call free with repair.",
        "lead": "Built-in, integrated and PRO refrigerators, freezers, wine storage and undercounter units. Sealed-system work, hinges, ice makers and controls, done in your kitchen without pulling the cabinetry apart.",
        "photo": "sz-builtin-sxs",
        "photo_2": "digital-manifold",
        "products": [
            ("refrigerator", "Built-in refrigerators", "Side-by-side, over-and-under and all-refrigerator / all-freezer columns, 36 to 48 inch.", "/services/refrigerator-repair/sub-zero/"),
            ("refrigerator", "Integrated (panel-ready)", "Units hidden behind cabinet panels. We work on them in place and keep the panels aligned.", "/services/refrigerator-repair/sub-zero/"),
            ("wine", "Wine storage", "Full-size and undercounter wine units: zones that drift warm, fans, sensors and seals.", "/services/wine-cooler-repair/"),
            ("freezer", "Freezers, drawers & ice makers", "Undercounter drawers, freezer columns and built-in ice makers.", "/services/freezer-repair/"),
        ],
        "parts_line": "Compressors, control boards, hinge cassettes, gaskets, fan motors and ice maker parts",
        "prices": [
            ("Compressor replacement (dual-refrigeration models)", "$850 – $1,800"),
            ("Condenser or evaporator service", "$520 – $1,100"),
            ("Main control board", "$420 – $880"),
            ("Built-in door hinge & spring cassette", "$280 – $580"),
            ("Ice maker auger motor + solenoid", "$260 – $520"),
            ("Door auto-close cam", "$220 – $440"),
            ("Door or drawer gasket", "$180 – $380"),
            ("Panel-ready door re-alignment", "$160 – $340"),
        ],
        "faqs": [
            ("Is a Sub-Zero worth repairing?",
             "Almost always. A built-in Sub-Zero is designed for a long service life, and most failures are a part, not the whole system. Even a compressor job usually costs a fraction of a new built-in plus the cabinetry work to fit it. We tell you honestly at the diagnosis if a repair does not make sense."),
            ("Are you a Sub-Zero factory-authorized service?",
             "No. We are an independent, licensed repair company. We use original Sub-Zero parts bought from authorized distributors and back our work with 1 year on parts and 90 days on labor. If your unit is still under the factory warranty, use the manufacturer's service first."),
            ("Can you fix a panel-ready unit without damaging the cabinets?",
             "Yes. Panel-ready units are serviced in place. We protect the floor and panels, and re-align the door so the panel sits flush with the cabinetry when we are done."),
            ("Do you carry Sub-Zero parts on the van?",
             "Common parts, yes. Brand-specific parts such as a control board or a hinge cassette are often ordered for your exact model, and we tell you the timing together with the price."),
        ],
        "combos": [("refrigerator-repair", "Sub-Zero refrigerator repair")],
        "product_photos": ["sz-builtin-sxs", "builtin-panel-tech", None, None],
    },
}

COMBO_PAGES = {
    ("sub-zero", "refrigerator-repair"): {
        "noun": "Sub-Zero refrigerator",
        "icon": "refrigerator",
        "h1": "Sub-Zero Refrigerator Repair in Orange County",
        "meta": "Sub-Zero refrigerator not cooling, warm, frosting or the door won't close? Built-in, integrated and PRO repair in Orange County. Prices from $160, $80 service call free with repair.",
        "lead": "Warm fresh-food section, frost in the freezer, a door that will not close on its own or an ice maker that quit. We diagnose built-in, integrated and PRO models in place and give you the full price before any work.",
        "photo": "sz-builtin-sxs",
        "symptoms": [
            "Refrigerator section warm, freezer fine (or the other way round)",
            "Running constantly, or the condenser fan is loud",
            "Frost or ice building up on the back wall",
            "Door won't close by itself or doesn't seal",
            "Ice maker stopped making ice or leaks",
            "Service light or alarm on the control panel",
        ],
        "causes": [
            ("One section warm", "Dirty condenser on top of the unit, evaporator fan, or a failing compressor on dual-refrigeration models", "Clean and check the condenser, test fans and sensors, read sealed-system pressures"),
            ("Runs nonstop", "Condenser blocked by dust, failing condenser fan, low refrigerant", "Check airflow at the top grille, measure current draw and pressures"),
            ("Frost on the back wall", "Defrost heater, defrost sensor or control fault", "Test the defrost circuit and control before replacing anything"),
            ("Door won't self-close", "Worn hinge cassette or auto-close cam, sagging panel", "Replace the cassette or cam, re-align the door and panel"),
            ("No ice / leaking", "Water valve, auger motor, frozen fill tube", "Test the valve and motor, clear and protect the fill line"),
        ],
        "gallery": [
            ("sz-builtin-sxs", "Sub-Zero built-in side-by-side on a service call"),
            ("builtin-panel-tech", "Working inside a panel-ready built-in, in place"),
            ("tg-vitalik-brand-subzero-model-label", "Sub-Zero model and serial label checked before ordering parts"),
            ("gauges-compressor", "Gauges on the compressor to read sealed-system pressures"),
        ],
        "faqs": [
            ("Why is my Sub-Zero refrigerator warm but the freezer is fine?",
             "Many Sub-Zero built-ins have two separate cooling systems, so one section can fail while the other keeps working. The usual causes are a dusty condenser, an evaporator fan or a sensor. Less often it is the compressor for that section. We test it in that order."),
            ("How much does Sub-Zero refrigerator repair cost?",
             "Most repairs fall between $160 and $880: gaskets, hinges, ice maker parts, fans and boards. Sealed-system work, such as a compressor on a dual-refrigeration model, runs $850 to $1,800. You get the exact price before any work starts."),
            ("How often should the condenser be cleaned?",
             "Every 6 to 12 months, more often with pets. On most built-ins the condenser sits behind the top grille. A clogged condenser is one of the most common reasons a Sub-Zero runs warm or nonstop."),
            ("Can you repair it the same day?",
             "Often, yes: cleaning, fans, valves and gaskets are usually same-visit. Model-specific parts like a board or a hinge cassette may need to be ordered, and we tell you the timing with the price."),
        ],
    },
}

from .brand_data import MORE_BRANDS, MORE_COMBOS  # noqa: E402
from .brand_data2 import NEW_BRANDS, NEW_COMBOS  # noqa: E402
BRAND_PAGES.update(MORE_BRANDS)
BRAND_PAGES.update(NEW_BRANDS)
COMBO_PAGES.update(MORE_COMBOS)
COMBO_PAGES.update(NEW_COMBOS)

BREADCRUMB_NAMES.update({"brands": "Brands"})
for _slug, _b in BRAND_PAGES.items():
    BREADCRUMB_NAMES[_slug] = _b["name"]


# ---------------------------------------------------------------- blocks
def _clean(label):
    return re.sub(r"\s*\([^)]*\)", "", label).replace(":", "").strip()


def _range(text):
    nums = [int(x.replace(",", "")) for x in re.findall(r"\$([\d,]+)", text)]
    return (nums[0], nums[-1]) if nums else (None, None)


def price_table(rows, noun, path):
    """Cost table written the way people search ("how much does X cost").

    Placed low on the page. Phrased for searches from anywhere in the U.S.,
    not just Orange County, and mirrored in an OfferCatalog so the ranges are
    machine-readable."""
    year = datetime.date.today().year
    trs = "".join(
        f"<tr><td>{esc(noun)} {esc(_clean(a)[0].lower() + _clean(a)[1:])}</td>"
        f"<td class=\"price\">{esc(b)}</td></tr>" for a, b in rows)
    lo = min(_range(b)[0] for _, b in rows)
    hi = max(_range(b)[1] for _, b in rows)
    cheap, big = rows[-1], rows[0]
    summary = (f"Most {noun} repairs cost between ${lo:,} and ${hi:,} in {year}, parts and labor included. "
               f"For example, {_clean(cheap[0]).lower()} typically runs {cheap[1]}, while "
               f"{_clean(big[0]).lower()} runs {big[1]}. The final price depends on the model "
               f"and what the diagnosis finds.")
    html = f"""<section class="section section--tight price-ref"><div class="wrap">
  <div class="section-head"><h2>How much does {esc(noun)} repair cost? ({year} prices)</h2>
    <p class="lede">{esc(summary)}</p></div>
  <div class="cause-table price-table"><table>
    <thead><tr><th>{esc(noun)} repair</th><th>Typical cost (parts + labor)</th></tr></thead><tbody>{trs}</tbody>
  </table></div>
  <p class="price-ref__note">In Orange County, CA the service call is $80 and free when you go ahead with the repair. You get the exact price before any work starts.</p>
</div></section>"""
    offers = []
    for a, b in rows:
        mn, mx = _range(b)
        offers.append({"@type": "Offer",
                       "itemOffered": {"@type": "Service", "name": f"{noun} {_clean(a).lower()}"},
                       "priceSpecification": {"@type": "PriceSpecification", "priceCurrency": "USD",
                                              "minPrice": mn, "maxPrice": mx}})
    catalog = {"@context": "https://schema.org", "@type": "OfferCatalog",
               "name": f"{noun} repair cost ({year})", "url": SITE["url"] + path,
               "itemListElement": offers}
    return html, catalog


def oem_block(brand, parts_line):
    return f"""<section class="section section--tight"><div class="wrap">
  <div class="oem-note reveal">
    <div class="oem-note__ic">{icon('award', size=28)}</div>
    <div><h3>Original {esc(brand)} parts only</h3>
    <p>{esc(parts_line)}: we install factory (OEM) parts bought from authorized distributors, not cheaper aftermarket copies that can fit poorly or run outside spec. 1 year on parts, 90 days on labor. Still under the manufacturer's warranty? Tell us when you book and we will point you to factory service first.</p></div>
  </div>
</div></section>"""


def hero(crumbs, h1, lead, photo):
    trail = " <span>›</span> ".join(
        f'<a href="{h}">{esc(t)}</a>' if h else f"<span>{esc(t)}</span>" for t, h in crumbs)
    return f"""<section class="page-hero"><div class="wrap page-hero-grid">
  <div>
    <div class="breadcrumb">{trail}</div>
    <h1>{esc(h1)}</h1>
    <p class="hero-lead">{esc(lead)}</p>
    <div class="hero-cta">
      <a class="btn btn--primary btn--lg cta-call" href="{SITE['phone_href']}">{icon('phone', size=20)} Call Now</a>
      <a class="btn btn--outline btn--lg cta-book" href="#request">{icon('calendar', size=20)} Request Appointment</a>
    </div>
    <p class="hero-terms">{icon('dollar', size=18)}<span>{P.DIAGNOSTIC_LEAD_HTML}</span></p>
    <ul class="hero-proof">
      <li><a href="{SITE['yelp_url']}" target="_blank" rel="noopener nofollow">{P.stars()} {SITE['yelp_rating']} on Yelp · {SITE['yelp_reviews']} reviews</a></li>
      <li>{icon('shield-plain', size=17)} Licensed CA #{SITE['license']}</li>
      <li>{icon('award', size=17)} 1 year on OEM parts / 90 days labor</li>
    </ul>
  </div>
  <div class="media reveal">{img(photo, sizes='(max-width:1000px) 90vw, 460px', loading='eager', fetchpriority='high')}</div>
</div></section>"""


def request_form(noun, icon_name, example, path):
    fake = {"noun": noun, "icon": icon_name, "symptoms": [example], "slug": "__x__"}
    return P.service_request_form(fake).replace("/services/__x__/", path)


def independent_note(maker):
    return f"""<section class="section section--tight"><div class="wrap">
  <p class="independent-note">{esc(INDEPENDENT.format(maker=maker))}</p></div></section>"""


def faq_section(title, faqs):
    return f"""<section class="section section--surface"><div class="wrap">
  <div class="section-head center"><p class="eyebrow">FAQ</p><h2>{esc(title)}</h2></div>
  <div style="display:flex;justify-content:center">{faq_block(faqs)}</div>
</div></section>"""


# ---------------------------------------------------------------- pages
def _photo_for(href, b):
    """Photo for a product card: the linked page's own hero photo."""
    from .data import SERVICES_BY_SLUG
    parts = [x for x in href.strip("/").split("/") if x]
    if len(parts) == 3 and parts[0] == "services":
        c = COMBO_PAGES.get((parts[2], parts[1]))
        if c:
            return c["photo"]
    if len(parts) >= 2 and parts[1] in SERVICES_BY_SLUG:
        return SERVICES_BY_SLUG[parts[1]]["photo"]
    return b["photo"]


def render_brand(slug):
    b = BRAND_PAGES[slug]
    path = f"/brands/{slug}/"
    price_html, catalog = price_table(b['prices'], b['name'], path)
    pp = b.get("product_photos") or []
    cards = "".join(P.photo_card(h, pp[i] if i < len(pp) and pp[i] else _photo_for(h, b), t, d)
                    for i, (ic, t, d, h) in enumerate(b["products"]))
    body = f"""
{hero([('Home', '/'), ('Brands', '/brands/'), (b['name'], None)], b['title'], b['lead'], b['photo'])}
<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">What we repair</p><h2>{esc(b['name'])} appliances we work on</h2></div>
  <div class="cards grid-4">{cards}</div>
</div></section>
{oem_block(b['name'], b['parts_line'])}
{request_form(b['name'] + ' appliance', 'wrench', b.get('example', 'not cooling'), path)}
{P.steps_section()}
{P.why_split(b['photo_2'], heading=f"Why {b['name']} owners call Fortex")}
{faq_section(f"{b['name']} repair FAQs", b['faqs'])}
{price_html}
{cta_band(heading=f"Need your {b['name']} repaired?", book_href="#request")}
"""
    schema = {"@context": "https://schema.org", "@type": "Service",
              "serviceType": f"{b['name']} appliance repair",
              "provider": {"@id": SITE["url"] + "/#business"},
              "areaServed": SITE["region"], "name": b["title"]}
    return f"{path}index.html", page(
        f"{b['title']}, CA | {SITE['name']}", b["meta"], path, body,
        extra_schema=[schema, faq_schema(b["faqs"]), catalog], og_image=b["photo"], book_href="#request")


def render_combo(bslug, uslug):
    b, c = BRAND_PAGES[bslug], COMBO_PAGES[(bslug, uslug)]
    from .data import SERVICES_BY_SLUG
    svc = SERVICES_BY_SLUG[uslug]
    path = f"/services/{uslug}/{bslug}/"
    price_html, catalog = price_table(c.get('prices', b['prices']), c['noun'], path)
    symptoms = "".join(f'<li>{icon("check", size=20)}<span>{esc(x)}</span></li>' for x in c["symptoms"])
    causes = P.causes_block({"causes": c["causes"]})
    gallery = P.gallery_block({"gallery": c["gallery"]})
    body = f"""
{hero([('Home', '/'), ('Services', '/services/'), (svc['short'], f'/services/{uslug}/'), (b['name'], None)], c['h1'], c['lead'], c['photo'])}
<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Common problems</p><h2>What we fix on {esc(c['noun'])}s</h2></div>
  <ul class="checks">{symptoms}</ul>
  {P.cta_row('Sound like yours?', 'Same-day appointments may be available. Call to check.', href='#request')}
</div></section>
{request_form(c['noun'], c['icon'], c['symptoms'][0].lower(), path)}
{causes}
{oem_block(b['name'], b['parts_line'])}
{gallery}
{P.steps_section()}
{faq_section(f"{c['noun']} repair FAQs", c['faqs'])}
{price_html}
<section class="section section--tight"><div class="wrap"><p class="center">More {esc(b['name'])}: <a href="/brands/{bslug}/">all {esc(b['name'])} appliances we repair</a> · Other brands: <a href="/services/{uslug}/">{esc(svc['name'].lower())}</a></p></div></section>
{cta_band(heading=f"Need your {c['noun']} fixed?", book_href="#request")}
"""
    schema = {"@context": "https://schema.org", "@type": "Service",
              "serviceType": f"{c['noun']} repair",
              "provider": {"@id": SITE["url"] + "/#business"},
              "areaServed": SITE["region"], "name": c["h1"]}
    return f"{path}index.html", page(
        f"{c['h1']}, CA | {SITE['name']}", c["meta"], path, body,
        extra_schema=[schema, faq_schema(c["faqs"]), catalog], og_image=c["photo"], book_href="#request")


def render_brands_index():
    cards = "".join(
        P.photo_card(f"/brands/{s}/", b.get("card_photo", b["photo"]), b["name"],
                     b["lead"][:120].rsplit(" ", 1)[0] + "…", more=f"{b['name']} repair")
        for s, b in BRAND_PAGES.items())
    body = f"""
<section class="page-hero page-hero--simple"><div class="wrap">
  <div class="breadcrumb"><a href="/">Home</a> <span>›</span> <span>Brands</span></div>
  <h1>High-End &amp; Built-In Appliance Repair by Brand</h1>
  <p class="hero-lead">Prices, common problems and what to expect for the brands we work on most. We repair every major brand, these are the ones with their own page.</p>
</div></section>
<section class="section"><div class="wrap"><div class="cards grid-4">{cards}</div></div></section>
{P.steps_section()}
{cta_band()}
"""
    return "/brands/index.html", page(
        f"Appliance Repair by Brand, Orange County | {SITE['name']}",
        "Sub-Zero, Wolf, Viking, Thermador, LG and more: repair prices, common problems and OEM parts. Independent repair across Orange County.",
        "/brands/", body)


def brand_pages():
    out = [render_brands_index()]
    out += [render_brand(s) for s in BRAND_PAGES]
    out += [render_combo(b, u) for (b, u) in COMBO_PAGES]
    return out


def brand_links(uslug):
    """'By brand' block for a service page: links to its brand subpages."""
    items = [(b, BRAND_PAGES[b]) for (b, u) in COMBO_PAGES if u == uslug]
    if not items:
        return ""
    links = "".join(
        f'<a class="brand-chip" href="/services/{uslug}/{b}/">{esc(d["name"])}</a>' for b, d in items)
    return f"""<section class="section section--tight"><div class="wrap">
  <div class="section-head"><p class="eyebrow">By brand</p><h2>Repair by brand</h2>
    <p class="lede">Common problems and typical prices for specific brands.</p></div>
  <div class="brand-chips">{links}</div>
</div></section>"""
