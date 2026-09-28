---
name: Retro OS Portfolio
colors:
  surface: '#fbf8ff'
  surface-dim: '#dad9e6'
  surface-bright: '#fbf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f2ff'
  surface-container: '#eeecfa'
  surface-container-high: '#e8e7f4'
  surface-container-highest: '#e3e1ee'
  on-surface: '#1a1b24'
  on-surface-variant: '#4e4637'
  inverse-surface: '#2f303a'
  inverse-on-surface: '#f1effd'
  outline: '#807665'
  outline-variant: '#d2c5b1'
  surface-tint: '#7b5900'
  primary: '#7b5900'
  on-primary: '#ffffff'
  primary-container: '#f4c464'
  on-primary-container: '#6f5000'
  inverse-primary: '#efbf60'
  secondary: '#4156ba'
  on-secondary: '#ffffff'
  secondary-container: '#8397ff'
  on-secondary-container: '#0c288f'
  tertiary: '#8b496a'
  on-tertiary: '#ffffff'
  tertiary-container: '#ffb6d6'
  on-tertiary-container: '#804060'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdea4'
  primary-fixed-dim: '#efbf60'
  on-primary-fixed: '#261900'
  on-primary-fixed-variant: '#5d4200'
  secondary-fixed: '#dee1ff'
  secondary-fixed-dim: '#b9c3ff'
  on-secondary-fixed: '#001159'
  on-secondary-fixed-variant: '#263ca1'
  tertiary-fixed: '#ffd8e7'
  tertiary-fixed-dim: '#ffafd3'
  on-tertiary-fixed: '#3a0525'
  on-tertiary-fixed-variant: '#6f3251'
  background: '#fbf8ff'
  on-background: '#1a1b24'
  surface-variant: '#e3e1ee'
typography:
  headline-xl:
    fontFamily: Bricolage Grotesque
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
  headline-xl-mobile:
    fontFamily: Bricolage Grotesque
    fontSize: 32px
    fontWeight: '800'
    lineHeight: 40px
  headline-lg:
    fontFamily: Bricolage Grotesque
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Bricolage Grotesque
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  headline-md:
    fontFamily: Bricolage Grotesque
    fontSize: 22px
    fontWeight: '700'
    lineHeight: 28px
  body-lg:
    fontFamily: JetBrains Mono
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
  body-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
  body-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '600'
    lineHeight: 16px
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
spacing:
  gutter: 1rem
  gutter-desktop: 1.5rem
  margin: 1rem
  margin-desktop: 2.5rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system channels the tactile, playful nostalgia of early graphical user interfaces, blending late-90s desktop operating system paradigms with contemporary vaporwave and retro-futuristic charm. Tailored for creative technologists, front-end architects, and digital product designers, it transforms personal portfolios from standard static feeds into an interactive, layered desktop ecosystem.

The aesthetic fuses raw retro-brutalism with sweet, dreamy pastel palettes. Chunky window chrome, faux-beveled borders, segmented pixel progress indicators, and draggable desktop sticky notes introduce physical tactility to web surfaces. The emotional tone evokes playful curiosity, computational nostalgia, and self-aware irony—offering instant visual distinction without sacrificing functional utility.

## Colors

The palette balances warm amber-yellow sticky note tones against nostalgic digital pastels: periwinkle window bars, bubblegum pink modal banners, and a serene grid-lined pastel blue canvas (`#BDD7EE`). High-contrast ink outlines (`#12131C`) bind the pastels together into an authentic desktop GUI experience.

### Roles & Surface Rules
- **Primary (`#F4C464`):** The signature desktop sticky note and active window accent. Used for high-priority notification callouts, folder highlight fills, primary button states, and active tabs.
- **Secondary (`#7B8FF7`):** Classic periwinkle blue window header fill, terminal links, and interactive scrollbar thumbs.
- **Tertiary (`#F4A3C8`):** Retro candy pink for alert dialogues, selection boxes, system status badges, and decorative hardware frames.
- **Neutral (`#12131C`):** Strict, zero-blur border ink, high-contrast text, hard window drop shadows, and window control buttons.
- **Canvas & Window Wells (`#FFFFFF` & `#F5F6FA`):** Inset viewport containers, text fields, document sheets, and desktop background grid lines (`#A4C6E8` on `#CCE3F8`).

## Typography

Typography establishes an intentional contrast between expressive retro-modern character and strict computing precision.

- **Headline Font (`Bricolage Grotesque`):** Used across major window titles, hero portfolio intro statements, and prominent modal queries (`How are you? :)`). Its distinctive, idiosyncratic letterforms evoke experimental digital publishing while retaining commanding punch.
- **Body & Label Font (`JetBrains Mono`):** Used for directory trees, system file paths (`C:\User\Documents\...`), dialogue prompts, button labels, and system status readouts. Its monospace rhythm grounds the entire UI in nostalgic terminal and classic IDE conventions.

## Layout & Spacing

The layout model mimics a virtual desktop workspace overlaid on an explicit 24px pastel grid canvas. Layout density stays compact and tactile, keeping navigation dense and exploratory.

### Spatial Framework
- **Desktop Canvas Mode (Large Screens):** Freeform window architecture with a base 12-column layout grid underneath for standard responsive fallback. Windows can stack, overlap, or tile with consistent `gutter-desktop` (24px) gutters. Outer viewport margins lock at `margin-desktop` (40px) to simulate an authentic operating system workspace.
- **Mobile Mode (Under 768px):** Windows convert from free-floating draggable panels into a structured, full-width stacked window layout. Outer margin reduces to `margin` (16px), keeping the window title bar, minimize/maximize buttons, and borders visible as framing cards.
- **Micro Rhythms:** Interior container padding follows tight 4px, 8px, and 16px steps (`space-xs`, `space-sm`, `space-md`), reflecting space-efficient classic dialog boxes.

## Elevation & Depth

This system rejects soft ambient blur shadows in favor of crisp, hard-edged brutalist bevels and solid pixel drop shadows. Depth conveys physical elevation tiers directly drawn from 90s system managers:

- **Level 0 (Desktop Canvas):** Pastel blue grid pattern rendered via repeating CSS linear gradients (`#A4C6E8` 1px grid over `#CCE3F8`). Flat and non-elevated.
- **Level 1 (Docked/Inset Panels):** Inset bevel simulation. Border: 2px solid `#12131C`, interior wells have top/left inner shadow `inset 2px 2px 0px #8D99AE` and bottom/right inner shadow `inset -2px -2px 0px #FFFFFF`.
- **Level 2 (Active Cards & Floating Sticky Notes):** Solid, unblurred drop shadow: `4px 4px 0px #12131C` with 2px solid border in `#12131C`.
- **Level 3 (Focused Windows & Interactive Modals):** Accentuated drop shadow: `6px 6px 0px #12131C` or `8px 8px 0px #12131C`. Brings top-level modal dialogs and active window chrome directly to the foreground.
- **Active Button Depress:** Shifts the element `translate(2px, 2px)` while reducing shadow from `3px 3px 0px #12131C` to `1px 1px 0px #12131C`, creating a tangible, mechanical click.

## Shapes

All structural elements adhere strictly to 0px corner radii (`roundedness: 0`). 

Windows, buttons, input fields, scrollbars, tabs, and status badges maintain sharp 90-degree geometric corners. Pixelated silhouettes extend to icons, control widgets, and modal dismiss buttons, reinforcing the authentic hardware and OS rendering constraints of early GUI environments.

## Components

### Retro Window Frames
- **Title Bar:** 32px height filled with primary (`#F4C464`), secondary (`#7B8FF7`), or tertiary (`#F4A3C8`) pastels. Contains left-aligned bold title text (`JetBrains Mono`, 12px) and right-aligned classic square control buttons (`_`, `□`, `×`).
- **Control Buttons:** 18x18px squares with 1.5px solid `#12131C` borders, white or tinted background, and centered micro-icons. Hover state flips to inverted colors.
- **Window Body:** `#FFFFFF` background encased in a 2px solid `#12131C` frame with bottom-right hard drop shadow (`6px 6px 0px #12131C`).

### Buttons
- **Default Action:** White or `#F5F6FA` background, 2px solid `#12131C` border, hard shadow `3px 3px 0px #12131C`. Padding: 6px 16px. Font: `JetBrains Mono` semi-bold.
- **Primary Action:** `#F4C464` fill with identical border and shadow.
- **Active/Pressed State:** `transform: translate(2px, 2px); box-shadow: 1px 1px 0px #12131C;`.

### Input Fields & Search Bars
- **Style:** Faux-inset sunken text boxes (`background: #FFFFFF; border: 2px solid #12131C; box-shadow: inset 2px 2px 0px #C3C7DB;`).
- **Typography:** `JetBrains Mono` 13px with high-contrast text and blinking block cursor.
- **Trailing Close/Clear Button:** Mini square containing `×` icon embedded at the right margin.

### Checkboxes & Radio Buttons
- **Checkbox:** Sharp 16x16px square, 2px solid `#12131C` border, inset inner tone. Checked state displays a crisp pixel-art checkmark (`✓`) in `#12131C`.
- **Radio:** 16x16px square rotated 45 degrees or marked with centered square pixel dot when active.

### Segmented Progress Bars
- **Outer Track:** Inset sunken trough with 2px solid border, 22px height, white background.
- **Fill Segments:** Discrete blue/periwinkle (`#7B8FF7`) rectangular blocks spaced 2px apart, advancing rhythmically to convey retro file-transfer loading states.

### Sticky Notes & Desktop Chips
- **Sticky Note:** Yellow (`#F4C464`) container with a lighter yellow header strip (`#FDE39B`), 2px solid border, and `4px 4px 0px #12131C` shadow. Ideal for portfolio testimonials, quick bio snippets, or interactive memos.
- **Desktop File/Folder Chips:** Vertical stack containing pixelated dual-tone folder/document icon and a compact text badge with a faint dotted focus outline when selected.
### About Modal
- Not on the page itself. It opens from the hero's `ABOUT.TXT` button, and closes with the × button, a click on the backdrop, or Esc.
- **Frame:** Retro window modal (max width 3xl) with a periwinkle-to-lavender title bar that stays pinned while scrolling and reads like a file path (`C:\USERS\LOGAN\README_ABOUT.TXT`).
- **Body:** Portrait photo in a 2px ink frame with a `3px 3px 0px` hard shadow, next to long-form bio copy in `VT323` and a row of interest chips.

### Contact Sticky Note
- A sticky note (`CONTACT.LNK`) in the bottom utility row, after FILE_TRANSFER and MINI_SYNTH (5 / 4 / 3 columns at `lg`).
- Holds a short prompt and a 2×2 grid of white link buttons (Email, LinkedIn, Behance, Instagram). The note is kept compact because its height sets the height of the row; the neighboring windows center their content vertically so they don't show empty space.

### Case Study Viewer (modal)
- Opens from any project card (`LAUNCH SPECS` or clicking the thumbnail) and shows the **entire** case study inside the page. It's a large retro window (max width 6xl, 94vh) whose scrolling body uses the same pastel grid canvas as the desktop, so a case study looks like a miniature version of the main screen.
- **Chrome:** title bar `C:\PORTFOLIO\<FILE> // CASE_STUDY` with an `OPEN AS PAGE ↗` link to the standalone case study page (when there is one) and a close button; a status bar at the bottom shows the window count, category and `ESC TO CLOSE`.
- **Hero window (`00 // README.TXT`):** matches the main hero, with an eyebrow chip, a pink `VT323` headline, the lede, a yellow inset meta box (team, course, tools, role), action buttons (live app, PDF, Behance) and the cover image in a captioned frame.
- **Section windows (`01 // <Section>` …):** one retro window per case study section. Title-bar gradients cycle through pink/purple, sky/indigo, amber/pink, mint/sky and purple/rose. Section content is made from these blocks:
  - **Cards:** `retro-card`s in a 1–3 column grid, each with a pastel header strip (cycling colors) and `VT323` body text or `▸` bullet lists.
  - **Figures:** images in a 2px ink frame with a hard shadow and a monospace caption strip.
  - **Split:** a card next to a figure.
  - **Quotes:** a sticky note with user quotes.
  - **Embeds:** iframes (live app, Figma, PDF) in an ink frame with a dark label bar and an `OPEN ↗` link.
  - **Text, lists, captions and numbered sources.**
- Closing the viewer clears its content so embedded video and live apps stop. The page behind it doesn't scroll while the viewer is open.

## Content

All copy and imagery come from `portfolio-main/` (the original site). The desktop page links into its case-study pages and loads its assets through relative `portfolio-main/...` paths, so the two folders must stay side by side.

### Identity
- **Name:** Logan Oscher, a third-year student at UNC Chapel Hill double-majoring in Computer Science and Media & Journalism (AD/PR).
- **Focus:** web design, graphic design, and software engineering, plus UI/UX and interactive media.
- **Contact:** loganosc@unc.edu · linkedin.com/in/logan-oscher · behance.net/loganoscher · instagram.com/loganocreates
- **Photo:** `portfolio-main/assets/about-photo.png` (identity card and About modal). Favicons: `portfolio-main/assets/favicon_io/`.

### Projects (gallery order)
| # | File chip | Project | Filter | Course | Primary link |
|---|-----------|---------|--------|--------|--------------|
| 01 | `Vanguard_YIR.fig` | Vanguard Year-in-Review Redesign (investors 50+) | UI/UX | MEJO 581 | `vanguard-case-study.html` (+ pitch PDF) |
| 02 | `Swiped.app` | Swiped: Meal Swaps Made Easy | Full-Stack | COMP 426 | `swiped-case-study.html` (+ live app) |
| 03 | `DinkLink.fig` | DinkLink: Pickleball Matchmaking | UI/UX | MEJO 433 | `dinklink-case-study.html` (+ Behance) |
| 04 | `eBay_Redesign.fig` | eBay Interface Redesign | UI/UX | — | Behance gallery |
| 05 | `UNC_Hockey.gfx` | UNC Hockey Graphic Collection | Media & GFX | — | Behance gallery |

### Content Rules
- Card descriptions, modal key points, and tool chips should only restate what the source case studies say. Don't add tools or claims that aren't there.
- Each card keeps its own pastel for the thumbnail badge, tag chips, and `LAUNCH SPECS` button (sky, pink, amber, mint, lavender, rose), so projects are easy to tell apart at a glance.
- When adding a project, add a card in `#projects-grid` and an entry in `caseStudies` (in the page script) under the same key. Each entry holds the hero fields (`eyebrow`, `title`, `lede`, `cover`, `meta`, `actions`, optional `page`) and a list of `sections` made from the block types above.
- eBay and UNC Hockey don't have standalone pages in portfolio-main. Their viewers show the overview text from the original site's project popups plus the cover image, and link to Behance for the full work.
