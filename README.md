# CogniFlo website

A plain static site — HTML and CSS, no build step, no dependencies, no framework.
Every page works if you just double-click it. That's deliberate: it means it will
still work in five years, and it costs nothing to host.

---

## Before you go live — the placeholder checklist

Six things are fake right now. Work down this list, then delete the amber
"Preview" bar (last item).

- [ ] **Email address.** `hello@cogniflo.com` appears in the footer and on the
      Contact page.
- [ ] **LinkedIn URL.** Currently points at a company page that may not exist yet.
- [ ] **Contact form.** Not connected to an inbox — see "Making the form work" below.
- [ ] **Founder photo.** A grey placeholder card sits where Guy's photo goes.
- [ ] **Logo.** A CSS square with "CF" in it stands in for the real mark.
- [ ] **Site URL.** Canonical tags and the sitemap point at `YOUR-USERNAME.github.io`.
- [ ] **Delete the Preview bar** once the above are done.

All of these live in one place: the config block at the top of
`build.py`-generated pages. See "Editing the site" below.

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

## Adding your domain later

Once you buy a domain (roughly $12/year — Namecheap, Cloudflare and Porkbun are
all fine):

1. Create a file called `CNAME` in the repo containing one line: `cogniflo.com`
2. At your registrar, add these DNS records:

   | Type  | Name  | Value                  |
   |-------|-------|------------------------|
   | A     | @     | 185.199.108.153        |
   | A     | @     | 185.199.109.153        |
   | A     | @     | 185.199.110.153        |
   | A     | @     | 185.199.111.153        |
   | CNAME | www   | YOUR-USERNAME.github.io |

3. In *Settings → Pages*, enter the domain and tick **Enforce HTTPS**
   (wait for the certificate to issue first — usually under an hour).
4. Update `SITE_URL` in `build.py` and rebuild, so the canonical tags,
   sitemap and social-card URLs point at the new domain.

---

## Editing the site

Two ways, depending on how you like to work.

**Just edit the HTML.** Every page is self-contained — the CSS is inlined in a
`<style>` block in each file. Change the text, save, upload. Nothing will break.
The tradeoff is that shared bits (nav, footer, styles) are repeated across the
five pages, so a change to the footer means editing five files.

**Or use the generator.** `source/build.py` and `source/shared.py` produce all
six pages from one set of components, so the nav, footer and styles live in one
place. The config block at the top of `source/shared.py` holds every value from
the checklist above — email, LinkedIn, site URL, form endpoint, and the
`DRAFT = True` flag that shows the Preview bar. Edit, run `python3 build.py`
from inside `source/`, and re-upload. This is the better route if you plan to
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
