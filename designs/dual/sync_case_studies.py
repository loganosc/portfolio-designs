#!/usr/bin/env python3
"""Regenerate the embedded case studies in index.html from the site's case-study pages.

The Dual design shows each case study in a modal, so the content lives in
<template id="cs-..."> blocks inside index.html. Those blocks are generated from
the real pages in the repo root; edit the pages, then run:

    python3 designs/dual/sync_case_studies.py          # rewrite index.html
    python3 designs/dual/sync_case_studies.py --check  # exit 1 if out of date

eBay and UNC Hockey have no standalone page (they link to Behance), so their
templates are hand-written and left alone.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
INDEX = HERE / "index.html"

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
# Relative asset/page references need to climb out of designs/dual/
RELATIVE_REF = re.compile(r'\b(src|href|data)="(?![a-z]+:|#|/|\.\./)([^"]+)"')


def render(page_path):
    page = (ROOT / page_path).read_text()
    main = re.search(r"<main[^>]*>\n(.*?)\s*</main>", page, re.S)
    if not main:
        raise SystemExit(f"{page_path}: no <main> element found")
    body = main.group(1).lstrip()
    body = EMPTY_ACTIONS.sub("", BACK_LINK.sub("", body))
    body = RELATIVE_REF.sub(lambda m: f'{m.group(1)}="../../{m.group(2)}"', body)
    return body.rstrip() + "\n"


def main():
    html = INDEX.read_text()
    updated = html
    for key, page in SOURCES.items():
        block = re.compile(rf'(<template id="cs-{key}">\n)(.*?)(</template>)', re.S)
        if not block.search(updated):
            raise SystemExit(f'index.html: <template id="cs-{key}"> not found')
        content = render(page)
        updated = block.sub(lambda m: m.group(1) + content + m.group(3), updated, count=1)

    if "--check" in sys.argv:
        if updated != html:
            print("Embedded case studies are out of date; run sync_case_studies.py")
            sys.exit(1)
        print("Embedded case studies are up to date")
        return

    if updated == html:
        print("No changes")
    else:
        INDEX.write_text(updated)
        print(f"Updated {len(SOURCES)} case studies in {INDEX.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
