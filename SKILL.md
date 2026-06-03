---
name: travel-planning-skill
description: >-
  Plan complete travel itineraries with a map route and a time-blocked daily
  schedule. Use this skill whenever the user wants to plan a trip or asks for an
  itinerary, route, or day plan for visiting a place — for example "plan a day in
  Nanjing", "help me plan a 3-day Tokyo trip", or "I want to go to X, leaving at
  9 and back by 6, must see Y". Trigger even when the user gives only partial
  details. The defining behavior of this skill: it ALWAYS confirms every trip
  parameter with the user BEFORE producing any route or schedule, so it never
  wastes effort planning the wrong trip.
---

# Travel Planning Skill

Turn a loose travel wish ("I want to go to X, leave around 9, back by 6, I really
want to see Y, rest is up to you") into two deliverables:

1. A **route map** — an interactive map if a maps/places tool is available, otherwise shareable map links.
2. A **time-blocked daily schedule** — realistic, with travel legs, meals, and buffer time.

If the trip starts in another city, the inbound and return legs are part of the
plan too — query a real option (e.g. via a 12306 MCP) and recommend it, but never
buy the ticket yourself (see `references/transport-and-booking.md`).

The user can revise anything at any point ("drop that temple", "this is too
rushed", "add a coffee stop"), and you regenerate only what's affected.

## The one rule that defines this skill: confirm before you plan

Do **not** produce a route or a schedule until the user has confirmed the trip
parameters. This is not bureaucracy — itinerary planning is expensive to redo,
and a single wrong assumption (wrong day, wrong pace, a closed attraction)
cascades through every downstream stop. Confirming first is faster overall and
respects the user's time.

The user often says "everything else is up to you." That does **not** mean skip
confirmation — it means *you* fill the open slots with sensible defaults and then
show those defaults back for a quick yes/no. The user approves a plan-shape, not
a blank check. Surface your assumptions; let them veto.

Concretely, the flow is always: **Intake → Confirm → Build → Revise.** Never jump
from a partial request straight to a finished itinerary.

---

## Phase 1 — Intake & Confirmation

Goal: reach a confirmed, unambiguous trip spec while asking as few questions as
possible. Read `references/intake-checklist.md` for the full field list, the
default values to assume, and example confirmation summaries.

Steps:

1. **Extract** everything the user already gave. Re-read the whole conversation —
   they may have mentioned the city, dates, or must-sees earlier. Don't re-ask
   for anything already stated.

2. **Fill gaps with explicit defaults**, don't interrogate. For each unstated
   parameter, pick a reasonable default (see the checklist) instead of asking.
   Asking ten questions for a casual day trip is a worse experience than
   proposing defaults and letting the user correct one or two.

3. **Resolve the few things that genuinely change the plan.** Only these deserve
   a direct question, and only when you truly can't infer them:
   - dates / which day(s), if pacing or opening hours depend on it
   - daily start and end time (and where the day starts/ends — hotel? station?)
   - must-go places and any hard "won't go" exclusions
   - rough pace (packed vs relaxed) and transport mode (walk / transit / drive)
   - origin city + inbound/return timing, if the trip starts elsewhere — these legs
     are part of the plan (see `references/transport-and-booking.md`)
   Ask at most a small batch of these at once. Bundle them; don't drip one at a time.

4. **Present a compact confirmation summary** and explicitly wait. Format it so
   the user can approve in one glance or correct a single line. End with a clear
   prompt like "Look right? Tell me what to change, or say go and I'll build it."

   Example confirmation block:
   ```
   Here's what I've got — confirm or correct:
   • Destination: Nanjing (old city core)
   • When: this Saturday, one day
   • Hours: out from hotel near Xinjiekou ~9:00, back by ~18:00
   • Must-do: Ruins of St. Paul'... (your picks)
   • Pace: relaxed, ~4–5 stops + meals
   • Getting around: metro + walking
   • Assumed for you: lunch near midpoint, one coffee/dessert break, indoor backup if it rains
   Say "go" and I'll plot the route and schedule.
   ```

5. **Only after a clear "go"** (or equivalent confirmation) do you proceed to
   Phase 2. If the user corrects something, update the summary and reconfirm the
   changed part — you don't need to re-list everything.

A note on judgment: if the request is genuinely complete and unambiguous already
(all of: place, day, hours, must-sees, pace), you may present the summary and
build in the same turn — but still *show* the summary first so nothing is a
surprise. The gate is about no hidden assumptions, not about forcing a round trip.

---

## Phase 2 — Build the itinerary

Only enter this phase after confirmation. Produce both deliverables.

### Route map

Read `references/maps-and-routing.md` for the decision logic. In short:
- If a maps/places tool or MCP is available (e.g. a places search + map display),
  use it: look up each stop to get real coordinates, hours, and ratings, then
  render an ordered route.
- Otherwise, generate shareable map links with the helper:
  `python scripts/build_map_links.py` (see the script's `--help`). It builds
  Google Maps directions URLs for international trips and Amap/Baidu URLs for
  mainland-China trips, with waypoints in visiting order.
- For mainland China, default to Amap (高德) or Baidu, since Google Maps is
  unreliable there. For everywhere else, default to Google Maps.

### Inter-city transport (getting there & back)

Only when the trip starts in a different city. Read
`references/transport-and-booking.md`. In short:
- If a transport tool is available (e.g. a **12306 MCP** for mainland-China rail, or
  a flight search), query the real board and recommend a concrete service that fits
  the confirmed timing — number, departure/arrival, duration, rough fare.
- Otherwise, give booking-site links (12306 / Ctrip / etc.) for the user to search.
- **Query and recommend only — never purchase.** Booking needs real-name auth, a
  captcha, and live payment; hand the exact train/date to the user to buy.

### Time-blocked schedule

Read `references/scheduling-heuristics.md` for pacing rules, travel-time
estimation, meal placement, and opening-hours handling. Key points:
- Order stops to minimize backtracking, not just by user mention order.
- Insert realistic travel legs between stops (mode-dependent) and a buffer.
- Place meals at sensible times near the route; don't strand the user far from food at 13:00.
- Check opening hours/closing days for must-dos; flag conflicts instead of silently scheduling a closed venue.
- Respect the hard start/end times. If the must-dos don't fit, say so and offer to cut or extend rather than overstuffing.

Use this output template:

```
## [Destination] — [date], [start]–[end]

[1–2 sentence framing of the day's shape.]

[ROUTE MAP: interactive map, or the generated link(s)]

### Schedule
| Time        | Stop                    | Notes |
|-------------|-------------------------|-------|
| 9:00–9:20   | Travel: hotel → Stop 1  | metro line 1, 2 stops |
| 9:20–10:30  | Stop 1                  | opens 9:00; the must-see |
| ...         | ...                     | ... |

### Notes
- Backup if rain / if a stop is closed: ...
- Anything time-sensitive (last entry, reservation): ...
```

After presenting, invite revision in one line: "Want anything dropped, added, or
re-paced?"

---

## Phase 3 — Revise on request

Travelers change their minds; treat revision as normal, not failure. Common edits
and how to handle them:

- **"Drop / I don't want to go to X"** — remove it, re-stitch the route around the
  gap, and recompute timing. Offer to fill the freed time or to end earlier.
- **"This is too rushed" / "too empty"** — adjust stop count and dwell times to
  the new pace; keep the must-dos.
- **"Add Y"** — slot it in geographically (near its neighbors), not at the end;
  warn if it pushes past the end time.
- **"Swap the order" / "do the museum first"** — reorder and recheck opening hours
  and travel legs.
- **A change that breaks a constraint** (e.g. adding three stops to a fixed
  6-hour window) — don't silently overstuff. Name the conflict and offer choices,
  the same way the intake gate works.

Regenerate only the affected parts and the map; don't make the user re-confirm the
whole trip for a one-stop change. If a change is large enough to shift the day's
shape, briefly reconfirm just that shift before rebuilding.

---

## Reference files

- `references/intake-checklist.md` — full parameter list, default values, and confirmation-summary examples. Read this in Phase 1.
- `references/maps-and-routing.md` — tool detection and map-link generation, China vs. international. Read this in Phase 2.
- `references/scheduling-heuristics.md` — pacing, travel-time estimates, meals, opening hours. Read this in Phase 2.
- `references/transport-and-booking.md` — inter-city legs, 12306/transport-tool use, and the query-vs-book boundary. Read this in Phase 2 when the trip spans cities.
- `scripts/build_map_links.py` — deterministic builder for Google Maps / Amap / Baidu route URLs. Run when no maps tool is available.
