# Signet Stack Ltd — corporate website

Source for the **[signetstack.io](https://signetstack.io)** website: the public site for
**Signet Stack Ltd**, a house of frontier-technology brands built around the
**SignetStack Labs™** master brand.

The site is a **data-driven static build**. A single Python script
(`assets/build_site.py`) holds all copy and structured content and renders the
entire `website/` folder — 25 pages of plain HTML/CSS, no runtime, no database,
no client framework. It can be hosted on any static host; in production it is
published to **GitHub Pages** by the CI workflow in `.github/workflows/deploy.yml`.

> © Signet Stack Ltd. All rights reserved. This repository is published for
> transparency and hosting only — it is **not** open source. See
> [`LICENSE`](LICENSE) and [`TRADEMARKS.md`](TRADEMARKS.md).

---

## What this repository contains

```
.
├── README.md                     ← you are here
├── LICENSE                       Proprietary licence (all rights reserved)
├── TRADEMARKS.md                 Trademark & brand-name notice
├── SECURITY.md                   How to report a security issue
├── CONTRIBUTING.md               How site content is edited & shipped
├── .github/
│   ├── workflows/deploy.yml      CI: build + publish to GitHub Pages
│   └── CODEOWNERS                Review ownership
├── assets/                       Build sources (not served)
│   ├── build_site.py             ★ all site content + the page generator
│   ├── build_brand_family.py     Generates the per-brand SVG marks
│   └── make_logo_signetlabs.py   Font/geometry helpers for the marks
└── website/                      ★ the generated, published site
    ├── *.html                    25 pages (see below)
    ├── CNAME                     Custom domain (signetstack.io)
    ├── .nojekyll                 Serve as-is (skip Jekyll)
    ├── README.md / DEPLOY.md     Site-level docs
    └── assets/
        ├── styles.css            Single stylesheet (CSS variables, per-brand --accent)
        ├── marks/*.svg           Scalable brand marks
        └── img/                  favicon + brand-architecture poster
```

**Only `website/` is served.** Everything in `assets/` is build-time source.
Confidential material (board decks, executive summaries, brand kits, and the
internal source documents) is **deliberately excluded** from this repository by
`.gitignore` and is never committed.

### The pages
| Area | Pages |
|------|-------|
| Company | `index` · `company` · `careers` · `contact` · `privacy` · `terms` |
| Platform | `platform` (the **Signet Data Trust Network Platform** hub) |
| Platform modules | `signet-core` · `signet-vault` · `signet-ai-governance` · `signet-lake` · `signet-stream` · `signet-clean-room` · `signet-embedded` · `signet-data-trust-network` · `signet-pades` |
| Product brands | `brands` (hub) · `velocity` · `dxp` |
| Flagship product | `v5-omni` (HFT V5 Omni, under SignetStack Velocity) |
| Sister company | `signetify` (links to [signetify.com](https://signetify.com)) |
| Newsroom | `insights` + `insight-pqc-readiness` · `insight-auditable-ai` · `insight-house-of-brands` |

---

## Build & preview locally

Requires **Python 3.10+** and **Pillow** (used to render the SVG marks).

```bash
pip install pillow
python3 assets/build_site.py          # regenerates website/  → "Site built: 25 pages"
python3 -m http.server 8099 --directory website
# open http://localhost:8099
```

The build is deterministic: edit content in `assets/build_site.py`, re-run, and
the whole site is regenerated. Never hand-edit files in `website/*.html` — they
are overwritten on the next build.

---

## Editing content

All copy lives in clearly-named Python data structures at the top of
`assets/build_site.py`:

| Structure | Controls |
|-----------|----------|
| `COMPANY` | Legal name, emails, Companies House no., registered office, tagline |
| `PLATFORM` | The Signet Data Trust Network Platform hub copy + layers + certs |
| `MODULES` / `MODULE_ORDER` | The nine platform module pages |
| `DIV` / `ORDER` | Product-brand division pages (Velocity, DXP) |
| `SISTER` | Signetify sister-company panel |
| `INSIGHTS` | Newsroom posts |
| `ROLES` | Open roles on the careers page |
| `SOCIAL` | Footer social links |

Edit, commit, and CI rebuilds and republishes automatically. See
[`CONTRIBUTING.md`](CONTRIBUTING.md) for the full workflow and
[`website/DEPLOY.md`](website/DEPLOY.md) for hosting/DNS.

### Adding a brand or module (the scalable part)
1. Add an SVG mark to `website/assets/marks/<slug>.svg` (or generate a kit via
   `build_brand_family.py`).
2. Add a `DIV["<slug>"]` (product brand) or `MODULES["<slug>"]` (platform module)
   entry, and append `<slug>` to `ORDER` / `MODULE_ORDER`.
3. Re-run the build. The nav dropdown, hub grids, footer and the new themed page
   are all generated automatically.

---

## Deployment

Published to **GitHub Pages** via `.github/workflows/deploy.yml` on every push to
`main` that touches the site. The workflow installs Pillow, runs the build,
writes `CNAME`/`.nojekyll`, and deploys `website/` as the Pages artifact.

Full step-by-step (Pages enablement, custom domain, DNS records, HTTPS, mail) is
in **[`website/DEPLOY.md`](website/DEPLOY.md)**.

> **Note:** GitHub Pages from a *private* repo requires a paid plan (GitHub Team
> or Enterprise Cloud). On the Free plan, publish from a **public** repo — which
> is safe here, since the repo contains only the public website and its build
> sources.

---

## Design system

- Dark **Carbon** theme (`#0B0F14`); **IBM Plex Sans / IBM Plex Mono** (Google Fonts).
- Master chrome is neutral (white/platinum). Each brand/module page sets its own
  `--accent` — Velocity cyan, DXP coral, the platform deep-teal, Signetify
  emerald, etc. — driven by CSS variables in a single `styles.css`.
- The nested-hexagon **signet seal** is the master mark; per-domain marks carry a
  distinct glyph and accent.

Brand specifics (palette hexes, type, logo construction) are documented in the
brand memory and the per-brand kits held privately by Signet Stack Ltd.

---

## Legal

**Signet Stack Ltd** — Registered in England & Wales, Companies House No.
**13011013**. Registered office: 86–90 Paul Street, London EC2A 4NE.
General: info@signetstack.io · Partnerships/careers: johnson@signetstack.io.

This repository is proprietary. See [`LICENSE`](LICENSE) and
[`TRADEMARKS.md`](TRADEMARKS.md). Content describing products reflects honestly-
stated maturity (pre-GA / roadmap items are labelled as such); no certification
is claimed that is not held.
