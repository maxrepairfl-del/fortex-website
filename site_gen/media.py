"""Real job photos from assets/photo-library, wired to pages.

Plain data only (images.py imports this). Every photo used anywhere on the
site from the library is declared here; its slug is the file name without
extension, and its alt text is the caption.

Rules: real job photos first, no customer faces, addresses or paperwork.
Captions say what is in the frame, not what we claim happened.
"""

# service slug -> (hero photo, alt)
HEROES = {
    "refrigerator-repair": ("refrigeration/job-brand-lg-french-door-fridge-kitchen", "French-door refrigerator on a service call"),
    "dishwasher-repair": ("dishwashers/gallery-dishwashers-142", "Stainless built-in dishwasher on a Fortex service call"),
    "washing-machine-repair": ("laundry/gallery-laundry-10", "Front-load washer and dryer pair in a laundry room on a Fortex service call"),
    "dryer-repair": ("laundry/gallery-laundry-15", "Electric dryer in a laundry room on a Fortex service call"),
    "freezer-repair": ("refrigeration/gallery-refrigeration-136", "Freezer compartment with ice built up over the evaporator cover"),
    "microwave-repair": ("cooking/gallery-cooking-16", "Over-the-range microwave above a gas range on a Fortex service call"),
    "oven-repair": ("cooking/gallery-cooking-62", "Built-in wall oven heating during a test"),
    "stove-cooktop-repair": ("cooking/gallery-cooking-9", "Professional gas range in a white kitchen on a Fortex service call"),
    "commercial-freezer-repair": ("commercial/gallery-commercial-150", "Two-door commercial reach-in refrigerator in a restaurant kitchen"),
    "ice-machine-repair": ("commercial/tg-vitalik-brand-hoshizaki-ice-machine", "Hoshizaki commercial ice machine on a Fortex service call"),
}

# service slug -> [(photo, caption)]
GALLERIES = {
    "refrigerator-repair": [
        ("refrigeration/job-fridge-evaporator-iced-over", "Evaporator buried in ice: the defrost system stopped working"),
        ("refrigeration/job-fridge-evaporator-after-defrost", "Evaporator cleared of ice and the defrost circuit tested"),
        ("refrigeration/tg-vitalik-fridge-ir-thermometer-43f-warm", "43°F in the fresh-food section, above the safe 40°F"),
        ("refrigeration/job-refrigerant-gauges", "Gauges on the sealed system before anyone talks compressor"),
        ("refrigeration/tg-vitalik-fridge-compressor-embraco", "Compressor and start relay in the machine compartment"),
        ("refrigeration/job-fridge-door-ice-maker", "In-door ice maker opened up for testing"),
        ("refrigeration/job-fridge-condenser-fan-blade", "Condenser fan blade, a common cause of warm fridges"),
        ("refrigeration/job-tech-panel-ready-builtin-fridge", "Working inside a panel-ready built-in refrigerator"),
    ],
    "dishwasher-repair": [
        ("dishwashers/job-dishwasher-pulled-out", "Dishwasher pulled out of the cabinet to reach the pump and valve"),
        ("dishwashers/job-brand-maytag-dishwasher-circulation-pump", "Circulation pump under a Maytag dishwasher"),
        ("dishwashers/job-dishwasher-inlet-valve-underside", "Water inlet valve and hoses under the tub"),
        ("dishwashers/job-dishwasher-racks-open", "Racks and spray arms checked during diagnosis"),
        ("dishwashers/gallery-dishwashers-32", "Fisher & Paykel DishDrawer on a service call"),
        ("dishwashers/job-brand-monogram-dishwasher", "GE Monogram panel dishwasher"),
        ("dishwashers/gallery-dishwashers-148", "Dishwasher running a test cycle"),
    ],
    "washing-machine-repair": [
        ("laundry/gallery-laundry-106", "Front panel off a front-load washer to reach the tub and boot"),
        ("laundry/tg-vitalik-drain-pump-in-hand-2", "Drain pump removed: the usual reason a washer won't drain"),
        ("laundry/tg-vitalik-washer-drum-gasket-check", "Checking the door boot for tears and trapped debris"),
        ("laundry/job-washer-top-load-drive-motor", "Drive motor and pulley under a top-load washer"),
        ("laundry/tg-vitalik-washer-inlet-valves", "Hot and cold inlet valves tested for flow"),
        ("laundry/job-washer-impeller-gloved", "Top-load washer impeller removed"),
        ("laundry/gallery-laundry-103", "Front-load washer door boot pulled back for inspection"),
        ("laundry/job-brand-ge-front-load-washer", "GE front-load washer on a service call"),
    ],
    "dryer-repair": [
        ("laundry/job-dryer-blower-housing-lint", "Blower housing packed with lint, a fire risk and the cause of slow drying"),
        ("laundry/tg-vitalik-dryer-drum-rollers", "Worn drum rollers: the source of thumping and squealing"),
        ("laundry/tg-vitalik-dryer-belt-pulley", "Drive belt and idler pulley under the drum"),
        ("laundry/job-dryer-gas-valve-multimeter", "Testing the gas valve coils with a multimeter"),
        ("laundry/job-dryer-burner-flame", "Dryer gas burner lit during a test"),
        ("laundry/gallery-laundry-47", "Lint build-up inside a dryer cabinet"),
        ("laundry/tg-vitalik-dryer-vent-duct-ceiling", "Rigid vent duct run to the ceiling exhaust"),
        ("laundry/job-dryer-lint-fire-damage", "Scorch marks left by lint near the heater"),
    ],
    "freezer-repair": [
        ("refrigeration/job-fridge-evaporator-iced-over-2", "Freezer evaporator frosted solid"),
        ("refrigeration/job-fridge-evaporator-bottom-freezer", "Bottom-freezer evaporator and defrost heater, panel off"),
        ("refrigeration/tg-vitalik-fridge-evaporator-fan", "Evaporator fan behind the freezer panel"),
        ("refrigeration/job-fridge-evaporator-defrost-heater", "Defrost heater and sensor on the evaporator"),
        ("refrigeration/tg-vitalik-freezer-meter-diagnosis", "Meter readings taken inside the freezer"),
        ("refrigeration/job-fridge-ir-thermometer-34f", "Temperature check with an infrared thermometer"),
        ("refrigeration/job-fridge-ice-bin-crushed-ice", "Ice bin and dispenser chute checked"),
        ("refrigeration/tg-vitalik-fridge-compressor-secop", "Compressor in a freezer machine compartment"),
    ],
    "microwave-repair": [
        ("cooking/tg-vitalik-microwave-opened", "Microwave cabinet off: transformer, magnetron and board"),
        ("cooking/tg-vitalik-microwave-magnetron-in-hand", "Magnetron removed for replacement"),
        ("cooking/tg-vitalik-microwave-magnetron-installed", "Microwave magnetron"),
        ("cooking/tg-vitalik-microwave-meter-test", "Testing the high-voltage circuit with a meter"),
        ("cooking/tg-vitalik-microwave-error-display", "Error code on the microwave display"),
        ("cooking/job-brand-viking-microwave", "Viking built-in microwave on a service call"),
        ("cooking/job-microwave-disassembled", "Built-in microwave opened on the counter"),
        ("cooking/gallery-cooking-29", "Built-in microwave above a wall oven"),
    ],
    "oven-repair": [
        ("cooking/job-oven-gas-burner-flame", "Gas oven burner lit after an igniter replacement"),
        ("cooking/job-oven-bake-element-red", "Bake element glowing during the heat test"),
        ("cooking/job-oven-broil-element-glow", "Broil element tested at full power"),
        ("cooking/gallery-cooking-43", "Wall oven pulled out of the cabinet on a cart"),
        ("cooking/tg-vitalik-oven-control-board", "Oven control board under test"),
        ("cooking/job-oven-convection-blower-in-hand", "Convection blower removed for replacement"),
        ("cooking/gallery-cooking-113", "Broiler flame checked through the oven door"),
        ("cooking/gallery-cooking-26", "Double wall oven on a service call"),
    ],
    "stove-cooktop-repair": [
        ("cooking/tg-vitalik-pro-range-cooktop-lifted", "Cooktop lifted on a pro range to reach valves and igniters"),
        ("cooking/gallery-cooking-22", "Gas cooktop with burners removed"),
        ("cooking/gallery-cooking-23", "Gas lines and valves under a cooktop"),
        ("cooking/job-brand-thermador-star-burner", "Thermador star burner"),
        ("cooking/tg-vitalik-gas-burner-flame-test", "Gas burner flame test"),
        ("cooking/gallery-cooking-101", "Radiant elements under an electric glass cooktop"),
        ("cooking/tg-vitalik-electric-glass-cooktop", "Electric glass cooktop on a service call"),
        ("cooking/gallery-cooking-38", "Rangetop with griddle in a customer's kitchen"),
    ],
    "commercial-freezer-repair": [
        ("commercial/gallery-commercial-52", "Walk-in cooler evaporator fan"),
        ("commercial/gallery-commercial-53", "Walk-in evaporator with twin fans"),
        ("commercial/gallery-commercial-42", "Condensing unit with gauges attached"),
        ("commercial/gallery-commercial-68", "Condenser coil on commercial refrigeration"),
        ("commercial/job-commercial-kitchen-line", "Restaurant kitchen line with reach-in refrigeration"),
    ],
    "ice-machine-repair": [
        ("commercial/tg-vitalik-brand-hoshizaki-ice-machine-board", "Hoshizaki ice machine control board"),
        ("commercial/tg-vitalik-brand-hoshizaki-label", "Hoshizaki data plate checked before ordering parts"),
        ("commercial/tg-vitalik-ice-machine-cubes", "Ice cubes in a commercial ice machine bin"),
        ("commercial/tg-vitalik-ice-machine-fans-compressor", "Condenser fans and compressor on an ice machine"),
        ("commercial/tg-vitalik-ice-machine-pump", "Water pump on a commercial ice machine"),
        ("commercial/gallery-commercial-2", "Stainless ice machine and bin on a service call"),
    ],
}

TEAM = [
    ("team/job-team-selfie-kitchen-3", "Two Fortex technicians after a repair in a customer's kitchen"),
    ("team/gallery-team-110", "Fortex technicians on a refrigerator job"),
    ("team/job-team-selfie-kitchen-1", "Fortex technicians in branded shirts on a service call"),
    ("team/job-tools-dewalt-impact-driver", "Tools ready in the service van"),
]

# Extra photos used by brand pages: (photo, alt)
EXTRA = [
    ("refrigeration/tg-vitalik-brand-thermador-builtin-fridge-label", "Thermador built-in refrigerator data plate"),
    ("refrigeration/tg-vitalik-brand-thermador-builtin-fridge-label-2", "Thermador built-in refrigerator-freezer rating label"),
    ("refrigeration/tg-vitalik-brand-subzero-model-label", "Sub-Zero model and serial label"),
    ("refrigeration/tg-vitalik-brand-lg-instaview-fridge", "LG InstaView refrigerator on a service call"),
    ("refrigeration/job-brand-lg-fridge-control-board", "LG refrigerator main control board"),
    ("refrigeration/job-brand-samsung-fridge-compressor", "Samsung refrigerator compressor"),
    ("refrigeration/job-brand-samsung-fridge-control-board", "Samsung refrigerator control board"),
    ("refrigeration/job-brand-samsung-fridge-model-label", "Samsung refrigerator model label"),
    ("refrigeration/gallery-refrigeration-114", "KitchenAid built-in refrigerator in a wood kitchen"),
    ("refrigeration/gallery-refrigeration-5", "Built-in refrigerator open for diagnosis"),
    ("laundry/job-brand-samsung-washer", "Samsung front-load washer"),
    ("laundry/job-brand-samsung-washer-open", "Samsung dryer with the front panel removed"),
    ("laundry/tg-vitalik-brand-samsung-washer-controls", "Samsung washer control panel"),
    ("laundry/gallery-laundry-24", "Samsung top-load washer"),
    ("laundry/gallery-laundry-83", "Samsung washer and dryer stack"),
    ("laundry/job-brand-samsung-dryer-hands", "Technician working on Samsung dryer wiring"),
    ("laundry/gallery-laundry-84", "Samsung stacked dryer on a service call"),
    ("laundry/job-brand-ge-top-load-washer", "GE top-load washer"),
    ("laundry/job-brand-ge-top-load-washer-controls", "GE top-load washer controls"),
    ("laundry/tg-vitalik-brand-ge-washer-top-off", "GE washer with the top panel off"),
    ("laundry/gallery-laundry-63", "GE front-load washer"),
    ("laundry/gallery-laundry-120", "Stacked washer and dryer on a service call"),
    ("laundry/job-brand-whirlpool-top-load-washer", "Whirlpool top-load washer"),
    ("laundry/job-washer-top-load-basket", "Top-load washer basket and agitator"),
    ("laundry/gallery-laundry-20", "Front-load washer on a service call"),
    ("laundry/gallery-laundry-4", "Top-load washer opened up for repair"),
    ("laundry/tg-vitalik-dryer-drum-roller-closeup", "Dryer drum roller up close"),
    ("laundry/tg-vitalik-dryer-idler-pulley", "Dryer idler pulley"),
    ("laundry/job-dryer-gas-burner-meter", "Gas dryer burner assembly under test"),
    ("dishwashers/job-dishwasher-stainless-front", "Bosch stainless dishwasher on a service call"),
    ("dishwashers/job-brand-fisher-paykel-dishdrawer", "Fisher & Paykel DishDrawer"),
    ("refrigeration/tg-vitalik-brand-bosch-side-by-side-open", "Bosch side-by-side refrigerator open on a service call"),
    ("dishwashers/tg-vitalik-brand-bosch-dishwasher-label", "Bosch dishwasher model label"),
    ("dishwashers/tg-vitalik-bosch-dishwasher-pump", "Pump and wiring under a Bosch dishwasher"),
    ("dishwashers/tg-vitalik-bosch-dishwasher-pump-area", "Base of a Bosch dishwasher opened to the pump"),
    ("commercial/tg-vitalik-brand-hoshizaki-board-2", "Hoshizaki control board up close"),
    ("wine/job-wine-room-glass-doors", "Wine room behind glass doors"),
    ("parts-and-diagnostics/job-tech-control-board-shoe-covers", "Technician in shoe covers testing a control board on a service call"),
]


def _all():
    seen = {}
    for p, a in HEROES.values():
        seen.setdefault(p, a)
    for items in GALLERIES.values():
        for p, c in items:
            seen.setdefault(p, c)
    for p, a in TEAM + EXTRA:
        seen.setdefault(p, a)
    return seen


def slug(path):
    return path.split("/", 1)[1]


# slug -> (source under assets/photos, alt), same shape as images.JOB_PHOTOS
LIB_PHOTOS = {slug(p): (f"../photo-library/{p}.jpg", a) for p, a in _all().items()}
