#!/usr/bin/env python3
"""SignetStack brand mark + wordmark + shared font/geometry helpers — Carbon & Cyan.
Mark = hexagonal signet seal containing ascending signal bars.
Note: build_brand_family.py imports the font helpers (find_font, F, PLEX_BOLD,
PLEX_MED) from here; the standalone lockup drawing below is not used by the site build."""
import math, os, glob
from PIL import Image, ImageDraw, ImageFont

CARBON   = (11, 15, 20, 255)     # #0B0F14
CYAN     = (18, 194, 201, 255)   # #12C2C9
CYAN_BR  = (22, 224, 212, 255)   # #16E0D4
LIGHT    = (232, 237, 242, 255)  # #E8EDF2
SLATE    = (27, 38, 48, 255)     # #1B2630
AMBER    = (242, 183, 5, 255)    # #F2B705
MUTED    = (138, 150, 162, 255)

ASSET = os.path.dirname(os.path.abspath(__file__))

def find_font(substrings, fallbacks):
    cands = []
    for d in [os.path.expanduser("~/Library/Fonts"), "/Library/Fonts", "/System/Library/Fonts", "/System/Library/Fonts/Supplemental"]:
        cands += glob.glob(os.path.join(d, "*.ttf")) + glob.glob(os.path.join(d, "*.otf"))
    for sub in substrings:
        for c in cands:
            if sub.lower() in os.path.basename(c).lower():
                return c
    for fb in fallbacks:
        if os.path.exists(fb):
            return fb
    return None

PLEX_BOLD = find_font(["IBMPlexSans-Bold", "IBMPlexSans-SemiBold"], ["/System/Library/Fonts/Avenir Next.ttc"])
PLEX_MED  = find_font(["IBMPlexSans-Medium", "IBMPlexSans-Regular"], ["/System/Library/Fonts/Avenir Next.ttc"])

def F(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", size, index=8)

def hexagon(cx, cy, R):
    pts = []
    for i in range(6):
        a = math.radians(60 * i - 90)  # pointy-top
        pts.append((cx + R * math.cos(a), cy + R * math.sin(a)))
    return pts

def draw_mark(size, hex_color, bar_color, accent=None):
    """Return an RGBA image of the hex-seal mark sized ~size x size."""
    SS = 4  # supersample
    W = size * SS
    img = Image.new("RGBA", (W, W), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = cy = W / 2
    R = W * 0.46
    stroke = int(W * 0.072)
    pts = hexagon(cx, cy, R)
    # outline ring
    for i in range(6):
        p1, p2 = pts[i], pts[(i + 1) % 6]
        d.line([p1, p2], fill=hex_color, width=stroke, joint="curve")
    # round the vertices
    for p in pts:
        d.ellipse([p[0]-stroke/2, p[1]-stroke/2, p[0]+stroke/2, p[1]+stroke/2], fill=hex_color)
    # ascending signal bars inside (3 bars)
    bw = W * 0.115
    gap = W * 0.072
    base_y = cy + R * 0.40
    heights = [0.30, 0.52, 0.78]
    total_w = 3 * bw + 2 * gap
    x0 = cx - total_w / 2
    for i, hf in enumerate(heights):
        bh = R * hf
        x = x0 + i * (bw + gap)
        col = accent if (accent and i == 2) else bar_color
        d.rounded_rectangle([x, base_y - bh, x + bw, base_y], radius=bw*0.32, fill=col)
    return img.resize((size, size), Image.LANCZOS)

def trim(img):
    bb = img.getbbox()
    return img.crop(bb) if bb else img

def build_lockup(text_color, mark_img, descriptor_color, fname):
    """mark on left + 'SignetStack Labs' wordmark + descriptor line."""
    H = 420
    wm_size = 300
    desc_size = 60
    fbold = F(PLEX_BOLD, wm_size)
    fmed  = F(PLEX_MED, desc_size)
    tmp = Image.new("RGBA", (10, 10)); td = ImageDraw.Draw(tmp)
    word = "SignetStack Labs"
    desc = "A HOUSE OF FRONTIER-TECHNOLOGY BRANDS"
    wb = td.textbbox((0, 0), word, font=fbold)
    ww, wh = wb[2]-wb[0], wb[3]-wb[1]
    db = td.textbbox((0, 0), desc, font=fmed)
    dw = db[2]-db[0]
    mark_h = int(H * 0.86)
    mk = mark_img.resize((mark_h, mark_h), Image.LANCZOS)
    gap = int(H * 0.16)
    text_w = max(ww, dw)
    W = mark_h + gap + text_w + 40
    img = Image.new("RGBA", (W + 40, H + 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    my = (H - mark_h)//2 + 20
    img.alpha_composite(mk, (20, my))
    tx = 20 + mark_h + gap
    # vertically: wordmark then descriptor, as a block centered
    block_h = wh + int(desc_size*1.4)
    ty = (H - block_h)//2 + 20 - wb[1]
    d.text((tx, ty), word, font=fbold, fill=text_color)
    d.text((tx + 4, ty + wb[3] + int(H*0.045)), desc, font=fmed, fill=descriptor_color)
    trim(img).save(os.path.join(ASSET, fname))

if __name__ == "__main__":
    # marks
    mark_cyan = draw_mark(560, CYAN, CYAN, accent=CYAN_BR)
    trim(mark_cyan).save(os.path.join(ASSET, "signetlabs_mark_cyan.png"))
    mark_dark = draw_mark(560, CARBON, CYAN, accent=CYAN_BR)
    trim(mark_dark).save(os.path.join(ASSET, "signetlabs_mark_dark.png"))
    mark_light = draw_mark(560, LIGHT, CYAN, accent=CYAN_BR)
    trim(mark_light).save(os.path.join(ASSET, "signetlabs_mark_light.png"))
    # lockups
    build_lockup(LIGHT, draw_mark(560, CYAN, CYAN, accent=CYAN_BR), MUTED, "signetlabs_logo_dark.png")    # for dark bg
    build_lockup(CARBON, draw_mark(560, CARBON, CYAN, accent=CYAN_BR), (90,100,112,255), "signetlabs_logo_light.png")  # for light bg
    print("PLEX_BOLD:", os.path.basename(PLEX_BOLD or "NONE"))
    print("PLEX_MED :", os.path.basename(PLEX_MED or "NONE"))
    for n in ["signetlabs_mark_cyan","signetlabs_mark_dark","signetlabs_mark_light","signetlabs_logo_dark","signetlabs_logo_light"]:
        im = Image.open(os.path.join(ASSET, n + ".png")); print(n, im.size)
