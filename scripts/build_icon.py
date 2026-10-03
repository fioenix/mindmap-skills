#!/usr/bin/env python3
import math
import os
import shutil
import subprocess
import base64
from PIL import Image

def generate_conic_background(size=512):
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
            angle_rad = math.atan2(dy, dx)
            angle_deg = math.degrees(angle_rad)
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
    repo_dir = "/Users/fioenix/Projects/mindmap-skills"
    bg_img = generate_conic_background(512)
    bg_path = "/tmp/fn_conic_bg.png"
    bg_img.save(bg_path, format="PNG")
    
    with open(bg_path, "rb") as f:
        bg_b64 = base64.b64encode(f.read()).decode("utf-8")

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <!-- Squircle shape clipping -->
    <clipPath id="squircle-clip">
      <rect x="0" y="0" width="512" height="512" rx="108" ry="108" />
    </clipPath>
    <!-- Soft shadow for 3D elevation on iridescent ground -->
    <filter id="crisp-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#0B0B17" flood-opacity="0.28" />
    </filter>
  </defs>

  <!-- Background: FINOLABS Signature Iridescent Conic Swirl -->
  <g clip-path="url(#squircle-clip)">
    <image href="data:image/png;base64,{bg_b64}" width="512" height="512" preserveAspectRatio="none" />
    <!-- Fine inner highlight border -->
    <rect x="2" y="2" width="508" height="508" rx="106" ry="106" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-opacity="0.55" />
  </g>

  <!-- Foreground: Mindmap Hierarchy (Pure White with Depth) -->
  <g filter="url(#crisp-shadow)">
    <!-- Connecting Branches -->
    <g fill="none" stroke="#FFFFFF" stroke-linecap="round" stroke-linejoin="round">
      <!-- Top Right Branch System -->
      <path d="M 288 226 C 340 226, 345 152, 388 152" stroke-width="14" />
      <path d="M 416 152 C 438 152, 442 110, 458 110" stroke-width="9" />
      <path d="M 416 152 C 438 152, 442 194, 458 194" stroke-width="9" />

      <!-- Bottom Right Branch System -->
      <path d="M 288 286 C 340 286, 345 360, 388 360" stroke-width="14" />
      <path d="M 416 360 C 438 360, 442 318, 458 318" stroke-width="9" />
      <path d="M 416 360 C 438 360, 442 402, 458 402" stroke-width="9" />

      <!-- Top Left Branch System -->
      <path d="M 224 226 C 172 226, 167 152, 124 152" stroke-width="14" />
      <path d="M 96 152 C 74 152, 70 110, 54 110" stroke-width="9" />
      <path d="M 96 152 C 74 152, 70 194, 54 194" stroke-width="9" />

      <!-- Bottom Left Branch System -->
      <path d="M 224 286 C 172 286, 167 360, 124 360" stroke-width="14" />
      <path d="M 96 360 C 74 360, 70 318, 54 318" stroke-width="9" />
      <path d="M 96 360 C 74 360, 70 402, 54 402" stroke-width="9" />
    </g>

    <!-- Sub-nodes (Pill Capsules) -->
    <rect x="372" y="139" width="50" height="26" rx="13" fill="#FFFFFF" />
    <rect x="372" y="347" width="50" height="26" rx="13" fill="#FFFFFF" />
    <rect x="90" y="139" width="50" height="26" rx="13" fill="#FFFFFF" />
    <rect x="90" y="347" width="50" height="26" rx="13" fill="#FFFFFF" />

    <!-- Leaf Nodes (Dots) -->
    <circle cx="458" cy="110" r="11" fill="#FFFFFF" />
    <circle cx="458" cy="194" r="11" fill="#FFFFFF" />
    <circle cx="458" cy="318" r="11" fill="#FFFFFF" />
    <circle cx="458" cy="402" r="11" fill="#FFFFFF" />

    <circle cx="54" cy="110" r="11" fill="#FFFFFF" />
    <circle cx="54" cy="194" r="11" fill="#FFFFFF" />
    <circle cx="54" cy="318" r="11" fill="#FFFFFF" />
    <circle cx="54" cy="402" r="11" fill="#FFFFFF" />

    <!-- Central Root Node: FINOLABS Primary Mark Framing -->
    <rect x="204" y="204" width="104" height="104" rx="26" fill="#FFFFFF" />
    <rect x="220" y="220" width="72" height="72" rx="18" fill="#0B0B17" />

    <!-- FINO Phoenix 3-Flame Crest (Geometric Mini) -->
    <!-- Left plume: Mint #7FE2CE -->
    <path d="M 239 268 C 233 252, 235 240, 241 238 C 247 242, 247 258, 243 268 Z" fill="#7FE2CE" />
    <!-- Center plume: Violet #9750C4 -->
    <path d="M 256 268 C 251 244, 258 232, 265 235 C 270 246, 267 261, 261 268 Z" fill="#9750C4" />
    <!-- Right plume: Teal #87D3E1 -->
    <path d="M 273 268 C 273 252, 279 244, 283 248 C 283 258, 279 268, 275 270 Z" fill="#87D3E1" />
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
