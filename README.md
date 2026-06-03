# Travel Planning Skill — an Agent Skill

**English** | [简体中文](README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Agent Skill](https://img.shields.io/badge/Claude-Agent%20Skill-8A2BE2)](https://docs.claude.com)
[![Validate skill](https://github.com/618034128/Travel-Planning-Skill/actions/workflows/validate.yml/badge.svg)](https://github.com/618034128/Travel-Planning-Skill/actions/workflows/validate.yml)
[![GitHub stars](https://img.shields.io/github/stars/618034128/Travel-Planning-Skill?style=social)](https://github.com/618034128/Travel-Planning-Skill/stargazers)

A [Claude Agent Skill](https://docs.claude.com) that turns a loose travel wish into
a **map route + a time-blocked daily schedule** — and, crucially, **confirms every
trip parameter with you before it plans anything**, so it never wastes effort
building the wrong trip.

You say: *"I want to spend Saturday in Nanjing with two friends, out around 9 back
by evening, we love trendy cafes and dessert, rest is up to you."*
The agent confirms the gaps (defaulting the rest), then produces an ordered route
and an hour-by-hour plan. Don't like a stop? Say so and it re-stitches the day.

## See it in action

A real run — a Lianyungang → Nanjing weekend, with a 12306 train recommendation
and Amap fallback links generated when no maps tool was connected:
**[examples/nanjing-weekend.md](examples/nanjing-weekend.md)**.

## What's inside

```
travel-planning-skill/
├── SKILL.md                          # workflow: Intake → Confirm → Build → Revise
├── references/
│   ├── intake-checklist.md           # what to confirm, defaults, confirmation examples
│   ├── maps-and-routing.md           # maps-tool detection + link generation (China vs intl)
│   ├── scheduling-heuristics.md      # pacing, travel-time, meals, opening hours
│   └── transport-and-booking.md      # inter-city legs, 12306 MCP use, query-vs-book boundary
├── scripts/
│   └── build_map_links.py            # builds Google Maps / Amap / Baidu route URLs
└── examples/
    └── nanjing-weekend.md            # a real, worked-through itinerary
```

## Design highlights

- **Confirmation gate.** The skill's defining rule: no route, no schedule, until the
  trip spec is confirmed. "Everything else is up to you" means *default and show
  back for approval*, not *skip confirmation*.
- **Default aggressively, ask narrowly.** It fills unstated fields with sensible
  defaults and only asks about the few things that genuinely change the plan.
- **Maps-tool adaptive.** If the host agent has a places/map tool, it renders an
  interactive route. Otherwise it generates shareable links — Google Maps for
  international trips, Amap/Baidu for mainland China (where Google Maps is unreliable).
- **Inter-city aware, with an honest booking boundary.** For trips that start in
  another city, it queries real options for the inbound/return legs — using a 12306
  MCP for mainland-China rail when one is connected — and recommends a concrete
  train. It never buys: booking needs real-name auth and payment, so it hands the
  exact train and date back to you to purchase.
- **Realistic schedules.** Travel legs, meal slots, dwell times, opening-hour checks,
  and buffers — not a fantasy plan that ignores how long things take.
- **Revision-first.** Dropping, adding, re-pacing, and reordering stops are treated
  as the normal loop, regenerating only what's affected.

## Install

Drop the `travel-planning-skill/` folder into your agent's skills directory, or
install the packaged `.skill` file in a client that supports skills.

## License

MIT — see [LICENSE](LICENSE).
