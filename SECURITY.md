# Security policy

This repository holds the source for the public **signetstack.io** website — a
static site with no backend, no authentication and no user data. The likely
scope of any issue here is limited (e.g. an outdated dependency in the build
workflow, a misconfiguration, or a content/link problem).

## Reporting a vulnerability

Please report security concerns privately. **Do not open a public issue** for a
suspected vulnerability.

- **Email:** info@signetstack.io (subject line: `SECURITY`)
- Alternatively, use GitHub's **private vulnerability reporting** on this
  repository (Security → Report a vulnerability) if enabled.

Please include: a description, steps to reproduce, affected URL/file, and impact.
We aim to acknowledge reports within **5 working days**.

## Scope

In scope:
- This repository's build scripts and CI workflow.
- Content/links served from signetstack.io that present a security risk
  (e.g. malicious redirect, exposed secret).

Out of scope:
- The Signet Stack products themselves (Velocity, the Signet Data Trust Network
  Platform, etc.) — these are not contained in this repository. Product security
  matters should also be sent to info@signetstack.io and will be routed
  appropriately.
- Findings that require physical access, social engineering, or denial-of-service
  testing against GitHub's infrastructure.

## Note on disclosure

The website intentionally states product maturity honestly (pre-GA and roadmap
items are labelled), and **claims no certification that is not held**. If you
believe any published claim is inaccurate, please contact info@signetstack.io.

Thank you for helping keep Signet Stack secure.
