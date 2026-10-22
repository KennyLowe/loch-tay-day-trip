# The Tay Day
Responsive static itinerary for Kenny: Aberfeldy, Acharn and Kenmore on Friday 23 October 2026.

Serve the repository root with any static server, e.g. python3 -m http.server 8000. No dependencies, API keys or build step. Relative assets and .nojekyll support a GitHub Pages repository subpath. Publishing intentionally not configured or enabled.

Seven timed stops, Google Maps driving and walking approach links, classic/gentler modes, print-to-PDF, no-JavaScript fallback, keyboard focus, reduced motion and original inline SVG landscape. Optional Google Fonts with system/Georgia fallback. No tracking, geolocation, storage or service worker. Maps require connectivity; not offline trail navigation.

## Information provenance
Prepared 22 October 2026. Geographic and route content uses general knowledge and has not been independently live-verified. All durations and distances are estimates. No live venue hours, weather, parking, road/trail status or sunset time checked. Food names are candidates to contact, not bookings. UI explicitly marks uncertainty and links Met Office, Walkhighlands, Traffic Scotland, access guidance and venue listings. Walking links locate entrances/destinations, not waterfall circuits. Gentler plan is not certified accessible.

## Checks
- node --check app.js
- node --test tests/app.test.cjs
- python3 tests/check_html.py

Tests cover both modes, map URL structure, print control, HTML nesting, local assets, fragment targets and external-link safety. Real browser/device visual testing remains recommended before publication.

## Build-session results
HTML structure/resource/link-safety check passed. Node-based behavior tests are supplied but could not run in the build container (node executable unavailable). No real-browser visual check performed. No live external travel facts verified.
