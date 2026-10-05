#!/usr/bin/env python3
import math
import os
import subprocess
import base64
from PIL import Image

def generate_conic_background(size=512):
    # FINOLABS signature token: --fn-gradient-iridescent
    # conic-gradient(from 220deg at 60% 40%, #BFE9C6 0deg, #87D3E1 70deg, #B49BD8 150deg, #9750C4 210deg, #C9A8E5 270deg, #7FE2CE 330deg, #BFE9C6 360deg)
    stops = [
        (0.0,   (191, 233, 198)),  # #BFE9C6 0deg
        (70.0,  (135, 211, 225)),  # #87D3E1 70deg
        (150.0, (180, 155, 216)),  # #B49BD8 150deg
        (210.0, (151, 80,  196)),  # #9750C4 210deg
        (270.0, (201, 168, 229)),  # #C9A8E5 270deg
        (330.0, (127, 226, 206)),  # #7FE2CE 330deg
        (360.0, (191, 233, 198)),  # #BFE9C6 360deg
    ]
    img = Image.new("RGBA", (size, size))
    pixels = img.load()
    cx = size * 0.60
    cy = size * 0.40
    
    for y in range(size):
        for x in range(size):
            dx = x - cx
            dy = y - cy
            angle_deg = math.degrees(math.atan2(dy, dx))
            deg = (angle_deg - 220.0) % 360.0
            if deg < 0:
                deg += 360.0
            for i in range(len(stops) - 1):
                d0, c0 = stops[i]
                d1, c1 = stops[i+1]
                if d0 <= deg <= d1:
                    t = (deg - d0) / (d1 - d0)
                    r = int(c0[0] + (c1[0] - c0[0]) * t)
                    g = int(c0[1] + (c1[1] - c0[1]) * t)
                    b = int(c0[2] + (c1[2] - c0[2]) * t)
                    pixels[x, y] = (r, g, b, 255)
                    break
    return img

def main():
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bg_img = generate_conic_background(512)
    bg_path = "/tmp/fn_conic_bg.png"
    bg_img.save(bg_path, format="PNG")
    
    with open(bg_path, "rb") as f:
        bg_b64 = base64.b64encode(f.read()).decode("utf-8")

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <!-- Squircle shape clipping (FINOLABS Apple-style standard) -->
    <clipPath id="squircle-clip">
      <rect x="0" y="0" width="512" height="512" rx="108" ry="108" />
    </clipPath>
    <!-- Soft shadow for 3D elevation on iridescent ground -->
    <filter id="soft-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#0B0B17" flood-opacity="0.22" />
    </filter>
  </defs>

  <!-- Background: FINOLABS Signature Iridescent Conic Swirl -->
  <g clip-path="url(#squircle-clip)">
    <image href="data:image/png;base64,{bg_b64}" width="512" height="512" preserveAspectRatio="none" />
  </g>

  <!-- Foreground: Pure Minimalist Markmap Branching Glyph -->
  <g filter="url(#soft-shadow)" fill="none" stroke="#FFFFFF" stroke-width="36" stroke-linecap="round" stroke-linejoin="round">
    <!-- Horizontal Stem -->
    <path d="M 115 256 L 385 256" />
    <!-- Branching Arc -->
    <path d="M 365 145 C 285 145, 235 180, 235 256 C 235 332, 285 367, 365 367" />
  </g>
</svg>
'''

    # Write SVG files
    icon_svg_path = os.path.join(repo_dir, "assets/icon.svg")
    logo_svg_path = os.path.join(repo_dir, "logo.svg")
    
    with open(icon_svg_path, "w") as f:
        f.write(svg_content)
    with open(logo_svg_path, "w") as f:
        f.write(svg_content)
    print("Updated assets/icon.svg and logo.svg")

    # Render PNG using macOS qlmanage
    subprocess.run(["qlmanage", "-t", "-s", "512", "-o", "/tmp", icon_svg_path], check=True)
    rendered_png = "/tmp/icon.svg.png"
    icon_png_path = os.path.join(repo_dir, "assets/icon.png")
    
    # Ensure exact 512x512 RGBA
    png_img = Image.open(rendered_png)
    if png_img.size != (512, 512):
        png_img = png_img.resize((512, 512), Image.Resampling.LANCZOS)
    png_img.save(icon_png_path, format="PNG")
    print(f"Saved {icon_png_path} ({png_img.size})")

if __name__ == "__main__":
    main()
