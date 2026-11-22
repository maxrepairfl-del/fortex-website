"""Repair stories: posts inside /our-work/ (owner briefs of 2026-11-21).

Each story is published once, as a section of /our-work/ with its own anchor.
Service pages show one compact card linking to that anchor. Story text is the
owner-approved copy; photo markers were replaced by the photos themselves.
Do not add facts here that the briefs did not supply (no model, city, date,
price, test results or service-life promises).
"""
from .components import esc
from .images import picture, widths_for
from .icons import icon

# Each body item is ("p", html) or ("photo", slug, caption).
CASES = [
    {
        "id": "microwave-not-heating-sparking",
        "service": "microwave-repair",
        "title": "Microwave Not Heating and Sparking: A Repair Story",
        "detail": "Viking microwave",
        "card_desc": "A damaged magnetron, a replacement already in stock, and a repair completed in one visit.",
        "photo": "viking-microwave-front",
        "preview": ("viking-microwave-front", "Viking microwave during the service visit.", None),
        "body": [
            ("p", "This Viking microwave had stopped heating food, and the customer was seeing sparks inside. That can look pretty alarming, so we opened it up to find out what was going on."),
            ("p", "The problem turned out to be the magnetron, the part that generates the microwave energy used to heat food. Once we removed it, the damage to its antenna cap was clearly visible in the photo."),
            ("photo", "viking-microwave-magnetron-damaged-cap", "Damaged antenna cap on the removed magnetron."),
            ("p", "We checked the fuses and sensors as well, rather than stopping at the visibly damaged part."),
            ("p", "Fortunately, we had a compatible replacement magnetron in stock. That made a big difference for this job: we could replace it and finish the repair that same day, without making the customer wait for a part to arrive."),
            ("photo", "viking-microwave-interior", "Internal view of the microwave during magnetron replacement."),
            ("p", "After replacing the magnetron, we checked the microwave’s operation before wrapping up the visit."),
            ("p", "One thing we always remind customers: don’t run a microwave empty. It needs food or a suitable load inside to absorb the energy it produces. That doesn’t mean you need to add water to everything you heat. Just follow the instructions for your appliance."),
            ("p", "We can’t say that running it empty caused the damage in this particular case. But if you see sparks, stop the microwave rather than running it again to see whether they disappear."),
            ("p", 'For this customer, having the right part available meant we could take care of the problem in one visit. This was one of our microwave repair visits.'),
        ],
    },
    {
        "id": "oven-control-board-bake-element",
        "service": "oven-repair",
        "title": "Oven Control Board and Bake Element Replacement: A Repair Story",
        "detail": "Dacor range",
        "card_desc": "How we discussed original and aftermarket parts with the owner, and why reaching the board took more than four hours of work.",
        "photo": "dacor-range-overview",
        "preview": ("dacor-range-overview", "Dacor range during the service visit.", None),
        "body": [
            ("p", "The owner told us this Dacor range had worked for about 20 years before its first breakdown. They wanted to keep it, so we took a look at what it would need."),
            ("p", "We found heat damage at the power-wire connector on the control board. The connection on the board was burned, and a relay on the board had failed too. The oven’s bake element was also worn and no longer performing as it should."),
            ("photo", "dacor-range-control-board-heat-damage", "Original control board with heat damage at a wiring connection."),
            ("p", "We explained that the control board needed replacing to get the range working properly, and we strongly recommended replacing the bake element as well."),
            ("p", "With both parts priced as original replacements, plus the work needed to install them, the total was more than the customer wanted to spend. They asked a fair question: was there a sensible way to bring the cost down?"),
            ("p", "For the board, there was. We found a lower-cost aftermarket replacement made to fit this application, with a one-year warranty. It was available as a direct replacement, so we wouldn’t have to adapt a different board to make it work. Given the relatively straightforward design of this board, we felt it was a reasonable option to discuss with the customer."),
            ("photo", "dacor-range-aftermarket-control-board", "Aftermarket replacement control board installed during the repair."),
            ("p", "Our recommendation for the bake element was different."),
            ("p", "We didn’t have a direct aftermarket replacement available for this model. It might have been possible to find something with similar dimensions and resistance, but that would still leave questions about how it would fit and distribute heat inside the oven. We didn’t feel that was a good place to experiment just to save on the part."),
            ("p", 'So we talked through the difference: an aftermarket board made for the application was one option; adapting a merely similar heating element was another. We recommended the original bake element, and the customer chose to go ahead with the aftermarket board and original element. This oven repair involved both the control board and the bake element.'),
            ("p", "Getting those parts installed was a job in itself."),
            ("p", "The board looked as though it would be easy to reach behind the front panel. But seeing it and having enough room to replace it turned out to be two different things. We had to lift the cooktop assembly and continue taking things apart from there. Even the photo with the top lifted only shows part of the access work."),
            ("photo", "dacor-range-cooktop-lifted", "Cooktop assembly lifted during access to the control board."),
            ("p", "With tubing, wiring, and older components around the board, we worked carefully through the disassembly. The repair took more than four hours."),
            ("p", "The photo of the glowing bake element shows the new original part heating during the service visit."),
            ("photo", "dacor-oven-bake-element-heating", "New original bake element heating during service."),
            ("p", "After roughly 20 years of use, this range was worth having a conversation about before deciding to replace it. We couldn’t promise another 20 years, but we could explain the options and help the owner choose a repair they were comfortable with."),
            ("p", "That meant being clear about which part was original, which was aftermarket, and why we recommended each one."),
        ],
    },
]
CASES_BY_SERVICE = {c["service"]: c for c in CASES}


def case_url(c):
    """Where the full story lives: on its service page (owner, 2026-11-21:
    Our Work is an overview by appliance with short cards; each full story is
    published once, on the page of the appliance it is about)."""
    return f"/services/{c['service']}/#{c['id']}"


# ------------------------------------------------- dryer page (owner briefs 2026-11-21)
# Replaces the old cause table on /services/dryer-repair/. Four visible topics,
# each with its approved story collapsed under a title and one line. The
# stories live on the service page only (not in Our Work). Approved copy
# verbatim; facts limited to what the owner confirmed. Photo items are
# ("photo", slug, caption[, alt]) where alt overrides the default when the same
# frame appears in two stories (heating and noise share LG photos; that is not
# presented as two separate jobs).
DRYER_TOPICS = [
    {
        "id": "dryer-not-heating", "title": "Dryer Not Heating",
        "intro": "We check the heating parts, controls and airflow before recommending any part.",
        "stories": [{
            "id": "dryer-igniter-lint-repair",
            "title": "Not Heating: Damaged Igniter and Overheating",
                "card_desc": "We found a damaged igniter, a faulty high-limit thermostat, and lint restricting airflow.",
                "preview": ('dryer-story-burner-lint', 'Burner area after partial lint removal.', 'Gas dryer burner area after partial lint removal during diagnosis'),
            "body": [
                ("p", "When we opened this gas dryer, we found heavy lint buildup around the burner. The igniter had partly broken apart, but that wasn’t the only thing that needed attention."),
                ("photo", "dryer-story-lg-front", "The LG dryer during the service visit."),
                ("p", "By the time we took the burner-area photo, we had already vacuumed away much of the lint around the burner. You can still see what remained."),
                ("p", "Lint was restricting airflow, and we also found that the high-limit thermostat wasn’t cutting off the heat properly. That thermostat is there to help protect the dryer from overheating."),
                ("p", "Simply fitting a new igniter would have left those other problems in place. We replaced the igniter, high-limit thermostat, thermal fuse, and temperature sensor, and cleaned the affected areas inside the dryer."),
                ("p", "We also checked the drum rollers. They had buildup around them, but we found no damage that called for replacement. We cleaned them as part of the service rather than add unnecessary parts to the repair bill. After servicing, the drum ran without the extra squeaking or rattling."),
                ("photo", "dryer-story-after-cleaning", "The same dryer after internal cleaning."),
                ("p", "Some stubborn dark staining remained on the metal. We removed the lint and debris, but didn’t try to polish every hidden surface back to a shine. The goal was to address the buildup and repair the faults we found, rather than make the inside look brand new."),
                ("p", "This is why we look beyond the first damaged part. A dryer not heating can involve more than the part that produces or starts the heat."),
                ("p", "Our advice? Clean the lint screen after every load. If clothes start taking longer to dry, don’t just keep adding another cycle. And if you notice a burning smell, stop using the dryer and have it checked."),
            ],
        }],
    },
    {
        "id": "dryer-not-drying", "title": "Dryer Not Drying Clothes",
        "intro": "A dryer can turn and heat but still leave clothes damp when airflow is lost.",
        "stories": [
            {
                "id": "dryer-airflow-blocked",
                "title": "Not Drying: Lint Blocking the Internal Airflow",
                "card_desc": "The components were working. Clearing the lint blockage and servicing the dryer was all it needed.",
                "preview": ('dryer-story-lint-opening', 'Lint had covered almost the entire opening, leaving only a few small holes visible.', 'Lint almost completely covering an internal dryer air opening'),
                "body": [
                    ("p", "Here’s another situation we see: a dryer isn’t drying clothes properly, but nothing actually needs replacing. The problem is lint blocking the airflow."),
                    ("p", "That’s what we found here. We checked the components, and they were working. So we gave the dryer a thorough service: cleaned the rollers, cleared the blockages, vacuumed the inside, and ran it afterward to check its operation."),
                    ("p", "No replacement parts were needed. This time, maintenance was enough."),
                    ("p", "A small tip from us: clean the lint screen after every load. If drying starts taking longer even with a clean screen, there may be a blockage farther along the airflow path."),
                ],
            },
            {
                "id": "dryer-vent-clogged",
                "title": "Not Drying: Clogged Dryer Vent",
                "card_desc": "The dryer was heating, but lint in the exhaust duct was restricting airflow.",
                "preview": ('dryer-story-duct-lint', 'Lint buildup inside the duct connected to the dryer.', 'Lint buildup inside a dryer exhaust connection'),
                "body": [
                    ("p", "Sometimes the dryer is working, but the clothes still aren’t drying properly. That was the situation here: nothing in the dryer needed replacing, but lint had built up in the exhaust path."),
                    ("p", "We found buildup in the connecting duct and at the wall connection. The dryer could produce heat, but the restricted airflow was stopping it from carrying the moist air away properly."),
                    ("photo", "dryer-story-wall-connection", "The exhaust connection during inspection."),
                    ("p", "No appliance parts needed replacing. What was needed was dryer vent cleaning to clear the blockage, rather than a repair inside the dryer."),
                    ("p", "How quickly a dryer vent collects lint varies from home to home. On service visits, we’ve seen heavily blocked vents after around five years, and others that were still relatively clear after much longer. That doesn’t mean it’s a good idea to wait until drying stops."),
                    ("p", "The length of the exhaust duct, the number of bends, how often the dryer is used, and the installation all make a difference. A long run to a roof outlet can create more resistance to airflow than a short, direct route outside."),
                    ("p", "A small tip: cleaning the lint screen doesn’t replace dryer vent cleaning. The general recommendation is to clean the exhaust duct once a year, or sooner if drying starts taking longer."),
                    ("p", "We inspect dryer vent restrictions and clean dryer vents that exit through an exterior side wall. We do not clean vents that exit through the roof. We’ll explain what we find and the work needed before proceeding."),
                ],
            },
            {
                "id": "dryer-blower-wheel-cracked",
                "title": "Heating but Not Drying: Cracked Blower Wheel",
                "card_desc": "The drum turned and the dryer heated, but a cracked blower wheel wasn’t moving enough air.",
                "preview": ('dryer-story-blower-wheel', 'The damaged blower wheel after removal.', 'Removed dryer blower wheel found cracked during diagnosis'),
                "body": [
                    ("p", "We started with a quick airflow check. A paper towel held at the intake wasn’t being pulled against it as we would expect. Something wasn’t moving air properly. The question was why."),
                    ("p", "We checked for lint blockages and looked at the drive components. Finding the answer took more disassembly than expected on this GE stacked washer-dryer."),
                    ("photo", "dryer-story-ge-stack-open", "Opening up the dryer to investigate the airflow problem."),
                    ("p", "The blower wheel was still turning, which made the fault easy to miss. But it wasn’t turning consistently with the motor. Once we removed it, we found that it had cracked."),
                    ("p", "That explained why the dryer could seem to be working while still leaving clothes damp. This wasn’t a blockage that cleaning would solve. The blower wheel needed replacing."),
                    ("p", "The drum was turning, the heat was there, but the cracked blower wheel wasn’t moving enough air. That was the missing piece."),
                ],
            },
        ],
    },
    {
        "id": "dryer-making-noise", "title": "Dryer Making Noise",
        "intro": "We check for buildup and wear before deciding what needs replacing.",
        "stories": [{
            "id": "dryer-squeak-rollers-serviced",
            "title": "Squeaking Noise: Buildup Around the Drum Rollers",
            "card_desc": "Hair and lint were restricting the rollers. Cleaning and servicing resolved the noise without new rollers.",
            "preview": ('dryer-story-rollers-before', 'Inside the dryer before cleaning and servicing.', 'Dryer interior with lint buildup and drum-support rollers visible'),
            "body": [
                ("p", "This dryer was making noise, but the drum rollers themselves were still in good condition. Hair and lint had collected around them, making it harder for them to turn freely."),
                ("photo", "dryer-story-lg-front", "The LG dryer during the service visit.", "Dark LG dryer during the service visit"),
                ("p", "Once we opened it up, we could check the rollers and their shafts rather than assume they all needed replacing."),
                ("p", "We removed the buildup, cleaned the rollers and their shafts, and checked them for wear. There was no damage that called for replacement, so we serviced the existing parts and tested the dryer afterward."),
                ("p", "The noise was gone. No new rollers were needed."),
                ("photo", "dryer-story-after-cleaning", "After internal cleaning and servicing.", "Dryer interior after cleaning and servicing"),
                ("p", "That isn’t always how it goes. If a roller has stopped turning and developed a flat spot, or its shaft has worn a groove, cleaning won’t undo that damage. Those parts need replacing."),
                ("p", "A small tip from us: don’t wait for a squeak to become a loud grinding or thumping noise. Having it checked early may mean the existing parts can still be serviced, as they could here."),
            ],
        }],
    },
    {
        "id": "dryer-not-spinning", "title": "Dryer Not Spinning",
        "intro": "A stopped drum does not always mean a failed motor.",
        "stories": [{
            "id": "dryer-blower-jammed-motor-ok",
            "title": "Not Spinning: A Blocked Blower",
            "card_desc": "Lint had jammed the blower. Clearing the blockages resolved the problem without replacing the motors.",
            "preview": ('dryer-story-blower-passage', 'Lint packed into the internal passage leading toward the blower.', 'Lint packed into an internal dryer duct leading toward the blower'),
            "body": [
                ("p", "In these two repairs, lint buildup had jammed the blower. The dryers had stopped turning, but neither needed a new motor."),
                ("p", "In the first dryer, we found a torn lint screen that had been letting lint through. Over time, the buildup interfered with the blower’s rotation. On this design, the same motor drives the blower and the drum belt, so a jammed blower can stop the drum too."),
                ("p", "A torn lint screen also needs attention so it does not keep allowing lint into the dryer. Clearing the blockage alone does not resolve that issue."),
                ("p", "We found a similar blockage in another dryer:"),
                ("photo", "dryer-story-second-blockage", "Lint and hair buildup found during another service visit."),
                ("p", "Both owners stopped using their dryers and called when they noticed the drum wasn’t turning. We cleared the blockages and cleaned the affected areas. The motors were still working, so no motor replacement was needed."),
                ("p", "Sometimes a dryer in this condition can still turn while empty, then struggle or stop once wet clothes are added. That doesn’t necessarily mean the load is too large. Something may be making the motor work harder than it should."),
                ("p", "Our advice? If the drum stops turning, don’t keep restarting the dryer, try to help it along by hand, or work around the problem with smaller loads. Have it checked. Catching a blockage before it causes further damage may keep a straightforward cleaning from becoming a more expensive repair."),
            ],
        }],
    },
]


def _story_body(items, sizes="(max-width:700px) 92vw, 560px"):
    out = []
    for item in items:
        if item[0] == "p":
            out.append(f"<p>{item[1]}</p>")
        else:
            slug, cap = item[1], item[2]
            alt = item[3] if len(item) > 3 else None
            full = f"/images/{slug}-{widths_for(slug)[-1]}.jpg"
            out.append(f'<figure class="story__photo"><a href="{full}" aria-label="Open larger photo: {esc(cap)}">'
                       f'{picture(slug, sizes=sizes, alt=alt)}</a><figcaption>{esc(cap)}</figcaption></figure>')
    return "".join(out)


def story_card(c, heading="h4"):
    """One repair story as a card (UX brief 2026-11-21).

    Collapsed, it already shows the preview photo, a symptom-and-cause title,
    one line and "See this repair". Opening it adds the rest of the story and
    photos below; the preview is not repeated inside. The whole story is in
    the HTML, and a link to #id opens it (static/js/main.js)."""
    slug, cap, alt = c["preview"]
    return f"""<details class="story story--card" id="{c['id']}">
      <summary class="story__head">
        <{heading} class="story__title">{esc(c['title'])}</{heading}>
        <figure class="story__thumb">{picture(slug, sizes="(max-width:600px) 92vw, 180px", alt=alt)}<figcaption>{esc(cap)}</figcaption></figure>
        <div class="story__sum"><p>{esc(c['card_desc'])}</p>
          <span class="story__toggle"><span class="story__open">See this repair</span><span class="story__close">Hide details</span> {icon('arrow-right', size=18)}</span></div>
      </summary>
      <div class="story__body">{_story_body(c['body'])}
        <button type="button" class="story__hide" data-story-close>Hide details {icon('arrow-right', size=18)}</button></div>
    </details>"""


def dryer_problems_section():
    groups = []
    for t in DRYER_TOPICS:
        intro = f'<p class="problem-group__intro">{esc(t["intro"])}</p>' if t.get("intro") else ""
        single = ' data-open-single' if len(t["stories"]) == 1 else ""
        groups.append(f"""<div class="problem-group" id="{t['id']}"{single}>
    <h3 class="problem-group__title">{esc(t['title'])}</h3>{intro}
    {''.join(story_card(c) for c in t['stories'])}
  </div>""")
    return f"""<section class="section section--stories"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Likely causes</p>
    <h2>Common Dryer Problems: A Look at Our Repairs</h2></div>
  {''.join(groups)}
</div></section>"""


SERVICE_STORY_HEAD = {
    "microwave-repair": "A recent microwave repair",
    "oven-repair": "A recent oven repair",
}


def service_story_section(slug):
    """The full repair story on its own service page, after the cause table."""
    c = CASES_BY_SERVICE.get(slug)
    if not c:
        return ""
    return f"""<section class="section section--tight"><div class="wrap">
  <div class="problem-group" data-open-single>
    <h2 class="problem-group__title">{esc(SERVICE_STORY_HEAD[slug])}</h2>
    {story_card(c, heading="h3")}
  </div>
</div></section>"""


def our_work_examples():
    """Our Work: an overview by appliance. Short cards only; each links to the
    full story on its service page. The card ids keep the old links
    /our-work/#microwave-not-heating-sparking and #oven-control-board-bake-element
    working (a fragment never reaches the server, so no redirect is possible)."""
    cards = ""
    for c in CASES:
        slug = c["preview"][0]
        cards += f"""<a class="case-card" id="{c['id']}" href="{case_url(c)}">
  <div class="case-card__img">{picture(slug, sizes="(max-width:700px) 92vw, 220px")}</div>
  <div class="case-card__text"><p class="eyebrow">{esc(c['detail'])}</p><h3>{esc(c['title'])}</h3>
    <p>{esc(c['card_desc'])}</p><span class="more-link">Read the repair story {icon('arrow-right', size=16)}</span></div>
</a>"""
    dryer = ""
    for t in DRYER_TOPICS:
        subs = "".join(f'<li><a href="/services/dryer-repair/#{s["id"]}">{esc(s["title"])}</a></li>'
                       for s in t["stories"])
        dryer += (f'<li><a href="/services/dryer-repair/#{t["id"]}"><strong>{esc(t["title"])}</strong></a>'
                  f'<ul>{subs}</ul></li>')
    return f"""<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Repair stories</p><h2>Repair examples by appliance</h2>
    <p class="lede">Short summaries of real jobs. Each full story, with all the photos, is on the page for that appliance.</p></div>
  <div class="case-cards">{cards}</div>
  <div class="work-examples" id="dryer-repair-examples">
    <h3>Dryer repair examples</h3>
    <ul class="work-examples__list">{dryer}</ul>
    <p><a class="more-link" href="/services/dryer-repair/#dryer-not-heating">All dryer repair stories {icon('arrow-right', size=16)}</a></p>
  </div>
</div></section>"""
