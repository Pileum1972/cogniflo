# -*- coding: utf-8 -*-
"""The Digital CI Feedback Loop — five stages, as a light panel for the dark page.

Content is Guy's own framework (Digital_CI_Feedback_Loop1.pdf), informed by
The Hackett Group's research on smart automation and advanced analytics. That
attribution travels with the diagram — it is on the panel, not just in a note.

Colour does real work here: step 4 is amber because it is the step the argument
turns on ("most organizations stop at automation"). Every other step is blue.
Two colours only, validated:
  #2f6bff ↔ #d97706  ΔE 33.0 protan, 38.7 normal — all six checks pass.
Each step also carries its number and name, so colour is never the only channel.
"""

INK      = "#0f172a"
INK_SOFT = "#475569"
INK_MUTE = "#94a3b8"
RULE     = "#e2e8f0"
BLUE     = "#2f6bff"
AMBER    = "#d97706"

FONT = "Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif"

STEPS = [
    ("1", "DISCOVER",  "Process X-Ray",                 "DISCOVERY",
     ["Value stream mapping", "Current-state visualization",
      "Digital twin simulation", "End-to-end flow analysis"], False),
    ("2", "ANALYZE",   "Process Mining &amp; Intelligence", "INTELLIGENCE",
     ["Process mining (event logs)", "Task mining (user activity)",
      "Bottleneck &amp; root cause", "Predictive models"], False),
    ("3", "AUTOMATE",  "Process Automation",            "AUTOMATION",
     ["Robotic Process Automation", "Smart data capture",
      "Cognitive automation", "Agile orchestration"], False),
    ("4", "ENGAGE",    "CI Improvement",                "HUMAN LAYER",
     ["Digital suggestion boards", "Idea voting &amp; clustering",
      "Employee pulse feedback", "Gamified recognition"], True),
    ("5", "REFINE",    "Improved Business Rules",       "OPTIMIZATION",
     ["Updated decision logic", "Refined workflow routing",
      "Adaptive bot parameters", "New process standards"], False),
]

BOX_W, BOX_H = 210.0, 74.0
LEFT, GAP = 30.0, 32.5
TOP = 92.0


def _centres():
    return [LEFT + BOX_W / 2 + i * (BOX_W + GAP) for i in range(len(STEPS))]


def loop_svg():
    cx = _centres()
    out = []

    # ---- connecting arrows between the step boxes -------------------------
    for i in range(len(STEPS) - 1):
        x1 = cx[i] + BOX_W / 2
        x2 = cx[i + 1] - BOX_W / 2
        out.append(
            f'<line x1="{x1:.1f}" y1="{TOP + BOX_H/2:.1f}" x2="{x2 - 9:.1f}" '
            f'y2="{TOP + BOX_H/2:.1f}" stroke="{BLUE}" stroke-width="2" '
            f'marker-end="url(#loopArrow)"/>')

    # ---- step boxes + detail columns --------------------------------------
    for i, (num, title, sub, group, bullets, accent) in enumerate(STEPS):
        c = cx[i]
        colour = AMBER if accent else BLUE
        fill = "#fffbeb" if accent else "#eef4ff"
        x = c - BOX_W / 2

        out.append(
            f'<rect x="{x:.1f}" y="{TOP}" width="{BOX_W}" height="{BOX_H}" rx="9" '
            f'fill="{fill}" stroke="{colour}" stroke-width="1.6"/>')
        out.append(
            f'<text x="{x + 15:.1f}" y="{TOP + 23:.1f}" font-family="{FONT}" '
            f'font-size="10.5" font-weight="700" letter-spacing="1.1" '
            f'fill="{colour}">STEP {num} · {title}</text>')
        # long labels shrink rather than run into the connecting arrow
        fsz = 13.0 if len(sub) > 22 else 14.5
        out.append(
            f'<text x="{x + 15:.1f}" y="{TOP + 50:.1f}" font-family="{FONT}" '
            f'font-size="{fsz}" font-weight="600" fill="{INK}">{sub}</text>')

        # group label + rule
        gy = TOP + BOX_H + 44
        out.append(
            f'<text x="{x:.1f}" y="{gy}" font-family="{FONT}" font-size="10" '
            f'font-weight="700" letter-spacing="1.2" fill="{colour}">{group}</text>')
        out.append(
            f'<line x1="{x:.1f}" y1="{gy + 9:.1f}" x2="{x + BOX_W:.1f}" '
            f'y2="{gy + 9:.1f}" stroke="{RULE}" stroke-width="1"/>')

        by = gy + 30
        for b in bullets:
            out.append(
                f'<text x="{x:.1f}" y="{by}" font-family="{FONT}" font-size="11.5" '
                f'fill="{INK_SOFT}">{b}</text>')
            by += 21

    # ---- the return path: step 5 back to step 1 --------------------------
    # Routed around the OUTSIDE of the detail columns. An earlier version ran the
    # riser straight down the middle of column 1 and struck through four lines of
    # its text — the kind of collision only a render reveals.
    ry = 350.0
    mid_y = TOP + BOX_H / 2
    x_out_r, x_out_l = 1224.0, 16.0
    r_edge = cx[-1] + BOX_W / 2
    l_edge = cx[0] - BOX_W / 2
    out.append(
        f'<path d="M{r_edge:.1f} {mid_y:.1f} L{x_out_r:.1f} {mid_y:.1f} '
        f'L{x_out_r:.1f} {ry:.1f} L{x_out_l:.1f} {ry:.1f} '
        f'L{x_out_l:.1f} {mid_y:.1f} L{l_edge - 9:.1f} {mid_y:.1f}" '
        f'fill="none" stroke="{BLUE}" stroke-width="2" stroke-dasharray="7 5" '
        f'marker-end="url(#loopArrow)"/>')
    out.append(
        f'<rect x="502" y="{ry - 15:.1f}" width="236" height="30" rx="15" '
        f'fill="#ffffff" stroke="{RULE}" stroke-width="1"/>')
    out.append(
        f'<text x="620" y="{ry + 5:.1f}" text-anchor="middle" '
        f'font-family="{FONT}" font-size="11.5" font-weight="700" letter-spacing="1.1" '
        f'fill="{BLUE}">CONTINUOUS FEEDBACK LOOP</text>')

    # ---- the argument, on the panel --------------------------------------
    out.append(
        f'<text x="{LEFT}" y="412" font-family="{FONT}" font-size="12.5" '
        f'fill="{INK}"><tspan font-weight="700">Most organizations stop at Step 3.</tspan>'
        f'<tspan fill="{INK_SOFT}"> Step 4 captures what machines cannot see — the friction,</tspan></text>')
    out.append(
        f'<text x="{LEFT}" y="431" font-family="{FONT}" font-size="12.5" '
        f'fill="{INK_SOFT}">workarounds and ideas only the people closest to the work can surface.</text>')
    out.append(
        f'<text x="{LEFT}" y="458" font-family="{FONT}" font-size="10.5" '
        f'fill="{INK_MUTE}">Framework informed by The Hackett Group&#8217;s research on '
        f'smart automation &amp; advanced analytics.</text>')

    body = "\n  ".join(out)
    return f'''<svg viewBox="0 0 1240 478" role="img" xmlns="http://www.w3.org/2000/svg"
     aria-label="The Digital CI Feedback Loop. Five stages run left to right: step one Discover,
     the Process X-Ray, covering value stream mapping, current-state visualization, digital twin
     simulation and end-to-end flow analysis. Step two Analyze, process mining and intelligence,
     covering process mining of event logs, task mining of user activity, bottleneck and root
     cause analysis and predictive models. Step three Automate, process automation, covering
     robotic process automation, smart data capture, cognitive automation and agile orchestration.
     Step four Engage, highlighted as the pivotal human layer, covering digital suggestion boards,
     idea voting and clustering, employee pulse feedback and gamified recognition. Step five
     Refine, improved business rules, covering updated decision logic, refined workflow routing,
     adaptive bot parameters and new process standards. A dashed continuous feedback loop returns
     from step five to step one. Most organizations stop at step three; step four captures what
     machines cannot see.">
  <defs>
    <marker id="loopArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0 0 L10 5 L0 10 z" fill="{BLUE}"/>
    </marker>
  </defs>
  <text x="{LEFT}" y="38" font-family="{FONT}" font-size="10.5" font-weight="700"
        letter-spacing="1.3" fill="{INK_MUTE}">DIGITAL CONTINUOUS IMPROVEMENT</text>
  <text x="{LEFT}" y="68" font-family="{FONT}" font-size="21" font-weight="700"
        letter-spacing="-.4" fill="{INK}">The Digital CI Feedback Loop</text>
  {body}
</svg>'''


if __name__ == "__main__":
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    svg = loop_svg()
    with open(os.path.join(here, "loop-preview.svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote loop-preview.svg", len(svg), "bytes")
