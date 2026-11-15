# -*- coding: utf-8 -*-
"""One-page Process X-Ray leave-behind (PDF).

Deliberately LIGHT rather than matching the dark site: this is a document
people print, forward and mark up. A dark background burns ink and photocopies
badly, which is the wrong trade for a leave-behind.
"""
import math
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

INK   = HexColor("#0f172a")
SOFT  = HexColor("#475569")
MUTE  = HexColor("#94a3b8")
BLUE  = HexColor("#2f6bff")
RULE  = HexColor("#e2e8f0")
TINT  = HexColor("#eef4ff")

W, H = letter
M = 0.82 * inch


def _logo(c, cx, cy, r=13):
    """The node-ring mark, drawn with primitives (same idea as art.py)."""
    pts = []
    for a in range(40, 321, 28):
        rad = math.radians(a)
        pts.append((cx + r * math.cos(rad), cy + r * math.sin(rad)))
    c.setStrokeColor(BLUE)
    c.setLineWidth(1.5)
    c.setLineCap(1)
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        c.line(x1, y1, x2, y2)
    c.setFillColor(BLUE)
    for i, (x, y) in enumerate(pts):
        rr = 2.5 if i in (0, 5, 10) else 1.8
        c.circle(x, y, rr, stroke=0, fill=1)


def _wrap(c, text, x, y, width, font="Helvetica", size=10, leading=14, colour=SOFT):
    c.setFont(font, size)
    c.setFillColor(colour)
    words, line = text.split(), ""
    for w in words:
        t = (line + " " + w).strip()
        if c.stringWidth(t, font, size) <= width:
            line = t
        else:
            c.drawString(x, y, line)
            y -= leading
            line = w
    if line:
        c.drawString(x, y, line)
        y -= leading
    return y


def build(path, email="hello@cogniflo.com", site="cogniflo.com"):
    c = canvas.Canvas(path, pagesize=letter)
    c.setTitle("The Process X-Ray — CogniFlo")
    c.setAuthor("CogniFlo Consulting Group")
    c.setSubject("A two-week, fixed-fee process diagnostic")

    # ---------- header ----------
    _logo(c, M + 13, H - M - 6)
    c.setFont("Helvetica-Bold", 15)
    c.setFillColor(INK)
    c.drawString(M + 36, H - M - 4, "CogniFlo")
    c.setFont("Helvetica", 7.2)
    c.setFillColor(MUTE)
    c.drawString(M + 36, H - M - 15, "C O N S U L T I N G   G R O U P")

    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 8)
    c.drawRightString(W - M, H - M - 8, "TWO WEEKS · FIXED FEE")

    y = H - M - 52
    c.setStrokeColor(RULE); c.setLineWidth(1)
    c.line(M, y, W - M, y)

    # ---------- title ----------
    y -= 46
    c.setFont("Helvetica-Bold", 30)
    c.setFillColor(INK)
    c.drawString(M, y, "The Process X-Ray")
    y -= 24
    c.setFont("Helvetica", 13)
    c.setFillColor(BLUE)
    c.drawString(M, y, "What your process actually does — read from your own data.")

    y -= 30
    y = _wrap(c, "Most improvement programmes start with a workshop where people describe the "
                 "process from memory. We start with your event log. In two weeks we map what "
                 "genuinely happens across one end-to-end process, quantify what the deviations "
                 "cost, and tell you what is worth automating — and what is not.",
              M, y, W - 2 * M, size=10.5, leading=15)

    # ---------- three steps ----------
    y -= 16
    c.setFillColor(TINT)
    c.rect(M, y - 96, W - 2 * M, 96, stroke=0, fill=1)
    colw = (W - 2 * M) / 3
    steps = [
        ("01  EXTRACT", "Days 1–3", "We pull the event log from your ERP or workflow system. "
                                    "No new tooling for your team to run."),
        ("02  DISCOVER", "Days 4–8", "We map every variant, not the idealised one — including "
                                     "the rework loops nobody documented."),
        ("03  QUANTIFY", "Days 9–10", "We attach cost and cycle time to each deviation and rank "
                                      "them by what they are worth fixing."),
    ]
    for i, (head, when, body) in enumerate(steps):
        x = M + 16 + i * colw
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(BLUE)
        c.drawString(x, y - 22, head)
        c.setFont("Helvetica", 8)
        c.setFillColor(MUTE)
        c.drawString(x, y - 34, when)
        _wrap(c, body, x, y - 50, colw - 30, size=8.6, leading=11.5)
    y -= 118

    # ---------- deliverables ----------
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(INK)
    c.drawString(M, y, "What lands on your desk")
    y -= 20

    items = [
        ("The as-is process, mapped from system data",
         "Every path, with volumes and durations — not a whiteboard sketch."),
        ("Waste and delay quantified in cost and cycle time",
         "Each deviation carries a number your finance team recognises."),
        ("A prioritised improvement roadmap",
         "Sequenced by return, with the effort behind each item made explicit."),
        ("A clear automation verdict",
         "Which steps are stable enough to automate, and which would only scale the waste."),
    ]
    for title, sub in items:
        c.setFillColor(BLUE)
        c.circle(M + 3.5, y + 3.5, 3.2, stroke=0, fill=1)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(INK)
        c.drawString(M + 15, y, title)
        c.setFont("Helvetica", 9.2)
        c.setFillColor(SOFT)
        c.drawString(M + 15, y - 13, sub)
        y -= 33

    # ---------- who it's for ----------
    y -= 6
    c.setStrokeColor(RULE)
    c.line(M, y, W - M, y)
    y -= 24
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(INK)
    c.drawString(M, y, "Who it is for")
    y -= 15
    y = _wrap(c, "Mid-to-large enterprises in healthcare and life sciences, financial services, "
                 "insurance, and manufacturing — where the process is intricate, the data is "
                 "abundant, and a decade of workarounds has quietly accumulated. Usually "
                 "commissioned by a CFO, COO, or the head of transformation, CI or shared services.",
              M, y, W - 2 * M, size=9.6, leading=13.5)

    # ---------- footer / CTA ----------
    fy = M + 58
    c.setFillColor(HexColor("#0b1220"))
    c.rect(M, M - 6, W - 2 * M, 64, stroke=0, fill=1)
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(HexColor("#ffffff"))
    c.drawString(M + 20, fy - 22, "What is the one process costing you the most?")
    c.setFont("Helvetica", 9.4)
    c.setFillColor(HexColor("#b8c4dc"))
    c.drawString(M + 20, fy - 38, "Tell us about it and we will tell you what we would look at first.")
    c.setFont("Helvetica-Bold", 9.6)
    c.setFillColor(HexColor("#6f9bff"))
    c.drawRightString(W - M - 20, fy - 22, email)
    c.setFont("Helvetica", 9)
    c.drawRightString(W - M - 20, fy - 38, site)

    c.setFont("Helvetica", 7.4)
    c.setFillColor(MUTE)
    c.drawString(M, M - 20, "Don't automate waste — eliminate it first.")
    c.drawRightString(W - M, M - 20, "CogniFlo Consulting Group")

    c.showPage()
    c.save()
    return path
