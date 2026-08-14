"""Generate icon PNGs (transparent background) used across the Advanced Power BI
overview deck. Built with Pillow primitives only -- no external icon library
dependency required.

Each icon is drawn on a square canvas at high resolution, flat/minimal style,
single accent color, then saved as PNG with alpha transparency.
"""
from PIL import Image, ImageDraw
import math
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "assets", "icons")
os.makedirs(OUT_DIR, exist_ok=True)

SIZE = 512
PAD = 60


def canvas():
    return Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def save(img, name):
    path = os.path.join(OUT_DIR, f"{name}.png")
    img.save(path)
    print("wrote", path)


def stroke(draw, xy, color, width, **kw):
    draw.line(xy, fill=color, width=width, **kw)


# ---------------------------------------------------------------- foundation
def icon_layers(color):
    img = canvas()
    d = ImageDraw.Draw(img)
    rgb = hex_to_rgb(color)
    cx, cy = SIZE // 2, SIZE // 2
    w = 300
    h = 70
    offsets = [-110, 0, 110]
    for i, off in enumerate(offsets):
        top = cy + off - h // 2
        pts = [
            (cx - w // 2, top + h // 2),
            (cx, top),
            (cx + w // 2, top + h // 2),
            (cx, top + h),
        ]
        alpha = 255 if i == 2 else (170 if i == 1 else 110)
        d.polygon(pts, outline=rgb + (255,), width=10)
        if i == 2:
            d.polygon(pts, fill=rgb + (alpha,))
    save(img, "layers")


# ---------------------------------------------------------------- dax / formula
def icon_formula(color):
    img = canvas()
    d = ImageDraw.Draw(img)
    rgb = hex_to_rgb(color)
    d.ellipse([PAD, PAD, SIZE - PAD, SIZE - PAD], outline=rgb + (255,), width=16)
    fx = SIZE * 0.30
    fy = SIZE * 0.68
    d.line([(fx, fy), (fx + 40, SIZE * 0.32)], fill=rgb + (255,), width=18)
    d.line([(fx + 40, SIZE * 0.32), (fx + 120, SIZE * 0.32)], fill=rgb + (255,), width=18)
    d.line([(fx + 10, SIZE * 0.5), (fx + 90, SIZE * 0.5)], fill=rgb + (255,), width=14)
    d.line([(SIZE * 0.56, SIZE * 0.35), (SIZE * 0.78, SIZE * 0.65)], fill=rgb + (255,), width=16)
    d.line([(SIZE * 0.78, SIZE * 0.35), (SIZE * 0.56, SIZE * 0.65)], fill=rgb + (255,), width=16)
    save(img, "formula")


# ---------------------------------------------------------------- funnel / query
def icon_funnel(color):
    img = canvas()
    d = ImageDraw.Draw(img)
    rgb = hex_to_rgb(color)
    top_w = 360
    bottom_w = 60
    top_y = PAD + 20
    bottom_y = SIZE - PAD - 40
    cx = SIZE // 2
    pts = [
        (cx - top_w // 2, top_y),
        (cx + top_w // 2, top_y),
        (cx + bottom_w // 2, bottom_y),
        (cx - bottom_w // 2, bottom_y),
    ]
    d.polygon(pts, outline=rgb + (255,), width=16)
    d.line([(cx - bottom_w // 2, bottom_y), (cx - bottom_w // 2, bottom_y + 70)], fill=rgb + (255,), width=16)
    d.line([(cx + bottom_w // 2, bottom_y), (cx + bottom_w // 2, bottom_y + 70)], fill=rgb + (255,), width=16)
    for i, yy in enumerate([top_y + 60, top_y + 130]):
        span = top_w - i * 110
        d.line([(cx - span // 2, yy), (cx + span // 2, yy)], fill=rgb + (140,), width=8)
    save(img, "funnel")


# ---------------------------------------------------------------- canvas / report
def icon_canvas_layout(color):
    img = canvas()
    d = ImageDraw.Draw(img)
    rgb = hex_to_rgb(color)
    d.rounded_rectangle([PAD, PAD, SIZE - PAD, SIZE - PAD], radius=28, outline=rgb + (255,), width=14)
    midx = SIZE * 0.42
    d.line([(midx, PAD + 10), (midx, SIZE - PAD - 10)], fill=rgb + (255,), width=10)
    d.line([(midx, SIZE * 0.55), (SIZE - PAD - 10, SIZE * 0.55)], fill=rgb + (255,), width=10)
    d.rounded_rectangle([PAD + 24, PAD + 24, midx - 16, SIZE - PAD - 24], radius=10, fill=rgb + (60,))
    d.rounded_rectangle([midx + 16, PAD + 24, SIZE - PAD - 24, SIZE * 0.55 - 8], radius=10, fill=rgb + (110,))
    d.rounded_rectangle([midx + 16, SIZE * 0.55 + 8, SIZE - PAD - 24, SIZE - PAD - 24], radius=10, fill=rgb + (60,))
    save(img, "canvas_layout")


# ---------------------------------------------------------------- speed / gauge
def icon_gauge(color):
    img = canvas()
    d = ImageDraw.Draw(img)
    rgb = hex_to_rgb(color)
    bbox = [PAD, PAD, SIZE - PAD, SIZE - PAD]
    d.arc(bbox, start=180, end=360, fill=rgb + (255,), width=22)
    cx, cy = SIZE // 2, SIZE // 2
    ang = math.radians(300)
    r = (SIZE - 2 * PAD) / 2 - 20
    nx, ny = cx + r * math.cos(ang), cy + r * math.sin(ang) * -1 + (SIZE * 0.0)
    # needle pointing to ~ upper right-ish
    needle_ang = math.radians(35)
    nx = cx + r * math.cos(needle_ang)
    ny = cy - r * math.sin(needle_ang)
    d.line([(cx, cy), (nx, ny)], fill=rgb + (255,), width=16)
    d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=rgb + (255,))
    save(img, "gauge")


# ---------------------------------------------------------------- spark / ai
def icon_spark(color):
    img = canvas()
    d = ImageDraw.Draw(img)
    rgb = hex_to_rgb(color)
    cx, cy = SIZE // 2, SIZE // 2

    def star(cx, cy, r_out, r_in, points=4, rot=0):
        pts = []
        for i in range(points * 2):
            r = r_out if i % 2 == 0 else r_in
            ang = math.pi * i / points + rot
            pts.append((cx + r * math.sin(ang), cy - r * math.cos(ang)))
        return pts

    d.polygon(star(cx, cy, 190, 70, 4, 0), fill=rgb + (255,))
    d.polygon(star(cx + 150, cy - 150, 60, 22, 4, 0.3), fill=rgb + (170,))
    d.polygon(star(cx - 160, cy + 130, 40, 16, 4, 0.6), fill=rgb + (120,))
    save(img, "spark")


# ---------------------------------------------------------------- shield / security
def icon_shield(color):
    img = canvas()
    d = ImageDraw.Draw(img)
    rgb = hex_to_rgb(color)
    cx = SIZE // 2
    top = PAD
    w = SIZE - 2 * PAD
    pts = [
        (cx - w // 2, top + 40),
        (cx, top),
        (cx + w // 2, top + 40),
        (cx + w // 2, top + 220),
        (cx, SIZE - PAD),
        (cx - w // 2, top + 220),
    ]
    d.polygon(pts, outline=rgb + (255,), width=16)
    # checkmark
    cy_ = top + 230
    d.line([(cx - 70, cy_), (cx - 20, cy_ + 60)], fill=rgb + (255,), width=20)
    d.line([(cx - 20, cy_ + 60), (cx + 90, cy_ - 60)], fill=rgb + (255,), width=20)
    save(img, "shield")


# ---------------------------------------------------------------- gear / ops
def icon_gear(color):
    img = canvas()
    d = ImageDraw.Draw(img)
    rgb = hex_to_rgb(color)
    cx, cy = SIZE // 2, SIZE // 2
    r_outer = 210
    r_inner = 150
    teeth = 8
    tooth_w = 0.16
    pts = []
    for i in range(teeth * 2):
        ang = math.pi * i / teeth
        if i % 2 == 0:
            r = r_outer
        else:
            r = r_inner
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    d.polygon(pts, fill=rgb + (255,))
    d.ellipse([cx - 90, cy - 90, cx + 90, cy + 90], fill=(0, 0, 0, 0))
    d.ellipse([cx - 80, cy - 80, cx + 80, cy + 80], outline=(255, 255, 255, 0), width=0)
    # punch a hole using composite
    mask = Image.new("L", (SIZE, SIZE), 0)
    md = ImageDraw.Draw(mask)
    md.ellipse([cx - 80, cy - 80, cx + 80, cy + 80], fill=255)
    hole = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    img = Image.composite(hole, img, mask)
    save(img, "gear")


# ---------------------------------------------------------------- rocket / capstone
def icon_rocket(color):
    img = canvas()
    d = ImageDraw.Draw(img)
    rgb = hex_to_rgb(color)
    cx = SIZE // 2
    # body
    body = [
        (cx, PAD),
        (cx + 70, SIZE * 0.55),
        (cx + 70, SIZE * 0.75),
        (cx - 70, SIZE * 0.75),
        (cx - 70, SIZE * 0.55),
    ]
    d.polygon(body, fill=rgb + (255,))
    # fins
    d.polygon([(cx - 70, SIZE * 0.55), (cx - 140, SIZE * 0.78), (cx - 70, SIZE * 0.75)], fill=rgb + (200,))
    d.polygon([(cx + 70, SIZE * 0.55), (cx + 140, SIZE * 0.78), (cx + 70, SIZE * 0.75)], fill=rgb + (200,))
    # window
    d.ellipse([cx - 30, SIZE * 0.3, cx + 30, SIZE * 0.42], fill=(255, 255, 255, 255))
    # flame
    d.polygon([(cx - 30, SIZE * 0.75), (cx, SIZE * 0.92), (cx + 30, SIZE * 0.75)], fill=rgb + (140,))
    save(img, "rocket")


PALETTE_ACCENT = "3DDC97"

icon_layers(PALETTE_ACCENT)
icon_formula(PALETTE_ACCENT)
icon_funnel(PALETTE_ACCENT)
icon_canvas_layout(PALETTE_ACCENT)
icon_gauge(PALETTE_ACCENT)
icon_spark(PALETTE_ACCENT)
icon_shield(PALETTE_ACCENT)
icon_gear(PALETTE_ACCENT)
icon_rocket(PALETTE_ACCENT)

print("done")
