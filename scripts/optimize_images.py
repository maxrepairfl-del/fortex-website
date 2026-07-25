#!/usr/bin/env python3
"""Generate responsive web images from the originals using macOS `sips`.

For every photo in the manifest we emit JPEGs at each width in images.WIDTHS
(PNGs for transparent brand graphics) into dist/images/, then record the
largest variant's pixel dimensions in _image_meta.json so the page builder can
set width/height and avoid layout shift.

Run: python3 scripts/optimize_images.py [--force]
"""
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from site_gen import images as M  # noqa: E402

ASSETS = os.path.join(ROOT, "assets")
PHOTOS_DIR = os.path.join(ASSETS, "photos")
OUT = os.path.join(ROOT, "dist", "images")
FORCE = "--force" in sys.argv


def needs_build(src, dst):
    if FORCE or not os.path.exists(dst):
        return True
    return os.path.getmtime(src) > os.path.getmtime(dst)


def sips_resize(src, dst, width, fmt):
    cmd = ["sips", "-s", "format", fmt]
    if fmt == "jpeg":
        cmd += ["-s", "formatOptions", str(M.JPEG_QUALITY)]
    cmd += ["-Z", str(width), src, "--out", dst]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def dims(path):
    out = subprocess.run(
        ["sips", "-g", "pixelWidth", "-g", "pixelHeight", path],
        capture_output=True, text=True, check=True,
    ).stdout
    w = h = 0
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("pixelWidth:"):
            w = int(line.split(":")[1])
        elif line.startswith("pixelHeight:"):
            h = int(line.split(":")[1])
    return w, h


def jobs():
    """Yield (slug, src_path, fmt, ext) for every manifest entry."""
    for slug, (fname, _alt) in M.PHOTOS.items():
        yield slug, os.path.join(PHOTOS_DIR, fname), "jpeg", "jpg"
    for slug, (relpath, _alt) in M.BRAND.items():
        src = os.path.join(ASSETS, relpath)
        if relpath.lower().endswith(".png"):
            yield slug, src, "png", "png"
        else:
            yield slug, src, "jpeg", "jpg"


def build_one(job):
    slug, src, fmt, ext = job
    if not os.path.exists(src):
        print(f"  !! missing source: {src}")
        return None
    made = 0
    for w in M.WIDTHS:
        dst = os.path.join(OUT, f"{slug}-{w}.{ext}")
        if needs_build(src, dst):
            sips_resize(src, dst, w, fmt)
            made += 1
    largest = os.path.join(OUT, f"{slug}-{M.WIDTHS[-1]}.{ext}")
    meta = dims(largest)
    print(f"  {slug:22s} {ext}  +{made} variants  {meta[0]}x{meta[1]}")
    return slug, meta


def main():
    os.makedirs(OUT, exist_ok=True)
    all_jobs = list(jobs())
    print(f"Optimizing {len(all_jobs)} images x {len(M.WIDTHS)} widths -> {OUT}")
    meta = {}
    with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as ex:
        for result in ex.map(build_one, all_jobs):
            if result:
                meta[result[0]] = list(result[1])
    with open(M.META_PATH, "w") as f:
        json.dump(meta, f, indent=0, sort_keys=True)
    # report total output weight
    total = sum(
        os.path.getsize(os.path.join(OUT, f))
        for f in os.listdir(OUT) if os.path.isfile(os.path.join(OUT, f))
    )
    print(f"Done. {len(meta)} images, dist/images total {total/1e6:.1f} MB")


if __name__ == "__main__":
    main()
