# Transport & Booking

Most trips start somewhere other than the destination. This covers the **inter-city
legs** — getting there and back — and the firm line between what the skill does
(query and recommend) and what the user must do (actually buy).

## When this applies

Whenever the origin differs from the destination — "I want to go from Lianyungang to
Nanjing", "fly to Tokyo Friday night, back Sunday evening" — the arrival and
departure legs are part of the plan, not background. Capture them in Phase 1 (see
the origin / inbound / return rows in `intake-checklist.md`) and schedule them in
Phase 2 like any other leg.

## Step 1: Detect a transport tool

Check what the current agent has available:

- A **12306 MCP** (mainland-China rail) — real-time train numbers, departure/arrival
  times, fares, seat availability, and transfer planning. A query server such as
  `mcp-server-12306` is the recommended one. Use it to look up concrete trains for
  the inbound and return legs.
- A **flight or multi-modal search** tool — use it the same way for air legs.
- A general **search/fetch** capability — fall back to it to read published
  timetables when no dedicated tool exists.
- Nothing — give the user booking-site links (12306, Ctrip, etc.) to search.

### Recommended MCP config (12306, query-only)

For a Claude client that loads MCP servers:

```json
{
  "mcpServers": {
    "12306": { "command": "uvx", "args": ["mcp-server-12306"] }
  }
}
```

## Step 2: Query, then recommend a specific option

With a transport tool available, don't stop at "take a train." Look up the real
board and recommend a concrete option that fits the confirmed timing:

- **Arrival leg:** pick a service that lands with enough evening left to be useful,
  but not so late the user can't check in or eat.
- **Return leg:** pick the latest sensible departure that still respects how late
  the user wants to stay, and state the arrival-home time so they can judge it.
- Always surface **train/flight number, departure, arrival, duration, and rough
  fare.** Name the source and note that schedules can change.

## Step 3: The booking boundary — query yes, purchase no

**The skill never completes a purchase.** Train and hotel booking require real-name
authentication, a captcha, and live payment; 12306 in particular blocks automated
buying by design. The query MCPs reflect this — they look things up, they do not
buy. Be honest about it:

- **Do:** find trains, compare times and prices, recommend the best fit, and hand
  over the exact train number + date for the user to search.
- **Don't:** claim to have booked anything, ask for the user's payment details or ID
  number to buy on their behalf, or imply an MCP can purchase.
- **Hand off cleanly:** "Here's the train — buy it on the 12306 app/site, it's a
  minute's work."

The same holds for lodging: recommend an area and a couple of specific properties,
link the search, but the user books.
