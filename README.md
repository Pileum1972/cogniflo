# CogniFlo website

A plain static site — HTML and CSS, no build step, no dependencies, no framework.
Every page works if you just double-click it. That's deliberate: it means it will
still work in five years, and it costs nothing to host.

---

## Before you go live — the checklist

The site is live at **https://cogniflogroup.com** but is deliberately held back
from search while it's being finished. These are still outstanding.

- [x] **Email address.** Now `guy@cogniflogroup.com` throughout. ~~Interim Gmail.~~
- [ ] **LinkedIn URL.** Points at `linkedin.com/company/cogniflo`, which does not
      exist — and the company is CogniFlo *Group*. Create the page, or set
      `LINKEDIN = ""` to drop the link cleanly.
- [ ] **Contact form.** Not connected to an inbox — see "Making the form work".
- [ ] **DMARC record.** SPF and DKIM are in place; DMARC is not. See "Email".
- [ ] **`NOINDEX = False`** — until you do this the site will never appear in
      Google, no matter how long you wait. See "Keeping it out of search".
- [ ] **`DRAFT = False`** to remove the amber Preview bar. Do this last.

Everything above lives in one place: the config block at the top of
`shared.py`. Edit, run `python3 build.py`, re-upload.

**Already done:** custom domain and HTTPS, favicons and social card, founder
photo, logo mark, canonical tags and sitemap on the real domain, SPF and DKIM.

---

## Keeping it out of search while you work

`NOINDEX = True` in `shared.py` does two things:

- puts `<meta name="robots" content="noindex, nofollow">` in the `<head>` of
  every page — this is the part that actually works
- makes `robots.txt` say `Disallow: /`, which crawlers usually honour, and stops
  the sitemap being advertised

The site stays fully live, and anyone you send the link to sees it normally. It
just won't turn up in search results.

**When you're ready to launch:** set `NOINDEX = False`, rebuild, upload, *then*
submit `sitemap.xml` in Google Search Console. The other order wastes a crawl —
Google fetches the sitemap, finds noindex on every page, and drops them.

A note on what this is not: noindex keeps the site out of search, not out of
sight. The pages are still publicly reachable by anyone with the URL. That is
the right trade while the site is unfinished but has no inbound links; it is not
confidentiality.

---

## Publishing it on GitHub Pages (free, no git required)

You can do this entirely in the browser. It takes about ten minutes.

1. **Make a GitHub account** at github.com if you don't have one. Free.
2. **Create a repository.** Click the `+` top-right → *New repository*.
   Name it `cogniflo`. Set it to **Public** (Pages is free only on public repos).
   Don't tick "Add a README" — you already have one. Click *Create repository*.
3. **Upload the files.** On the empty repo page click
   *uploading an existing file*. Drag in **everything from this folder** —
   all the `.html` files, `robots.txt`, `sitemap.xml`, `.nojekyll`, and the
   `assets` folder. Scroll down, click *Commit changes*.
   - If `.nojekyll` won't upload because it starts with a dot, use
     *Add file → Create new file*, type `.nojekyll` as the name, leave it
     empty, and commit.
4. **Turn on Pages.** Go to *Settings* (top of the repo) → *Pages* in the left
   sidebar. Under **Source** choose *Deploy from a branch*. Under **Branch**
   choose `main` and `/ (root)`. Click *Save*.
5. **Wait two minutes,** then refresh that page. It will show your live URL:
   `https://YOUR-USERNAME.github.io/cogniflo`

That's it. It's live, on HTTPS, free, with no traffic limit you'll realistically hit.

**To change anything later:** click the file in GitHub, click the pencil icon,
edit, commit. The site updates in about a minute.

---

## Making the contact form work

GitHub Pages serves files but can't run code, so it can't process a form on its
own. The form is already wired for [Formspree](https://formspree.io), which is
free for 50 submissions a month — far more than you'll need early on.

1. Sign up at formspree.io with the email you want enquiries sent to.
2. Create a new form. It gives you an endpoint like
   `https://formspree.io/f/abcdwxyz`.
3. Open `contact.html`, find `action="https://formspree.io/f/YOUR_FORM_ID"`,
   and replace that URL with yours.
4. Submit the form once yourself. Formspree emails you to confirm the address;
   click the link and you're done.

Until you do this, the form shows an honest "not connected yet" message instead
of pretending to send. It will never silently swallow an enquiry.

A spam honeypot field is already included, so you shouldn't get bot submissions.

---

## The custom domain — cogniflogroup.com

A `CNAME` file in the repo root already contains `cogniflogroup.com`. Two more
steps:

**1. In GitHub:** Settings → Pages → Custom domain → enter `cogniflogroup.com`
→ Save. Do this *before* the DNS below, so nobody else can claim a subdomain.

**2. At your registrar,** add these records:

| Type  | Name  | Value                   |
|-------|-------|-------------------------|
| A     | @     | 185.199.108.153         |
| A     | @     | 185.199.109.153         |
| A     | @     | 185.199.110.153         |
| A     | @     | 185.199.111.153         |
| CNAME | www   | pileum1972.github.io    |

Optional IPv6, alongside (not instead of) the A records:
`2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`,
`2606:50c0:8003::153`.

The www CNAME points at `pileum1972.github.io` with **no repository name**.

**3. Wait, then tick "Enforce HTTPS"** in Settings → Pages. The checkbox can
take up to 24 hours to become available while the certificate is issued. Don't
skip it — without it the site serves over plain HTTP.

## Email at the domain

Nothing is configured yet. Two routes:

- **Free:** Zoho Mail Forever Free — 5 users, 5GB each, one domain, real
  sending and receiving with SPF and DKIM. No IMAP/POP, so webmail and the
  mobile app only.
- **Paid:** Google Workspace or Microsoft 365 Business Basic, about $6–7 per
  user per month, with better deliverability into enterprise inboxes.

Avoid the old "Cloudflare forwarding plus Gmail send-as" trick: Google is
ending *Send mail as* for third-party addresses in January 2027.

Whichever you pick, publish **SPF, DKIM and DMARC** records. A new domain with
no sending reputation lands in spam without them. Start DMARC at `p=none`.

Once the mailbox is live, change `EMAIL` in `shared.py`, run
`python3 build.py`, and re-upload.

### DMARC

Still to add. One TXT record at the registrar, host `_dmarc`:

```
v=DMARC1; p=none; rua=mailto:guy@cogniflogroup.com; fo=1
```

`p=none` is monitor-only — it changes nothing about delivery, it just starts the
reports so you can see who is sending as your domain. Leave it a month, then
consider `p=quarantine`.

---

## Editing the site

Two ways, depending on how you like to work.

**Just edit the HTML.** Every page is self-contained — the CSS is inlined in a
`<style>` block in each file. Change the text, save, upload. Nothing will break.
The tradeoff is that shared bits (nav, footer, styles) are repeated across the
five pages, so a change to the footer means editing five files.

**Or use the generator.** `build.py` and `shared.py` produce all
six pages from one set of components, so the nav, footer and styles live in one
place. The config block at the top of `shared.py` holds every value from
the checklist above — email, LinkedIn, site URL, form endpoint, and the
`DRAFT = True` flag that shows the Preview bar. Edit, run `python3 build.py`
from the repo root, and re-upload. This is the better route if you plan to
change the site often.

### Changing the colours

At the top of the `<style>` block in each page is a `:root` block. Every colour
in the site comes from those variables:

```css
--bg:      #0a1020;   /* page background   */
--surface: #131f3a;   /* cards             */
--ink:     #f2f5fc;   /* headings          */
--ink-body:#b8c4dc;   /* body copy         */
--accent:  #4fd1c5;   /* primary accent    */
```

Change those five and the whole site re-skins. The current values are checked
for WCAG AA contrast — if you swap them, re-check with a contrast tool before
publishing.

---

## What's in here

```
index.html        Home
services.html     Six services, each with capabilities and outcomes
approach.html     The methodology, in sequence
about.html        Mission, vision, values, founder
contact.html      Form and contact details
404.html          Served automatically for bad URLs
robots.txt        Points crawlers at the sitemap
sitemap.xml       Submit this in Google Search Console
.nojekyll         Stops GitHub processing the files unnecessarily
assets/           Favicon and social share card
```

---

## After launch

- **Google Search Console** (free): add the site, submit `sitemap.xml`.
  This is how you find out what people search before they land on you.
- **Analytics:** Plausible and Fathom are simple and privacy-friendly but paid;
  Google Analytics is free. Either way it's one script tag in the `<head>`.
- **Test the social card:** paste your URL into LinkedIn's Post Inspector to
  check the preview image renders.
