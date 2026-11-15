# -*- coding: utf-8 -*-
"""Illustrative Process X-Ray artefacts.

These are LIGHT panels that sit on the dark page, so they read as product
output rather than decoration — the same device OFI uses on its Solutions page.

IMPORTANT: every number here is fabricated for illustration. Nothing in this
file is client data, and the panels are labelled as samples on the page. That
labelling is not optional — it is the difference between demonstrating
capability and inventing a result.

Palette (validated, light surface, see dataviz validator):
  #2f6bff  normal flow / within terms   — ΔE 39.1 normal, 32.0 protan vs red
  #dc2626  rework loop / past due
Both marks also carry text labels, so identity is never colour alone.
"""

INK      = "#0f172a"
INK_SOFT = "#475569"
INK_MUTE = "#94a3b8"
GRID     = "#e2e8f0"
BLUE     = "#2f6bff"
RED      = "#dc2626"
PANEL    = "#ffffff"

FONT = "Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif"


# ---------------------------------------------------------------------------
# 1. Discovered process map — order to cash
# ---------------------------------------------------------------------------
def _node(cx, cy, label, sub, w=158, h=54, colour=BLUE, faded=False):
    x, y = cx - w / 2, cy - h / 2
    stroke = colour if not faded else RED
    fill = "#eef4ff" if not faded else "#fef2f2"
    return f'''<g>
  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>
  <text x="{cx}" y="{cy - 3}" text-anchor="middle" font-family="{FONT}" font-size="14"
        font-weight="600" fill="{INK}">{label}</text>
  <text x="{cx}" y="{cy + 15}" text-anchor="middle" font-family="{FONT}" font-size="11.5"
        fill="{INK_MUTE}">{sub}</text>
</g>'''


def _loop(cx, top_y, bot_y, label, sub, note):
    """A clean rework loop: down the left side, back up the right.
    Symmetrical geometry reads instantly; crossing curves do not."""
    lx, rx = cx - 42, cx + 42
    return "\n  ".join([
        f'<path d="M{lx} {top_y} C {lx - 34} {top_y + 46}, {lx - 34} {bot_y - 46}, {lx} {bot_y - 9}" '
        f'fill="none" stroke="{RED}" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowRed)"/>',
        f'<path d="M{rx} {bot_y} C {rx + 34} {bot_y - 46}, {rx + 34} {top_y + 46}, {rx} {top_y + 9}" '
        f'fill="none" stroke="{RED}" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowRed)"/>',
        _node(cx, (top_y + bot_y) / 2 + 24, label, sub, faded=True),
        f'<text x="{cx}" y="{bot_y + 32}" text-anchor="middle" font-family="{FONT}" '
        f'font-size="12.5" font-weight="600" fill="{RED}">{note}</text>',
    ])


def process_map_svg():
    nodes = [
        (105, 120, "Order Received", "47,312 cases"),
        (315, 120, "Credit Check", "47,312 · 1.2d"),
        (525, 120, "Order Confirmed", "47,312 · 0.6d"),
        (735, 120, "Fulfilled", "46,988 · 9.4d"),
        (945, 120, "Invoice Issued", "46,988 · 2.1d"),
        (1150, 120, "Payment Received", "44,109 · 61%"),
    ]
    out = []

    edge_labels = ["1.2d", "0.6d", "9.4d", "2.1d", "25.1d"]
    for i in range(len(nodes) - 1):
        x1 = nodes[i][0] + 79
        x2 = nodes[i + 1][0] - 79
        out.append(f'<line x1="{x1}" y1="120" x2="{x2 - 9}" y2="120" stroke="{BLUE}" '
                   f'stroke-width="2" marker-end="url(#arrowBlue)"/>')
        out.append(f'<text x="{(x1 + x2) / 2:.0f}" y="110" text-anchor="middle" font-family="{FONT}" '
                   f'font-size="11.5" fill="{INK_MUTE}">{edge_labels[i]}</text>')

    for cx, cy, label, sub in nodes:
        out.append(_node(cx, cy, label, sub))

    out.append(_loop(315, 147, 262, "Order Amended", "8,516 · 4.7d",
                     "rework · 18% of orders"))
    out.append(_loop(945, 147, 262, "Dispute Review", "6,578 · 21.3d",
                     "rework · 14% of invoices, +21 days"))

    out.append(f'<text x="620" y="352" text-anchor="middle" font-family="{FONT}" font-size="12.5" '
               f'fill="{INK_SOFT}">Average end-to-end cycle <tspan font-weight="700" fill="{INK}">'
               f'38.4 days</tspan> against a 21-day standard</text>')

    body = "\n  ".join(out)
    return f'''<svg viewBox="0 0 1240 380" role="img" xmlns="http://www.w3.org/2000/svg"
     aria-label="Illustrative discovered process map for order to cash. The main flow runs from
     order received through credit check, order confirmation, fulfilment and invoicing to payment,
     averaging 38.4 days. Two rework loops are highlighted: order amendment affecting 18 percent of
     orders, and dispute review affecting 14 percent of invoices and adding 21 days each.">
  <defs>
    <marker id="arrowBlue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0 0 L10 5 L0 10 z" fill="{BLUE}"/>
    </marker>
    <marker id="arrowRed" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0 0 L10 5 L0 10 z" fill="{RED}"/>
    </marker>
  </defs>
  {body}
</svg>'''


# ---------------------------------------------------------------------------
# 2. Invoice ageing — horizontal bars
# ---------------------------------------------------------------------------
def ageing_svg():
    rows = [
        ("0–30 days",   6820, "$12.4M", False),
        ("31–60 days",  2940, "$5.1M",  False),
        ("61–90 days",  1180, "$2.6M",  False),
        ("91–180 days",  640, "$2.9M",  True),
        ("180+ days",         213, "$1.3M",  True),
    ]
    mx = max(r[1] for r in rows)
    x0, w_max = 132, 330
    out = []

    # recessive gridlines
    for i in range(1, 5):
        gx = x0 + w_max * i / 4
        out.append(f'<line x1="{gx:.1f}" y1="80" x2="{gx:.1f}" y2="290" stroke="{GRID}" stroke-width="1"/>')

    y = 96
    for label, n, val, bad in rows:
        w = max(4, w_max * n / mx)
        c = RED if bad else BLUE
        out.append(f'<text x="118" y="{y + 17}" text-anchor="end" font-family="{FONT}" '
                   f'font-size="13" fill="{INK_SOFT}">{label}</text>')
        out.append(f'<rect x="{x0}" y="{y}" width="{w:.1f}" height="24" rx="4" fill="{c}"/>')
        out.append(f'<text x="{x0 + w + 12:.1f}" y="{y + 17}" font-family="{FONT}" font-size="13" '
                   f'font-weight="600" fill="{INK}">{n:,}</text>')
        out.append(f'<text x="{x0 + w + 74:.1f}" y="{y + 17}" font-family="{FONT}" font-size="12.5" '
                   f'fill="{INK_MUTE}">{val}</text>')
        y += 42

    body = "\n  ".join(out)
    return f'''<svg viewBox="0 0 620 330" role="img" xmlns="http://www.w3.org/2000/svg"
     aria-label="Illustrative open invoices by age. 0 to 30 days: 6,820 invoices worth 12.4 million
     dollars. 31 to 60 days: 2,940 worth 5.1 million. 61 to 90 days: 1,180 worth 2.6 million.
     91 to 180 days: 640 worth 2.9 million, past due. 180 days and over: 213 worth 1.3 million,
     past due. 4.2 million dollars sits beyond 90 days.">
  <g font-family="{FONT}">
    <rect x="0" y="24" width="13" height="13" rx="3" fill="{BLUE}"/>
    <text x="20" y="35" font-size="12.5" fill="{INK_SOFT}">Within terms</text>
    <rect x="128" y="24" width="13" height="13" rx="3" fill="{RED}"/>
    <text x="148" y="35" font-size="12.5" fill="{INK_SOFT}">Past due 90+ days</text>
    <text x="0" y="66" font-size="12" fill="{INK_MUTE}">OPEN INVOICES</text>
  </g>
  {body}
</svg>'''


# ---------------------------------------------------------------------------
# 3. Headline findings — stat tiles (a number, not a chart)
# ---------------------------------------------------------------------------
TILES = [
    ("214", "process variants discovered", "against 1 documented"),
    ("61%", "of orders follow the happy path", "39% deviate at least once"),
    ("38.4d", "average order-to-cash cycle", "against a 21-day standard"),
    ("$4.2M", "invoiced value beyond 90 days", "1.9M of it past 180"),
]


def tiles_html():
    out = ""
    for n, label, sub in TILES:
        out += (f'<div class="xr-tile"><div class="xr-n">{n}</div>'
                f'<div class="xr-l">{label}</div><div class="xr-s">{sub}</div></div>')
    return out


# ---------------------------------------------------------------------------
CSS = """
/* ---------- Process X-Ray artefact panels ----------
   Light panels on the dark page so they read as product output. */
.xr-panel{
  background:#fff;border-radius:14px;overflow:hidden;
  box-shadow:0 30px 60px -30px rgba(0,0,0,.9), 0 0 0 1px rgba(255,255,255,.06);
}
.xr-bar{
  display:flex;align-items:center;gap:10px;
  padding:13px 18px;background:#f1f5f9;border-bottom:1px solid #e2e8f0;
}
.xr-dot{width:10px;height:10px;border-radius:50%;background:#cbd5e1;flex:0 0 auto;}
.xr-title{
  font-family:'Inter',sans-serif;font-size:.82rem;font-weight:600;color:#334155;
  letter-spacing:.01em;margin-left:6px;
}
.xr-tag{
  margin-left:auto;font-size:.66rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
  color:#64748b;background:#e2e8f0;border-radius:4px;padding:4px 8px;
}
.xr-body{padding:22px 20px 24px;}
.xr-body svg{width:100%;height:auto;display:block;}

.xr-tiles{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0;}
.xr-tile:nth-child(-n+2){border-bottom:1px solid #e2e8f0;}
.xr-tile:nth-child(2n){border-right:none;}
.xr-tile{padding:20px 22px;border-right:1px solid #e2e8f0;}
.xr-tile:last-child{border-right:none;}
@media (max-width:520px){
  .xr-tiles{grid-template-columns:1fr;}
  .xr-tile{border-right:none;border-bottom:1px solid #e2e8f0;}
  .xr-tile:last-child{border-bottom:none;}
}
.xr-n{font-family:'Poppins',sans-serif;font-size:1.9rem;font-weight:700;color:#0f172a;
  letter-spacing:-.03em;line-height:1;}
.xr-l{font-size:.86rem;color:#334155;margin-top:9px;line-height:1.4;font-weight:500;}
.xr-s{font-size:.78rem;color:#94a3b8;margin-top:5px;line-height:1.4;}

.xr-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:24px;margin-top:24px;}
@media (max-width:860px){.xr-grid{grid-template-columns:1fr;}}

.xr-note{
  margin-top:22px;font-size:.86rem;color:var(--ink-muted);
  display:flex;gap:10px;align-items:flex-start;
}
.xr-note svg{width:16px;height:16px;flex:0 0 auto;margin-top:3px;color:var(--ink-muted);}
"""
