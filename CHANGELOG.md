# Changelog

All notable changes to this skill are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/).

## [0.2.0] - 2026-06-03

### Added
- Inter-city transport handling: capture the origin city and inbound/return legs
  during intake, and schedule them in Phase 2.
- `references/transport-and-booking.md` — detecting and configuring a 12306 MCP for
  mainland-China rail, the query-then-recommend flow, and the hard boundary between
  querying options and completing a purchase.

### Changed
- Restructured the package into `references/` and `scripts/` to match the documented
  layout (previously the files were flat).
- Renamed the skill from `travel-itinerary-planner` to `travel-planning-skill`.

## [0.1.0] - 2026-06-03

### Added
- Initial release. A confirm-before-you-plan itinerary planner that produces a map
  route plus a time-blocked daily schedule, adapts to available maps tools, and
  falls back to Amap / Baidu / Google route links.
