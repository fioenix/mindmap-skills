#!/usr/bin/env python3
import os
import subprocess
from PIL import Image

def generate_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <!-- Apple / FINOLABS standard squircle -->
    <clipPath id="squircle-clip">
      <rect x="0" y="0" width="512" height="512" rx="112" ry="112" />
    </clipPath>

    <!-- FINOLABS Signature Iridescent Gradient (pure vector linear) -->
    <linearGradient id="fn-iridescent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#BFE9C6" />
      <stop offset="28%" stop-color="#87D3E1" />
      <stop offset="68%" stop-color="#C9A8E5" />
      <stop offset="100%" stop-color="#9750C4" />
    </linearGradient>

    <!-- Elevation drop shadow per FINOLABS shadow-xl token -->
    <filter id="ink-elevation" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#0B0B17" flood-opacity="0.22" />
    </filter>
  </defs>

  <g clip-path="url(#squircle-clip)">
    <!-- Surface: FINOLABS Iridescent Gradient -->
    <rect width="512" height="512" fill="url(#fn-iridescent)" />

    <!-- Foreground: Precision Architectural Mindmap in Lab Ink (#0B0B17) -->
    <g filter="url(#ink-elevation)">
      <!-- Branches (Strokes) -->
      <g fill="none" stroke="#0B0B17" stroke-linecap="round" stroke-linejoin="round">
        <!-- Main Branch 1 (Top) -->
        <path d="M 135 256 C 210 256, 220 156, 305 156 L 320 156" stroke-width="18" />
        <path d="M 320 156 C 355 156, 365 112, 390 112 L 415 112" stroke-width="12" />
        <path d="M 320 156 C 355 156, 365 184, 390 184 L 415 184" stroke-width="12" />

        <!-- Main Branch 2 (Middle) -->
        <path d="M 135 256 L 335 256" stroke-width="18" />
        <path d="M 335 256 L 415 256" stroke-width="12" />

        <!-- Main Branch 3 (Bottom) -->
        <path d="M 135 256 C 210 256, 220 356, 305 356 L 320 356" stroke-width="18" />
        <path d="M 320 356 C 355 356, 365 328, 390 328 L 415 328" stroke-width="12" />
        <path d="M 320 356 C 355 356, 365 400, 390 400 L 415 400" stroke-width="12" />
      </g>

      <!-- Nodes -->
      <!-- Root Node (Major Hub) -->
      <circle cx="135" cy="256" r="28" fill="#0B0B17" />
      <circle cx="135" cy="256" r="11" fill="#FFFFFF" />

      <!-- Level 1 Nodes (Junctions) -->
      <circle cx="320" cy="156" r="18" fill="#0B0B17" />
      <circle cx="320" cy="156" r="7.5" fill="#FFFFFF" />

      <circle cx="335" cy="256" r="18" fill="#0B0B17" />
      <circle cx="335" cy="256" r="7.5" fill="#FFFFFF" />

      <circle cx="320" cy="356" r="18" fill="#0B0B17" />
      <circle cx="320" cy="356" r="7.5" fill="#FFFFFF" />

      <!-- Level 2 Leaf Terminals (Solid Dots) -->
      <circle cx="415" cy="112" r="11" fill="#0B0B17" />
      <circle cx="415" cy="184" r="11" fill="#0B0B17" />
      <circle cx="415" cy="256" r="11" fill="#0B0B17" />
      <circle cx="415" cy="328" r="11" fill="#0B0B17" />
      <circle cx="415" cy="400" r="11" fill="#0B0B17" />
    </g>
  </g>
</svg>
'''

def main():
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    svg_content = generate_svg()

    # Write SVG files (assets/icon.svg and logo.svg)
    icon_svg_path = os.path.join(repo_dir, "assets/icon.svg")
    logo_svg_path = os.path.join(repo_dir, "logo.svg")
    
    with open(icon_svg_path, "w") as f:
        f.write(svg_content)
    with open(logo_svg_path, "w") as f:
        f.write(svg_content)
    print("Updated assets/icon.svg and logo.svg (pure vector SVG)")

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
