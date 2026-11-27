"""Render the proof explorer's schematic orbit as a GIF with Pillow."""
import math
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent


def project(index, level, angle):
    x = 9 * ((index + .5) / 2**level - .5)
    z = .74 if level % 2 else -.74
    horizontal = x * math.cos(angle) - z * math.sin(angle)
    depth = x * math.sin(angle) + z * math.cos(angle)
    scale = 94 / (6 - depth * .25)
    return 410 + horizontal * scale * 4.9, 62 + (level * 1.05 - .13 * depth) * scale * 4.7


frames = []
for step in range(48):
    angle = 2 * math.pi * step / 48
    image = Image.new("RGB", (820, 380), "#172c35")
    draw = ImageDraw.Draw(image)
    draw.text((22, 20), "Monomial digit choices", fill="#f5faf8", font_size=24)
    draw.text((22, 350), "Muted: omit   /   Green: include   /   Schematic spacing", fill="#c6dedb", font_size=17)
    for level in range(1, 4):
        for index in range(2**level):
            draw.line(
                [project(index // 2, level - 1, angle), project(index, level, angle)],
                fill="#a6f2c2" if index % 2 else "#678d9d",
                width=3,
            )
    for level in range(4):
        for index in range(2**level):
            x, y = project(index, level, angle)
            draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill="#f5faf8")
            if level == 3:
                draw.text((x, y + 12), f"{index:03b}", anchor="mt", fill="#f5faf8", font_size=17)
    frames.append(image)
frames[0].save(ROOT / "prefix-tree.gif", save_all=True, append_images=frames[1:], duration=74, loop=0)
