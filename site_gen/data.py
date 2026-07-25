"""All site content. Edit copy here; templates stay untouched.

NOTE: items marked FIXME need confirmation from the owner before launch
(see plan "Open items"): real email, real review quotes, social links.
"""

SITE = {
    "name": "Fortex Appliance Repair",
    "short": "Fortex",
    "phone": "(949) 478-0089",
    "phone_href": "tel:+19494780089",
    "sms_href": "sms:+19494780089",
    # Public contact address. Deliberately a Gmail, not a domain address: the
    # only working domain mailbox is maksym.technician@fortexappliancerepair.com,
    # which is reserved for Google Business Profile / RingCentral verification.
    # service@fortexappliancerepair.com was on every page until 2026-07-25 and
    # had never existed — mail to it bounced with "550 5.1.1 User does not exist".
    "email": "fortexappliancerepair@gmail.com",
    # Formspree endpoint for booking/quote submissions, e.g.
    # "https://formspree.io/f/xdkoblqz". The build refuses to emit forms while
    # this is empty — an unwired form silently swallows leads.
    "form_endpoint": "https://formspree.io/f/mdaqpezy",
    "domain": "fortexappliancerepair.com",
    "url": "https://www.fortexappliancerepair.com",
    "license": "50759",
    "region": "Orange County, CA",
    "tagline": "Same-Day Appliance Repair in Orange County",
    "hours": "Mon–Fri 8am–7pm · Sat 9am–1pm",  # confirmed by owner (Sun closed)
    "promo": "Free service call with any completed repair",
    "warranty": "12-month parts / 90-day labor warranty",
    "founded": 2016,
    # YouTube "business card" / process video. FIXME: set the 11-char video id
    # (the part after youtu.be/ or watch?v=). Leave "" to hide the video section.
    "video_id": "pVSjzivPWlU",
    "video_title": "See how a Fortex repair works",
    # social — FIXME add real handles
    "yelp_url": "https://www.yelp.com/biz/fortex-appliance-repair-huntington-beach",
    "google_url": "https://share.google/ThxHGuDC4zLfMW4Bm",
    "instagram": "",
    "facebook": "",
}

STATS = [
    ("2,000+", "Repairs completed"),
    ("5.0★", "Yelp & Google rating"),
    ("Same-Day", "Service available"),
    ("100%", "Licensed & insured"),
]

BRANDS = [
    "Samsung", "LG", "Whirlpool", "GE", "GE Profile", "GE Monogram", "Maytag",
    "KitchenAid", "Frigidaire", "Kenmore", "Bosch", "Sub-Zero", "Wolf", "Viking",
    "Thermador", "Electrolux", "Amana", "Miele", "Jenn-Air", "Fisher & Paykel",
    "Haier", "Hisense", "Hotpoint", "Speed Queen", "Dacor", "Asko", "Bertazzoni",
    "Gaggenau", "Magic Chef", "Crosley", "Admiral", "Roper", "Westinghouse",
    "Marvel", "U-Line", "Scotsman", "Avanti", "Danby", "Tappan", "Estate",
]

# ---------------------------------------------------------------- how it works
STEPS = [
    ("calendar", "Easy Scheduling",
     "Call, text, or book online in under a minute. Tell us the appliance and the symptom and we lock in a same-day or next-day window that fits your schedule."),
    ("shield", "Free Diagnostic",
     "Our licensed technician arrives on time, diagnoses the problem, and gives you an upfront, all-in price. The service call is free when you approve the repair — no hidden fees."),
    ("award", "12-Month Warranty",
     "We fix it right with original manufacturer parts and back the work with a 12-month parts and 90-day labor warranty. Most repairs are done in a single visit."),
]

# ---------------------------------------------------------------- why fortex
WHY = [
    ("bolt", "Same-day & next-day service",
     "Most repairs scheduled the same or next day across Orange County — we know a broken fridge can't wait."),
    ("shield-plain", "Licensed & insured",
     f"California license #{SITE['license']} and full liability insurance. A vetted, uniformed technician every time."),
    ("dollar", "Upfront, honest pricing",
     "A clear all-in quote before any work begins. Free service call with your repair and no surprise add-ons."),
    ("award", "Warrantied repairs",
     "Original manufacturer parts and a 12-month parts / 90-day labor warranty on every job."),
    ("truck", "We come to you",
     "Fully stocked vans mean most parts are on board, so we finish the job in one visit whenever possible."),
    ("leaf", "Clean, respectful service",
     "Shoe covers, tidy work area, and a friendly tech who treats your home like their own."),
]

# ---------------------------------------------------------------- services
# slug, name (page title style), short (nav/grid), icon, photo (image slug)
SERVICES = [
    {
        "slug": "refrigerator-repair", "name": "Refrigerator Repair", "short": "Refrigerators",
        "icon": "refrigerator", "photo": "fridge-branded",
        "card": "Not cooling, leaking, or making noise? We fix all refrigerator types and brands.",
        "intro": "A warm refrigerator means food spoiling by the hour, so it's our most-requested same-day repair. Our technicians service French-door, side-by-side, top- and bottom-freezer, and built-in refrigerators from every major brand — diagnosing the real cause instead of guessing.",
        "symptoms": [
            "Refrigerator not cooling or freezer too warm",
            "Water leaking onto the floor or pooling inside",
            "Loud buzzing, knocking, or clicking noises",
            "Ice maker not working or dispenser jammed",
            "Frost build-up in the freezer",
            "Compressor or fan running constantly",
        ],
        "faqs": [
            ("My fridge stopped cooling — can you come today?",
             "In most of Orange County, yes. Call or text us and we'll give you the earliest same-day or next-day window available."),
            ("Is it worth repairing or should I replace it?",
             "After the free diagnostic we'll tell you honestly. As a rule of thumb, if the repair costs less than half of a comparable new unit, repair is the smart choice — especially for higher-end and built-in brands."),
            ("Do you work on built-in and high-end refrigerators?",
             "Yes — we regularly service Sub-Zero, Viking, Bosch, Thermador, and other premium built-in refrigerators."),
        ],
    },
    {
        "slug": "dishwasher-repair", "name": "Dishwasher Repair", "short": "Dishwashers",
        "icon": "dishwasher", "photo": "dishwasher-1",
        "card": "Not draining, not cleaning, or leaking? We get your dishwasher running like new.",
        "intro": "When a dishwasher won't drain or leaves dishes dirty, it's usually a pump, spray arm, or seal issue we can fix on the spot. We repair every major dishwasher brand and restore proper cleaning, draining, and leak-free operation.",
        "symptoms": [
            "Dishwasher won't drain or water stands in the bottom",
            "Dishes come out dirty or gritty",
            "Leaking onto the floor or under the cabinets",
            "Won't start, fill, or complete a cycle",
            "Door won't latch or detergent won't dispense",
            "Bad odor or standing water smell",
        ],
        "faqs": [
            ("Why won't my dishwasher drain?",
             "Most commonly a clogged filter, drain pump, or drain hose. We clear the blockage, test the pump, and make sure it drains fully before we leave."),
            ("My dishwasher leaks — is that a quick fix?",
             "Often, yes. Leaks usually trace back to a worn door gasket, spray arm, or pump seal — all parts we carry on the van."),
        ],
    },
    {
        "slug": "washing-machine-repair", "name": "Washing Machine Repair", "short": "Washing Machines",
        "icon": "washer", "photo": "washer-1",
        "card": "Won't spin, drain, or shaking hard? We repair front- and top-load washers.",
        "intro": "A washer that won't drain or spin can leave you with a tub full of soaking laundry. We repair front-load and top-load washing machines — fixing drainage, spin, balance, and leak problems quickly so laundry day gets back on track.",
        "symptoms": [
            "Washer won't spin or drain",
            "Shaking, banging, or 'walking' during spin",
            "Leaking water during the cycle",
            "Won't fill, start, or advance through cycles",
            "Clothes still soaking wet after the spin",
            "Burning smell or error code on the display",
        ],
        "faqs": [
            ("My washer won't spin or drain — what's wrong?",
             "Usually a clogged drain pump, a failed lid switch, or a worn drive belt. We diagnose the exact cause and most parts are on the van for a one-visit fix."),
            ("It shakes violently on spin — is that fixable?",
             "Yes. Excessive shaking is typically worn suspension/shocks or a balance issue, both of which we repair routinely."),
        ],
    },
    {
        "slug": "dryer-repair", "name": "Dryer Repair", "short": "Dryers",
        "icon": "dryer", "photo": "dryer-branded",
        "card": "Not heating or taking forever to dry? We fix electric and gas dryers.",
        "intro": "If your dryer runs but clothes stay damp, the heating element, thermostat, or venting is usually to blame. We repair gas and electric dryers from all major brands and restore fast, even, safe drying.",
        "symptoms": [
            "Dryer not heating or runs cold",
            "Takes multiple cycles to dry clothes",
            "Won't turn on or stops mid-cycle",
            "Loud thumping, squealing, or grinding",
            "Drum won't tumble",
            "Overheating or burning smell",
        ],
        "faqs": [
            ("My dryer runs but won't heat — can you fix it?",
             "Yes, that's one of the most common dryer repairs. It's usually the heating element, thermal fuse, or gas igniter — all parts we stock."),
            ("Clothes take forever to dry. Is it the dryer or the vent?",
             "We'll diagnose exactly where the problem is — whether it's a worn heating element, a failed thermostat, or restricted airflow — so you know precisely what needs to be fixed."),
        ],
    },
    {
        "slug": "freezer-repair", "name": "Freezer Repair", "short": "Freezers",
        "icon": "freezer", "photo": "fridge-2",
        "card": "Frosting over or not freezing? We repair stand-alone and built-in freezers.",
        "intro": "A failing freezer puts hundreds of dollars of food at risk. We repair upright, chest, and built-in freezers — solving frost build-up, temperature, and defrost problems before your food thaws.",
        "symptoms": [
            "Freezer not freezing or holding temperature",
            "Heavy frost or ice build-up",
            "Defrost system failure",
            "Running constantly or short-cycling",
            "Leaking or pooling water",
            "Loud or unusual noises",
        ],
        "faqs": [
            ("My freezer is frosting over — what causes that?",
             "Usually a faulty defrost heater, thermostat, or door seal letting humid air in. We pinpoint the cause and restore a frost-free freezer."),
            ("Can you save the food in my freezer?",
             "If you call at the first sign of trouble, often yes — that's why we prioritize same-day freezer and refrigerator calls."),
        ],
    },
    {
        "slug": "garbage-disposal-repair", "name": "Garbage Disposal Repair", "short": "Garbage Disposals",
        "icon": "disposal", "photo": "dishwasher-2",
        "card": "Jammed, humming, or leaking? We repair and replace garbage disposals.",
        "intro": "A jammed or leaking garbage disposal is a quick fix for a pro. We repair and replace disposals of every horsepower, clear jams, stop leaks, and get your sink draining cleanly again.",
        "symptoms": [
            "Disposal hums but won't turn",
            "Completely dead — no sound at all",
            "Leaking under the sink",
            "Draining slowly or backing up",
            "Loud grinding or rattling",
            "Persistent bad odor",
        ],
        "faqs": [
            ("My disposal just hums — is it dead?",
             "Usually not. A hum means it's jammed, not burned out. We clear the jam, reset it, and test it — and replace the unit only if it's truly failed."),
            ("Can you replace it the same visit?",
             "Yes. We carry quality replacement disposals and can swap a failed unit on the spot in most cases."),
        ],
    },
    {
        "slug": "microwave-repair", "name": "Microwave Repair", "short": "Microwave Ovens",
        "icon": "microwave", "photo": "microwave-1",
        "card": "Not heating or sparking? We repair built-in and over-the-range microwaves.",
        "intro": "We repair over-the-range, built-in, and countertop microwaves — solving no-heat, sparking, turntable, and control-panel problems safely. Built-in and OTR units are our specialty, where replacement is costly and a repair makes sense.",
        "symptoms": [
            "Microwave runs but doesn't heat",
            "Sparking or arcing inside",
            "Buttons or touchpad not responding",
            "Turntable won't turn",
            "Loud buzzing or humming",
            "Door won't latch or light stays on",
        ],
        "faqs": [
            ("Is it safe to repair a microwave?",
             "In trained hands, yes. Microwaves store high voltage even unplugged, so this is not a DIY job — our technicians discharge and service them safely."),
            ("My over-the-range microwave died — repair or replace?",
             "Built-in and OTR microwaves are expensive to replace and often cheaper to repair. We'll give you an honest recommendation after the diagnostic."),
        ],
    },
    {
        "slug": "oven-stove-repair", "name": "Oven & Stove Repair", "short": "Ovens & Stoves",
        "icon": "oven", "photo": "oven-1",
        "card": "Not heating evenly or burner won't light? We fix ovens, stoves, and ranges.",
        "intro": "From a burner that won't light to an oven that won't hold temperature, we repair gas and electric ovens, stoves, cooktops, and ranges. We calibrate, replace elements and igniters, and get your kitchen cooking again.",
        "symptoms": [
            "Oven won't heat or won't reach temperature",
            "Uneven baking or wrong temperature",
            "Gas burner won't light or click",
            "Electric element not heating",
            "Control panel or display not working",
            "Oven door won't close or seal",
        ],
        "faqs": [
            ("My oven won't hold the right temperature.",
             "That's typically a failed bake element, igniter, or temperature sensor. We test each, replace what's needed, and verify the calibration before we leave."),
            ("Do you repair both gas and electric ranges?",
             "Yes — gas, electric, dual-fuel, and induction cooktops and ranges from all major brands."),
        ],
    },
    {
        "slug": "wine-cooler-repair", "name": "Wine Cooler Repair", "short": "Wine Coolers",
        "icon": "wine", "photo": "fridge-wide",
        "card": "Not holding temperature? We repair wine coolers and beverage centers.",
        "intro": "Wine and beverage coolers need precise, stable temperatures to protect your collection. We repair built-in and free-standing wine coolers — fixing cooling, temperature, and humidity problems on both compressor and thermoelectric units.",
        "symptoms": [
            "Cooler not cooling or too warm",
            "Temperature swings or won't hold a set point",
            "Too cold or freezing bottles",
            "Loud humming or vibration",
            "Interior light or display not working",
            "Condensation or leaking inside",
        ],
        "faqs": [
            ("Do you service built-in wine coolers?",
             "Yes — both built-in and free-standing units, including dual-zone coolers and premium brands."),
            ("My cooler won't get cold enough.",
             "That's usually a fan, thermostat, or compressor issue. We diagnose the exact cause and protect your collection with a fast repair."),
        ],
    },
    {
        "slug": "commercial-freezer-repair", "name": "Commercial Freezer Repair", "short": "Commercial Freezers",
        "icon": "commercial-freezer", "photo": "freezer-frost",
        "card": "Restaurant or business freezer down? Priority repair to protect your inventory.",
        "intro": "For restaurants, cafés, and shops, a down freezer means inventory loss by the hour. We provide priority repair for commercial freezers, reach-ins, and walk-in units — getting your kitchen back in operation fast.",
        "symptoms": [
            "Freezer not holding safe temperature",
            "Excess frost or ice on coils",
            "Compressor running constantly",
            "Door gasket or seal failure",
            "Defrost or thermostat failure",
            "Unusual noise or water on the floor",
        ],
        "faqs": [
            ("How fast can you respond for a business?",
             "We prioritize commercial calls because every hour counts. Call us and we'll get a technician out as fast as possible."),
            ("Do you service reach-in and walk-in units?",
             "Yes — reach-in freezers, prep tables, and walk-in units for restaurants and retail businesses across Orange County."),
        ],
    },
    {
        "slug": "ice-machine-repair", "name": "Ice Machine Repair", "short": "Ice Machines",
        "icon": "ice", "photo": "fridge-diagnostic",
        "card": "No ice or cloudy ice? We repair residential and commercial ice machines.",
        "intro": "Whether it's a built-in home ice maker or a commercial ice machine, no ice is a real problem. We repair and descale residential and commercial ice machines — restoring clean, consistent ice production.",
        "symptoms": [
            "No ice or very slow production",
            "Small, cloudy, or bad-tasting ice",
            "Leaking water around the unit",
            "Ice maker won't cycle or eject",
            "Scale or mineral build-up",
            "Loud noises during the cycle",
        ],
        "faqs": [
            ("My ice maker stopped making ice.",
             "Common causes are a clogged water line, failed inlet valve, or a faulty ejector. We diagnose and repair all of them, residential or commercial."),
            ("Do you descale and maintain ice machines?",
             "Yes — descaling and cleaning are part of keeping production high and the ice clean. Ask us about routine maintenance for commercial units."),
        ],
    },
]

# Singular, properly-cased noun for headings ("Refrigerator problems we fix").
_NOUNS = {
    "refrigerator-repair": "Refrigerator", "dishwasher-repair": "Dishwasher",
    "washing-machine-repair": "Washing Machine", "dryer-repair": "Dryer",
    "freezer-repair": "Freezer", "garbage-disposal-repair": "Garbage Disposal",
    "microwave-repair": "Microwave", "oven-stove-repair": "Oven & Stove",
    "dryer-vent-cleaning": "Dryer Vent", "wine-cooler-repair": "Wine Cooler",
    "commercial-freezer-repair": "Commercial Freezer", "ice-machine-repair": "Ice Machine",
}
for _s in SERVICES:
    _s["noun"] = _NOUNS[_s["slug"]]

SERVICES_BY_SLUG = {s["slug"]: s for s in SERVICES}

# ---------------------------------------------------------------- service areas
CITIES = [
    {"slug": "irvine", "name": "Irvine", "photo": "fridge-wide",
     "blurb": "Fast, licensed appliance repair throughout Irvine — from Woodbridge and Northwood to the Spectrum and University Park.",
     "areas": "Woodbridge, Northwood, Turtle Rock, University Park, Quail Hill, Great Park, Portola Springs and Orchard Hills"},
    {"slug": "huntington-beach", "name": "Huntington Beach", "photo": "dryer-branded",
     "blurb": "Same-day appliance repair across Huntington Beach, from downtown and the pier to Huntington Harbour and Edwards Hill.",
     "areas": "Downtown HB, Huntington Harbour, Goldenwest, Edwards Hill, Seacliff and Bolsa Chica"},
    {"slug": "anaheim", "name": "Anaheim", "photo": "oven-1",
     "blurb": "Trusted appliance repair in Anaheim and Anaheim Hills — reliable techs for homes near the resort district and beyond.",
     "areas": "Anaheim Hills, Anaheim Resort, Platinum Triangle, West Anaheim and The Colony"},
    {"slug": "santa-ana", "name": "Santa Ana", "photo": "washer-1",
     "blurb": "Licensed, insured appliance repair throughout Santa Ana — quick scheduling and honest, upfront pricing.",
     "areas": "Downtown Santa Ana, Floral Park, French Park, South Coast Metro and Park Santiago"},
    {"slug": "yorba-linda", "name": "Yorba Linda", "photo": "fridge-branded",
     "blurb": "Professional appliance repair in Yorba Linda — same-day and next-day service for every major brand.",
     "areas": "East Lake Village, Travis Ranch, Fairmont, Bryant Ranch and Hidden Hills"},
]
# Additional cities listed in the footer / areas page (no dedicated page yet)
NEARBY = ["Newport Beach", "Costa Mesa", "Tustin", "Lake Forest", "Fountain Valley",
          "Orange", "Garden Grove", "Fullerton", "Mission Viejo", "Laguna Niguel"]

CITIES_BY_SLUG = {c["slug"]: c for c in CITIES}

# Approximate city centres (lat, lon), used to draw the coverage map in
# components.coverage_map(). Drawn as inline SVG rather than a Google Maps embed:
# an embed needs an API key with billing attached, loads third-party script on
# every page, and sets cookies — a lot of cost for a picture that never changes.
CITY_COORDS = {
    "Irvine":          (33.6846, -117.8265),
    "Huntington Beach": (33.6603, -117.9992),
    "Anaheim":         (33.8366, -117.9143),
    "Santa Ana":       (33.7455, -117.8677),
    "Yorba Linda":     (33.8886, -117.8131),
    "Newport Beach":   (33.6189, -117.9298),
    "Costa Mesa":      (33.6411, -117.9187),
    "Tustin":          (33.7458, -117.8261),
    "Lake Forest":     (33.6469, -117.6892),
    "Fountain Valley": (33.7092, -117.9537),
    "Orange":          (33.7879, -117.8531),
    "Garden Grove":    (33.7739, -117.9414),
    "Fullerton":       (33.8704, -117.9243),
    "Mission Viejo":   (33.6000, -117.6719),
    "Laguna Niguel":   (33.5225, -117.7075),
}

# Label nudges in SVG units for cities that sit close enough for their labels to
# collide. Santa Ana and Tustin are ~4 km apart on almost the same latitude, so
# without this their names overlap. (dx, dy) — positive dy moves the label below.
LABEL_OFFSETS = {
    "Tustin":        (26, 40),
    "Costa Mesa":    (-14, 0),
    "Newport Beach": (10, 34),
    "Orange":        (26, 0),
    # Nudged left and up so it clears Santa Ana once the labels grow on mobile.
    "Garden Grove":  (-46, -14),
}

# Coastline waypoints (lat, lon) from Seal Beach down to Dana Point, so the map
# reads as Orange County rather than as dots floating in space.
COASTLINE = [
    (33.7542, -118.1100),
    (33.7100, -118.0600),
    (33.6603, -117.9992),
    (33.6100, -117.9400),
    (33.5600, -117.8300),
    (33.5225, -117.7600),
    (33.4700, -117.6900),
]

# ---------------------------------------------------------------- reviews
# ONLY genuine, verbatim customer reviews belong here. Two invented "Google"
# entries were removed on 2026-07-25 — they were written from review *themes*
# rather than real wording, but rendered as verified reviews with schema.org
# markup. Publishing those risks an FTC endorsement violation and a Google
# structured-data penalty. To add more, paste the exact text from the Yelp or
# Google profile; never paraphrase or reconstruct.
REVIEWS = [
    # --- Yelp (verbatim excerpts from the 5.0★ / 101-review profile) ---
    {"name": "", "city": "Orange County", "source": "Yelp", "rating": 5, "verified": True,
     "text": "Maks was very professional, made the repair quickly, and told me to call back if there were any issues. Couldn't ask for more."},
    {"name": "", "city": "Orange County", "source": "Yelp", "rating": 5, "verified": True,
     "text": "They came out in the pouring rain at 7 at night to check out my dishwasher — and it wasn't even an emergency. That kind of service is rare."},
    {"name": "", "city": "Orange County", "source": "Yelp", "rating": 5, "verified": True,
     "text": "Fast, honest, and tidy. I really appreciate the plastic booties he wears over his shoes. Highly recommend Fortex."},
]

# ---------------------------------------------------------------- home FAQ
HOME_FAQ = [
    ("Do you offer same-day appliance repair?",
     "Yes. We offer same-day and next-day appointments across Orange County whenever our schedule allows. Call or text early in the day for the best chance at a same-day slot."),
    ("How much does a repair cost?",
     "Every repair starts with a diagnostic, and the service call is free when you approve the repair. You'll get a clear, all-in price before any work begins — no hidden fees or surprise charges."),
    ("Are you licensed and insured?",
     f"Yes. Fortex Appliance Repair holds California license #{SITE['license']} and carries full liability insurance. A vetted, uniformed technician handles every job."),
    ("What brands do you repair?",
     "All major brands, including Samsung, LG, Whirlpool, GE, Bosch, Maytag, KitchenAid, Frigidaire, Kenmore, Sub-Zero, Viking, and more — from everyday to high-end and built-in appliances."),
    ("Do you guarantee your work?",
     "We do. Repairs use original manufacturer parts and are backed by a 12-month parts and 90-day labor warranty."),
    ("Which areas do you serve?",
     "We serve Irvine, Huntington Beach, Anaheim, Santa Ana, Yorba Linda, and surrounding Orange County cities including Newport Beach, Costa Mesa, Tustin, and Lake Forest."),
]

# choices used by the booking form (label, icon)
BOOKING_APPLIANCES = [
    ("Refrigerator", "refrigerator"), ("Washer", "washer"), ("Dryer", "dryer"),
    ("Dishwasher", "dishwasher"), ("Oven / Stove", "oven"), ("Microwave", "microwave"),
    ("Freezer", "freezer"), ("Garbage Disposal", "disposal"), ("Other", "tools"),
]
