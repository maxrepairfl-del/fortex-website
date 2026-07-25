#!/usr/bin/env python3
"""Build the Fortex static site into dist/.

Renders every page, copies static assets, and writes sitemap.xml, robots.txt,
the web manifest, and Netlify config. Does NOT touch dist/images (run
scripts/optimize_images.py for those).

Usage:
  python3 scripts/optimize_images.py   # once, or when photos change
  python3 build.py                     # rebuild HTML/CSS/JS
"""
import datetime
import os
import shutil

from site_gen.pages import all_pages
from site_gen.data import SITE

if not SITE.get("form_endpoint"):
    raise SystemExit(
        "Refusing to build: SITE['form_endpoint'] is empty in site_gen/data.py.\n"
        "The booking and quote forms would post nowhere and drop every lead "
        "without showing the customer an error.\n"
        "Create a form at https://formspree.io, then set form_endpoint to its "
        "URL (e.g. https://formspree.io/f/xdkoblqz)."
    )

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
STATIC = os.path.join(ROOT, "static")
YEAR = datetime.date.today().year
TODAY = datetime.date.today().isoformat()

# Paths excluded from the sitemap (utility/thank-you/error pages)
NOINDEX = {"/book/thank-you/", "/404.html"}


def write(path, content):
    full = os.path.join(DIST, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def copy_static():
    for sub in ("css", "js", "img"):
        src = os.path.join(STATIC, sub)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(DIST, sub), dirs_exist_ok=True)


def canonical_of(path):
    # "/services/index.html" -> "/services/"
    p = "/" + path.lstrip("/")
    if p.endswith("/index.html"):
        p = p[: -len("index.html")]
    return p


def write_sitemap(paths):
    urls = []
    for p in sorted(set(paths)):
        if p in NOINDEX:
            continue
        prio = "1.0" if p == "/" else ("0.8" if (p.startswith("/services/") or p.startswith("/areas/")) else "0.6")
        urls.append(
            f"  <url><loc>{SITE['url']}{p}</loc><lastmod>{TODAY}</lastmod>"
            f"<changefreq>weekly</changefreq><priority>{prio}</priority></url>"
        )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(urls) + "\n</urlset>\n")
    write("/sitemap.xml", xml)


def write_meta_files():
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n")
    write("/site.webmanifest", (
        '{\n'
        f'  "name": "{SITE["name"]}",\n'
        '  "short_name": "Fortex",\n'
        '  "start_url": "/",\n'
        '  "display": "standalone",\n'
        '  "background_color": "#ffffff",\n'
        '  "theme_color": "#E11B22",\n'
        '  "icons": [\n'
        '    { "src": "/img/favicon.svg", "type": "image/svg+xml", "sizes": "any" },\n'
        '    { "src": "/img/apple-touch-icon.png", "type": "image/png", "sizes": "180x180" }\n'
        '  ]\n}\n'
    ))
    # Vercel serves dist/ as-is; 404.html is picked up automatically and the
    # cache headers live in vercel.json at the repo root.


def make_apple_icon():
    """Rasterize the favicon to a 180x180 PNG via sips, if possible."""
    import subprocess
    svg = os.path.join(STATIC, "img", "favicon.svg")
    out = os.path.join(DIST, "img", "apple-touch-icon.png")
    try:
        subprocess.run(["sips", "-s", "format", "png", "-z", "180", "180", svg, "--out", out],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return os.path.exists(out)
    except Exception:
        return False


def clean_dist():
    """Remove generated output but keep dist/images (expensive to rebuild)."""
    if not os.path.isdir(DIST):
        return
    for entry in os.listdir(DIST):
        if entry == "images":
            continue
        path = os.path.join(DIST, entry)
        shutil.rmtree(path) if os.path.isdir(path) else os.remove(path)


def main():
    os.makedirs(DIST, exist_ok=True)
    clean_dist()
    pages = all_pages()
    paths = []
    for path, html in pages:
        html = html.replace("{year}", str(YEAR))
        write(path, html)
        paths.append(canonical_of(path))
    copy_static()
    write_sitemap(paths)
    write_meta_files()
    icon_ok = make_apple_icon()

    n_imgs = len(os.listdir(os.path.join(DIST, "images"))) if os.path.isdir(os.path.join(DIST, "images")) else 0
    print(f"Built {len(pages)} pages -> dist/")
    for p in sorted(canonical_of(x[0]) for x in pages):
        print(f"  {p}")
    print(f"Static copied. apple-touch-icon: {'ok' if icon_ok else 'skipped'}. "
          f"dist/images variants: {n_imgs}")
    print("Run a local preview with:  cd dist && python3 -m http.server 8080")


if __name__ == "__main__":
    main()
