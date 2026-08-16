# -*- coding: utf-8 -*-
"""Generate the five-page CogniFlo prototype."""
import os
from shared import (page, icon, btn, arrowlink, arrowtext, ICONS, CTA_BAND,
                    EMAIL, PHONE_DISPLAY, PHONE_HREF, LINKEDIN,
                    SITE_URL, FORM_ENDPOINT, CSS, header, FOOTER, JS)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
os.makedirs(OUT, exist_ok=True)

# =====================================================================
# Service data — single source of truth, used on home + services pages
# =====================================================================
SERVICES = [
    dict(
        slug="strategy", ico="bulb",
        name="Strategy &amp; Operating Model Design",
        tag="Vision &amp; roadmap",
        short="Establish the why and the how of transformation &mdash; before deploying any technology.",
        lede="Most transformation programmes fail on alignment, not execution. We set the destination, the governance and the measures first, so every project downstream has something to point at.",
        caps=[
            "Enterprise Transformation Vision &amp; Roadmap",
            "Lean Six Sigma Diagnostic &amp; Maturity Assessment",
            "Center of Excellence (CoE) Design",
            "Governance, KPI &amp; Operating Model Blueprint",
            "Change Management &amp; Communication Strategy (ADKAR-based)",
        ],
        outcome="A clear, aligned transformation strategy with measurable business objectives, real executive sponsorship, and sustainability designed in from day one.",
    ),
    dict(
        slug="process", ico="cog",
        name="Process Optimization &amp; Re-Engineering",
        tag="Simplify &amp; stabilise",
        short="Simplify and stabilise before you digitise, using Lean and Six Sigma.",
        lede="This is the step most programmes skip. We remove the waste, the rework and the variation first &mdash; so what you eventually automate is a process worth scaling.",
        caps=[
            "End-to-End Discovery &amp; Value Stream Mapping",
            "Cash Flow Value Stream Mapping (as-is vs future-state)",
            "Waste &amp; Variance Elimination (Lean, DMAIC)",
            "Root Cause &amp; Failure Analysis (Fishbone, 5 Whys, FMEA)",
            "Standard Work &amp; Process Capability (SPC)",
            "Future-State Process &amp; KPI Redesign",
        ],
        outcome="Efficient, standardised, capable processes delivering measurable gains in cost, quality and cycle time &mdash; and genuinely ready for digital enablement.",
    ),
    dict(
        slug="automation", ico="rocket",
        name="Intelligent Automation &amp; Digital Enablement",
        tag="Scale efficiency",
        short="Scale efficiency and intelligence across the enterprise &mdash; after optimisation.",
        lede="Once the process is stable, automation compounds instead of amplifying problems. We build the pipeline, prioritise by return, and track what each automation actually delivers.",
        caps=[
            "Robotic Process Automation (UiPath, Power Automate, Automation Anywhere)",
            "Process Mining &amp; Task Mining (Celonis, Disco, Power BI)",
            "Generative AI for Operations, Knowledge and Analytics",
            "Workflow Orchestration &amp; Integration (low-code / API)",
            "Automation Pipeline Design, Prioritisation &amp; ROI Tracking",
        ],
        outcome="Accelerated throughput, less manual handling, stronger compliance, and real-time visibility into operational performance.",
    ),
    dict(
        slug="capability", ico="users",
        name="Capability Building &amp; CoE Enablement",
        tag="Empower your people",
        short="Empower your people to sustain the change and drive the next one.",
        lede="Our aim is to make ourselves unnecessary. We build the internal capability, the playbooks and the governance that let improvement continue after we leave.",
        caps=[
            "Lean Six Sigma Training &amp; Certification (Yellow / Green / Black Belt)",
            "Digital Transformation &amp; Change Leadership Programmes",
            "RPA Developer &amp; Analyst Learning Pathways",
            "Process Mining &amp; Data Analytics Skill Development",
            "CoE Playbook &amp; Maturity Framework",
        ],
        outcome="A self-reliant organisation with certified change agents, real digital fluency, and a continuous improvement culture that holds.",
    ),
    dict(
        slug="value", ico="dollar",
        name="Financial Tracking &amp; Value Realization",
        tag="Measure the impact",
        short="Make improvement visible, measurable and financially accountable.",
        lede="If the CFO can't see it in the numbers, it didn't happen. We connect every improvement to a financial line and keep it visible quarter after quarter.",
        caps=[
            "KPI &amp; Benefits Realization Framework",
            "Transformation ROI Dashboard &amp; Reporting",
            "Quarterly CI Health Check &amp; Portfolio Review",
            "Value Capture &amp; Reinvestment Governance",
        ],
        outcome="Sustained, provable ROI and continuous alignment between business goals, digital execution and financial performance.",
    ),
    dict(
        slug="change", ico="megaphone",
        name="Change Management &amp; Communication",
        tag="Make it stick",
        short="Align stakeholders and embed sustainability from day one.",
        lede="Technically correct and organisationally rejected is still a failure. We plan adoption with the same rigour we plan the process design.",
        caps=[
            "Stakeholder Analysis &amp; Change Impact Assessment",
            "ADKAR-Based Change Strategy &amp; Readiness Planning",
            "Executive Sponsorship &amp; Coalition Building",
            "Communication Planning &amp; Campaign Execution",
            "Training, Reinforcement &amp; Adoption Measurement",
        ],
        outcome="Aligned stakeholders, visible executive sponsorship and measurable adoption &mdash; so the improvement holds after the consultants leave.",
    ),
]


def service_cards():
    out = ""
    for s in SERVICES:
        out += f"""
      <a class="card card--link reveal" href="services.html#{s['slug']}">
        {icon(s['ico'])}
        <h3>{s['name']}</h3>
        <p>{s['short']}</p>
        {arrowtext("Learn more")}
      </a>"""
    return out


FOUNDER_BIO = """
<p><strong>Guy Desormes</strong> is a business transformation executive and Lean Six Sigma Master Black Belt with more than two decades leading large-scale performance improvement, mergers and acquisitions, and enterprise operational excellence across manufacturing, life sciences, finance and hospitality.</p>
<p>He has led transformational initiatives at <strong>Mylan Pharmaceuticals</strong>, <strong>Wyndham Worldwide</strong> and <strong>Bank of America</strong>, improving cost, quality and delivery performance while driving organisational alignment and cultural engagement. He played a key role in integration efforts for <strong>two of the largest M&amp;A deals in U.S. history</strong> &mdash; revitalising operational capability, optimising complex supply chains and accelerating post-merger value capture.</p>
<p>Guy is certified and trained by <strong>Sigma Breakthrough Technologies, Inc. (SBTI)</strong>, founded by Six Sigma pioneer Dr. Stephen Zinkgraf, and is recognised for translating advanced CI methodology into practical business outcomes. His career reflects an uncommon combination of Fortune 500 leadership discipline and entrepreneurial execution, further demonstrated through ventures in hospitality, real estate and strategic business advisory.</p>
<p>Today he leads <strong>CogniFlo</strong>, uniting Lean principles with Industry 4.0 technologies to build intelligent, resilient and continuously improving enterprises &mdash; integrating AI, process intelligence, IoT, automation and digital supply chain systems.</p>
<p>Guided by servant leadership and the Shingo principles, Guy believes sustainable transformation is rooted in respect, humility and the empowerment of people to solve problems and grow.</p>
"""

# =====================================================================
# HOME
# =====================================================================
home = f"""
<section class="hero">
  <div class="wrap">
    <div class="hero-inner">
      <p class="eyebrow">Enterprise Transformation Consulting</p>
      <h1>Fix the process.<br>Then automate it.</h1>
      <p class="lede">Most transformation programmes pour technology onto broken processes and quietly scale the waste. We do it in the right order &mdash; eliminate the waste first, then automate what's left.</p>
      <blockquote class="pullquote">&ldquo;Don't Automate Waste &mdash; Eliminate It First.&rdquo;</blockquote>
      <div class="btns">
        {btn("Book a 30-minute review", "contact.html")}
        {btn("See our services", "services.html", "ghost", arrow=False)}
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="creds reveal">
      <div class="cred"><div class="n">20+ years</div><p>Leading enterprise performance improvement at Fortune 500 scale</p></div>
      <div class="cred"><div class="n">Master Black Belt</div><p>Lean Six Sigma, certified by SBTI &mdash; founded by Six Sigma pioneer Dr. Stephen Zinkgraf</p></div>
      <div class="cred"><div class="n">2 of the largest</div><p>M&amp;A integrations in U.S. history, delivered hands-on</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">Our philosophy</p>
        <h2>Automation makes a bad process faster, not better</h2>
      </div>
      <div class="reveal">
        <p>Transformation doesn't start with technology &mdash; it starts with understanding what your process actually does today, as opposed to what the documentation claims.</p>
        <p>We help organisations see, simplify and stabilise their operations <span class="hl">before a single bot is built</span>, blending Lean and Six Sigma, process mining, automation and change enablement into one disciplined method. Every engagement is judged on a number the finance team recognises.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="head reveal">
      <p class="eyebrow">Who we work with</p>
      <h2>Built for complex, data-heavy operations</h2>
      <p class="lede">Mid-to-large enterprises where processes are intricate, data is abundant, and legacy systems have quietly accumulated a decade of workarounds.</p>
    </div>
    <div class="grid grid-4">
      <div class="card reveal">{icon("heart")}<h3>Healthcare &amp; Life Sciences</h3><p>Revenue cycle, patient intake, clinical supply and regulatory workflows.</p></div>
      <div class="card reveal">{icon("bank")}<h3>Financial Services</h3><p>Reconciliation, onboarding, servicing and the controls-heavy back office.</p></div>
      <div class="card reveal">{icon("shield")}<h3>Insurance</h3><p>Claims handling, underwriting operations and policy administration.</p></div>
      <div class="card reveal">{icon("factory")}<h3>Manufacturing &amp; Supply Chain</h3><p>Order to cash, procure to pay, planning and plant-level flow.</p></div>
    </div>
    <p class="terms reveal" style="margin-top:26px;">Typically we're brought in by a CFO, COO, or the leader of a transformation, CI or shared services function.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="offer reveal">
      <p class="eyebrow">Where most clients start</p>
      <h2>The Process X-Ray</h2>
      <p class="lede">Two weeks. One end-to-end process. We pull your event log data and map what actually happens &mdash; every variation, every rework loop, every handoff that stalls &mdash; <span class="hl">not what the SOP says happens</span>.</p>
      <ul class="checklist">
        <li>{ICONS["check"]}<span>The true as-is process, mapped from your own system data</span></li>
        <li>{ICONS["check"]}<span>Waste and delay quantified in cost and cycle time</span></li>
        <li>{ICONS["check"]}<span>A prioritised improvement roadmap</span></li>
        <li>{ICONS["check"]}<span>A clear view of what's genuinely worth automating &mdash; and what isn't</span></li>
      </ul>
      <p class="terms">Fixed scope. Fixed fee. No obligation beyond it.</p>
      <div class="btns">{btn("Request a Process X-Ray", "contact.html")}</div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="head reveal">
      <p class="eyebrow">Our services</p>
      <h2>Transformation services</h2>
      <p class="lede">Six capabilities, delivered in the sequence that makes each one work.</p>
    </div>
    <div class="grid grid-3">{service_cards()}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head reveal">
      <p class="eyebrow">How it works</p>
      <h2>What a CogniFlo engagement looks like</h2>
    </div>
    <div class="steps">
      <div class="step reveal">
        <div class="dur">2 weeks</div>
        <h3>Diagnose</h3>
        <p>We pull your event log data and map what actually happens in one end-to-end process. You get the waste quantified in cost and cycle time, and a ranked list of where to start.</p>
      </div>
      <div class="step reveal">
        <div class="dur">8&ndash;12 weeks</div>
        <h3>Redesign</h3>
        <p>We remove the waste and the variation using Lean and Six Sigma, so the process is stable, capable and actually worth scaling.</p>
      </div>
      <div class="step reveal">
        <div class="dur">Ongoing</div>
        <h3>Automate &amp; sustain</h3>
        <p>Only then do we apply RPA, AI and workflow orchestration &mdash; and stand up the governance, KPIs and internal capability that keep the gains.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="founder">
      <div class="portrait reveal"><div><span>GD</span>Photograph of Guy Desormes goes here</div></div>
      <div class="reveal">
        <p class="eyebrow">Who you'll work with</p>
        <h2>Two decades of transformation, from inside the enterprise</h2>
        <p>CogniFlo is led by <strong>Guy Desormes</strong> &mdash; a Lean Six Sigma Master Black Belt certified by SBTI, the firm founded by Six Sigma pioneer Dr. Stephen Zinkgraf.</p>
        <p>Guy has led enterprise performance improvement at Mylan Pharmaceuticals, Wyndham Worldwide and Bank of America, including post-merger integration on two of the largest M&amp;A deals in U.S. history &mdash; revitalising operational capability, untangling complex supply chains and accelerating value capture.</p>
        <p>He has done this work from the inside, under real pressure, at Fortune 500 scale. That's the perspective he brings to your operation.</p>
        <div style="margin-top:24px;">{arrowlink("Read Guy's full background", "about.html#founder")}</div>
      </div>
    </div>
  </div>
</section>

{CTA_BAND}
"""

# =====================================================================
# SERVICES
# =====================================================================
def service_sections():
    out = ""
    for s in SERVICES:
        caps = "".join(f"<li>{c}</li>" for c in s["caps"])
        out += f"""
  <article class="svc" id="{s['slug']}">
    <div class="svc-grid">
      <div class="reveal">
        {icon(s['ico'])}
        <p class="eyebrow">{s['tag']}</p>
        <h2>{s['name']}</h2>
        <p class="lede">{s['lede']}</p>
        <div class="outcome"><b>Outcome:</b> {s['outcome']}</div>
      </div>
      <div class="reveal">
        <h3>Capabilities</h3>
        <ul class="caps">{caps}</ul>
      </div>
    </div>
  </article>"""
    return out


services = f"""
<section class="hero hero--sub">
  <div class="wrap">
    <div class="hero-inner">
      <p class="eyebrow">Services</p>
      <h1>Empowering your enterprise through process excellence</h1>
      <p class="lede">Six capabilities that blend Lean Six Sigma, process mining, automation and change enablement into one disciplined, results-driven approach &mdash; delivered <span class="hl">in the order that makes each one work</span>.</p>
      <div class="btns">{btn("Start with a Process X-Ray", "contact.html")}</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    {service_sections()}
  </div>
</section>

{CTA_BAND}
"""

# =====================================================================
# APPROACH
# =====================================================================
PILLARS = [
    ("trending", "Lean &amp; Six Sigma", "Disciplined waste elimination and process stabilisation using DMAIC and value stream mapping &mdash; the foundation everything else sits on."),
    ("scan", "Process Mining", "Data-driven discovery of what your processes actually do, surfacing the bottlenecks, rework loops and variants nobody documented."),
    ("rocket", "Intelligent Automation", "Strategic deployment of RPA, AI and workflow orchestration &mdash; applied only once the underlying process deserves it."),
    ("users", "Change Enablement", "Capability building, governance and communication, so improvement continues long after the engagement ends."),
]

approach = f"""
<section class="hero hero--sub">
  <div class="wrap">
    <div class="hero-inner">
      <p class="eyebrow">Process excellence first</p>
      <h1>The CogniFlo methodology</h1>
      <p class="lede">Transformation doesn't start with technology &mdash; it starts with <span class="hl">process excellence</span>. We integrate four disciplines in a deliberate sequence, because the order is what makes them work.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head reveal">
      <p class="eyebrow">Four disciplines</p>
      <h2>What we bring to the work</h2>
    </div>
    <div class="grid grid-pair">
      {"".join(f'<div class="card card--split reveal"><div class="cardhead">{icon(i)}<h3>{n}</h3></div><p>{d}</p></div>' for i, n, d in PILLARS)}
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="head reveal">
      <p class="eyebrow">The sequence</p>
      <h2>Why the order matters more than the tools</h2>
      <p class="lede">Every one of these disciplines is available to buy on its own. The difference is refusing to run them out of order.</p>
    </div>
    <div class="steps">
      <div class="step reveal"><h3>See it</h3><p>Process mining on your own event log data. Not a workshop where people describe the process from memory &mdash; the actual sequence of events, with every variant and delay visible.</p></div>
      <div class="step reveal"><h3>Simplify it</h3><p>Lean and Six Sigma to strip out waste, rework and variation. This is the step that gets skipped, and it's the reason most automation programmes underdeliver.</p></div>
      <div class="step reveal"><h3>Scale it</h3><p>Automation and AI applied to a process that's now stable and capable, so the technology compounds the gain instead of entrenching the problem.</p></div>
      <div class="step reveal"><h3>Sustain it</h3><p>Capability, governance and financial tracking, so the improvement is still there in twelve months and your team can run the next one without us.</p></div>
    </div>
    <blockquote class="pullquote reveal" style="margin-top:52px;max-width:34ch;">&ldquo;Don't Automate Waste &mdash; Eliminate It First.&rdquo;</blockquote>
  </div>
</section>

{CTA_BAND}
"""

# =====================================================================
# ABOUT
# =====================================================================
VALUES = [
    ("Empower Every Voice", "The best ideas live closest to the work. We elevate the voices of team members at every level, creating inclusive systems where frontline insight is recognised, rewarded and acted upon."),
    ("Lead Through Service", "We serve first &mdash; clients, teams and community. At CogniFlo, leadership is not about authority but about enabling the success of others. We seek first to understand, and always act in service of delivering value."),
    ("Pursue Flow with Purpose", "We design systems that flow, so people can thrive. Flow is not just technical efficiency &mdash; it's a human enabler. By reducing waste and friction, we unlock creativity, clarity and contribution."),
    ("Grow Through Curiosity", "Learning is our default setting. We cultivate systems of experimentation, reflection and feedback, where growth is not an event but a way of working."),
]

about = f"""
<section class="hero hero--sub">
  <div class="wrap">
    <div class="hero-inner">
      <p class="eyebrow">About</p>
      <h1>We help organisations unlock what's locked inside their processes</h1>
      <p class="lede">CogniFlo blends Lean principles with intelligent technology so operations don't just run better &mdash; they learn. We believe transformation begins with <span class="hl">understanding and optimising, before automating</span>.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid-3">
      <div class="card reveal"><h3>Our mission</h3><p>Every organisation has untapped potential locked inside its processes. Our mission is to unlock it &mdash; combining Lean principles with intelligent technology so operations don't just run better, they learn.</p></div>
      <div class="card reveal"><h3>Our vision</h3><p>To be the global leader in process-first enterprise transformation: building self-reliant organisations with a genuine continuous improvement culture and real digital fluency.</p></div>
      <div class="card reveal"><h3>What we believe</h3><p>Transformation starts with understanding and optimising &mdash; before automating. Everything else we do follows from that one commitment.</p></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="head center reveal">
      <p class="eyebrow">Core values</p>
      <h2>The principles that guide the work</h2>
    </div>
    <div class="grid grid-pair">
      {"".join(f'<div class="card value reveal"><h3>{n}</h3><p>{d}</p></div>' for n, d in VALUES)}
    </div>
  </div>
</section>

<section class="section" id="founder">
  <div class="wrap">
    <div class="head reveal">
      <p class="eyebrow">Leadership</p>
      <h2>Meet our founder</h2>
    </div>
    <div class="founder">
      <div class="portrait reveal"><div><span>GD</span>Photograph of Guy Desormes goes here</div></div>
      <div class="reveal">
        <h3 style="font-size:1.8rem;">Guy Desormes</h3>
        <p class="role">Founder &amp; Managing Director</p>
        <p>A Lean Six Sigma Master Black Belt with more than twenty years driving operational excellence and digital transformation across global enterprises &mdash; certified by SBTI, the firm founded by Six Sigma pioneer Dr. Stephen Zinkgraf.</p>
        <p>Guy has led enterprise performance improvement at Mylan Pharmaceuticals, Wyndham Worldwide and Bank of America, including post-merger integration on two of the largest M&amp;A deals in U.S. history.</p>
        <div class="btns" style="margin-top:26px;">
          <a class="btn btn--ghost" href="{LINKEDIN}">{ICONS["linkedin"]}LinkedIn</a>
          <a class="btn btn--ghost" href="mailto:{EMAIL}">{ICONS["mail"]}Email Guy</a>
        </div>
        <details class="bio">
          <summary>Read the full background</summary>
          <div class="biobody">{FOUNDER_BIO}</div>
        </details>
      </div>
    </div>
  </div>
</section>

{CTA_BAND}
"""

# =====================================================================
# CONTACT
# =====================================================================
PHONE_ITEM = (
    f'<li><a class="contact-item" href="tel:{PHONE_HREF}">{icon("phone")}'
    f'<div><div class="lbl">Phone</div><div class="val">{PHONE_DISPLAY}</div></div></a></li>'
    if PHONE_DISPLAY else ""
)

contact = f"""
<section class="hero hero--sub">
  <div class="wrap">
    <div class="hero-inner">
      <p class="eyebrow">Contact</p>
      <h1>Tell us about the process that's costing you the most</h1>
      <p class="lede">We'll tell you what we'd look at first &mdash; no pitch, no obligation. If it turns out we're not the right fit, we'll say so and point you somewhere better.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split" style="align-items:start;">
      <div class="reveal">
        <div class="form-card">
          <div id="formOk" hidden tabindex="-1">
            <h3>Thank you &mdash; that's come through.</h3>
            <p>We read every message ourselves and reply within one business day.</p>
          </div>
          <div id="formErr" class="formmsg" hidden role="alert"><span class="msg"></span></div>
          <form id="contactForm" action="{FORM_ENDPOINT}" method="POST" novalidate>
            <input type="hidden" name="_subject" value="New enquiry from the CogniFlo website">
            <div class="hp" aria-hidden="true"><label for="_gotcha">Leave this empty</label><input type="text" id="_gotcha" name="_gotcha" tabindex="-1" autocomplete="off"></div>
            <div class="field">
              <label for="name">Your name</label>
              <input type="text" id="name" name="name" autocomplete="name" required>
            </div>
            <div class="field">
              <label for="email">Work email</label>
              <input type="email" id="email" name="email" autocomplete="email" required>
            </div>
            <div class="field">
              <label for="message">What's the process? <span class="hint">&mdash; a sentence or two is plenty</span></label>
              <textarea id="message" name="message" placeholder="e.g. Our order-to-cash cycle takes 40 days and nobody can tell me where the time goes."></textarea>
            </div>
            <button type="submit" class="btn btn--primary" style="width:100%;justify-content:center;">Send message{ICONS["arrow"]}</button>
          </form>
        </div>
      </div>
      <div class="reveal">
        <h2>Other ways to reach us</h2>
        <p>If you'd rather skip the form, either of these reaches us directly.</p>
        <ul class="contact-list" style="margin-top:28px;">
          <li><a class="contact-item" href="mailto:{EMAIL}">{icon("mail")}<div><div class="lbl">Email</div><div class="val">{EMAIL}</div></div></a></li>
          {PHONE_ITEM}
          <li><a class="contact-item" href="{LINKEDIN}">{icon("linkedin")}<div><div class="lbl">LinkedIn</div><div class="val">Follow CogniFlo</div></div></a></li>
        </ul>
        <div class="outcome" style="margin-top:32px;">
          <b>Most people start here:</b> the Process X-Ray &mdash; a two-week, fixed-fee diagnostic on one end-to-end process. Mention it in your message and we'll send the scope.
        </div>
      </div>
    </div>
  </div>
</section>
"""

# =====================================================================
PAGES = [
    ("index.html", "CogniFlo | Process Excellence Before Automation",
     "We help enterprises eliminate process waste before automating it — fusing Lean Six Sigma, process mining and intelligent automation into measurable results.", home),
    ("services.html", "Transformation Services | CogniFlo",
     "Strategy, process re-engineering, intelligent automation, capability building, value realization and change management — delivered in the order that actually works.", services),
    ("approach.html", "Our Methodology: Process Excellence First | CogniFlo",
     "Lean Six Sigma, process mining, intelligent automation and change enablement, combined into one disciplined method. Don't automate waste — eliminate it first.", approach),
    ("about.html", "About CogniFlo | Led by Guy Desormes, LSS Master Black Belt",
     "CogniFlo is led by a Lean Six Sigma Master Black Belt with 20+ years of enterprise transformation at Mylan, Wyndham Worldwide and Bank of America.", about),
    ("contact.html", "Contact CogniFlo",
     "Tell us about the process that's costing you the most. We'll tell you what we'd look at first — no pitch, no obligation.", contact),
]

for fn, title, desc, body in PAGES:
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        f.write(page(fn, title, desc, body, fn))
    print("wrote", fn)


# =====================================================================
# 404 — GitHub Pages serves /404.html automatically
# =====================================================================
notfound_body = f"""
<section class="hero hero--sub">
  <div class="wrap">
    <div class="hero-inner">
      <p class="eyebrow">404</p>
      <h1>That page isn't here</h1>
      <p class="lede">The link may be out of date, or we may have moved something. Here's where most people are heading:</p>
      <div class="btns">
        {btn("Back to the home page", "index.html")}
        {btn("See our services", "services.html", "ghost", arrow=False)}
      </div>
    </div>
  </div>
</section>
"""
with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
    f.write(page("404.html", "Page not found | CogniFlo",
                 "That page isn't here. Head back to the CogniFlo home page.",
                 notfound_body, "404.html"))
print("wrote 404.html")

# =====================================================================
# robots.txt + sitemap.xml + .nojekyll
# =====================================================================
with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")

urls = ""
for fn, *_ in PAGES:
    loc = SITE_URL + "/" + ("" if fn == "index.html" else fn)
    pri = "1.0" if fn == "index.html" else "0.8"
    urls += f"  <url>\n    <loc>{loc}</loc>\n    <priority>{pri}</priority>\n  </url>\n"
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{urls}</urlset>\n")

# Tells GitHub Pages to serve files as-is instead of running them through Jekyll
open(os.path.join(OUT, ".nojekyll"), "w").close()
print("wrote robots.txt, sitemap.xml, .nojekyll")

# =====================================================================
# assets: favicon + social card
# =====================================================================
ASSETS = os.path.join(OUT, "assets")
os.makedirs(ASSETS, exist_ok=True)

FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#4fd1c5"/><stop offset="1" stop-color="#5b9dff"/>
  </linearGradient></defs>
  <rect width="64" height="64" rx="16" fill="url(#g)"/>
  <path d="M42 24a12 12 0 1 0 0 16" fill="none" stroke="#06121a" stroke-width="7"
        stroke-linecap="round"/>
</svg>
"""
with open(os.path.join(ASSETS, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(FAVICON_SVG)

try:
    from PIL import Image, ImageDraw, ImageFont

    def font(size, bold=True):
        paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
            else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        ]
        for p in paths:
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
        return ImageFont.load_default()

    # --- favicon PNGs ---
    for size, name in [(32, "favicon.png"), (180, "apple-touch-icon.png")]:
        im = Image.new("RGB", (size, size), "#4fd1c5")
        d = ImageDraw.Draw(im)
        for y in range(size):                       # simple diagonal gradient
            t = y / max(size - 1, 1)
            d.line([(0, y), (size, y)],
                   fill=(int(79 + (91 - 79) * t), int(209 + (157 - 209) * t),
                         int(197 + (255 - 197) * t)))
        r = size * 0.30
        cx = cy = size / 2
        d.arc([cx - r, cy - r, cx + r, cy + r], start=40, end=320,
              fill=(6, 18, 26), width=max(2, int(size * 0.13)))
        im.save(os.path.join(ASSETS, name))

    # --- social card 1200x630 ---
    W, H = 1200, 630
    card = Image.new("RGB", (W, H), "#0a1020")
    d = ImageDraw.Draw(card)
    for y in range(H):                              # vertical wash
        t = y / (H - 1)
        d.line([(0, y), (W, y)],
               fill=(int(13 - 3 * t), int(23 - 7 * t), int(48 - 16 * t)))
    for i in range(260, 0, -1):                     # accent glow, top-left
        a = i / 260
        d.ellipse([-160 - i, -190 - i, 300 + i, 210 + i],
                  outline=(int(10 + 22 * a), int(16 + 46 * a), int(32 + 44 * a)))
    d.rectangle([0, 0, 10, H], fill="#4fd1c5")
    d.text((84, 150), "CogniFlo", font=font(78), fill="#f2f5fc")
    d.text((88, 244), "CONSULTING GROUP", font=font(23), fill="#8b9ac0")
    d.text((84, 330), "Fix the process.", font=font(60), fill="#f2f5fc")
    d.text((84, 400), "Then automate it.", font=font(60), fill="#4fd1c5")
    d.text((84, 508), "Don't Automate Waste — Eliminate It First.",
           font=font(27, bold=False), fill="#b8c4dc")
    card.save(os.path.join(ASSETS, "social-card.png"))
    print("wrote assets/ (favicon.svg, favicon.png, apple-touch-icon.png, social-card.png)")
except ImportError:
    print("!! Pillow not installed — favicon PNGs and social card skipped")

print("done ->", OUT)
