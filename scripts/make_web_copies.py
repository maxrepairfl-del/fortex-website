#!/usr/bin/env python3
"""Make named web copies (AVIF/WebP/JPEG) of library photos listed in images.WEB_COPIES.

Originals stay untouched. EXIF orientation is applied; nothing is upscaled.
Run: python3 scripts/make_web_copies.py
"""
import json, os, sys
from PIL import Image, ImageOps
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from site_gen import images as M  # noqa: E402
OUT = os.path.join(ROOT, "dist", "images"); os.makedirs(OUT, exist_ok=True)
meta = M.load_meta()
for slug, (rel, _alt, *crop) in M.WEB_COPIES.items():
    im = ImageOps.exif_transpose(Image.open(os.path.join(ROOT, "assets", rel))).convert("RGB")
    for opt in crop:  # extra options: an int rotates (degrees CCW), a 4-tuple crops
        im = im.rotate(opt, expand=True) if isinstance(opt, int) else im.crop(opt)
    big = None
    for w in M.WEB_WIDTHS:
        w = min(w, im.width)
        r = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS) if w < im.width else im
        for ext, kw in (("jpg", dict(quality=78, optimize=True, progressive=True)),
                        ("webp", dict(quality=76, method=6)), ("avif", dict(quality=60))):
            r.save(os.path.join(OUT, f"{slug}-{w}.{ext}"), **kw)
        big = r.size
    meta[slug] = list(big)
    print(slug, big)
json.dump(meta, open(M.META_PATH, "w"), indent=0, sort_keys=True)
