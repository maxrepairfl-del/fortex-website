"""Second batch of appliance x brand pages (2026-11-12): only brands we have
our own job photos for. Prices: same sources as brand_data.py; Thermador
refrigerator, Bosch, Fisher & Paykel and Hoshizaki are estimates by class."""
from .brand_data import WASHER_PRICES, DRYER_PRICES

DISHWASHER_PRICES = [
    ("Drain pump", "$190 – $340"),
    ("Leak in the base pan / float switch", "$220 – $380"),
    ("Main control board", "$220 – $420"),
    ("Heating element + thermostat", "$180 – $300"),
    ("Water inlet valve", "$180 – $260"),
    ("Circulation pump / wash motor", "$220 – $420"),
    ("Door latch or door springs", "$180 – $260"),
]
DISHDRAWER_PRICES = [
    ("Drawer control board / motor", "$280 – $520"),
    ("Drain pump", "$200 – $360"),
    ("Lid actuator / lid seal", "$220 – $400"),
    ("Water inlet valve", "$180 – $300"),
    ("Drawer slides or cable harness", "$220 – $420"),
]
BUILTIN_FRIDGE_PRICES = [
    ("Compressor / sealed system", "$750 – $1,500"),
    ("Main control board", "$420 – $850"),
    ("Evaporator or condenser fan", "$260 – $480"),
    ("Ice maker", "$260 – $520"),
    ("Defrost heater + sensor", "$220 – $420"),
    ("Door hinge / closer", "$250 – $500"),
    ("Door gasket", "$180 – $380"),
]
ICE_MACHINE_PRICES = [
    ("Descale, sanitize and clean", "$250 – $450"),
    ("Water pump", "$250 – $450"),
    ("Water inlet valve", "$220 – $400"),
    ("Float switch or thermistor", "$200 – $380"),
    ("Condenser fan motor", "$250 – $450"),
    ("Control board", "$450 – $850"),
    ("Compressor / sealed system", "$1,200 – $2,500"),
]

NEW_BRANDS = {
    "ge": {
        "name": "GE", "maker": "GE Appliances",
        "title": "GE Appliance Repair in Orange County",
        "meta": "GE, GE Profile and Café washer, dryer, refrigerator, range and microwave repair in Orange County. $80 service call free with repair.",
        "lead": "GE, GE Profile and Café washers, dryers, refrigerators, ranges and microwaves. Washers that won't spin or drain, fridges warming up, ranges that won't heat.",
        "photo": "ge-washer-front-load-overview-clear", "photo_2": "job-brand-ge-top-load-washer",
        "products": [
            ("washer", "Washers", "Front-load and top-load GE and GE Profile washers.", "/services/washing-machine-repair/ge/"),
            ("dryer", "Dryers", "Electric and gas dryers.", "/services/dryer-repair/"),
            ("refrigerator", "Refrigerators", "French-door, side-by-side and bottom-freezer.", "/services/refrigerator-repair/"),
            ("oven", "Ranges & microwaves", "Gas and electric ranges, wall ovens, over-the-range microwaves.", "/services/stove-cooktop-repair/"),
        ],
        "product_photos": [None, "ge-profile-washer-dryer-stack-overview-clear", None, None],
        "parts_line": "Drain pumps, lid locks, shift actuators, control boards and heaters",
        "prices": WASHER_PRICES[:4] + DRYER_PRICES[:2],
        "faqs": [
            ("Do you repair GE Profile and Café appliances?", "Yes. GE Profile and Café use the same service parts as GE, and we repair all three."),
            ("Do you use original GE parts?", "Yes, OEM parts from authorized distributors, with 1 year on parts and 90 days on labor."),
            ("Can you fix a GE washer that won't spin?", "Usually in one visit: the common causes are the lid lock, the shift actuator on top-loaders, the drain pump or the belt."),
        ],
    },
    "whirlpool": {
        "name": "Whirlpool", "maker": "Whirlpool Corporation",
        "title": "Whirlpool Appliance Repair in Orange County",
        "meta": "Whirlpool washer, dryer, refrigerator, dishwasher and range repair in Orange County. OEM parts, price before work. $80 service call free with repair.",
        "lead": "Whirlpool top-load and front-load washers, dryers, refrigerators, dishwashers and ranges. Washers that won't agitate or spin, dryers that won't heat, fridges warming up.",
        "photo": "job-brand-whirlpool-top-load-washer", "photo_2": "job-washer-top-load-drive-motor",
        "products": [
            ("washer", "Washers", "Top-load and front-load, including Cabrio and Duet.", "/services/washing-machine-repair/whirlpool/"),
            ("dryer", "Dryers", "Electric and gas dryers.", "/services/dryer-repair/"),
            ("refrigerator", "Refrigerators", "French-door, side-by-side and top-freezer.", "/services/refrigerator-repair/"),
            ("dishwasher", "Dishwashers", "Drain, wash and leak problems.", "/services/dishwasher-repair/"),
        ],
        "product_photos": [None, "no-brand-dryer-drum-rollers-check-detail-clear", None, "job-brand-maytag-dishwasher-circulation-pump"],
        "parts_line": "Drive motors, couplers, lid locks, pumps, belts and control boards",
        "prices": WASHER_PRICES[:4] + DRYER_PRICES[:2],
        "faqs": [
            ("Do you repair Maytag, KitchenAid and Amana too?", "Yes. They are made by Whirlpool and share most service parts, and we repair all of them."),
            ("Do you use original Whirlpool parts?", "Yes, OEM parts from authorized distributors, with 1 year on parts and 90 days on labor."),
            ("Is an older Whirlpool washer worth fixing?", "Usually. Most Whirlpool washer repairs are a part under $500, far less than a new machine. We tell you honestly if it isn't worth it."),
        ],
    },
    "bosch": {
        "name": "Bosch", "maker": "BSH Home Appliances Corporation",
        "title": "Bosch Dishwasher & Appliance Repair in Orange County",
        "meta": "Bosch dishwasher repair in Orange County: E15 and E24 errors, not draining, not heating, leaking. Bosch refrigerators and ranges too. $80 service call free with repair.",
        "lead": "Bosch dishwashers first of all: E15 leak errors, E24 drain errors, no heat, no wash. We also repair Bosch refrigerators, ranges and wall ovens.",
        "photo": "job-dishwasher-stainless-front", "photo_2": "bosch-dishwasher-pump-detail-blurry",
        "products": [
            ("dishwasher", "Dishwashers", "100, 300, 500, 800 Series and Benchmark.", "/services/dishwasher-repair/bosch/"),
            ("refrigerator", "Refrigerators", "French-door and counter-depth.", "/services/refrigerator-repair/"),
            ("oven", "Ranges & wall ovens", "Gas, electric and induction.", "/services/oven-repair/"),
        ],
        "product_photos": [None, "bosch-side-by-side-refrigerator-open-overview-clear", None],
        "parts_line": "Drain pumps, circulation pumps, heaters, float switches, door springs and control boards",
        "prices": DISHWASHER_PRICES,
        "faqs": [
            ("What does E15 mean on a Bosch dishwasher?", "Water in the base pan has tripped the float switch. The dishwasher stops to prevent a flood. We find the leak, fix it and dry the base."),
            ("What does E24 mean?", "The dishwasher can't drain: usually a clogged filter, a blocked drain hose or a failed drain pump."),
            ("Do you use original Bosch parts?", "Yes, OEM parts from authorized distributors, with 1 year on parts and 90 days on labor."),
        ],
    },
    "fisher-paykel": {
        "name": "Fisher & Paykel", "maker": "Fisher & Paykel Appliances",
        "title": "Fisher & Paykel Appliance Repair in Orange County",
        "meta": "Fisher & Paykel DishDrawer repair in Orange County: drawer won't close or start, not draining, error codes. $80 service call free with repair.",
        "lead": "Single and double DishDrawer dishwashers: a drawer that won't start or lock, water left in the bottom, error codes and leaks. We also repair Fisher & Paykel refrigerators and ranges.",
        "photo": "job-brand-fisher-paykel-dishdrawer", "photo_2": "tech-portrait",
        "products": [
            ("dishwasher", "DishDrawer dishwashers", "Single and double drawers, integrated and stainless.", "/services/dishwasher-repair/fisher-paykel/"),
            ("refrigerator", "Refrigerators", "Integrated and freestanding.", "/services/refrigerator-repair/"),
            ("oven", "Ranges & cooktops", "Gas, induction and dual-fuel.", "/services/stove-cooktop-repair/"),
        ],
        "product_photos": [None, None, None],  # L273 is KitchenAid (owner 2026-11-21)
        "parts_line": "Drawer motors and boards, drain pumps, lid actuators, seals and cable harnesses",
        "prices": DISHDRAWER_PRICES,
        "faqs": [
            ("Can one drawer fail while the other works?", "Yes. Each DishDrawer has its own pump and board, so one drawer can stop while the other keeps working."),
            ("Why won't my DishDrawer close or start?", "Often a lid actuator, a worn cable harness that flexes with the drawer, or a control board fault. We test before replacing."),
            ("Do you use original Fisher & Paykel parts?", "Yes, OEM parts from authorized distributors, with 1 year on parts and 90 days on labor."),
        ],
    },
    "hoshizaki": {
        "name": "Hoshizaki", "maker": "Hoshizaki America, Inc.",
        "title": "Hoshizaki Repair in Orange County",
        "meta": "Hoshizaki ice machine repair for restaurants, bars and offices in Orange County: low ice, no ice, leaks, cleaning and descaling. Commercial service.",
        "lead": "Hoshizaki cubers, flakers and undercounter ice machines for restaurants, bars, offices and clinics. Low ice, no ice, leaks, slow harvest, cleaning and descaling.",
        "photo": "hoshizaki-ice-machine-undercounter-overview-clear", "photo_2": "hoshizaki-ice-machine-control-board-detail-clear-2",
        "products": [
            ("ice", "Cubers & flakers", "Modular heads, self-contained and undercounter units.", "/services/ice-machine-repair/hoshizaki/"),
            ("commercial-freezer", "Commercial refrigeration", "Reach-ins, prep tables and walk-ins.", "/services/commercial-freezer-repair/"),
        ],
        "parts_line": "Water pumps, inlet valves, float switches, thermistors, fan motors and control boards",
        "prices": ICE_MACHINE_PRICES,
        "faqs": [
            ("How often should a Hoshizaki be cleaned?", "Every 6 months at minimum, more often with hard water. Scale is the most common cause of low ice and slow harvest."),
            ("Do you service restaurants and bars?", "Yes, commercial ice machines and refrigeration across Orange County."),
            ("Do you use original Hoshizaki parts?", "Yes, OEM parts from authorized distributors."),
        ],
    },
}

NEW_COMBOS = {
    ("thermador", "refrigerator-repair"): {
        "noun": "Thermador refrigerator", "icon": "refrigerator",
        "h1": "Thermador Refrigerator Repair in Orange County",
        "meta": "Thermador Freedom and built-in refrigerator repair in Orange County: not cooling, ice maker, frost, door alignment. $80 service call free with repair.",
        "lead": "Freedom column and built-in Thermador refrigerators and freezers: a warm fresh-food column, frost on the back wall, an ice maker that quit or a door that won't close flush. Serviced in place.",
        "photo": "tech-portrait", "prices": BUILTIN_FRIDGE_PRICES,  # L273 is KitchenAid, not Thermador (owner 2026-11-21); no clean Thermador fridge shot yet
        "symptoms": ["Refrigerator or freezer column warm", "Frost building up inside", "Ice maker not making ice", "Door won't close flush or seal", "Fan noise or clicking", "Error or alarm on the display"],
        "causes": [
            ("Column warm", "Dirty condenser, evaporator fan, defrost fault, sealed system", "Clean and test airflow, check fans and defrost, read pressures"),
            ("Frost inside", "Defrost heater, sensor or door seal", "Test the defrost circuit, check the gasket"),
            ("No ice", "Water valve, ice maker module, frozen fill tube", "Test the valve and module, clear the fill line"),
            ("Door not flush", "Hinge or closer, panel alignment", "Adjust or replace the hinge, re-align the panel"),
            ("Alarm / error", "Sensor or control board", "Read the fault, test sensors before the board"),
        ],
        "gallery": [
            ("thermador-built-in-refrigerator-model-label-detail-clear", "Thermador built-in refrigerator data plate"),
            ("thermador-bottom-freezer-refrigerator-model-label-detail-clear", "Rating label checked before ordering parts"),
            ("no-brand-built-in-french-door-refrigerator-open-overview-clear", "Built-in refrigerator open for diagnosis"),
        ],
        "faqs": [
            ("How much does Thermador refrigerator repair cost?", "Most repairs fall between $180 and $850: fans, defrost parts, ice makers, hinges and boards. Sealed-system work runs $750 to $1,500. You get the exact price before any work."),
            ("Can you repair a Freedom column without removing it?", "Yes, columns are serviced in place and the panels re-aligned afterwards."),
            ("Do you use original Thermador parts?", "Yes, OEM parts from authorized distributors, with 1 year on parts and 90 days on labor."),
        ],
    },
    ("samsung", "washing-machine-repair"): {
        "noun": "Samsung washer", "icon": "washer",
        "h1": "Samsung Washer Repair in Orange County",
        "meta": "Samsung washer not draining, not spinning, 4C / 5C / UE / dC error, door locked? Samsung front-load and top-load repair in Orange County.",
        "lead": "Water left in the drum, a washer that won't spin or shakes, error codes and a door that stays locked. We repair Samsung front-load, top-load and stacked units.",
        "photo": "job-brand-samsung-washer", "prices": WASHER_PRICES,
        "symptoms": ["5C or SE error, won't drain", "4C error, won't fill", "UE / UB, won't spin or shakes", "dC or LO, door won't lock or unlock", "Loud banging during spin", "Leaking under the machine"],
        "causes": [
            ("5C / won't drain", "Clogged pump filter, failed drain pump", "Clear the filter, test and replace the pump"),
            ("4C / won't fill", "Inlet valve, low water pressure, clogged screens", "Check the screens and pressure, test the valve"),
            ("UE / shaking", "Unbalanced load, worn shocks or suspension rods", "Check the load and suspension, replace worn parts"),
            ("dC / door", "Door lock assembly or latch", "Test the lock and switch, replace the lock"),
            ("Banging on spin (top-load)", "Suspension rods, worn tub dampers", "Replace the rods and dampers"),
        ],
        "gallery": [
            ("samsung-washer-control-panel-detail-clear", "Samsung washer control panel"),
            ("samsung-washer-top-load-overview-clear", "Samsung top-load washer"),
        ],
        "faqs": [
            ("How much does Samsung washer repair cost?", "Most Samsung washer repairs fall between $160 and $520: drain pump, inlet valve, door lock, suspension and boards. Bearings and tub seal run $350 to $640."),
            ("What does 5C mean on a Samsung washer?", "It can't drain. Clean the filter behind the small door at the bottom front first; if the code comes back, the pump or hose is the cause."),
            ("Do you fix Samsung top-loaders that bang during spin?", "Yes, usually worn suspension rods. It's a common Samsung top-load repair."),
        ],
    },
    ("samsung", "dryer-repair"): {
        "noun": "Samsung dryer", "icon": "dryer",
        "h1": "Samsung Dryer Repair in Orange County",
        "meta": "Samsung dryer not heating, HE / hE / tS error, not tumbling, squeaking? Samsung electric and gas dryer repair in Orange County.",
        "lead": "No heat, HE or tS errors, long dry times, squeaks and a drum that won't turn. We repair Samsung electric and gas dryers and measure the airflow while we're there.",
        "photo": "samsung-washer-dryer-stack-overview-clear-2", "prices": DRYER_PRICES,
        "symptoms": ["Runs but doesn't heat", "HE / hE heating error", "tS or tO sensor error", "Takes two cycles to dry", "Squeaking or thumping", "Drum doesn't turn"],
        "causes": [
            ("No heat / HE", "Thermal fuse, high-limit thermostat, heating element or gas coils", "Test each part, find why the fuse blew"),
            ("tS / tO", "Thermistor or wiring", "Measure the thermistor, check the harness"),
            ("Long dry times", "Restricted airflow, weak heat", "Measure airflow and heat. If the house duct is blocked, it needs a vent-cleaning service"),
            ("Squeak / thump", "Drum rollers, idler pulley, glides", "Replace worn rollers and glides"),
            ("Drum won't turn", "Belt, idler or motor", "Replace the belt or idler, test the motor"),
        ],
        "gallery": [
            ("job-brand-samsung-dryer-hands", "Technician working on Samsung dryer wiring"),
            ("dryer-ir", "Measuring dryer temperature during diagnosis"),
            ("no-brand-dryer-drum-roller-closeup-detail-clear", "Worn dryer drum roller"),
        ],
        "faqs": [
            ("How much does Samsung dryer repair cost?", "Most Samsung dryer repairs fall between $160 and $380: thermal fuse, element, thermostat, belt and rollers. A control board runs $280 to $520."),
            ("Why does my Samsung dryer keep blowing the fuse?", "Almost always restricted airflow. We measure it every time and tell you if the house duct needs a vent-cleaning service; we do not clean ducts ourselves."),
            ("Do you repair Samsung gas dryers?", "Yes, igniters, gas valve coils and flame sensors."),
        ],
    },
    ("ge", "washing-machine-repair"): {
        "noun": "GE washer", "icon": "washer",
        "h1": "GE Washer Repair in Orange County",
        "meta": "GE washer won't spin, drain or agitate, lid lock blinking, error codes? GE and GE Profile front-load and top-load washer repair in Orange County.",
        "lead": "Top-loaders that won't spin or agitate, a blinking lid lock, front-loaders that won't drain, leaks and noise. We repair GE and GE Profile washers.",
        "photo": "ge-washer-front-load-overview-clear", "prices": WASHER_PRICES,
        "symptoms": ["Won't spin or agitate", "Lid lock light blinking", "Won't drain", "Leaking", "Loud noise during spin", "Stops mid-cycle"],
        "causes": [
            ("Won't spin / agitate", "Shift actuator, lid lock, drive belt or motor", "Test the actuator and lock, check the drive"),
            ("Lid lock blinking", "Lid lock assembly or wiring", "Test the lock and harness, replace the lock"),
            ("Won't drain", "Drain pump, clogged hose", "Clear the hose, test the pump"),
            ("Leaking", "Pump seal, hoses, tub seal", "Trace the leak, replace the failed part"),
            ("Noise on spin", "Bearings, suspension", "Confirm by hand, quote the fix"),
        ],
        "gallery": [
            ("job-brand-ge-front-load-washer", "GE front-load washer on a service call"),
            ("job-brand-ge-top-load-washer", "GE top-load washer"),
            ("job-brand-ge-top-load-washer-controls", "GE top-load washer controls"),
            ("ge-washer-top-panel-open-control-board-disassembled-clear", "GE washer with the top panel off"),
        ],
        "faqs": [
            ("How much does GE washer repair cost?", "Most GE washer repairs fall between $160 and $520: lid lock, shift actuator, drain pump, valves and boards. Bearings run $350 to $640."),
            ("My GE top-loader fills but won't agitate. Why?", "Most often the shift actuator or the lid lock. Both are tested in one visit."),
            ("Do you repair GE Profile washers?", "Yes, GE Profile uses the same service parts."),
        ],
    },
    ("whirlpool", "washing-machine-repair"): {
        "noun": "Whirlpool washer", "icon": "washer",
        "h1": "Whirlpool Washer Repair in Orange County",
        "meta": "Whirlpool washer won't spin, drain or agitate, lid lock flashing, F codes? Whirlpool top-load and front-load washer repair in Orange County.",
        "lead": "Top-loaders that won't agitate or spin, a flashing lid lock, F-codes, front-loaders that won't drain and loud spins. We repair Whirlpool, Cabrio and Duet washers.",
        "photo": "job-brand-whirlpool-top-load-washer", "prices": WASHER_PRICES,
        "symptoms": ["Won't agitate", "Won't spin", "Lid lock flashing", "F-code on the display", "Won't drain", "Grinding or loud spin"],
        "causes": [
            ("Won't agitate", "Motor coupler, drive block, shifter", "Inspect the coupler and drive, replace the worn part"),
            ("Won't spin", "Lid switch or lock, belt, motor", "Test the lock and motor, check the belt"),
            ("Lid lock flashing", "Lid lock assembly", "Test and replace the lock"),
            ("Won't drain", "Drain pump, clogged hose", "Clear the hose, test the pump"),
            ("Grinding", "Bearings, gearcase", "Confirm the source, quote the repair"),
        ],
        "gallery": [
            ("job-washer-top-load-basket", "Top-load washer basket and agitator"),
            ("job-washer-top-load-drive-motor", "Drive motor and pulley under a top-loader"),
            ("job-washer-impeller-gloved", "Washer impeller removed"),
            ("maytag-commercial-washer-top-load-panel-off-disassembled-clear", "Top-load washer opened up for repair"),
        ],
        "faqs": [
            ("How much does Whirlpool washer repair cost?", "Most Whirlpool washer repairs fall between $160 and $520: coupler, lid lock, pump, valves and boards. Bearings or a gearcase run $350 to $640."),
            ("Do you repair Maytag and Kenmore washers too?", "Yes. Many share Whirlpool parts, and we repair them all."),
            ("Can you fix it the same day?", "Often: couplers, lid locks and pumps are on the van."),
        ],
    },
    ("bosch", "dishwasher-repair"): {
        "noun": "Bosch dishwasher", "icon": "dishwasher",
        "h1": "Bosch Dishwasher Repair in Orange County",
        "meta": "Bosch dishwasher E15, E24, E22 error, not draining, not drying, leaking? Bosch dishwasher repair in Orange County. $80 service call free with repair.",
        "lead": "E15 leak errors, E24 drain errors, dishes left wet or dirty, a door that falls open. We repair all Bosch dishwasher series and dry out the base properly.",
        "photo": "job-dishwasher-stainless-front", "prices": DISHWASHER_PRICES,
        "symptoms": ["E15: water in the base", "E24 / E25: won't drain", "E22: filter blocked", "Dishes not clean or not dry", "Door falls open", "Won't start"],
        "causes": [
            ("E15", "Leak into the base pan: pump seal, hose, door gasket", "Find and fix the leak, dry the base, reset the float"),
            ("E24 / E25", "Clogged filter or drain hose, drain pump", "Clear the filter and hose, test the pump"),
            ("Not cleaning", "Circulation pump, spray arms, heater", "Test the pump and heater, clean the arms"),
            ("Door falls open", "Broken door springs or cables", "Replace springs and cables on both sides"),
            ("Won't start", "Door latch, control board", "Test the latch first, then the board"),
        ],
        "gallery": [
            ("bosch-dishwasher-model-label-detail-clear", "Bosch dishwasher model label"),
            ("bosch-dishwasher-pump-detail-blurry", "Pump and wiring under a Bosch dishwasher"),
            ("bosch-dishwasher-pump-area-detail-clear", "Base of a Bosch dishwasher opened to the pump"),
            ("job-dishwasher-inlet-valve-underside", "Inlet valve and hoses under the tub"),
        ],
        "faqs": [
            ("How much does Bosch dishwasher repair cost?", "Most Bosch repairs fall between $180 and $420: drain pump, leak repair, heater, valve, springs and boards."),
            ("Can I clear E15 myself?", "Tilting the machine can empty the base, but the leak is still there. It will come back until the leak is fixed."),
            ("Do you use original Bosch parts?", "Yes, OEM parts from authorized distributors, with 1 year on parts and 90 days on labor."),
        ],
    },
    ("fisher-paykel", "dishwasher-repair"): {
        "noun": "Fisher & Paykel DishDrawer", "icon": "dishwasher",
        "h1": "Fisher & Paykel DishDrawer Repair in Orange County",
        "meta": "Fisher & Paykel DishDrawer won't start, won't close, not draining, error code? Single and double DishDrawer repair in Orange County.",
        "lead": "A drawer that won't start or lock, water left in the bottom, beeping and error codes, leaks. We repair single and double DishDrawers, integrated and stainless.",
        "photo": "job-brand-fisher-paykel-dishdrawer", "prices": DISHDRAWER_PRICES,
        "symptoms": ["Drawer won't start", "Lid doesn't close or seal", "Water left in the drawer", "Beeping / error code", "One drawer works, the other doesn't", "Leaking"],
        "causes": [
            ("Won't start", "Lid actuator, control board, harness", "Test the actuator and harness, then the board"),
            ("Water left", "Drain pump, filter", "Clear the filter, test the pump"),
            ("One drawer dead", "That drawer's board, motor or cable", "Test that drawer's parts on their own"),
            ("Leaking", "Lid seal, hoses", "Replace the seal or hose"),
            ("Error codes", "Sensor, valve or motor fault", "Read the code, test the named part"),
        ],
        # job-brand-fisher-paykel-dishdrawer, fisher-paykel-dishdrawer-double-overview-clear and -33 are the
        # same frame (L132) at different sizes: no gallery until there are other
        # real, different photos (owner brief, 2026-11-20).
        "gallery": [],
        "faqs": [
            ("How much does DishDrawer repair cost?", "Most repairs fall between $180 and $520: drain pump, lid actuator and seal, valve, motor and boards."),
            ("Is a DishDrawer worth fixing?", "Usually. A new DishDrawer is expensive and has to fit the same cabinet opening, so a repair is almost always cheaper."),
            ("Do you use original parts?", "Yes, OEM parts from authorized distributors."),
        ],
    },
    ("hoshizaki", "ice-machine-repair"): {
        "noun": "Hoshizaki ice machine", "icon": "ice",
        "h1": "Hoshizaki Ice Machine Repair in Orange County",
        "meta": "Hoshizaki ice machine low ice, no ice, leaking, slow harvest? Commercial Hoshizaki repair, cleaning and descaling in Orange County.",
        "lead": "Low ice, no ice, a machine that runs but won't harvest, leaks and scale. We repair and clean Hoshizaki cubers, flakers and undercounter units for restaurants, bars and offices.",
        "photo": "hoshizaki-ice-machine-undercounter-overview-clear", "prices": ICE_MACHINE_PRICES,
        "symptoms": ["Low ice production", "No ice at all", "Ice cubes small or cloudy", "Long or failed harvest", "Water leaking", "Machine runs but bin stays empty"],
        "causes": [
            ("Low ice", "Scale on the evaporator, dirty condenser", "Descale and sanitize, clean the condenser"),
            ("No ice", "Water valve, pump, float switch, board", "Test water supply and pump, read the board"),
            ("Small / cloudy cubes", "Water pump, scale, low water", "Check the pump and water flow, descale"),
            ("Harvest fails", "Thermistor, hot-gas valve", "Test the thermistor and valve"),
            ("Leaking", "Drain line, pump, water tank", "Trace and fix the leak"),
        ],
        "gallery": [
            ("hoshizaki-ice-machine-control-board-detail-clear-2", "Hoshizaki control board under test"),
            ("hoshizaki-ice-machine-control-board-detail-clear", "Hoshizaki control board up close"),
            ("hoshizaki-ice-machine-model-label-detail-clear", "Hoshizaki data plate"),
            ("no-brand-commercial-ice-machine-water-pump-detail-clear", "Water pump on a commercial ice machine"),
        ],
        "faqs": [
            ("How much does Hoshizaki repair cost?", "Most repairs fall between $200 and $850: cleaning and descaling, pumps, valves, sensors, fan motors and boards. Sealed-system work runs $1,200 to $2,500."),
            ("How often should it be descaled?", "Every 6 months, more often with hard water. Scale is the most common cause of low ice."),
            ("Do you offer regular cleaning for restaurants?", "Yes, ask us about scheduled cleaning when you book."),
        ],
    },
}
