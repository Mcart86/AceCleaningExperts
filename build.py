#!/usr/bin/env python3
import os
import json

ROOT = os.path.dirname(os.path.abspath(__file__))
PHONE = "856-582-1711"
PHONE_TEL = "8565821711"
EMAIL = "info@acecleaningexpertsnj.com"
DOMAIN = "https://www.acecleaningexpertsnj.com"

# ---------------------------------------------------------------- icons ----
ICONS = {
"paw": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="7" cy="9" r="1.6"/><circle cx="12" cy="6.5" r="1.6"/><circle cx="17" cy="9" r="1.6"/><path d="M12 12c-3 0-5.5 2-5.5 4.5S8.5 20 12 20s5.5-1 5.5-3.5S15 12 12 12z"/></svg>',
"leaf": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 19c8 0 14-6 14-14-8 0-14 6-14 14z"/><path d="M5 19c2-4 5-7 9-9"/></svg>',
"sparkle": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.6 4.4L18 9l-4.4 1.6L12 15l-1.6-4.4L6 9l4.4-1.6z"/><path d="M18.5 15l.8 2.2L21.5 18l-2.2.8-.8 2.2-.8-2.2-2.2-.8 2.2-.8z"/></svg>',
"steam": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6 21c-1.5-2 1.5-3 0-5"/><path d="M12 21c-1.5-2 1.5-3 0-5"/><path d="M18 21c-1.5-2 1.5-3 0-5"/></svg>',
"calendar": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="1.5"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
"rug": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="13" rx="1.5"/><rect x="6.5" y="7.5" width="11" height="6" rx="0.5"/><path d="M4 20h2M8 20h2M12 20h2M16 20h2"/></svg>',
"sofa": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 11V8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v3"/><rect x="3" y="11" width="18" height="6" rx="1.5"/><path d="M4 17v2M20 17v2"/></svg>',
"tile": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="8" height="8" rx="0.5"/><rect x="13" y="3" width="8" height="8" rx="0.5"/><rect x="3" y="13" width="8" height="8" rx="0.5"/><rect x="13" y="13" width="8" height="8" rx="0.5"/></svg>',
"building": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="3" width="14" height="18" rx="1"/><path d="M9 8h1M14 8h1M9 12h1M14 12h1M9 16h1M14 16h1"/><path d="M10 21v-4h4v4"/></svg>',
"flag": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 21V4"/><path d="M5 4h14l-2.5 4L19 12H5"/></svg>',
"shield": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg>',
"star": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l2.6 5.6 6.1.6-4.6 4.2 1.3 6-5.4-3.1-5.4 3.1 1.3-6-4.6-4.2 6.1-.6z"/></svg>',
"home": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11l8-7 8 7"/><path d="M6 10v9a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1v-9"/></svg>',
"clock": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></svg>',
"check": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12l5 5 11-11"/></svg>',
"pin": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.3"/></svg>',
"phone": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M6.6 10.8c1.4 2.8 3.8 5.2 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.9 21 3 13.1 3 3.6c0-.6.4-1 1-1h3.4c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>',
"mail": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="1.5"/><path d="M3.5 6.5l8.5 6 8.5-6"/></svg>',
"menu": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
"arrow": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
"droplet": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/></svg>',
"chevron": '<svg class="chev" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>',
"users": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><path d="M16 8.2a3 3 0 1 1 1 5.8"/><path d="M19 14c2 .4 3.5 1.9 3.5 4"/></svg>',
"briefcase": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="18" height="13" rx="1.5"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M3 12h18"/></svg>',
"utensils": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3v7a2 2 0 0 0 2 2v9M7 3v7M9 3v7M17 3c-1.5 0-2.5 1.5-2.5 4s1 4 2.5 4v10"/></svg>',
"book": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5.5C4 4.7 4.7 4 5.5 4H12v16H5.5A1.5 1.5 0 0 1 4 18.5v-13z"/><path d="M20 5.5c0-.8-.7-1.5-1.5-1.5H12v16h6.5a1.5 1.5 0 0 0 1.5-1.5v-13z"/></svg>',
"hardhat": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 16a8 8 0 0 1 16 0z"/><path d="M2 16h20M11 5v5M9 5h6"/></svg>',
"facebook": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 8h2V5h-2a4 4 0 0 0-4 4v2H9v3h2v7h3v-7h2.2l.8-3H14V9c0-.6.4-1 1-1z"/></svg>',
"search": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>',
"compass": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M15 9l-2 6-4-2 2-6z"/></svg>',
"spade": '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C12 2 4 10 4 15a5 5 0 0 0 8 4c-.3 1.5-1 2.5-2 3.3V23h4v-.7c-1-.8-1.7-1.8-2-3.3a5 5 0 0 0 8-4C20 10 12 2 12 2z"/></svg>',
"ace_card": '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="3" y="1.5" width="18" height="21" rx="2.5"/><path d="M12 8.2c0 0-3.4 3.6-3.4 5.8a2.4 2.4 0 0 0 3.9 1.9c-.15.7-.5 1.2-1 1.6v.7h1v-.7c-.5-.4-.85-.9-1-1.6a2.4 2.4 0 0 0 3.9-1.9c0-2.2-3.4-5.8-3.4-5.8z" fill="currentColor" stroke="none"/><text x="5.2" y="7" font-size="5.5" font-weight="700" fill="currentColor" font-family="Georgia, serif">A</text></svg>',
}

def icon(name):
    return ICONS[name]

NAV = [
    ("Home", "/", "home"),
    ("About", "/about-us/", "about"),
    ("Services", "/services/", "services"),
    ("Commercial", "/commercial-carpet-cleaning/", "commercial"),
    ("Our Work", "/our-work/", "our-work"),
    ("Service Areas", "/service-areas/", "areas"),
    ("Contact", "/contact/", "contact"),
]

def head(title, desc, canonical):
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{DOMAIN}{canonical}">
<meta property="og:image" content="{DOMAIN}/images/ace-logo.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700;9..144,900&family=Inter:wght@400;500;600;700;800&family=Caveat:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
<link rel="icon" href="/images/ace-logo.jpg">
"""

def header(active):
    SERVICE_LINKS = [
        ("/carpet-cleaning-service/", "Carpet Cleaning"),
        ("/upholstery-cleaning/", "Upholstery Cleaning"),
        ("/tile-grout-cleaning/", "Tile &amp; Grout Cleaning"),
    ]
    links = []
    for label, href, key in NAV:
        cur = ' aria-current="page"' if key == active else ""
        if key == "areas":
            town_links = "\n          ".join(
                f'<a href="/service-areas/{t["slug"]}/">{t["name"]}</a>' for t in TOWNS
            )
            links.append(f'''<div class="nav-dropdown">
        <a href="{href}"{cur} class="nav-dropdown-trigger">{label} {icon('chevron')}</a>
        <div class="nav-dropdown-panel">
          {town_links}
          <a href="/service-areas/" class="nav-dropdown-viewall">View All Service Areas</a>
        </div>
      </div>''')
        elif key == "services":
            svc_links = "\n          ".join(
                f'<a href="{s_href}">{s_label}</a>' for s_href, s_label in SERVICE_LINKS
            )
            links.append(f'''<div class="nav-dropdown">
        <a href="{href}"{cur} class="nav-dropdown-trigger">{label} {icon('chevron')}</a>
        <div class="nav-dropdown-panel">
          {svc_links}
          <a href="/services/" class="nav-dropdown-viewall">View All Services</a>
        </div>
      </div>''')
        else:
            links.append(f'<a href="{href}"{cur}>{label}</a>')
    nav_links = "\n      ".join(links)
    return f"""<header class="site-header">
  <div class="wrap nav-row">
    <a href="/" class="logo">
      <img src="/images/ace-logo.jpg" alt="Ace Cleaning Experts - Veteran-Owned Carpet &amp; Floor Cleaning, South Jersey" class="logo-img">
    </a>
    <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" id="navToggle">{icon('menu')}</button>
    <nav class="primary-nav" id="primaryNav">
      {nav_links}
    </nav>
    <div class="nav-cta">
      <div class="nav-phone">
        <span class="call-label">Call Now</span>
        <a class="call-number" href="tel:{PHONE_TEL}">{PHONE}</a>
      </div>
      <a href="/contact/" class="btn btn-primary">Get Free Quote</a>
    </div>
  </div>
</header>
"""

def footer():
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <div class="footer-logo-badge"><img src="/images/ace-logo.jpg" alt="Ace Cleaning Experts logo" class="footer-logo-img"></div>
      <p>Veteran-owned, family-operated carpet and floor cleaning serving South Jersey for 40+ years.</p>
      <div class="foot-social">
        <a href="https://www.facebook.com/AceCleaningExperts/" aria-label="Facebook">{icon('facebook')}</a>
      </div>
    </div>
    <div>
      <h4>Get In Touch</h4>
      <ul>
        <li><a href="tel:{PHONE_TEL}">{icon('phone')} &nbsp;{PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">{icon('mail')} &nbsp;{EMAIL}</a></li>
        <li>Mon&ndash;Sat: 9:00am&ndash;5:00pm</li>
        <li>Sunday: Closed</li>
      </ul>
    </div>
    <div>
      <h4>Quick Links</h4>
      <ul>
        <li><a href="/about-us/">About Us</a></li>
        <li><a href="/services/">All Services</a></li>
        <li><a href="/commercial-carpet-cleaning/">Commercial</a></li>
        <li><a href="/service-areas/">Service Areas</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul>
    </div>
    <div>
      <h4>Service Area</h4>
      <ul>
        <li>Sewell &middot; Deptford &middot; Haddonfield</li>
        <li>Atlantic, Camden, Gloucester &amp; Cape May Counties</li>
        <li>Philadelphia &amp; Wilmington, DE</li>
      </ul>
    </div>
  </div>
  <div class="wrap foot-bottom">
    <span>&copy; <span id="yr"></span> Ace Cleaning Experts. All rights reserved.</span>
    <span>Veteran-Owned &middot; Family-Operated &middot; South Jersey, NJ</span>
  </div>
</footer>
<script src="/js/main.js"></script>
"""

def page(path, title, desc, active, body):
    full = f"""<!DOCTYPE html>
<html lang="en">
<head>
{head(title, desc, path)}
</head>
<body>
{header(active)}
<main>
{body}
</main>
{footer()}
</body>
</html>
"""
    out_dir = os.path.join(ROOT, path.strip("/"))
    if path == "/":
        out_path = os.path.join(ROOT, "index.html")
    else:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w") as f:
        f.write(full)
    print("wrote", out_path)

# ---------------------------------------------------------------- shared partials ----

def cta_band(headline="Ready to Love Your Floors Again?", sub="Fast response, honest pricing, and a crew that shows up when they say they will."):
    return f"""<section class="cta-band">
  <div class="wrap">
    <h2>{headline}</h2>
    <p class="lede">{sub}</p>
    <div class="btn-row">
      <a href="/contact/" class="btn btn-dark">Get Free Quote</a>
      <a href="tel:{PHONE_TEL}" class="btn btn-outline-light">{icon('phone')} Call {PHONE}</a>
    </div>
    <div class="cta-strip">
      <span>Fast Response</span>
      <span>Veteran-Owned</span>
      <span>Deep Cleaning Guaranteed</span>
      <span>Serving South Jersey for 40+ Years</span>
    </div>
  </div>
</section>"""

def trust_strip():
    items = [
        ("shield", "Veteran-Owned"),
        ("home", "Family-Owned &amp; Operated"),
        ("check", "Fully Insured"),
        ("building", "Residential &amp; Commercial"),
    ]
    lis = "\n    ".join(f'<div class="item">{icon(n)}<span>{t}</span></div>' for n, t in items)
    return f'<div class="trust-strip"><div class="wrap">\n    {lis}\n  </div></div>'

def stats_bar():
    return f"""<div class="stats-float-card"><div class="stats-grid stats-grid-5">
    <div class="stat"><div class="stat-num">40+</div><div class="stat-label">Years Experience</div></div>
    <div class="stat"><div class="stat-num">10,000+</div><div class="stat-label">Homes Cleaned</div></div>
    <div class="stat"><div class="stat-num stat-num-bold">5&#9733;</div><div class="stat-label">Star Rating</div></div>
    <div class="stat"><div class="stat-num">100%</div><div class="stat-label">Satisfaction Guaranteed</div></div>
    <div class="stat"><div class="stat-num stat-icon"><img src="/images/us-flag-v1.webp" alt="American flag" style="width:44px;height:auto;border-radius:2px;box-shadow:var(--shadow-sm);"></div><div class="stat-label">Veteran Owned</div></div>
  </div></div>"""

def breadcrumb(trail):
    parts = " / ".join(f'<a href="{h}">{l}</a>' if h else l for l, h in trail)
    return f'<div class="breadcrumb">{parts}</div>'

def faq(items):
    out = ['<div class="faq-list">']
    for q, a in items:
        out.append(f'<details class="faq-item"><summary>{q} {icon("chevron")}</summary><p>{a}</p></details>')
    out.append('</div>')
    return "\n".join(out)

def process_steps(steps):
    out = ['<div class="step-list">']
    for i, (t, d) in enumerate(steps, 1):
        out.append(f'<div class="step"><div class="num">{i}</div><div><h3>{t}</h3><p>{d}</p></div></div>')
    out.append('</div>')
    return "\n".join(out)

GALLERY_IMAGES = [
    ("gallery-01", "Red patterned commercial carpet cleaning in progress"),
    ("gallery-02", "Commercial carpet before and after cleaning, dirt lifted"),
    ("gallery-03", "Green carpet cleaned, stain treatment in progress"),
    ("gallery-04", "Patterned commercial carpet cleaning"),
    ("gallery-05", "Gray carpet before and after cleaning"),
    ("gallery-06", "Upholstery fabric cleaning, before and after"),
    ("gallery-07", "Restaurant carpet mid-clean, dirt lifted with hose"),
    ("gallery-08", "Staircase carpet before and after cleaning, side by side"),
    ("gallery-09", "Stained carpet before and after deep cleaning"),
    ("gallery-10-v2", "Rotary tile cleaning tool in action on stone floor"),
    ("gallery-11", "Patterned commercial carpet cleaning, ice cream shop"),
    ("gallery-12", "Area rug cleaning, dirty and clean sides compared"),
    ("gallery-13", "Beige patterned carpet before and after cleaning"),
    ("gallery-14", "Pink carpet before and after deep cleaning"),
    ("gallery-15", "Carpet close-up showing dirty and clean sections"),
    ("gallery-16", "Large room carpet before and after cleaning"),
    ("gallery-17", "Striped commercial carpet cleaning"),
    ("gallery-18", "Ornate patterned commercial carpet cleaning"),
    ("gallery-19", "Polka-dot patterned commercial carpet cleaning"),
    ("gallery-20", "Diamond-patterned commercial carpet cleaning"),
    ("gallery-21", "Triangle-patterned commercial carpet cleaning"),
    ("gallery-22", "Star-patterned commercial carpet cleaning"),
    ("gallery-23", "Restaurant stone-look tile floor being deep cleaned, dirt lifted"),
    ("gallery-24", "Staircase carpet mid-clean, dirty and freshly cleaned sections side by side"),
    ("gallery-25", "Restaurant entry mat before and after cleaning, logo colors restored"),
]

ALL_SERVICES = [
    ("/carpet-cleaning-service/", "Carpet Cleaning"),
    ("/upholstery-cleaning/", "Upholstery Cleaning"),
    ("/tile-grout-cleaning/", "Tile, Grout &amp; Hardwood"),
    ("/commercial-carpet-cleaning/", "Commercial Floor Care"),
]

PRIORITY_AREAS = [
    ("/service-areas/sewell-nj/", "Sewell, NJ"),
    ("/service-areas/deptford-nj/", "Deptford, NJ"),
    ("/service-areas/haddonfield-nj/", "Haddonfield, NJ"),
]

def related_links(current_href):
    other_services = "\n          ".join(
        f'<li>{icon("check")} <a href="{href}">{label}</a></li>'
        for href, label in ALL_SERVICES if href != current_href
    )
    areas = "\n          ".join(
        f'<li>{icon("check")} <a href="{href}">{label}</a></li>'
        for href, label in PRIORITY_AREAS
    )
    return f'''<section>
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Explore More</span>
      <h2>More Ways We Can Help</h2>
    </div>
    <div class="related-split">
      <div class="related-panel panel-red">
        <h3>Other Services</h3>
        <ul class="checklist">
          {other_services}
        </ul>
      </div>
      <div class="related-panel panel-charcoal">
        <h3>Popular Service Areas</h3>
        <ul class="checklist">
          {areas}
        </ul>
        <p style="margin-top:16px;"><a href="/service-areas/" class="go">View All Service Areas {icon('arrow')}</a></p>
      </div>
    </div>
  </div>
</section>'''

def mini_ba_slider(before_src, after_src, before_alt, after_alt, placeholder=False):
    if placeholder:
        return f'<div class="ba-slider ba-slider-mini"><div class="placeholder-block" style="width:100%; height:100%; border:none; border-radius:0;">{icon("rug")}<span>Before &amp; After</span></div></div>'
    return f'''<div class="ba-slider ba-slider-mini">
      <img src="{before_src}" alt="{before_alt}" class="ba-before">
      <img src="{after_src}" alt="{after_alt}" class="ba-after">
      <span class="ba-tag before-tag">Before</span>
      <span class="ba-tag after-tag">After</span>
      <div class="ba-handle"></div>
      <input type="range" min="0" max="100" value="50" class="ba-range" aria-label="Drag to compare before and after">
    </div>'''

def service_showcase_card(href, category, headline, description, chips, photo_src, photo_alt):
    badge_cls = "svc-category-charcoal" if category == "Commercial Service" else "svc-category-red"
    return f'''<div class="svc-showcase-card">
      <img src="{photo_src}" alt="{photo_alt}" class="svc-photo">
      <div class="svc-body">
        <span class="svc-category {badge_cls}">{category}</span>
        <h3>{headline}</h3>
        <p>{description}</p>
        <div class="svc-chip-row">
          {"".join(f'<div class="svc-chip">{icon(ic)}<span>{label}</span></div>' for ic, label in chips)}
        </div>
        <a href="{href}" class="svc-explore">Explore Service <span class="explore-arrow">{icon('arrow')}</span></a>
      </div>
    </div>'''

def gallery_grid(images=GALLERY_IMAGES):
    items = "\n    ".join(
        f'<button type="button" class="gallery-item" data-full="/images/{name}.webp" aria-label="View larger: {alt}">'
        f'<img src="/images/{name}-thumb.webp" alt="{alt}" loading="lazy"></button>'
        for name, alt in images
    )
    return f'''<div class="gallery-grid">
    {items}
  </div>
  <div class="lightbox" id="lightbox" hidden>
    <button type="button" class="lightbox-close" id="lightboxClose" aria-label="Close">&times;</button>
    <img src="" alt="" id="lightboxImg">
  </div>'''

def quote_snippet(text, name, stars=5, inline=False, photo=None, photo_alt="", color="charcoal"):
    cls = "quote-strip-card inline" if inline else "quote-strip-card"
    if color == "red":
        cls += " color-red"
    return f'''<div class="{cls}">
      <blockquote>&ldquo;{text}&rdquo;</blockquote>
      <div class="quote-strip-attrib">&mdash; {name}, Google Review</div>
    </div>'''

def placeholder(label, extra_class=""):
    return f'<div class="placeholder-block {extra_class}">{icon("droplet")}<span>{label}</span></div>'

def card_divider():
    return '<div class="card-divider" role="presentation"></div>'

# ---------------------------------------------------------- location pages ----
# Each town: slug, display name, county, zip, and a short paragraph of genuinely
# specific local detail (verified facts, not generic filler) plus a services note.
TOWNS = [
    {
        "slug": "sewell-nj",
        "name": "Sewell",
        "county": "Gloucester County",
        "zip": "08080",
        "about": "Sewell sits within Washington Township and Mantua Township in Gloucester County, "
                 "just off Route 42 &mdash; home turf for us, and one of our most-requested towns for "
                 "carpet and floor cleaning. Whether you're near Washington Township High School or "
                 "closer to Rowan College of South Jersey, we're a short drive away.",
        "local_note": "As one of our home-base towns, we're in and out of Sewell multiple times a week &mdash; "
                       "carpet cleaning for homes along Route 42, plus tile and grout work for the businesses "
                       "near Rowan College of South Jersey.",
    },
    {
        "slug": "deptford-nj",
        "name": "Deptford Township",
        "county": "Gloucester County",
        "zip": "08096",
        "about": "Deptford Township has been a Gloucester County hub since Route 42 opened it up to "
                 "suburban growth in the late 1950s, and the Deptford Mall has anchored the area since "
                 "1975. We handle carpet, tile and upholstery cleaning for homes and the businesses that "
                 "keep this busy corridor running.",
        "local_note": "With the Deptford Mall corridor as one of Gloucester County's busiest retail stretches, "
                       "commercial floor care is a big part of what we do here, alongside residential carpet "
                       "cleaning throughout the township's neighborhoods.",
    },
    {
        "slug": "haddonfield-nj",
        "name": "Haddonfield",
        "county": "Camden County",
        "zip": "08033",
        "about": "Haddonfield's historic Kings Highway district &mdash; over 200 shops, restaurants and "
                 "galleries along a National Register Historic District &mdash; means a lot of older homes "
                 "and storefronts with floors worth taking care of properly. We're comfortable working "
                 "carefully in Haddonfield's colonial-era homes as well as its busy downtown storefronts.",
        "local_note": "Haddonfield's mix of colonial-era homes and Kings Highway storefronts means we do a "
                       "lot of careful upholstery and tile work here &mdash; older homes and antique furniture "
                       "call for a gentler touch than newer construction.",
    },
    {
        "slug": "west-deptford-nj",
        "name": "West Deptford",
        "county": "Gloucester County",
        "zip": None,
        "about": "West Deptford sits along the Delaware River and is home to Ladd's Castle, the oldest brick "
                 "house in Gloucester County and a National Register landmark, along with the RiverWinds "
                 "Community Center's waterfront trails and golf course. From the Green-Fields neighborhood "
                 "to the streets around Thorofare, we handle carpet, tile and upholstery cleaning for homes "
                 "and businesses throughout the township.",
        "local_note": "Between the riverfront homes near RiverWinds and the neighborhoods around Thorofare, "
                       "carpet and tile cleaning make up most of our West Deptford calls.",
    },
    {
        "slug": "logan-township-nj",
        "name": "Logan Township",
        "county": "Gloucester County",
        "zip": "08085",
        "about": "Logan Township runs along Raccoon Creek near Swedesboro, with roots going back to some of "
                 "the first Swedish settlers in the Repaupo section along the Delaware River meadowlands. "
                 "It's a mix of quiet farmland and newer development, and we're a regular stop for carpet, "
                 "tile and upholstery cleaning across the township.",
        "local_note": "Logan Township's mix of farmland and newer development means we see everything from "
                       "older farmhouse carpets to fresh-build tile floors &mdash; we adjust our approach to "
                       "match either.",
    },
    {
        "slug": "washington-township-nj",
        "name": "Washington Township",
        "county": "Gloucester County",
        "zip": "08080",
        "about": "Washington Township stretches from the Grenloch Terrace section &mdash; once a Lenni Lenape "
                 "village and later a 19th-century industrial hub near Grenloch Lake &mdash; out through Sewell "
                 "and Turnersville. It's one of the most populous townships in Gloucester County, and one of "
                 "the areas we serve most often for carpet, tile and upholstery cleaning.",
        "local_note": "As one of Gloucester County's most populous townships, Washington Township keeps us "
                       "busy across all four services &mdash; from carpet cleaning in Grenloch Terrace to "
                       "commercial work in the retail corridors near Turnersville.",
    },
    {
        "slug": "franklin-township-nj",
        "name": "Franklin Township",
        "county": "Gloucester County",
        "zip": "08322",
        "about": "Franklin Township is the largest township by area in Gloucester County, taking in "
                 "Franklinville, Malaga and several other rural communities. Malaga's glassworks date back "
                 "to 1814, and Franklinville still has its historic railroad station. We serve homes and "
                 "businesses across the township's more spread-out communities for carpet, tile and "
                 "upholstery cleaning.",
        "local_note": "Franklin Township's spread-out communities, from Franklinville to Malaga, mean more "
                       "driving between jobs &mdash; but we treat every stop the same: same pricing, same "
                       "process, no matter how far off the main road you are.",
    },
    {
        "slug": "cherry-hill-nj",
        "name": "Cherry Hill",
        "county": "Camden County",
        "zip": "08003",
        "about": "Cherry Hill takes its name from the blooming cherry trees that gave the former Delaware "
                 "Township its new identity in 1961, the same year the Cherry Hill Mall opened as one of the "
                 "first enclosed shopping centers in the country. It's one of the largest townships in South "
                 "Jersey, and we handle carpet, tile and upholstery cleaning for homes and businesses "
                 "throughout it.",
        "local_note": "Cherry Hill's size and mix of retail and residential means we handle everything from "
                       "mall-adjacent commercial floor care to carpet and upholstery cleaning in neighborhoods "
                       "throughout the township.",
    },
    {
        "slug": "voorhees-nj",
        "name": "Voorhees",
        "county": "Camden County",
        "zip": "08043",
        "about": "Voorhees was named for Governor Foster McGowan Voorhees when it split off as its own "
                 "township in 1899, and today it's home to the Flyers Skate Zone, the Philadelphia Flyers' "
                 "training facility. From the neighborhoods around Voorhees Town Center to the quieter streets "
                 "further out, we're a regular for carpet, tile and upholstery cleaning across the township.",
        "local_note": "From the shops around Voorhees Town Center to the residential streets further out, we "
                       "handle a mix of commercial and residential carpet, tile and upholstery work throughout "
                       "Voorhees.",
    },
    {
        "slug": "blackwood-nj",
        "name": "Blackwood",
        "county": "Camden County",
        "zip": "08012",
        "about": "Blackwood is home to Camden County College's 320-acre main campus, established in 1967, "
                 "along with Pennco Tech and a mix of longtime residential streets. It's part of Gloucester "
                 "Township, and we serve homes and businesses throughout the area for carpet, tile and "
                 "upholstery cleaning.",
        "local_note": "With Camden County College and Pennco Tech nearby, we do a fair amount of commercial "
                       "and light-institutional floor care in Blackwood, alongside residential carpet cleaning "
                       "throughout the neighborhood.",
    },
    {
        "slug": "turnersville-nj",
        "name": "Turnersville",
        "county": "Gloucester County",
        "zip": "08012",
        "about": "Turnersville grew from a historic farming crossroads into one of Washington Township's "
                 "busiest commercial hubs, right at the intersection of Route 42 and the Atlantic City "
                 "Expressway. Between the retail corridor and the neighborhoods around it, it's one of our "
                 "most frequent stops for carpet, tile and upholstery cleaning.",
        "local_note": "Turnersville's retail corridor at Route 42 and the Atlantic City Expressway means "
                       "commercial floor care is a regular part of our work here, alongside carpet cleaning "
                       "in the surrounding neighborhoods.",
    },
    {
        "slug": "philadelphia-pa",
        "name": "Philadelphia",
        "state": "PA",
        "county": "Philadelphia County",
        "zip": None,
        "about": "Just across the Delaware River from our South Jersey home base, Philadelphia is one of "
                 "the extended areas we regularly take appointments in &mdash; call ahead to confirm your "
                 "address and schedule, and we'll let you know honestly if it's a fit for the day you need.",
        "local_note": "We take Philadelphia appointments closest to the bridges and river crossings from South "
                       "Jersey &mdash; call ahead and we'll confirm honestly whether your specific address fits "
                       "into that day's schedule.",
    },
    {
        "slug": "wilmington-de",
        "name": "Wilmington",
        "state": "DE",
        "county": "New Castle County",
        "zip": None,
        "about": "Wilmington and the surrounding New Castle County area are part of our extended service "
                 "zone beyond South Jersey. Give us a call to confirm your address and we'll schedule "
                 "honestly around drive time &mdash; no runaround about whether we can make it work.",
        "local_note": "Wilmington appointments work the same way as anywhere in our extended area &mdash; "
                       "we'll confirm your address and schedule around drive time before committing to a day, "
                       "so there's no guessing on either end.",
    },
]

# Real customer reviews reused across town pages that don't have a dedicated one yet.
TOWN_REVIEW_POOL = [
    ("By far the best carpet cleaning and upholstery cleaning company in the area. They're extremely professional and <span class=\"qs-highlight\">pay attention to the finest details</span>. I highly recommend Ace.", "Andrea"),
    ("<span class=\"qs-highlight\">Very professional from start to finish</span>. Great price, and I'll be using their services again.", "Barbara D."),
    ("Our dog had an accident and our robot vacuum rolled it all over the home office. Team came out ASAP and <span class=\"qs-highlight\">cleaned up a disaster</span>. Friendly, accommodating and reasonably priced.", "Ema"),
    ("Will definitely use them again &mdash; <span class=\"qs-highlight\">couldn't be happier with their work</span>!", "Leslie"),
    ("Wonderful family business &mdash; they do a great job and <span class=\"qs-highlight\">are always on time</span>.", "Cyndi"),
    ("<span class=\"qs-highlight\">Fantastic job</span>!!!!", "Christine"),
    ("Great place and <span class=\"qs-highlight\">great people</span>!", "Diane"),
    ("<span class=\"qs-highlight\">Only the best</span> by Ace Cleaners!!", "Diane"),
    ("Ace Cleaning Experts makes our marble tile <span class=\"qs-highlight\">look like new every time</span>.", "Fabrizio"),
    ("Having a home with 2 young children our carpets were a mess. One call and they had us scheduled quickly, arrived early and <span class=\"qs-highlight\">had the job done within the time frame they gave</span>. We'll definitely be repeat customers.", "Dan"),
    ("They are the best around! <span class=\"qs-highlight\">My carpets and my couches came out amazing</span>.", "Joe"),
    ("My carpets <span class=\"qs-highlight\">looked and smelled brand new</span> after they were cleaned. They exceeded my expectations.", "Jeff"),
    ("Ace is <span class=\"qs-highlight\">my favorite carpet cleaner of all time</span>. They are responsive, reliable and trustworthy.", "Anne"),
    ("Nick and Jeff were professional, friendly, and thorough from start to finish. You can really tell <span class=\"qs-highlight\">they take pride in their work</span>.", "Chris"),
    ("I've used Ace for well over 10 years &mdash; not only to support a local company, but because <span class=\"qs-highlight\">they're always professional and always on-time</span>.", "David"),
    ("Great service and people. Been using them <span class=\"qs-highlight\">since 1990, never a complaint</span>.", "Bob"),
]

def town_page(t):
    name = t["name"]
    state = t.get("state", "NJ")
    locality = f'{t["county"]} &middot; {t["zip"]}' if t.get("zip") else t["county"]
    county_variant = (
        "county-badge-red" if t["county"] == "Gloucester County"
        else "county-badge-charcoal" if t["county"] == "Camden County"
        else "county-badge-neutral"
    )
    hero_variant = "" if t["county"] == "Gloucester County" else " dark"
    review_text, review_name = TOWN_REVIEW_POOL[TOWNS.index(t) % len(TOWN_REVIEW_POOL)]
    pricing_line = (
        "wherever you're located in South Jersey" if state == "NJ"
        else f"wherever you're located in the {name} area"
    )
    body = f"""
<section class="page-hero{hero_variant}">
  <div class="wrap">
    <div class="page-hero-copy">
      {breadcrumb([("Home","/"),("Service Areas","/service-areas/"),(name, None)])}
      <span class="county-badge {county_variant}">{locality}</span>
      <h1>Carpet &amp; Floor Cleaning in {name}, {state}</h1>
      <p class="lede">{t["about"]}</p>
      <div class="btn-row">
        <a href="/contact/" class="btn btn-primary">Get Free Quote</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-outline">{icon('phone')} Call {PHONE}</a>
      </div>
    </div>
  </div>
</section>

<div class="wrap">
{quote_snippet(review_text, review_name, color=("red" if hero_variant == " dark" else "charcoal"))}
</div>

<section>
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">What We Offer</span>
      <h2>Services Available in {name}</h2>
    </div>
    <div class="grid-4">
      <div class="svc-card">
        <div class="svc-body">
          <div class="icon">{icon('rug')}</div>
          <h3>Carpet Cleaning</h3>
          <p>Deep steam extraction with Scotchgard protection.</p>
          <a href="/carpet-cleaning-service/" class="go">Learn More {icon('arrow')}</a>
        </div>
      </div>
      <div class="svc-card">
        <div class="svc-body">
          <div class="icon">{icon('sofa')}</div>
          <h3>Upholstery Cleaning</h3>
          <p>Fabric-safe cleaning for sofas &amp; chairs.</p>
          <a href="/upholstery-cleaning/" class="go">Learn More {icon('arrow')}</a>
        </div>
      </div>
      <div class="svc-card">
        <div class="svc-body">
          <div class="icon">{icon('tile')}</div>
          <h3>Tile, Grout &amp; Hardwood</h3>
          <p>Kitchens, bathrooms &amp; floors.</p>
          <a href="/tile-grout-cleaning/" class="go">Learn More {icon('arrow')}</a>
        </div>
      </div>
      <div class="svc-card">
        <div class="svc-body">
          <div class="icon">{icon('building')}</div>
          <h3>Commercial Floor Care</h3>
          <p>Offices, retail &amp; medical spaces.</p>
          <a href="/commercial-carpet-cleaning/" class="go">Learn More {icon('arrow')}</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section style="background:var(--gray);">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Local to {name}</span>
      <h2>What We Clean Most Here</h2>
    </div>
    <p class="lede" style="max-width:760px;">{t["local_note"]}</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Common Questions</span>
      <h2>{name} Cleaning FAQ</h2>
    </div>
    {faq([
        (f"How fast can you get to {name}?", f"{name} is one of our regularly serviced areas, so scheduling is usually quick &mdash; call {PHONE} and we'll give you a real timeframe, not a runaround."),
        (f"Do you serve both homes and businesses in {name}?", f"Yes &mdash; residential and commercial jobs throughout {name}, from single rooms to full offices or storefronts."),
        ("Is pricing different by town?", f"No &mdash; our pricing is based on the job, not the zip code. You'll get the same honest, up-front quote {pricing_line}."),
    ])}
  </div>
</section>

{cta_band(f"Ready to Book in {name}?", f"Fast response, honest pricing, and a crew that shows up when they say they will.")}
"""
    page(f"/service-areas/{t['slug']}/", f"Carpet Cleaning in {name}, {state} | Ace Cleaning Experts",
         f"Professional carpet, tile and upholstery cleaning in {name}, {state}. EPA-certified products, honest pricing. Call {PHONE}.",
         "areas", body)

# Edit/add entries here to revise testimonials — each is (quote, name, town, star_count)
TESTIMONIALS = [
    ("[Add Review Headline]", "[Insert a short, real customer quote here before launch — pull a strong line from a verified Google or Facebook review.]", "[Customer Name]", "[Town]", 5),
    ("[Add Review Headline]", "[Insert a second real, permission-cleared review here.]", "[Customer Name]", "[Town]", 5),
    ("[Add Review Headline]", "[Insert a third real, permission-cleared review here.]", "[Customer Name]", "[Town]", 5),
]

def testimonials(items=TESTIMONIALS):
    cards = []
    for headline, quote, name, town, stars in items:
        star_str = "&#9733;" * stars
        cards.append(f'''      <div class="testi-card">
        <div class="quote-mark">&ldquo;</div>
        <div class="stars">{star_str}</div>
        <p class="quote-body">{quote}</p>
        <div class="who">{name}</div>
        <div class="where">{town}, NJ</div>
      </div>''')
    grid = "\n".join(cards)
    return f'<div class="testi-grid">\n{grid}\n    </div>\n    <p class="testi-note">Swap each card for a real, permission-cleared review before launch.</p>'

def testimonial_carousel(items=TESTIMONIALS):
    slides = []
    for i, (headline, quote, name, town, stars) in enumerate(items):
        star_str = "&#9733;" * stars
        active = " is-active" if i == 0 else ""
        slides.append(f'''    <div class="carousel-slide{active}" data-slide="{i}">
      <div class="stars">{star_str}</div>
      <h3 class="carousel-headline">{headline}</h3>
      <p class="carousel-quote">{quote}</p>
      <div class="who">{name}</div>
      <div class="where">{town}, NJ</div>
    </div>''')
    slides_html = "\n".join(slides)
    dots = "\n    ".join(
        f'<button type="button" class="carousel-dot{" is-active" if i == 0 else ""}" data-goto="{i}" aria-label="Show testimonial {i + 1}"></button>'
        for i in range(len(items))
    )
    return f'''<div class="testi-carousel" id="testiCarousel">
  <button type="button" class="carousel-arrow carousel-prev" aria-label="Previous testimonial">{icon('chevron')}</button>
  <div class="carousel-track">
{slides_html}
  </div>
  <button type="button" class="carousel-arrow carousel-next" aria-label="Next testimonial">{icon('chevron')}</button>
</div>
<div class="carousel-dots">
    {dots}
</div>
<p class="testi-note">Swap each slide for a real, permission-cleared review before launch.</p>'''

print("build.py scaffold loaded")

# ============================================================== HOME ====
home_body = f"""
<section class="hero hero-split">
  <div class="wrap hero-split-wrap">
    <div class="hero-copy">
      <span class="eyebrow">South Jersey's Carpet, Tile &amp; Upholstery Cleaning Experts</span>
      <h1>Your Family's Home Deserves a Family You Can Trust</h1>
      <p class="lede">Serving homes and businesses across South Jersey for 40+ years with deep steam extraction, EPA-certified products, and a crew that treats your home like their own. No upsells, no runaround &mdash; just honest carpet, tile and upholstery cleaning, done right the first time.</p>
      <div class="btn-row">
        <a href="/contact/" class="btn btn-primary">Get Free Quote</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-outline">{icon('phone')} Call {PHONE}</a>
      </div>
    </div>
    <div class="hero-image-wrap">
      <img src="/images/hero-family.jpg" alt="Three generations of the Ace Cleaning Experts family" class="hero-visual hero-photo">
    </div>
  </div>
</section>

<div class="wrap">
{quote_snippet("I've been using Ace Cleaning Experts <span class=\"qs-highlight\">for over 20 years</span>, and they consistently do a fantastic job. Professional, efficient, reasonably priced, and incredibly courteous.", "Karen")}
</div>

{stats_bar()}

<section id="before-after" class="ba-section">
  <div class="wrap ba-intro-row">
    <div class="ba-intro-copy">
      <span class="eyebrow">The Proof</span>
      <h2>Real Results. Every Time.</h2>
      <p class="lede">We don't just clean &mdash; we transform your floors. See the difference for yourself.</p>
      <a href="/our-work/" class="btn btn-primary">View More Results {icon('arrow')}</a>
    </div>
    <div class="ba-intro-slider">
      <div class="ba-slider">
        <img src="/images/carpet-before-v2.webp" alt="Dirty, stained carpet before Ace Cleaning Experts deep clean" class="ba-before">
        <img src="/images/carpet-after-v2.webp" alt="Same carpet after Ace Cleaning Experts deep clean, looking like new" class="ba-after">
        <span class="ba-tag before-tag">Before</span>
        <span class="ba-tag after-tag">After</span>
        <div class="ba-handle"></div>
        <input type="range" min="0" max="100" value="50" class="ba-range" aria-label="Drag to compare before and after">
      </div>
    </div>
  </div>
  <div class="wrap">
    <div class="ba-mini-grid">
      <div class="ba-mini">
        <div class="ba-slider ba-slider-mini">
          <img src="/images/carpet-mini-before.webp" alt="Dirty carpet before Ace Cleaning Experts cleaning" class="ba-before">
          <img src="/images/carpet-mini-after.webp" alt="Same carpet after Ace Cleaning Experts cleaning" class="ba-after">
          <span class="ba-tag before-tag">Before</span>
          <span class="ba-tag after-tag">After</span>
          <div class="ba-handle"></div>
          <input type="range" min="0" max="100" value="50" class="ba-range" aria-label="Drag to compare carpet before and after">
        </div>
        <div class="ba-mini-label">Carpet</div>
      </div>
      <div class="ba-mini">
        <div class="ba-slider ba-slider-mini">
          <img src="/images/tile-mini-before.webp" alt="Dirty, stained grout before Ace Cleaning Experts tile cleaning" class="ba-before">
          <img src="/images/tile-mini-after.webp" alt="Same tile floor after Ace Cleaning Experts tile cleaning, grout restored" class="ba-after">
          <span class="ba-tag before-tag">Before</span>
          <span class="ba-tag after-tag">After</span>
          <div class="ba-handle"></div>
          <input type="range" min="0" max="100" value="50" class="ba-range" aria-label="Drag to compare tile before and after">
        </div>
        <div class="ba-mini-label">Tile</div>
      </div>
      <div class="ba-mini">
        <div class="ba-slider ba-slider-mini">
          <img src="/images/upholstery-mini-before-v2.webp" alt="Stained upholstery before Ace Cleaning Experts cleaning" class="ba-before">
          <img src="/images/upholstery-mini-after-v2.webp" alt="Same upholstery after Ace Cleaning Experts cleaning" class="ba-after">
          <span class="ba-tag before-tag">Before</span>
          <span class="ba-tag after-tag">After</span>
          <div class="ba-handle"></div>
          <input type="range" min="0" max="100" value="50" class="ba-range" aria-label="Drag to compare upholstery before and after">
        </div>
        <div class="ba-mini-label">Upholstery</div>
      </div>
    </div>
  </div>
</section>

{card_divider()}

<section id="why-ace">
  <div class="wrap why-row">
    <div class="card-fan">
      <img src="/images/why-ace-team.webp" alt="Ace Cleaning Experts owner and family in front of the company van" class="why-ace-photo">
    </div>
    <div>
      <span class="eyebrow">Why South Jersey Chooses Ace</span>
      <h2>Experience. Integrity. Results You Can Count On.</h2>
      <p class="lede" style="font-size:1.05rem;">We've been doing this for 40+ years &mdash; not because it's trendy, but because South Jersey homes and businesses keep calling us back.</p>
      <div class="benefit-grid">
        <div class="benefit-item"><span class="b-icon">{icon('shield')}</span><div><strong>Veteran-Owned</strong><span>Proudly served our country. Now proudly serving you.</span></div></div>
        <div class="benefit-item"><span class="b-icon">{icon('users')}</span><div><strong>Experienced Technicians</strong><span>Trained and experienced in the latest techniques.</span></div></div>
        <div class="benefit-item"><span class="b-icon">{icon('home')}</span><div><strong>Family-Owned &amp; Operated</strong><span>Local, honest and committed to our community.</span></div></div>
        <div class="benefit-item"><span class="b-icon">{icon('check')}</span><div><strong>Satisfaction Guaranteed</strong><span>If you're not happy, we'll make it right.</span></div></div>
        <div class="benefit-item"><span class="b-icon">{icon('droplet')}</span><div><strong>Professional Equipment</strong><span>Truck-mounted systems for a deeper clean.</span></div></div>
        <div class="benefit-item"><span class="b-icon">{icon('star')}</span><div><strong>40+ Years Experience</strong><span>Serving South Jersey since 1983.</span></div></div>
      </div>
    </div>
  </div>
</section>

<section style="background:var(--gray);">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Our Cleaning Services</span>
      <h2>Professional Cleaning. Proven Results.</h2>
      <p class="lede" style="margin:0 auto;">Advanced cleaning solutions for a healthier, cleaner space.</p>
    </div>
    <div class="grid-4">
      {service_showcase_card(
          "/carpet-cleaning-service/", "Residential Service", "Revive Your Carpets",
          "Deep steam extraction removes embedded dirt, allergens and stubborn stains for a fresher, healthier home.",
          [("paw", "Safe for Kids &amp; Pets"), ("clock", "Fast Dry Time"), ("leaf", "Eco Friendly")],
          "/images/carpet-service.webp", "Clean carpet after Ace Cleaning Experts service",
      )}
      {service_showcase_card(
          "/tile-grout-cleaning/", "Residential Service", "Restore Tile &amp; Grout",
          "Grout scrubbed back toward its original color &mdash; deep cleaning only, no upsells.",
          [("sparkle", "Deep Cleaning"), ("shield", "Protects Longer"), ("check", "No Harsh Chemicals")],
          "/images/tile-service.webp", "Mosaic tile floor cleaned by Ace Cleaning Experts, dirty grout restored to clean",
      )}
      {service_showcase_card(
          "/upholstery-cleaning/", "Residential Service", "Refresh Your Furniture",
          "Fabric-safe cleaning lifts stains and odors without soaking, over-wetting or fading your furniture.",
          [("steam", "Odor Removal"), ("shield", "Stain Protection"), ("sofa", "Extends Life")],
          "/images/upholstery-gallery-02.webp", "Recliner cushion before and after Ace Cleaning Experts upholstery cleaning",
      )}
      {service_showcase_card(
          "/commercial-carpet-cleaning/", "Commercial Service", "Keep Your Business Looking Its Best",
          "Flexible scheduling that works around your business hours, not ours.",
          [("building", "Flexible Scheduling"), ("shield", "Trusted by Businesses"), ("calendar", "Custom Solutions")],
          "/images/commercial-service.webp", "Area rug being deep cleaned by Ace Cleaning Experts",
      )}
    </div>
    <div class="trust-badge-box">
      {icon('ace_card')}
      <div>
        <strong>Veteran-Owned. Family-Operated. Serving South Jersey Since 1983.</strong>
        <div class="sub">Fully Insured &bull; Professional Equipment &bull; 100% Satisfaction Guaranteed</div>
      </div>
    </div>
    <p style="text-align:center; margin-top:40px;"><a href="/services/" class="btn btn-outline">View All Services</a></p>
  </div>
</section>

<section id="meet-ace">
  <div class="wrap meet-ace-row">
    <div>
      <span class="eyebrow">Meet Ace</span>
      <h2>The People Behind Ace</h2>
      <p class="lede">Veteran-owned and family-operated, serving South Jersey for 40+ years. The person who quotes your job is accountable for the crew that shows up to do it &mdash; no corporate hand-offs, no call centers.</p>
      <p style="margin:22px 0 0;"><a href="/about-us/" class="btn btn-outline">Learn More About Us {icon('arrow')}</a></p>
    </div>
    <div class="card-fan">
      <img src="/images/meet-ace-team-v2.webp" alt="The Ace Cleaning Experts family washing the company van together" class="meet-ace-photo">
    </div>
  </div>
</section>

<section style="background:var(--gray);" id="areas">
  <div class="wrap area-row">
    <div>
      <span class="eyebrow">Where We Work</span>
      <h2>Proudly Serving South Jersey</h2>
      <p class="lede">Home base in Sewell, Deptford and Haddonfield &mdash; with crews out across Gloucester and Camden counties, and beyond, every week.</p>
      <p style="margin-top:26px;"><a href="/service-areas/" class="btn btn-primary">View All Service Areas</a></p>
    </div>
    <div class="card-fan">
      <img src="/images/team-sponsor-jersey-v1.webp" alt="Ace Cleaning Experts logo on the back of a sponsored local youth baseball team jersey" class="area-badge">
    </div>
  </div>
</section>

<section id="faq" class="section-red">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Questions</span>
      <h2>Frequently Asked Questions</h2>
    </div>
    {faq([
        ("How often should I have my carpets cleaned?", "Most homes do well with a deep clean every 12&ndash;18 months; homes with kids, pets or allergy sufferers often benefit from cleaning closer to every 6&ndash;12 months."),
        ("Is your process safe for kids and pets?", "Yes &mdash; our cleaning agents are EPA-certified and chosen to be safe once dry, while still being tough on dirt, bacteria and allergens."),
        ("Do you offer commercial cleaning?", "Yes, we work with offices, retail spaces, restaurants and medical facilities, including evening and weekend scheduling."),
        ("What areas do you serve?", "We're based in Sewell, Deptford and Haddonfield, with regular jobs throughout Gloucester, Camden, Atlantic and Cape May counties, plus Philadelphia and Wilmington, DE."),
        ("How long until I can walk on the carpet?", "Most carpets are dry to the touch within a few hours. We'll walk you through drying time before we leave."),
        ("Do I need to move my furniture?", "Our technicians move light furniture as part of the visit &mdash; just let us know about large or fragile pieces when you book."),
    ])}
  </div>
</section>

{cta_band("Ready to Love Your Floors Again?", "Veteran-owned. Family-operated. No upsells, no runaround &mdash; just honest work, every time.")}
"""
page("/", "Ace Cleaning Experts | South Jersey's Trusted Carpet Cleaning Experts",
     "Veteran-owned, family-operated carpet, tile and upholstery cleaning serving Sewell, Deptford, Haddonfield and all of South Jersey for 40+ years. Call 856-582-1711.",
     "home", home_body)

# ============================================================ OUR WORK ===
our_work_body = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="page-hero-copy">
      {breadcrumb([("Home","/"),("Our Work", None)])}
      <span class="eyebrow">See The Difference</span>
      <h1>Our Work</h1>
      <p class="lede">Real before-and-after results from carpet, tile and upholstery jobs across South Jersey &mdash; no stock photos, just our own work.</p>
    </div>
  </div>
</section>

<div class="wrap">
{quote_snippet("Will definitely use them again &mdash; <span class=\"qs-highlight\">couldn't be happier with their work</span>!", "Leslie")}
</div>

<section>
  <div class="wrap">
    {gallery_grid()}
  </div>
</section>

{cta_band("Ready to See Results Like This in Your Home?", "Fast response, honest pricing, and a crew that shows up when they say they will.")}
"""
page("/our-work/", "Our Work | Real Before & After Photos | Ace Cleaning Experts",
     "See real before-and-after photos from Ace Cleaning Experts' carpet, tile and upholstery cleaning jobs across South Jersey.",
     "our-work", our_work_body)

# ============================================================== ABOUT ===
about_body = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="page-hero-copy">
      {breadcrumb([("Home","/"),("About Us", None)])}
      <span class="eyebrow">Our Story</span>
      <h1>Four Decades of Clean Carpets and Floors</h1>
      <p class="lede">Ace Cleaning Experts started the way most good local businesses do &mdash; with a family, a van, and a determination to do the job right. For over 40 years, we've helped South Jersey families and businesses restore carpets, tile, upholstery and grout &mdash; eliminating stubborn dirt, stains and odors along the way. We're still locally owned and operated: not a franchise, not a national call center, just the same commitment to honest pricing and work you can trust.</p>
    </div>
  </div>
</section>

<div class="wrap">
{quote_snippet("Consistent, quality workmanship and price point <span class=\"qs-highlight\">for decades</span>. There is no other competition that comes close.", "Glenn")}
</div>

<section>
  <div class="wrap">
    <div class="feature-row">
      <div class="feature-copy">
        <img src="/images/us-flag-v1.webp" alt="American flag" style="width:60px; height:auto; margin-bottom:16px; border-radius:2px; box-shadow:var(--shadow-sm);">
        <h3>Owned by Jeff DeNobile, U.S. Marine Corps Veteran</h3>
        <p class="lede" style="font-size:1.05rem;">Ace Cleaning Experts is owned and run by Jeff DeNobile, a U.S. Marine Corps veteran who brought that same discipline and attention to detail into the business. We're proud to be veteran-owned and family-operated, serving the same South Jersey communities we call home. The person who quotes your job is accountable for the crew that shows up to do it &mdash; no corporate hand-offs, no surprise fees.</p>
      </div>
      <div class="feature-visual"><img class="card-edge" src="/images/veteran-owned.webp" alt="Jeff DeNobile, owner of Ace Cleaning Experts, in U.S. Marine Corps dress uniform" style="width:100%;height:100%;object-fit:cover;border-radius:var(--radius);"></div>
    </div>
    <div class="feature-row reverse">
      <div class="feature-copy">
        <h3>The Same Care We'd Want in Our Own Homes</h3>
        <p class="lede" style="font-size:1.05rem;">Every technician is trained on EPA-certified cleaning agents and modern extraction equipment, and every job wraps up with a walkthrough so you know exactly what was done.</p>
      </div>
      <div class="feature-visual"><img class="card-edge" src="/images/technician-care.webp" alt="Ace Cleaning Experts technicians at work cleaning carpets" style="width:100%;height:100%;object-fit:cover;border-radius:var(--radius);"></div>
    </div>
  </div>
</section>

<section class="section-red">
  <div class="wrap" style="max-width:820px; text-align:center;">
    <span class="eyebrow">What We Solve</span>
    <h2>Problems Big and Small, Solved Right</h2>
    <p class="lede" style="margin:0 auto;">Whether it's one stubborn stain or odor you can't get out, a full-home deep clean, or something larger like water damage restoration, we've got 40+ years of experience figuring out the right fix. Our staff keeps learning the newest techniques so every job gets the highest-quality clean at a fair price &mdash; and we'll always tell you honestly what your carpet, tile or upholstery actually needs.</p>
  </div>
</section>

<section class="section-tint">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Credentials</span>
      <h2>What Backs Up Our Work</h2>
    </div>
    <div class="grid-4">
      <div class="svc-card" style="text-align:center; padding:30px 22px;">
        <div class="icon" style="margin:0 auto 16px;">{icon('shield')}</div>
        <h3 style="font-size:1rem;">Fully Insured</h3>
        <p style="margin:0; color:var(--charcoal-70); font-size:0.9rem;">Every job is covered, start to finish.</p>
      </div>
      <div class="svc-card" style="text-align:center; padding:30px 22px;">
        <div class="icon" style="margin:0 auto 16px;">{icon('droplet')}</div>
        <h3 style="font-size:1rem;">EPA-Certified Products</h3>
        <p style="margin:0; color:var(--charcoal-70); font-size:0.9rem;">Safe for kids, pets and allergy sufferers.</p>
      </div>
      <div class="svc-card" style="text-align:center; padding:30px 22px;">
        <div class="icon" style="margin:0 auto 16px;">{icon('star')}</div>
        <h3 style="font-size:1rem;">Veteran-Owned</h3>
        <p style="margin:0; color:var(--charcoal-70); font-size:0.9rem;">Proudly built and run by a veteran.</p>
      </div>
      <div class="svc-card" style="text-align:center; padding:30px 22px;">
        <div class="icon" style="margin:0 auto 16px;">{icon('check')}</div>
        <h3 style="font-size:1rem;">Scotchgard Protection</h3>
        <p style="margin:0; color:var(--charcoal-70); font-size:0.9rem;">Applied after every deep clean.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Our Equipment</span>
      <h2>Professional-Grade Truck-Mounted Cleaning Systems</h2>
      <p class="lede" style="margin:0 auto;">Every job runs through a HydraMaster Titan truck-mounted extraction system &mdash; the same commercial-grade equipment top cleaning companies rely on, delivering higher heat, stronger suction, and faster dry times than rental machines or portable units.</p>
    </div>
    <div class="grid-2" style="gap:24px; margin-top:36px;">
      <img src="/images/equipment-titan-575-v1.webp" alt="HydraMaster Titan 575 truck-mounted carpet cleaning system in the Ace Cleaning Experts van" style="width:100%; border-radius:var(--radius); box-shadow:var(--shadow-sm); aspect-ratio:3/4; object-fit:cover;">
      <img src="/images/equipment-02.webp" alt="Professional cleaning hoses and equipment organized in the Ace Cleaning Experts van" style="width:100%; border-radius:var(--radius); box-shadow:var(--shadow-sm); aspect-ratio:3/4; object-fit:cover;">
    </div>
  </div>
</section>

{cta_band("Come See Why South Jersey Calls Ace First", "Talk to a real person on the first ring &mdash; no scripts, no upsells.")}
"""
page("/about-us/", "About Ace Cleaning Experts | Veteran-Owned, Family-Operated NJ Cleaners",
     "Meet Ace Cleaning Experts: a veteran-owned, family-operated carpet and floor cleaning company serving South Jersey for 40+ years. Local, insured, EPA-certified.",
     "about", about_body)

# ============================================================ SERVICES ==
services_body = f"""
<section class="page-hero dark">
  <div class="wrap">
    <div class="page-hero-copy">
      {breadcrumb([("Home","/"),("Services", None)])}
      <span class="eyebrow">What We Do</span>
      <h1>Cleaning Services for Every Room and Every Business</h1>
      <p class="lede">Carpet, upholstery, tile, grout, hardwood and commercial floor care &mdash; all handled by the same local crew, with EPA-certified products and 40+ years of hands-on experience behind every job.</p>
    </div>
  </div>
</section>

<div class="wrap">
{quote_snippet("Ace cleaned the tile in my kitchen and two bathrooms, plus two area rugs and my basement carpeting and stairs. <span class=\"qs-highlight\">Everything looks great</span>, they were on time, and pricing was fair. Will use them again for my floor cleaning needs!", "Christopher", color="red")}
</div>

<section>
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">One Company, Every Surface</span>
      <h2>Why Homeowners Use Ace for More Than One Room</h2>
      <p class="lede" style="margin:0 auto;">Most cleaning companies specialize in one thing. We handle carpet, upholstery, tile, grout, hardwood and commercial floors with the same crew, the same pricing approach, and the same point of contact &mdash; so you're not juggling three different companies and three different invoices to get your whole home or business done.</p>
    </div>
    <div class="grid-4">
      <div class="svc-card">
        <img src="/images/carpet-service.webp" alt="Clean carpet after Ace Cleaning Experts service" class="svc-photo">
        <div class="svc-body">
          <div class="icon">{icon('rug')}</div>
          <h3>Carpet Cleaning</h3>
          <p>Deep steam extraction pulls out dirt, allergens and set-in stains most vacuums never touch &mdash; with settings adjusted to your specific carpet's fiber type.</p>
          <a href="/carpet-cleaning-service/" class="go">Learn More {icon('arrow')}</a>
        </div>
      </div>
      <div class="svc-card">
        <img src="/images/upholstery-gallery-02.webp" alt="Recliner cushion before and after Ace Cleaning Experts upholstery cleaning" class="svc-photo">
        <div class="svc-body">
          <div class="icon">{icon('sofa')}</div>
          <h3>Upholstery Cleaning</h3>
          <p>Fabric-safe treatment for sofas, sectionals and dining chairs &mdash; leather included, tested first so there are no surprises.</p>
          <a href="/upholstery-cleaning/" class="go">Learn More {icon('arrow')}</a>
        </div>
      </div>
      <div class="svc-card">
        <img src="/images/tile-service.webp" alt="Mosaic tile floor cleaned by Ace Cleaning Experts, dirty grout restored to clean" class="svc-photo">
        <div class="svc-body">
          <div class="icon">{icon('tile')}</div>
          <h3>Tile, Grout &amp; Hardwood</h3>
          <p>Grout scrubbed back toward its original color &mdash; deep cleaning only, and we'll tell you honestly if something needs more than that.</p>
          <a href="/tile-grout-cleaning/" class="go">Learn More {icon('arrow')}</a>
        </div>
      </div>
      <div class="svc-card">
        <img src="/images/commercial-service.webp" alt="Area rug being deep cleaned by Ace Cleaning Experts" class="svc-photo">
        <div class="svc-body">
          <div class="icon">{icon('building')}</div>
          <h3>Commercial Floor Care</h3>
          <p>Flexible after-hours scheduling for offices and retail, priced by square footage or a walkthrough quote.</p>
          <a href="/commercial-carpet-cleaning/" class="go">Learn More {icon('arrow')}</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section style="background:var(--gray);">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">How It Works</span>
      <h2>From Call to Clean, Here's What to Expect</h2>
    </div>
    {process_steps([
        ("Call or request a quote", "Tell us what you need cleaned and where &mdash; most estimates are handled right over the phone."),
        ("We inspect and recommend", "Our technician looks at the actual carpet, tile or fabric and recommends only what it needs."),
        ("Deep clean with certified equipment", "EPA-certified solutions and professional-grade extraction equipment do the heavy lifting."),
        ("Scotchgard, walkthrough &amp; done", "We protect the finish, walk you through the results, and leave the space ready to use."),
    ])}
  </div>
</section>

<section class="section-red">
  <div class="wrap" style="max-width:780px; text-align:center;">
    <span class="eyebrow">Our Guarantee</span>
    <h2>If You're Not Satisfied, We'll Make It Right</h2>
    <p class="lede" style="margin:0 auto;">No hedging, no fine print. Customers are often surprised to find that a cleaning company can still feel personable and locally owned &mdash; we're the same crew every visit, committed to getting the job done right the first time, not a call-center dispatching whoever's available.</p>
  </div>
</section>

{cta_band()}
"""
page("/services/", "Cleaning Services | Ace Cleaning Experts, South Jersey",
     "Explore carpet, upholstery, tile, grout, hardwood floor and commercial cleaning services from Ace Cleaning Experts &mdash; South Jersey's veteran-owned cleaning crew.",
     "services", services_body)

# ==================================================== CARPET CLEANING ===
carpet_body = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="page-hero-copy">
      {breadcrumb([("Home","/"),("Services","/services/"),("Carpet Cleaning", None)])}
      <span class="eyebrow">Residential &amp; Light Commercial</span>
      <h1>Carpet Cleaning That Actually Lasts</h1>
      <p class="lede">Deep steam extraction pulls dirt, allergens and set-in stains out of the fibers &mdash; not just off the surface &mdash; and every job finishes with a Scotchgard application.</p>
      <div class="btn-row">
        <a href="/contact/" class="btn btn-primary">Get Free Quote</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-outline">{icon('phone')} Call {PHONE}</a>
      </div>
    </div>
  </div>
</section>

<div class="wrap">
{quote_snippet("Our dog had an accident and our robot vacuum rolled over it and all over the home office. Team came out ASAP, within 2 hrs of me calling, and <span class=\"qs-highlight\">cleaned up a disaster</span>. Friendly, accommodating and reasonably priced.", "Ema")}
</div>

<section style="background:var(--gray);">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Our Process</span>
      <h2>How We Clean Every Carpet</h2>
    </div>
    <div class="grid-2" style="gap:32px;">
      <div>
        <h3 style="font-size:1.15rem;">We Assess Before We Clean</h3>
        <p style="color:var(--charcoal-70);">Before any equipment comes out, we walk the space and look for heavily soiled areas and visible stains that need spot pre-treatment first. That assessment shapes the rest of the job &mdash; we don't run the same generic pass over every carpet.</p>
      </div>
      <div>
        <h3 style="font-size:1.15rem;">Built for Every Fiber Type</h3>
        <p style="color:var(--charcoal-70);">Berber, frieze, wool, cut pile, loop pile &mdash; every fiber reacts differently to heat, moisture and agitation. We adjust our equipment settings to match your specific carpet, so it gets cleaned effectively without getting damaged in the process.</p>
      </div>
    </div>
    <div style="margin-top:28px; max-width:760px;">
      <h3 style="font-size:1.15rem;">Pet Stains &amp; Odor: Our Enzyme Enhancer</h3>
      <p style="color:var(--charcoal-70); margin:0;">Standard shampoo covers up pet odor instead of removing it. We use a patented enzyme enhancer that breaks down the organic compounds causing the smell at the source &mdash; not just the surface &mdash; so the odor doesn't come back once the carpet dries.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">What's Included</span>
      <h2>Every Carpet Cleaning Visit Covers</h2>
    </div>
    <ul class="checklist grid-2" style="display:grid;">
      <li>{icon('spade')} Pre-treatment of high-traffic areas and visible stains</li>
      <li>{icon('spade')} Hot water / steam extraction with EPA-certified solutions</li>
      <li>{icon('spade')} Pet odor and stain treatment where needed</li>
      <li>{icon('spade')} Scotchgard fabric protector applied after cleaning</li>
      <li>{icon('spade')} Fast-dry techniques to minimize downtime</li>
      <li>{icon('spade')} Straightforward, honest pricing quoted up front</li>
    </ul>
  </div>
</section>

<section style="background:var(--gray);">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Real Results</span>
      <h2>Recent Carpet Cleaning Work</h2>
    </div>
    {gallery_grid([
        ("gallery-05", "Gray carpet before and after cleaning"),
        ("gallery-09", "Stained carpet before and after deep cleaning"),
        ("gallery-08", "Staircase carpet before and after cleaning, side by side"),
        ("gallery-07", "Restaurant carpet mid-clean, dirt lifted with hose"),
    ])}
  </div>
</section>

<section class="section-red">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Common Questions</span>
      <h2>Carpet Cleaning FAQ</h2>
    </div>
    {faq([
        ("How often should I have my carpets cleaned?", "Most homes do well with a deep clean every 12&ndash;18 months; homes with kids, pets or allergy sufferers often benefit from cleaning closer to every 6&ndash;12 months."),
        ("Is your process safe for kids and pets?", "Yes &mdash; our cleaning agents are EPA-certified and chosen specifically to be safe once dry, while still being tough on dirt, bacteria and allergens."),
        ("How long until I can walk on the carpet?", "Most carpets are dry to the touch within a few hours. We'll walk you through drying time and care tips before we leave."),
        ("Do I need to move my furniture?", "Our technicians move light furniture as part of the visit. For large or fragile pieces, just let us know when you book and we'll plan around it."),
    ])}
  </div>
</section>

{related_links("/carpet-cleaning-service/")}

{cta_band()}
"""
page("/carpet-cleaning-service/", "Carpet Cleaning in South Jersey | Ace Cleaning Experts",
     "Professional carpet cleaning in Sewell, Deptford, Haddonfield and South Jersey. EPA-certified deep steam extraction with Scotchgard protection. Call 856-582-1711.",
     "services", carpet_body)

# ================================================= UPHOLSTERY CLEANING ==
uphol_body = f"""
<section class="page-hero dark">
  <div class="wrap">
    <div class="page-hero-copy">
      {breadcrumb([("Home","/"),("Services","/services/"),("Upholstery Cleaning", None)])}
      <span class="eyebrow">Sofas &middot; Sectionals &middot; Dining Chairs</span>
      <h1>Upholstery Cleaning That Respects the Fabric</h1>
      <p class="lede">Every fabric is different, so we test and match our method to the material before we start &mdash; lifting stains and odor without soaking, over-wetting or fading the piece you care about.</p>
      <div class="btn-row">
        <a href="/contact/" class="btn btn-primary">Get Free Quote</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-outline">{icon('phone')} Call {PHONE}</a>
      </div>
    </div>
  </div>
</section>

<div class="wrap">
{quote_snippet("By far the best carpet cleaning and upholstery cleaning company in the area. They're extremely professional and <span class=\"qs-highlight\">pay attention to the finest details</span>. Quick to get back to you regarding appointments. I highly recommend Ace.", "Andrea", color="red")}
</div>

<section style="background:var(--gray);">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Our Process</span>
      <h2>Leather or Fabric, Tested Before We Clean</h2>
    </div>
    <div class="grid-2" style="gap:32px;">
      <div>
        <h3 style="font-size:1.15rem;">We Clean Both Leather and Fabric</h3>
        <p style="color:var(--charcoal-70);">Sofas, sectionals, dining chairs, accent pieces &mdash; whether it's fabric or leather, we match our method to the material instead of using one generic approach on everything that comes through the door.</p>
      </div>
      <div>
        <h3 style="font-size:1.15rem;">We Test First, Always</h3>
        <p style="color:var(--charcoal-70);">Where it applies, we test an inconspicuous spot before starting the full clean &mdash; checking how the material responds before we commit to a method, so there are no surprises on the piece you care about.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">What's Included</span>
      <h2>Every Upholstery Visit Covers</h2>
    </div>
    <ul class="checklist grid-2" style="display:grid;">
      <li>{icon('spade')} Fabric identification and spot-testing before cleaning</li>
      <li>{icon('spade')} EPA-certified, low-moisture cleaning agents</li>
      <li>{icon('spade')} Targeted stain and odor removal</li>
      <li>{icon('spade')} Scotchgard protection to guard against future spills</li>
      <li>{icon('spade')} Sofas, sectionals, loveseats, dining and accent chairs</li>
      <li>{icon('spade')} Faster dry times than DIY rental machines</li>
    </ul>
  </div>
</section>

<section style="background:var(--gray);">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Real Results</span>
      <h2>Recent Upholstery Cleaning Work</h2>
    </div>
    {gallery_grid([
        ("upholstery-mini-before-v2", "Stained upholstery cushion before cleaning"),
        ("upholstery-gallery-01", "Recliner cushion with stain before cleaning"),
        ("upholstery-gallery-02", "Recliner cushion before and after cleaning, side by side"),
        ("upholstery-gallery-03", "Living room sofa and carpet after cleaning"),
    ])}
  </div>
</section>

<section class="section-red">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Common Questions</span>
      <h2>Upholstery Cleaning FAQ</h2>
    </div>
    {faq([
        ("Will cleaning shrink or fade my furniture?", "We test each fabric first and choose a method suited to it, which is exactly why we avoid the over-wetting that causes shrinking or color bleed with DIY machines."),
        ("Can you get pet odor out of a couch?", "In most cases, yes. Odor treatment is a standard part of our upholstery process, not an upcharge."),
        ("How long does a sofa take to dry?", "Most pieces are dry within a few hours thanks to our low-moisture approach and extraction equipment."),
        ("Do you clean leather?", "Yes &mdash; we clean both leather and fabric upholstery. We test the piece first and match our method to the material rather than using the same approach on everything."),
    ])}
  </div>
</section>

{related_links("/upholstery-cleaning/")}

{cta_band()}
"""
page("/upholstery-cleaning/", "Upholstery Cleaning in South Jersey | Ace Cleaning Experts",
     "Professional fabric upholstery cleaning for sofas, sectionals and chairs across South Jersey. Fabric-safe, EPA-certified, Scotchgard-protected. Call 856-582-1711.",
     "services", uphol_body)

# ============================================== TILE / GROUT / HARDWOOD =
tile_body = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="page-hero-copy">
      {breadcrumb([("Home","/"),("Services","/services/"),("Tile, Grout &amp; Hardwood", None)])}
      <span class="eyebrow">Kitchens &middot; Bathrooms &middot; Hardwood Floors</span>
      <h1>Tile, Grout &amp; Hardwood Floor Cleaning</h1>
      <p class="lede">Grout holds onto dirt long after mopping stops working. We deep-clean it back toward its original color, and we clean hardwood floors the right way &mdash; without soaking or dulling the finish.</p>
      <div class="btn-row">
        <a href="/contact/" class="btn btn-primary">Get Free Quote</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-outline">{icon('phone')} Call {PHONE}</a>
      </div>
    </div>
  </div>
</section>

<div class="wrap">
{quote_snippet("On time and did a good job cleaning tile and grout for a <span class=\"qs-highlight\">reasonable price</span>.", "Mark")}
</div>

<section style="background:var(--gray);">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">What We Do</span>
      <h2>Deep Cleaning, Done Honestly</h2>
    </div>
    <p class="lede" style="max-width:760px;">We focus on one thing and do it well: deep cleaning tile and grout back toward its original color. We don't apply sealer after cleaning, and we don't offer grout recoloring or staining as an add-on. If your grout needs one of those services, we'll tell you honestly instead of upselling something outside our specialty &mdash; so you know exactly what you're getting before we start.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">What's Included</span>
      <h2>Every Visit Covers</h2>
    </div>
    <ul class="checklist grid-2" style="display:grid;">
      <li>{icon('spade')} Deep tile and grout cleaning to lift embedded dirt</li>
      <li>{icon('spade')} EPA-certified solutions safe for kitchens and bathrooms</li>
      <li>{icon('spade')} Hardwood floor cleaning suited to the floor's finish</li>
      <li>{icon('spade')} Mildew and grime treatment in high-moisture areas</li>
      <li>{icon('spade')} Honest guidance on what grout can and can't be restored</li>
      <li>{icon('spade')} Straightforward, up-front pricing</li>
    </ul>
  </div>
</section>

<section style="background:var(--gray);">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Real Results</span>
      <h2>Recent Tile &amp; Grout Work</h2>
    </div>
    {gallery_grid([
        ("tile-gallery-01", "Kitchen tile floor being cleaned, wet clean patches visible"),
        ("gallery-10-v2", "Rotary tile cleaning tool in action on stone floor"),
        ("tile-service", "Mosaic tile floor cleaned, dirty grout restored to clean"),
        ("tile-mini-after", "Same tile floor after cleaning, grout restored"),
    ])}
  </div>
</section>

<section class="section-red">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Common Questions</span>
      <h2>Tile, Grout &amp; Hardwood FAQ</h2>
    </div>
    {faq([
        ("Can you make old grout look new again?", "Deep cleaning brings most grout back significantly lighter and more even in color. Severely stained or damaged grout may need sealing or re-grouting from a specialist &mdash; we'll tell you honestly when that's the case rather than trying to clean past the point it'll help."),
        ("Is the process safe for hardwood floors?", "Yes &mdash; we match our approach to your floor's finish and avoid the over-wetting that causes warping or dulling."),
        ("How long before I can walk on the floor?", "Tile and grout are typically usable within an hour or two; hardwood dry times vary slightly by finish, and we'll confirm before we leave."),
        ("Do you seal grout after cleaning?", "No &mdash; we focus on deep cleaning only and don't offer sealing as part of our service. If sealing is something you're looking for, we can point you toward it honestly rather than upsell something we don't specialize in."),
    ])}
  </div>
</section>

{related_links("/tile-grout-cleaning/")}

{cta_band()}
"""
page("/tile-grout-cleaning/", "Tile, Grout &amp; Hardwood Floor Cleaning | Ace Cleaning Experts",
     "Tile, grout and hardwood floor cleaning across South Jersey. EPA-certified products, honest guidance, and results you can see. Call 856-582-1711.",
     "services", tile_body)

# ==================================================== COMMERCIAL =========
commercial_body = f"""
<section class="page-hero dark">
  <div class="wrap">
    <div class="page-hero-copy">
      {breadcrumb([("Home","/"),("Commercial Floor Care", None)])}
      <span class="eyebrow">Offices &middot; Retail &middot; Medical &middot; Restaurants</span>
      <h1>Commercial Carpet &amp; Floor Care</h1>
      <p class="lede">We work around your business, not the other way around. Evening and weekend appointments keep cleaning off your customers' radar and off your staff's schedule &mdash; for carpet and hard floors alike.</p>
      <div class="btn-row">
        <a href="/contact/" class="btn btn-primary">Request a Commercial Quote</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-outline">{icon('phone')} Call {PHONE}</a>
      </div>
    </div>
  </div>
</section>

<div class="wrap">
{quote_snippet("<span class=\"qs-highlight\">Very professional from start to finish</span>. Great price, and I'll be using their services again.", "Barbara D.", color="red")}
</div>

<section>
  <div class="wrap">
    <div class="feature-row">
      <div class="feature-copy">
        <span class="eyebrow">Built for Businesses</span>
        <h2>What Commercial Clients Get</h2>
        <ul class="checklist" style="margin-top:22px;">
          <li>{icon('spade')} Flexible scheduling, including evenings and weekends</li>
          <li>{icon('spade')} Carpet, tile, grout and hardwood floor care</li>
          <li>{icon('spade')} EPA-certified products safe for staff and visitors</li>
          <li>{icon('spade')} Fast-dry techniques to minimize closed hours</li>
          <li>{icon('spade')} Straightforward quotes with no hidden fees</li>
          <li>{icon('spade')} One point of contact for recurring service</li>
        </ul>
      </div>
      <div class="feature-visual"><img class="card-edge" src="/images/commercial-service.webp" alt="Commercial floor cleaning by Ace Cleaning Experts" style="width:100%;height:100%;object-fit:cover;border-radius:var(--radius);"></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="grid-2" style="gap:32px;">
      <div>
        <h3 style="font-size:1.15rem;">Trusted by South Jersey Businesses</h3>
        <p style="color:var(--charcoal-70);">We hold recurring contract service with businesses including Adelphia, Otts, and Villari's, among others &mdash; the kind of long-term relationships that come from showing up on schedule, every time, without surprises.</p>
      </div>
      <div>
        <h3 style="font-size:1.15rem;">How We Price Commercial Jobs</h3>
        <p style="color:var(--charcoal-70);">Pricing is based on square footage and, for larger or more complex spaces, a walkthrough so we can quote accurately before we start &mdash; no guessing, no surprise line items on the invoice.</p>
      </div>
    </div>
  </div>
</section>

<section style="background:var(--gray);">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Who We Work With</span>
      <h2>Industries We Regularly Serve</h2>
    </div>
    <div class="grid-4">
      <div class="who-card"><div class="icon">{icon('building')}</div><h3>Offices</h3><p>Evening visits keep cleaning off the workday.</p></div>
      <div class="who-card"><div class="icon icon-charcoal">{icon('briefcase')}</div><h3>Retail Stores</h3><p>Scheduled around store hours and foot traffic.</p></div>
      <div class="who-card"><div class="icon">{icon('shield')}</div><h3>Medical Facilities</h3><p>EPA-certified products safe for patients and staff.</p></div>
      <div class="who-card"><div class="icon icon-charcoal">{icon('utensils')}</div><h3>Restaurants</h3><p>Fast-dry service that respects your open hours.</p></div>
    </div>
  </div>
</section>

<div class="stats-bar">
  <div class="wrap stats-grid stats-grid-4">
    <div class="stat"><div class="stat-num">40+</div><div class="stat-label">Years in Business</div></div>
    <div class="stat"><div class="stat-num stat-num-bold">5&#9733;</div><div class="stat-label">Star Rating</div></div>
    <div class="stat"><div class="stat-num" style="font-size:clamp(1.4rem,3vw,2rem);">Insured</div><div class="stat-label">&amp; EPA-Certified</div></div>
    <div class="stat"><div class="stat-num stat-icon"><img src="/images/us-flag-v1.webp" alt="American flag" style="width:44px;height:auto;border-radius:2px;box-shadow:var(--shadow-sm);"></div><div class="stat-label">Veteran Owned</div></div>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Real Results</span>
      <h2>Recent Commercial Work</h2>
    </div>
    {gallery_grid([
        ("gallery-01", "Red patterned commercial carpet cleaning in progress"),
        ("gallery-02", "Commercial carpet before and after cleaning, dirt lifted"),
        ("gallery-04", "Patterned commercial carpet cleaning"),
        ("gallery-11", "Patterned commercial carpet cleaning, ice cream shop"),
    ])}
  </div>
</section>

<section class="section-red">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Common Questions</span>
      <h2>Commercial Floor Care FAQ</h2>
    </div>
    {faq([
        ("Can you schedule cleaning outside business hours?", "Yes &mdash; evening and weekend appointments are common for commercial accounts specifically so cleaning doesn't disrupt your day."),
        ("Do you offer recurring service contracts?", "We can set up a regular cleaning schedule that fits your space and foot traffic. Call to talk through frequency and pricing."),
        ("What types of flooring do you handle commercially?", "Commercial carpet, tile, grout and hardwood &mdash; the same EPA-certified process used residentially, scaled to your square footage."),
    ])}
  </div>
</section>

{related_links("/commercial-carpet-cleaning/")}

{cta_band("Keep Your Space Looking Its Best", "Tell us about your space and schedule &mdash; we'll build a cleaning plan around it.")}
"""
page("/commercial-carpet-cleaning/", "Commercial Carpet &amp; Floor Cleaning | South Jersey | Ace Cleaning Experts",
     "Commercial carpet, tile and hardwood floor care for South Jersey offices, retail, medical and restaurant spaces. Flexible scheduling. Call 856-582-1711.",
     "commercial", commercial_body)

# ==================================================== SERVICE AREAS ======
_GLOUCESTER = [t for t in TOWNS if t["county"] == "Gloucester County"]
_CAMDEN = [t for t in TOWNS if t["county"] == "Camden County"]
_FEATURED_SLUGS = [
    "sewell-nj", "deptford-nj", "washington-township-nj", "cherry-hill-nj",
    "voorhees-nj", "haddonfield-nj", "blackwood-nj", "turnersville-nj",
]
_FEATURED_TOWNS = [next(t for t in TOWNS if t["slug"] == s) for s in _FEATURED_SLUGS]
_AREA_SEARCH_DATA = json.dumps([
    {"name": t["name"], "slug": t["slug"], "county": t["county"], "zip": t["zip"]} for t in TOWNS
])

def _featured_card(t):
    short = t["name"].replace(" Township", "")
    variant = "color-gloucester" if t["county"] == "Gloucester County" else "color-camden"
    return f'''<a href="/service-areas/{t["slug"]}/" class="areas-feat-card {variant}">
      <span class="afc-name">{short}</span>
      <span class="afc-meta">{t["county"]}</span>
      <span class="afc-arrow">{icon('arrow')}</span>
    </a>'''

_featured_cards = "\n    ".join(_featured_card(t) for t in _FEATURED_TOWNS)

def _county_town_list(towns):
    return "\n        ".join(
        f'<li><a href="/service-areas/{t["slug"]}/">{t["name"]}</a></li>' for t in towns
    )

areas_body = f"""
<section class="areas-hero">
  <div class="wrap areas-hero-grid">
    <div class="areas-hero-copy">
      {breadcrumb([("Home","/"),("Service Areas", None)])}
      <span class="eyebrow">South Jersey, Done Right</span>
      <h1>Proudly Serving<br><span class="text-red">South Jersey</span></h1>
      <p class="lede">We bring professional carpet, tile and upholstery cleaning to homeowners and businesses throughout Gloucester, Camden, Atlantic and Cape May Counties &mdash; and we take appointments across the bridge in Philadelphia and Delaware, too.</p>
      <div class="btn-row">
        <a href="tel:{PHONE_TEL}" class="btn btn-primary">{icon('phone')} Call {PHONE}</a>
        <a href="/contact/" class="btn btn-outline">Request a Free Quote</a>
      </div>
      <div class="areas-search" id="areasSearch">
        <label class="areas-search-box" for="areaSearchInput">
          {icon('search')}
          <input type="text" id="areaSearchInput" placeholder="Search your city or ZIP code&hellip;" autocomplete="off" aria-label="Search your city or ZIP code">
        </label>
        <div class="areas-search-results" id="areaSearchResults" hidden></div>
      </div>
      <p class="areas-search-helper">{icon('phone')} Not sure if we service your town? Give us a call &mdash; we&rsquo;re happy to check.</p>
      <script type="application/json" id="areaSearchData">{_AREA_SEARCH_DATA}</script>
    </div>
    <div class="areas-hero-photo">
      <img class="card-edge" src="/images/areas-hero-van-v1.webp" alt="Ace Cleaning Experts service van parked outside a South Jersey home">
      <span class="areas-hero-tag">Est. 1983</span>
    </div>
  </div>
</section>

<div class="wrap">
{quote_snippet("Will definitely use them again &mdash; <span class=\"qs-highlight\">couldn't be happier with their work</span>!", "Leslie")}
</div>

<section class="areas-featured">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Home Turf</span>
      <h2>Where We Work Most Often</h2>
      <p class="lede">These are the towns that keep our vans busiest, week to week.</p>
    </div>
  </div>
  <div class="areas-feat-track">
    <div class="wrap areas-feat-track-inner">
    {_featured_cards}
    </div>
  </div>
</section>

<section class="areas-counties">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">All Service Areas</span>
      <h2>Browse by County</h2>
      <p class="lede">Our home counties, and the counties we're expanding into as we take on more South Jersey shore-area work.</p>
    </div>
    <div class="areas-county-grid">
      <div class="areas-county-card size-lg color-red">
        <div class="acc-top">{icon('home')}<h3>Gloucester County</h3></div>
        <p>Our home county &mdash; Sewell and Deptford Township are where Ace got its start in 1983, and it's still where we run the most jobs every week.</p>
        <ul class="acc-towns">
        {_county_town_list(_GLOUCESTER)}
        </ul>
        <a href="/service-areas/sewell-nj/" class="acc-link">View Local Page {icon('arrow')}</a>
      </div>
      <div class="areas-county-card size-md color-charcoal">
        <div class="acc-top">{icon('building')}<h3>Camden County</h3></div>
        <p>From Haddonfield to Cherry Hill, we're a regular sight in driveways and loading docks across Camden County.</p>
        <ul class="acc-towns">
        {_county_town_list(_CAMDEN)}
        </ul>
        <a href="/service-areas/haddonfield-nj/" class="acc-link">View Local Page {icon('arrow')}</a>
      </div>
      <div class="areas-county-card size-sm color-tint">
        <div class="acc-top">{icon('leaf')}<h3>Atlantic County</h3></div>
        <p>We take on shore-area jobs by request throughout Atlantic County. Give us a call to confirm your town and get on the schedule.</p>
        <a href="tel:{PHONE_TEL}" class="acc-link">{icon('phone')} Call {PHONE}</a>
      </div>
      <div class="areas-county-card size-sm color-gray">
        <div class="acc-top">{icon('flag')}<h3>Cape May County</h3></div>
        <p>Cape May County jobs are scheduled by request. Call ahead and we'll confirm we can make it out to you.</p>
        <a href="tel:{PHONE_TEL}" class="acc-link">{icon('phone')} Call {PHONE}</a>
      </div>
    </div>
  </div>
</section>

{card_divider()}

<section class="areas-support">
  <div class="wrap areas-support-inner">
    <div class="areas-support-icon">{icon('mail')}</div>
    <div class="areas-support-copy">
      <h3>Can&rsquo;t find your town?</h3>
      <p>We may still service your area &mdash; our town pages don't cover every last street. Give us a call and we'll be happy to confirm.</p>
    </div>
    <a href="tel:{PHONE_TEL}" class="btn btn-primary">{icon('phone')} Call {PHONE}</a>
  </div>
</section>

<section class="areas-bridge">
  <div class="wrap areas-bridge-grid">
    <div class="areas-bridge-copy">
      <span class="eyebrow eyebrow-light">Extended Area</span>
      <h2>Just Across the Bridge</h2>
      <p>We also schedule appointments in Philadelphia, PA and in Wilmington and the surrounding Delaware area &mdash; just give us a call first to confirm.</p>
      <div class="areas-bridge-btns">
        <a href="/service-areas/philadelphia-pa/" class="btn btn-outline-light">Philadelphia {icon('arrow')}</a>
        <a href="/service-areas/wilmington-de/" class="btn btn-outline-light">Wilmington {icon('arrow')}</a>
      </div>
      <p class="areas-bridge-note">Give us a call &mdash; we're happy to check!</p>
    </div>
    <div class="areas-bridge-art">
      <img src="/images/philly-skyline-support-v1.webp" alt="Philadelphia skyline along the Schuylkill River">
    </div>
  </div>
</section>
"""
page("/service-areas/", "Service Areas | Ace Cleaning Experts, South Jersey",
     "Ace Cleaning Experts serves Sewell, Deptford, Haddonfield and all of Atlantic, Camden, Gloucester and Cape May counties, plus Philadelphia and Wilmington, DE.",
     "areas", areas_body)

for _t in TOWNS:
    town_page(_t)

# ==================================================== CONTACT ============
contact_body = f"""
<section class="page-hero dark">
  <div class="wrap">
    <div class="page-hero-copy">
      {breadcrumb([("Home","/"),("Contact", None)])}
      <span class="eyebrow">Get In Touch</span>
      <h1>Let's Get Your Space Looking Its Best</h1>
      <p class="lede">Call us directly for the fastest response, or send over a few details and we'll follow up to schedule your free quote.</p>
    </div>
  </div>
</section>

<div class="wrap">
{quote_snippet("<span class=\"qs-highlight\">Easy to get a quote from the owner</span>. Good prices for multiple rooms to be cleaned.", "Kevin", color="red")}
</div>

<section>
  <div class="wrap" style="display:grid; grid-template-columns: 0.9fr 1.1fr; gap:60px; align-items:flex-start;">
    <div>
      <h3>Contact Details</h3>
      <ul style="margin-top:20px;">
        <li style="display:flex; gap:12px; margin-bottom:16px;">{icon('phone')} <a href="tel:{PHONE_TEL}" style="font-weight:700;">{PHONE}</a></li>
        <li style="display:flex; gap:12px; margin-bottom:16px;">{icon('mail')} <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li style="display:flex; gap:12px; margin-bottom:16px;">{icon('clock')} Mon&ndash;Sat: 9:00am&ndash;5:00pm, Sunday: Closed</li>
        <li style="display:flex; gap:12px;">{icon('pin')} Serving Sewell, Deptford, Haddonfield &amp; all of South Jersey</li>
      </ul>
      <div style="margin-top:32px; padding:22px; background:var(--red); border-radius:var(--radius); font-size:0.92rem; color:var(--white);">
        <strong>Fastest way to reach us:</strong> call {PHONE}. Most quotes take less than five minutes over the phone.
      </div>
    </div>
    <div>
      <!-- Form posts to Formspree. Replace YOUR_FORM_ID with your real endpoint from formspree.io before launch. -->
      <div class="quote-wizard" id="quoteWizard">
        <div class="wizard-progress">Step <span id="wizStepNum">1</span> of 3</div>
        <form class="form-grid wizard-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST" id="quoteForm">
          <div class="wizard-step" data-step="1">
            <label class="wizard-question">What do you need cleaned?</label>
            <div class="wizard-choices" role="group" aria-label="Service needed">
              <button type="button" class="wizard-choice" data-value="Carpet Cleaning">Carpet Cleaning</button>
              <button type="button" class="wizard-choice" data-value="Upholstery Cleaning">Upholstery Cleaning</button>
              <button type="button" class="wizard-choice" data-value="Tile, Grout &amp; Hardwood">Tile, Grout &amp; Hardwood</button>
              <button type="button" class="wizard-choice" data-value="Commercial Floor Care">Commercial Floor Care</button>
              <button type="button" class="wizard-choice" data-value="Not Sure Yet">Not Sure Yet</button>
            </div>
            <input type="hidden" name="service" id="wizServiceInput">
          </div>
          <div class="wizard-step" data-step="2">
            <div class="field full"><label for="town">What town are you in?</label><input id="town" name="town" type="text" placeholder="e.g. Sewell, NJ" required></div>
            <div class="wizard-nav">
              <button type="button" class="wizard-back">Back</button>
              <button type="button" class="btn btn-primary wizard-next">Continue</button>
            </div>
          </div>
          <div class="wizard-step" data-step="3">
            <div class="field"><label for="name">Name</label><input id="name" name="name" type="text" required></div>
            <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" required></div>
            <div class="field full"><label for="email">Email</label><input id="email" name="email" type="email" required></div>
            <div class="field full"><label for="message">Message (optional)</label><textarea id="message" name="message" placeholder="Anything else we should know?"></textarea></div>
            <div class="wizard-nav">
              <button type="button" class="wizard-back">Back</button>
              <button type="submit" class="btn btn-primary">Get My Free Quote</button>
            </div>
          </div>
        </form>
        <div class="wizard-success" id="wizardSuccess" hidden>
          <h3>You're all set!</h3>
          <p>We'll follow up shortly to schedule your free quote. Need it faster? Call <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""
page("/contact/", "Contact Ace Cleaning Experts | Free Quote | South Jersey",
     "Contact Ace Cleaning Experts for a free carpet, tile or upholstery cleaning quote. Call 856-582-1711 or send your details online.",
     "contact", contact_body)

print("all pages generated")








