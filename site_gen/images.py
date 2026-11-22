"""Image manifest + responsive <img> helper.

Single source of truth for the photo library. `optimize_images.py` reads
PHOTOS / BRAND to generate resized JPEG/PNG variants into dist/images, and
writes _image_meta.json (slug -> [w, h] of the largest variant). The page
builder imports `img()` to emit responsive <img srcset> markup.
"""
import json
import os

# Responsive widths generated for every photo (px). All source photos are
# 5000-6000px wide landscape, so every width is available.
WIDTHS = [400, 800, 1200, 1600, 2000]
JPEG_QUALITY = 72

HERE = os.path.dirname(os.path.abspath(__file__))
META_PATH = os.path.join(HERE, "_image_meta.json")

# slug -> (source file under assets/photos, alt text)
# One slug per source photo; templates reference these slugs.
PHOTOS = {
    "toolbag-shoecovers":  ("IMG_8562.JPG", "Fortex technician's tool bag and protective shoe covers on a clean kitchen floor"),
    "tech-portrait":       ("IMG_8563.JPG", "Fortex appliance repair technician standing in a doorway, arms crossed"),
    "tech-arrival":        ("IMG_8564.JPG", "Uniformed Fortex technician arriving for a service call with his tool bag"),
    "dishwasher-2":        ("IMG_8565.JPG", "Technician repairing a dishwasher door with a power drill"),
    "dishwasher-1":        ("IMG_8566.JPG", "Fortex technician servicing a dishwasher spray arm"),
    "dishwasher-3":        ("IMG_8567.JPG", "Close-up of a technician removing a dishwasher part"),
    "range-tools":         ("IMG_8568.JPG", "Tool bag in front of an open gas range during a repair"),
    "oven-diagnostic":     ("IMG_8569.JPG", "Technician measuring oven temperature with an infrared thermometer"),
    "oven-1":              ("IMG_8570.JPG", "Fortex technician repairing an oven with a power drill"),
    "oven-2":              ("IMG_8571.JPG", "Technician kneeling to repair an oven, wearing shoe covers"),
    "oven-3":              ("IMG_8572.JPG", "Technician servicing the inside of an oven"),
    "oven-detail":         ("IMG_8573.JPG", "Close-up of a drill driving a screw on an oven door"),
    "microwave-1":         ("IMG_8574.JPG", "Fortex technician installing an over-the-range microwave"),
    "microwave-2":         ("IMG_8575.JPG", "Technician repairing a microwave control panel with a drill"),
    "fridge-2":            ("IMG_8576.JPG", "Technician repairing an open side-by-side refrigerator"),
    "fridge-tools":        ("IMG_8577.JPG", "Professional Milwaukee tool belt in front of an open refrigerator"),
    "fridge-tools-2":      ("IMG_8578.JPG", "Detail of a technician's tool belt during a refrigerator repair"),
    "fridge-diagnostic":   ("IMG_8579.JPG", "Technician checking refrigerator temperature with an infrared thermometer"),
    "diagnostic-meter":    ("IMG_8580.JPG", "Infrared thermometer reading an appliance temperature during diagnosis"),
    "freezer-frost":       ("IMG_8581.JPG", "Technician diagnosing a frosted-up freezer compartment"),
    "fridge-wide":         ("IMG_8582.JPG", "Fortex technician servicing a stainless side-by-side refrigerator in a kitchen"),
    "fridge-branded":      ("IMG_8583.JPG", "Fortex technician in a branded shirt repairing a French-door refrigerator"),
    "fridge-diagnostic-2": ("IMG_8584.JPG", "Technician measuring refrigerator temperature with an infrared thermometer"),
    "dryer-branded":       ("IMG_8585.JPG", "Fortex technician in a branded shirt repairing a stacked dryer"),
    "dryer-1":             ("IMG_8586.JPG", "Fortex technician repairing a dryer with a power drill"),
    "dryer-2":             ("IMG_8587.JPG", "Technician servicing a dryer control panel"),
    "washer-1":            ("IMG_8588.JPG", "Fortex technician repairing a front-load washing machine"),
    "tech-fun":            ("IMG_8589.JPG", "Friendly Fortex technician with a drill in front of a washer and dryer"),
}

# Job photos sent by the technicians over Telegram (960x1280, already
# compressed). Only widths up to the source size are generated, so nothing is
# upscaled. slug -> (source file under assets/photos, alt text)
JOB_WIDTHS = [400, 800, 960]
JOB_PHOTOS = {
    "cellar-room":       ("wine-cellar/cellar-27.jpg", "Glass-walled wine room on a Fortex wine cellar cooling service call"),
    "cellar-room-2":     ("wine-cellar/cellar-35.jpg", "Glass-front wine cabinets in a living room"),
    "cellar-temp":       ("wine-cellar/cellar-26.jpg", "Technician checking wine cellar temperature with an infrared thermometer"),
    "cellar-controller": ("wine-cellar/cellar-22.jpg", "Wine cellar temperature controller showing 58°F against a 55°F setpoint"),
    "cellar-pressure":   ("wine-cellar/cellar-20.jpg", "Refrigerant pressure control inside a wine cellar condensing unit"),
    "cellar-coil-clean": ("wine-cellar/cellar-25.jpg", "Condenser coil of a wine cellar cooling unit being cleaned with foam"),
    "cellar-coil":       ("wine-cellar/cellar-24.jpg", "Condenser coil of a wine cellar cooling unit"),
    "cellar-compressor": ("wine-cellar/cellar-31.jpg", "Compressor inside the outdoor condensing unit of a wine cellar split system"),
    "cellar-evaporator": ("wine-cellar/cellar-32.jpg", "Technician tracing wiring on a wine cellar evaporator unit"),
    "cellar-attic":      ("wine-cellar/cellar-33.jpg", "Ducted wine cellar evaporator installed in an attic"),
    "cellar-pump":       ("wine-cellar/cellar-23.jpg", "Condensate pump for a wine cellar cooling system under a house"),
    "cellar-gauges":     ("wine-cellar/cellar-34.jpg", "Refrigerant gauges connected to an outdoor wine cellar condensing unit"),
}


# Real job photos picked from the team's Telegram chats (2026-11-11), kept in
# assets/photos-real. 720-1280px, so they use JOB_WIDTHS like the cellar set.
REAL_PHOTOS = {
    "sz-builtin-sxs":      ("../photos-real/brand-subzero-builtin-side-by-side.jpg", "Sub-Zero built-in side-by-side refrigerator"),
    "builtin-panel-tech":  ("../photos-real/tech-panel-ready-builtin-fridge.jpg", "Panel-ready Sub-Zero built-in refrigerator during service"),
    "brazing-builtin":     ("../photos-real/team-selfie-kitchen-2.jpg", "Two Fortex technicians brazing a sealed-system line on a built-in refrigerator"),
    "gauges-compressor":   ("../photos-real/refrigerant-gauges.jpg", "Refrigerant manifold gauges connected at a refrigerator compressor"),
    "digital-manifold":    ("../photos-real/digital-manifold-gauge.jpg", "Digital refrigerant manifold reading pressures on a refrigerator sealed system"),
    "gauges-tools":        ("../photos-real/refrigerant-gauges-tools.jpg", "Refrigerant gauges, hoses and tools laid out on a refrigerator repair"),
    "team-thumbs":         ("../photos-real/team-selfie-kitchen-3.jpg", "Two Fortex technicians smiling after a repair in a customer's kitchen"),
    "pro-range-gold":      ("../photos-real/pro-range-48-gold-knobs.jpg", "48-inch professional gas range on a Fortex service call"),
    "lg-washtower":        ("../photos-real/brand-lg-washtower-white.jpg", "Stacked washer and dryer tower serviced by Fortex"),
    "commercial-line":     ("../photos-real/commercial-kitchen-line.jpg", "Restaurant kitchen line with commercial refrigeration"),
    "wolf-burners-lit": ("../photos-real/brand-wolf-range-burners-lit.jpg", "Gas range with all burners lit"),
    "wolf-front": ("../photos-real/brand-wolf-range-front.jpg", "Wolf gas range with red knobs"),
    "wolf-top-off": ("../photos-real/brand-wolf-range-top-off.jpg", "Wolf range with the cooktop lifted for burner repair"),
    "pro-range-open": ("../photos-real/pro-range-disassembled.jpg", "Professional range with the control panel open during repair"),
    "viking-range-48": ("../photos-real/brand-viking-range-48.jpg", "Viking 48-inch range on a Fortex service call"),
    "viking-rangetop": ("../photos-real/brand-viking-rangetop.jpg", "Viking rangetop in a white kitchen"),
    "viking-rangetop-2": ("../photos-real/brand-viking-rangetop-2.jpg", "Close-up of a Viking rangetop and its badge"),
    "viking-microwave": ("../photos-real/brand-viking-microwave.jpg", "Viking built-in microwave being serviced"),
    "thermador-range": ("../photos-real/brand-thermador-pro-grand-range.jpg", "Thermador Pro Grand range with star burners"),
    "thermador-top": ("../photos-real/brand-thermador-pro-grand-top.jpg", "Thermador Pro Grand cooktop with star-shaped burners"),
    "thermador-star": ("../photos-real/brand-thermador-star-burner.jpg", "Close-up of a Thermador star burner"),
    "thermador-knob": ("../photos-real/brand-thermador-knob-gloved.jpg", "Technician's gloved hand holding a Thermador control knob"),
    "lg-thinq": ("../photos-real/brand-lg-thinq-dispenser.jpg", "LG ThinQ refrigerator dispenser being checked by a technician"),
    "lg-compressor-label": ("../photos-real/brand-lg-compressor-label.jpg", "Label on an LG linear refrigerator compressor"),
    "lg-model-label": ("../photos-real/brand-lg-fridge-model-label.jpg", "LG refrigerator model and serial label"),
    "lg-compressor": ("../photos-real/brand-lg-compressor.jpg", "LG refrigerator compressor in the machine compartment"),
    "lg-washer-front": ("../photos-real/brand-lg-washer-front.jpg", "LG front-load washer on a pedestal"),
    "lg-washer-drum": ("../photos-real/brand-lg-washer-drum-logo.jpg", "Front-load washer with the front panel removed"),
    "washtower-black": ("../photos-real/brand-lg-washtower-black.jpg", "Stacked black-steel washer and dryer tower"),
    "washer-gasket": ("../photos-real/washer-gasket-hand.jpg", "Technician pulling back a front-load washer door gasket"),
    "drain-pump-hand": ("../photos-real/drain-pump-in-hand.jpg", "Drain pump removed from a machine for replacement"),
    "dryer-ir": ("../photos-real/dryer-ir-thermometer.jpg", "Infrared thermometer reading dryer temperature"),
    "dryer-vent-clog": ("../photos-real/dryer-vent-lint-clog.jpg", "Lint pulled from a clogged dryer vent"),
    "dryer-lint-burn": ("../photos-real/dryer-lint-fire-damage.jpg", "Dryer interior scorched by lint build-up"),
    "samsung-family-hub": ("../photos-real/brand-samsung-family-hub.jpg", "Samsung Family Hub refrigerator on a service call"),
    "samsung-washer": ("../photos-real/brand-samsung-washer.jpg", "Samsung front-load washer"),
    "samsung-washer-open": ("../photos-real/brand-samsung-washer-open.jpg", "Samsung dryer with the front panel removed"),
    "samsung-dryer": ("../photos-real/brand-samsung-dryer-hands.jpg", "Technician's hands working on Samsung dryer wiring"),
    "oven-flame": ("../photos-real/oven-gas-burner-flame.jpg", "Gas oven burner lit after an igniter repair"),
    "broil-glow": ("../photos-real/oven-broil-element-glow.jpg", "Oven broil element glowing during a test"),
    "clamp-meter":         ("../photos-real/clamp-meter-reading.jpg", "Clamp meter measuring current draw during an appliance diagnosis"),
}
JOB_PHOTOS.update(REAL_PHOTOS)

from .media import LIB_PHOTOS  # noqa: E402
JOB_PHOTOS.update(LIB_PHOTOS)


# Named web copies made from the originals in assets/photo-library by
# scripts/make_web_copies.py (AVIF + WebP + JPEG, EXIF orientation applied).
# The originals are never renamed or touched. slug -> (source under assets/, alt)
WEB_COPIES = {
    "sub-zero-built-in-refrigerator-overview-l302": (
        "photo-library/refrigeration/job-brand-subzero-builtin-side-by-side.jpg",
        "Sub-Zero built-in side-by-side refrigerator",
        (80, 395, 825, 1280)),  # owner: centre on the fridge (2026-11-13)
    "sub-zero-built-in-refrigerator-work-l321": (
        "photo-library/refrigeration/job-tech-panel-ready-builtin-fridge.jpg",
        "Panel-ready Sub-Zero built-in refrigerator during service"),
    # Repair stories on /our-work/ (owner briefs 2026-11-21). Files named by the owner.
    "dacor-range-overview": (
        "photo-library/cooking/job-pro-range-dual-oven.jpg",
        "Dacor range during the service visit"),
    "dacor-range-control-board-heat-damage": (
        "photo-library/cooking/dacor range PCB replacement 3 old part.jpg",
        "Original Dacor range control board with heat damage at a wiring connection"),
    "dacor-range-aftermarket-control-board": (
        "photo-library/cooking/dacor range PCB replacement 3.jpg",
        "Aftermarket replacement control board installed in the Dacor range"),
    "dacor-range-cooktop-lifted": (
        "photo-library/cooking/dacor range PCB replacement.jpg",
        "Dacor range with the cooktop assembly lifted for access to the control board"),
    "dacor-oven-bake-element-heating": (
        "photo-library/cooking/job-oven-bake-element-red.jpg",
        "New original bake element heating in the Dacor oven"),
    "viking-microwave-front": (
        "photo-library/cooking/Viking microwave magnetron replacemen 1.jpg",
        "Viking microwave during a service visit", 90),  # shot sideways: rotate upright
    "viking-microwave-magnetron-damaged-cap": (
        "photo-library/cooking/Viking microwave magnetron replacement damaged magnetron(burnt).jpg",
        "Removed microwave magnetron with a damaged antenna cap"),
    "viking-microwave-interior": (
        "photo-library/cooking/Viking microwave magnetron replacement.jpg",
        "Viking microwave interior during magnetron replacement"),
}
WEB_WIDTHS = [400, 640, 960]


def widths_for(slug):
    if slug in WEB_COPIES:
        # Web copies are never upscaled: cap at the source width (og:image too).
        full = _META.get(slug, (WEB_WIDTHS[-1], None))[0]
        return sorted({min(w, full) for w in WEB_WIDTHS})
    return JOB_WIDTHS if slug in JOB_PHOTOS else WIDTHS


# slug -> (source file under assets/, alt text). PNGs keep transparency.
BRAND = {
    "marketing-team":     ("brand/marketing-team.jpg",     "A Fortex technician with customers holding broken appliances"),
    "banner-technician":  ("brand/banner-technician.png",  "Appliance repair technician with a wrench"),
    "banner-call":        ("brand/banner-call.png",        "Calling an appliance repair technician on a phone"),
    "yelp-badge":         ("brand/yelp-badge.png",         "People Love Us on Yelp"),
}


def load_meta():
    """slug -> [w, h] of the largest generated variant (for width/height attrs)."""
    try:
        with open(META_PATH) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


_META = load_meta()


def img(slug, sizes="100vw", cls="", loading="lazy", fetchpriority=None,
        decoding="async", base="/images"):
    """Return a responsive <img> tag for a manifest slug."""
    if slug in WEB_COPIES:
        return picture(slug, sizes, cls, loading, fetchpriority, decoding, base)
    is_brand = slug in BRAND
    ext = "png" if (is_brand and BRAND[slug][0].endswith(".png")) else "jpg"
    alt = (BRAND.get(slug) or PHOTOS.get(slug) or JOB_PHOTOS.get(slug))[1]

    widths = widths_for(slug)
    srcset = ", ".join(f"{base}/{slug}-{w}.{ext} {w}w" for w in widths)
    fallback = f"{base}/{slug}-{widths[-2]}.{ext}"

    wh = ""
    if slug in _META:
        w, h = _META[slug]
        wh = f' width="{w}" height="{h}"'

    attrs = [
        f'src="{fallback}"',
        f'srcset="{srcset}"',
        f'sizes="{sizes}"',
        f'alt="{alt}"',
        f'loading="{loading}"',
        f'decoding="{decoding}"',
    ]
    if cls:
        attrs.append(f'class="{cls}"')
    if fetchpriority:
        attrs.append(f'fetchpriority="{fetchpriority}"')
    if wh:
        attrs.append(wh.strip())
    return "<img " + " ".join(attrs) + ">"


def is_portrait(slug):
    """True when the generated image is taller than wide (keep the whole appliance)."""
    wh = _META.get(slug)
    return bool(wh) and wh[1] > wh[0]


def picture(slug, sizes="100vw", cls="", loading="lazy", fetchpriority=None,
            decoding="async", base="/images"):
    """<picture> with AVIF and WebP sources and a JPEG fallback (web copies)."""
    alt = WEB_COPIES[slug][1]
    full = _META.get(slug, (WEB_WIDTHS[-1], None))[0]
    ws = sorted({min(w, full) for w in WEB_WIDTHS})
    def srcset(ext):
        return ", ".join(f"{base}/{slug}-{w}.{ext} {w}w" for w in ws)
    w, h = _META.get(slug, (None, None))
    wh = f' width="{w}" height="{h}"' if w else ""
    extra = (f' class="{cls}"' if cls else "") + (f' fetchpriority="{fetchpriority}"' if fetchpriority else "")
    return (f'<picture><source type="image/avif" srcset="{srcset("avif")}" sizes="{sizes}">'
            f'<source type="image/webp" srcset="{srcset("webp")}" sizes="{sizes}">'
            f'<img src="{base}/{slug}-{ws[-1]}.jpg" srcset="{srcset("jpg")}" sizes="{sizes}" alt="{alt}" '
            f'loading="{loading}" decoding="{decoding}"{extra}{wh}></picture>')
