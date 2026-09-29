#!/usr/bin/env python3
"""Regenerate the embedded case studies in each design from the site's case-study pages.

Dual and Logan.os show each case study in a modal, so the content lives in
<template id="cs-..."> blocks inside each design's index.html. Those blocks are
generated from the real pages in the repo root; edit the pages, then run:

    python3 scripts/sync_case_studies.py          # rewrite every design's index.html
    python3 scripts/sync_case_studies.py --check  # exit 1 if any is out of date

eBay and UNC Hockey have no standalone page (they link to Behance), so their
templates are hand-written and left alone.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Designs that embed case studies. Each lives two levels below the repo root,
# which the relative-path rewrite below relies on. A design can swap each case
# study's hero image for its own cover ("{key}" is the template key) and skip
# case studies it doesn't show.
TARGETS = {
    ROOT / "designs" / "dual" / "index.html": {},
    ROOT / "designs" / "logan-os" / "index.html": {
        "cover": 'src="assets/covers/{key}.webp" width="800" height="376"',
        "skip": {"fees"},
    },
}

# template key -> source page (relative to the repo root)
SOURCES = {
    "swiped": "swiped-case-study.html",
    "dinklink": "dinklink-case-study.html",
    "vanguard": "vanguard-case-study.html",
    "fees": "digital-processing-fees-case-study.html",
}

# "Back to portfolio" links make no sense inside the modal; drop them, then any
# action row they leave empty.
BACK_LINK = re.compile(r'\s*<a [^>]*href="index\.html[^"]*"[^>]*>Back to portfolio</a>')
EMPTY_ACTIONS = re.compile(r'<div class="case-actions">\s*</div>')
# Relative asset/page references need to climb out of designs/<name>/
RELATIVE_REF = re.compile(r'\b(src|href|data)="(?![a-z]+:|#|/|\.\./)([^"]+)"')
HERO_IMG = re.compile(r'(<section class="case-study-hero.*?<figure>\s*<img )src="[^"]*"', re.S)


def render(page_path):
    page = (ROOT / page_path).read_text()
    main = re.search(r"<main[^>]*>\n(.*?)\s*</main>", page, re.S)
    if not main:
        raise SystemExit(f"{page_path}: no <main> element found")
    body = main.group(1).lstrip()
    body = EMPTY_ACTIONS.sub("", BACK_LINK.sub("", body))
    body = RELATIVE_REF.sub(lambda m: f'{m.group(1)}="../../{m.group(2)}"', body)
    return body.rstrip() + "\n"


def sync(index, rendered, options):
    html = index.read_text()
    updated = html
    cover = options.get("cover")
    for key, content in rendered.items():
        if key in options.get("skip", ()):
            continue
        if cover:
            content, found = HERO_IMG.subn(lambda m: m.group(1) + cover.format(key=key), content, count=1)
            if not found:
                raise SystemExit(f"{SOURCES[key]}: no hero image found")
        block = re.compile(rf'(<template id="cs-{key}">\n)(.*?)(</template>)', re.S)
        if not block.search(updated):
            raise SystemExit(f'{index.relative_to(ROOT)}: <template id="cs-{key}"> not found')
        updated = block.sub(lambda m: m.group(1) + content + m.group(3), updated, count=1)
    return html, updated


def main():
    rendered = {key: render(page) for key, page in SOURCES.items()}
    stale = []
    for index, options in TARGETS.items():
        name = index.relative_to(ROOT)
        html, updated = sync(index, rendered, options)
        if updated == html:
            print(f"{name}: up to date")
        elif "--check" in sys.argv:
            stale.append(name)
            print(f"{name}: embedded case studies are out of date")
        else:
            index.write_text(updated)
            print(f"{name}: updated its embedded case studies")

    if stale:
        print("Run: python3 scripts/sync_case_studies.py")
        sys.exit(1)


if __name__ == "__main__":
    main()
