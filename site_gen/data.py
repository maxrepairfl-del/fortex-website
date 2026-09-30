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
    # Google Search Console: paste the content="..." value from the "HTML tag"
    # verification method here, then rebuild and deploy. Verifying this way needs
    # no DNS edit, so the Zoho mail records are never at risk.
    "google_site_verification": "zSfVYjeLCH30q6qbZxdtjg3NBDO1HIQRJ41XYCk3hzY",
    # Ratings and counts, checked against the live profiles 2026-08-20. Used in
    # the visible copy on the reviews page and the trust strip; update here and
    # they change everywhere. Yelp slipped to 4.9 after a 1-star on 2026-08-20 —
    # never round this up, a published rating has to match the source profile.
    "yelp_rating": "4.9",
    "yelp_reviews": 114,
    "google_rating": "5.0",  # FIXME re-verify against the GBP profile
    "google_reviews": 44,
    "license": "50759",
    "region": "Orange County, CA",
    "tagline": "Same-Day Appliance Repair in Orange County",
    # Must stay identical to the hours on Google Business Profile and Yelp —
    # Google treats a site/GBP mismatch as a negative local signal.
    "hours": "Mon–Fri 9am–6pm · Sat 9am–4pm",  # Sun closed
    "promo": "Free service call with any completed repair",
    "warranty": "1-year warranty on OEM parts · 90-day labor",
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
    ("4.9★", "Yelp & Google rating"),
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
    ("shield", "Upfront Price",
     "Our licensed technician arrives on time, diagnoses the problem, and gives you an upfront, all-in price. Free service visit with any repair, no hidden fees."),
    ("award", "Warrantied Work",
     "We fix it right and stand behind it: a full year on original manufacturer (OEM) parts and 90 days on our labor. Most repairs are done in a single visit."),
]

# ---------------------------------------------------------------- why fortex
WHY = [
    ("bolt", "Same-day & next-day service",
     "Most repairs scheduled the same or next day across Orange County. We know a broken appliance can't wait."),
    ("shield-plain", "Licensed & insured",
     f"California license #{SITE['license']} and full liability insurance. A vetted, uniformed technician every time."),
    ("dollar", "Upfront, honest pricing",
     "A clear all-in quote before any work begins. Free service call with your repair and no surprise add-ons."),
    ("award", "Warrantied repairs",
     "A full year on original manufacturer (OEM) parts and 90 days on our labor, on every job."),
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
        "hero_sub": 'Fridge not cooling, leaking, or making unusual noises? We diagnose and repair refrigerators, including built-in models.',
        "card": "Not cooling, leaking, or making noise? We fix all refrigerator types and brands.",
        "intro": "A warm refrigerator spoils food by the hour, which is why it is our most-requested same-day repair. We service French-door, side-by-side, top- and bottom-freezer, and built-in refrigerators from every major brand, diagnosing the real cause instead of swapping parts until something works.",
        "symptoms": [
            "Not cooling, or the freezer is warm while the fridge is cold",
            "Water leaking onto the floor or pooling under the crisper",
            "Loud buzzing, knocking, or clicking",
            "Ice maker producing nothing, or dumping slush",
            "Frost building up on the back wall of the freezer",
            "Compressor or fan running constantly and never shutting off",
            "Water dispenser slow, dripping, or dead",
            "Door not sealing, or sweating around the frame",
        ],
        "causes": [
            ("Fridge warm, freezer cold", "Failed evaporator fan or a blocked defrost drain",
             "Confirm airflow between the compartments before touching the sealed system, which is where the expensive mistakes get made"),
            ("Frost on the back wall", "Defrost heater, thermostat, or timer",
             "Test the defrost circuit end to end, replace the part that failed, and clear the drain line properly so it does not re-freeze"),
            ("Water on the floor", "Frozen or clogged defrost drain",
             "Thaw and clear the full drain line, not just the opening, which is why a kettle of hot water only buys a few weeks"),
            ("Running constantly", "Dirty condenser coils or a failing condenser fan",
             "Clean the coils, test the fan draw, and measure whether the compressor is actually holding temperature"),
            ("Ice maker dead", "Water inlet valve, fill tube ice-up, or the module itself",
             "Test the valve and module separately, since replacing the whole assembly when only the valve failed is the common overcharge"),
            ("Noisy", "Evaporator or condenser fan bearings",
             "Locate which fan by sound and by stopping each in turn, then replace only that motor"),
        ],
        "types": [
            ("Built-in &amp; column refrigerators",
             "Sub-Zero, Thermador, Viking, Miele and similar, pulled from the cabinetry, serviced, and reset flush. These are the ones most companies will not take on."),
            ("French-door &amp; side-by-side",
             "The common failures here are the ice maker and the defrost drain, and both are usually fixable in one visit."),
            ("Top- and bottom-freezer",
             "Simpler machines, cheaper repairs, and almost always worth fixing rather than replacing."),
            ("Wine coolers &amp; beverage centres",
             "Undercounter and freestanding units, including dual-zone. Thermoelectric and compressor-driven both."),
        ],
        "faqs": [
            ("My fridge stopped cooling. Can you come today?",
             "In most of Orange County, yes. Call or text and we will give you the earliest same-day or next-day window we have. Food spoils by the hour, so we treat a warm refrigerator as urgent."),
            ("How much will it cost?",
             "It depends on what failed, and the range is genuinely wide: a fan motor and a sealed-system fault are not in the same world. The service visit is free when you approve the repair and $80 if you decide not to go ahead. You get the full price before anything is touched."),
            ("The fridge is warm but the freezer is still cold. What does that mean?",
             "Usually a failed evaporator fan or a blocked defrost drain rather than the compressor, which is good news because it is the cheaper end. Air is made cold in the freezer and blown across; when that airflow stops the fridge warms while the freezer stays fine."),
            ("There is water on my kitchen floor.",
             "Nine times out of ten this is a frozen defrost drain backing up. Pouring hot water down the visible opening clears the top of the line and it re-freezes within a few weeks. We thaw and clear the whole line so it stays clear."),
            ("Is it worth repairing or should I replace it?",
             "We will tell you honestly once we have diagnosed it. The rough rule is that if the repair costs less than half of a comparable new unit, repair wins. For a built-in, replacement also means cabinetry work, so repair almost always wins."),
            ("Do you work on built-in and high-end refrigerators?",
             "Yes, regularly. Sub-Zero, Thermador, Viking, Bosch, Miele and similar. These need the unit pulled from the cabinetry and reset properly afterwards, which is the part most companies would rather not deal with."),
            ("My ice maker stopped working.",
             "Three usual suspects: the water inlet valve, the fill tube icing over, or the ice maker module. We test them separately, because replacing the whole assembly when only the valve failed is the most common way people get overcharged on this repair."),
            ("Can you fix a refrigerator that is running constantly?",
             "Yes, and it is worth fixing rather than living with. Usually dirty condenser coils or a failing condenser fan, both inexpensive. Left alone it runs the compressor to death, and that is the repair you do not want."),
            ("How long does the repair take?",
             "Most are done in one visit, typically one to two hours. Our vans carry the common fans, valves, thermostats and defrost parts. A compressor or a control board for a built-in may need ordering, and we tell you at the quote."),
            ("What warranty do I get?",
             "Our labor carries 90 days on every completed repair, and original manufacturer (OEM) parts carry a full year. We tell you which parts are going in before you approve the work."),
        ],
    },
    {
        "slug": "dishwasher-repair", "name": "Dishwasher Repair", "short": "Dishwashers",
        "icon": "dishwasher", "photo": "dishwasher-1",
        "hero_sub": 'Dishwasher not draining, leaving dishes dirty, or leaking? We repair every major brand, built-in and drawer models included.',
        "card": "Not draining, not cleaning, or leaking? We get your dishwasher running like new.",
        "intro": "When a dishwasher won't drain or leaves dishes dirty, it's usually a pump, spray arm, or seal issue we can fix on the spot. We repair every major dishwasher brand and restore proper cleaning, draining, and leak-free operation.",
        "symptoms": [
            "Won't drain, or water stands in the bottom",
            'Dishes come out dirty, gritty, or still wet',
            'Leaking onto the floor or under the cabinets',
            "Won't start, fill, or finish a cycle",
            "Door won't latch, or the seal is failing",
            'Grinding, humming, or loud running',
            'Detergent door not opening',
            'Error code or flashing lights',
        ],
        "causes": [
            ("Won't drain", 'Blocked filter, drain hose, or a failed pump',
             'Clear the filter and hose first, because a pump gets replaced far more often than it actually fails'),
            ('Dishes still dirty', 'Clogged spray arms or a weak wash pump',
             'Clear the spray-arm jets and measure the wash pressure before condemning the pump'),
            ('Leaking', 'Door seal, or the tub-to-pump connection',
             'Run a cycle and trace where the water actually appears rather than replacing the seal on spec'),
            ("Won't fill", 'Water inlet valve or a closed supply valve',
             'Check the supply is open first; a closed valve under the sink is a common and free fix'),
            ("Won't start", 'Door latch switch or the control board',
             'Test the latch switch first, since it fails far more often and costs a fraction of a board'),
        ],
        "types": [
            ('Built-in dishwashers', 'Standard 24-inch and compact units, pulled from under the counter and reset properly.'),
            ('Drawer dishwashers', 'Single and double drawer units, including Fisher &amp; Paykel.'),
            ('Panel-ready &amp; integrated', 'Units behind cabinet panels, removed and refitted without damaging the front.'),
            ('Every major brand', 'Bosch, Miele, KitchenAid, Whirlpool, Samsung, LG, Thermador and the rest.'),
        ],
        "faqs": [
            ("My dishwasher won't drain. Is that a big repair?",
             'Usually not. Most of the time it is a blocked filter or drain hose rather than a failed pump, and that is a quick fix. We clear and test before quoting anything larger.'),
            ('How much will it cost?',
             'It depends on which part failed, and the honest range is wide. The service visit is free with any repair and $80 otherwise, and you get the full price before any work starts. If it turns out to be something simple we sort it out there and then, covered by the same $80.'),
            ('Dishes come out dirty even on a long cycle.',
             'Nearly always blocked spray arms, sometimes a weak wash pump. We clear the jets and measure the actual wash pressure, so you are not paying for a pump that was working fine.'),
            ('There is water under my dishwasher.',
             'Could be the door seal or the connection between tub and pump. We run a cycle and watch where the water actually appears rather than replacing the seal and hoping.'),
            ("It won't start at all.",
             'The door latch switch is the usual culprit and it is an inexpensive part. Control boards do fail, but far less often, so we test the latch first.'),
            ('Do you repair panel-ready and integrated dishwashers?',
             'Yes. They come out from behind the cabinet panel and go back without damage to the front. Bosch, Miele and Thermador are routine for us.'),
            ('Is it worth repairing or should I replace it?',
             'We will tell you honestly once we have diagnosed it. As a rule, if the repair is less than half the cost of a comparable new unit, repair wins, and for panel-ready models replacement also means refitting the panel.'),
            ('How long does a dishwasher repair take?',
             'Most are finished in one visit, usually around an hour. Pumps, valves, latches and seals are on the van.'),
            ('My dishwasher smells.',
             'Almost always the filter and the drain area rather than a fault. We clean it out and show you how to keep on top of it, and if the smell is coming from standing water we find why it is not draining.'),
            ('What warranty do I get?',
             'Our labor carries 90 days on every completed repair, and original manufacturer (OEM) parts carry a full year. We tell you which parts are going in before you approve the work.'),
        ],
    },
    {
        "slug": "washing-machine-repair", "name": "Washing Machine Repair", "short": "Washing Machines",
        "icon": "washer", "photo": "washer-1",
        "hero_sub": 'Washer not spinning, not draining, or walking across the floor? We repair top-load and front-load machines from every major brand.',
        "card": "Won't spin, drain, or shaking hard? We repair front- and top-load washers.",
        "intro": "A washer that won't drain or spin can leave you with a tub full of soaking laundry. We repair front-load and top-load washing machines, fixing drainage, spin, balance, and leak problems quickly so laundry day gets back on track.",
        "symptoms": [
            "Won't spin, or clothes come out soaking",
            "Won't drain, or water stands in the drum",
            'Shakes violently or moves across the floor',
            "Won't fill, or fills very slowly",
            'Leaking from the door or underneath',
            'Loud banging or grinding on spin',
            "Door locked shut and won't open",
            'Error code on the display',
        ],
        "causes": [
            ("Won't drain", 'Blocked pump filter or a failed drain pump',
             'Open the pump filter first, coins and hairpins live there and the repair is often nothing more'),
            ("Won't spin", 'Worn drive belt, motor, or a door-lock switch',
             'A front-loader will not spin at all if the door lock is failing, which is cheaper than any of the alternatives'),
            ('Walks across the floor', 'Worn suspension or shipping bolts still fitted',
             'Check the levelling and the suspension; on a new install the shipping bolts are sometimes still in'),
            ('Leaking underneath', 'Door boot, pump seal, or a split hose',
             'Trace it wet rather than guessing, because the boot is the expensive one and often not the cause'),
            ('Bangs on spin', 'Worn drum bearings',
             'We tell you straight when a bearing job costs more than the machine is worth'),
        ],
        "types": [
            ('Front-load washers', 'Door boots, pumps, bearings and locks on every major brand.'),
            ('Top-load washers', 'Agitator and impeller machines, including the older direct-drive models.'),
            ('Stacked washer-dryers', 'Units that have to come apart to be reached, closet installs included.'),
            ('Every major brand', 'LG, Samsung, Whirlpool, Maytag, Bosch, Speed Queen, Miele and the rest.'),
        ],
        "faqs": [
            ("My washer won't spin. What's wrong?",
             'On a front-loader it is often the door-lock switch, which the machine treats as a safety stop. Otherwise the drive belt or motor. We test the cheap causes first.'),
            ('How much will it cost?',
             'It depends on which part failed, and the honest range is wide. The service visit is free with any repair and $80 otherwise, and you get the full price before any work starts. If it turns out to be something simple we sort it out there and then, covered by the same $80.'),
            ("It won't drain and the drum is full of water.",
             'Start with the pump filter, usually behind a small hatch at the bottom front. Coins, hairpins and buttons collect there. We clear it and check the pump actually runs before replacing anything.'),
            ('The machine shakes and moves across the floor.',
             'Either the suspension is worn or, on a recent install, the shipping bolts were never removed. Both are quick to establish and one of them is free.'),
            ('There is water on the floor under the washer.',
             'Door boot, pump seal or a split hose. We run it and trace where the water actually comes from, because the boot is the expensive part and often not the culprit.'),
            ('It bangs loudly on the spin cycle.',
             'That is usually drum bearings, and it is the one washer repair that often costs more than the machine is worth. We will tell you that plainly rather than take the job.'),
            ("The door is locked shut and I can't open it.",
             'Normal when a cycle fails part way. There is a manual release, and we can talk you through it on the phone before booking anything.'),
            ('Do you repair stacked units?',
             'Yes, including closet installs that have to be pulled and partly dismantled to reach. It is routine work for us.'),
            ('Is it worth repairing?',
             'Depends entirely on what failed. A pump or a door lock is always worth it. Bearings on an older machine usually are not, and we will say so.'),
            ('What warranty do I get?',
             'Our labor carries 90 days on every completed repair, and original manufacturer (OEM) parts carry a full year. We tell you which parts are going in before you approve the work.'),
        ],
    },
    {
        "slug": "dryer-repair", "name": "Dryer Repair", "short": "Dryers",
        "icon": "dryer", "photo": "dryer-1",
        "hero_sub": 'Dryer not heating, not spinning, or taking too long? We repair gas and electric dryers.',
        "card": "Not heating, taking three cycles to dry, or squealing? We fix gas and electric dryers.",
        "intro": "A dryer that needs three cycles to dry one load is costing you time and power every single wash. We repair gas and electric dryers from every major brand, replacing heating elements, igniters, thermostats, belts, rollers and blower wheels, and finding out whether the fault is the machine or the air it is trying to push.",
        "symptoms": [
            "Runs but clothes come out damp",
            "No heat at all",
            "Takes two or three cycles to dry one load",
            "Squealing, grinding, or thumping while turning",
            "Drum not turning though the motor runs",
            "Shuts off part-way through a cycle",
            "Very hot to the touch, or a burning smell",
            "Won't start, or the door latch will not hold",
        ],
        "causes": [
            ("No heat, electric", "Heating element or thermal fuse",
             "Test element continuity and the fuse together, since a blown fuse is usually a symptom of restricted airflow rather than the fault itself"),
            ("No heat, gas", "Igniter or flame sensor",
             "Measure the igniter current and confirm the sensor opens the gas valve, the same failure pattern as a gas oven"),
            ("Damp clothes, long cycles", "Restricted airflow or a worn blower wheel",
             "Measure the actual airflow and find where it is lost, which is often outside the machine entirely"),
            ("Squealing or grinding", "Drum rollers, idler pulley, or belt",
             "Replace the worn set rather than one part, because the others are the same age and will follow within months"),
            ("Drum will not turn", "Broken belt or failed drive motor",
             "Check the belt first, replace the motor only when it is genuinely dead"),
            ("Stops mid-cycle", "High-limit thermostat cutting out on heat",
             "Clear the restriction causing the overheat, then replace the thermostat, in that order, or it simply trips again"),
        ],
        "types": [
            ("Gas dryers", "Igniters, valves, flame sensors and thermostats on every major brand."),
            ("Electric dryers", "Heating elements, thermal fuses, timers and control boards."),
            ("Stacked washer-dryers", "Units that have to come apart to be reached, including the awkward closet installs."),
            ("Vented &amp; condenser", "Both, including the compact condenser dryers common in Orange County condos."),
        ],
        "faqs": [
            ("My dryer runs but won't heat. Can you fix it?",
             "Almost always yes, and usually in one visit. On an electric dryer it is the heating element or a thermal fuse; on a gas dryer it is the igniter. Our vans carry all three."),
            ("How much will it cost?",
             "It depends which part failed. The service visit is free when you approve the repair and $80 if you decide not to go ahead, and you get the full price before any work starts."),
            ("It takes three cycles to dry one load.",
             "That is nearly always airflow rather than heat. The heat is being made but it is not being moved through the clothes, either because the blower wheel is worn or because the venting behind the machine is restricted. We measure the airflow and tell you which it is."),
            ("Is a long drying time actually a problem?",
             "Yes, and not only for your power bill. Restricted airflow makes the dryer overheat, which trips the high-limit thermostat and, over time, kills the heating element. It is also the condition behind most dryer fires."),
            ("Do you clean dryer vents?",
             "Yes, where the run is reachable from both ends: an opening at the dryer and an outside vent hood we can get to. Long runs buried inside walls or ceilings with no outside access are not something we take on, and we will tell you that at the visit rather than charge you to find out."),
            ("My dryer squeals when it turns.",
             "Drum rollers, the idler pulley, or the belt. We replace the worn set rather than a single part, because the rest are the same age and would have you calling us again in a few months."),
            ("The drum isn't turning at all.",
             "Usually a snapped belt, which is an inexpensive fix. Sometimes the drive motor. We check the belt first rather than quoting the motor straight away."),
            ("Do you repair stacked and closet-installed units?",
             "Yes. They have to be pulled and partly dismantled to be reached, which is why some companies avoid them. It is routine work for us."),
            ("How long does a dryer repair take?",
             "Most are done in a single visit, usually around an hour. Elements, igniters, fuses, belts and roller kits are all on the van."),
            ("What warranty do I get?",
             "Our labor carries 90 days on every completed repair, and original manufacturer (OEM) parts carry a full year. We tell you which parts are going in before you approve the work."),
        ],
    },
    {
        "slug": "freezer-repair", "name": "Freezer Repair", "short": "Freezers",
        "icon": "freezer", "photo": "fridge-2",
        "hero_sub": 'Freezer not freezing, frosting over, or running constantly? We repair upright, chest and built-in freezers.',
        "card": "Frosting over or not freezing? We repair stand-alone and built-in freezers.",
        "intro": "A failing freezer puts hundreds of dollars of food at risk. We repair upright, chest, and built-in freezers, solving frost build-up, temperature, and defrost problems before your food thaws.",
        "symptoms": [
            'Not freezing, or food is thawing',
            'Heavy frost or ice on the walls',
            'Running constantly and never cutting out',
            'Water pooling under or inside',
            'Door not sealing, or icing around the frame',
            'Loud buzzing or clicking',
            'Temperature swinging up and down',
            'Alarm sounding or error code',
        ],
        "causes": [
            ('Not freezing', 'Failed evaporator fan, defrost fault, or a sealed-system problem',
             'Establish whether air is moving before anyone talks about the sealed system, which is where the expensive mistakes happen'),
            ('Heavy frost', 'Defrost heater, thermostat, or timer',
             'Test the defrost circuit end to end and clear the drain so it does not simply re-freeze'),
            ('Running constantly', 'Dirty condenser coils or a failing fan',
             'Clean the coils and measure whether it is actually holding temperature; left alone this kills the compressor'),
            ('Water underneath', 'Blocked defrost drain',
             'Thaw and clear the whole line, not just the visible opening, which is why hot water only buys a few weeks'),
            ('Door icing up', 'Failed or distorted door seal',
             'Replace the seal and check the door is sitting square, because a new seal on a dropped door ices up again'),
        ],
        "types": [
            ('Upright freezers', 'Freestanding and garage-ready models from every major brand.'),
            ('Chest freezers', 'Including the older manual-defrost units that are usually well worth repairing.'),
            ('Built-in &amp; column freezers', 'Sub-Zero, Thermador, Viking and similar, pulled from the cabinetry and reset flush.'),
            ('Commercial units', 'Reach-ins and small walk-ins on our commercial freezer page.'),
        ],
        "faqs": [
            ('My freezer stopped freezing. How fast can you come?',
             'We treat it as urgent, because a freezer full of food is worth more than the repair. Call or text and we will give you the earliest window we have.'),
            ('How much will it cost?',
             'It depends on which part failed, and the honest range is wide. The service visit is free with any repair and $80 otherwise, and you get the full price before any work starts. If it turns out to be something simple we sort it out there and then, covered by the same $80.'),
            ('There is heavy frost on the walls.',
             'That is the defrost system rather than the cooling. A heater, thermostat or timer has failed and the frost that should melt each cycle is building up instead. We test the whole circuit and clear the drain so it stays clear.'),
            ('It runs all the time and never stops.',
             'Usually dirty condenser coils or a failing fan, both inexpensive. Worth fixing quickly: running non-stop is what kills the compressor, and that is the repair you do not want.'),
            ('There is water on the floor under it.',
             'A blocked defrost drain backing up. Clearing the visible opening buys a few weeks; we thaw and clear the whole line.'),
            ('Do you work on built-in and column freezers?',
             'Yes, including Sub-Zero, Thermador and Viking. They need pulling from the cabinetry and resetting properly afterwards, which is the part most companies avoid.'),
            ('Is it worth repairing an old chest freezer?',
             'Often yes. They are simple machines, the parts are cheap, and a working chest freezer that cost little to fix is better value than a new one.'),
            ('My freezer is cold but the fridge above is warm.',
             'That points to airflow between the compartments rather than the cooling itself, which is usually the cheaper end. See our refrigerator page, and we handle both in the same visit.'),
            ('How long does the repair take?',
             'Most are done in one visit. Fans, thermostats, heaters and seals are on the van; a compressor or a board for a built-in may need ordering, and we say so at the quote.'),
            ('What warranty do I get?',
             'Our labor carries 90 days on every completed repair, and original manufacturer (OEM) parts carry a full year. We tell you which parts are going in before you approve the work.'),
        ],
    },
    {
        "slug": "garbage-disposal-repair", "name": "Garbage Disposal Repair", "short": "Garbage Disposals",
        "icon": "disposal", "photo": "dishwasher-2",
        "card": "Jammed, humming, or leaking? We repair and replace garbage disposals.",
        "intro": "A jammed or leaking garbage disposal is a quick fix for a pro. We repair and replace disposals of every horsepower, clear jams, stop leaks, and get your sink draining cleanly again.",
        "symptoms": [
            "Disposal hums but won't turn",
            "Completely dead, no sound at all",
            "Leaking under the sink",
            "Draining slowly or backing up",
            "Loud grinding or rattling",
            "Persistent bad odor",
        ],
        "faqs": [
            ("My disposal just hums. Is it dead?",
             "Usually not. A hum means it's jammed, not burned out. We clear the jam, reset it, and test it, and replace the unit only if it's truly failed."),
            ("Can you replace it the same visit?",
             "Yes. We carry quality replacement disposals and can swap a failed unit on the spot in most cases."),
        ],
    },
    {
        "slug": "microwave-repair", "name": "Microwave Repair", "short": "Microwave Ovens",
        "icon": "microwave", "photo": "microwave-1",
        "card": "Not heating or sparking? We repair built-in and over-the-range microwaves.",
        "intro": "We repair over-the-range, built-in, and countertop microwaves, solving no-heat, sparking, turntable, and control-panel problems safely. Built-in and OTR units are our specialty, where replacement is costly and a repair makes sense.",
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
             "In trained hands, yes. Microwaves store high voltage even unplugged, so this is not a DIY job. Our technicians discharge and service them safely."),
            ("My over-the-range microwave died, repair or replace?",
             "Built-in and OTR microwaves are expensive to replace and often cheaper to repair. We'll give you an honest recommendation after the diagnostic."),
        ],
    },
    {
        "slug": "oven-repair", "name": "Oven Repair", "short": "Ovens",
        "icon": "oven", "photo": "oven-1",
        "hero_sub": 'Oven not heating or baking unevenly? We repair gas and electric ovens, including wall ovens and double ovens.',
        "card": "Not heating, baking unevenly, or won't hold temperature? We repair every oven type.",
        "intro": "An oven that won't hold temperature ruins dinner and every batch after it. We repair gas and electric ovens, freestanding, built-in wall ovens, double ovens, and the oven half of a range, replacing elements, igniters, sensors and control boards, then verifying the calibration before we leave.",
        "symptoms": [
            "Oven won't heat or won't reach temperature",
            "Bakes unevenly, burns one side, or runs hot or cold",
            "Gas oven clicks but won't light",
            "Broil works but bake doesn't, or the reverse",
            "Control panel, display, or touchpad dead",
            "Oven door won't close, seal, or the glass is broken",
            "F-codes or error codes on the display",
            "Self-clean cycle killed the oven",
        ],
        "causes": [
            ("Won't heat at all", "Failed bake element or igniter",
             "Test element draw and igniter current, replace the failed part, confirm it reaches the set temperature"),
            ("Runs hot or cold", "Drifted temperature sensor",
             "Measure sensor resistance cold and hot, replace it, recalibrate against a reference thermometer"),
            ("Clicks but never lights", "Weak gas igniter",
             "A weak igniter still glows but no longer draws enough current to open the safety valve, so gas never flows"),
            ("Bakes unevenly", "Convection fan or a leaking door seal",
             "Test the fan motor and the seal. A leaking door is the cause people least expect"),
            ("Dead display or F-code", "Control board or touchpad",
             "Read the code and isolate board from touchpad, so only the part that actually failed gets replaced"),
        ],
        "types": [
            ("Built-in &amp; wall ovens",
             "Single and double wall ovens pulled from the cabinet, serviced, and reset flush. Sub-Zero, Thermador, Wolf, Viking, Bosch and Miele included."),
            ("Double ovens",
             "Upper and lower cavities are separate heating systems that usually share one control board. We diagnose them independently, so you never pay to replace a part that still works."),
            ("Range ovens",
             "The oven half of a freestanding or slide-in range, gas or electric. Burner and cooktop faults live on our <a href=\"/services/stove-cooktop-repair/\">stove &amp; cooktop page</a>."),
            ("Gas, electric &amp; dual-fuel",
             "All three, plus convection and steam ovens, from every major brand sold in the U.S."),
        ],
        "maintenance": [
            ("Standard", 185, "Deep cleaning and degreasing of the cavity, racks and door glass, burner or element cleaning, hinge and seal lubrication, and a full temperature calibration."),
            ("Deep", 240, "Everything in Standard, plus removal and degreasing of the fan and back panel, cleaning of the convection assembly, and replacement of worn door seals."),
        ],
        "faqs": [
            ("How much will my oven repair cost?",
             "It depends entirely on which part failed. The same symptom can be an inexpensive igniter or a control board that costs several times more. Guessing before we look would be dishonest. The service call is $80 and it is waived once you approve the repair. The technician finds the real cause and gives you the full, all-in price before touching anything, and you decide then."),
            ("What does the $80 service call cover?",
             "A licensed technician comes out, diagnoses the actual fault, and gives you a complete price for the fix. If you approve the repair, the $80 is waived and you only pay for the repair itself. If you decide not to go ahead, you pay the $80 and owe nothing further. And if it turns out to be something simple, like a tripped breaker or a child lock, we sort it out there and then, covered by the same $80, with nothing extra to pay."),
            ("My oven won't hold the right temperature.",
             "That is almost always a failed bake element, igniter, or temperature sensor. We test each one, replace what actually failed, and verify the calibration against a reference thermometer before we leave."),
            ("Do you repair double ovens?",
             "Yes. The upper and lower cavities are separate heating systems that usually share a single control board, so we diagnose them independently. That way you are not paying to replace a part that still works."),
            ("Do you work on built-in and wall ovens?",
             "Yes, including high-end built-ins. We pull the unit from the cabinet, service it, and reset it flush. Sub-Zero, Thermador, Wolf, Viking, Bosch, Miele and other premium brands are routine for us."),
            ("My gas oven clicks but never lights. Is that dangerous?",
             "It is the most common gas oven fault, and it is a weak igniter rather than a gas leak. The igniter has to draw enough current to open the safety valve; once it weakens it still glows but never opens the valve, so no gas flows. If you actually smell gas, that is different, shut off the supply and call us straight away."),
            ("Do you repair both gas and electric ovens?",
             "Yes, gas, electric, dual-fuel, convection and steam ovens from every major brand."),
            ("How long does an oven repair take?",
             "Most are finished in a single visit, usually under two hours. Our vans carry the common elements, igniters and sensors. A control board for a premium built-in sometimes has to be ordered, and we tell you that at the quote rather than afterwards."),
            ("Is it worth repairing my oven or should I replace it?",
             "We will tell you honestly once we have diagnosed it. The rough rule is that if the repair costs less than half of a comparable new unit, repairing wins, and for built-in ovens, where replacing also means cabinetry work, repair almost always wins."),
            ("What warranty do I get?",
             "Our labor carries 90 days on every completed repair, and original manufacturer (OEM) parts carry a full year. We tell you which parts are going in before you approve the work."),
        ],
    },
    {
        "slug": "stove-cooktop-repair", "name": "Stove & Cooktop Repair", "short": "Stoves & Cooktops",
        "icon": "oven", "photo": "oven-1",
        "hero_sub": "Burner won't light or cooktop won't heat? We repair gas, electric, and induction cooking surfaces.",
        "card": "Burner won't light, element stays cold, or clicking that never stops? We fix it.",
        "intro": "Burners that will not light, elements that stay cold, and igniters that click without end. We repair gas, electric and induction cooktops, plus the burner side of freestanding and slide-in ranges, from every major brand.",
        "symptoms": [
            "Gas burner won't light or keeps clicking",
            "Flame is weak, yellow, or uneven",
            "Electric element won't heat or heats intermittently",
            "Induction zone not recognising pans",
            "Glass cooktop cracked or a surface burner shorting",
            "Control knobs or touch controls not responding",
        ],
        "causes": [
            ("Clicks but won't light", "Clogged burner port or failed spark module",
             "Clear and clean the ports first; replace the spark module only when it is genuinely failing"),
            ("Clicks constantly, even when off", "Moisture or a stuck igniter switch",
             "Dry and clean the switch assembly, replace it when the contacts are burnt"),
            ("Weak or yellow flame", "Gas valve or a restricted orifice",
             "Clean or replace the orifice and verify the valve delivers the correct pressure"),
            ("Element won't heat", "Burnt element or infinite switch",
             "Test both. The switch fails more often than people expect and costs less to replace"),
        ],
        "types": [
            ("Gas cooktops &amp; ranges", "Sealed and open burners, spark modules, valves and orifices on every major brand."),
            ("Electric &amp; radiant glass", "Coil elements, radiant elements under ceramic glass, and the switches behind them."),
            ("Induction", "Induction cooktops including pan-detection faults and failed generator boards."),
            ("Built-in cooktops", "Units dropped into the counter, pulled, serviced and resealed properly."),
        ],
        "maintenance": [
            ("Standard", 175, "Burner head and port clearing, degreasing of grates and drip pans, igniter cleaning, and knob and valve lubrication."),
            ("Deep", 230, "Everything in Standard, plus orifice clearing, full removal and degreasing of the burner assembly, and cleaning of the spark module contacts."),
        ],
        "faqs": [
            ("How much will my cooktop repair cost?",
             "It depends on which part failed. The service call is $80 and it is waived once you approve the repair. The technician diagnoses the real cause and gives you the full price before any work starts."),
            ("My burner clicks but won't light.",
             "Usually a clogged burner port or a failing spark module. Cleaning the ports fixes a good share of these; when the module itself is going, we replace it."),
            ("The igniter keeps clicking even when the stove is off.",
             "That is moisture or a stuck igniter switch. We dry and clean the switch assembly, and replace it when the contacts are burnt."),
            ("Do you repair induction cooktops?",
             "Yes, induction, gas, electric coil and radiant glass cooktops from every major brand."),
            ("Can you replace cracked cooktop glass?",
             "On most brands yes, though the glass is often the single most expensive part on the appliance. We will price it and tell you honestly when replacing the unit makes more sense."),
            ("Do you fix the oven too?",
             "Yes, on a separate page. The parts and the faults are different enough to deserve it."),
        ],
    },
    {
        "slug": "wine-cooler-repair", "name": "Wine Cooler Repair", "short": "Wine Coolers",
        "icon": "wine", "photo": "fridge-wide",
        "card": "Not holding temperature? We repair wine coolers and beverage centers.",
        "intro": "Wine and beverage coolers need precise, stable temperatures to protect your collection. We repair built-in and free-standing wine coolers, fixing cooling, temperature, and humidity problems on both compressor and thermoelectric units.",
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
             "Yes, both built-in and free-standing units, including dual-zone coolers and premium brands."),
            ("My cooler won't get cold enough.",
             "That's usually a fan, thermostat, or compressor issue. We diagnose the exact cause and protect your collection with a fast repair."),
        ],
    },
    {
        "slug": "commercial-freezer-repair", "name": "Commercial Freezer Repair", "short": "Commercial Freezers",
        "icon": "commercial-freezer", "photo": "freezer-frost",
        "card": "Restaurant or business freezer down? Priority repair to protect your inventory.",
        "intro": "For restaurants, cafés, and shops, a down freezer means inventory loss by the hour. We provide priority repair for commercial freezers, reach-ins, and walk-in units, getting your kitchen back in operation fast.",
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
             "Yes, reach-in freezers, prep tables, and walk-in units for restaurants and retail businesses across Orange County."),
        ],
    },
    {
        "slug": "ice-machine-repair", "name": "Ice Machine Repair", "short": "Ice Machines",
        "icon": "ice", "photo": "fridge-diagnostic",
        "card": "No ice or cloudy ice? We repair residential and commercial ice machines.",
        "intro": "Whether it's a built-in home ice maker or a commercial ice machine, no ice is a real problem. We repair and descale residential and commercial ice machines, restoring clean, consistent ice production.",
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
             "Yes, descaling and cleaning are part of keeping production high and the ice clean. Ask us about routine maintenance for commercial units."),
        ],
    },
]

# Singular, properly-cased noun for headings ("Refrigerator problems we fix").
_NOUNS = {
    "refrigerator-repair": "Refrigerator", "dishwasher-repair": "Dishwasher",
    "washing-machine-repair": "Washing Machine", "dryer-repair": "Dryer",
    "freezer-repair": "Freezer", "garbage-disposal-repair": "Garbage Disposal",
    "microwave-repair": "Microwave",
    "oven-repair": "Oven", "stove-cooktop-repair": "Stove / Cooktop",
    "dryer-vent-cleaning": "Dryer Vent", "wine-cooler-repair": "Wine Cooler",
    "commercial-freezer-repair": "Commercial Freezer", "ice-machine-repair": "Ice Machine",
}
for _s in SERVICES:
    _s["noun"] = _NOUNS[_s["slug"]]

SERVICES_BY_SLUG = {s["slug"]: s for s in SERVICES}

# ---------------------------------------------------------------- service areas
CITIES = [
    {"slug": "irvine", "name": "Irvine", "photo": "fridge-wide",
     "blurb": "Fast, licensed appliance repair throughout Irvine, from Woodbridge and Northwood to the Spectrum and University Park.",
     "areas": "Woodbridge, Northwood, Turtle Rock, University Park, Quail Hill, Great Park, Portola Springs and Orchard Hills"},
    {"slug": "huntington-beach", "name": "Huntington Beach", "photo": "dryer-branded",
     "blurb": "Same-day appliance repair across Huntington Beach, from downtown and the pier to Huntington Harbour and Edwards Hill.",
     "areas": "Downtown HB, Huntington Harbour, Goldenwest, Edwards Hill, Seacliff and Bolsa Chica"},
    {"slug": "anaheim", "name": "Anaheim", "photo": "oven-1",
     "blurb": "Trusted appliance repair in Anaheim and Anaheim Hills, reliable techs for homes near the resort district and beyond.",
     "areas": "Anaheim Hills, Anaheim Resort, Platinum Triangle, West Anaheim and The Colony"},
    {"slug": "santa-ana", "name": "Santa Ana", "photo": "washer-1",
     "blurb": "Licensed, insured appliance repair throughout Santa Ana, quick scheduling and honest, upfront pricing.",
     "areas": "Downtown Santa Ana, Floral Park, French Park, South Coast Metro and Park Santiago"},
    {"slug": "yorba-linda", "name": "Yorba Linda", "photo": "fridge-branded",
     "blurb": "Professional appliance repair in Yorba Linda, same-day and next-day service for every major brand.",
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

# Outline of the area we actually cover, drawn as one shaded polygon on the map:
# inland from Fullerton across to Yorba Linda, south past Lake Forest and Mission
# Viejo to Laguna Niguel, then back up the coast through Newport and Huntington
# Beach to Seal Beach.
SERVICE_AREA_POLYGON = [
    (33.9250, -118.0250),
    (33.9300, -117.7550),
    (33.8250, -117.6450),
    (33.6900, -117.5900),
    (33.5750, -117.6100),
    (33.4900, -117.6950),
    (33.5450, -117.8000),
    (33.5950, -117.8950),
    (33.6350, -117.9700),
    (33.7150, -118.0650),
    (33.7600, -118.1150),
]


# ---------------------------------------------------------------- reviews
# ONLY genuine, verbatim customer reviews belong here. Two invented "Google"
# entries were removed on 2026-07-25 — they were written from review *themes*
# rather than real wording, but rendered as verified reviews with schema.org
# markup. Publishing those risks an FTC endorsement violation and a Google
# structured-data penalty. To add more, paste the exact text from the Yelp or
# Google profile; never paraphrase or reconstruct.
# Deliberately empty. Roadmap decision 2026-08-31, "не переоткрывать": do not
# copy review text from Yelp onto the site, it is someone else's content. The
# rating, the count and a link to the source say the same thing and are ours to
# publish. If the owner ever gathers quotes customers gave him directly, they
# belong here.
REVIEWS = []

# ---------------------------------------------------------------- home FAQ
HOME_FAQ = [
    ("Do you offer same-day appliance repair?",
     "Yes. We offer same-day and next-day appointments across Orange County whenever our schedule allows. Call or text early in the day for the best chance at a same-day slot."),
    ("How much does a repair cost?",
     "Every repair starts with a diagnostic, and the service call is free when you approve the repair. You'll get a clear, all-in price before any work begins, no hidden fees or surprise charges."),
    ("Are you licensed and insured?",
     f"Yes. Fortex Appliance Repair holds California license #{SITE['license']} and carries full liability insurance. A vetted, uniformed technician handles every job."),
    ("What brands do you repair?",
     "All major brands, including Samsung, LG, Whirlpool, GE, Bosch, Maytag, KitchenAid, Frigidaire, Kenmore, Sub-Zero, Viking, and more, from everyday to high-end and built-in appliances."),
    ("Do you guarantee your work?",
     "We do. Original manufacturer (OEM) parts carry a full year, and our labor carries 90 days on every repair. We tell you which parts we are fitting before you approve the work."),
    ("Which areas do you serve?",
     "We serve Irvine, Huntington Beach, Anaheim, Santa Ana, Yorba Linda, and surrounding Orange County cities including Newport Beach, Costa Mesa, Tustin, and Lake Forest."),
]

# choices used by the booking form (label, icon)
BOOKING_APPLIANCES = [
    ("Refrigerator", "refrigerator"), ("Washer", "washer"), ("Dryer", "dryer"),
    ("Dishwasher", "dishwasher"), ("Oven", "oven"), ("Stove / Cooktop", "oven"),
    ("Microwave", "microwave"),
    ("Freezer", "freezer"), ("Garbage Disposal", "disposal"), ("Other", "tools"),
]
