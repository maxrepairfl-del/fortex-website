"""Real job photos from assets/photo-library, wired to pages.

Plain data only (images.py imports this). Every photo used anywhere on the
site from the library is declared here; its slug is the file name without
extension, and its alt text is the caption.

Rules: real job photos first, no customer faces, addresses or paperwork.
Captions say what is in the frame, not what we claim happened.
"""
import re

# service slug -> (hero photo, alt)
HEROES = {
    "refrigerator-repair": ("refrigeration/job-brand-lg-french-door-fridge-kitchen", "French-door refrigerator on a service call"),
    "dishwasher-repair": ("dishwashers/no-brand-dishwasher-stainless-built-in-overview-clear", "Stainless built-in dishwasher on a Fortex service call"),
    "washing-machine-repair": ("laundry/no-brand-washer-dryer-pair-laundry-room-overview-clear", "Front-load washer and dryer pair in a laundry room on a Fortex service call"),
    "dryer-repair": ("laundry/lg-dryer-front-overview-clear", "LG dryer in a laundry room on a Fortex service call"),
    "freezer-repair": ("refrigeration/no-brand-freezer-evaporator-frost-side-by-side-detail-clear", "Freezer compartment with ice built up over the evaporator cover"),
    "microwave-repair": ("cooking/kitchenaid-microwave-over-range-overview-clear", "Over-the-range microwave above a gas range on a Fortex service call"),
    "oven-repair": ("cooking/kitchenaid-wall-oven-microwave-overview-clear", "Built-in wall oven heating during a test"),
    "stove-cooktop-repair": ("cooking/thermador-pro-gas-range-36-overview-clear-3", "Professional gas range in a white kitchen on a Fortex service call"),
    "commercial-freezer-repair": ("commercial/no-brand-commercial-reach-in-refrigerator-two-door-overview-clear", "Two-door commercial reach-in refrigerator in a restaurant kitchen"),
    "ice-machine-repair": ("commercial/hoshizaki-ice-machine-undercounter-overview-clear", "Hoshizaki commercial ice machine on a Fortex service call"),
}

# service slug -> [(photo, caption)]
GALLERIES = {
    "refrigerator-repair": [
        ("refrigeration/job-fridge-evaporator-iced-over", "Evaporator buried in ice: the defrost system stopped working"),
        ("refrigeration/job-fridge-evaporator-after-defrost", "Evaporator cleared of ice and the defrost circuit tested"),
        ("refrigeration/no-brand-refrigerator-ir-thermometer-43f-warm-detail-clear", "43°F in the fresh-food section, above the safe 40°F"),
        ("refrigeration/job-refrigerant-gauges", "Gauges on the sealed system before anyone talks compressor"),
        ("refrigeration/no-brand-refrigerator-compressor-embraco-label-detail-blurry", "Compressor and start relay in the machine compartment"),
        ("refrigeration/job-fridge-door-ice-maker", "In-door ice maker opened up for testing"),
        ("refrigeration/job-fridge-condenser-fan-blade", "Condenser fan blade, a common cause of warm fridges"),
        ("refrigeration/job-tech-panel-ready-builtin-fridge", "Working inside a panel-ready built-in refrigerator"),
    ],
    "dishwasher-repair": [
        ("dishwashers/job-dishwasher-pulled-out", "Dishwasher pulled out of the cabinet to reach the pump and valve"),
        ("dishwashers/job-brand-maytag-dishwasher-circulation-pump", "Circulation pump under a Maytag dishwasher"),
        ("dishwashers/job-dishwasher-inlet-valve-underside", "Water inlet valve and hoses under the tub"),
        ("dishwashers/job-dishwasher-racks-open", "Racks and spray arms checked during diagnosis"),
        ("dishwashers/fisher-paykel-dishdrawer-double-overview-clear", "Fisher & Paykel DishDrawer on a service call"),
        ("dishwashers/job-brand-monogram-dishwasher", "GE Monogram panel dishwasher"),
        ("dishwashers/no-brand-dishwasher-door-open-racks-overview-clear", "Dishwasher running a test cycle"),
    ],
    "washing-machine-repair": [
        ("laundry/no-brand-washer-front-panel-removed-disassembled-clear", "Front panel off a front-load washer to reach the tub and boot"),
        ("laundry/no-brand-washer-drain-pump-in-hand-detail-clear", "Drain pump removed: the usual reason a washer won't drain"),
        ("laundry/no-brand-washer-drum-gasket-check-detail-clear", "Checking the door boot for tears and trapped debris"),
        ("laundry/job-washer-top-load-drive-motor", "Drive motor and pulley under a top-load washer"),
        ("laundry/no-brand-washer-inlet-valves-detail-clear", "Hot and cold inlet valves tested for flow"),
        ("laundry/job-washer-impeller-gloved", "Top-load washer impeller removed"),
        ("laundry/no-brand-washer-door-boot-inspection-detail-clear", "Front-load washer door boot pulled back for inspection"),
        ("laundry/job-brand-ge-front-load-washer", "GE front-load washer on a service call"),
    ],
    "dryer-repair": [
        ("laundry/job-dryer-blower-housing-lint", "Blower housing packed with lint, a fire risk and the cause of slow drying"),
        ("laundry/no-brand-dryer-drum-rollers-check-detail-clear", "Worn drum rollers: the source of thumping and squealing"),
        ("laundry/no-brand-dryer-belt-motor-pulley-detail-clear", "Drive belt and idler pulley under the drum"),
        ("laundry/job-dryer-gas-valve-multimeter", "Testing the gas valve coils with a multimeter"),
        ("laundry/job-dryer-burner-flame", "Dryer gas burner lit during a test"),
        ("laundry/no-brand-gas-dryer-heater-housing-lint-disassembled-clear", "Lint build-up inside a dryer cabinet"),
        ("laundry/no-brand-dryer-vent-duct-ceiling-detail-clear", "Rigid vent duct run to the ceiling exhaust"),
        ("laundry/job-dryer-lint-fire-damage", "Scorch marks left by lint near the heater"),
    ],
    "freezer-repair": [
        ("refrigeration/job-fridge-evaporator-iced-over-2", "Freezer evaporator frosted solid"),
        ("refrigeration/job-fridge-evaporator-bottom-freezer", "Bottom-freezer evaporator and defrost heater, panel off"),
        ("refrigeration/no-brand-refrigerator-evaporator-fan-detail-blurry", "Evaporator fan behind the freezer panel"),
        ("refrigeration/job-fridge-evaporator-defrost-heater", "Defrost heater and sensor on the evaporator"),
        ("refrigeration/no-brand-freezer-meter-diagnosis-detail-clear", "Meter readings taken inside the freezer"),
        ("refrigeration/job-fridge-ir-thermometer-34f", "Temperature check with an infrared thermometer"),
        ("refrigeration/job-fridge-ice-bin-crushed-ice", "Ice bin and dispenser chute checked"),
        ("refrigeration/no-brand-refrigerator-compressor-secop-detail-clear", "Compressor in a freezer machine compartment"),
    ],
    "microwave-repair": [
        ("cooking/Viking microwave magnetron replacement", "Viking microwave with the cabinet off: transformer, magnetron and board"),
        ("cooking/Viking microwave magnetron replacement damaged magnetron(burnt)", "Magnetron removed for replacement"),
        ("cooking/Viking microwave magnetron replacemen 1", "Testing the high-voltage circuit with a meter"),
        ("cooking/microwave-error-display", "Error code on the microwave display"),
        ("cooking/job-brand-viking-microwave", "Viking built-in microwave on a service call"),
        ("cooking/job-microwave-disassembled", "Built-in microwave opened on the counter"),
        ("cooking/wolf-microwave-wall-oven-column-overview-clear", "Built-in microwave above a wall oven"),
    ],
    "oven-repair": [
        ("cooking/job-oven-gas-burner-flame", "Gas oven burner lit after an igniter replacement"),
        ("cooking/job-oven-bake-element-red", "Bake element glowing during the heat test"),
        ("cooking/job-oven-broil-element-glow", "Broil element tested at full power"),
        ("cooking/no-brand-wall-oven-microwave-combo-pulled-out-disassembled-clear-2", "Wall oven pulled out of the cabinet on a cart"),
        ("cooking/job-oven-convection-blower-in-hand", "Convection blower removed for replacement"),
        ("cooking/no-brand-oven-broil-burner-flame-detail-clear", "Broiler flame checked through the oven door"),
        ("cooking/kitchenaid-superba-double-wall-oven-overview-clear", "Double wall oven on a service call"),
    ],
    "stove-cooktop-repair": [
        ("cooking/dacor range PCB replacement", "Dacor range with the cooktop lifted to reach the control board"),
        ("cooking/no-brand-gas-cooktop-top-removed-disassembled-clear", "Gas cooktop with burners removed"),
        ("cooking/no-brand-gas-cooktop-underside-wiring-disassembled-clear", "Gas lines and valves under a cooktop"),
        ("cooking/job-brand-thermador-star-burner", "Thermador star burner"),
        ("cooking/no-brand-electric-cooktop-radiant-elements-exposed-disassembled-clear", "Radiant elements under an electric glass cooktop"),
        ("cooking/no-brand-electric-glass-cooktop-overview-clear-2", "Electric glass cooktop on a service call"),
        ("cooking/no-brand-gas-rangetop-griddle-48-overview-clear", "Rangetop with griddle in a customer's kitchen"),
    ],
    "commercial-freezer-repair": [
        ("commercial/larkin-walk-in-cooler-evaporator-fan-detail-clear", "Walk-in cooler evaporator fan"),
        ("commercial/larkin-walk-in-cooler-evaporator-two-fans-detail-clear", "Walk-in evaporator with twin fans"),
        ("commercial/no-brand-commercial-ice-machine-gauges-sealed-system-disassembled-clear", "Condensing unit with gauges attached"),
        ("commercial/no-brand-walk-in-cooler-evaporator-coil-detail-clear", "Condenser coil on commercial refrigeration"),
        ("commercial/job-commercial-kitchen-line", "Restaurant kitchen line with reach-in refrigeration"),
    ],
    "ice-machine-repair": [
        ("commercial/hoshizaki-ice-machine-control-board-detail-clear-2", "Hoshizaki ice machine control board"),
        ("commercial/hoshizaki-ice-machine-model-label-detail-clear", "Hoshizaki data plate checked before ordering parts"),
        ("commercial/no-brand-commercial-ice-machine-evaporator-cubes-detail-clear", "Ice cubes in a commercial ice machine bin"),
        ("commercial/no-brand-commercial-ice-machine-condenser-fans-compressor-detail-clear", "Condenser fans and compressor on an ice machine"),
        ("commercial/no-brand-commercial-ice-machine-water-pump-detail-clear", "Water pump on a commercial ice machine"),
        ("commercial/no-brand-commercial-ice-machine-bin-open-overview-clear", "Stainless ice machine and bin on a service call"),
    ],
}

TEAM = [
    ("team/job-team-selfie-kitchen-3", "Two Fortex technicians after a repair in a customer's kitchen"),
    ("team/team-selfie-refrigerator-job-clear", "Fortex technicians on a refrigerator job"),
    ("team/job-team-selfie-kitchen-1", "Fortex technicians in branded shirts on a service call"),
    ("team/job-tools-dewalt-impact-driver", "Tools ready in the service van"),
]

# Extra photos used by brand pages: (photo, alt)
EXTRA = [
    ("refrigeration/thermador-built-in-refrigerator-model-label-detail-clear", "Thermador built-in refrigerator data plate"),
    ("refrigeration/thermador-bottom-freezer-refrigerator-model-label-detail-clear", "Thermador built-in refrigerator-freezer rating label"),
    ("refrigeration/sub-zero-refrigerator-model-label-detail-clear-2", "Sub-Zero model and serial label"),
    ("refrigeration/lg-instaview-refrigerator-door-detail-clear", "LG InstaView refrigerator on a service call"),
    ("refrigeration/job-brand-lg-fridge-control-board", "LG refrigerator main control board"),
    ("refrigeration/job-brand-samsung-fridge-compressor", "Samsung refrigerator compressor"),
    ("refrigeration/job-brand-samsung-fridge-control-board", "Samsung refrigerator control board"),
    ("refrigeration/job-brand-samsung-fridge-model-label", "Samsung refrigerator model label"),
    ("refrigeration/kitchenaid-built-in-refrigerator-wood-kitchen-overview-clear", "KitchenAid built-in refrigerator in a wood kitchen"),
    ("cooking/kitchenaid-double-wall-oven-overview-clear", "KitchenAid double wall oven"),
    ("cooking/kitchenaid-electric-cooktop-overview-clear", "KitchenAid electric cooktop"),
    ("refrigeration/no-brand-built-in-french-door-refrigerator-open-overview-clear", "Built-in refrigerator open for diagnosis"),
    ("laundry/job-brand-samsung-washer", "Samsung front-load washer"),
    ("laundry/job-brand-samsung-washer-open", "Samsung dryer with the front panel removed"),
    ("laundry/samsung-washer-control-panel-detail-clear", "Samsung washer control panel"),
    ("laundry/samsung-washer-top-load-overview-clear", "Samsung top-load washer"),
    ("laundry/samsung-washer-dryer-stack-overview-clear", "Samsung washer and dryer stack"),
    ("laundry/job-brand-samsung-dryer-hands", "Technician working on Samsung dryer wiring"),
    ("laundry/samsung-washer-dryer-stack-overview-clear-2", "Samsung stacked dryer on a service call"),
    ("laundry/job-brand-ge-top-load-washer", "GE top-load washer"),
    ("laundry/job-brand-ge-top-load-washer-controls", "GE top-load washer controls"),
    ("laundry/ge-washer-top-panel-open-control-board-disassembled-clear", "GE washer with the top panel off"),
    ("laundry/ge-washer-front-load-overview-clear", "GE front-load washer"),
    ("laundry/ge-profile-washer-dryer-stack-overview-clear", "Stacked washer and dryer on a service call"),
    ("laundry/job-brand-whirlpool-top-load-washer", "Whirlpool top-load washer"),
    ("laundry/job-washer-top-load-basket", "Top-load washer basket and agitator"),
    ("laundry/maytag-washer-front-load-overview-clear", "Front-load washer on a service call"),
    ("laundry/maytag-commercial-washer-top-load-panel-off-disassembled-clear", "Top-load washer opened up for repair"),
    ("laundry/no-brand-dryer-drum-roller-closeup-detail-clear", "Dryer drum roller up close"),
    ("laundry/no-brand-dryer-idler-pulley-old-new-detail-clear", "Dryer idler pulley"),
    ("laundry/job-dryer-gas-burner-meter", "Gas dryer burner assembly under test"),
    ("dishwashers/job-dishwasher-stainless-front", "Bosch stainless dishwasher on a service call"),
    ("dishwashers/job-brand-fisher-paykel-dishdrawer", "Fisher & Paykel DishDrawer"),
    ("refrigeration/bosch-side-by-side-refrigerator-open-overview-clear", "Bosch side-by-side refrigerator open on a service call"),
    ("dishwashers/bosch-dishwasher-model-label-detail-clear", "Bosch dishwasher model label"),
    ("dishwashers/bosch-dishwasher-pump-detail-blurry", "Pump and wiring under a Bosch dishwasher"),
    ("dishwashers/bosch-dishwasher-pump-area-detail-clear", "Base of a Bosch dishwasher opened to the pump"),
    ("commercial/hoshizaki-ice-machine-control-board-detail-clear", "Hoshizaki control board up close"),
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
    # Web slug from the file name: lower case, spaces and symbols to dashes
    # (the owner names files like "Thermador Range Overview.jpg").
    return re.sub(r"[^a-z0-9]+", "-", path.split("/", 1)[1].lower()).strip("-")


# slug -> (source under assets/photos, alt), same shape as images.JOB_PHOTOS
LIB_PHOTOS = {slug(p): (f"../photo-library/{p}.jpg", a) for p, a in _all().items()}
