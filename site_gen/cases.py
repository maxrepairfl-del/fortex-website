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
        "body": [
            ("p", "This Viking microwave had stopped heating food, and the customer was seeing sparks inside. That can look pretty alarming, so we opened it up to find out what was going on."),
            ("p", "The problem turned out to be the magnetron, the part that generates the microwave energy used to heat food. Once we removed it, the damage to its antenna cap was clearly visible in the photo."),
            ("photo", "viking-microwave-magnetron-damaged-cap", "Damaged antenna cap on the removed magnetron."),
            ("p", "We checked the fuses and sensors as well, rather than stopping at the visibly damaged part."),
            ("p", "Fortunately, we had a compatible replacement magnetron in stock. That made a big difference for this job: we could replace it and finish the repair that same day, without making the customer wait for a part to arrive."),
            ("photo", "viking-microwave-interior", "Internal view of the microwave during magnetron replacement."),
            ("p", "After replacing the magnetron, we checked the microwave’s operation before wrapping up the visit."),
            ("photo", "viking-microwave-front", "Viking microwave during the service visit."),
            ("p", "One thing we always remind customers: don’t run a microwave empty. It needs food or a suitable load inside to absorb the energy it produces. That doesn’t mean you need to add water to everything you heat. Just follow the instructions for your appliance."),
            ("p", "We can’t say that running it empty caused the damage in this particular case. But if you see sparks, stop the microwave rather than running it again to see whether they disappear."),
            ("p", 'For this customer, having the right part available meant we could take care of the problem in one visit. This was one of our <a href="/services/microwave-repair/">microwave repair</a> visits.'),
        ],
    },
    {
        "id": "oven-control-board-bake-element",
        "service": "oven-repair",
        "title": "Oven Control Board and Bake Element Replacement: A Repair Story",
        "detail": "Dacor range",
        "card_desc": "How we discussed original and aftermarket parts with the owner, and why reaching the board took more than four hours of work.",
        "photo": "dacor-range-overview",
        "body": [
            ("p", "The owner told us this Dacor range had worked for about 20 years before its first breakdown. They wanted to keep it, so we took a look at what it would need."),
            ("photo", "dacor-range-overview", "Dacor range during the service visit."),
            ("p", "We found heat damage at the power-wire connector on the control board. The connection on the board was burned, and a relay on the board had failed too. The oven’s bake element was also worn and no longer performing as it should."),
            ("photo", "dacor-range-control-board-heat-damage", "Original control board with heat damage at a wiring connection."),
            ("p", "We explained that the control board needed replacing to get the range working properly, and we strongly recommended replacing the bake element as well."),
            ("p", "With both parts priced as original replacements, plus the work needed to install them, the total was more than the customer wanted to spend. They asked a fair question: was there a sensible way to bring the cost down?"),
            ("p", "For the board, there was. We found a lower-cost aftermarket replacement made to fit this application, with a one-year warranty. It was available as a direct replacement, so we wouldn’t have to adapt a different board to make it work. Given the relatively straightforward design of this board, we felt it was a reasonable option to discuss with the customer."),
            ("photo", "dacor-range-aftermarket-control-board", "Aftermarket replacement control board installed during the repair."),
            ("p", "Our recommendation for the bake element was different."),
            ("p", "We didn’t have a direct aftermarket replacement available for this model. It might have been possible to find something with similar dimensions and resistance, but that would still leave questions about how it would fit and distribute heat inside the oven. We didn’t feel that was a good place to experiment just to save on the part."),
            ("p", 'So we talked through the difference: an aftermarket board made for the application was one option; adapting a merely similar heating element was another. We recommended the original bake element, and the customer chose to go ahead with the aftermarket board and original element. This <a href="/services/oven-repair/">oven repair</a> involved both the control board and the bake element.'),
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
    return f"/our-work/#{c['id']}"


def _fig(slug, cap):
    full = f"/images/{slug}-{widths_for(slug)[-1]}.jpg"
    return (f'<figure class="story__photo"><a href="{full}" aria-label="Open larger photo: {esc(cap)}">'
            f'{picture(slug, sizes="(max-width:700px) 92vw, 460px")}</a>'
            f'<figcaption>{esc(cap)}</figcaption></figure>')


def render_story(c):
    parts = []
    for item in c["body"]:
        parts.append(f"<p>{item[1]}</p>" if item[0] == "p" else _fig(item[1], item[2]))
    return f"""<article class="story" id="{c['id']}">
  <p class="eyebrow">Repair story · {esc(c['detail'])}</p>
  <h2>{esc(c['title'])}</h2>
  {''.join(parts)}
</article>"""


def story_index():
    """Compact list of stories at the top of /our-work/."""
    return "".join(case_card(c, link_label="Read the story", href=f"#{c['id']}") for c in CASES)


def case_card(c, link_label="Read the repair story", href=None):
    return f"""<a class="case-card" href="{href or case_url(c)}">
  <div class="case-card__img">{picture(c['photo'], sizes="(max-width:700px) 92vw, 220px")}</div>
  <div class="case-card__text"><p class="eyebrow">Repair story</p><h3>{esc(c['title'])}</h3>
    <p>{esc(c['card_desc'])}</p><span class="more-link">{esc(link_label)} {icon('arrow-right', size=16)}</span></div>
</a>"""


def service_case_section(slug):
    """One compact card on a service page, after 'What is usually behind it'."""
    c = CASES_BY_SERVICE.get(slug)
    if not c:
        return ""
    return f"""<section class="section section--tight"><div class="wrap">{case_card(c)}</div></section>"""
