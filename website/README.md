# SignetStack Labs — corporate website

A data-driven static site for **Signet Stack Ltd**, built around the **SignetStack Labs** master brand, housing the divisions (SignetStack Velocity, PQC, AI Governance, DXP) with **Signetify** as a sister company. Pure HTML/CSS/JS — host anywhere (Netlify, GitHub Pages, S3/CloudFront, any static host).

## Run locally
```bash
python3 -m http.server 8099 --directory website
# open http://localhost:8099
```

## Structure
```
website/
  index.html            Home
  company.html          About Signet Stack Ltd (house-of-brands model)
  brands.html           Brands hub
  velocity.html pqc.html ai-governance.html dxp.html   Division pages (accent-themed)
  v5-omni.html          Flagship product (HFT V5 Omni, under Velocity)
  signetify.html        Sister company (placeholder identity)
  insights.html + insight-*.html    Newsroom + posts
  careers.html  contact.html  privacy.html  terms.html
  assets/
    styles.css          Single stylesheet (CSS variables; --accent themed per division)
    marks/*.svg         Brand marks (master + per-division + signetify), scalable
    img/                favicon, brand-architecture poster
```

## Design system
- Dark **Carbon** theme (`#0B0F14`), **IBM Plex Sans/Mono** (Google Fonts).
- Master/chrome is neutral (white/platinum); each division page sets its own `--accent` (Velocity cyan, PQC violet, AI Governance gold, DXP coral). Signetify = emerald.
- The nested-hex seal is the site logo; division marks appear on cards/pages.

## Adding a new brand later (the scalable part)
1. Add a brand entry to `BRANDS` in `assets/build_brand_family.py` (name, key, accent/bright/deep, glyph, folder) and generate its kit, **or** just add its SVG mark to `website/assets/marks/<slug>.svg`.
2. Add a `DIV["<slug>"]` entry in `assets/build_site.py` (name, kicker, accent, tagline, overview, capabilities, optional stats) and add `<slug>` to `ORDER`.
3. Rebuild: `python3 assets/build_site.py`. The brands grid, nav dropdown, footer and a new themed division page are generated automatically.

## Notes / before launch
- **Signetify** identity & copy are placeholders pending its own brand.
- Contact form is a front-end demo (no backend) — wire to your form handler/email.
- `privacy.html` / `terms.html` are templates — have counsel review.
- Emails are `info@signetstack.io` (general) and `johnson@signetstack.io` (founder/partnerships/careers). Add the registered office address (UK trading-disclosure requirement) and confirm the SignetStack Labs / signetstack.io trademark & domain.
- Fonts load from Google Fonts CDN (needs internet); to self-host, drop IBM Plex files in `assets/fonts/` and swap the `<link>` for `@font-face`.
