# Ace Cleaning Experts — Website

A static, zero-build website for Ace Cleaning Experts NJ. Plain HTML/CSS/JS —
no framework, no build step, deploys straight to Vercel.

## Structure

```
/index.html                     Home
/about-us/                      About
/services/                      Services overview
/carpet-cleaning-service/       Carpet Cleaning
/upholstery-cleaning/           Upholstery Cleaning
/tile-grout-cleaning/           Tile, Grout & Hardwood
/commercial-carpet-cleaning/    Commercial Floor Care
/service-areas/                 Service Areas
/contact/                       Contact + quote form
/css/style.css                  Design system (colors, type, components)
/js/main.js                     Mobile nav toggle + footer year
/images/                        Logo + hero photo
/build.py                       Generator script — edit THIS, not the HTML
```

URL paths intentionally match the current WordPress site's permalinks so
existing Google Ads Final URLs, backlinks, and the GMB listing keep working.

## Editing content

All page content lives in **`build.py`**, not in the HTML files directly —
the HTML is generated output. To make a copy change:

1. Edit the relevant `*_body` string in `build.py`
2. Run `python3 build.py`
3. The HTML files update in place

## Before launch — open items

- [ ] **Confirm "Veteran-Owned" claim** with the client — not previously
      documented, appears throughout nav/hero/credentials/footer.
- [ ] **Confirm service area footprint** — this build lists Atlantic, Camden,
      Gloucester & Cape May Counties + Philadelphia/Wilmington DE. Prior
      confirmed data was Gloucester & Camden + most of Burlington County,
      South Jersey-only positioning.
- [ ] **Photos**: only logo + one hero family photo are real; remaining
      "Photo:" placeholder boxes need real job-site images.
- [ ] **Testimonials**: homepage quote is a placeholder — swap for a real,
      permission-cleared review.
- [ ] **Contact form**: replace `YOUR_FORM_ID` in `contact_body` (build.py)
      with a real Formspree endpoint.
- [ ] **Address / map**: no street address included — add once confirmed.
- [ ] **Analytics**: add GA / Ads conversion tags to `head()` in build.py.
- [ ] **Favicon**: currently the generated "A" mark / logo jpg — swap if a
      vector favicon exists.

## Deploying to Vercel

Framework preset: **Other** (static, no build command). Output directory:
root. Connect this repo in Vercel, then point acecleaningexpertsnj.com's DNS
at Vercel once ready to go live.
