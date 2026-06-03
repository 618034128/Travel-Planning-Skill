# Scheduling Heuristics

How to turn a confirmed set of stops into a realistic time-blocked day. The goal is
a schedule a real person can actually follow — not a fantasy that ignores travel
time, meals, and closing hours.

## Ordering

- Order stops to **minimize backtracking**, not by the order the user mentioned
  them. Cluster geographically: do nearby stops together, sweep in one direction.
- Anchor to the confirmed start and end locations. The first stop should be near
  the start point; the last near the end point (or near transit home).
- Keep must-dos in the plan even if it means a small detour; they're the point.

## Travel legs

Insert an explicit travel block between every pair of stops. Rough estimates when
you don't have a routing tool:

| Mode | City rule of thumb |
|------|--------------------|
| Walking | ~12 min/km; add time for crossings in dense areas |
| Transit | wait + ride; assume 5–10 min wait + line time; add walk to/from stations |
| Driving | faster point-to-point but add parking time in city centers |

Always round up and add a small buffer. Underestimating travel is the most common
way a plan falls apart by mid-afternoon.

## Dwell time

Typical time at a stop (adjust for the user's pace):

| Stop type | Relaxed | Packed |
|-----------|---------|--------|
| Major sight / museum | 90–150 min | 60–90 min |
| Temple / garden / viewpoint | 45–75 min | 30–45 min |
| Market / street / neighborhood walk | 60–90 min | 30–60 min |
| Cafe / dessert / coffee break | 45–60 min | 30 min |
| Sit-down meal | 60–75 min | 45 min |

A relaxed day is ~4–5 substantive stops plus meals and a break. A packed day can
push 6–7 but warn the user it will feel like a march.

## Meals

- Place lunch ~12:00–13:30 and dinner (if the day runs late) ~18:00–19:30, near
  the route at that time — don't strand the user far from food.
- If the user gave food preferences or a must-eat spot, build the route so they're
  near it at the right hour.
- One coffee/dessert/tea break in the afternoon is a good default for a relaxed day.

## Opening hours & closing days

- For must-do venues, check opening hours and weekly closing days (many museums
  close one weekday). Use a search tool if available.
- If a must-do is closed on the chosen day, **flag it during confirmation or
  immediately** — offer to move the day, swap the stop, or visit at a different
  time. Never silently schedule a closed venue.
- Watch last-entry times (often 30–60 min before closing) and timed-entry or
  reservation requirements.

## Respecting the time window

- Honor the confirmed start and end times as hard bounds.
- If the must-dos plus realistic travel don't fit the window, **say so** and offer
  options: cut a stop, shorten dwell times, extend the end time, or split across
  another day. Do not overstuff a fixed window and pretend it fits.

## Buffer & resilience

- Leave 15–30 min of unallocated slack across the day for slow meals, lines, or
  lingering.
- Add a one-line backup: an indoor option if rain is possible, and what to do if a
  stop is unexpectedly closed.
