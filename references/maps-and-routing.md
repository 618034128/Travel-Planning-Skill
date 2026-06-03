# Maps & Routing

How to produce the route map in Phase 2. Two paths: use a maps/places tool if one
exists, otherwise generate shareable links.

## Step 1: Detect capability

Check what's available in the current agent:
- A **places search** tool (returns coordinates, ratings, hours) — use it to look
  up each stop and to discover good fillers ("a coffee shop near X").
- A **map display** tool (renders markers / an itinerary route) — use it to show
  the ordered route visually.
- A general **search/fetch** capability — use it to verify opening hours and
  current status of must-do venues.

If a places/map tool exists, prefer it end to end: search each stop → collect
coordinates + hours + rating → render the ordered route on the map. This gives the
richest result (the same kind of interactive itinerary map a maps-enabled
assistant produces).

## Step 2: Fallback — generate map links

If no maps tool is available, build URLs with `scripts/build_map_links.py`. It
takes an ordered list of stops (names, or `lat,lng` if you have them) and emits a
directions URL with all stops as waypoints in order. Run `python
scripts/build_map_links.py --help` for exact flags.

### Provider selection

- **Mainland China destinations** → default to **Amap (高德)** or **Baidu**. Google
  Maps is unreliable inside mainland China (coverage, access). Offer both if unsure
  which app the user has.
- **Everywhere else** → default to **Google Maps**.
- If the user names a preferred app, honor it.

### URL shapes (for reference; the script handles encoding)

- Google Maps directions:
  `https://www.google.com/maps/dir/?api=1&origin=ORIGIN&destination=DEST&waypoints=A|B|C&travelmode=walking|transit|driving`
- Google Maps single search/marker:
  `https://www.google.com/maps/search/?api=1&query=PLACE`
- Amap directions (web):
  `https://uri.amap.com/navigation?from=lng,lat,name&to=lng,lat,name&mode=car|bus|walk`
- Amap marker:
  `https://uri.amap.com/marker?position=lng,lat&name=NAME`
- Baidu directions:
  `https://api.map.baidu.com/direction?origin=NAME&destination=NAME&mode=walking|transit|driving&region=CITY&output=html`

Note coordinate order differs: Google uses `lat,lng`; Amap/Baidu URI APIs commonly
use `lng,lat`. The script normalizes this — don't hand-assemble if you can run it.

## Step 3: Always pair the map with the text schedule

The map shows *where*; the schedule (see `scheduling-heuristics.md`) shows *when*.
Always deliver both. A bare map without timing isn't a plan, and a schedule without
a map is hard to follow on the ground.

## When you lack coordinates

If you can't get coordinates (no places tool, unfamiliar venues), pass place names
plus the city to the script — the map apps resolve names to locations. Keep names
specific and disambiguated (e.g. "Liji Islamic Restaurant, Qinhuai, Nanjing" not
just "Liji"), since common names collide across cities.
