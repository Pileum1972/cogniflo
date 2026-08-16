# -*- coding: utf-8 -*-
"""Generated SVG artwork — hero background and logo mark.

These are vector, a few KB each, and inlined as data URIs so every page stays
self-contained. Nothing here depends on a stock photo licence.
"""
import math
import base64


# ---------------------------------------------------------------- hero mesh
def hero_svg(R=46):
    """Dark hexagonal-mesh field with perspective, glow curves and light bloom."""
    tw = math.sqrt(3) * R           # lattice width
    th = 3 * R                      # lattice vertical period

    def hexpath(cx, cy):
        pts = []
        for a in (90, 150, 210, 270, 330, 30):
            r = math.radians(a)
            pts.append((cx + R * math.cos(r), cy - R * math.sin(r)))
        return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + "Z"

    centres = [(0, 0), (tw, 0), (0, th), (tw, th),
               (tw / 2, 1.5 * R), (tw / 2, 1.5 * R - th), (tw / 2, 1.5 * R + th)]
    hexes = "".join(f'<path d="{hexpath(cx, cy)}"/>' for cx, cy in centres)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice">
<defs>
  <linearGradient id="base" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0d1b33"/>
    <stop offset="0.45" stop-color="#0a1226"/>
    <stop offset="1" stop-color="#05070f"/>
  </linearGradient>
  <pattern id="hex" width="{tw:.2f}" height="{th:.2f}" patternUnits="userSpaceOnUse">
    <g fill="none" stroke="#7fd8e8" stroke-width="1.1" stroke-opacity="0.16">{hexes}</g>
  </pattern>
  <radialGradient id="glowA" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#3fe0d0" stop-opacity="0.30"/>
    <stop offset="1" stop-color="#3fe0d0" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="glowB" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#7b4dff" stop-opacity="0.34"/>
    <stop offset="1" stop-color="#7b4dff" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="glowC" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#2f6bff" stop-opacity="0.26"/>
    <stop offset="1" stop-color="#2f6bff" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="wire1" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#3fe0d0" stop-opacity="0"/>
    <stop offset="0.25" stop-color="#7ff0e4" stop-opacity="0.95"/>
    <stop offset="0.75" stop-color="#3fe0d0" stop-opacity="0.55"/>
    <stop offset="1" stop-color="#3fe0d0" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="wire2" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#7b4dff" stop-opacity="0"/>
    <stop offset="0.45" stop-color="#b79bff" stop-opacity="0.75"/>
    <stop offset="1" stop-color="#7b4dff" stop-opacity="0"/>
  </linearGradient>
  <filter id="soft" x="-30%" y="-120%" width="160%" height="340%">
    <feGaussianBlur stdDeviation="9"/>
  </filter>
  <filter id="softer" x="-30%" y="-120%" width="160%" height="340%">
    <feGaussianBlur stdDeviation="22"/>
  </filter>
</defs>

<rect width="1600" height="900" fill="url(#base)"/>

<!-- mesh, thrown into perspective -->
<g transform="translate(800 470) rotate(-13) skewY(7) scale(1.5) translate(-800 -470)">
  <rect x="-500" y="-400" width="2900" height="1900" fill="url(#hex)"/>
</g>

<!-- floor light streak -->
<g opacity="0.5">
  <path d="M-60 812 L1660 700" stroke="#8fa9ff" stroke-opacity="0.55" stroke-width="2" filter="url(#soft)"/>
</g>

<!-- glowing signal traces -->
<g filter="url(#softer)" opacity="0.85">
  <path d="M-40 300 C 240 140, 420 470, 700 300 S 1180 90, 1660 250"
        fill="none" stroke="url(#wire1)" stroke-width="14"/>
</g>
<path d="M-40 300 C 240 140, 420 470, 700 300 S 1180 90, 1660 250"
      fill="none" stroke="url(#wire1)" stroke-width="3"/>

<g filter="url(#softer)" opacity="0.7">
  <path d="M-40 620 C 300 700, 520 380, 880 520 S 1320 760, 1660 610"
        fill="none" stroke="url(#wire2)" stroke-width="16"/>
</g>
<path d="M-40 620 C 300 700, 520 380, 880 520 S 1320 760, 1660 610"
      fill="none" stroke="url(#wire2)" stroke-width="2.4"/>

<!-- bloom -->
<ellipse cx="180" cy="180" rx="620" ry="470" fill="url(#glowA)"/>
<ellipse cx="1340" cy="760" rx="700" ry="520" fill="url(#glowB)"/>
<ellipse cx="900" cy="330" rx="820" ry="560" fill="url(#glowC)"/>

<!-- vignette so text always sits on something dark -->
<rect width="1600" height="900" fill="#05070f" opacity="0.30"/>
</svg>'''


# ---------------------------------------------------------------- logo mark
def logo_svg(colour="#2f6bff"):
    """A 'C' described by connected nodes — echoes the original network mark."""
    R, cx, cy = 34.0, 50.0, 50.0
    # Open ring with a gap on the right so the silhouette reads as a "C".
    # Deliberately few, chunky nodes — this has to survive at 24px in a navbar.
    angles = [40, 68, 96, 124, 152, 180, 208, 236, 264, 292, 320]
    pts = [(cx + R * math.cos(math.radians(a)), cy - R * math.sin(math.radians(a)))
           for a in angles]

    lines = ""
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        lines += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>'
    # two faint chords only — enough to suggest a network, not a cat's cradle
    for i, j in ((1, 8), (3, 10)):
        x1, y1 = pts[i]
        x2, y2 = pts[j]
        lines += (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"'
                  f' stroke-width="1.8" stroke-opacity="0.30"/>')

    nodes = ""
    for i, (x, y) in enumerate(pts):
        r = 6.4 if i in (0, 5, 10) else 4.6
        nodes += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}"/>'
    nodes += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="5.2" fill="#3fe0d0"/>'

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="CogniFlo">
  <g stroke="{colour}" stroke-width="3.4" stroke-linecap="round">{lines}</g>
  <g fill="{colour}">{nodes}</g>
</svg>'''


def data_uri(svg):
    b64 = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return f"data:image/svg+xml;base64,{b64}"


HERO_SVG = hero_svg()
HERO_URI = data_uri(HERO_SVG)
LOGO_SVG = logo_svg()
