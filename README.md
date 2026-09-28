# Portfolio design explorations

Alternate designs for the portfolio, kept separate from the live site repo (loganosc/portfolio → loganoscher.com).

| Folder | Design |
|---|---|
| `/` (repo root) | Snapshot of the current live site |
| [`designs/dual/`](designs/dual/) | "Dual": Retro OS file-browser layout |
| [`designs/pastel-os/`](designs/pastel-os/) | "Pastel OS": Retro OS workspace layout |

Both designs pull images and case-study pages from the root `assets/` folder, so open them from inside this repo (e.g. `open designs/pastel-os/index.html`).

## Dual

A System 7-style Finder window. A bio inspector panel sits above a project browser with a sidebar of volumes (Product & UX, Media & Graphics, About, Resume), large-grid/compact-list view modes, and tag filtering.

![Dual design](designs/dual/screenshot.png)

**Editing Dual:** styles are prebuilt with Tailwind, and the case-study modals are generated from the root `*-case-study.html` pages.

```bash
cd designs/dual
npm install          # first time only
npm run build        # after changing Tailwind classes in index.html
npm run sync         # after editing a root case-study page
```

## Pastel OS

A pastel workspace window with a large intro headline, a "verify humanity" widget, and a searchable project directory with tag filters and color-coded "Launch Specs" cards.

![Pastel OS design](designs/pastel-os/screenshot.png)
