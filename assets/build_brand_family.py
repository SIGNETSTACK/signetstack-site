#!/usr/bin/env python3
"""Signet Stack Ltd brand family — full reusable kit + LinkedIn banners per brand.
Shared hexagon signet seal + per-domain glyph; shared Carbon base + IBM Plex; distinct accent each."""
import os, math
from PIL import Image, ImageDraw, ImageFont
from make_logo_signetlabs import find_font, F, PLEX_BOLD, PLEX_MED

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLEX_MONO = find_font(["IBMPlexMono-Medium", "IBMPlexMono-Regular"], ["/System/Library/Fonts/Menlo.ttc"])

# shared palette
CARBON = (11, 15, 20, 255); LIGHT = (232, 237, 242, 255); SLATE = (27, 38, 48, 255)
MUTED = (138, 150, 162, 255); DGRAY = (90, 100, 112, 255)
def hx2rgba(h):
    h = h.lstrip("#"); return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 255)
def rgb(t): return t[:3]

BRANDS = [
    {"key": "signetstack-velocity", "name": "SignetStack Velocity", "desc": "ULTRA-LOW-LATENCY  ·  HFT",
     "accent": "#12C2C9", "bright": "#16E0D4", "deep": "#0B7C82", "glyph": "bars",
     "folder": "SignetStack_Velocity_Brand_Kit", "accent_name": "Cyan",
     "tagline": "Ultra-Low-Latency & High-Frequency Trading",
     "chip_style": "metric", "chips": [("18 mo", "live"), ("~9 µs", "decision"), ("1,971", "tests · 0 fail"), ("$0", "defect loss")]},
    {"key": "signetstack-pqc", "name": "SignetStack PQC", "desc": "POST-QUANTUM CRYPTOGRAPHY",
     "accent": "#8B5CF6", "bright": "#A78BFA", "deep": "#5B3FC0", "glyph": "lattice",
     "folder": "SignetStack_PQC_Brand_Kit", "accent_name": "Quantum Violet",
     "tagline": "Quantum-resilient cryptography & key management",
     "chip_style": "tag", "chips": ["Crypto-agile", "Lattice-based", "Quantum-resilient"]},
    {"key": "signetstack-aigov", "name": "SignetStack AI Governance", "desc": "AI GOVERNANCE & ASSURANCE",
     "accent": "#E3A52B", "bright": "#F4BE4A", "deep": "#9A6E14", "glyph": "oversight",
     "folder": "SignetStack_AI_Governance_Brand_Kit", "accent_name": "Gold",
     "tagline": "AI governance, assurance & oversight",
     "chip_style": "tag", "chips": ["Explainable", "Auditable", "Accountable"]},
    {"key": "signetstack-dxp", "name": "SignetStack DXP", "desc": "DIGITAL EXPERIENCE PLATFORM",
     "accent": "#FF5C8A", "bright": "#FF85A8", "deep": "#C53E6A", "glyph": "layers",
     "folder": "SignetStack_DXP_Brand_Kit", "accent_name": "Coral",
     "tagline": "Composable digital experience platform",
     "chip_style": "tag", "chips": ["Composable", "Personalized", "Omnichannel"]},
    {"key": "signetstack-rnd", "name": "SignetStack R&D", "desc": "RESEARCH & ADVANCED DEVELOPMENT",
     "accent": "#10B981", "bright": "#34D399", "deep": "#0A6E50", "glyph": "lattice",
     "folder": "SignetStack_RnD_Brand_Kit", "accent_name": "Emerald",
     "tagline": "Cryptography research & advanced development",
     "chip_style": "tag", "chips": ["Post-quantum", "Crypto-agile", "Proof-first"]},
]

# ---------------- MARK (hexagon seal + glyph) ----------------
def hexagon_pts(cx, cy, R):
    return [(cx + R * math.cos(math.radians(60 * i - 90)), cy + R * math.sin(math.radians(60 * i - 90))) for i in range(6)]

def draw_glyph(d, glyph, cx, cy, R, W, gcol, accent):
    if glyph == "bars":
        bw, gap = W * 0.115, W * 0.072; base = cy + R * 0.40; x0 = cx - (3 * bw + 2 * gap) / 2
        for i, hf in enumerate([0.30, 0.52, 0.78]):
            bh = R * hf; x = x0 + i * (bw + gap)
            d.rounded_rectangle([x, base - bh, x + bw, base], radius=bw * 0.32, fill=accent if i == 2 else gcol)
    elif glyph == "lattice":
        hs = R * 0.46; lw = max(2, int(W * 0.026)); nr = W * 0.052
        cor = [(cx - hs, cy - hs), (cx + hs, cy - hs), (cx + hs, cy + hs), (cx - hs, cy + hs)]
        for i in range(4): d.line([cor[i], cor[(i + 1) % 4]], fill=gcol, width=lw)
        for c in cor: d.line([(cx, cy), c], fill=gcol, width=lw)
        for c in cor: d.ellipse([c[0] - nr, c[1] - nr, c[0] + nr, c[1] + nr], fill=gcol)
        cnr = nr * 1.35; d.ellipse([cx - cnr, cy - cnr, cx + cnr, cy + cnr], fill=accent)
    elif glyph == "oversight":
        rr = R * 0.56; rw = max(2, int(W * 0.030)); lw = max(2, int(W * 0.024))
        sats = [(cx + rr * math.cos(math.radians(a)), cy + rr * math.sin(math.radians(a))) for a in (-90, 30, 150)]
        for sx, sy in sats: d.line([(cx, cy), (sx, sy)], fill=gcol, width=lw)
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=gcol, width=rw)
        sr = W * 0.052
        for sx, sy in sats: d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=gcol)
        cnr = W * 0.085; d.ellipse([cx - cnr, cy - cnr, cx + cnr, cy + cnr], fill=accent)
    elif glyph == "layers":
        wh = R * 0.64; hh = R * 0.30; lw = max(2, int(W * 0.048)); off = R * 0.42
        for i, yy in enumerate([cy - off, cy, cy + off]):
            pts = [(cx, yy - hh), (cx + wh, yy), (cx, yy + hh), (cx - wh, yy), (cx, yy - hh)]
            d.line(pts, fill=accent if i == 2 else gcol, width=lw, joint="curve")

def draw_mark(size, hex_color, glyph_color, accent, glyph, SS=4):
    W = size * SS
    img = Image.new("RGBA", (W, W), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    cx = cy = W / 2; R = W * 0.46; stroke = int(W * 0.072)
    pts = hexagon_pts(cx, cy, R)
    for i in range(6): d.line([pts[i], pts[(i + 1) % 6]], fill=hex_color, width=stroke, joint="curve")
    for p in pts: d.ellipse([p[0] - stroke / 2, p[1] - stroke / 2, p[0] + stroke / 2, p[1] + stroke / 2], fill=hex_color)
    draw_glyph(d, glyph, cx, cy, R, W, glyph_color, accent)
    return img.resize((size, size), Image.LANCZOS)

def trim(img, pad=0):
    bb = img.getbbox()
    if not bb: return img
    img = img.crop(bb)
    if pad:
        o = Image.new("RGBA", (img.width + 2 * pad, img.height + 2 * pad), (0, 0, 0, 0)); o.alpha_composite(img, (pad, pad)); return o
    return img

def rounded_bg(size, color, rf=0.0):
    w, h = size; img = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    (d.rounded_rectangle([0, 0, w - 1, h - 1], radius=int(min(w, h) * rf), fill=color) if rf > 0 else d.rectangle([0, 0, w, h], fill=color))
    return img

# ---------------- SVG ----------------
def svg_glyph(glyph, gcol, accent):
    cx, cy, R = 60, 67, 55
    if glyph == "bars":
        bw, gap = 13.5, 8.5; base = cy + R * 0.40; x0 = cx - (3 * bw + 2 * gap) / 2; s = ""
        for i, hf in enumerate([0.30, 0.52, 0.78]):
            bh = R * hf; x = x0 + i * (bw + gap)
            s += f'<rect x="{x:.1f}" y="{base-bh:.1f}" width="{bw}" height="{bh:.1f}" rx="4.3" fill="{accent if i==2 else gcol}"/>'
        return s
    if glyph == "lattice":
        hs = R * 0.46; nr = 55 * 0.052 * (120 / 120); nr = 6.0
        cor = [(cx - hs, cy - hs), (cx + hs, cy - hs), (cx + hs, cy + hs), (cx - hs, cy + hs)]
        lines = "".join(f'<line x1="{cor[i][0]:.1f}" y1="{cor[i][1]:.1f}" x2="{cor[(i+1)%4][0]:.1f}" y2="{cor[(i+1)%4][1]:.1f}"/>' for i in range(4))
        lines += "".join(f'<line x1="{cx}" y1="{cy}" x2="{c[0]:.1f}" y2="{c[1]:.1f}"/>' for c in cor)
        nodes = "".join(f'<circle cx="{c[0]:.1f}" cy="{c[1]:.1f}" r="{nr}" fill="{gcol}"/>' for c in cor)
        nodes += f'<circle cx="{cx}" cy="{cy}" r="{nr*1.35:.1f}" fill="{accent}"/>'
        return f'<g stroke="{gcol}" stroke-width="3.2">{lines}</g>{nodes}'
    if glyph == "oversight":
        rr = R * 0.56; sats = [(cx + rr * math.cos(math.radians(a)), cy + rr * math.sin(math.radians(a))) for a in (-90, 30, 150)]
        lines = "".join(f'<line x1="{cx}" y1="{cy}" x2="{s[0]:.1f}" y2="{s[1]:.1f}"/>' for s in sats)
        ring = f'<circle cx="{cx}" cy="{cy}" r="{rr:.1f}" fill="none" stroke="{gcol}" stroke-width="3.6"/>'
        nodes = "".join(f'<circle cx="{s[0]:.1f}" cy="{s[1]:.1f}" r="6" fill="{gcol}"/>' for s in sats)
        return f'<g stroke="{gcol}" stroke-width="3">{lines}</g>{ring}{nodes}<circle cx="{cx}" cy="{cy}" r="9.5" fill="{accent}"/>'
    if glyph == "layers":
        wh = R * 0.64; hh = R * 0.30; off = R * 0.42; s = ""
        for i, yy in enumerate([cy - off, cy, cy + off]):
            pts = f"{cx},{yy-hh:.1f} {cx+wh:.1f},{yy:.1f} {cx},{yy+hh:.1f} {cx-wh:.1f},{yy:.1f}"
            s += f'<polygon points="{pts}" fill="none" stroke="{accent if i==2 else gcol}" stroke-width="5.5" stroke-linejoin="round"/>'
        return s
    return ""

def svg_mark(stroke, glyph, gcol, accent):
    pts = hexagon_pts(60, 67, 55)
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 134" width="120" height="134">'
            f'<polygon points="{poly}" fill="none" stroke="{stroke}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>'
            f'{svg_glyph(glyph, gcol, accent)}</svg>')

# ---------------- LOCKUP ----------------
def build_lockup(b, text_color, desc_color, stacked=False, H=460):
    A = hx2rgba(b["accent"]); Br = hx2rgba(b["bright"])
    word = b["name"]; desc = b["desc"]
    wm = int(H * (0.66 if not stacked else 0.36)); ds = int(H * (0.135 if not stacked else 0.082))
    fb = F(PLEX_BOLD, wm); fm = F(PLEX_MED, ds)
    tmp = Image.new("RGBA", (10, 10)); td = ImageDraw.Draw(tmp)
    wb = td.textbbox((0, 0), word, font=fb); ww, wh = wb[2] - wb[0], wb[3] - wb[1]
    db = td.textbbox((0, 0), desc, font=fm); dw = db[2] - db[0]
    mk = trim(draw_mark(int(H * 1.5), A, A, Br, b["glyph"]))
    if not stacked:
        mh = int(H * 0.84); gap = int(H * 0.17)
        mk = mk.resize((int(mk.width * mh / mk.height), mh), Image.LANCZOS)
        tw = max(ww, dw); img = Image.new("RGBA", (mk.width + gap + tw + 80, H + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
        img.alpha_composite(mk, (20, (H - mk.height) // 2 + 20)); tx = 20 + mk.width + gap
        bh = wh + int(ds * 1.5); ty = (H - bh) // 2 + 20 - wb[1]
        d.text((tx, ty), word, font=fb, fill=text_color)
        d.text((tx + 4, ty + wb[3] + int(H * 0.05)), desc, font=fm, fill=desc_color)
    else:
        mh = int(H * 0.52); mk = mk.resize((int(mk.width * mh / mk.height), mh), Image.LANCZOS)
        tw = max(ww, dw, mk.width); W = tw + 120; img = Image.new("RGBA", (W, H + 60), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
        img.alpha_composite(mk, ((W - mk.width) // 2, 10)); ty = 10 + mh + int(H * 0.10)
        d.text(((W - ww) // 2 - wb[0], ty - wb[1]), word, font=fb, fill=text_color)
        d.text(((W - dw) // 2 - db[0], ty + wh + int(H * 0.06)), desc, font=fm, fill=desc_color)
    return trim(img, pad=8)

def gradient(w, h, top, bot):
    img = Image.new("RGBA", (w, h)); d = ImageDraw.Draw(img)
    for y in range(h):
        t = y / (h - 1); c = tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)) + (255,)
        d.line([(0, y), (w, y)], fill=c)
    return img

def build_brand(b):
    KIT = os.path.join(ROOT, b["folder"])
    for sub in ("", "logo-png", "logo-svg", "icons", "linkedin"):
        os.makedirs(os.path.join(KIT, sub), exist_ok=True)
    A = hx2rgba(b["accent"]); Br = hx2rgba(b["bright"]); Dp = hx2rgba(b["deep"])
    glyph = b["glyph"]
    # marks PNG
    for nm, col in (("accent", A), ("carbon", CARBON), ("white", LIGHT)):
        ac = Br if nm == "accent" else col
        trim(draw_mark(1200, col, col, ac, glyph)).save(os.path.join(KIT, "logo-png", f"{b['key']}-mark-{nm}.png"))
    # icons
    def icon(bg, mc, ac, fname, rf=0.0, size=1024):
        cv = rounded_bg((size, size), bg, rf); mk = trim(draw_mark(int(size * 0.92), mc, mc, ac, glyph))
        s = (size * 0.58) / mk.height; mk = mk.resize((int(mk.width * s), int(mk.height * s)), Image.LANCZOS)
        cv.alpha_composite(mk, ((size - mk.width) // 2, (size - mk.height) // 2)); cv.save(os.path.join(KIT, "icons", fname))
    icon(CARBON, A, Br, "icon-square-carbon.png"); icon(A, CARBON, CARBON, "icon-square-accent.png")
    icon(LIGHT, A, Br, "icon-square-light.png"); icon(CARBON, A, Br, "icon-rounded-carbon.png", rf=0.22)
    base = Image.open(os.path.join(KIT, "icons", "icon-rounded-carbon.png"))
    for s in (256, 64, 32): base.resize((s, s), Image.LANCZOS).save(os.path.join(KIT, "icons", f"favicon-{s}.png"))
    # lockups
    lk_dark = build_lockup(b, LIGHT, MUTED); lk_light = build_lockup(b, CARBON, DGRAY)
    lk_dark.save(os.path.join(KIT, "logo-png", f"{b['key']}-logo-horizontal-onDark.png"))
    lk_light.save(os.path.join(KIT, "logo-png", f"{b['key']}-logo-horizontal-onLight.png"))
    build_lockup(b, LIGHT, MUTED, stacked=True).save(os.path.join(KIT, "logo-png", f"{b['key']}-logo-stacked-onDark.png"))
    build_lockup(b, CARBON, DGRAY, stacked=True).save(os.path.join(KIT, "logo-png", f"{b['key']}-logo-stacked-onLight.png"))
    def on_bg(lk, bg, fname):
        p = int(lk.height * 0.5); cv = rounded_bg((lk.width + 2 * p, lk.height + 2 * p), bg); cv.alpha_composite(lk, (p, p)); cv.save(os.path.join(KIT, "logo-png", fname))
    on_bg(lk_dark, CARBON, f"{b['key']}-logo-onCarbon.png"); on_bg(lk_light, LIGHT, f"{b['key']}-logo-onLight-bg.png")
    # svg
    open(os.path.join(KIT, "logo-svg", f"{b['key']}-mark-accent.svg"), "w").write(svg_mark(b["accent"], glyph, b["accent"], b["bright"]))
    open(os.path.join(KIT, "logo-svg", f"{b['key']}-mark-carbon.svg"), "w").write(svg_mark("#0B0F14", glyph, "#0B0F14", "#0B0F14"))
    open(os.path.join(KIT, "logo-svg", f"{b['key']}-mark-white.svg"), "w").write(svg_mark("#E8EDF2", glyph, "#E8EDF2", "#E8EDF2"))
    # brand sheet
    brand_sheet(b, KIT, lk_dark, lk_light)
    # banners
    make_banner(b, KIT, 1584, 396, "linkedin-personal-banner-1584x396.png")
    make_banner(b, KIT, 1128, 191, "linkedin-company-cover-1128x191.png", company=True)
    write_readme(b, KIT)
    return lk_dark

def brand_sheet(b, KIT, lk_dark, lk_light):
    A = hx2rgba(b["accent"]); Br = hx2rgba(b["bright"]); Dp = hx2rgba(b["deep"]); glyph = b["glyph"]
    W, H = 2000, 1414; img = Image.new("RGBA", (W, H), rgb(LIGHT) + (255,)); d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 250], fill=rgb(CARBON) + (255,))
    hd = trim(lk_dark); s = 150 / hd.height; img.alpha_composite(hd.resize((int(hd.width * s), 150), Image.LANCZOS), (90, 50))
    d.text((W - 600, 95), "BRAND ASSET SHEET", font=F(PLEX_MED, 34), fill=rgb(Br) + (255,))
    d.text((W - 600, 140), b["name"] + " · a SignetStack Labs company", font=F(PLEX_MED, 24), fill=rgb(MUTED) + (255,))
    fsec = F(PLEX_BOLD, 30); fsm = F(PLEX_MED, 24); fmono = F(PLEX_MONO, 22)
    def section(x, y, label):
        d.text((x, y), label.upper(), font=fsec, fill=rgb(Dp) + (255,)); d.line([x, y + 44, x + 380, y + 44], fill=rgb(A) + (255,), width=3)
    section(90, 320, "Logo — primary lockup")
    d.rounded_rectangle([90, 380, 950, 600], radius=14, fill=rgb(CARBON) + (255,))
    a = trim(lk_dark); s = 150 / a.height; img.alpha_composite(a.resize((int(a.width * s), 150), Image.LANCZOS), (130, 405))
    d.rounded_rectangle([90, 620, 950, 840], radius=14, outline=rgb(MUTED) + (255,), width=2, fill=(255, 255, 255, 255))
    bb = trim(lk_light); s = 150 / bb.height; img.alpha_composite(bb.resize((int(bb.width * s), 150), Image.LANCZOS), (130, 645))
    section(90, 900, "Mark")
    specs = [(CARBON, A, Br), (A, CARBON, CARBON), (LIGHT, A, Br)]
    mx = 90
    for bg, mc, ac in specs:
        d.rounded_rectangle([mx, 960, mx + 180, 1140], radius=14, fill=rgb(bg) + (255,), outline=rgb(MUTED) + (255,) if bg == LIGHT else None, width=2)
        mk = trim(draw_mark(300, mc, mc, ac, glyph)); s = 120 / mk.height
        img.alpha_composite(mk.resize((int(mk.width * s), 120), Image.LANCZOS), (mx + 90 - int(mk.width * s) // 2, 990)); mx += 210
    section(1050, 320, "Colour palette")
    sw = [("Carbon", CARBON, "#0B0F14"), (b["accent_name"], A, b["accent"]), ("Bright " + b["accent_name"], Br, b["bright"]),
          ("Deep (text on light)", Dp, b["deep"]), ("Slate", SLATE, "#1B2630"), ("Light Surface", LIGHT, "#E8EDF2")]
    sy = 380
    for nm, col, hxs in sw:
        d.rounded_rectangle([1050, sy, 1130, sy + 64], radius=8, fill=rgb(col) + (255,), outline=rgb(MUTED) + (255,) if col == LIGHT else None, width=2)
        d.text((1155, sy + 6), nm, font=F(PLEX_BOLD, 26), fill=rgb(CARBON) + (255,))
        d.text((1155, sy + 38), hxs, font=fmono, fill=rgb(DGRAY)); sy += 80
    section(1050, 940, "Typography")
    d.text((1050, 996), "IBM Plex Sans", font=F(PLEX_BOLD, 40), fill=rgb(CARBON) + (255,))
    d.text((1050, 1050), "Headlines & body  ·  Aa Bb Cc 0123", font=fsm, fill=rgb(DGRAY))
    d.text((1050, 1096), "IBM Plex Mono", font=F(PLEX_MONO, 36), fill=rgb(CARBON) + (255,))
    d.text((1050, 1146), "Numerals & metrics  ·  0123  µs  %", font=fmono, fill=rgb(DGRAY))
    d.line([90, 1300, W - 90, 1300], fill=(200, 208, 216, 255), width=2)
    d.text((90, 1325), "Clear space ≥ the height of the mark on all sides  ·  Minimum lockup height 24 px  ·  Never recolour, stretch, or add effects.", font=fsm, fill=(110, 120, 132, 255))
    img.convert("RGB").save(os.path.join(KIT, f"{b['key']}-brand-sheet.png"), quality=95)

def make_banner(b, KIT, w, h, fname, company=False):
    scale = 2; W, Hh = w * scale, h * scale
    A = hx2rgba(b["accent"]); Br = hx2rgba(b["bright"])
    img = gradient(W, Hh, rgb(CARBON), rgb(SLATE)); d = ImageDraw.Draw(img)
    mk = trim(draw_mark(int(Hh * 2.2), A, A, A, b["glyph"])); mks = int(Hh * 1.9)
    mk = mk.resize((int(mk.width * mks / mk.height), mks), Image.LANCZOS)
    faint = mk.copy(); faint.putalpha(mk.getchannel("A").point(lambda a: int(a * 0.10)))
    img.alpha_composite(faint, (int(W - mk.width * 0.62), int(Hh * 0.5 - mk.height * 0.5)))
    d.rectangle([0, 0, int(8 * scale), Hh], fill=rgb(A) + (255,))
    lk = trim(build_lockup(b, LIGHT, MUTED))
    if company:
        th = int(Hh * 0.42); avail = W - int(130 * scale) - int(420 * scale)
        s = min(th / lk.height, avail / lk.width); lk = lk.resize((int(lk.width * s), int(lk.height * s)), Image.LANCZOS)
        img.alpha_composite(lk, (int(60 * scale), (Hh - lk.height) // 2))
        fend = F(PLEX_MED, int(Hh * 0.085)); et = "A SIGNETSTACK LABS COMPANY"; eb = d.textbbox((0, 0), et, font=fend)
        d.text((W - (eb[2] - eb[0]) - int(70 * scale), (Hh - (eb[3] - eb[1])) // 2 - eb[1]), et, font=fend, fill=(120, 134, 150, 255))
    else:
        lx = int(W * 0.30); th = int(Hh * 0.30); avail = W - lx - int(70 * scale)
        s = min(th / lk.height, avail / lk.width); lk = lk.resize((int(lk.width * s), int(lk.height * s)), Image.LANCZOS)
        ly = int(Hh * 0.22); img.alpha_composite(lk, (lx, ly))
        ftag = F(PLEX_MED, int(Hh * 0.068))
        d.text((lx + 4, ly + lk.height + int(Hh * 0.045)), b["tagline"], font=ftag, fill=rgb(MUTED) + (255,))
        cy = int(Hh * 0.80); d.line([lx + 4, cy - int(Hh * 0.055), int(W * 0.92), cy - int(Hh * 0.055)], fill=rgb(A) + (140,), width=scale)
        xx = lx + 4
        if b["chip_style"] == "metric":
            fnum = F(PLEX_MONO, int(Hh * 0.072)); flbl = F(PLEX_MED, int(Hh * 0.042)); gap = int(W * 0.035)
            for num, lbl in b["chips"]:
                nb = d.textbbox((0, 0), num, font=fnum); d.text((xx, cy), num, font=fnum, fill=rgb(Br) + (255,))
                d.text((xx + (nb[2] - nb[0]) + int(8 * scale), cy + int(Hh * 0.014)), lbl, font=flbl, fill=rgb(MUTED) + (255,))
                lb = d.textbbox((0, 0), lbl, font=flbl); xx += (nb[2] - nb[0]) + (lb[2] - lb[0]) + gap
        else:
            ftag2 = F(PLEX_MED, int(Hh * 0.062)); gap = int(W * 0.028)
            for i, word in enumerate(b["chips"]):
                if i:
                    d.text((xx, cy), "·", font=ftag2, fill=rgb(A) + (255,)); db = d.textbbox((0, 0), "·", font=ftag2); xx += (db[2] - db[0]) + gap
                d.text((xx, cy), word, font=ftag2, fill=rgb(Br) + (255,)); wb = d.textbbox((0, 0), word, font=ftag2); xx += (wb[2] - wb[0]) + gap
        fend = F(PLEX_MED, int(Hh * 0.044)); et = "A SIGNETSTACK LABS COMPANY"; eb = d.textbbox((0, 0), et, font=fend)
        d.text((W - (eb[2] - eb[0]) - int(60 * scale), int(Hh * 0.10)), et, font=fend, fill=(120, 134, 150, 255))
    img.convert("RGB").resize((w, h), Image.LANCZOS).save(os.path.join(KIT, "linkedin", fname), quality=95)
    img.convert("RGB").save(os.path.join(KIT, "linkedin", fname.replace(".png", "@2x.png")), quality=95)

def write_readme(b, KIT):
    txt = f"""# {b['name']} — Brand Asset Kit
*{b['tagline']} · a SignetStack Labs company*

Part of the SignetStack Labs brand family. Open `{b['key']}-brand-sheet.png` for the one-page reference.

## Palette (shared Carbon base + IBM Plex type)
| Name | Hex | Use |
|---|---|---|
| Carbon | `#0B0F14` | Primary dark background |
| {b['accent_name']} | `{b['accent']}` | Primary accent (fills — pair with carbon/dark text) |
| Bright {b['accent_name']} | `{b['bright']}` | Accent highlight / text on dark |
| Deep | `{b['deep']}` | Accent **text on light** backgrounds (readable) |
| Slate | `#1B2630` | Panels / secondary dark |
| Light Surface | `#E8EDF2` | Light background |

**Type:** IBM Plex Sans (headlines & body), IBM Plex Mono (numerals/metrics).
**Mark:** the shared Signet hexagon seal with the {b['name']} domain glyph.

## Files
- `logo-png/` — horizontal & stacked lockups (onDark / onLight), lockup on solid bg, mark only (accent / carbon / white).
- `logo-svg/` — scalable mark in accent / carbon / white.
- `icons/` — 1024px square icons (carbon / accent / light), rounded app icon, favicons (256/64/32).
- `linkedin/` — personal background banner 1584×396 (+@2x) and company cover 1128×191 (+@2x).

## Rules
Clear space ≥ the mark height · minimum lockup 24px · use onDark on dark, onLight on light · never recolour, stretch, or add effects.
"""
    open(os.path.join(KIT, "README.md"), "w").write(txt)

# ---------------- FAMILY OVERVIEW ----------------
def family_sheet(lockups):
    W, H = 2000, 1200; img = Image.new("RGBA", (W, H), rgb(CARBON) + (255,)); d = ImageDraw.Draw(img)
    d.text((90, 70), "SIGNET STACK LTD", font=F(PLEX_BOLD, 52), fill=rgb(LIGHT) + (255,))
    d.text((92, 140), "Brand family — one signet seal, four domains", font=F(PLEX_MED, 30), fill=rgb(MUTED) + (255,))
    d.line([90, 210, W - 90, 210], fill=(40, 54, 66, 255), width=3)
    cw = (W - 180) // 4
    for i, b in enumerate(BRANDS):
        A = hx2rgba(b["accent"]); Br = hx2rgba(b["bright"]); x = 90 + i * cw
        d.line([x + 20, 250, x + 20, H - 120], fill=(34, 46, 56, 255), width=2) if i else None
        mk = trim(draw_mark(560, A, A, Br, b["glyph"])); mh = 300; mk = mk.resize((int(mk.width * mh / mk.height), mh), Image.LANCZOS)
        img.alpha_composite(mk, (x + cw // 2 - mk.width // 2, 300))
        d.text((x + cw // 2, 660), b["name"], font=F(PLEX_BOLD, 36), fill=rgb(LIGHT) + (255,), anchor="ma")
        # wrap desc
        dsc = b["desc"].replace("  ·  ", "\n").replace(" · ", "\n")
        for j, line in enumerate(dsc.split("\n")):
            d.text((x + cw // 2, 720 + j * 38), line, font=F(PLEX_MED, 22), fill=rgb(Br) + (255,), anchor="ma")
        d.rounded_rectangle([x + cw // 2 - 70, 840, x + cw // 2 + 70, 880], radius=8, fill=rgb(A) + (255,))
        d.text((x + cw // 2, 848), b["accent"], font=F(PLEX_MONO, 22), fill=rgb(CARBON) + (255,), anchor="ma")
    d.text((90, H - 80), "Shared system: Carbon #0B0F14 · IBM Plex Sans / Mono · hexagonal signet seal + per-domain glyph.", font=F(PLEX_MED, 24), fill=rgb(MUTED) + (255,))
    img.convert("RGB").save(os.path.join(ROOT, "Signet_Stack_Brand_Family.png"), quality=95)

if __name__ == "__main__":
    locks = [build_brand(b) for b in BRANDS]
    # The house-of-brands architecture overview is maintained separately (kept out of this repo).
    print("Done. Divisions:", ", ".join(b["name"] for b in BRANDS))
