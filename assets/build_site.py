#!/usr/bin/env python3
"""SignetStack Labs, data-driven multi-brand corporate website (static).
SignetStack Labs = master brand · Signet Stack Ltd = legal entity · Signetify = sister company.
Adding a future brand = add a dict to DIVISIONS + its SVG mark, then rebuild."""
import os, shutil, sys, html, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_brand_family import svg_mark, BRANDS  # build_brand_family is __main__-guarded (safe to import)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "website")
A = os.path.join(SITE, "assets")
os.makedirs(os.path.join(A, "marks"), exist_ok=True)
os.makedirs(os.path.join(A, "img"), exist_ok=True)

# ---------------- DATA ----------------
COMPANY = {"legal": "Signet Stack Ltd", "master": "SignetStack Labs", "year": "2026",
           "email": "info@signetstack.io",
           # Founder address is stored base64-encoded and assembled client-side (see footer
           # decoder) so the plaintext never appears in the HTML source or this repo, keeps it
           # human-usable on the page while staying out of crawlers / search indexes.
           "founder_email_b64": "am9obnNvbkBzaWduZXRzdGFjay5pbw==", "loc": "London · Remote-first",
           "reg": "13011013", "reg_line": "Registered in England &amp; Wales · Companies House No. 13011013",
           "office": "86-90 Paul Street, London EC2A 4NE",
           "tagline": "A house of frontier-technology brands."}

DIV = {  # slug -> enriched page data, sourced from each project's docs (public-safe)
 "velocity": {"key": "signetstack-velocity", "name": "Velocity Quant Technologies", "domain": "Velocity",
   "kicker": "Ultra-Low-Latency · HFT", "accent": "#12C2C9", "bright": "#16E0D4", "deep": "#0B7C82",
   "tagline": "Microsecond execution, built to be trusted with real capital.",
   "overview": "Velocity Quant Technologies builds production, institutional-grade trading and liquidity technology. Its flagship engine, HFT V5 Omni, watches multiple venues in microseconds, decides with a layered statistical, machine-learning and Bayesian stack, executes inside a hard safety perimeter, and learns from every outcome, running live on real money for eighteen months across five generations, with today's V5 in production for the last eight, and architected to extend across asset classes.",
   "caps": [("Microsecond speed","Quote-to-decision in single-digit microseconds end to end, using kernel-bypass networking and lock-free, CPU-pinned engineering found only in tier-1 firms."),
            ("Safe self-learning","A closed feedback loop scores its own predictions and recalibrates continuously, with guardrails that are harder to build than the learning itself."),
            ("Structural safety","An 18-trigger circuit breaker, a dead-man's switch and continuous capital reconciliation halt trouble automatically. It stops itself rather than press on."),
            ("Multi-strategy, multi-venue","Many strategies across many venues at once, coordinated without interference, double-spend or contagion."),
            ("It protects its edge","Disguises its own trading footprint so faster players cannot recognise the engine and trade against it."),
            ("Multi-asset by design","One proven core extends to FX, equities, commodities and indices as interchangeable plugins, extension, not rebuild.")],
   "audience": ["Proprietary trading desks, multi-strategy, low-latency execution","Brokers & venues, best-execution and smart order routing","Asset managers, systematic, regime-aware execution","Banks, treasury & FX-style conversion at a better blended rate","Securities exchanges, liquidity, market quality & member loyalty"],
   "diffs": [("The moat is the combination","Any one capability exists somewhere; assembling microsecond speed, safe learning, structural safety and multi-asset extensibility in one live system takes a specialist team years."),
             ("Never custodies funds","Capital stays in the institution's own venue accounts; the access granted cannot move money off-exchange and can be revoked instantly."),
             ("Measured, not modelled","Latency and safety are demonstrable on demand with real orders and a standing test suite, not back-tested claims.")],
   "tags": [], "status": "The engine has run live on real money for eighteen months across five generations and multiple cryptocurrency venues, with zero capital loss attributable to a software defect; the current generation, V5, has been in production for the last eight. The multi-asset roadmap (FX → equities → commodities → indices) extends the proven core rather than rebuilding it.",
   "stats": [("18 mo","live on real money · V1→V5"),("~9 µs","median decision latency"),
             ("1,971","tests · 0 failures · 4 safety tools"),("$0","defect-attributable capital loss")],
   "flagship": True},
 "pqc": {"key": "signetstack-pqc", "name": "SignetStack PQC", "domain": "PQC",
   "kicker": "Post-Quantum Cryptography", "accent": "#8B5CF6", "bright": "#A78BFA", "deep": "#5B3FC0",
   "tagline": "Quantum-resistant by default. Crypto-agile by design.",
   "overview": "SignetStack PQC is the cryptographic engine that protects long-lived, regulated data against the quantum threat, from day one, not a future migration project. It implements the NIST-standardized post-quantum algorithms (ML-KEM, ML-DSA, SLH-DSA) alongside proven classical primitives, with hybrid X25519 + ML-KEM key establishment, all behind a crypto-agile interface so new standards can be adopted without re-architecting your systems or invalidating historical records.",
   "caps": [("Standardized PQ signatures","ML-DSA (FIPS 204, CRYSTALS-Dilithium) plus SLH-DSA (FIPS 205, SPHINCS+) hash-based signatures for conservative, layered defense."),
            ("Standardized PQ key encapsulation","ML-KEM (FIPS 203, CRYSTALS-Kyber) for quantum-resistant key establishment."),
            ("Hybrid migration","Combined X25519 + ML-KEM key exchange, a secret stays protected unless both the classical and post-quantum parts are broken at once."),
            ("Crypto-agility","Algorithms sit behind a selectable interface; new standards can be added without breaking historical verification."),
            ("Signed, verifiable artifacts","Tamper-evident, hash-chained audit logging with post-quantum-signed attestations and deterministic, replayable verification."),
            ("Strong classical suite","AES-256-GCM, SHA-2/SHA-3, HKDF and ChaCha20-Poly1305, with hardware acceleration."),
            ("Portable to the edge","A heap-free, stack-only native path runs the same standardized primitives on constrained Cortex-M / RISC-V devices.")],
   "audience": ["Regulated financial services, long retention horizons under MiFID II, DORA, Basel III","Healthcare & life sciences, records under HIPAA / 21 CFR Part 11","Government & critical infrastructure, facing 2035 PQ-migration mandates","AI platforms, signing and proving data & audit provenance for the long run","Software & data platforms, embedding quantum-resistant signing and encryption"],
   "diffs": [("Post-quantum by default, not an upsell","Standardized PQC signing is the default path, eliminating the multi-year migration most enterprises still face."),
             ("Cross-implementation validation","Outputs are byte-checked against multiple independent implementations and NIST vectors, so a bug in any single library is caught."),
             ("Crypto-agility designed in early","Adopting a future standard is an additive change, never a re-architecture, and never invalidates historical chains."),
             ("Supply-chain provenance","Releases ship with SBOMs, signed provenance and reproducible-build verification.")],
   "tags": ["ML-KEM · FIPS 203","ML-DSA · FIPS 204","SLH-DSA · FIPS 205","Hybrid X25519 + ML-KEM","AES-256-GCM","SHA-2 / SHA-3","FIPS 140-3 (validation in progress)"],
   "status": "Live and in active use as the cryptographic core across the Signet Stack platform, an engine and SDK that products embed, rather than a standalone app. FIPS 140-3 module validation (CMVP) is in progress, not yet certified; quantum-resistant content encryption is on the roadmap.",
   "stats": [], "flagship": False},
 "ai-governance": {"key": "signetstack-aigov", "name": "SignetStack AI Governance", "domain": "AI Governance",
   "kicker": "AI Governance & Assurance", "accent": "#E3A52B", "bright": "#F4BE4A", "deep": "#9A6E14",
   "tagline": "Proof, not dashboards.",
   "overview": "SignetStack AI Governance turns every AI decision into cryptographic evidence a regulator can independently re-verify, years later, offline. It signs each governed action into a tamper-evident, timestamped, co-signed record the moment it happens; the dashboard is only a viewer, the cryptographic record is the source of truth. One underlying record projects into the evidence format each regulator expects, and every record is post-quantum-signed from day one.",
   "caps": [("Authority Attestation Chain","Every governed AI decision produces a signed record capturing who decided, under what policy, what was decided, and what action followed."),
            ("Tamper-evident chaining","Each record cryptographically references the previous one, so altering any historical entry breaks the chain and is immediately detectable."),
            ("Independent time anchoring","Records are counter-stamped by a third-party RFC 3161 timestamp authority, making post-dating cryptographically impossible."),
            ("Cross-witness co-signing","A peer node co-signs each record, so no single compromised system can forge one alone."),
            ("Offline replay verification","A standalone verifier lets auditors re-check the math themselves, years later, without depending on the vendor or any cloud."),
            ("Cross-regulator projection","One underlying record re-shapes into the evidence format each regulator's auditor expects, not a separate tool per regime."),
            ("Hard multi-tenant isolation","Every data surface is partitioned by tenant; a separately governed operator view exposes only aggregate status, never customer content.")],
   "audience": ["Regulated financial services: DORA, MiFID II, AI-driven decisions","Healthcare & life sciences: HIPAA, 21 CFR Part 11 workflows","High-risk AI operators in the EU: EU AI Act Annex III deployments","Compliance, risk & legal leaders: CISO, DPO, GRC, general counsel","Multi-tenant platform & managed-service operators"],
   "diffs": [("Evidence is the primitive, not the dashboard","Records are signed at the moment of the decision; a tool that ingests logs after the fact can never make them retroactively tamper-evident."),
             ("Post-quantum from day one","Quantum-resistant signing (ML-DSA) is the default, not a future migration project."),
             ("One record, many regulators","A single record projects into multiple regulatory languages at once, so compliance cost doesn't compound with each new regime."),
             ("Structural, not procedural, isolation","The operator/tenant boundary is enforced in the system's structure and verified by content-blind tests.")],
   "tags": ["EU AI Act","GDPR","DORA","MiFID II RTS 22","EU Cyber Resilience Act","NIST SSDF","Maps to SOC 2 criteria","Maps to ISO/IEC 27001:2022"],
   "status": "A working, verifiable platform approaching commercial general availability, not yet a fully GA, certified product. The core attestation chain, timestamping, co-signing, offline verifier and projections for DORA / MiFID II / CRA are live; HIPAA and 21 CFR Part 11 projections, hardware-backed keys, and platform certifications (SOC 2, ISO 27001) are on the roadmap.",
   "stats": [], "flagship": False},
 "dxp": {"key": "signetstack-dxp", "name": "SignetStack DXP", "domain": "DXP",
   "kicker": "Digital Experience Platform", "accent": "#FF5C8A", "bright": "#FF85A8", "deep": "#C53E6A",
   "tagline": "The digital experience platform built for the agentic era.",
   "overview": "SignetStack DXP is an enterprise, headless, agent-first digital experience platform, a composable content, commerce and AI substrate where compliance and auditability are built into the architecture, not bolted on. It serves any frontend, channel or AI agent through open APIs, with a tamper-evident audit trail woven into the core. Its no-code sibling product, Signetify, lives at signetify.com; SignetStack DXP is the enterprise platform underneath, for organisations that must power many frontends from one governed backend.",
   "caps": [("Headless content","Content is served as structured data through a unified API; any frontend renders it however it wants, no presentation opinions in the backend."),
            ("Agent-first commerce","Native support for AI agents acting on a user's behalf, with cryptographically scoped, bounded authority and full attribution of every action."),
            ("Personalization & adaptive UX","Real-time, context-aware experiences driven by behavioural signals as a closed feedback loop, not a batch pipeline."),
            ("Omnichannel delivery","One backend, many channels, websites, apps, documentation, commerce surfaces and machine/agent consumers."),
            ("Composable integrations","Open, swap-in interfaces for payments, key management (BYOK), search and AI inference, integrate what you already use, avoid lock-in."),
            ("AI-native search","Hybrid semantic + keyword search with encryption at rest, so relevance and confidentiality coexist."),
            ("Experimentation & analytics","A/B testing and a time-series analytics pipeline for measuring experiences and surfacing emerging segments.")],
   "audience": ["Regulated enterprises, finance, healthcare, public sector","Digital & e-commerce teams, headless storefronts and content","Platform & engineering leaders, composable, API-first, no lock-in","Teams adopting AI agents, governed and bounded","Compliance, risk & security stakeholders in the due-diligence seat"],
   "diffs": [("Compliance built into the architecture","Auditability and regulatory mapping are core design properties, not optional add-ons."),
             ("Tamper-evident audit trail","Every event is cryptographically chained, making the record independently verifiable and resistant to silent tampering."),
             ("Bounded, governed AI agents","Agent authority is cryptographically scoped with explicit limits and human-checkpoint thresholds, autonomy without losing accountability."),
             ("Composable & lock-in-resistant","Open interfaces across payments, keys, AI and search let enterprises bring their own providers.")],
   "tags": ["Headless / API-first","GDPR (consent & erasure)","Designed for SOC 2 alignment","Designed for ISO 27001 alignment","BYOK","Post-quantum ready"],
   "status": "Pre-GA, available for design partners and early access. The platform is a working, multi-module implementation across content, commerce, AI, search and agents; formal SOC 2 / ISO 27001 certification, and some generative/voice and real-time features, are on the roadmap.",
   "stats": [], "flagship": False},
 "research": {"key": "signetstack-rnd", "name": "SignetStack R&D", "domain": "R&D",
   "kicker": "Research & Advanced Development", "accent": "#10B981", "bright": "#34D399", "deep": "#0A6E50",
   "tagline": "The innovation arm of SignetStack Labs, where the hardest cryptography, agentic AI and the future of the web are invented, and proven before they ship.",
   "overview": "SignetStack R&D is the innovation, research and advanced-development arm of SignetStack Labs, where the hardest problems are invented around before they are productised. Its proven output today is the post-quantum, hardware-adaptive cryptographic core that every Signet product inherits, from the Signet Data Trust Network Platform to the independent venture Velocity Quant Technologies. Its frontier reaches into agentic AI, multimodal generation and the future of the web. The method never changes: nothing graduates on a claim, every result is run through the Signet Observatory as a reproducible, tamper-evident proof before it reaches production.",
   "caps": [("Post-quantum & crypto-agility","Backend-agnostic post-quantum cryptography: ML-KEM, ML-DSA and SLH-DSA behind a stable interface, so adopting a new NIST-standardized library or algorithm is an additive change, never a re-architecture, and never invalidates historical records."),
            ("Standards & validation research","Novel approaches to validating hybrid classical + post-quantum cryptographic modules to FIPS 140-3 / CMVP across multiple hardware and OS targets from a single codebase. Validation is in preparation, not yet certified."),
            ("Hardware-adaptive, accelerated crypto","Secure, AI-native cryptographic compute that adapts across CPU SIMD paths (AES-NI, ARMv8) and GPU backends, choosing the fastest safe path for the workload without changing the security model."),
            ("Cryptography at the web & edge boundary","Novel patterns for safe GPU-accelerated cryptography across the browser/WASM trust boundary and on constrained edge devices, designed so key material never crosses the boundary, with a tamper-evident trail for everything that does."),
            ("Proof, not promises, the Signet Observatory","An experiment control plane that runs reproducible proof experiments across cryptography, machine learning, agents, trust and performance, with hash-chained, tamper-evident results anyone can inspect.")],
   "frontiers": [
     {"name": "Cryptography", "tag": "Quantum-safe, end to end.", "items": [
        ("Hybrid post-quantum transport", "TLS 1.3 hybrid key exchange, classical X25519 combined with ML-KEM, so connections resist <em>harvest-now, decrypt-later</em> attacks, with graceful fallback for legacy peers.", False),
        ("Quantum-safe identity &amp; credentials", "Decentralised identifiers and verifiable credentials signed with post-quantum signatures, with privacy-preserving selective disclosure, including verifiable identity for autonomous agents.", False),
        ("Post-quantum supply-chain attestation", "Quantum-resistant signing of software bills-of-materials with transparency logging, so provenance stays verifiable across decade-long lifecycles.", False),
        ("Long-term crypto-agile archival", "Algorithm-agnostic re-encryption and epoch re-keying for multi-decade retention, today's records survive tomorrow's standards.", False),
        ("Quantum key distribution &amp; PQ ledgers", "Physics-based key distribution as a future key source (post-quantum cryptography always the fallback), and a quantum-native, Byzantine-fault-tolerant ledger for tamper-evident governance records.", True)]},
     {"name": "Autonomous &amp; interpretable AI", "tag": "Autonomy you can audit.", "items": [
        ("AI as a supervisory safety layer", "Language-model agents acting as a deliberative risk and governance layer, never on the latency-critical path, interpreting context and enforcing policy.", False),
        ("Glass-box interpretability", "Instrumenting every decision so its full reasoning trace, attributions, context and counterfactuals, can be inspected and explained: from <em>trust it</em> to <em>audit it</em>.", False),
        ("Generative digital-twin rehearsal", "High-fidelity generative simulations that rehearse strategies and policies across thousands of synthetic scenarios, including crises, before anything touches production.", False),
        ("Causal inference &amp; collective learning", "Reasoning about interventions and counterfactuals rather than mere correlation, and privacy-preserving federated learning so a fleet improves together by sharing model updates, never raw data.", False),
        ("Constitutional governance &amp; safe autonomy", "Machine-enforceable, version-controlled policy with human amendment and override, plus scoped, sandboxed, human-reviewed self-improvement, every autonomous capability with explicit escape hatches.", False),
        ("Autonomous economic agents", "Long-horizon research into AI that operates as a governed legal-economic entity, and secure agent-to-agent settlement protocols.", True)]},
     {"name": "Experience &amp; the future web", "tag": "Invent the site, don't template it.", "items": [
        ("Multimodal design ingestion", "Turning a screenshot, a screen recording, a wireframe or a design file into a working, production-ready site through vision-model decomposition.", False),
        ("Agentic web operations", "Bounded, human-overridable AI agents that build, run and operate a site, autonomy without losing accountability.", False),
        ("Adaptive composition &amp; personalization", "Every design and content choice treated as a learned, evidence-weighted decision, with experiences that improve in real time from engagement signals.", False),
        ("Immersive &amp; generative experience", "3D and spatial interfaces, generative and data-driven visuals, motion and gamification as first-class design primitives.", False),
        ("Native retrieval: Signet RAG", "Retrieval-augmented generation grounded in verifiable, provenance-tracked data, answers you can trace.", False)]},
     {"name": "Scale &amp; production hardening", "tag": "Built to grow without surprises.", "items": [
        ("Staged capacity engineering", "Composable scaling, horizontal compute, read replicas, connection pooling, hot-path caching and columnar analytics, that grows throughput predictably while keeping latency low.", False),
        ("Metric-driven autoscaling", "Precise, measurable thresholds that turn capacity decisions into observable, predetermined actions rather than guesswork.", False),
        ("Purpose-built event storage", "High-ingest, columnar time-series storage for extreme-scale event workloads.", False),
        ("Open, secure substrate", "Durable workflow orchestration, unified observability and a zero-trust, defence-in-depth posture built on open standards.", False)]}],
   "audience": [],
   "diffs": [("Proof-first, not paper-first","Every result is reproduced as a verifiable, hash-chained experiment before it ships, research you can independently re-run, not claims you have to take on trust."),
             ("Built once, inherited everywhere","R&D output isn't a demo; it lands in the shared cryptographic core that the platform and every Signet brand are built on."),
             ("Honest about maturity","We separate what's proven, what's in preparation, and what's still on the bench, and we never claim a certification we don't hold.")],
   "tags": ["NIST FIPS 203: ML-KEM","FIPS 204: ML-DSA","FIPS 205: SLH-DSA","FIPS 140-3, in preparation","Hybrid classical + PQ","Crypto-agile by design"],
   "status": "SignetStack R&D is an active research function, not a product you buy, its outputs ship inside Signet products as they mature. Post-quantum primitives (ML-KEM, ML-DSA, SLH-DSA) and hardware-adaptive cryptography are implemented and exercised today; FIPS 140-3 / CMVP validation is in preparation and not yet certified; the GPU/AI-accelerated and web/edge crypto-safety tracks are at research-to-hardening stage.",
   "stats": [("3","NIST PQC standards in use: ML-KEM, ML-DSA, SLH-DSA"),("4","active research tracks"),("CPU · GPU · edge","hardware-adaptive crypto targets"),("Proof-first","reproducible, hash-chained results")],
   "flagship": False},
}
ORDER = ["dxp", "research", "velocity"]   # SignetStack product brands (besides the platform)
SIGNETIFY_URL = "https://signetify.com"
DEMO_PADES = """<section class="band" id="demo"><div class="wrap"><div class="sec-head"><div class="kick">Try it now</div><h2>Sign a PDF in your browser. Nothing leaves your machine.</h2><p class="lead">Choose a PDF or a sample. We sign it, verify the signature, then tamper a byte so you can watch verification fail. The signing runs entirely client-side in the demo; classical signatures here, the post-quantum path is the product.</p></div><div class="card" style="padding:0;overflow:hidden;border-radius:14px"><iframe src="https://signetstack.github.io/signet-pades-demo/" title="Signet PAdES live signing demo" loading="lazy" style="display:block;width:100%;height:740px;border:0;background:#fff" sandbox="allow-scripts allow-same-origin allow-downloads" referrerpolicy="no-referrer"></iframe></div><p class="muted" style="margin-top:12px;font-size:.85rem">Demo hosted at <code>signetstack.github.io/signet-pades-demo</code>. If the iframe is blocked, <a href="https://signetstack.github.io/signet-pades-demo/" target="_blank" rel="noopener">open it in a new tab</a>.</p></div></section>"""

# ---- The Signet Data Trust Network Platform (canonical, from SDTNP) ----
PA, PAB, PAD = "#6E8AFF", "#9DB4FF", "#3D5BD9"   # one signature accent for the whole platform
PLATFORM = {"name": "Signet Data Trust Network Platform", "short": "Data Trust Network Platform",
   "accent": PA, "bright": PAB, "deep": PAD,
   "thesis": "PKI proves who you are. Signet proves what happened to your data.",
   "tagline": "Cryptographic, post-quantum proof for regulated data, across its whole lifecycle.",
   "overview": "The Signet Data Trust Network Platform is a vertically-integrated, post-quantum data-trust platform for regulated industries. It replaces narrative compliance, editable logs, deletion-by-form, keys in spreadsheets, with verifiable cryptographic proof of a datum's integrity, provenance, lawful basis, access history and irreversible erasure, across every format and every stage of its lifecycle. A shared cryptographic foundation lets a single dataset be traced, ingested, governed, stored, trained on, attested, with each transition independently signed and verifiable by any regulator or counterparty.",
   "layers": [("Foundation","Signet Core + Signet Forge, the post-quantum crypto, data-format, audit-chain and erasure primitives every module is built on."),
              ("Key custody","Signet Vault, the key hierarchy and provable crypto-erasure the platform depends on."),
              ("Domain modules","AI Governance, Lake, Stream, Clean Room and Embedded, governance, encryption at rest, in motion, in collaboration, and at the edge."),
              ("Trust network","Signet Data Trust Network, the cross-organisation transparency log that makes provenance verifiable by anyone."),
              ("Intelligence & experience","Signet Inference Engine and Signet Intelligence power AI and analytics; a compliance dashboard surfaces the platform.")],
   "certs": ["FIPS 140-3: CMVP validation in preparation","SOC 2, in planning","ISO 27001, in planning","NCSC CPA, planned","Common Criteria, on the roadmap"]}

MODULE_ORDER = ["core", "vault", "kms", "ai-governance", "lake", "stream", "clean-room", "embedded", "data-trust-network", "pades"]
MODULES = {
 "core": {"name": "Signet Core", "icon": "core", "kicker": "Post-Quantum Foundation",
   "tagline": "The cryptographic engine the whole platform is built on.",
   "overview": "Signet Core is the cryptographic and data engine every Signet module is built on: FIPS-track AES-256-GCM, SHA-2/3 and HKDF alongside the NIST-standardized post-quantum algorithms ML-KEM-768 and ML-DSA-65, plus the tamper-evident audit-chain and verifiable crypto-erasure primitives the rest of the platform depends on.",
   "caps": [("Post-quantum by default","ML-KEM-768 (FIPS 203) and ML-DSA-65 (FIPS 204), with hybrid X25519 + ML-KEM key establishment."),
            ("FIPS-track classical suite","AES-256-GCM, SHA-2 / SHA-3, HKDF and DRBG, with hardware acceleration."),
            ("Audit-chain & erasure","Tamper-evident hash-chaining and verifiable crypto-erasure, reused across every module."),
            ("Crypto-agile","Algorithms sit behind a selectable interface, so new standards drop in without re-architecting."),
            ("Encrypted Parquet: Signet Forge","A companion library brings modular + post-quantum encryption to Apache Parquet, with a WebAssembly demo you can try in your browser. <a href=\"signet-forge.html\">See Signet Forge →</a>")],
   "tags": ["ML-KEM · FIPS 203","ML-DSA · FIPS 204","SLH-DSA · FIPS 205","Hybrid X25519 + ML-KEM","AES-256-GCM"],
   "status": "A library and engine, in active use across the platform, not a standalone app. FIPS 140-3 module validation (CMVP) is in preparation, not yet certified."},
 "vault": {"name": "Signet Vault", "icon": "vault", "kicker": "Post-Quantum Key Management",
   "tagline": "Keys, custody and provable erasure, quantum-resistant.",
   "overview": "Signet Vault is the platform's post-quantum key-management service: a layered key hierarchy with hardware-backed custody (PKCS#11 / HSM), and GDPR Article 17 crypto-shredding that produces signed, independently-verifiable proofs that data is irrecoverable.",
   "caps": [("Layered key hierarchy","A multi-level hierarchy with hardware-backed roots and per-tenant data keys."),
            ("Crypto-shred erasure","GDPR Art.17 erasure by destroying keys, with a signed proof the data can never be recovered."),
            ("Shamir secret sharing","Split the most critical secrets so no single holder can reconstruct them."),
            ("HSM & REST API","PKCS#11 hardware modules behind a clean REST interface for every module.")],
   "tags": ["PKCS#11 / HSM","GDPR Art.17","Post-quantum"], "status": "Pre-GA."},
 "kms": {"name": "Signet KMS", "icon": "kms", "kicker": "Confidential-Computing Key Management",
   "tagline": "Enclave-isolated keys, multi-tenant, post-quantum-aware.",
   "overview": "Signet KMS is the portfolio-wide, post-quantum-aware key-management service: a multi-tenant KMS whose most sensitive operations run inside a confidential-computing enclave, so plaintext key material never leaves a hardware-isolated boundary. Every caller is bound to its own tenant by mutual TLS, sensitive operations can require M-of-N quorum approval, keys can be federated across organisations, and every operation emits a signed, four-layer attestation bundle.",
   "caps": [("Enclave-isolated operations","A TEE worker models the Nitro Enclave boundary, key unwrap, re-seal and HMAC happen inside; plaintext key material never crosses the enclave."),
            ("KEK / DEK / signer managers","Key-encryption keys, data-encryption keys and signing keys, sharded per tenant for hard isolation."),
            ("mTLS tenant binding","Mutual-TLS with a certificate SAN-URI bound to the tenant, so a caller can only ever reach its own keys."),
            ("Quorum & federation","M-of-N quorum approval for sensitive operations, plus cross-organisation key federation."),
            ("Per-operation attestation","Every operation emits a four-layer signed bundle, identity, policy, decision, commitment, for independent audit."),
            ("Confidential cloud or on-prem","Deploys to AWS Nitro, Azure Confidential and GCP Confidential VMs, or an on-prem PKCS#11 HSM.")],
   "tags": ["Confidential computing","AWS Nitro / Azure / GCP","mTLS · per-tenant","FIPS 140-3 algorithm map","Post-quantum-aware"],
   "status": "K-1 alpha (v0.1.0-alpha), core key managers, the mutual-TLS REST surface, the confidential-computing worker, quorum/federation and per-operation attestation are implemented; FIPS-mode operation and SOC 2 Type I scoping are in preparation, not yet certified."},
 "ai-governance": {"name": "Signet AI Governance", "icon": "aigov", "kicker": "EU AI Act & GDPR Compliance Engine",
   "tagline": "Proof, not dashboards.",
   "overview": "Signet AI Governance turns every AI decision into cryptographic evidence a regulator can independently re-verify, years later, offline. It signs each governed action into a tamper-evident, timestamped, co-signed record the moment it happens; the dashboard is only a viewer, the cryptographic record is the source of truth. One underlying record projects into the evidence format each regulator expects, and every record is post-quantum-signed from day one.",
   "caps": [("Authority Attestation Chain","Each governed AI decision produces a signed record of who decided, under what policy, what was decided, and what followed."),
            ("Tamper-evident chaining","Each record references the previous one, so altering history breaks the chain and is immediately detectable."),
            ("Independent time anchoring","Counter-stamped by a third-party RFC 3161 authority, making post-dating cryptographically impossible."),
            ("Cross-witness co-signing","A peer node co-signs each record, so no single compromised system can forge one alone."),
            ("Offline replay verification","A standalone verifier lets auditors re-check the math themselves, without the vendor or any cloud."),
            ("Cross-regulator projection","One record re-shapes into the evidence each regulator's auditor expects, not a tool per regime.")],
   "tags": ["EU AI Act","GDPR","DORA","MiFID II RTS 22","EU Cyber Resilience Act","Maps to SOC 2 / ISO 27001"],
   "status": "The most mature module, a working, verifiable platform approaching general availability. Core attestation, timestamping, co-signing, the offline verifier and projections for DORA / MiFID II / CRA are live; HIPAA and 21 CFR Part 11 projections and platform certifications are on the roadmap."},
 "lake": {"name": "Signet Lake", "icon": "lake", "kicker": "Lakehouse Encryption",
   "tagline": "Column-level, post-quantum encryption for data lakes.",
   "overview": "Signet Lake brings FIPS-track, per-column encryption to data lakehouses, with column-level access control and verifiable crypto-erasure, across S3, ADLS, GCS and local backends.",
   "caps": [("Per-column encryption","Encrypt individual columns with modular post-quantum encryption."),
            ("Column-level RBAC","Allow, deny or redact access at the column level."),
            ("Crypto-shred erasure","Verifiable erasure of a subject's data by key destruction."),
            ("Multi-cloud backends","S3, ADLS, GCS and local storage.")],
   "tags": ["S3 / ADLS / GCS","Post-quantum","GDPR Art.17"], "status": "Pre-GA."},
 "stream": {"name": "Signet Stream", "icon": "stream", "kicker": "Real-Time Secure Pipeline",
   "tagline": "Post-quantum security for data in motion.",
   "overview": "Signet Stream secures real-time data pipelines with a hash-chained, encrypted write-ahead log, post-quantum epoch sealing, and streaming GDPR erasure, with Arrow Flight and FIX 4.4/5.0 ingest for high-throughput and market data.",
   "caps": [("Hash-chained encrypted WAL","Every record chained and encrypted as it streams."),
            ("Signed epoch sealing","Periodic Merkle epochs sealed with post-quantum (ML-DSA-65) signatures."),
            ("Arrow Flight & FIX ingest","High-throughput ingest, including FIX 4.4/5.0 for market data."),
            ("Streaming erasure","GDPR erasure applied to data in motion.")],
   "tags": ["Arrow Flight","FIX 4.4 / 5.0","Post-quantum"], "status": "Pre-GA."},
 "clean-room": {"name": "Signet Clean Room", "icon": "cleanroom", "kicker": "Multi-Party Collaboration",
   "tagline": "Collaborate on data you never have to share.",
   "overview": "Signet Clean Room lets multiple organisations compute over shared data without exposing it, private set intersection, federated learning with differential privacy, and federated SQL, with jointly-signed Model Passports.",
   "caps": [("Private set intersection","Find overlaps without revealing either party's full dataset."),
            ("Federated learning + DP","Train across parties with differential-privacy budgets, data stays put."),
            ("Federated SQL","Query across organisations under policy."),
            ("Joint Model Passports","Signed provenance for jointly-trained models.")],
   "tags": ["Differential privacy","Federated learning","Post-quantum"], "status": "Pre-GA."},
 "embedded": {"name": "Signet Embedded", "icon": "embedded", "kicker": "Edge / OT / ICS Security SDK",
   "tagline": "Post-quantum security down to the device.",
   "overview": "Signet Embedded is a zero-heap post-quantum security SDK for edge, OT and ICS devices: ML-KEM-768 and ML-DSA-65 plus stateful hash-based signatures, device attestation, and a tamper-evident on-device audit ledger, for Cortex-M and RISC-V.",
   "caps": [("Zero-heap PQC","ML-KEM-768 / ML-DSA-65 with no heap allocation, for constrained devices."),
            ("Stateful hash signatures","HSS / LMS for long-lived device identities."),
            ("Device attestation","Prove a device's identity and integrity."),
            ("On-device audit ledger","A compact, tamper-evident ledger in as little as 32 KB.")],
   "tags": ["Cortex-M / RISC-V","ML-KEM / ML-DSA","HSS / LMS"], "status": "Pre-GA, a header-only library."},
 "data-trust-network": {"name": "Signet Data Trust Network", "icon": "dtn", "kicker": "Cross-Org Provenance Network",
   "tagline": "A transparency log for what happened to data.",
   "overview": "The Signet Data Trust Network is the cross-organisation provenance layer: an append-only, Merkle-tree transparency log (RFC 6962-style), post-quantum-signed, with a regulator export API and split-view detection, so any counterparty or regulator can verify a datum's full history.",
   "caps": [("Append-only Merkle log","A tamper-evident, RFC 6962-style transparency log."),
            ("Post-quantum signed","Every attestation signed with ML-DSA-65."),
            ("Regulator export API","Hand a regulator a verifiable evidence bundle on demand."),
            ("Split-view detection","Gossip-based checks so no one is shown a different version of history.")],
   "tags": ["RFC 6962-style","Post-quantum","Regulator export"], "status": "Pre-GA, the network emerges as modules publish attestations to it."},
 "pades": {"name": "Signet PAdES Enterprise", "icon": "pades", "kicker": "Post-Quantum Advanced E-Signatures (AdES)",
   "tagline": "Long-term, quantum-resistant signatures across the whole AdES family.",
   "overview": "Signet PAdES Enterprise is a from-scratch, dependency-light post-quantum digital-signature engine that spans the entire ETSI AdES family: PAdES for PDFs, CAdES for binary/CMS, XAdES for XML and JAdES for JSON/JWS, at the B-B, B-T, B-LT and B-LTA profiles, signed with ML-DSA-65 (FIPS 204). It does not just produce signatures: it independently validates them too, including decade-old long-term archival signatures from other vendors, making it a verification engine as much as a signer.",
   "caps": [("The whole AdES family","PAdES (PDF), CAdES (CMS), XAdES (XML) and JAdES (JSON/JWS), one engine, four ETSI standards, no third-party signing library."),
            ("Every profile, end to end","B-B, B-T, B-LT and B-LTA across each family, produced and verified, including long-term archival (LTA) timestamps."),
            ("Post-quantum signing","ML-DSA-65 (FIPS 204) via RFC 9882 ML-DSA-in-CMS, alongside classical ECDSA / Ed25519 for mixed estates."),
            ("Verifies others' signatures","Validates third-party and decade-old archival signatures at audit time, byte-exactly reproducing the ETSI archive-time-stamp-v3 imprint and validating EU DSS CAdES-LTA timestamps. Re-validate counterparty signatures for eIDAS, cross-border contracts and multi-vendor archives."),
            ("Independently cross-checked","Output is verified against independent oracles, qpdf, OpenSSL CMS, poppler pdfsig, EU DSS 6.4 and veraPDF, not just self-reported."),
            ("Self-verifying & fail-closed","Every signature performs a round-trip verify and fails closed; long-term validation via DSS dictionary, OCSP/CRL embedding and RFC 3161 timestamps.")],
   "tags": ["ETSI EN 319 142 · PAdES","EN 319 122 · CAdES","EN 319 132 · XAdES","TS 119 182 · JAdES","B-B / B-T / B-LT / B-LTA","ML-DSA-65 · FIPS 204","eIDAS-aligned"],
   "status": "The signature engine is complete and verified across all four AdES families and all four profiles, producing and independently validating signatures, cross-checked against qpdf, OpenSSL, poppler, EU DSS 6.4 and veraPDF. Enterprise / multi-tenant SaaS tiers are on the roadmap."},
}
COMPONENTS = [("Signet Forge","forge","Encrypted Apache Parquet, modular + post-quantum encryption for columnar data."),
              ("Signet Inference Engine","inference","FIPS-auditable, SIMD-accelerated ML inference with signed Model Passports."),
              ("Signet Intelligence","intelligence","ML anomaly detection and a SIEM bridge over platform audit metadata.")]

# stroke line-icons (24-grid, currentColor)
ICONS = {
 "core": '<polygon points="12,3 20,7.5 20,16.5 12,21 4,16.5 4,7.5"/><circle cx="12" cy="12" r="2.6" fill="currentColor" stroke="none"/>',
 "vault": '<rect x="3.5" y="5" width="17" height="14" rx="2"/><circle cx="12" cy="12" r="3"/><path d="M12 12 v2.4"/><path d="M7 19 v1.6 M17 19 v1.6"/>',
 "kms": '<rect x="3.5" y="3.5" width="17" height="17" rx="3.5"/><circle cx="12" cy="9.7" r="2.5"/><path d="M12 12.2 V17"/><path d="M12 14.6 h2.3 M12 16.3 h1.7"/>',
 "aigov": '<circle cx="12" cy="12" r="8"/><path d="M8.6 12.2 l2.2 2.2 l4.6-5"/>',
 "lake": '<ellipse cx="12" cy="6" rx="7" ry="2.6"/><path d="M5 6 v6 c0 1.4 3.1 2.6 7 2.6 s7-1.2 7-2.6 V6"/><path d="M5 12 c0 1.4 3.1 2.6 7 2.6 s7-1.2 7-2.6"/>',
 "stream": '<path d="M3 8 q4 -3.2 8 0 t8 0"/><path d="M3 13 q4 -3.2 8 0 t8 0"/><path d="M3 18 q4 -3.2 8 0 t8 0"/>',
 "cleanroom": '<circle cx="9" cy="12" r="5.4"/><circle cx="15" cy="12" r="5.4"/>',
 "embedded": '<rect x="7" y="7" width="10" height="10" rx="1.5"/><path d="M10 4 v3 M14 4 v3 M10 17 v3 M14 17 v3 M4 10 h3 M4 14 h3 M17 10 h3 M17 14 h3"/>',
 "dtn": '<circle cx="6" cy="7" r="2"/><circle cx="18" cy="7" r="2"/><circle cx="12" cy="18" r="2"/><path d="M7.6 8.4 L10.8 16.2 M16.4 8.4 L13.2 16.2 M8 7 h8"/>',
 "pades": '<polygon points="12,3 20,7.5 20,16.5 12,21 4,16.5 4,7.5"/><path d="M8 10 h8 v5 h-8 z"/><path d="M8 10 l4 3 l4-3"/><circle cx="12" cy="13" r="1.4" fill="currentColor" stroke="none"/>',
 "forge": '<rect x="4" y="4" width="6.5" height="6.5" rx="1"/><rect x="13.5" y="4" width="6.5" height="6.5" rx="1"/><rect x="4" y="13.5" width="6.5" height="6.5" rx="1"/><rect x="13.5" y="13.5" width="6.5" height="6.5" rx="1"/>',
 "inference": '<circle cx="6" cy="7" r="1.7"/><circle cx="6" cy="17" r="1.7"/><circle cx="18" cy="12" r="1.7"/><path d="M7.6 7.7 L16.4 11.4 M7.6 16.3 L16.4 12.6"/>',
 "intelligence": '<path d="M3 12 h4 l2-6 l3 13 l2.4-9 l1.4 4 h5.8"/>',
 "platform": '<polygon points="12,3 20,7.5 20,16.5 12,21 4,16.5 4,7.5"/><path d="M12 7.5 l4 2.2 v4.6 l-4 2.2 l-4-2.2 V9.7z"/>',
}
def icon_svg(key):
    return f'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{ICONS.get(key,"")}</svg>'
def mslug(k): return "signet-" + k

# Social: LinkedIn confirmed; X / GitHub assumed at the 'signetstack' slug (edit if different)
SOCIAL = [("LinkedIn", "https://uk.linkedin.com/company/signetstack", "linkedin"),
          ("X", "https://x.com/signetstack", "x"),
          ("GitHub", "https://github.com/signetstack", "github")]
SOCIAL_ICONS = {
 "linkedin": '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z"/>',
 "x": '<path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231 5.45-6.231zm-1.161 17.52h1.833L7.084 4.126H5.117l11.966 15.644z"/>',
 "github": '<path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>',
}
def social_row():
    return "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{SOCIAL_ICONS[k]}</svg></a>' for n, u, k in SOCIAL)

SISTER = {"name": "Signetify", "accent": "#00A6C2", "bright": "#2BC4DD", "deep": "#0E91A8", "gold": "#FACD2A",
   "tagline": "The trust layer for the agentic web.",
   "blurb": "Signetify is a sister company in the Signet Stack family, the AI-native platform for building, running and growing online businesses, where you and an AI agent are equal collaborators on the same live site, and every asset and transaction carries built-in, verifiable provenance."}

INSIGHTS = [
 {"slug":"house-of-brands","title":"Why we built SignetStack Labs as a house of brands","date":"May 2026","author":"SignetStack Labs",
  "excerpt":"One proven core, many specialist brands, and why that structure compounds.",
  "body":["The hardest parts of frontier technology, speed, safety, learning, operational maturity, are expensive to build once and wasteful to rebuild per market.",
          "SignetStack Labs is structured so that the proven core is built once and inherited by every brand. PQC, AI Governance and DXP carry the same engineering discipline into their own domains; the independent venture Velocity Quant Technologies, separately owned, applies that discipline in trading.",
          "The result is a family that grows by extension, not by starting over, and every improvement to the shared foundation lifts every brand at once."]},
 {"slug":"pqc-readiness","title":"Post-quantum readiness: why crypto-agility matters now","date":"Apr 2026","author":"SignetStack PQC",
  "excerpt":"You don't migrate to post-quantum cryptography overnight. You make it swappable.",
  "body":["The migration to post-quantum cryptography is not a single switch, it is a multi-year programme across systems most organisations have never fully inventoried.",
          "The pragmatic first step is crypto-agility: abstracting algorithms behind a policy layer so primitives can be replaced as standards finalise, without re-architecting applications.",
          "Start by discovering where cryptography lives, prioritise what is most exposed, and run hybrid schemes through the transition."]},
 {"slug":"auditable-ai","title":"Governing AI you can actually audit","date":"Mar 2026","author":"SignetStack AI Governance",
  "excerpt":"Explainability and tamper-evident audit turn AI risk from a worry into a control.",
  "body":["Boards and regulators are converging on the same question: when an AI system makes a decision, can you explain it, and can you prove what happened?",
          "Two capabilities make that answerable, explainability that reads in plain language, and a tamper-evident audit trail that can be replayed.",
          "Governance should reduce how often a human must intervene, never the human's ultimate authority."]},
]

ROLES = [("Applied Cryptographer","SignetStack PQC","Remote"),
         ("ML Governance Lead","SignetStack AI Governance","Remote / London"),
         ("Senior Frontend Engineer","SignetStack DXP","Remote"),
         ("Founding Brand Designer","SignetStack Labs","Remote / London"),
         ("Senior Systems Engineer (Low-Latency)","Velocity Quant Technologies","Remote / London")]

# ---------------- master mark SVG (inline, neutral) ----------------
import math
def hexpts(cx, cy, R): return [(cx + R*math.cos(math.radians(60*i-90)), cy + R*math.sin(math.radians(60*i-90))) for i in range(6)]
def svg_master(color):
    o = " ".join(f"{x:.1f},{y:.1f}" for x, y in hexpts(60, 67, 55)); inner = " ".join(f"{x:.1f},{y:.1f}" for x, y in hexpts(60, 67, 55*0.46))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 134"><polygon points="{o}" fill="none" stroke="{color}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/><polygon points="{inner}" fill="{color}"/></svg>')
def svg_signetify(color, bright):
    # distinct (non-hexagon) sister mark: rounded square seal + check
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120">'
            f'<rect x="14" y="14" width="92" height="92" rx="26" fill="none" stroke="{color}" stroke-width="9"/>'
            f'<path d="M40 62 L55 77 L83 44" fill="none" stroke="{bright}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def write_marks():
    M = os.path.join(A, "marks")
    open(f"{M}/master-white.svg", "w").write(svg_master("#E8EDF2"))
    open(f"{M}/master-carbon.svg", "w").write(svg_master("#0B0F14"))
    bykey = {b["key"]: b for b in BRANDS}
    for slug in ORDER:
        b = bykey[DIV[slug]["key"]]; open(f"{M}/{slug}.svg", "w").write(svg_mark(b["accent"], b["glyph"], b["accent"], b["bright"]))
    open(f"{M}/signetify.svg", "w").write(svg_signetify(SISTER["accent"], SISTER["bright"]))
    # favicon-ish: copy master rounded icon if present
    src = os.path.join(ROOT, "SignetStack_Labs_Master_Brand_Kit", "icons", "favicon-256.png")
    if os.path.exists(src): shutil.copy(src, os.path.join(A, "img", "favicon.png"))
    # (brand architecture is now a responsive CSS diagram, arch_diagram(); no poster PNG)
    # real Signetify brand SVGs (source of truth in ~/Downloads)
    dl = os.path.expanduser("~/Downloads")
    for src_name, dst in [("signetify.svg", "signetify-logo.svg"), ("FAVICON signetify.svg", "signetify-icon.svg")]:
        s = os.path.join(dl, src_name)
        if os.path.exists(s): shutil.copy(s, os.path.join(M, dst))

# ---------------- CSS ----------------
CSS = """
:root{--carbon:#0B0F14;--carbon2:#0E141B;--slate:#161F29;--slate2:#1B2630;--line:#243341;
--ink:#E8EDF2;--mut:#9CABB8;--mut2:#6F7E8B;--platinum:#C9D0D9;--accent:#C9D0D9;--accent-bright:#E8EDF2;--accent-deep:#9CABB8;}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--carbon);color:var(--ink);font-family:'IBM Plex Sans',system-ui,Arial,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.mono{font-family:'IBM Plex Mono',ui-monospace,monospace}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px}
.kick{font-size:12px;font-weight:600;letter-spacing:2.4px;text-transform:uppercase;color:var(--accent-deep)}
h1,h2,h3{line-height:1.1;font-weight:700;letter-spacing:-.02em}
h1{font-size:clamp(2.1rem,5vw,3.6rem)}
h2{font-size:clamp(1.5rem,3vw,2.3rem)}
p.lead{font-size:clamp(1.05rem,1.6vw,1.3rem);color:var(--mut)}
section{padding:72px 0}
.muted{color:var(--mut)}
/* header */
header.nav{position:sticky;top:0;z-index:50;background:rgba(11,15,20,.9);backdrop-filter:blur(14px) saturate(1.1);border-bottom:1px solid var(--line)}
.nav .wrap{display:flex;align-items:center;gap:28px;height:68px}
.brandlogo{display:flex;align-items:center;gap:11px;font-weight:700;font-size:1.12rem;letter-spacing:-.01em}
.brandlogo svg{width:30px;height:34px}
.navlinks{display:flex;align-items:center;gap:24px;margin-left:auto}
.navlinks a:not(.btn){font-size:.95rem;color:var(--platinum);font-weight:500;transition:color .15s}
.navlinks a:not(.btn):hover,.navlinks a:not(.btn).active{color:var(--ink)}
.dropdown{position:relative}
.dropdown>a::after{content:'▾';font-size:.7em;margin-left:5px;color:var(--mut2)}
.menu{position:absolute;top:130%;left:50%;transform:translateX(-50%) translateY(6px);background:var(--slate);border:1px solid var(--line);border-radius:12px;padding:8px;min-width:230px;opacity:0;visibility:hidden;transition:.16s;box-shadow:0 18px 40px rgba(0,0,0,.4)}
.dropdown:hover .menu{opacity:1;visibility:visible;transform:translateX(-50%) translateY(0)}
.menu a{display:flex;align-items:center;gap:10px;padding:9px 11px;border-radius:8px;color:var(--ink);font-size:.92rem}
.menu a:hover{background:var(--slate2)}
.menu a svg{width:20px;height:22px;flex:0 0 20px}
.menu .dom{color:var(--mut2);font-size:.78rem}
.btn{display:inline-flex;align-items:center;gap:8px;padding:11px 20px;border-radius:10px;font-weight:600;font-size:.95rem;transition:.15s;cursor:pointer;border:1px solid transparent}
.btn-primary{background:var(--accent);color:#0B0F14;font-weight:700;box-shadow:0 2px 14px rgba(0,0,0,.25)}
.btn-primary:hover{filter:brightness(1.06)}
.btn-ghost{border-color:var(--line);color:var(--ink)}
.btn-ghost:hover{border-color:var(--accent);color:var(--accent-bright)}
.navtoggle{display:none;margin-left:auto;background:none;border:1px solid var(--line);border-radius:8px;color:var(--ink);font-size:1.3rem;width:42px;height:38px}
/* hero */
.hero{padding:96px 0 64px;position:relative;overflow:hidden}
.hero .eyebrow{margin-bottom:18px}
.hero h1{max-width:16ch;margin:.2em 0 .35em}
.hero p.lead{max-width:60ch}
.hero .cta{margin-top:34px;display:flex;gap:14px;flex-wrap:wrap}
.heromark{position:absolute;right:4%;top:50%;transform:translateY(-50%);width:360px;max-width:32vw;opacity:.08;pointer-events:none}
.heromark svg{width:100%;display:block}
/* brand-architecture diagram */
.archd{--tick:var(--line);width:100%}
.archd .arch-master{display:flex;justify-content:center}
.archd .an-master{text-align:center;border:1px solid var(--line);border-radius:14px;background:linear-gradient(180deg,var(--slate),var(--carbon2));padding:18px 26px;min-width:240px}
.archd .an-master .an-mark{width:30px;height:34px;vertical-align:middle;margin-right:9px}
.archd .an-master .an-name{display:inline-block;font-weight:700;font-size:1.18rem;letter-spacing:-.01em;color:var(--ink);vertical-align:middle}
.archd .arch-stem{height:22px;width:2px;background:var(--tick);margin:0 auto}
.archd .arch-bus{height:2px;background:var(--tick);margin:0 auto;width:min(80%,640px)}
.archd .arch-row{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:0}
.archd .arch-node{position:relative;flex:1 1 150px;max-width:210px;margin-top:22px;background:var(--carbon2);border:1px solid var(--line);border-top:3px solid var(--c);border-radius:12px;padding:16px 16px 18px;text-align:center}
.archd .arch-node::before{content:"";position:absolute;top:-22px;left:50%;transform:translateX(-50%);width:2px;height:22px;background:var(--tick)}
.archd .arch-node .an-name{font-weight:700;font-size:1rem;color:var(--ink);line-height:1.25}
.archd .arch-node .an-kick{font-size:.72rem;font-weight:600;letter-spacing:.6px;text-transform:uppercase;color:var(--c);margin-top:7px;line-height:1.3}
.archd .arch-node .an-desc{font-size:.82rem;color:var(--mut);margin-top:9px;line-height:1.45}
.archd .an-hl{box-shadow:0 0 0 1px var(--c),0 14px 30px rgba(0,0,0,.35);background:var(--slate)}
.archd .an-sister{border-style:dashed;opacity:.96}
.archd .an-sister::before{background-image:linear-gradient(var(--tick) 50%,transparent 0);background-size:2px 6px;background-color:transparent}
.archd .an-tag{display:inline-block;font-size:.62rem;font-weight:700;letter-spacing:.8px;text-transform:uppercase;color:var(--mut2);border:1px solid var(--line);border-radius:6px;padding:2px 7px;margin-bottom:9px}
.archd .arch-cap{text-align:center;color:var(--mut2);font-size:.82rem;margin-top:20px}
@media(max-width:680px){.archd .arch-bus{display:none}.archd .arch-node{flex-basis:100%;max-width:none}.archd .arch-node::before{display:none}.archd .arch-stem{height:14px}.archd .arch-row{gap:12px}}
/* future-directions frontiers */
.frontier{margin-top:34px}
.frontier:first-of-type{margin-top:6px}
.frontier-head{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;border-left:3px solid var(--accent);padding-left:14px;margin-bottom:18px}
.frontier-head h3{font-size:1.18rem}
.frontier-head p{font-size:.92rem;margin:0}
.xtag{display:inline-block;font-size:.58rem;font-weight:700;letter-spacing:.7px;text-transform:uppercase;color:var(--accent-bright);border:1px solid var(--accent-deep);border-radius:5px;padding:1px 6px;vertical-align:middle;margin-left:7px}
/* grids & cards */
.grid{display:grid;gap:20px}
.g3{grid-template-columns:repeat(3,1fr)}.g2{grid-template-columns:repeat(2,1fr)}.g4{grid-template-columns:repeat(4,1fr)}
.card{background:var(--slate);border:1px solid var(--line);border-radius:16px;padding:26px;transition:.18s}
.card:hover{border-color:var(--accent);transform:translateY(-3px)}
.brandcard{display:block;position:relative;overflow:hidden}
.brandcard .top{height:4px;background:var(--ba);border-radius:16px 16px 0 0;position:absolute;top:0;left:0;right:0}
.brandcard svg{width:54px;height:60px;margin-bottom:16px}
.brandcard h3{font-size:1.25rem}
.brandcard .dom{font-size:.78rem;letter-spacing:1.5px;text-transform:uppercase;color:var(--bd);font-weight:600;margin:4px 0 10px}
.brandcard p{color:var(--mut);font-size:.95rem}
.brandcard .more{margin-top:14px;color:var(--bb);font-weight:600;font-size:.9rem}
.statrow{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:8px}
.stat .n{font-size:clamp(1.7rem,3vw,2.4rem);font-weight:700;color:var(--accent-deep)}
.stat .l{font-size:.85rem;color:var(--mut)}
.cap{padding:22px;background:var(--carbon2);border:1px solid var(--line);border-radius:14px}
.cap h4{font-size:1.05rem;margin-bottom:7px}
.cap p{color:var(--mut);font-size:.92rem}
.cap .dot{width:34px;height:34px;border-radius:9px;background:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:13px;color:#0B0F14;font-weight:700;font-family:'IBM Plex Mono'}
.band{background:linear-gradient(180deg,var(--carbon2),var(--carbon))}
.split{display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center}
.feature-img{border:1px solid var(--line);border-radius:16px;width:100%}
.tag{display:inline-block;padding:5px 12px;border:1px solid var(--line);border-radius:999px;font-size:.82rem;color:var(--mut);margin:0 6px 8px 0}
.sec-head{max-width:62ch;margin-bottom:36px}
.sec-head h2{margin:.3em 0}
/* sister */
.sister{border:1px solid var(--line);border-radius:18px;padding:34px;display:flex;gap:26px;align-items:center;background:var(--slate)}
.sister svg,.sister .sister-ico{width:64px;height:64px;flex:0 0 64px;border-radius:14px}
.sig-logo{height:60px;width:auto;margin-bottom:20px;display:block}
.vp{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:8px}
.vp div{background:var(--carbon2);border:1px solid var(--line);border-radius:12px;padding:16px 18px;font-weight:600}
.vp .mono{color:var(--accent);font-size:.8rem;display:block;margin-bottom:4px}
.tier{display:flex;flex-direction:column}
.tier .price{font-family:'IBM Plex Mono';font-size:1.1rem;color:var(--accent);margin:.2em 0 .6em}
.tier .sub{color:var(--mut2);font-size:.82rem;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px}
.tier ul{list-style:none;margin-top:6px}.tier li{color:var(--mut);font-size:.9rem;padding-left:16px;position:relative;margin-bottom:6px}
.tier li:before{content:'›';position:absolute;left:0;color:var(--accent)}
.tags-row{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}
.aud{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:8px}
.aud div{padding-left:24px;position:relative;color:var(--mut)}
.aud div:before{content:'▹';position:absolute;left:0;color:var(--accent);font-weight:700}
.statusbox{border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:12px;padding:18px 22px;color:var(--mut);font-size:.95rem;background:var(--carbon2);margin-top:8px}
.statusbox strong{color:var(--ink)}
.relbox{border:1px dashed var(--line);border-radius:12px;padding:16px 20px;margin-top:18px;color:var(--mut);font-size:.92rem}
@media(max-width:860px){.aud{grid-template-columns:1fr}}
.ico{width:100%;height:100%;display:block}
.menu.wide{min-width:560px;display:grid;grid-template-columns:1fr 1fr;gap:2px}
.menu .mi{width:22px;height:22px;flex:0 0 22px;display:inline-flex}
.menu .mi-img{width:22px;height:22px;flex:0 0 22px;border-radius:6px}
.iconbox{display:inline-flex;color:var(--accent)}
.iconbox.sm{width:42px;height:42px}.iconbox.lg{width:58px;height:58px}
.modcard{display:block;border:1px solid var(--line);border-radius:16px;padding:24px;background:var(--slate);transition:.18s}
.modcard:hover{border-color:var(--accent);transform:translateY(-3px)}
.modcard .iconbox{width:40px;height:40px;color:var(--accent);margin-bottom:14px}
.modcard h3{font-size:1.12rem}
.modcard .dom{font-size:.74rem;letter-spacing:1.2px;text-transform:uppercase;color:var(--accent-deep);font-weight:600;margin:3px 0 9px}
.modcard p{color:var(--mut);font-size:.92rem}
.compline{display:flex;gap:16px;align-items:flex-start;padding:16px 0;border-bottom:1px solid var(--line)}
.compline .iconbox{width:34px;height:34px;flex:0 0 34px;color:var(--accent);margin-top:2px}
.compline b{color:var(--ink)}.compline span{color:var(--mut);font-size:.92rem}
.layer{display:flex;gap:18px;align-items:flex-start;padding:16px 18px;border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:12px;background:var(--carbon2);margin-bottom:12px}
.layer .ln{font-family:'IBM Plex Mono';color:var(--accent);font-weight:600;flex:0 0 150px}
.layer p{color:var(--mut);font-size:.93rem}
.thesis{font-size:clamp(1.4rem,3vw,2rem);font-weight:700;letter-spacing:-.02em;line-height:1.25}
.thesis em{color:var(--accent);font-style:normal}
.social{display:flex;gap:10px;margin-top:18px}
.social a{width:36px;height:36px;border:1px solid var(--line);border-radius:9px;display:inline-flex;align-items:center;justify-content:center;color:var(--mut);transition:.15s}
.social a:hover{color:var(--ink);border-color:var(--accent);transform:translateY(-2px)}
.social svg{width:18px;height:18px}
/* posts */
.post{border-bottom:1px solid var(--line);padding:26px 0;display:block}
.post:hover h3{color:var(--accent-bright)}
.post .meta{font-size:.82rem;color:var(--mut2);margin-bottom:6px}
.article{max-width:720px;margin:0 auto}
.article p{margin:1em 0;color:var(--mut)}
/* form */
.field{display:flex;flex-direction:column;gap:6px;margin-bottom:16px}
.field label{font-size:.85rem;color:var(--mut)}
.field input,.field textarea{background:var(--carbon2);border:1px solid var(--line);border-radius:10px;padding:12px;color:var(--ink);font-family:inherit;font-size:.95rem}
.field input:focus,.field textarea:focus{outline:none;border-color:var(--accent)}
/* footer */
footer{border-top:1px solid var(--line);background:var(--carbon2);padding:56px 0 30px}
.fgrid{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:32px}
footer h5{font-size:.78rem;letter-spacing:1.5px;text-transform:uppercase;color:var(--mut2);margin-bottom:14px}
footer ul{list-style:none}footer li{margin-bottom:9px}
footer a{color:var(--mut);font-size:.92rem}footer a:hover{color:var(--ink)}
.flogo{display:flex;align-items:center;gap:10px;font-weight:700;margin-bottom:14px}
.flogo svg{width:30px;height:34px}
.legal{border-top:1px solid var(--line);margin-top:40px;padding-top:22px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;color:var(--mut2);font-size:.85rem}
.rule{height:1px;background:var(--line);border:0;margin:0}
@media(max-width:860px){
 .navlinks{display:none;position:absolute;top:68px;left:0;right:0;flex-direction:column;background:var(--slate);border-bottom:1px solid var(--line);padding:16px 24px;gap:14px;align-items:flex-start}
 .navlinks.open{display:flex}.navtoggle{display:block}
 .menu{position:static;opacity:1;visibility:visible;transform:none;box-shadow:none;border:none;background:none;padding:8px 0 0 12px;min-width:0}
 .g3,.g4,.g2,.split,.fgrid,.statrow{grid-template-columns:1fr}
 .sister{flex-direction:column;text-align:center}
 .split{gap:28px}
 .heromark{display:none}
 .navlinks a.btn{margin-top:4px}
}
"""

# ---------------- helpers ----------------
def mark(slug, cls=""): return f'<span class="m {cls}">__INCLUDE_{slug}__</span>'

def head(title, desc):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{html.escape(desc)}">
<link rel="icon" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css"></head>"""

def navbar(active=""):
    def cls(n): return ' class="active"' if n == active else ''
    pit = ""
    for k in MODULE_ORDER:
        dom, href = MODULES[k]["kicker"], f'{mslug(k)}.html'
        if k == "pades":  # PAdES ships a live in-browser signing demo — highlight it like Forge.
            dom += ' · <span style="color:var(--accent)">Live demo</span>'
            href = 'pades.html#demo'
        pit += f'<a href="{href}"><span class="mi" style="color:{PA}">{icon_svg(MODULES[k]["icon"])}</span><span>{MODULES[k]["name"]}™<br><span class="dom">{dom}</span></span></a>'
    # Shared components with their own surfaces (live demos / standalone pages) get a slot too.
    pit += f'<a href="signet-forge.html"><span class="mi" style="color:{PA}">{icon_svg("forge")}</span><span>Signet Forge™<br><span class="dom">Encrypted Parquet · Live WASM demo</span></span></a>'
    bit = "".join(f'<a href="{slug}.html"><svg>{{{slug}}}</svg><span>{DIV[slug]["name"]}™<br><span class="dom">{DIV[slug]["kicker"]}</span></span></a>' for slug in ORDER)
    bit += f'<a href="signetify.html"><img class="mi-img" src="assets/marks/signetify-icon.svg" alt=""><span>Signetify™<br><span class="dom">Sister company · signetify.com</span></span></a>'
    return f"""<header class="nav"><div class="wrap">
<a class="brandlogo" href="index.html"><svg>{{master-white}}</svg>SignetStack&nbsp;Labs</a>
<button class="navtoggle" onclick="document.getElementById('nl').classList.toggle('open')">≡</button>
<nav class="navlinks" id="nl">
<a href="company.html"{cls('company')}>Company</a>
<span class="dropdown"><a href="platform.html"{cls('platform')}>Platform</a><div class="menu wide">{pit}</div></span>
<span class="dropdown"><a href="brands.html"{cls('brands')}>Brands</a><div class="menu">{bit}</div></span>
<a href="insights.html"{cls('insights')}>Insights</a>
<a href="careers.html"{cls('careers')}>Careers</a>
<a href="contact.html" class="btn btn-primary">Get in touch</a>
</nav></div></header>"""

def footer():
    plinks = "".join(f'<li><a href="{mslug(k)}.html">{MODULES[k]["name"]}™</a></li>' for k in MODULE_ORDER[:6])
    plinks += '<li><a href="pades.html#demo">Signet PAdES™ <span style="color:var(--accent)">· demo</span></a></li>'
    plinks += '<li><a href="signet-forge.html">Signet Forge™ <span style="color:var(--accent)">· demo</span></a></li>'
    blinks = "".join(f'<li><a href="{s}.html">{DIV[s]["name"]}™</a></li>' for s in ORDER)
    return f"""<footer><div class="wrap">
<div class="fgrid">
<div><div class="flogo"><svg>{{master-white}}</svg>SignetStack Labs™</div>
<p class="muted" style="font-size:.92rem;max-width:36ch">{COMPANY['tagline']} The Signet Data Trust Network Platform, specialist brands, and Signetify, built on one proven cryptographic core.</p>
<p class="muted" style="font-size:.8rem;margin-top:12px">Registered office: {COMPANY['office']}</p>
<div class="social">{social_row()}</div></div>
<div><h5>Platform</h5><ul>{plinks}<li><a href="platform.html">All modules →</a></li></ul></div>
<div><h5>Brands</h5><ul>{blinks}<li><a href="{SIGNETIFY_URL}" target="_blank" rel="noopener">Signetify™ ↗</a></li><li><a href="brands.html">All brands →</a></li></ul></div>
<div><h5>Company</h5><ul><li><a href="company.html">About</a></li><li><a href="careers.html">Careers</a></li><li><a href="insights.html">Insights</a></li><li><a href="contact.html">Contact</a></li><li><a href="privacy.html">Privacy</a></li><li><a href="terms.html">Terms</a></li></ul></div>
</div>
<div class="legal"><span>© {COMPANY['year']} {COMPANY['legal']} · {COMPANY['reg_line']}. SignetStack Labs is a brand of {COMPANY['legal']}; Signetify is a sister company.</span><span>{COMPANY['loc']}</span></div>
</div></footer>
<script>document.querySelectorAll('.navlinks a:not(.dropdown a)').forEach(a=>a.addEventListener('click',()=>document.getElementById('nl').classList.remove('open')));</script>"""

# Client-side email assembler: decodes base64 `data-e` on <a class="eml"> into a mailto link
# (and visible text unless data-show="0"). Plain (non-f) string so JS braces are literal.
EMAIL_DECODER_JS = ("<script>document.querySelectorAll('a.eml[data-e]').forEach(function(a){"
    "try{var e=atob(a.getAttribute('data-e')),s=a.getAttribute('data-s');"
    "a.href='mailto:'+e+(s?'?subject='+encodeURIComponent(s):'');"
    "if(a.getAttribute('data-show')!=='0')a.textContent=e;}catch(x){}});</script>")

def page(fname, title, desc, body, active="", accentvars=None):
    style = ""
    if accentvars:
        a, b, dp = accentvars
        style = f'<style>body{{--accent:{a};--accent-bright:{b};--accent-deep:{dp}}}</style>'
    out = head(title, desc) + style + "<body>" + navbar(active) + body + footer() + EMAIL_DECODER_JS + "</body></html>"
    # inline marks: replace <svg ...>{key}</svg> -> <svg ...viewBox=..>INNER</svg> (preserve any attrs)
    for m in os.listdir(os.path.join(A, "marks")):
        k = m[:-4]; v = open(os.path.join(A, "marks", m)).read()
        inner = v.split(">", 1)[1].rsplit("</svg>", 1)[0]
        vb = "0 0 120 134" if "134" in v else "0 0 120 120"
        out = re.sub(r'<svg([^>]*)>\{' + re.escape(k) + r'\}</svg>',
                     lambda mm: f'<svg{mm.group(1)} viewBox="{vb}">{inner}</svg>', out)
    # canonical URL (extensionless) for this page
    slug = fname[:-5]
    canon = "https://signetstack.io/" + ("" if slug == "index" else slug)
    og_img = "https://signetstack.io/assets/img/og-card.png"
    et, ed = html.escape(title, quote=True), html.escape(desc, quote=True)
    head_extra = (
        f'<link rel="canonical" href="{canon}">'
        f'<meta property="og:type" content="website">'
        f'<meta property="og:site_name" content="SignetStack Labs">'
        f'<meta property="og:url" content="{canon}">'
        f'<meta property="og:title" content="{et}">'
        f'<meta property="og:description" content="{ed}">'
        f'<meta property="og:image" content="{og_img}">'
        f'<meta property="og:image:secure_url" content="{og_img}">'
        f'<meta property="og:image:type" content="image/png">'
        f'<meta property="og:image:width" content="1200">'
        f'<meta property="og:image:height" content="630">'
        f'<meta property="og:image:alt" content="SignetStack Labs">'
        f'<meta name="twitter:card" content="summary_large_image">'
        f'<meta name="twitter:title" content="{et}">'
        f'<meta name="twitter:description" content="{ed}">'
        f'<meta name="twitter:image" content="{og_img}">'
    )
    out = out.replace("</head>", head_extra + "</head>", 1)
    # clean URLs: drop .html from internal page links (files stay flat; Pages serves /company -> company.html).
    # Skips external links (have ://), assets (.css/.svg/.png/.js), mailto, and anchors with a path slash.
    out = re.sub(r'href="index\.html(#[^"]*)?"', lambda m: f'href="/{m.group(1) or ""}"', out)
    out = re.sub(r'href="([a-z0-9][a-z0-9-]*)\.html(#[^"]*)?"', r'href="\1\2"', out)
    with open(os.path.join(SITE, fname), "w") as f:
        f.write(out)

def divvars(slug): return (DIV[slug]["accent"], DIV[slug]["bright"], DIV[slug]["deep"])

def brand_card(slug):
    d = DIV[slug]
    return f"""<a class="brandcard card" href="{slug}.html" style="--bd:{d['deep']};--bb:{d['bright']};--ba:{d['accent']}">
<span class="top"></span><svg>{{{slug}}}</svg>
<h3>{d['name']}™</h3><div class="dom">{d['kicker']}</div>
<p>{d['tagline']}</p><div class="more">Explore {d['domain']} →</div></a>"""

def arch_diagram(highlight=None):
    """Responsive CSS house-of-brands diagram (replaces the legacy PNG poster)."""
    def node(name, kick, desc, color, slug=None, sister=False, independent=False):
        hl = " an-hl" if slug and slug == highlight else ""
        sis = " an-sister" if (sister or independent) else ""
        tag = ('<span class="an-tag">Sister company</span>' if sister
               else '<span class="an-tag">Independent venture</span>' if independent else "")
        return (f'<div class="arch-node{sis}{hl}" style="--c:{color}">{tag}'
                f'<div class="an-name">{name}</div><div class="an-kick">{kick}</div>'
                f'<div class="an-desc">{desc}</div></div>')
    children = (
        node(PLATFORM['short'], "The platform", "Post-quantum data-trust platform &amp; its modules.", PA, slug="platform")
        + node("SignetStack DXP™", DIV['dxp']['kicker'], "Composable, agent-first experience platform.", DIV['dxp']['accent'], slug="dxp")
        + node("SignetStack R&amp;D™", DIV['research']['kicker'], "Cryptography research, invented &amp; proven here.", DIV['research']['accent'], slug="research")
        + node("Velocity Quant Technologies™", DIV['velocity']['kicker'], "Microsecond execution, HFT V5 Omni. Separately owned.", DIV['velocity']['accent'], slug="velocity", independent=True)
        + node(f"{SISTER['name']}™", "No-code · signetify.com", SISTER['tagline'], SISTER['accent'], sister=True)
    )
    sub = "color:var(--mut2);font-size:.72rem;font-weight:600;letter-spacing:.6px;text-transform:uppercase;margin-top:8px"
    return (f'<div class="archd"><div class="arch-master"><div class="an-master">'
            f'<svg class="an-mark">{{master-white}}</svg><span class="an-name">SignetStack&nbsp;Labs™</span>'
            f'<div style="{sub}">Master brand · one proven core</div></div></div>'
            f'<div class="arch-stem"></div><div class="arch-bus"></div>'
            f'<div class="arch-row">{children}</div>'
            f'<div class="arch-cap">One neutral master brand: the Signet Data Trust Network Platform and its specialist brands on one post-quantum core, alongside sister company Signetify and the independent venture Velocity Quant Technologies.</div></div>')

# ---------------- PAGES ----------------
def build():
    write_marks()

    modcard = lambda k: f'<a class="modcard" href="{mslug(k)}.html"><span class="iconbox" style="color:{PA}">{icon_svg(MODULES[k]["icon"])}</span><h3>{MODULES[k]["name"]}™</h3><div class="dom" style="color:{PAD}">{MODULES[k]["kicker"]}</div><p>{MODULES[k]["tagline"]}</p></a>'
    modgrid = "".join(modcard(k) for k in MODULE_ORDER)
    vstat = "".join(f'<div class="stat"><div class="n mono" style="color:{DIV["velocity"]["deep"]}">{n}</div><div class="l">{l}</div></div>' for n, l in DIV['velocity']['stats'])
    ins_cards = "".join(f'<a class="card" href="insight-{p["slug"]}.html"><div class="post meta" style="border:0;padding:0">{p["date"]} · {p["author"]}</div><h3 style="font-size:1.15rem;margin:.3em 0">{p["title"]}</h3><p class="muted" style="font-size:.95rem">{p["excerpt"]}</p></a>' for p in INSIGHTS)

    # HOME
    home = f"""
<section class="hero"><div class="heromark"><svg>{{master-white}}</svg></div><div class="wrap">
<div class="kick eyebrow">SignetStack Labs™ · a {COMPANY['legal']} company</div>
<h1>Frontier technology, built on one proven core.</h1>
<p class="lead">SignetStack Labs builds the Signet Data Trust Network Platform, a family of specialist brands, and the sister product Signetify, all on one hardened, post-quantum cryptographic core.</p>
<div class="cta"><a class="btn btn-primary" href="platform.html">Explore the platform</a><a class="btn btn-ghost" href="company.html">About the company</a></div>
</div></section>
<section class="band"><div class="wrap"><div class="sec-head"><div class="kick" style="color:{PAD}">The platform</div>
<h2 class="thesis">PKI proves who you are.<br><em>Signet proves what happened to your data.</em></h2>
<p class="lead" style="margin-top:1em">{PLATFORM['overview']}</p></div>
<div class="grid g3">{modgrid}</div>
<div class="cta" style="margin-top:26px"><a class="btn btn-primary" href="platform.html" style="--accent:{PA}">See the whole platform →</a></div></div></section>
<section><div class="wrap"><div class="sec-head"><div class="kick">The brands</div><h2>Specialist brands on the same core</h2></div>
<div class="grid g2">{''.join(brand_card(s) for s in ORDER)}</div>
<div class="sister" style="margin-top:20px"><img class="sister-ico" src="assets/marks/signetify-icon.svg" alt="Signetify"><div><div class="kick" style="color:{SISTER['accent']}">Sister company</div><h3 style="font-size:1.3rem;margin:.2em 0">{SISTER['name']}™, {SISTER['tagline']}</h3><p class="muted" style="max-width:62ch">The no-code website &amp; storefront builder, live at signetify.com.</p></div><a class="btn btn-ghost" href="signetify.html" style="margin-left:auto;--accent:{SISTER['accent']}">Learn more →</a></div>
</div></section>
<section class="band"><div class="wrap"><div class="split">
<div><div class="kick" style="color:{DIV['velocity']['deep']}">Independent venture · Velocity Quant Technologies</div>
<h2>HFT V5 Omni™</h2><p class="lead" style="margin:.5em 0 1em">A production, institutional-grade high-frequency trading engine, the fifth generation of a platform run live on real capital for eighteen months, with V5 itself in production for the last eight.</p>
<div class="statrow">{vstat}</div>
<div class="cta" style="margin-top:26px"><a class="btn btn-ghost" href="v5-omni.html">See the engine →</a></div></div>
<div>{arch_diagram(highlight="velocity")}</div>
</div></div></section>
<section><div class="wrap"><div class="sec-head"><div class="kick">Insights</div><h2>From the workshop</h2></div>
<div class="grid g3">{ins_cards}</div></div></section>
"""
    page("index.html", "SignetStack Labs: Frontier technology, one proven core", COMPANY['tagline'], home, "home")

    # COMPANY
    comp = f"""
<section class="hero"><div class="wrap"><div class="kick eyebrow">About · {COMPANY['legal']}</div>
<h1>We build frontier-technology that proves itself.</h1>
<p class="lead">{COMPANY['legal']} is the company behind SignetStack Labs, where the hardest engineering, a post-quantum cryptographic core, is built once and inherited by everything we ship.</p></div></section>
<section class="band"><div class="wrap"><div class="split">
<div><div class="kick">The model</div><h2>One core, many products</h2>
<p class="lead" style="margin-top:.6em">The expensive, precision-engineered part, cryptography, safety, provability, operational maturity, never gets rebuilt. Each product is a specialist application of the same proven foundation, the way you swap the head on a precision tool but never the motor.</p>
<p class="muted" style="margin-top:1em">The Signet Data Trust Network Platform proves what happened to regulated data; SignetStack DXP brings the same rigour to digital experience; and our sister product Signetify makes it approachable as no-code. More will follow, each on the same core. The independent venture Velocity Quant Technologies, separately owned, applies the same engineering discipline to ultra-low-latency trading.</p></div>
<div>{arch_diagram()}</div></div></div></section>
<section><div class="wrap"><div class="sec-head"><div class="kick">Principles</div><h2>How we operate</h2></div>
<div class="grid g3">
<div class="cap"><div class="dot">01</div><h4>Build the hard part once</h4><p>Shared, proven engineering, never rebuilt per market.</p></div>
<div class="cap"><div class="dot">02</div><h4>Proof, not narrative</h4><p>We replace claims with cryptographic evidence anyone can re-verify.</p></div>
<div class="cap"><div class="dot">03</div><h4>Honest by default</h4><p>We state what's proven, what's planned, and what's not done yet.</p></div>
<div class="cap"><div class="dot">04</div><h4>Post-quantum from day one</h4><p>The standards every record will need, built in now, not migrated later.</p></div>
<div class="cap"><div class="dot">05</div><h4>Govern as we grow</h4><p>Human authority is retained; automation reduces toil, not accountability.</p></div>
<div class="cap"><div class="dot">06</div><h4>Compounding by design</h4><p>Every core improvement lifts every product at once.</p></div>
</div></div></section>
<section class="band"><div class="wrap"><div class="sister"><img class="sister-ico" src="assets/marks/signetify-icon.svg" alt="Signetify">
<div><div class="kick" style="color:{SISTER['accent']}">Sister company</div><h2 style="font-size:1.5rem;margin:.2em 0">{SISTER['name']}™</h2><p class="muted" style="max-width:60ch">{SISTER['blurb']}</p></div>
<a class="btn btn-ghost" href="signetify.html" style="margin-left:auto;--accent:{SISTER['accent']}">Learn more →</a></div>
<p class="muted" style="margin-top:40px"><strong>Leadership.</strong> Our leadership and team details are published as the company grows. <a href="careers.html" style="color:var(--ink)">We're hiring →</a></p></div></section>
"""
    page("company.html", f"Company, {COMPANY['legal']}", "About Signet Stack Ltd, the Signet Data Trust Network Platform and the SignetStack Labs brands.", comp, "company")

    # PLATFORM HUB
    layers = "".join(f'<div class="layer"><div class="ln">{nm}</div><p>{ds}</p></div>' for nm, ds in PLATFORM['layers'])
    # Signet Forge has a dedicated demo page; other components are descriptive lines for now.
    comp_links = {"Signet Forge": "signet-forge.html"}
    def _compline(nm, ic, ds):
        body = f'<span class="iconbox">{icon_svg(ic)}</span><div><b>{nm}</b>, <span>{ds}</span>'
        if nm in comp_links:
            body += f' <a href="{comp_links[nm]}" style="color:{PA};white-space:nowrap">Try the demo →</a>'
        return f'<div class="compline">{body}</div></div>'
    comps = "".join(_compline(nm, ic, ds) for nm, ic, ds in COMPONENTS)
    certs = "".join(f'<span class="tag">{c}</span>' for c in PLATFORM['certs'])
    plat = f"""
<section class="hero"><div class="wrap">
<div class="iconbox lg" style="color:{PA};margin-bottom:16px">{icon_svg("platform")}</div>
<div class="kick eyebrow">{PLATFORM['short']}</div>
<h1>{PLATFORM['name']}™</h1>
<p class="thesis" style="margin:.45em 0 .55em">PKI proves who you are. <em>Signet proves what happened to your data.</em></p>
<p class="lead" style="max-width:64ch">{PLATFORM['overview']}</p>
<div class="cta"><a class="btn btn-primary" href="contact.html">Talk to us</a></div></div></section>
<section class="band"><div class="wrap"><div class="sec-head"><div class="kick">The modules</div><h2>One platform, composable modules</h2></div>
<div class="grid g3">{modgrid}</div></div></section>
<section><div class="wrap"><div class="sec-head"><div class="kick">How it fits together</div><h2>From cryptographic core to verifiable proof</h2></div>{layers}</div></section>
<section class="band"><div class="wrap"><div class="sec-head"><div class="kick">Powered by</div><h2>Shared components</h2></div>{comps}
<a class="card" href="signet-forge.html" style="display:flex;align-items:center;gap:18px;margin-top:24px;text-decoration:none;color:inherit;border-left:4px solid {PA}">
<span class="iconbox" style="color:{PA};flex-shrink:0">{icon_svg("forge")}</span>
<div style="flex:1"><div class="kick" style="color:{PA};margin-bottom:4px">Live in your browser · no upload</div>
<h3 style="font-size:1.15rem;margin:0">Signet Forge™, try the WebAssembly demo</h3>
<p class="muted" style="margin:.4em 0 0;font-size:.95rem">Drop a Parquet file, decode it client-side, optionally decrypt it with an AES-256 footer key, all without leaving your browser.</p></div>
<span style="color:{PA};font-weight:600;white-space:nowrap">Open demo →</span></a>
</div></section>
<section><div class="wrap"><div class="sec-head"><div class="kick">Certification &amp; trust</div><h2>Engineered to the standards, stated honestly</h2></div>
<div class="tags-row">{certs}</div>
<div class="statusbox" style="margin-top:20px">Engineered to FIPS 140-3 requirements, with NIST-standardized post-quantum algorithms throughout. We claim no certification we do not hold: FIPS 140-3 CMVP validation is in preparation, and SOC 2, ISO 27001, NCSC CPA and Common Criteria are in planning or on the roadmap. Every module is pre-GA; AI Governance is the most mature.</div></div></section>
<section class="band"><div class="wrap" style="text-align:center"><h2>{PLATFORM['tagline']}</h2><div class="cta" style="justify-content:center;margin-top:22px"><a class="btn btn-primary" href="contact.html">Get in touch</a></div></div></section>
"""
    page("platform.html", f"{PLATFORM['name']}: SignetStack Labs", PLATFORM['overview'][:155], plat, "platform", (PA, PAB, PAD))

    # MODULE PAGES
    for k in MODULE_ORDER:
        m = MODULES[k]
        demo_cta = '<a class="btn btn-primary" href="#demo">Try the live demo</a>' if k == "pades" else ""
        demo_sec = DEMO_PADES if k == "pades" else ""
        mcaps = "".join(f'<div class="cap"><div class="dot">{i+1:02d}</div><h4>{t}</h4><p>{p}</p></div>' for i, (t, p) in enumerate(m["caps"]))
        mtags = "".join(f'<span class="tag">{t}</span>' for t in m.get("tags", []))
        tag_sec = f'<section><div class="wrap"><div class="sec-head"><div class="kick">Standards &amp; alignment</div><h2>What it speaks</h2></div><div class="tags-row">{mtags}</div></div></section>' if m.get("tags") else ""
        mbody = f"""
<section class="hero"><div class="wrap">
<div class="iconbox lg" style="color:{PA};margin-bottom:16px">{icon_svg(m['icon'])}</div>
<div class="kick eyebrow">{m['kicker']}</div><h1>{m['name']}™</h1>
<p class="lead" style="max-width:60ch;margin-top:.4em">{m['tagline']}</p>
<div class="cta">{demo_cta}<a class="btn btn-primary" href="contact.html">Talk to us</a><a class="btn btn-ghost" href="platform.html">← The platform</a></div></div></section>
<section class="band"><div class="wrap"><div class="sec-head"><div class="kick">Overview</div><h2>{m['tagline']}</h2><p class="lead">{m['overview']}</p></div></div></section>
<section><div class="wrap"><div class="sec-head"><div class="kick">Capabilities</div><h2>What it delivers</h2></div><div class="grid g3">{mcaps}</div></div></section>
{tag_sec}
<section{' class="band"' if not m.get('tags') else ''}><div class="wrap"><div class="sec-head"><div class="kick">Status, stated honestly</div></div><div class="statusbox">{m['status']}</div>
<div class="relbox">Part of the <a href="platform.html" style="color:{PA}">Signet Data Trust Network Platform</a>, built on Signet Core and the platform's shared cryptographic foundation.</div></div></section>
{demo_sec}
<section class="band"><div class="wrap" style="text-align:center"><h2>{m['tagline']}</h2><div class="cta" style="justify-content:center;margin-top:22px"><a class="btn btn-primary" href="contact.html">Talk to us</a></div></div></section>
"""
        page(f"{mslug(k)}.html", f"{m['name']}, {m['kicker']}", m["overview"][:150], mbody, "platform", (PA, PAB, PAD))

    # SIGNET FORGE, live in-browser WASM demo, source: github.com/SIGNETSTACK/SIGNET_FORGE
    forge_demo_url = "https://signetstack.github.io/SIGNET_FORGE/demo/"
    forge_repo_url = "https://github.com/SIGNETSTACK/SIGNET_FORGE"
    forge_docs_url = "https://signetstack.github.io/SIGNET_FORGE/"
    forge_caps = [
        ("Encrypted Apache Parquet", "Modular column-level encryption (PME) layered on Apache Parquet, encrypt some columns, leave others in the clear, decrypt with the keys you control."),
        ("Post-quantum by design", "AES-256-GCM today, with a clean migration path to NIST-standardized post-quantum primitives (ML-KEM, ML-DSA), so records you write today survive the quantum era."),
        ("Reads in the browser", "A WebAssembly build runs the decrypt+decode path entirely client-side: the file never leaves the user's machine, no upload, no server, no telemetry."),
        ("Zero runtime dependencies", "C++20 core, no Apache Arrow or third-party Parquet runtime, every byte that touches your data is in this one repo, auditable end-to-end."),
        ("MiFID II &amp; EU AI Act aligned", "Footer KeyValue metadata carries signing traces, lineage tokens and policy IDs end-to-end, the file is the record of record."),
        ("Open + commercial dual-licensed", "Source-available under the Forge Source-Available License for inspection; commercial terms for production use, see the repo."),
    ]
    forge_tests = [
        ("Encrypt your own CSV, in your browser", "Drag a <code>.csv</code> onto the demo. A panel opens, generates a fresh AES-256 key for you (via <code>crypto.getRandomValues</code>), takes an AAD prefix, and the <strong>Encrypt &amp; download .parquet</strong> button writes an encrypted Parquet straight back to your machine. A one-click <em>Decrypt it here to verify</em> button then re-feeds it through the decryption path with the same key + AAD pre-filled, closing the round trip without leaving the page.", "Open the in-browser flow →", forge_demo_url),
        ("Decrypt an AES-256 PME file", "Already have an encrypted Parquet? Tick <em>Encrypted file (AES-256 PME)</em>, paste a footer key (64 hex chars) and optional column key, then drop the file. From there: <strong>Download .parquet</strong> saves the original bytes (encrypted files stay encrypted, safe to forward), and <strong>Download CSV</strong> / <strong>Download JSON</strong> export the decrypted rows. All client-side, no network round-trip.", "Open the encrypted-file flow →", forge_demo_url),
        ("Open the bundled sample, or bring any .parquet", "One drop loads the bundled <code>sample.parquet</code> from the demo, or any Parquet from your machine, schema, row groups and a paged preview render in under a second; nothing leaves your browser.", "Open the demo →", forge_demo_url),
    ]
    # Precautions surfaced before encryption, strong-encryption tools delete data
    # safely on purpose. Users need to know what they own (the key) and what the
    # system will not recover for them (anything once the key is gone).
    forge_precautions = [
        ("Generate keys with a CSPRNG, not by hand",
         "Use <code>openssl rand -hex 32</code> (or your platform's equivalent) for every file. Hand-typed or guessable keys collapse AES-256 to whatever your imagination is, usually a few bits of real entropy."),
        ("Save the key before you close the terminal",
         "When you run <code>KEY=$(openssl rand -hex 32)</code>, that 64-character hex string only exists in your shell's environment. Close the tab without copying it into a password manager (1Password, Bitwarden, <code>pass</code>) and the file becomes permanently unreadable. <strong>That is by design, it is the crypto-shred guarantee, not a bug.</strong>"),
        ("The AAD prefix must match, character for character",
         "If you encrypted with <code>--aad-prefix \"mydata-2026-05-31\"</code>, you must type that <em>exact</em> string into the demo's AAD field. A capital letter, a missing dash, an extra space, any difference makes the GCM tag fail to verify, and there is no recovery path."),
        ("Use a trusted device",
         "The demo keeps your file in the browser, no upload, no server, no telemetry, but the device itself still sees the plaintext after decryption. Don't use shared kiosks, active screen-sharing sessions, or machines with cross-device clipboard sync turned on while you paste keys."),
        ("Never share keys over email, chat or SMS",
         "Treat an AES-256 key the way you'd treat a password: send it through a password-manager share, a Signal / age / GPG-encrypted channel, or a vault, never inline in a message that gets logged, indexed or back-up-synced in plaintext."),
        ("Public demo is for evaluation; production wants the local build",
         "The hosted demo loads its JS and WebAssembly from this site for convenience. For regulated PII / financial / health data, build the CLI or library locally with <code>-DSIGNET_ENABLE_COMMERCIAL=ON</code> so the entire compile, key-handling and storage surface stays inside your trust boundary."),
        ("Downloading an encrypted .parquet is just sharing the ciphertext",
         "The <strong>Download .parquet</strong> button is a passthrough, it writes the exact bytes you uploaded. An encrypted file <em>stays</em> encrypted on disk and is safe to email, attach or upload to shared storage. But sharing the file does <em>not</em> share the key, the recipient still needs the footer key, optional column key, and the same AAD prefix to decrypt. Send those separately, through a different channel."),
        ("Report vulnerabilities responsibly",
         f'Found a real cryptographic or implementation issue? Use the coordinated-disclosure path in <a href="{forge_repo_url}/blob/main/SECURITY.md" target="_blank" rel="noopener">SECURITY.md</a> on the Forge repository, please don\'t open a public issue.'),
    ]
    # CLI workflow surfaced as a concrete recipe, every line tested locally,
    # round-trip verified into the demo.
    forge_cli_steps = [
        ("Build the CLI (one time)",
         "<pre><code>cd /path/to/SIGNET_FORGE\ncmake --preset release -DSIGNET_ENABLE_COMMERCIAL=ON\ncmake --build --preset release --target signet_cli\n# binary at build/signet_cli</code></pre>"),
        ("Generate a fresh AES-256 key",
         "<pre><code>KEY=$(openssl rand -hex 32)\necho $KEY     # SAVE THIS to a password manager NOW</code></pre>"),
        ("Convert + encrypt your CSV in one shot",
         "<pre><code>./build/signet_cli convert mydata.csv mydata.parquet \\\n    --encrypt \\\n    --footer-key  $KEY \\\n    --column-key  $KEY \\\n    --aad-prefix  \"mydata-YYYY-MM-DD\"</code></pre>"),
        ("Open the file in the demo above",
         "Tick <em>Encrypted file (AES-256 PME)</em>, paste <code>$KEY</code> into both the footer and column key fields, type the exact same AAD prefix, then drop the <code>.parquet</code> file. Decryption happens entirely in your browser."),
    ]
    forge_caps_html = "".join(f'<div class="cap"><div class="dot">{i+1:02d}</div><h4>{t}</h4><p>{p}</p></div>' for i, (t, p) in enumerate(forge_caps))
    forge_tests_html = "".join(f'<div class="cap"><div class="dot">{i+1:02d}</div><h4>{t}</h4><p>{p}</p><a class="btn btn-ghost" href="{u}" target="_blank" rel="noopener" style="margin-top:12px">{lbl}</a></div>' for i, (t, p, lbl, u) in enumerate(forge_tests))
    forge_safety_html = "".join(f'<div class="cap"><div class="dot" style="background:#F59E0B;color:#fff">!</div><h4>{t}</h4><p>{p}</p></div>' for t, p in forge_precautions)
    forge_cli_html = "".join(f'<div class="cap"><div class="dot">{i+1:02d}</div><h4>{t}</h4>{p}</div>' for i, (t, p) in enumerate(forge_cli_steps))
    forge_tags = ["Apache Parquet", "AES-256-GCM (PME)", "ML-KEM · ML-DSA (roadmap)", "C++20 · zero deps", "WebAssembly", "MiFID II RTS 22", "EU AI Act"]
    forge_tags_html = "".join(f'<span class="tag">{t}</span>' for t in forge_tags)
    forge_body = f"""
<section class="hero"><div class="wrap">
<div class="iconbox lg" style="color:{PA};margin-bottom:16px">{icon_svg("forge")}</div>
<div class="kick eyebrow">Shared component · Signet Data Trust Network Platform</div>
<h1>Signet Forge™</h1>
<p class="thesis" style="margin:.45em 0 .55em">Encrypted Apache Parquet. <em>Read it in the browser. Never uploaded.</em></p>
<p class="lead" style="max-width:64ch">Signet Forge is the post-quantum-ready, encrypted-Parquet companion library to Signet Core, a C++20 engine with a WebAssembly build that decodes and decrypts Parquet entirely client-side. It powers per-column encryption across Signet Lake, signing-trace embedding for Signet AI Governance, and tamper-evident columnar audit trails for the platform.</p>
<div class="cta">
<a class="btn btn-primary" href="{forge_demo_url}" target="_blank" rel="noopener">Open the live demo ↗</a>
<a class="btn btn-ghost" href="{forge_repo_url}" target="_blank" rel="noopener">View on GitHub ↗</a>
<a class="btn btn-ghost" href="{forge_docs_url}" target="_blank" rel="noopener">API reference ↗</a>
</div></div></section>

<section class="band"><div class="wrap">
<div class="sec-head"><div class="kick">Try it now</div><h2>In your browser. No upload. No login.</h2>
<p class="lead">The demo below is the production WebAssembly build, served from the Signet Forge repository's GitHub Pages site. Your files never leave your machine, the decrypt and decode happen entirely client-side.</p></div>

<div class="card" style="border-left:4px solid #F59E0B;background:rgba(245,158,11,0.06);padding:18px 22px;margin-bottom:18px">
<div class="kick" style="color:#F59E0B;margin-bottom:6px">Heads up · key custody is yours</div>
<p style="margin:0;font-size:.95rem"><strong>Your file stays in your browser, but your AES-256 key is yours alone to manage.</strong> If you lose it, the file is unrecoverable. That is the crypto-shred guarantee, not a bug. Save the key into a password manager <em>before</em> closing the terminal you generated it in, and make sure the AAD prefix you type into the demo matches the one used at encrypt time exactly. The full safety brief is below the demo.</p>
</div>

<div class="card" style="padding:0;overflow:hidden;border-radius:14px">
<iframe src="{forge_demo_url}" title="Signet Forge: Browser Parquet Preview" loading="lazy"
        style="display:block;width:100%;height:760px;border:0;background:#1a1a2e"
        sandbox="allow-scripts allow-same-origin allow-downloads"
        referrerpolicy="no-referrer"></iframe>
</div>
<p class="muted" style="margin-top:12px;font-size:.85rem">Demo hosted at <code>{forge_demo_url}</code>. If the iframe is blocked in your environment, <a href="{forge_demo_url}" target="_blank" rel="noopener">open it in a new tab</a>.</p>
</div></section>

<section><div class="wrap"><div class="sec-head"><div class="kick">Three things to try</div><h2>Immediate test scenarios</h2><p class="lead">Concrete proofs you can run today, each one ends in your browser, with no server roundtrip.</p></div>
<div class="grid g3">{forge_tests_html}</div></div></section>

<section class="band"><div class="wrap">
<div class="sec-head"><div class="kick" style="color:#F59E0B">Before you encrypt · read this once</div><h2>Important precautions</h2>
<p class="lead">Signet Forge gives you real cryptographic guarantees. That cuts both ways: when the system says a file is unrecoverable, it really is. These are the seven things every user should know before encrypting their first file.</p></div>
<div class="grid g3">{forge_safety_html}</div></div></section>

<section><div class="wrap">
<div class="sec-head"><div class="kick">For scripted or batch use, the CLI</div><h2>Same flow, on the command line</h2>
<p class="lead">The browser demo above handles single-file, interactive use. For scripted pipelines, batch jobs, or anything you want under version control, the <code>signet_cli</code> binary gives you the same encrypted round trip on the command line.</p></div>
<div class="grid g2">{forge_cli_html}</div>
<div class="statusbox" style="margin-top:20px"><strong>Why the local build:</strong> the encryption flags depend on the commercial-tier writer surface in the library, which is off by default for CLI builds. Reconfiguring with <code>-DSIGNET_ENABLE_COMMERCIAL=ON</code> turns it on for your local build only, it does not change the licence of the repository or your obligations under it. See <a href="{forge_repo_url}/blob/main/LICENSE_COMMERCIAL" target="_blank" rel="noopener">LICENSE_COMMERCIAL</a> on the Forge repository for commercial-use terms. <em>(The hosted WebAssembly demo is already built with the commercial flag, you don't need it for the in-browser flow above.)</em></div>
</div></section>

<section class="band"><div class="wrap"><div class="sec-head"><div class="kick">What it does</div><h2>Capabilities</h2></div><div class="grid g3">{forge_caps_html}</div></div></section>

<section><div class="wrap"><div class="sec-head"><div class="kick">Standards &amp; alignment</div><h2>What it speaks</h2></div><div class="tags-row">{forge_tags_html}</div></div></section>

<section class="band"><div class="wrap"><div class="sec-head"><div class="kick">Status, stated honestly</div></div>
<div class="statusbox">Signet Forge is source-available on GitHub and ships with a Doxygen API reference and a WebAssembly demo, both built and deployed via the repository's CI. The classical encryption suite (AES-256-GCM modular Parquet encryption) is implemented and exercised today; the post-quantum migration path (ML-KEM key wrapping, ML-DSA-signed footers) is on the near-term roadmap. Commercial licensing terms are listed alongside the open source-available licence.</div>
<div class="relbox">A shared component of the <a href="platform.html" style="color:{PA}">Signet Data Trust Network Platform</a>, built on the same cryptographic foundation as Signet Core, used end-to-end by Signet Lake, AI Governance and Stream.</div></div></section>

<section class="band"><div class="wrap" style="text-align:center"><h2>Encrypted Parquet, in the browser, on a post-quantum path.</h2><div class="cta" style="justify-content:center;margin-top:22px"><a class="btn btn-primary" href="{forge_demo_url}" target="_blank" rel="noopener">Open the demo ↗</a><a class="btn btn-ghost" href="contact.html">Talk to us</a></div></div></section>
"""
    page("signet-forge.html",
         "Signet Forge: Encrypted Apache Parquet, browser-native demo",
         "Signet Forge is the post-quantum-ready encrypted-Parquet library powering the Signet Data Trust Network Platform. Try the WebAssembly demo in your browser, your files never leave your machine. Read the safety brief before you encrypt.",
         forge_body, "platform", (PA, PAB, PAD))

    # BRANDS HUB
    platcard = f'<a class="brandcard card" href="platform.html" style="--bd:{PAD};--bb:{PAB};--ba:{PA}"><span class="top"></span><span class="iconbox" style="width:54px;height:54px;color:{PA};margin-bottom:16px">{icon_svg("platform")}</span><h3>{PLATFORM["name"]}™</h3><div class="dom" style="color:{PAD}">Data Trust · Post-Quantum</div><p>{PLATFORM["tagline"]}</p><div class="more" style="color:{PAB}">Explore the platform →</div></a>'
    sigcard = f'<a class="brandcard card" href="{SIGNETIFY_URL}" target="_blank" rel="noopener" style="--bd:{SISTER["deep"]};--bb:{SISTER["bright"]};--ba:{SISTER["accent"]}"><span class="top"></span><img src="assets/marks/signetify-icon.svg" style="width:54px;height:54px;border-radius:12px;margin-bottom:16px" alt="Signetify"><h3>Signetify™</h3><div class="dom" style="color:{SISTER["accent"]}">Sister company · signetify.com</div><p>{SISTER["tagline"]}</p><div class="more" style="color:{SISTER["bright"]}">Visit signetify.com ↗</div></a>'
    hub = f"""
<section class="hero"><div class="wrap"><div class="kick eyebrow">Platform &amp; brands</div>
<h1>One core. A platform, specialist brands, and a sister company.</h1>
<p class="lead">SignetStack Labs organises its work into the Signet Data Trust Network Platform and a set of specialist brands, all on one proven, post-quantum core, and growing.</p></div></section>
<section><div class="wrap"><div class="grid g2">{platcard}{''.join(brand_card(s) for s in ORDER)}{sigcard}</div>
<div class="card" style="margin-top:20px;text-align:center;border-style:dashed"><h3 style="font-size:1.1rem">More in the pipeline</h3><p class="muted">The core is built to carry new modules and brands. <a href="contact.html" style="color:var(--ink)">Partner with us →</a></p></div>
</div></section>
"""
    page("brands.html", "Platform & Brands: SignetStack Labs", "The Signet Data Trust Network Platform and the SignetStack brands.", hub, "brands")

    # DIVISION PAGES
    for slug in ORDER:
        d = DIV[slug]
        caps = "".join(f'<div class="cap"><div class="dot">{i+1:02d}</div><h4>{t}</h4><p>{p}</p></div>' for i,(t,p) in enumerate(d["caps"]))
        statblock = ""
        if d["stats"]:
            scells = "".join(f'<div class="stat"><div class="n mono">{n}</div><div class="l">{l}</div></div>' for n, l in d["stats"])
            statblock = f'<section><div class="wrap"><div class="statrow">{scells}</div></div></section>'
        flagship = ""
        if d.get("flagship"):
            flagship = f"""<section class="band"><div class="wrap"><div class="split">
<div><div class="kick">Flagship product</div><h2>HFT V5 Omni™</h2><p class="lead" style="margin:.5em 0 1em">The engine behind Velocity, watch, decide, act and learn, inside a hard safety perimeter, live on real money for eighteen months across five generations (V5 for the last eight).</p>
<a class="btn btn-primary" href="v5-omni.html">Explore HFT V5 Omni →</a></div>
<div>{arch_diagram(highlight="velocity")}</div></div></div></section>"""
        aud = "".join(f'<div>{a}</div>' for a in d.get("audience", []))
        aud_sec = f'<section><div class="wrap"><div class="sec-head"><div class="kick">Who it\'s for</div><h2>Built for the people who carry the risk</h2></div><div class="aud">{aud}</div></div></section>' if d.get("audience") else ""
        diffs = "".join(f'<div class="cap"><div class="dot">◆</div><h4>{t}</h4><p>{p}</p></div>' for t, p in d.get("diffs", []))
        diff_sec = f'<section class="band"><div class="wrap"><div class="sec-head"><div class="kick">Why it\'s different</div><h2>Hard to replicate, by design</h2></div><div class="grid g3">{diffs}</div></div></section>' if d.get("diffs") else ""
        fr_html = ""
        for fr in d.get("frontiers", []):
            cards = ""
            for t, p, expl in fr["items"]:
                badge = ' <span class="xtag">Exploratory</span>' if expl else ''
                cards += f'<div class="cap"><div class="dot">→</div><h4>{t}{badge}</h4><p>{p}</p></div>'
            fr_html += f'<div class="frontier"><div class="frontier-head"><h3>{fr["name"]}</h3><p class="muted">{fr["tag"]}</p></div><div class="grid g3">{cards}</div></div>'
        horizon_sec = f'<section><div class="wrap"><div class="sec-head"><div class="kick">Future directions</div><h2>What the lab is inventing next</h2></div>{fr_html}</div></section>' if d.get("frontiers") else ""
        tags = "".join(f'<span class="tag">{t}</span>' for t in d.get("tags", []))
        tag_sec = f'<section><div class="wrap"><div class="sec-head"><div class="kick">Standards &amp; compliance</div><h2>What it aligns to</h2></div><div class="tags-row">{tags}</div></div></section>' if d.get("tags") else ""
        status_sec = f'<section><div class="wrap"><div class="sec-head"><div class="kick">Status, stated honestly</div></div><div class="statusbox">{d["status"]}</div></div></section>' if d.get("status") else ""
        body = f"""
<section class="hero"><div class="heromark"><svg>{{{slug}}}</svg></div><div class="wrap">
<div style="width:74px;height:82px;margin-bottom:18px"><svg style="width:74px;height:82px">{{{slug}}}</svg></div>
<div class="kick eyebrow">{d['kicker']}</div><h1>{d['name']}™</h1>
<p class="lead" style="max-width:60ch;margin-top:.4em">{d['tagline']}</p>
<div class="cta"><a class="btn btn-primary" href="contact.html">Talk to {d['domain']}</a><a class="btn btn-ghost" href="brands.html">All brands</a></div>
</div></section>
{statblock}
<section class="band"><div class="wrap"><div class="sec-head"><div class="kick">Overview</div><h2>{d['tagline']}</h2><p class="lead">{d['overview']}</p></div></div></section>
<section><div class="wrap"><div class="sec-head"><div class="kick">Capabilities</div><h2>What {d['domain']} delivers</h2></div><div class="grid g3">{caps}</div></div></section>
{aud_sec}
{diff_sec}
{horizon_sec}
{flagship}
{tag_sec}
{status_sec}
<section class="band"><div class="wrap" style="text-align:center"><h2>{d['tagline']}</h2><div class="cta" style="justify-content:center;margin-top:22px"><a class="btn btn-primary" href="contact.html">Talk to {d['domain']}</a></div></div></section>
"""
        page(f"{slug}.html", f"{d['name']}, {d['kicker']}", d["overview"][:150], body, "brands", divvars(slug))

    # V5 OMNI PRODUCT
    v = DIV["velocity"]
    steps = [("Watch","Reads every venue at once, far faster than any human."),("Decide","Three independent layers of intelligence must all agree."),("Act","Fast execution inside a hard, automatic safety perimeter."),("Learn","Feeds every real outcome back; detects drift; retrains.")]
    omni = f"""
<section class="hero"><div class="wrap"><div class="kick eyebrow" style="color:{v['deep']}">Velocity Quant Technologies · Flagship</div>
<h1>HFT V5 Omni™</h1><p class="lead" style="max-width:62ch">A production, institutional-grade high-frequency trading engine: it watches markets in microseconds, decides with a layered intelligence stack, executes with sub-millisecond latency under a hard-wired safety framework, and learns from every outcome.</p>
<div class="cta"><a class="btn btn-primary" href="contact.html">Request a briefing</a><a class="btn btn-ghost" href="velocity.html">← Velocity Quant Technologies</a></div></div></section>
<section><div class="wrap"><div class="statrow">{''.join(f'<div class="stat"><div class="n mono">{n}</div><div class="l">{l}</div></div>' for n,l in v['stats'])}</div></div></section>
<section class="band"><div class="wrap"><div class="sec-head"><div class="kick">How it works</div><h2>Watch · Decide · Act · Learn</h2></div>
<div class="grid g4">{''.join(f'<div class="cap"><div class="dot">{i+1}</div><h4>{t}</h4><p>{p}</p></div>' for i,(t,p) in enumerate(steps))}</div></div></section>
<section><div class="wrap"><div class="sec-head"><div class="kick">Proven performance, measured, not modelled</div><h2>The engine's own work is microseconds; the milliseconds are the market's physics.</h2></div>
<div class="grid g3">
<div class="cap"><h4 class="mono" style="color:{v['deep']}">~9 µs</h4><p>Median decision latency (p99 ~63 µs), over 156k live trace records.</p></div>
<div class="cap"><h4 class="mono" style="color:{v['deep']}">~340 µs</h4><p>Order dispatch to exchange acknowledgement, on a real order.</p></div>
<div class="cap"><h4 class="mono" style="color:{v['deep']}">1,971 / 0</h4><p>Tests passing with zero failures and zero findings under four memory/threading safety tools.</p></div>
</div>
<p class="muted" style="margin-top:20px;font-size:.88rem">Figures are Velocity Quant Technologies's own measured, reproducible results (verified May 2026). Market-size and third-party figures, where referenced elsewhere, are independent estimates cited for context.</p></div></section>
<section class="band"><div class="wrap"><div class="split">
<div><div class="kick">Trust</div><h2>When something goes wrong, it stops itself</h2>
<p class="muted" style="margin-top:.7em">An 18-trigger circuit breaker, a dead-man's switch and continuous capital reconciliation halt trouble automatically. The engine never custodies client funds, capital stays in the institution's own accounts, and access can be revoked instantly. Eighteen months live with zero capital loss attributable to a software defect.</p></div>
<div><div class="kick">Roadmap</div><h2>Build once, multiply the market</h2>
<p class="muted" style="margin-top:.7em">The same proven core extends to FX, equities, commodities and indices as interchangeable plugins, extension, not rebuild. The first market pays for the core; every market after is mostly upside.</p></div>
</div></div></section>
"""
    page("v5-omni.html", "HFT V5 Omni: Velocity Quant Technologies", "The institutional-grade HFT engine behind Velocity Quant Technologies.", omni, "brands", divvars("velocity"))

    # SIGNETIFY (sister company), enriched from the Storefront product docs (public-safe)
    sig_vp = "".join(f'<div><span class="mono">{a}</span>{b}</div>' for a, b in
                     [("Build", "by voice"), ("Refine", "by hand"), ("Operate", "by agent"), ("Prove", "every byte")])
    sig_caps = [
        ("Conversational generation", "Describe your business by voice or text; Signetify streams a complete, multi-page site and storefront, section by section."),
        ("Native AI media", "Owned, end-to-end generation of imagery, with video, audio and 3D on the roadmap, not a thin wrapper over someone else's API."),
        ("Pixel-perfect editing", "Refine an AI build, or design from scratch, with full WYSIWYG control and live desktop / tablet / mobile preview."),
        ("Agentic commerce", "Authorise an AI agent to build and run your store, catalog, pricing, merchandising, support, with you in control and every action logged and reversible."),
        ("Co-creation OS", "You and an agent drive the same controls behind the same guardrails, producing the same audit trail, agents can do anything you can, and nothing you can't."),
        ("Provenance & verification", "Every asset carries cryptographic provenance from the moment it's created; tiered verification proves authenticity, up to court-admissible reports."),
        ("Creator marketplace", "Buy and sell provenance-locked templates, themes and media, with lineage-aware royalties paid automatically to original creators."),
        ("Built-in commerce", "Catalog, cart, checkout and orders out of the box, card data is handled by Stripe and never touches Signetify servers."),
        ("Real-time collaboration", "Sub-second live presence for teams editing many pages at once, with instant human override of any agent action."),
    ]
    sig_caps_html = "".join(f'<div class="cap"><div class="dot">{i+1:02d}</div><h4>{t}</h4><p>{p}</p></div>' for i, (t, p) in enumerate(sig_caps))
    sig_modes = [("Cinema", "Prompt-to-website, the fastest way to get a real, multi-page site live."),
                 ("Factory", "Production at scale, assemble multi-page builds, apply brand kits across pages, and publish to the marketplace."),
                 ("Edit", "Pixel-perfect refinement or design from scratch, full WYSIWYG, multi-viewport, by voice, click or text."),
                 ("Developer", "Code-level control and full web-application development on top of the platform.")]
    sig_modes_html = "".join(f'<div class="cap"><h4>{t}</h4><p>{p}</p></div>' for t, p in sig_modes)
    sig_tiers = [
        ("Free", "Get started", "", ["Prompt-to-website (Cinema)", "Marketplace browsing", "Basic provenance verification", "Subdomain hosting"]),
        ("Premium", "For serious creators", "from ~$29/mo", ["Factory + Edit modes", "Multi-page sites & custom domains", "Native image generation", "Clean, un-badged exports", "Publish to the marketplace + royalties"]),
        ("Enterprise", "For organisations", "Custom", ["Developer Mode & full analytics", "Team management", "Multi-jurisdiction compliance reports", "Signet Verify B2B API", "Dedicated support"]),
        ("Education", "Students & non-profits", "Subsidised", ["Premium-grade capabilities", "For verified students & NGOs"]),
    ]
    tparts = []
    for name, sub, price, items in sig_tiers:
        lis = "".join(f"<li>{x}</li>" for x in items)
        pr = f'<div class="price">{price}</div>' if price else '<div class="price">Free</div>'
        tparts.append(f'<div class="card tier"><h3 style="font-size:1.2rem">{name}</h3><div class="sub">{sub}</div>{pr}<ul>{lis}</ul></div>')
    sig_tiers_html = "".join(tparts)
    sig_tags = ["GDPR", "UK DPA 2018", "EU AI Act (in-scope)", "CCPA / CPRA", "PCI-DSS via Stripe", "Post-quantum-safe provenance", "WCAG 2.2 AA (targeted)", "Pursuing enterprise certifications"]
    sig_tags_html = "".join(f'<span class="tag">{t}</span>' for t in sig_tags)
    sg = f"""
<section class="hero"><div class="wrap">
<img class="sig-logo" src="assets/marks/signetify-logo.svg" alt="Signetify">
<div class="kick eyebrow">Sister company · the Signet Stack family</div>
<h1>The trust layer for the agentic web.</h1>
<p class="lead" style="max-width:62ch">{SISTER['blurb'].replace("Signetify","Signetify™",1)}</p>
<div class="vp">{sig_vp}</div>
<div class="cta" style="margin-top:30px"><a class="btn btn-primary" href="{SIGNETIFY_URL}" target="_blank" rel="noopener">Visit signetify.com →</a><a class="btn btn-ghost" href="contact.html">Get in touch</a></div>
<p class="muted" style="margin-top:18px;font-size:.92rem">The no-code website &amp; storefront builder is live at <a href="{SIGNETIFY_URL}" target="_blank" rel="noopener" style="color:var(--accent)">signetify.com</a>. For the enterprise platform underneath it, see <a href="dxp.html" style="color:var(--accent)">SignetStack DXP</a>.</p>
</div></section>
<section class="band"><div class="wrap"><div class="sec-head"><div class="kick">What it is</div>
<h2>Build by voice. Refine by hand. Operate by agent.</h2>
<p class="lead">Signetify is an AI-native platform for building, running and growing online businesses, where a human and an AI agent are equal collaborators on the same live site. Describe what you want and Signetify generates a complete commerce experience, copy, design, imagery and storefront, that you can refine pixel-by-pixel or hand to an agent to operate end to end. What makes it different is trust: every asset and every transaction carries built-in, verifiable provenance, so a store is regulator-ready from its first sale.</p></div></div></section>
<section><div class="wrap"><div class="sec-head"><div class="kick">Capabilities</div><h2>Far more than a website builder</h2></div>
<div class="grid g3">{sig_caps_html}</div></div></section>
<section class="band"><div class="wrap"><div class="sec-head"><div class="kick">The Modes system</div><h2>Not one editor, a set of creative intelligences</h2><p class="lead">Modes grow with you, from a single prompt to a full application.</p></div>
<div class="grid g4">{sig_modes_html}</div></div></section>
<section><div class="wrap"><div class="split">
<div><div class="kick">Trust by construction</div><h2>Every byte you serve carries proof</h2>
<p class="muted" style="margin-top:.7em">Every asset and transaction is provenanced from the moment it's created, the Signetify Signature, so you can prove what was made, who approved it, and that it hasn't been altered. Tiered verification scales from a quick authenticity check to a court-admissible report. <strong>Signet Verify</strong> extends this as a B2B capability that can prove whether content came from Signetify and detect AI-generated content from elsewhere.</p></div>
<div><div class="kick">Honesty, by design</div><h2>True · Real · Reversible · Visible</h2>
<p class="muted" style="margin-top:.7em">A hard architectural rule, not a marketing line: no dark patterns, no fake urgency, no fake scarcity, no nudges you can't undo. The platform that knows the most about a buyer is the one most disciplined about never exploiting it.</p></div>
</div></div></section>
<section class="band"><div class="wrap"><div class="sec-head"><div class="kick">Plans</div><h2>From a first prompt to enterprise scale</h2></div>
<div class="grid g4">{sig_tiers_html}</div>
<p class="muted" style="font-size:.85rem;margin-top:16px">Indicative pricing, see Signetify for current plans. Add-ons (advanced analytics, verification packs, on-prem deployment) are available across tiers.</p></div></section>
<section><div class="wrap"><div class="sec-head"><div class="kick">Trust &amp; compliance</div><h2>Regulator-ready by default</h2>
<p class="lead">Storefronts ship with exportable, signed audit trails from day one.</p></div>
<div class="tags-row">{sig_tags_html}</div></div></section>
<section class="band"><div class="wrap" style="text-align:center">
<h2>A store in minutes, regulator-ready from the first sale.</h2>
<div class="cta" style="justify-content:center;margin-top:24px"><a class="btn btn-primary" href="{SIGNETIFY_URL}" target="_blank" rel="noopener">Visit signetify.com →</a><a class="btn btn-ghost" href="contact.html">Get in touch</a></div></div></section>
"""
    page("signetify.html", "Signetify, the trust layer for the agentic web", SISTER['blurb'], sg, "", (SISTER['accent'], SISTER['bright'], SISTER['deep']))

    # INSIGHTS
    idx = f"""<section class="hero"><div class="wrap"><div class="kick eyebrow">Insights</div><h1>From the workshop</h1><p class="lead">Notes on building frontier technology, speed, cryptography, governance and experience.</p></div></section>
<section><div class="wrap" style="max-width:820px">{''.join(f'<a class="post" href="insight-{p["slug"]}.html"><div class="meta">{p["date"]} · {p["author"]}</div><h3 style="font-size:1.35rem">{p["title"]}</h3><p class="muted" style="margin-top:.3em">{p["excerpt"]}</p></a>' for p in INSIGHTS)}</div></section>"""
    page("insights.html", "Insights: SignetStack Labs", "Articles from the SignetStack Labs team.", idx, "insights")
    for p in INSIGHTS:
        art = f"""<section class="hero"><div class="wrap article"><div class="kick eyebrow">{p['date']} · {p['author']}</div><h1 style="font-size:clamp(1.8rem,4vw,2.8rem)">{p['title']}</h1></div></section>
<section style="padding-top:0"><div class="wrap"><div class="article">{''.join(f'<p>{para}</p>' for para in p['body'])}
<hr class="rule" style="margin:32px 0"><a class="btn btn-ghost" href="insights.html">← All insights</a></div></div></section>"""
        page(f"insight-{p['slug']}.html", f"{p['title']}: SignetStack Labs", p['excerpt'], art, "insights")

    # CAREERS
    roles = "".join(f'<a class="post eml" data-e="{COMPANY["founder_email_b64"]}" data-s="Application: {title}" data-show="0" href="contact.html"><div class="meta">{team} · {loc}</div><h3 style="font-size:1.2rem">{title}</h3></a>' for title,team,loc in ROLES)
    car = f"""<section class="hero"><div class="wrap"><div class="kick eyebrow">Careers</div><h1>Build the hard part once. With us.</h1>
<p class="lead" style="max-width:60ch">We're a small, senior, remote-first team building production systems where correctness and speed both matter. If you want your work to compound across a family of brands, we should talk.</p></div></section>
<section class="band"><div class="wrap"><div class="grid g3">
<div class="cap"><div class="dot">◆</div><h4>Senior by default</h4><p>Small teams, high ownership, real production from day one.</p></div>
<div class="cap"><div class="dot">◆</div><h4>Remote-first</h4><p>Work where you do your best work; we optimise for outcomes.</p></div>
<div class="cap"><div class="dot">◆</div><h4>Craft & honesty</h4><p>We ship things we can defend, and we say what isn't done yet.</p></div>
</div></div></section>
<section><div class="wrap" style="max-width:820px"><div class="sec-head"><div class="kick">Open roles</div><h2>Where we're hiring</h2></div>{roles}
<p class="muted" style="margin-top:24px">Don't see your role? Introduce yourself to <a class="eml" data-e="{COMPANY['founder_email_b64']}" href="contact.html" style="color:var(--ink)">the founder</a>.</p></div></section>"""
    page("careers.html", "Careers: SignetStack Labs", "Join SignetStack Labs, remote-first, senior, frontier engineering.", car, "careers")

    # CONTACT
    con = f"""<section class="hero"><div class="wrap"><div class="kick eyebrow">Contact</div><h1>Let's talk.</h1>
<p class="lead" style="max-width:56ch">Whether you're an institution, a partner, a candidate or press, tell us what you're working on.</p></div></section>
<section style="padding-top:0"><div class="wrap"><div class="split" style="align-items:start">
<form onsubmit="event.preventDefault();this.querySelector('.ok').style.display='block'">
<div class="field"><label>Name</label><input required placeholder="Your name"></div>
<div class="field"><label>Email</label><input type="email" required placeholder="you@company.com"></div>
<div class="field"><label>Organisation</label><input placeholder="Company / fund / publication"></div>
<div class="field"><label>How can we help?</label><textarea rows="5" required placeholder="A few lines on what you need"></textarea></div>
<button class="btn btn-primary" type="submit">Send message</button>
<p class="ok muted" style="display:none;margin-top:14px">Thanks, this is a demo form. Email us directly at <strong>{COMPANY['email']}</strong>.</p>
</form>
<div class="card"><h3 style="font-size:1.15rem">Direct</h3>
<p class="muted" style="margin:.6em 0">General: <a href="mailto:{COMPANY['email']}" style="color:var(--ink)">{COMPANY['email']}</a></p>
<p class="muted" style="margin:.3em 0">Founder &amp; partnerships: <a class="eml" data-e="{COMPANY['founder_email_b64']}" href="contact.html" style="color:var(--ink)">contact the founder</a></p>
<p class="muted" style="margin-top:.5em">Location: {COMPANY['loc']}</p>
<p class="muted" style="margin-top:.4em">{COMPANY['legal']} · {COMPANY['reg_line']}</p>
<p class="muted" style="margin-top:.3em">Registered office: {COMPANY['office']}</p>
<hr class="rule" style="margin:18px 0"><h5 style="color:var(--mut2);font-size:.78rem;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:10px">By brand</h5>
{''.join(f'<p class="muted" style="margin:.3em 0">{DIV[s]["name"]}</p>' for s in ORDER)}
<p class="muted" style="margin:.3em 0">{SISTER['name']}, <a href="{SIGNETIFY_URL}" target="_blank" rel="noopener" style="color:var(--ink)">signetify.com</a></p>
<hr class="rule" style="margin:18px 0"><h5 style="color:var(--mut2);font-size:.78rem;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:10px">Follow</h5><div class="social">{social_row()}</div></div>
</div></div></section>"""
    page("contact.html", "Contact: SignetStack Labs", "Get in touch with SignetStack Labs.", con, "")

    # LEGAL
    legal_body = lambda t, paras: f"""<section class="hero"><div class="wrap article"><div class="kick eyebrow">Legal</div><h1>{t}</h1></div></section>
<section style="padding-top:0"><div class="wrap"><div class="article"><p class="muted"><em>Template, to be reviewed by counsel before launch.</em></p>{''.join(f'<p>{p}</p>' for p in paras)}</div></div></section>"""
    page("privacy.html", "Privacy: SignetStack Labs", "Privacy policy.", legal_body("Privacy Policy", [
        f"{COMPANY['legal']}, a company registered in England &amp; Wales (Companies House No. {COMPANY['reg']}; registered office {COMPANY['office']}), (\"we\") operates SignetStack Labs and its brands. This policy explains what personal data we collect, why, and your rights over it.",
        "We collect only what we need, for example, details you submit through our contact form, and we do not sell personal data.",
        f"To exercise any data right, contact us at {COMPANY['email']}. This is placeholder copy and should be replaced with a counsel-reviewed policy reflecting your jurisdictions (e.g. UK GDPR)."]), "")
    page("terms.html", "Terms: SignetStack Labs", "Terms of use.", legal_body("Terms of Use", [
        f"These terms govern use of websites operated by {COMPANY['legal']}, a company registered in England &amp; Wales (Companies House No. {COMPANY['reg']}; registered office {COMPANY['office']}). By using this site you agree to them.",
        "Content is provided for general information. Product capabilities, figures and roadmaps may change; nothing here is an offer or a warranty.",
        "Placeholder copy, replace with counsel-reviewed terms before launch."]), "")

    # CSS
    open(os.path.join(A, "styles.css"), "w").write(CSS)
    pages = [f for f in os.listdir(SITE) if f.endswith(".html")]
    print(f"Site built: {len(pages)} pages →", SITE)

build()
