# Contributing

> This repository is **proprietary** to Signet Stack Ltd (see [`LICENSE`](LICENSE)).
> It is not open to external contributions. This guide is for **Signet Stack Ltd
> team members** maintaining the site. External pull requests will be closed.

## How the site works (in one paragraph)

The site is a **data-driven static build**. All copy and structure live in
`assets/build_site.py`. Running it regenerates the entire `website/` folder.
A GitHub Action (`.github/workflows/deploy.yml`) re-runs that build on every push
to `main` and publishes `website/` to GitHub Pages. So editing the site is:
**change content → commit → CI rebuilds & republishes.**

## Prerequisites

- Python **3.10+**
- `pip install pillow`

## Local workflow

```bash
# 1. edit content
$EDITOR assets/build_site.py

# 2. rebuild
python3 assets/build_site.py            # expect: "Site built: 25 pages"

# 3. preview
python3 -m http.server 8099 --directory website
#    open http://localhost:8099

# 4. commit the SOURCE change (and the regenerated website/ if you build locally)
git add assets/build_site.py website/
git commit -m "content: <what changed>"
git push        # CI rebuilds and republishes
```

> You can also edit `assets/build_site.py` directly in the **GitHub web editor**
> and commit — CI will rebuild from source, so you don't have to run the build
> yourself. Org SSO is the auth; PR review is the safety net.

**Never hand-edit `website/*.html`** — those files are generated and will be
overwritten on the next build. Edit `assets/build_site.py` instead.

## Where things live

| To change… | Edit… |
|------------|-------|
| Company name, emails, reg no., office, tagline | `COMPANY` |
| Platform hub copy / layers / certs | `PLATFORM` |
| A platform module page | `MODULES` (+ `MODULE_ORDER`) |
| A product-brand page (Velocity, DXP) | `DIV` (+ `ORDER`) |
| Signetify panel | `SISTER` |
| Newsroom posts | `INSIGHTS` |
| Open roles | `ROLES` |
| Footer social links | `SOCIAL` |
| A brand mark | `website/assets/marks/<slug>.svg` |
| Styling | `website/assets/styles.css` (CSS variables; per-brand `--accent`) |

## Content rules (important — keep us honest & safe)

These are hard constraints. Do not violate them in any committed copy:

- **No certification we don't hold.** SOC 2, ISO 27001, FIPS 140-3 CMVP, NCSC
  CPA, Common Criteria are described only as *in preparation / in planning / on
  the roadmap* — never as "certified" or "compliant."
- **No proprietary internals.** No cryptographic primitive internals beyond NIST
  standard names; no internal mode/tier names; no internal test counts beyond
  what is already approved; no financials, patents, audit findings, competitor
  names, or infrastructure/credentials.
- **No confidential files.** Board decks, executive summaries, brand kits and
  internal source docs must stay out of this repository (they are covered by
  `.gitignore` — keep it that way).
- The **company registration** (No. 13011013) and **registered office** are
  public/approved and may appear.

## Before each commit

- [ ] Build runs clean (`Site built: 25 pages`).
- [ ] No confidential file is staged (`git status` — check against `.gitignore`).
- [ ] Copy honours the content rules above.
- [ ] Links resolve; new pages appear in nav/footer as expected.
