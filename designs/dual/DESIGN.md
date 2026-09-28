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