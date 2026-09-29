# Logan.os

A full-bleed retro desktop: menu bar, a scrolling grid-paper desktop with overlapping-style windows, desktop file icons, and a taskbar. On first visit the live site shows inside a beige CRT from the first frame, a pixel cursor clicks the screen, and the camera dives in.

Plain HTML/CSS/JS, no build step: `index.html`, `styles.css`, `main.js`.

## Design system

- **Fonts:** `VT323` for headlines and body copy; `Silkscreen` for UI chrome (menus, title bars, buttons, labels, icon names). JetBrains Mono is loaded as a backup in both font stacks. Pixel text is never under 12px.
- **Colors:** tokens live on `:root` in `styles.css`. Ink `#12131C`, yellow `#FFDEA4`, light yellow `#FDE39B`, periwinkle `#7B8FF7`, light periwinkle `#C9D1FF` / `#dee1ff`, pink `#F4A3C8`, light pink `#FCE0ED` (About me button, inactive info tab), plum `#8b496a`, link blue `#263ca1`, desktop `#CCE3F8` with a `#A4C6E8` 24px grid, well `#F5F6FA`, surface `#fbf8ff`, room `#2f303a`.
- **Shape:** 0 radius everywhere except the intro's monitor hardware.
- **Depth:** 2px ink borders, hard unblurred shadows: windows 8px, cards 4px, buttons 3px. Buttons lift on hover (-1px, 4px shadow) and press to `translate(2px, 2px)` with a 1px shadow.
- **Title bars:** 32px, pastel fill with 1px ink pinstripes every 4px, title centered on a solid pastel chip, square controls at both ends.

## Intro

2.6s, once per session (`sessionStorage['logan-os:intro']`), replayed by the taskbar's Restart button. Skipped entirely under `prefers-reduced-motion` and on phones (iPhone/iPod, or a coarse pointer under 768px wide), where scaling the whole site animates poorly.

| Time | What happens |
| --- | --- |
| 0–0.5s | site sits inside the monitor |
| 0.5–1.2s | pixel cursor glides to the center |
| ~1.25s | click, with a square ripple |
| 1.45–2.35s | zoom: overlay scales 1 → 1/0.7222 while the site scales 0.7222 → 1, same origin and easing `cubic-bezier(.7,0,.25,1)` |
| 2.35–2.6s | overlay fades out and is removed |

Geometry is pure CSS: `.stage` is a size container, so the screen opening is `72.22cqw × 72.22cqh` (the viewport's aspect ratio) and `--u` is one design-canvas pixel at that scale. Bezel, chin, stand and radii scale with `--u`, with minimums so the hardware still reads on phones. The `is-intro` class is set on `<html>` by an inline script in `<head>` before first paint, so the site never flashes unscaled.

## Modern mode

A small mode-switch tip sits under Logan Info (both live in `.hero__side`): in retro it's the **Modernize.exe** window with a **Modernize** button, in modern a plain card saying "Miss the pixels?" with a **Go retro** button (same element; its text swaps via `.only-retro` / `.only-modern`). × hides it for good in the current mode only (`localStorage['logan-os:promo-retro']` / `['logan-os:promo-modern']`, applied in `<head>` as `.promo-dismissed-retro` / `.promo-dismissed-modern`). The taskbar's **Modernize** button switches to a black-and-white, editorial serif (Newsreader) version with the same layout and content; it then reads **Retro mode**. The choice is saved in `localStorage['logan-os:theme']` and applied by the inline `<head>` script before first paint, so neither look flashes. Modern mode skips the intro and hides the Restart button, the desktop icons, the `C:\LOGAN>` prompt and the title-bar controls. Cards and case-study heroes swap the pixel covers for product mockups from `assets/covers/modern/` (cropped to 16:10 on the cards, uncropped in the hero). Both images are in the markup with `.only-retro` / `.only-modern`, and hidden lazy images aren't fetched, so each mode downloads only its own. The sync script writes both images into the generated case-study heroes.

Every rule lives in `modern.css`, scoped to `html.is-modern`, so `styles.css` stays the retro source of truth. Borders and hard shadows in `styles.css` go through `--line`, `--shade`, `--bw` and `--bw-thin` (retro: ink, ink, 2px, 1.5px); modern mode sets them to a `#e4e4e7` hairline and no shadow, swaps the accent tokens to one neutral grey, and points `--pixel` and `--vt` at Newsreader. When you add a component, use those tokens for its borders and shadows, and give it font sizes in `modern.css` if it sets its own (the retro fonts run small, so their sizes don't carry over).

## Responsive

- **< 1200px:** tighter padding, H1 64px.
- **< 1024px:** Logan Info stacks under bio.txt; project grid goes to 2 columns.
- **< 768px:** one column with 16px margins, desktop icons become a horizontal scrolling row under the menu bar, the menu collapses into a dropdown, H1 52px, grid 1 column, taskbar keeps only Restart and the clock.

## Case study viewer

Each project's **Open** button shows its case study in a modal window (a `<dialog>`) instead of leaving the page. A modified click (Cmd/Ctrl/Shift) still opens the page itself.

- **Chrome:** a 40px title bar in the card's color reading `C:\Logan\Interactive_Works\<file>`, with a × button; a status bar with the project kind and category, an **Open as page ↗** link (or **View on Behance ↗** for eBay and UNC Hockey) and a **Close** button.
- **Body:** scrolls over the same grid-paper desktop. Every section of the case study becomes its own window, and its heading becomes a pinstriped title bar; title-bar colors cycle periwinkle, pink and yellow. Headings and body copy use VT323, and labels, badges and buttons use Silkscreen.
- **Image galleries:** every image in a `.case-grid` gets a yellow **+** badge and opens a large view (a second `<dialog>` over the viewer). Each gallery is one set, so Swiped's Product Screens open as 5 images you can swipe or scroll through, step through with **◀ Prev / Next ▶** or the ← → keys; a counter and the figure's caption sit in the bottom bar. Esc closes only the large view and focus returns to the image.
- **Closing:** Esc, ×, Close, or a click on the backdrop. Focus returns to the Open button, and the content is cleared so embedded video and Figma prototypes stop.

The content lives in `<template id="cs-…">` blocks at the bottom of `index.html`. Swiped, DinkLink and Vanguard are generated from the root `*-case-study.html` pages; after editing one of those pages, run `python3 scripts/sync_case_studies.py` from the repo root (it updates Dual too). eBay, UNC Hockey and InsightUI have no standalone page, so their templates are hand-written.

## Content

Project covers in `assets/covers/` are 800×376 lossless WebPs, used uncropped on the cards and as each case study's hero; `assets/headshot.webp` is a 256px crop of the portrait.

### Still to fill in
- **Resume URL:** the menu bar, the Contact tab and the `Resume.floppy` icon all link to `#`.
- **Copy to confirm:** project descriptions were completed from cut-off text in the design. Tags only list tools named in the case studies, so UNC Hockey uses `#Instagram #Social` because no tool is named.
