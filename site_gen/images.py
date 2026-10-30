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
    "cellar-room-2":     ("wine-cellar/cellar-35.jpg", "Glass-front wine cellar cabinets in an Orange County home"),
    "cellar-temp":       ("wine-cellar/cellar-26.jpg", "Technician checking wine cellar temperature with an infrared thermometer"),
    "cellar-controller": ("wine-cellar/cellar-22.jpg", "Wine cellar temperature controller showing 58°F against a 55°F setpoint"),
    "cellar-pressure":   ("wine-cellar/cellar-20.jpg", "Refrigerant pressure control inside a wine cellar condensing unit"),
    "cellar-coil-clean": ("wine-cellar/cellar-25.jpg", "Condenser coil of a wine cellar cooling unit being cleaned with foam"),
    "cellar-coil":       ("wine-cellar/cellar-24.jpg", "Condenser coil of a wine cellar cooling unit after cleaning"),
    "cellar-compressor": ("wine-cellar/cellar-31.jpg", "Compressor inside the outdoor condensing unit of a wine cellar split system"),
    "cellar-evaporator": ("wine-cellar/cellar-32.jpg", "Technician tracing wiring on a wine cellar evaporator unit"),
    "cellar-attic":      ("wine-cellar/cellar-33.jpg", "Ducted wine cellar evaporator installed in an attic"),
    "cellar-pump":       ("wine-cellar/cellar-23.jpg", "Condensate pump for a wine cellar cooling system under a house"),
    "cellar-gauges":     ("wine-cellar/cellar-34.jpg", "Refrigerant gauges connected to an outdoor wine cellar condensing unit"),
}


def widths_for(slug):
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
