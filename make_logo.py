"""
Generate an ancient / divine themed PNG logo for Naryani Shop using Pillow.
Run:  python make_logo.py   ->  assets/logo.png

Theme: Naryani = the Goddess. Design uses sacred Indian iconography —
Om (ॐ), lotus petals, a radiant sun-halo, and temple gold on deep
maroon/saffron, framed by a decorative ring.
"""

import math
import os

from PIL import Image, ImageDraw, ImageFont

SIZE = 1000
SS = 3  # supersample for crisp edges
OUT = os.path.join("assets", "logo.png")

# Ancient temple palette — maroon, saffron, gold
MAROON = (91, 20, 24)       # deep temple maroon
SAFFRON = (196, 92, 24)     # saffron / sindoor
DEEP = (60, 12, 16)
GOLD = (212, 175, 55)
GOLD_LT = (247, 224, 138)
GOLD_DK = (156, 120, 20)
CREAM = (255, 248, 225)


def radial_gradient(size, inner, outer):
    img = Image.new("RGB", (size, size), outer)
    px = img.load()
    cx = cy = size / 2
    maxd = math.hypot(cx, cy)
    for y in range(size):
        for x in range(size):
            d = min(1.0, math.hypot(x - cx, y - cy) / maxd)
            px[x, y] = (
                int(inner[0] + (outer[0] - inner[0]) * d),
                int(inner[1] + (outer[1] - inner[1]) * d),
                int(inner[2] + (outer[2] - inner[2]) * d),
            )
    return img


def load_font(size, bold=True, serif=True):
    candidates = []
    if serif:
        candidates += [
            "C:/Windows/Fonts/georgiab.ttf" if bold else "C:/Windows/Fonts/georgia.ttf",
            "C:/Windows/Fonts/timesbd.ttf" if bold else "C:/Windows/Fonts/times.ttf",
        ]
    candidates += [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_om(draw, cx, cy, scale, color):
    """Draw the Om (ॐ) symbol as vector strokes so it renders on any system."""
    w = max(2, int(round(14 * scale)))

    def arc(bbox, start, end):
        draw.arc(bbox, start, end, fill=color, width=w)

    def s(v):
        return v * scale

    # Big lower loop (the "3"-like belly of Om)
    arc([cx - s(120), cy - s(20), cx - s(10), cy + s(90)], 90, 360)
    arc([cx - s(30), cy - s(20), cx + s(90), cy + s(95)], 130, 400)
    # Upper small loop
    arc([cx - s(120), cy - s(120), cx - s(20), cy - s(30)], 90, 300)
    # Tail curving to the right from upper loop
    arc([cx - s(30), cy - s(130), cx + s(80), cy - s(30)], 150, 360)
    # Crescent (chandra) above right
    cxm, cym = cx + s(70), cy - s(120)
    arc([cxm - s(45), cym - s(35), cxm + s(45), cym + s(20)], 200, 340)
    # Bindu (dot) above the crescent
    r = s(14)
    draw.ellipse([cx + s(70) - r, cy - s(175) - r, cx + s(70) + r, cy - s(175) + r], fill=color)


def centered_text(draw, y, text, font, fill, spacing=0, canvas=SIZE):
    if spacing:
        widths = [draw.textlength(ch, font=font) for ch in text]
        total = sum(widths) + spacing * (len(text) - 1)
        x = (canvas - total) / 2
        for ch, w in zip(text, widths):
            draw.text((x, y), ch, font=font, fill=fill)
            x += w + spacing
    else:
        w = draw.textlength(text, font=font)
        draw.text(((canvas - w) / 2, y), text, font=font, fill=fill)


def petal(draw, cx, cy, angle, length, width, fill, outline):
    """Draw one lotus petal as a rotated pointed ellipse (polygon)."""
    pts = []
    steps = 24
    for i in range(steps + 1):
        t = i / steps * math.pi
        # pointed-leaf shape
        r = math.sin(t)
        px = (r * width) * math.cos(t * 0 + math.pi / 2)  # placeholder
    # simpler: build a leaf via two arcs approximated by points
    leaf = []
    for i in range(steps + 1):
        t = i / steps
        # distance along the petal
        d = t * length
        # half-width tapering at both ends (leaf/almond)
        hw = math.sin(t * math.pi) * width / 2
        leaf.append((d, hw))
    for i in range(steps, -1, -1):
        t = i / steps
        d = t * length
        hw = math.sin(t * math.pi) * width / 2
        leaf.append((d, -hw))
    # rotate + translate
    ca, sa = math.cos(angle), math.sin(angle)
    poly = [(cx + x * ca - y * sa, cy + x * sa + y * ca) for x, y in leaf]
    draw.polygon(poly, fill=fill, outline=outline)


def main():
    os.makedirs("assets", exist_ok=True)
    S = SIZE * SS
    cx = cy = S / 2
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))

    # circular badge with maroon->saffron radial glow (divine aura)
    grad = radial_gradient(S, SAFFRON, MAROON).convert("RGBA")
    cmask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(cmask).ellipse([40 * SS, 40 * SS, 960 * SS, 960 * SS], fill=255)
    grad.putalpha(cmask)
    img.paste(grad, (0, 0), grad)

    draw = ImageDraw.Draw(img)

    # --- radiant sun halo behind center (divine rays) ---
    rays = 48
    for i in range(rays):
        a = (i / rays) * 2 * math.pi
        r1 = 150 * SS
        r2 = 300 * SS
        x1, y1 = cx + r1 * math.cos(a), cy + r1 * math.sin(a)
        x2, y2 = cx + r2 * math.cos(a), cy + r2 * math.sin(a)
        col = GOLD_LT if i % 2 == 0 else GOLD
        draw.line([(x1, y1), (x2, y2)], fill=(*col, 90), width=3 * SS)

    # --- lotus of petals around the center ---
    n = 12
    for i in range(n):
        a = (i / n) * 2 * math.pi - math.pi / 2
        petal(draw, cx + 165 * SS * math.cos(a), cy + 165 * SS * math.sin(a),
              a, 150 * SS, 70 * SS, fill=(*GOLD, 230), outline=GOLD_DK)
    # inner ring of smaller petals
    for i in range(n):
        a = (i / n) * 2 * math.pi - math.pi / 2 + math.pi / n
        petal(draw, cx + 120 * SS * math.cos(a), cy + 120 * SS * math.sin(a),
              a, 95 * SS, 50 * SS, fill=(*CREAM, 235), outline=GOLD_DK)

    # --- central medallion ---
    draw.ellipse([cx - 130 * SS, cy - 130 * SS, cx + 130 * SS, cy + 130 * SS],
                 fill=MAROON, outline=GOLD, width=6 * SS)

    # --- Om symbol (ॐ) drawn as vector strokes, centered in the medallion ---
    draw_om(draw, cx - 15 * SS, cy + 5 * SS, SS, GOLD_LT)

    # --- decorative dotted temple border ---
    dots = 60
    for i in range(dots):
        a = (i / dots) * 2 * math.pi
        rx, ry = cx + 452 * SS * math.cos(a), cy + 452 * SS * math.sin(a)
        rr = 5 * SS
        draw.ellipse([rx - rr, ry - rr, rx + rr, ry + rr], fill=GOLD)
    draw.ellipse([46 * SS, 46 * SS, 954 * SS, 954 * SS], outline=GOLD, width=10 * SS)
    draw.ellipse([72 * SS, 72 * SS, 928 * SS, 928 * SS], outline=GOLD_DK, width=3 * SS)

    # --- brand wordmark on a banner ---
    f_brand = load_font(88 * SS, bold=True, serif=True)
    f_sub = load_font(40 * SS, bold=False, serif=True)
    centered_text(draw, cy + 300 * SS, "NARYANI", f_brand, GOLD_LT, spacing=6 * SS, canvas=S)
    centered_text(draw, cy + 392 * SS, "S H O P", f_sub, CREAM, spacing=12 * SS, canvas=S)

    img = img.resize((SIZE, SIZE), Image.LANCZOS)
    img.save(OUT)
    print(f"Saved {OUT} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
