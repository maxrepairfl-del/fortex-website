"""Third batch (2026-11-21, owner): KitchenAid and Monogram brand pages and
built-in refrigerator pages for KitchenAid, Viking and Monogram, so the
refrigerator page's "Repair by brand" row covers them.

Photos: only frames where the brand is readable on the photo itself. There is
no Viking or Monogram refrigerator photo yet, so those pages use the
technician portrait and the cards show an icon. Prices are the same estimated
built-in ranges as the Thermador refrigerator page (not Fortex job statistics).
"""
from .brand_data2 import BUILTIN_FRIDGE_PRICES

_BUILTIN_CAUSES = [
    ("Fresh-food section warm", "Dusty condenser behind the top grille, evaporator fan, defrost fault, sealed system", "Clean and test airflow, check fans and defrost, then read the sealed system"),
    ("Frost on the back wall", "Defrost heater, sensor or control, or a door that doesn't seal", "Test the defrost circuit, check the gasket and door closure"),
    ("No ice or no water", "Water valve, ice maker, frozen fill tube, filter", "Test the valve and ice maker, clear the fill line, check the filter"),
    ("Door won't close by itself", "Worn hinge or closer, heavy panel that has dropped", "Replace the worn part, realign the door"),
    ("Runs nonstop or loud", "Condenser fan or dirty condenser, evaporator fan", "Check airflow at the grille and both fans"),
]

KA_BUILTIN = "kitchenaid-built-in-refrigerator-wood-kitchen-overview-clear"

NEW_BRANDS3 = {
    "kitchenaid": {
        "name": "KitchenAid", "maker": "Whirlpool Corporation",
        "title": "KitchenAid Appliance Repair in Orange County",
        "meta": "KitchenAid built-in refrigerator, wall oven, range, cooktop and microwave repair in Orange County. Price agreed before work. $80 service call free with repair.",
        "lead": "KitchenAid built-in and French door refrigerators, wall ovens, ranges, cooktops and microwaves. Warm refrigerators, ice makers, ovens that won't heat, igniters and control boards.",
        "photo": KA_BUILTIN, "photo_2": "kitchenaid-double-wall-oven-overview-clear",
        "products": [
            ("refrigerator", "Built-in refrigerators", "Built-in side-by-side and bottom-freezer, plus French door.", "/services/refrigerator-repair/kitchenaid/"),
            ("oven", "Wall ovens", "Single, double and microwave combination ovens.", "/services/oven-repair/"),
            ("oven", "Ranges & cooktops", "Gas, dual-fuel and electric.", "/services/stove-cooktop-repair/"),
            ("microwave", "Microwaves", "Over-the-range and built-in.", "/services/microwave-repair/"),
        ],
        "product_photos": [KA_BUILTIN, "kitchenaid-double-wall-oven-overview-clear",
                           "kitchenaid-electric-cooktop-overview-clear", "kitchenaid-microwave-over-range-overview-clear"],
        "parts_line": "Compressors and fans, defrost and ice maker parts, bake and broil elements, igniters, sensors and control boards",
        "prices": [("Built-in refrigerator", BUILTIN_FRIDGE_PRICES)],
        "faqs": [
            ("Do you repair KitchenAid built-in refrigerators in place?", "Often, yes. Many repairs are done in place; some need the unit pulled out, and we tell you before we start."),
            ("Are you a KitchenAid factory-authorized service?", "No. We are an independent, licensed repair company. If your appliance is still under the factory warranty, use the manufacturer's service first."),
        ],
    },
    "monogram": {
        "name": "Monogram", "maker": "GE Appliances",
        "title": "Monogram Appliance Repair in Orange County",
        "meta": "Monogram built-in refrigerator, wall oven, range, microwave and dishwasher repair in Orange County. Price agreed before work. $80 service call free with repair.",
        "lead": "Monogram built-in and column refrigerators, wall ovens and ranges, microwaves and Advantium ovens, and dishwashers. Warm sections, ice makers, ovens that won't heat and control faults.",
        "photo": "job-brand-monogram-dishwasher", "photo_2": "tech-portrait",
        "products": [
            ("refrigerator", "Built-in refrigerators", "Side-by-side, bottom-freezer, French door and columns.", "/services/refrigerator-repair/monogram/"),
            ("oven", "Wall ovens & ranges", "Gas, electric and dual-fuel.", "/services/oven-repair/"),
            ("microwave", "Microwaves & Advantium", "Built-in, drawer and speed ovens.", "/services/microwave-repair/"),
            ("dishwasher", "Dishwashers", "Stainless and panel-ready.", "/services/dishwasher-repair/"),
        ],
        "product_photos": [None, None, None, "job-brand-monogram-dishwasher"],
        "parts_line": "Compressors and fans, defrost and ice maker parts, bake and broil elements, igniters, sensors, pumps and control boards",
        "prices": [("Built-in refrigerator", BUILTIN_FRIDGE_PRICES)],
        "faqs": [
            ("Do you repair Monogram built-in refrigerators in place?", "Often, yes. Many repairs are done in place; some need the unit pulled out, and we tell you before we start. Panel-ready doors are realigned afterwards."),
            ("Are you a Monogram factory-authorized service?", "No. We are an independent, licensed repair company. If your appliance is still under the factory warranty, use the manufacturer's service first."),
        ],
    },
}


def _combo(brand, h1_brand, lead, meta, photo, extra_faq):
    return {
        "noun": f"{brand} refrigerator", "icon": "refrigerator",
        "h1": f"{h1_brand} Refrigerator Repair in Orange County",
        "meta": meta, "lead": lead, "photo": photo, "prices": BUILTIN_FRIDGE_PRICES,
        "symptoms": ["Fresh-food section warm", "Frost building up inside", "Ice maker or water dispenser not working",
                     "Door won't close by itself", "Running nonstop or loud", "Error or alarm on the display"],
        "causes": _BUILTIN_CAUSES,
        "gallery": [],
        "faqs": [
            (f"How much does {brand} refrigerator repair cost?", ""),
            extra_faq,
            (f"Are you a {brand} factory-authorized service?", "No. We are an independent, licensed repair company. If your refrigerator is still under the factory warranty, use the manufacturer's service first."),
        ],
    }


NEW_COMBOS3 = {
    ("kitchenaid", "refrigerator-repair"): _combo(
        "KitchenAid", "KitchenAid Built-In",
        "Built-in side-by-side and bottom-freezer KitchenAid refrigerators, plus French door models: a warm fresh-food section, frost, an ice maker that quit or a door that won't close. Repaired in your kitchen.",
        "KitchenAid built-in refrigerator repair in Orange County: warm sections, frost, ice makers, doors. $80 service call, free with repair. Price agreed before work.",
        KA_BUILTIN,
        ("Can you repair a built-in KitchenAid without removing it?", "Often, yes. Many repairs are done in place; some need the unit pulled out, and we tell you before we start.")),
    ("viking", "refrigerator-repair"): _combo(
        "Viking", "Viking Built-In",
        "Viking built-in side-by-side, bottom-freezer and column refrigerators: a warm section, frost, ice maker and dispenser faults, doors that won't close. Repaired in your kitchen.",
        "Viking built-in refrigerator repair in Orange County: warm sections, frost, ice makers, doors. $80 service call, free with repair. Price agreed before work.",
        "tech-portrait",
        ("Can you repair a built-in Viking without removing it?", "Often, yes. Many repairs are done in place; some need the unit pulled out, and we tell you before we start. Panels are realigned afterwards.")),
    ("monogram", "refrigerator-repair"): _combo(
        "Monogram", "Monogram Built-In",
        "Monogram built-in side-by-side, bottom-freezer, French door and column refrigerators: a warm section, frost, ice maker and dispenser faults, doors that won't close. Repaired in your kitchen.",
        "Monogram built-in refrigerator repair in Orange County: warm sections, frost, ice makers, doors. $80 service call, free with repair. Price agreed before work.",
        "tech-portrait",
        ("Can you repair a panel-ready Monogram without damaging the cabinets?", "Yes. Many repairs are done in place; some need the unit pulled out. Either way we protect the floor and panels and realign the door so the panel sits flush.")),
}
