#!/usr/bin/env python3
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
PHONE = "856-582-1711"
PHONE_TEL = "8565821711"
EMAIL = "info@acecleaningexpertsnj.com"
DOMAIN = "https://www.acecleaningexpertsnj.com"

# ---------------------------------------------------------------- icons ----
ICONS = {
"rug": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="13" rx="1.5"/><rect x="6.5" y="7.5" width="11" height="6" rx="0.5"/><path d="M4 20h2M8 20h2M12 20h2M16 20h2"/></svg>',
"sofa": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 11V8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v3"/><rect x="3" y="11" width="18" height="6" rx="1.5"/><path d="M4 17v2M20 17v2"/></svg>',
"tile": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="8" height="8" rx="0.5"/><rect x="13" y="3" width="8" height="8" rx="0.5"/><rect x="3" y="13" width="8" height="8" rx="0.5"/><rect x="13" y="13" width="8" height="8" rx="0.5"/></svg>',
"building": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="3" width="14" height="18" rx="1"/><path d="M9 8h1M14 8h1M9 12h1M14 12h1M9 16h1M14 16h1"/><path d="M10 21v-4h4v4"/></svg>',
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
}

def icon(name):
    return ICONS[name]

NAV = [
    ("Home", "/", "home"),
    ("About", "/about-us/", "about"),
    ("Services", "/services/", "services"),
    ("Commercial", "/commercial-carpet-cleaning/", "commercial"),
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
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700;9..144,900&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
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
    return f"""<div class="announce">
  <div class="wrap">
    <span>{icon('star')} Veteran-Owned &amp; Family-Operated</span>
    <span class="center-item">Serving South Jersey for 40+ Years</span>
    <span>Residential &amp; Commercial Cleaning</span>
  </div>
</div>
<header class="site-header">
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
    return """<div class="stats-bar"><div class="wrap stats-grid stats-grid-4">
    <div class="stat"><div class="stat-num">40+</div><div class="stat-label">Years Experience</div></div>
    <div class="stat"><div class="stat-num">10,000+</div><div class="stat-label">Homes Cleaned</div></div>
    <div class="stat"><div class="stat-num stat-num-bold">5&#9733;</div><div class="stat-label">Star Rating</div></div>
    <div class="stat"><div class="stat-num">100%</div><div class="stat-label">Satisfaction Guaranteed</div></div>
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
]

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

def quote_snippet(text, name, stars=5, inline=False):
    star_str = "&#9733;" * stars
    cls = "quote-snippet inline" if inline else "quote-snippet"
    return f'''<div class="{cls}">
      <div class="qs-stars">{star_str}</div>
      <p class="qs-text">&ldquo;{text}&rdquo;</p>
      <div class="qs-who">&mdash; {name}</div>
    </div>'''

def placeholder(label, extra_class=""):
    return f'<div class="placeholder-block {extra_class}">{icon("droplet")}<span>{label}</span></div>'

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
    },
    {
        "slug": "west-deptford-nj",
        "name": "West Deptford",
        "county": "Gloucester County",
        "zip": None,
        "about": "[Placeholder &mdash; add specific local detail for West Deptford here: nearby "
                 "neighborhoods, landmarks, or well-known streets Ace commonly serves. Replace before launch.]",
    },
    {
        "slug": "logan-township-nj",
        "name": "Logan Township",
        "county": "Gloucester County",
        "zip": "08085",
        "about": "[Placeholder &mdash; add specific local detail for Logan Township here: nearby "
                 "neighborhoods, landmarks, or well-known streets Ace commonly serves. Replace before launch.]",
    },
    {
        "slug": "washington-township-nj",
        "name": "Washington Township",
        "county": "Gloucester County",
        "zip": "08080",
        "about": "[Placeholder &mdash; add specific local detail for Washington Township here: nearby "
                 "neighborhoods, landmarks, or well-known streets Ace commonly serves. Replace before launch.]",
    },
    {
        "slug": "franklin-township-nj",
        "name": "Franklin Township",
        "county": "Gloucester County",
        "zip": "08322",
        "about": "[Placeholder &mdash; add specific local detail for Franklin Township here: nearby "
                 "neighborhoods, landmarks, or well-known streets Ace commonly serves. Replace before launch.]",
    },
    {
        "slug": "cherry-hill-nj",
        "name": "Cherry Hill",
        "county": "Camden County",
        "zip": "08003",
        "about": "[Placeholder &mdash; add specific local detail for Cherry Hill here: nearby "
                 "neighborhoods, landmarks, or well-known streets Ace commonly serves. Replace before launch.]",
    },
    {
        "slug": "voorhees-nj",
        "name": "Voorhees",
        "county": "Camden County",
        "zip": "08043",
        "about": "[Placeholder &mdash; add specific local detail for Voorhees here: nearby "
                 "neighborhoods, landmarks, or well-known streets Ace commonly serves. Replace before launch.]",
    },
    {
        "slug": "blackwood-nj",
        "name": "Blackwood",
        "county": "Camden County",
        "zip": "08012",
        "about": "[Placeholder &mdash; add specific local detail for Blackwood here: nearby "
                 "neighborhoods, landmarks, or well-known streets Ace commonly serves. Replace before launch.]",
    },
    {
        "slug": "turnersville-nj",
        "name": "Turnersville",
        "county": "Gloucester County",
        "zip": "08012",
        "about": "[Placeholder &mdash; add specific local detail for Turnersville here: nearby "
                 "neighborhoods, landmarks, or well-known streets Ace commonly serves. Replace before launch.]",
    },
]

def town_page(t):
    name = t["name"]
    locality = f'{t["county"]} &middot; {t["zip"]}' if t.get("zip") else t["county"]
    body = f"""
<section class="page-hero">
  <div class="wrap">
    {breadcrumb([("Home","/"),("Service Areas","/service-areas/"),(name, None)])}
    <span class="eyebrow">{locality}</span>
    <h1>Carpet &amp; Floor Cleaning in {name}, NJ</h1>
    <p class="lede">{t["about"]}</p>
    <div class="btn-row">
      <a href="/contact/" class="btn btn-primary">Get Free Quote</a>
      <a href="tel:{PHONE_TEL}" class="btn btn-outline">{icon('phone')} Call {PHONE}</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">What We Offer</span>
      <h2>Services Available in {name}</h2>
    </div>
    <ul class="checklist grid-2" style="display:grid;">
      <li>{icon('check')} <a href="/carpet-cleaning-service/">Carpet Cleaning</a> &mdash; deep steam extraction with Scotchgard protection</li>
      <li>{icon('check')} <a href="/upholstery-cleaning/">Upholstery Cleaning</a> &mdash; fabric-safe cleaning for sofas &amp; chairs</li>
      <li>{icon('check')} <a href="/tile-grout-cleaning/">Tile, Grout &amp; Hardwood</a> &mdash; kitchens, bathrooms &amp; floors</li>
      <li>{icon('check')} <a href="/commercial-carpet-cleaning/">Commercial Floor Care</a> &mdash; offices, retail &amp; medical spaces</li>
    </ul>
  </div>
</section>

<section style="background:var(--gray);">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Common Questions</span>
      <h2>{name} Cleaning FAQ</h2>
    </div>
    {faq([
        (f"How fast can you get to {name}?", f"{name} is one of our regularly serviced areas, so scheduling is usually quick &mdash; call {PHONE} and we'll give you a real timeframe, not a runaround."),
        ("Do you serve both homes and businesses here?", "Yes &mdash; residential and commercial jobs, from single rooms to full offices or storefronts."),
        ("Is pricing different by town?", "No &mdash; our pricing is based on the job, not the zip code. You'll get the same honest, up-front quote wherever you're located in South Jersey."),
    ])}
  </div>
</section>

{cta_band(f"Ready to Book in {name}?", f"Fast response, honest pricing, and a crew that shows up when they say they will.")}
"""
    page(f"/service-areas/{t['slug']}/", f"Carpet Cleaning in {name}, NJ | Ace Cleaning Experts",
         f"Professional carpet, tile and upholstery cleaning in {name}, NJ. EPA-certified products, honest pricing. Call {PHONE}.",
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
<section class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <span class="eyebrow">South Jersey's Carpet, Tile &amp; Upholstery Cleaning Experts</span>
      <h1>Your Family's Home Deserves a Family You Can Trust</h1>
      <p class="lede">Serving homes and businesses for 40+ years with deep steam extraction, EPA-certified products, and a local crew that treats your home like their own.</p>
      <div class="btn-row">
        <a href="/contact/" class="btn btn-primary">Get Free Quote</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-outline">{icon('phone')} Call {PHONE}</a>
      </div>
      <ul class="hero-trust">
        <li>{icon('shield')} Veteran-Owned</li>
        <li>{icon('clock')} 40+ Years Experience</li>
        <li>{icon('building')} Residential &amp; Commercial</li>
      </ul>
    </div>
    <img src="/images/hero-family.jpg" alt="Three generations of the Ace Cleaning Experts family" class="hero-visual hero-photo">
  </div>
</section>

{stats_bar()}

<section id="before-after">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">The Proof</span>
      <h2>See the Ace Difference</h2>
    </div>
    <div class="ba-slider">
      <img src="/images/carpet-before-v2.webp" alt="Dirty, stained carpet before Ace Cleaning Experts deep clean" class="ba-before">
      <img src="/images/carpet-after-v2.webp" alt="Same carpet after Ace Cleaning Experts deep clean, looking like new" class="ba-after">
      <span class="ba-tag before-tag">Before</span>
      <span class="ba-tag after-tag">After</span>
      <div class="ba-handle"></div>
      <input type="range" min="0" max="100" value="50" class="ba-range" aria-label="Drag to compare before and after">
    </div>
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
    {quote_snippet("My carpets <span class=\"qs-highlight\">looked and smelled brand new</span> after they were cleaned. They exceeded my expectations.", "Jeff")}
  </div>
</section>

<section id="why-ace">
  <div class="wrap why-row">
    <img src="/images/why-ace-team.webp" alt="Ace Cleaning Experts owner and family in front of the company van" class="why-ace-photo">
    <div>
      <span class="eyebrow">Why Ace</span>
      <h2>Why South Jersey Chooses Ace</h2>
      <ul class="benefit-list">
        <li><span class="b-icon">{icon('shield')}</span><span class="b-text">Veteran-Owned</span></li>
        <li><span class="b-icon">{icon('home')}</span><span class="b-text">Family-Owned &amp; Operated</span></li>
        <li><span class="b-icon">{icon('droplet')}</span><span class="b-text">Professional-Grade Equipment</span></li>
        <li><span class="b-icon">{icon('star')}</span><span class="b-text">Experienced, Trained Technicians</span></li>
        <li><span class="b-icon">{icon('check')}</span><span class="b-text">Satisfaction Guaranteed</span></li>
      </ul>
      {quote_snippet("I've been using Ace Cleaning Experts <span class=\"qs-highlight\">for over 20 years</span>, and they consistently do a fantastic job. Professional, efficient, reasonably priced, and incredibly courteous.", "Karen", inline=True)}
    </div>
  </div>
</section>

<section style="background:var(--gray);">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">What We Do</span>
      <h2>Featured Services</h2>
    </div>
    <div class="grid-4">
      <div class="svc-card">
        <img src="/images/carpet-service.webp" alt="Clean carpet after Ace Cleaning Experts service" class="svc-photo">
        <div class="svc-body">
          <div class="icon">{icon('rug')}</div>
          <h3>Carpet Cleaning</h3>
          <p>Deep steam extraction that lifts dirt, allergens and stains.</p>
          <a href="/carpet-cleaning-service/" class="go">Learn More {icon('arrow')}</a>
        </div>
      </div>
      <div class="svc-card">
        <img src="/images/tile-service.webp" alt="Mosaic tile floor cleaned by Ace Cleaning Experts, dirty grout restored to clean" class="svc-photo">
        <div class="svc-body">
          <div class="icon">{icon('tile')}</div>
          <h3>Tile &amp; Grout</h3>
          <p>Grout deep-cleaned back toward its original color.</p>
          <a href="/tile-grout-cleaning/" class="go">Learn More {icon('arrow')}</a>
        </div>
      </div>
      <div class="svc-card">
        <div class="placeholder-block">{icon('sofa')}<span>Upholstery Photo</span></div>
        <div class="svc-body">
          <div class="icon">{icon('sofa')}</div>
          <h3>Upholstery</h3>
          <p>Fabric-safe cleaning for sofas, sectionals and chairs.</p>
          <a href="/upholstery-cleaning/" class="go">Learn More {icon('arrow')}</a>
        </div>
      </div>
      <div class="svc-card">
        <img src="/images/commercial-service.webp" alt="Area rug being deep cleaned by Ace Cleaning Experts" class="svc-photo">
        <div class="svc-body">
          <div class="icon">{icon('building')}</div>
          <h3>Commercial Cleaning</h3>
          <p>Flexible scheduling for offices, retail and medical spaces.</p>
          <a href="/commercial-carpet-cleaning/" class="go">Learn More {icon('arrow')}</a>
        </div>
      </div>
    </div>
    <div class="quote-pair">
      {quote_snippet("Ace is <span class=\"qs-highlight\">my favorite carpet cleaner of all time</span>. They are responsive, reliable and trustworthy.", "Anne")}
      {quote_snippet("Ace Cleaning Experts makes our marble tile <span class=\"qs-highlight\">look like new every time</span>.", "Fabrizio")}
    </div>
    <p style="text-align:center; margin-top:40px;"><a href="/services/" class="btn btn-outline">View All Services</a></p>
  </div>
</section>

<section style="background:var(--gray);">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">See The Difference</span>
      <h2>Our Work</h2>
    </div>
    {gallery_grid()}
  </div>
</section>

<section id="meet-ace">
  <div class="wrap meet-ace-row">
    <div>
      <span class="eyebrow">Meet Ace</span>
      <h2>The People Behind Ace</h2>
      <p class="lede">Veteran-owned and family-operated, serving South Jersey for 40+ years. The person who quotes your job is accountable for the crew that shows up to do it &mdash; no corporate hand-offs, no call centers.</p>
      {quote_snippet("Nick and Jeff were professional, friendly, and thorough from start to finish. You can really tell <span class=\"qs-highlight\">they take pride in their work</span>.", "Chris", inline=True)}
    </div>
    <img src="/images/meet-ace-team-v2.webp" alt="The Ace Cleaning Experts family washing the company van together" class="meet-ace-photo">
  </div>
</section>

<section style="background:var(--gray);" id="areas">
  <div class="wrap area-row">
    <div>
      <span class="eyebrow">Where We Work</span>
      <h2>Proudly Serving South Jersey</h2>
      <p class="lede">Home base in Sewell, Deptford and Haddonfield, with regular jobs throughout Gloucester and Camden counties &mdash; and beyond.</p>
      <div class="area-pill-grid">
        <a href="/service-areas/sewell-nj/" class="area-pill priority">Sewell</a>
        <a href="/service-areas/deptford-nj/" class="area-pill priority">Deptford</a>
        <a href="/service-areas/haddonfield-nj/" class="area-pill priority">Haddonfield</a>
        <a href="/service-areas/west-deptford-nj/" class="area-pill">West Deptford</a>
        <a href="/service-areas/cherry-hill-nj/" class="area-pill">Cherry Hill</a>
        <a href="/service-areas/washington-township-nj/" class="area-pill">Washington Township</a>
        <a href="/service-areas/voorhees-nj/" class="area-pill">Voorhees</a>
        <a href="/service-areas/blackwood-nj/" class="area-pill">Blackwood</a>
        <a href="/service-areas/turnersville-nj/" class="area-pill">Turnersville</a>
        <a href="/service-areas/logan-township-nj/" class="area-pill">Logan Township</a>
        <a href="/service-areas/franklin-township-nj/" class="area-pill">Franklin Township</a>
      </div>
      <p style="margin-top:26px;"><a href="/service-areas/" class="btn btn-outline">View All Service Areas</a></p>
      {quote_snippet("I've used Ace for well over 10 years \u2014 not only to support a local company, but because <span class=\"qs-highlight\">they're always professional and always on-time</span>.", "David", inline=True)}
    </div>
    <img src="/images/south-jersey-badge-v2.webp" alt="Ace Cleaning Experts sponsors a local South Jersey youth sports team" class="area-badge">
  </div>
</section>

<section id="faq">
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

<section style="padding:0 0 100px;">
  <div class="wrap" style="max-width:640px;">
    {quote_snippet("Great service and people. Been using them <span class=\"qs-highlight\">since 1990, never a complaint</span>.", "Bob")}
  </div>
</section>

{cta_band("Ready to Love Your Floors Again?", "Veteran-Owned. Family-Operated. Serving South Jersey Since 1983.")}
"""
page("/", "Ace Cleaning Experts | South Jersey's Trusted Carpet Cleaning Experts",
     "Veteran-owned, family-operated carpet, tile and upholstery cleaning serving Sewell, Deptford, Haddonfield and all of South Jersey for 40+ years. Call 856-582-1711.",
     "home", home_body)

# ============================================================== ABOUT ===
about_body = f"""
<section class="page-hero">
  <div class="wrap">
    {breadcrumb([("Home","/"),("About Us", None)])}
    <span class="eyebrow">Our Story</span>
    <h1>Four Decades of Straight Talk and Clean Carpets</h1>
    <p class="lede">Ace Cleaning Experts started the way most good local businesses do &mdash; with a family, a van, and a determination to do the job right. Forty-plus years later, we're still locally owned and operated: not a franchise, not a national call center, just the same commitment to honest pricing and work you can trust.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="feature-row">
      <div class="feature-copy">
        <h3>Veteran-Owned. Family-Operated. Still Local.</h3>
        <p class="lede" style="font-size:1.05rem;">We're proud to be a veteran-owned, family-operated business serving the same South Jersey communities we call home. The person who quotes your job is accountable for the crew that shows up to do it &mdash; no corporate hand-offs, no surprise fees.</p>
      </div>
      <div class="feature-visual"><img src="/images/veteran-owned.webp" alt="Ace Cleaning Experts owner in U.S. Marine Corps dress uniform" style="width:100%;height:100%;object-fit:cover;border-radius:var(--radius);"></div>
    </div>
    <div class="feature-row reverse">
      <div class="feature-copy">
        <h3>The Same Care We'd Want in Our Own Homes</h3>
        <p class="lede" style="font-size:1.05rem;">Every technician is trained on EPA-certified cleaning agents and modern extraction equipment, and every job wraps up with a walkthrough so you know exactly what was done.</p>
      </div>
      <div class="feature-visual"><img src="/images/technician-care.webp" alt="Ace Cleaning Experts technicians at work cleaning carpets" style="width:100%;height:100%;object-fit:cover;border-radius:var(--radius);"></div>
    </div>
  </div>
</section>

<section style="background:var(--gray);">
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

{cta_band("Come See Why South Jersey Calls Ace First", "Talk to a real person on the first ring &mdash; no scripts, no upsells.")}
"""
page("/about-us/", "About Ace Cleaning Experts | Veteran-Owned, Family-Operated NJ Cleaners",
     "Meet Ace Cleaning Experts: a veteran-owned, family-operated carpet and floor cleaning company serving South Jersey for 40+ years. Local, insured, EPA-certified.",
     "about", about_body)

# ============================================================ SERVICES ==
services_body = f"""
<section class="page-hero">
  <div class="wrap">
    {breadcrumb([("Home","/"),("Services", None)])}
    <span class="eyebrow">What We Do</span>
    <h1>Cleaning Services for Every Room and Every Business</h1>
    <p class="lede">Carpet, upholstery, tile, grout, hardwood and commercial floor care &mdash; all handled by the same local crew, with EPA-certified products and 40+ years of hands-on experience behind every job.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="grid-4">
      <div class="svc-card">
        <img src="/images/carpet-service.webp" alt="Clean carpet after Ace Cleaning Experts service" class="svc-photo">
        <div class="svc-body">
          <div class="icon">{icon('rug')}</div>
          <h3>Carpet Cleaning</h3>
          <p>Deep steam extraction that lifts dirt, allergens and stains.</p>
          <a href="/carpet-cleaning-service/" class="go">Learn More {icon('arrow')}</a>
        </div>
      </div>
      <div class="svc-card">
        <div class="placeholder-block">{icon('sofa')}<span>Upholstery Photo</span></div>
        <div class="svc-body">
          <div class="icon">{icon('sofa')}</div>
          <h3>Upholstery Cleaning</h3>
          <p>Fabric-safe treatment for sofas, sectionals and dining chairs.</p>
          <a href="/upholstery-cleaning/" class="go">Learn More {icon('arrow')}</a>
        </div>
      </div>
      <div class="svc-card">
        <img src="/images/tile-service.webp" alt="Mosaic tile floor cleaned by Ace Cleaning Experts, dirty grout restored to clean" class="svc-photo">
        <div class="svc-body">
          <div class="icon">{icon('tile')}</div>
          <h3>Tile, Grout &amp; Hardwood</h3>
          <p>Grout deep-cleaned back toward its original color.</p>
          <a href="/tile-grout-cleaning/" class="go">Learn More {icon('arrow')}</a>
        </div>
      </div>
      <div class="svc-card">
        <img src="/images/commercial-service.webp" alt="Area rug being deep cleaned by Ace Cleaning Experts" class="svc-photo">
        <div class="svc-body">
          <div class="icon">{icon('building')}</div>
          <h3>Commercial Floor Care</h3>
          <p>Flexible after-hours scheduling for offices and retail.</p>
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

{cta_band()}
"""
page("/services/", "Cleaning Services | Ace Cleaning Experts, South Jersey",
     "Explore carpet, upholstery, tile, grout, hardwood floor and commercial cleaning services from Ace Cleaning Experts &mdash; South Jersey's veteran-owned cleaning crew.",
     "services", services_body)

# ==================================================== CARPET CLEANING ===
carpet_body = f"""
<section class="page-hero">
  <div class="wrap">
    {breadcrumb([("Home","/"),("Services","/services/"),("Carpet Cleaning", None)])}
    <span class="eyebrow">Residential &amp; Light Commercial</span>
    <h1>Carpet Cleaning That Actually Lasts</h1>
    <p class="lede">Deep steam extraction pulls dirt, allergens and set-in stains out of the fibers &mdash; not just off the surface &mdash; and every job finishes with a Scotchgard application.</p>
    <div class="btn-row">
      <a href="/contact/" class="btn btn-primary">Get Free Quote</a>
      <a href="tel:{PHONE_TEL}" class="btn btn-outline">{icon('phone')} Call {PHONE}</a>
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
      <li>{icon('check')} Pre-treatment of high-traffic areas and visible stains</li>
      <li>{icon('check')} Hot water / steam extraction with EPA-certified solutions</li>
      <li>{icon('check')} Pet odor and stain treatment where needed</li>
      <li>{icon('check')} Scotchgard fabric protector applied after cleaning</li>
      <li>{icon('check')} Fast-dry techniques to minimize downtime</li>
      <li>{icon('check')} Straightforward, honest pricing quoted up front</li>
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

<section>
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

{cta_band()}
"""
page("/carpet-cleaning-service/", "Carpet Cleaning in South Jersey | Ace Cleaning Experts",
     "Professional carpet cleaning in Sewell, Deptford, Haddonfield and South Jersey. EPA-certified deep steam extraction with Scotchgard protection. Call 856-582-1711.",
     "services", carpet_body)

# ================================================= UPHOLSTERY CLEANING ==
uphol_body = f"""
<section class="page-hero">
  <div class="wrap">
    {breadcrumb([("Home","/"),("Services","/services/"),("Upholstery Cleaning", None)])}
    <span class="eyebrow">Sofas &middot; Sectionals &middot; Dining Chairs</span>
    <h1>Upholstery Cleaning That Respects the Fabric</h1>
    <p class="lede">Every fabric is different, so we test and match our method to the material before we start &mdash; lifting stains and odor without soaking, over-wetting or fading the piece you care about.</p>
    <div class="btn-row">
      <a href="/contact/" class="btn btn-primary">Get Free Quote</a>
      <a href="tel:{PHONE_TEL}" class="btn btn-outline">{icon('phone')} Call {PHONE}</a>
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
      <li>{icon('check')} Fabric identification and spot-testing before cleaning</li>
      <li>{icon('check')} EPA-certified, low-moisture cleaning agents</li>
      <li>{icon('check')} Targeted stain and odor removal</li>
      <li>{icon('check')} Scotchgard protection to guard against future spills</li>
      <li>{icon('check')} Sofas, sectionals, loveseats, dining and accent chairs</li>
      <li>{icon('check')} Faster dry times than DIY rental machines</li>
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

<section>
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Common Questions</span>
      <h2>Upholstery Cleaning FAQ</h2>
    </div>
    {faq([
        ("Will cleaning shrink or fade my furniture?", "We test each fabric first and choose a method suited to it, which is exactly why we avoid the over-wetting that causes shrinking or color bleed with DIY machines."),
        ("Can you get pet odor out of a couch?", "In most cases, yes. Odor treatment is a standard part of our upholstery process, not an upcharge."),
        ("How long does a sofa take to dry?", "Most pieces are dry within a few hours thanks to our low-moisture approach and extraction equipment."),
        ("Do you clean leather?", "Our current process is built for fabric upholstery. Call us and we can talk through what your specific piece needs."),
    ])}
  </div>
</section>

{cta_band()}
"""
page("/upholstery-cleaning/", "Upholstery Cleaning in South Jersey | Ace Cleaning Experts",
     "Professional fabric upholstery cleaning for sofas, sectionals and chairs across South Jersey. Fabric-safe, EPA-certified, Scotchgard-protected. Call 856-582-1711.",
     "services", uphol_body)

# ============================================== TILE / GROUT / HARDWOOD =
tile_body = f"""
<section class="page-hero">
  <div class="wrap">
    {breadcrumb([("Home","/"),("Services","/services/"),("Tile, Grout &amp; Hardwood", None)])}
    <span class="eyebrow">Kitchens &middot; Bathrooms &middot; Hardwood Floors</span>
    <h1>Tile, Grout &amp; Hardwood Floor Cleaning</h1>
    <p class="lede">Grout holds onto dirt long after mopping stops working. We deep-clean it back toward its original color, and we clean hardwood floors the right way &mdash; without soaking or dulling the finish.</p>
    <div class="btn-row">
      <a href="/contact/" class="btn btn-primary">Get Free Quote</a>
      <a href="tel:{PHONE_TEL}" class="btn btn-outline">{icon('phone')} Call {PHONE}</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">What's Included</span>
      <h2>Every Visit Covers</h2>
    </div>
    <ul class="checklist grid-2" style="display:grid;">
      <li>{icon('check')} Deep tile and grout cleaning to lift embedded dirt</li>
      <li>{icon('check')} EPA-certified solutions safe for kitchens and bathrooms</li>
      <li>{icon('check')} Hardwood floor cleaning suited to the floor's finish</li>
      <li>{icon('check')} Mildew and grime treatment in high-moisture areas</li>
      <li>{icon('check')} Honest guidance on what grout can and can't be restored</li>
      <li>{icon('check')} Straightforward, up-front pricing</li>
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
        ("tile-mini-before", "Dirty, stained grout before cleaning"),
        ("tile-mini-after", "Same tile floor after cleaning, grout restored"),
    ])}
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Common Questions</span>
      <h2>Tile, Grout &amp; Hardwood FAQ</h2>
    </div>
    {faq([
        ("Can you make old grout look new again?", "Deep cleaning brings most grout back significantly lighter and more even in color. Severely stained or damaged grout may need sealing or re-grouting, and we'll tell you honestly which applies."),
        ("Is the process safe for hardwood floors?", "Yes &mdash; we match our approach to your floor's finish and avoid the over-wetting that causes warping or dulling."),
        ("How long before I can walk on the floor?", "Tile and grout are typically usable within an hour or two; hardwood dry times vary slightly by finish, and we'll confirm before we leave."),
        ("Do you seal grout after cleaning?", "We can discuss sealing as part of your visit &mdash; ask when you book so we can plan the time needed."),
    ])}
  </div>
</section>

{cta_band()}
"""
page("/tile-grout-cleaning/", "Tile, Grout &amp; Hardwood Floor Cleaning | Ace Cleaning Experts",
     "Tile, grout and hardwood floor cleaning across South Jersey. EPA-certified products, honest guidance, and results you can see. Call 856-582-1711.",
     "services", tile_body)

# ==================================================== COMMERCIAL =========
commercial_body = f"""
<section class="page-hero">
  <div class="wrap">
    {breadcrumb([("Home","/"),("Commercial Floor Care", None)])}
    <span class="eyebrow">Offices &middot; Retail &middot; Medical &middot; Restaurants</span>
    <h1>Commercial Carpet &amp; Floor Care</h1>
    <p class="lede">We work around your business, not the other way around. Evening and weekend appointments keep cleaning off your customers' radar and off your staff's schedule &mdash; for carpet and hard floors alike.</p>
    <div class="btn-row">
      <a href="/contact/" class="btn btn-primary">Request a Commercial Quote</a>
      <a href="tel:{PHONE_TEL}" class="btn btn-outline">{icon('phone')} Call {PHONE}</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Built for Businesses</span>
      <h2>What Commercial Clients Get</h2>
    </div>
    <ul class="checklist grid-2" style="display:grid;">
      <li>{icon('check')} Flexible scheduling, including evenings and weekends</li>
      <li>{icon('check')} Carpet, tile, grout and hardwood floor care</li>
      <li>{icon('check')} EPA-certified products safe for staff and visitors</li>
      <li>{icon('check')} Fast-dry techniques to minimize closed hours</li>
      <li>{icon('check')} Straightforward quotes with no hidden fees</li>
      <li>{icon('check')} One point of contact for recurring service</li>
    </ul>
  </div>
</section>

<section style="background:var(--gray);">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Who We Work With</span>
      <h2>Industries We Regularly Serve</h2>
    </div>
    <div class="grid-4">
      <div class="who-card"><div class="icon">{icon('building')}</div><h3>Offices</h3></div>
      <div class="who-card"><div class="icon">{icon('briefcase')}</div><h3>Retail Stores</h3></div>
      <div class="who-card"><div class="icon">{icon('shield')}</div><h3>Medical Facilities</h3></div>
      <div class="who-card"><div class="icon">{icon('utensils')}</div><h3>Restaurants</h3></div>
    </div>
  </div>
</section>

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

<section style="background:var(--gray);">
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

{cta_band("Keep Your Space Looking Its Best", "Tell us about your space and schedule &mdash; we'll build a cleaning plan around it.")}
"""
page("/commercial-carpet-cleaning/", "Commercial Carpet &amp; Floor Cleaning | South Jersey | Ace Cleaning Experts",
     "Commercial carpet, tile and hardwood floor care for South Jersey offices, retail, medical and restaurant spaces. Flexible scheduling. Call 856-582-1711.",
     "commercial", commercial_body)

# ==================================================== SERVICE AREAS ======
areas_body = f"""
<section class="page-hero">
  <div class="wrap">
    {breadcrumb([("Home","/"),("Service Areas", None)])}
    <span class="eyebrow">Where We Work</span>
    <h1>Serving South Jersey, Philadelphia &amp; Delaware</h1>
    <p class="lede">Our home base is Sewell, Deptford and Haddonfield, with regular jobs across Atlantic, Camden, Gloucester and Cape May counties. We also take appointments in Philadelphia, Delaware and Wilmington &mdash; just give us a call to confirm your address.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Home Base</span>
      <h2>Priority Service Cities</h2>
    </div>
    <div class="area-pill-grid">
      <a href="/service-areas/sewell-nj/" class="area-pill priority">Sewell</a>
      <a href="/service-areas/deptford-nj/" class="area-pill priority">Deptford</a>
      <a href="/service-areas/haddonfield-nj/" class="area-pill priority">Haddonfield</a>
    </div>

    <div style="background:var(--gray); border-radius:var(--radius); padding:36px 32px; margin-top:48px;">
      <div class="section-head" style="margin-bottom:26px;">
        <span class="eyebrow">Towns We Cover</span>
        <h2>South Jersey Coverage</h2>
      </div>
      <div class="area-pill-grid">
        <a href="/service-areas/west-deptford-nj/" class="area-pill">West Deptford</a>
        <a href="/service-areas/cherry-hill-nj/" class="area-pill">Cherry Hill</a>
        <a href="/service-areas/washington-township-nj/" class="area-pill">Washington Township</a>
        <a href="/service-areas/voorhees-nj/" class="area-pill">Voorhees</a>
        <a href="/service-areas/blackwood-nj/" class="area-pill">Blackwood</a>
        <a href="/service-areas/turnersville-nj/" class="area-pill">Turnersville</a>
        <a href="/service-areas/logan-township-nj/" class="area-pill">Logan Township</a>
        <a href="/service-areas/franklin-township-nj/" class="area-pill">Franklin Township</a>
      </div>
      <div class="grid-4" style="margin-top:28px;">
        <div class="county-card"><h3>Gloucester County</h3><p style="margin:0; color:var(--charcoal-70); font-size:0.92rem;">Including Sewell &amp; Deptford, and surrounding communities.</p></div>
        <div class="county-card"><h3>Camden County</h3><p style="margin:0; color:var(--charcoal-70); font-size:0.92rem;">Including Haddonfield, and surrounding communities.</p></div>
        <div class="county-card"><h3>Atlantic County</h3><p style="margin:0; color:var(--charcoal-70); font-size:0.92rem;">Residential and commercial jobs throughout the county.</p></div>
        <div class="county-card"><h3>Cape May County</h3><p style="margin:0; color:var(--charcoal-70); font-size:0.92rem;">Residential and commercial jobs throughout the county.</p></div>
      </div>
    </div>

    <div class="section-head" style="margin-top:48px; margin-bottom:22px;">
      <span class="eyebrow">Extended Area</span>
      <h2>Just Across the Bridge</h2>
      <p class="lede">We also schedule appointments in Philadelphia, PA and in Wilmington and the surrounding Delaware area.</p>
    </div>
    <div class="area-pill-grid">
      <span class="area-pill">Philadelphia, PA</span>
      <span class="area-pill">Wilmington, DE</span>
      <span class="area-pill">Delaware &mdash; surrounding areas</span>
    </div>
  </div>
</section>

{cta_band("Don't See Your Town Listed?", "Give us a call &mdash; there's a good chance we already cover it.")}
"""
page("/service-areas/", "Service Areas | Ace Cleaning Experts, South Jersey",
     "Ace Cleaning Experts serves Sewell, Deptford, Haddonfield and all of Atlantic, Camden, Gloucester and Cape May counties, plus Philadelphia and Wilmington, DE.",
     "areas", areas_body)

for _t in TOWNS:
    town_page(_t)

# ==================================================== CONTACT ============
contact_body = f"""
<section class="page-hero">
  <div class="wrap">
    {breadcrumb([("Home","/"),("Contact", None)])}
    <span class="eyebrow">Get In Touch</span>
    <h1>Let's Get Your Space Looking Its Best</h1>
    <p class="lede">Call us directly for the fastest response, or send over a few details and we'll follow up to schedule your free quote.</p>
  </div>
</section>

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
      <div style="margin-top:32px; padding:22px; background:var(--red-tint); border:1px solid var(--red); border-radius:var(--radius); font-size:0.92rem;">
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








