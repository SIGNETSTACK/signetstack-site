# Deploy, update & migrate — SignetStack Labs site

The site is a **static build** (the `website/` folder: HTML, `assets/styles.css`, `assets/marks/*.svg`, `assets/img/*`). Source content lives in `assets/build_site.py`; running it regenerates `website/`.

Hosting: **GitHub Pages** (Signet Stack Ltd has GitHub Enterprise). A GitHub Action rebuilds and republishes on every change, so editing is "commit a change → site updates." Access is gated by the **GitHub org (Enterprise SSO/MFA)** — only org members can edit. With Enterprise you can keep the **source repo private** and still publish Pages.

---

## 1. One-time setup (GitHub Pages)

1. Create a repo in the Signet Stack Ltd org (private is fine on Enterprise) and push this project (root must include `.github/`, `assets/`, and `website/`).
2. Repo **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. The included workflow `.github/workflows/deploy.yml` does the rest on push to `main` (it `pip install pillow`, runs `python assets/build_site.py`, writes the `CNAME`/`.nojekyll`, and deploys `website/`). You can also run it manually (Actions → "Deploy website to GitHub Pages" → Run workflow).
4. First run publishes to `https://<org>.github.io/<repo>/` — verify it looks right, then add the custom domain below.

## 2. Custom domain — signetstack.io

`website/CNAME` already contains `signetstack.io`. In **Settings → Pages → Custom domain** enter `signetstack.io` and tick **Enforce HTTPS**. Then add DNS (at whoever manages the domain):

| Host | Type | Value |
|------|------|-------|
| `@` (apex) | `A` | `185.199.108.153` |
| `@` | `A` | `185.199.109.153` |
| `@` | `A` | `185.199.110.153` |
| `@` | `A` | `185.199.111.153` |
| `@` | `AAAA` (optional, IPv6) | `2606:50c0:8000::153` … `8003::153` |
| `www` | `CNAME` | `<org>.github.io.` |

HTTPS certificates provision automatically after DNS resolves (minutes–24h). Confirm `https://signetstack.io` loads with a valid padlock.

## 3. Email (so info@ / johnson@signetstack.io work)
Separate from the site: set up mail on the domain (Google Workspace / Microsoft 365 / Fastmail) and add **MX, SPF, DKIM, DMARC** records. (GitHub Pages records above are web-only.)

---

## Updating content (minimal, no separate CMS)

We deliberately keep this light — the rich no-code/drag-drop/visual editing lives in **Signetify** (the sister product), not here.

- **Easiest:** edit the text/links in `assets/build_site.py` (the `COMPANY`, `PLATFORM`, `MODULES`, `DIV`, `INSIGHTS`, `SOCIAL` data) directly in the **GitHub web editor** (or from your phone), commit — the Action rebuilds and republishes automatically. Org SSO is your auth; PR review is your safety net.
- **Add a brand/module:** add a `DIV`/`MODULES` entry (+ a mark) and commit.
- **Optional friendly UI (still git-based, free):** add **Sveltia CMS** (or Decap CMS) at `/admin` — a click-to-edit form UI authenticated via GitHub OAuth (your Enterprise SSO) that commits changes and triggers the same rebuild, with image uploads to a media folder. This is the lightest "no-code" layer and, being git-based, migrates cleanly. *(Ask and this can be wired up; it works best once content is externalized — see below.)*

> Recommended enabler: externalise the editable copy into a single `content.json` (decoupled from the build code). That makes web-editor edits trivial **and** makes the content portable for the Signetify migration. Not required to ship.

---

## Migrating the site into Signetify (when ready)

Because the site is **plain static HTML/CSS + structured content + assets**, it's portable. Options, cheapest→best:
1. **Re-host as-is** in Signetify if it accepts imported/custom-code sites — drop in the `website/` build; keep `signetstack.io` and just repoint DNS from Pages to Signetify.
2. **Re-platform the content**: import the structured content (ideally `content.json`) + media into Signetify's content model, and bring the design over as a Signetify theme. Migration becomes "map fields," not "re-author."
3. **Rebuild natively in Signetify** (best long-term, and dog-foods the product): recreate the design in Signetify, point `signetstack.io` at it. The current site remains the reference.

In all cases the domain, brand assets, and copy carry over; only the *hosting/editing layer* changes.

---

## Notes
- `website/assets/` (the real Signetify logo SVGs, favicon, brand-architecture poster) must be committed — the CI build keeps those and regenerates only the HTML + vector marks.
- Trademark clearance on the "SignetStack Labs" name is still advisable before heavy go-to-market.
- Social handles: LinkedIn confirmed; X/GitHub assume the `signetstack` slug — edit `SOCIAL` in `assets/build_site.py` if different.
