# Red Bank Outfitters — marketing site

Astro static site for Red Bank Outfitters, Red Bluff, CA (est. 1965).
Deployed on Netlify from `main`; the build publishes `dist/`.

## Stack

- **Astro** (static output, clean URLs — `/lodge`, `/upland/chukar`)
- `src/layouts/Base.astro` — site shell: head, announcement bar, nav, drawer,
  footer, consent banner, newsletter modal
- `src/pages/*.astro` — one file per page; body HTML injected via `set:html`
- `public/` — styles.css, script.js (all interactive behavior), img/, video/,
  `_redirects` (legacy WordPress URLs and old `.html` URLs → clean paths, all 301)
- `raw/` (gitignored) — original source images (WordPress pulls, wedding gallery)

## Develop

```bash
npm install
npm run dev        # local dev server
npm run build      # writes dist/
```

## Notes

- Rates are never invented: pricing is quoted by phone.
- `postcard` is an unlisted marketing mock-up (noindex, no site chrome).
- Ranch Login is gated on `OS_PATH` in `src/layouts/Base.astro` until the OS deploys.
- When the domain moves to redbankhunting.com, update `site` in `astro.config.mjs`
  and the SMS link on the postcard page.
