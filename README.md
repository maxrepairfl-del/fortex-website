# Fortex Appliance Repair — Website

A fast, custom-coded **static website** for Fortex Appliance Repair (Orange County, CA).
No frameworks and no build toolchain to install — pages are assembled by a small
Python generator, and images are optimized with macOS's built-in `sips`.

- **Premium + bold-conversion design** — big real photos, brand red + slate, click-to-call everywhere.
- **26 pages**: Home, Services index + 12 appliance pages, Service Areas index + 5 city pages,
  How It Works, About, Reviews, Book Online + Thank-You, and a 404.
- **Local SEO**: per-appliance and per-city pages, schema.org (LocalBusiness, Service, FAQ, Review),
  sitemap, OG tags, fast responsive images.
- **Custom booking form** that posts to Netlify Forms (emails you each lead).

## How it's organized

```
website/
  assets/            # original source images (logo, 28 photos, brand graphics)
  site_gen/          # the generator
    data.py          # ALL site content/copy — edit here
    images.py        # photo manifest + responsive <img> helper
    icons.py         # inline SVG icons + logo mark
    components.py    # header, footer, hero, cards, document shell, SEO/schema
    pages.py         # one renderer per page type
  scripts/
    optimize_images.py  # sips → responsive JPEG/PNG variants
  static/            # styles.css, main.js, favicon.svg
  build.py           # renders everything into dist/
  serve.py           # local preview server
  dist/              # ← generated output you deploy
```

## Build

```bash
cd website
python3 scripts/optimize_images.py   # once, or whenever photos change (uses sips)
python3 build.py                     # rebuild all HTML/CSS/JS into dist/
```

## Preview locally

```bash
python3 serve.py 8092
# open http://127.0.0.1:8092
```

## Edit content

Almost everything lives in **`site_gen/data.py`**: phone/email, services, symptoms, FAQs,
cities, reviews, brands. Change the text, run `python3 build.py`, refresh. To add a service
or city, copy an entry in `SERVICES` / `CITIES` — the page is generated automatically.

## Deploy (Vercel)

The repo <https://github.com/maxrepairfl-del/fortex-website> is connected to the Vercel
project `fortex-website` (team `fortex5`) and deploys automatically on push to `main`.

Images are generated locally with `sips` (macOS only), so **`dist/` is committed** and
Vercel serves it as-is — there is no build step on Vercel. `vercel.json` sets
`outputDirectory: dist` plus long-cache headers.

To ship a change:

```bash
python3 build.py
git add -A && git commit -m "Update site" && git push
```

### Lead capture

Both forms POST to the Formspree endpoint in `SITE["form_endpoint"]` (`site_gen/data.py`),
with `_next` pointing at `/book/thank-you/`. **`build.py` refuses to build while that value
is empty** — an unwired form would silently swallow every lead. Log in at
<https://formspree.io> to see submissions and set the notification email.

## Before launch — confirm these (see `data.py`, marked `FIXME`)

1. **Lead email** for booking submissions.
2. **Transparent logo** (SVG/PNG) if available — currently a hand-built SVG mark is used.
3. **Real review quotes** + Yelp/Google profile URLs.
4. **Service-area cities** to target (5 built; more are easy to add).
5. **Business hours** (currently "7 days, 8am–8pm").
6. **Social links** (Instagram/Facebook) for the footer.
7. Optional: compress the 256 MB process video (needs `ffmpeg`) for a hero/section loop.
