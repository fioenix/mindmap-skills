#!/usr/bin/env python3
import os
import subprocess
import tempfile
from PIL import Image

# Monoline mark: one hollow root node fanning out into three branches.
# Single brand color on a transparent canvas, matching the Vietnamizer icon family.
LIGHT_COLOR = "#9750C4"
DARK_COLOR = "#7FE2CE"


def generate_svg(color, title, size=128):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 128 128" role="img" aria-labelledby="title">
  <title id="title">{title}</title>
  <circle cx="40" cy="64" r="11" fill="none" stroke="{color}" stroke-width="9"/>
  <path d="M51 64 C72 64 72 34 100 34 M51 64 H100 M51 64 C72 64 72 94 100 94" fill="none" stroke="{color}" stroke-width="8" stroke-linecap="round"/>
</svg>
'''


def render_png(svg_content, png_path, color):
    # qlmanage renders onto opaque white; recover the alpha channel from the
    # known single foreground color so the PNG stays transparent like the SVG.
    with tempfile.TemporaryDirectory() as tmp_dir:
        svg_path = os.path.join(tmp_dir, "icon.svg")
        with open(svg_path, "w") as f:
            f.write(svg_content)
        subprocess.run(["qlmanage", "-t", "-s", "512", "-o", tmp_dir, svg_path],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        rendered = Image.open(os.path.join(tmp_dir, "icon.svg.png")).convert("RGB")

    if rendered.size != (512, 512):
        rendered = rendered.resize((512, 512), Image.Resampling.LANCZOS)

    rgb = tuple(int(color[i:i + 2], 16) for i in (1, 3, 5))
    # Use the channel with the largest distance from white for the best precision.
    channel = min(range(3), key=lambda c: rgb[c])
    span = 255 - rgb[channel]
    alpha = rendered.getchannel(channel).point(
        lambda v: max(0, min(255, round((255 - v) * 255 / span))))
    png_img = Image.new("RGBA", (512, 512), rgb + (0,))
    png_img.putalpha(alpha)
    png_img.save(png_path, format="PNG")


def main():
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    light_svg = generate_svg(LIGHT_COLOR, "Mindmap Skills — mindmap")
    dark_svg = generate_svg(DARK_COLOR, "Mindmap Skills — mindmap, dark")

    outputs = {
        "assets/icon.svg": light_svg,
        "logo.svg": light_svg,
        "assets/icon-dark.svg": dark_svg,
    }
    for rel_path, content in outputs.items():
        with open(os.path.join(repo_dir, rel_path), "w") as f:
            f.write(content)
    print("Updated assets/icon.svg, assets/icon-dark.svg and logo.svg")

    icon_png_path = os.path.join(repo_dir, "assets/icon.png")
    render_png(generate_svg(LIGHT_COLOR, "Mindmap Skills — mindmap", size=512),
               icon_png_path, LIGHT_COLOR)
    print(f"Saved {icon_png_path} (512, 512)")


if __name__ == "__main__":
    main()
