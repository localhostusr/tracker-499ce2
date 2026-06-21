# CLAUDE.md — The Wax Stacks (Vinyl Inventory)

> Branch-scoped doc. This file lives on `claude/vinyl-inventory-html-lx907a` and documents ONLY the vinyl
> project. `main` has its own CLAUDE.md for a different project (the "Shane the Hunt" career tracker) and is
> intentionally left untouched — only `vinyl-inventory.html` is ever cherry-picked from this branch to `main`.

## What this is
A single self-contained HTML inventory of a personal vinyl record collection, built from photos of the
records laid out on the floor. Styled as a 1960s/70s record-store / radio-DJ "vibe" (sunburst header,
spinning 45, Monoton/Pacifico/Oswald type, harvest-gold + burnt-orange palette). 57 records, all identified.

## Where things live
- Live site: https://localhostusr.github.io/tracker-499ce2/vinyl-inventory.html
- Repo: localhostusr/tracker-499ce2 (public; noindex meta + robots.txt disallow inherited from the repo)
- Dev branch: `claude/vinyl-inventory-html-lx907a` (all development happens here)
- Deliverable: `vinyl-inventory.html` at repo root (self-contained: HTML + CSS + JS + base64 photo thumbs)
- Build tooling (committed so it survives container resets — /tmp does NOT persist):
  - `tools/build_vinyl.py` — generator; reads `tools/records.json`, writes `../vinyl-inventory.html`
  - `tools/records.json` — the record data (source of truth for the catalog)

## Build / deploy workflow
1. Edit `tools/records.json` (data) and/or `tools/build_vinyl.py` (markup/CSS/JS).
2. Rebuild: `cd tools && python3 build_vinyl.py`  (writes ../vinyl-inventory.html)
3. Sanity check JS: extract the `<script>` and `node --check` it (no browser available in-env to click-test).
4. Commit to this dev branch and push.
5. Publish: cherry-pick `vinyl-inventory.html` onto `main` and push; GitHub Pages rebuilds in 1–3 min.
   Owner controls publishing — only push to `main` when they say "publish" / "push live".

## Data model (each record in records.json)
`{ artist, title, year, genre, status, note, condition, img, q }`
- `status`: "identified" | "tentative" | "unidentified" (all 57 are currently "identified").
- `img`: base64 data-URI of a photo crop — the instant placeholder + offline fallback.
- `q`: optional iTunes search-query override. `q:""` = skip the lookup and keep the photo (used for rare
  pressings not in the catalog: Chopin, Candy Man, Rudolph, Against the Wind, Star Wars themes).
  If `q` is absent it is derived from artist+title.
- `condition`: free text, shown as a ⚠ badge (e.g., Cat Stevens – Teaser and the Firecat: "Side 1 damaged").

## Cover art + audio (no network allowlist needed)
The in-env sandbox can only reach GitHub (iTunes/MusicBrainz/etc. are blocked), so all catalog calls happen
**client-side in the viewer's browser** via iTunes Search/Lookup **JSONP** (bypasses CORS + the egress
allowlist). On load it fetches album artwork + collectionId per record; tracklists/previews are fetched
lazily on flip/play. Results cache in localStorage. Everything degrades to the embedded photo if offline.

## Features
- Views: **Sleeves** (gallery), **List** (sortable table), **Stats** (by decade, by genre, most-collected,
  crate facts incl. total value).
- Hover a sleeve → the record slides out. Click → 3D flip to the tracklist.
- **Jukebox:** 30-sec previews; bottom now-playing bar (spinning deck + tonearm, play/pause, ⏮/⏭, progress).
- **Play-all queue:** ▶ / "Play all" queues an album's previews and auto-advances.
- **Drop the needle:** features a random record and plays it.
- **★ Favorites** (+ Faves filter) and **editable Est. value** per record, with a running collection total.
- Top stat bar shows Records · Artists · Faves · Est. value (status counts were removed — all identified).

## Persistence (localStorage, per browser, never leaves the device)
Keys: `vinylArt` (q→artwork URL), `vinylIds` (q→collectionId), `vinylFavs` (index→1),
`vinylValues` (index→number). The catalog itself lives in the committed HTML / records.json.

## Source photos (for re-identification, if needed)
Floor shots IMG_3547–3550 (full collection) + straight-on shots IMG_3556–3564 (clusters/individual sleeves).
Perspective in the floor shots makes precise cropping unreliable — prefer straight-on shots for new IDs.

## Known caveats
- Catalog art/audio need internet; first load is slower while it looks things up, then it's cached.
- Cannot run a browser in-env: JS is syntax-checked only, not click-tested — verify interactions live.
- Owner corrected a couple of guesses: the wild-horses sleeve IS *Against the Wind*; the stained-glass
  sleeve is *Neil Diamond – Tap Root Manuscript*.

## Status
Paused at owner's request. 57/57 identified. Dev branch has the latest build (retro restyle + jukebox +
flip + stats + shuffle + favorites/queue/value + top-bar cleanup), committed & pushed.
Live `main` may trail the newest features until the owner says to publish.
Possible next ideas: side A/B grouping, CSV/JSON export, real price lookups (needs an egress allowlist).
