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
from .images import img, is_portrait
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
        "lead": "Built-in, integrated and PRO refrigerators, freezers, wine storage and undercounter units. Sealed-system work, hinges, ice makers and controls, many done in place, some with the unit pulled out.",
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
             "Yes. Many repairs are done in place; some need the unit pulled out. Either way we protect the floor and panels, and re-align the door so the panel sits flush with the cabinetry when we are done."),
            ("Do you carry Sub-Zero parts on the van?",
             "Common parts, yes. Brand-specific parts such as a control board or a hinge cassette are often ordered for your exact model, and we tell you the timing together with the price."),
        ],
        "combos": [("refrigerator-repair", "Sub-Zero refrigerator repair")],
        "product_photos": ["sz-builtin-sxs", "builtin-panel-tech", None, None],
    },
}

SUBZERO_PRICES = [
    ("Dual-compressor sealed-system work", "$850 – $1,800"),
    ("Condenser / evaporator service", "$520 – $1,100"),
    ("Main control board", "$420 – $880"),
    ("Built-in door hinge and spring cassette", "$280 – $580"),
    ("Ice maker auger motor and solenoid", "$260 – $520"),
    ("Door auto-close cam", "$220 – $440"),
    ("Drawer gasket / door seal", "$180 – $380"),
    ("Panel-ready door realignment", "$160 – $340"),
]
BRAND_PAGES["sub-zero"]["prices"] = [("Refrigerator", SUBZERO_PRICES)]
BRAND_PAGES["sub-zero"]["photo"] = "sub-zero-built-in-refrigerator-overview-l302"
# Owner brief 2026-11-23: on Sub-Zero the appliance types are compact text
# cards (no photo, no icon panel). Installation type and door finish describe
# the same appliance, so built-in and panel-ready are not separate cards.
# Only this brand uses the text variant; the others keep their photo cards.
BRAND_PAGES["sub-zero"]["text_products"] = {
    "intro": "We service stainless-steel and panel-ready Sub-Zero appliances. Find your appliance type below.",
    "cards": [
        ("Refrigerators & freezers",
         "Built-in and integrated refrigerators and freezers, including stainless-steel and panel-ready models, separate columns and PRO models.",
         "Sub-Zero refrigerator repair", "/services/refrigerator-repair/sub-zero/"),
        ("Wine storage",
         "Full-size and undercounter wine storage units. We diagnose temperature problems, fan faults, sensors and door seals.",
         "Wine cooler repair", "/services/wine-cooler-repair/"),
        ("Undercounter units & drawers",
         "Undercounter refrigerators, freezer units and refrigeration drawers. We also repair ice makers built into Sub-Zero refrigerators.",
         None, None),
    ],
    "cta": "Not sure which type you have? Tell us what is happening and we will help.",
    "button": "Request Sub-Zero service",
}

COMBO_PAGES = {
    # Sample high-end landing page (owner's brief of 2026-11-13). Layout v2:
    # hero -> request -> models -> problems with photo -> trust/steps/area ->
    # FAQ -> estimated prices -> final call.
    ("sub-zero", "refrigerator-repair"): {
        "v2": True,
        "noun": "Sub-Zero refrigerator",
        "icon": "refrigerator",
        "h1": "Sub-Zero Refrigerator Repair in Orange County",
        "meta": "Sub-Zero built-in refrigerator repair in Orange County: warm sections, frost, doors that won't close, ice makers. $80 service call, free with repair. Price agreed before work.",
        "lead": "Built-in, integrated (panel-ready) and PRO Sub-Zero refrigerators, repaired in your kitchen. We find the cause first and agree the repair price with you before any work starts.",
        "photo": "sub-zero-built-in-refrigerator-overview-l302",
        # (series, model families, what it is, common repairs). Series names and
        # model families are Sub-Zero's own public product lines.
        "types": [
            ("Classic built-in", "BI-36 · BI-42 · BI-48 · CL series",
             "The stainless built-ins most kitchens have: side-by-side, over-and-under and French door, 36 to 48 inches wide.",
             "Condenser and evaporator fans, defrost, door gaskets, ice makers, control boards"),
            ("PRO 48", "PRO4850 · PRO4850G",
             "The 48-inch professional-style model with a heavy stainless exterior and a glass-door option.",
             "Compressor and sealed system, control board, ice maker, condenser fan"),
            ("Designer & integrated columns", "IC-30 · IC-36 · DEC · DET",
             "Panel-ready refrigerator and freezer columns that sit flush behind cabinet panels, single or paired.",
             "Hinges and auto-close cams, panel realignment, drawer rails, ice makers"),
            ("Undercounter & drawers", "UC-24 · DEU",
             "24-inch undercounter refrigerators, freezers and refrigerator drawers.",
             "Compressor, fan motors, drawer slides, door seals"),
        ],
        "symptoms": ["Refrigerator section warm"],
        "problems": [
            ("Refrigerator warm, freezer fine (or the reverse)",
             "Many Sub-Zero built-ins have two separate cooling systems, so one side can fail alone.",
             "We check the condenser and fans first, then sensors, then the sealed system for that section."),
            ("Running nonstop or loud",
             "Usually a dusty condenser behind the top grille or a failing condenser fan.",
             "We check airflow at the grille and the fan before anything bigger."),
            ("Frost on the back wall",
             "Points to the defrost circuit: heater, sensor or control.",
             "We test the defrost circuit before replacing parts."),
            ("Door won't close by itself",
             "Worn hinge cassette or auto-close cam, or a heavy panel that has dropped.",
             "We replace the worn part and realign the door and panel."),
            ("Ice maker stopped or leaks",
             "Water valve, auger motor or a frozen fill tube.",
             "We test the valve and motor and clear the fill line."),
        ],
        # No photo beside the problems (owner 2026-11-23): the panel-ready
        # work shot is a poor angle and there is no better Sub-Zero frame yet.
        "problem_photo": None,
        "prices": SUBZERO_PRICES,
        # (how often, what, why). Intervals follow Sub-Zero's own use & care
        # guidance.
        "care": [
            ("Every month", "Wipe the door gaskets with warm, soapy water",
             "Sticky or dirty gaskets stop sealing, and warm air gets in."),
            ("Every 6 months", "Clean the condenser behind the top grille",
             "Dust on the condenser is the most common reason a Sub-Zero runs warm or nonstop. More often with pets."),
            ("Every 6 months", "Replace the water filter",
             "Or when the filter light comes on. An old filter slows the ice maker and the dispenser."),
            ("Once a year", "Replace the air purification cartridge",
             "On models that have one. The control panel reminds you when it is due."),
        ],
        "faqs": [
            ("Why is my Sub-Zero refrigerator warm but the freezer is fine?",
             "Many Sub-Zero built-ins have two separate cooling systems, so one section can fail while the other keeps working. The usual causes are a dusty condenser, an evaporator fan or a sensor. Less often it is the compressor for that section. We check in that order."),
            ("How much does Sub-Zero refrigerator repair cost?",
             "It depends on the model and what the diagnosis finds. The estimated ranges for common Sub-Zero repairs are listed at the bottom of this page. The service call is $80 and free with repair, and we confirm the total before any work begins."),
            ("Can you repair a panel-ready unit without damaging the cabinets?",
             "Yes. Many repairs are done in place; some need the unit pulled out. Either way we protect the floor and panels and realign the door so the panel sits flush when we are done."),
            ("Are you a Sub-Zero factory-authorized service?",
             "No. We are an independent, licensed repair company. If your unit is still under the factory warranty, use the manufacturer's service first."),
            ("How often should the condenser be cleaned?",
             "Every 6 to 12 months, more often with pets. On most built-ins the condenser sits behind the top grille, and a clogged condenser is a common reason a Sub-Zero runs warm or nonstop."),
        ],
    },
}

from .brand_data import MORE_BRANDS, MORE_COMBOS  # noqa: E402
from .brand_data2 import NEW_BRANDS, NEW_COMBOS  # noqa: E402
BRAND_PAGES.update(MORE_BRANDS)
BRAND_PAGES.update(NEW_BRANDS)
COMBO_PAGES.update(MORE_COMBOS)
COMBO_PAGES.update(NEW_COMBOS)
from .brand_data3 import NEW_BRANDS3, NEW_COMBOS3  # noqa: E402
BRAND_PAGES.update(NEW_BRANDS3)
COMBO_PAGES.update(NEW_COMBOS3)

BREADCRUMB_NAMES.update({"brands": "Brands"})
for _slug, _b in BRAND_PAGES.items():
    BREADCRUMB_NAMES[_slug] = _b["name"]


# ---------------------------------------------------------------- blocks
def _clean(label):
    return re.sub(r"\s*\([^)]*\)", "", label).replace(":", "").strip()


def _range(text):
    nums = [int(x.replace(",", "")) for x in re.findall(r"\$([\d,]+)", text)]
    return (nums[0], nums[-1]) if nums else (None, None)


PRICE_FOOTNOTE = ("Estimated repair ranges are a guide. Your final quote depends on the appliance "
                  "model, parts required and diagnostic findings. We confirm the total before work "
                  "begins. Service call: $80, free with repair.")


def price_table(rows, noun, path, maintenance=None):
    """Estimated repair ranges, low on the page (after the FAQ).

    Plain visible HTML, mirrored in an OfferCatalog with the same numbers. No
    "most repairs cost X-Y" summary: the rows are reference ranges, not
    statistics of our own completed jobs.

    `rows` is a flat list of (repair, range) for a single-appliance page, or a
    list of (appliance, rows) groups for a brand page covering several
    appliances, so every row says which appliance it belongs to (owner
    package 2026-11-21, section 9)."""
    year = datetime.date.today().year
    groups = rows if rows and isinstance(rows[0][1], list) else [(None, rows)]

    def table(rs):
        trs = "".join(f"<tr><td>{esc(a)}</td><td class=\"price\">{esc(b)}</td></tr>" for a, b in rs)
        return f"""<div class="cause-table price-table"><table>
    <thead><tr><th>Repair</th><th>Estimated range</th></tr></thead><tbody>{trs}</tbody>
  </table></div>"""
    body = "".join(
        (f'<h3 class="price-ref__sub">{esc(g)} repair estimates</h3>' if g else "") + table(rs)
        for g, rs in groups)
    maint_html = ""
    if maintenance:
        mrows = "".join(
            f"<tr><td><strong>{esc(t)}</strong><span class=\"price-ref__desc\">{esc(d)}</span></td>"
            f"<td class=\"price\">${p}</td></tr>" for t, p, d in maintenance)
        maint_html = f"""
  <h3 class="price-ref__sub">{esc(noun)} maintenance</h3>
  <div class="cause-table price-table"><table>
    <thead><tr><th>Service</th><th>Fixed price</th></tr></thead><tbody>{mrows}</tbody>
  </table></div>
  <p class="price-ref__note">Maintenance is a flat price, booked on its own. No diagnostic fee.</p>"""
    html = f"""<section class="section section--tight price-ref" id="repair-costs"><div class="wrap">
  <div class="section-head"><h2>Estimated {esc(noun)} repair costs</h2></div>
  {body}
  <p class="price-ref__note">{esc(PRICE_FOOTNOTE)}</p>{maint_html}
</div></section>"""
    offers = []
    for g, rs in groups:
        for a, b in rs:
            mn, mx = _range(b)
            name = f"{noun} {g.lower()} {_clean(a).lower()}" if g else f"{noun} {_clean(a).lower()}"
            offers.append({"@type": "Offer",
                           "itemOffered": {"@type": "Service", "name": name},
                           "priceSpecification": {"@type": "PriceSpecification", "priceCurrency": "USD",
                                                  "minPrice": mn, "maxPrice": mx}})
    catalog = {"@context": "https://schema.org", "@type": "OfferCatalog",
               "name": f"Estimated {noun} repair costs ({year})", "url": SITE["url"] + path,
               "itemListElement": offers}
    for t, p, _d in maintenance or []:
        offers.append({"@type": "Offer", "price": p, "priceCurrency": "USD",
                       "itemOffered": {"@type": "Service", "name": f"{noun} {t.lower()}"}})
    return html, catalog


# Parts named on a brand x appliance page are the parts of THAT appliance, not
# the brand's whole range (audit 2026-11-16, A03).
UNIT_PARTS = {
    "refrigerator-repair": "Compressors, fan motors, sensors, defrost parts, door gaskets and ice maker parts",
    "washing-machine-repair": "Drain pumps, inlet valves, door locks, suspension parts, bearings and control boards",
    "dryer-repair": "Heating elements, thermal fuses, thermostats, belts, drum rollers, gas igniters and control boards",
    "stove-cooktop-repair": "Burner valves, igniters, spark modules, oven sensors, fan motors and control boards",
}


def parts_for(bslug, uslug):
    c = COMBO_PAGES[(bslug, uslug)]
    return c.get("parts_line") or UNIT_PARTS.get(uslug) or BRAND_PAGES[bslug]["parts_line"]


PRICE_FAQ = ("It depends on the model and what the diagnosis finds. Estimated ranges for common {noun} repairs "
             "are listed at the bottom of this page. The service call is $80 and free with repair, and we "
             "confirm the total before any work begins.")


def _faqs(faqs, noun):
    """Price questions point to the estimate table instead of quoting a 'most repairs' range."""
    return [(q, PRICE_FAQ.format(noun=noun) if q.lower().startswith("how much") else a) for q, a in faqs]


def oem_block(brand, parts_line):
    return f"""<section class="section section--tight"><div class="wrap">
  <div class="oem-note reveal">
    <div class="oem-note__ic">{icon('award', size=28)}</div>
    <div><h3>Original {esc(brand)} parts first, your budget in mind</h3>
    <p>{esc(parts_line)}: we prefer factory (OEM) parts bought from authorized distributors. You come first, though: when a lower-cost aftermarket part would do the job without losing quality, we will offer it, explain the difference, and you decide. 1 year on OEM parts, 90 days on labor. Warranty terms for any aftermarket option are explained before you approve the repair.</p></div>
  </div>
</div></section>"""


def hero(crumbs, h1, lead, photo, portrait=False):
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
    <p class="hero-terms">{icon('dollar', size=18)}<span>{P.DIAGNOSTIC_LEAD_HTML} The repair price is agreed with you before work starts. <a href="#repair-costs">See estimated repair costs</a></span></p>
    <ul class="hero-proof">
      <li><a href="{SITE['yelp_url']}" target="_blank" rel="noopener nofollow">{P.stars()} {SITE['yelp_rating']} on Yelp · {SITE['yelp_reviews']} reviews</a></li>
      <li>{icon('shield-plain', size=17)} Licensed CA #{SITE['license']}</li>
      <li>{icon('award', size=17)} 1 year on OEM parts / 90 days labor</li>
    </ul>
  </div>
  <div class="media{' media--portrait' if (portrait or is_portrait(photo)) else ''} reveal">{img(photo, sizes='(max-width:1000px) 80vw, 400px', loading='eager', fetchpriority='high')}</div>
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
        if c and c["photo"] != "tech-portrait":
            return c["photo"]
    # A general service page's hero shows some other brand's appliance: on a
    # brand page that card gets an icon instead of a wrong-brand photo
    # (owner, 2026-11-21: F&P refrigerator and range cards).
    return None


def render_brand(slug):
    b = BRAND_PAGES[slug]
    path = f"/brands/{slug}/"
    price_html, catalog = price_table(b['prices'], b['name'], path)
    pp = b.get("product_photos") or []
    tp = b.get("text_products")
    if tp:
        tcards = "".join(
            f'<div class="type-card"><h3>{esc(t)}</h3><p>{esc(d)}</p>'
            + (f'<a class="more-link" href="{h}">{esc(lbl)} {icon("arrow-right", size=16)}</a>' if h else "")
            + "</div>" for t, d, lbl, h in tp["cards"])
        products_html = f"""<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">What we repair</p><h2>{esc(b['name'])} appliances we repair</h2>
    <p class="lede">{esc(tp['intro'])}</p></div>
  <div class="type-cards">{tcards}</div>
  <div class="type-cta"><p>{esc(tp['cta'])}</p>
    <a class="btn btn--primary" href="#request">{icon('calendar', size=18)} {esc(tp['button'])}</a></div>
</div></section>"""
    else:
        cards = "".join(P.photo_card(h, pp[i] if i < len(pp) and pp[i] else _photo_for(h, b), t, d, ic=ic)
                        for i, (ic, t, d, h) in enumerate(b["products"]))
        products_html = f"""<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">What we repair</p><h2>{esc(b['name'])} appliances we work on</h2></div>
  <div class="cards grid-4">{cards}</div>
</div></section>"""
    body = f"""
{hero([('Home', '/'), ('Brands', '/brands/'), (b['name'], None)], b['title'], b['lead'], b['photo'])}
{products_html}
{problems_section(b['problems_noun'], b['problems'], None) if b.get('problems') else ''}
{oem_block(b['name'], b['parts_line'])}
{request_form(b['name'] + ' appliance', 'wrench', b.get('example', 'not cooling'), path)}
{P.steps_section()}
{P.why_split(b['photo_2'], heading=f"Why {b['name']} owners call Fortex")}
{faq_section(f"{b['name']} repair FAQs", _faqs(b['faqs'], b['name']))}
{price_html}
{cta_band(heading=f"Need your {b['name']} repaired?", book_href="#request")}
"""
    schema = {"@context": "https://schema.org", "@type": "Service",
              "serviceType": f"{b['name']} appliance repair",
              "provider": {"@id": SITE["url"] + "/#business"},
              "areaServed": SITE["region"], "name": b["title"]}
    return f"{path}index.html", page(
        f"{b['title']}, CA | {SITE['name']}", b["meta"], path, body,
        extra_schema=[schema, faq_schema(_faqs(b["faqs"], b["name"])), catalog], og_image=b["photo"], book_href="#request")


def types_section(noun, types):
    cards = "".join(
        f'''<div class="model-card reveal"><h3>{esc(t)}</h3><p class="model-card__codes">{esc(codes)}</p>
  <p>{esc(d)}</p><p class="model-card__fix"><strong>Common repairs:</strong> {esc(fix)}</p></div>'''
        for t, codes, d, fix in types)
    return f"""<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Models we service</p><h2>{esc(noun.split()[0])} models we repair</h2>
    <p class="lede">Every built-in Sub-Zero line. Many repairs are done in place; some need the unit pulled out. Wine storage has <a href="/services/wine-cooler-repair/">its own page</a>.</p></div>
  <div class="model-grid">{cards}</div>
</div></section>"""


def problems_section(noun, problems, photo):
    items = "".join(
        f'<li class="problem reveal"><h3>{esc(t)}</h3><p>{esc(cause)}</p><p class="problem__do">{esc(do)}</p></li>'
        for t, cause, do in problems)
    fig = ""
    if photo:
        fig = (f'<figure class="problems__photo reveal">{img(photo[0], sizes="(max-width:900px) 70vw, 340px")}'
               f'<figcaption>{esc(photo[1])}</figcaption></figure>')
    return f"""<section class="section section--surface"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Common problems</p><h2>What usually goes wrong on a {esc(noun)}</h2></div>
  <div class="problems{' problems--photo' if photo else ''}"><ul class="problems__list">{items}</ul>{fig}</div>
  {P.cta_row('Sound like yours?', 'Call, or leave your number and we will call you back.', href='#request')}
</div></section>"""


def care_section(noun, care):
    rows = "".join(
        f'''<li class="care-row reveal"><span class="care-row__when">{esc(w)}</span>
  <div><h3>{esc(t)}</h3><p>{esc(d)}</p></div></li>''' for w, t, d in care)
    return f"""<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Care tips</p><h2>How often to service a {esc(noun)}</h2>
    <p class="lede">A built-in Sub-Zero can run for decades with regular care. This is the care schedule to follow at home.</p></div>
  <ul class="care-list">{rows}</ul>
  {P.cta_row('Still running warm after this?', 'Call, or leave your number and we will call you back.', href='#request')}
</div></section>"""


def area_line():
    return f"""<section class="section section--tight"><div class="wrap">
  <p class="area-line">{icon('pin', size=18)}<span>We come to you across Orange County. <a href="/areas/">See the cities and neighborhoods we serve</a>.</span></p>
</div></section>"""


def render_combo_v2(bslug, uslug):
    b, c = BRAND_PAGES[bslug], COMBO_PAGES[(bslug, uslug)]
    from .data import SERVICES_BY_SLUG
    svc = SERVICES_BY_SLUG[uslug]
    path = f"/services/{uslug}/{bslug}/"
    price_html, catalog = price_table(c["prices"], c["noun"], path, c.get("maintenance"))
    body = f"""
{hero([('Home', '/'), ('Services', '/services/'), (svc['short'], f'/services/{uslug}/'), (b['name'], None)], c['h1'], c['lead'], c['photo'], portrait=True)}
{request_form(c['noun'], c['icon'], c['symptoms'][0].lower(), path)}
{types_section(c['noun'], c['types'])}
{problems_section(c['noun'], c['problems'], c.get('problem_photo'))}
{oem_block(b['name'], parts_for(bslug, uslug))}
{P.steps_section()}
{area_line()}
{care_section(c['noun'], c['care']) if c.get('care') else ''}
{faq_section(f"{c['noun']} repair FAQs", _faqs(c['faqs'], c['noun']))}
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
        extra_schema=[schema, faq_schema(_faqs(c["faqs"], c["noun"])), catalog], og_image=c["photo"], book_href="#request")


def render_combo(bslug, uslug):
    b, c = BRAND_PAGES[bslug], COMBO_PAGES[(bslug, uslug)]
    if c.get("v2"):
        return render_combo_v2(bslug, uslug)
    from .data import SERVICES_BY_SLUG
    svc = SERVICES_BY_SLUG[uslug]
    path = f"/services/{uslug}/{bslug}/"
    price_html, catalog = price_table(c.get('prices', b['prices']), c['noun'], path)
    symptoms = "".join(f'<li>{icon("check", size=20)}<span>{esc(x)}</span></li>' for x in c["symptoms"])
    causes = P.causes_block({"causes": c["causes"]})
    # Never repeat the hero photo in the gallery below it.
    gallery = P.gallery_block({"gallery": [g for g in c.get("gallery", []) if g[0] != c["photo"]]})
    body = f"""
{hero([('Home', '/'), ('Services', '/services/'), (svc['short'], f'/services/{uslug}/'), (b['name'], None)], c['h1'], c['lead'], c['photo'])}
<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Common problems</p><h2>What we fix on {esc(c['noun'])}s</h2></div>
  <ul class="checks">{symptoms}</ul>
  {P.cta_row('Sound like yours?', 'Same-day appointments may be available. Call to check.', href='#request')}
</div></section>
{request_form(c['noun'], c['icon'], c['symptoms'][0].lower(), path)}
{causes}
{oem_block(b['name'], parts_for(bslug, uslug))}
{gallery}
{P.steps_section()}
{faq_section(f"{c['noun']} repair FAQs", _faqs(c['faqs'], c['noun']))}
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
        extra_schema=[schema, faq_schema(_faqs(c["faqs"], c["noun"])), catalog], og_image=c["photo"], book_href="#request")


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
