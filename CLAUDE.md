# CLAUDE.md, Shane "The Hunt" Career Tracker

## What this is
A single self-contained HTML career-search tool built for Shane, a craft-beer sales and marketing pro
(Advanced Cicerone) who is leaving the beverage industry. It guides him from idea stage to targeted
applications and informational interviews. It is styled like an ecommerce storefront (Amazon aesthetic,
no Amazon trademarks) with a full-page bald eagle watermark, and the parody elements all do real work.

## Where things live
- Live site: https://localhostusr.github.io/tracker-499ce2/
- GitHub repo: localhostusr/tracker-499ce2 (public, hardened: obscure name + noindex meta + robots.txt disallow)
- Local repo (deploy source): ~/Documents/shane-the-hunt-tracker  (index.html + eagle-watermark.jpg + robots.txt)
- Working copy that gets edited: ~/Downloads/Shane The Hunt - Career Tracker.html
- Release tag: v1-shane (validated build, link already sent to Shane)

## Deploy workflow (how to ship a change)
1. Edit ~/Downloads/Shane The Hunt - Career Tracker.html
2. Copy it over the repo: cp "~/Downloads/Shane The Hunt - Career Tracker.html" ~/Documents/shane-the-hunt-tracker/index.html
3. gh auth switch --user localhostusr   (the CLI also has chriskohlPMP; localhostusr must be active to push)
4. git -C ~/Documents/shane-the-hunt-tracker add -A && commit && push origin main
5. GitHub Pages rebuilds in 1 to 3 min. The link Shane has never changes; it always serves the latest.

## Architecture
- One HTML file. Vanilla JS, no build step, no dependencies. CSS is base styles plus a later override
  block ("Amazon-style restyle") that re-themes via CSS variables.
- Tabs are data-driven from the TABS array; each entry maps to a section.tab by id. show(id) toggles them.
- Persistence is localStorage, per browser, private to the user. Keys: shaneOptState, shaneInterviews,
  shaneScorecard, shaneApplications, shaneVersions.
- IMPORTANT: Shane's typed-in data never reaches GitHub. The document is versioned by git; his data is
  versioned only by the in-app Saved Versions tab and the JSON backup export/import. Saving the web page
  does NOT save his data.

## Tabs
Start Here, Resources, Options Menu, Jargon Decoder, Info Interviews, Decision Scorecard, Applications,
Income Reference, The Journey, AI Edge, Saved Versions.
- Options Menu: 16 options across 3 lanes, with editable Interest/Status/Notes, star ratings + badges
  (parody, footnoted as for-fun), Add to Shortlist / Apply now, search filter, Frequently-pursued bundle.
- The Journey tab is the canonical written record of the strategy and every decision.
- Saved Versions: snapshot/restore + download/import JSON backup.

## The strategy (so future edits stay consistent)
Shane is an Autonomy-Seeker, not a Founder. Three lanes:
- Lane 1 Employee (climb, own nothing) = no-regret fallback.
- Lane 2 Center/Merge (payments, insurance, medical device) = enter W2, build a book, fork to independent.
  This is the recommended entry. SaaS is Lane 1 only (no independent fork).
- Lane 3 Autonomy now (independent agency, ISO agent, CRE, manufacturer rep).
Key assumption: ideal household is two earners, partner near $110k, which makes every San Diego scenario
viable without Shane needing $200k alone. So autonomy is a fit-and-upside choice, not a survival need.
Targets: $110k floor now, $150k+ long term, San Diego market.

## Testing
Validated with Playwright (Chromium). Scripts were written to /tmp (ephemeral, may not persist):
/tmp/test_tracker.py (functional), /tmp/validate.py (structural + mobile + harvest links), /tmp/shot.py
(screenshots). Last run: functional 8/8, structural 8/8, mobile clean (0px overflow), all 24 links resolve
or are bot-blocked (valid in a browser). If re-testing, serve the repo dir over http (localStorage on
file:// is unreliable) and reinstall Playwright if needed.

## Known caveats (already disclosed in the page)
- Star ratings and "Best Seller" badges are parody, footnoted. Real ranking is in The Journey tab.
- AI Edge tool prices are early-2026 ballparks; verify before subscribing. Categories age better than dollars.
- Financial figures are directional San Diego 2026 estimates at ~7% mortgage rates. Condo all-in was
  corrected to ~$4,850/mo (incl HOA); median house ~$6,300/mo.

## Status
Paused. Link sent to Shane. Everything committed and pushed; working tree clean; remote in sync.
Open next step previously teed up: an income-curve timeline (year 1/3/5/7) for the center-lane path.
