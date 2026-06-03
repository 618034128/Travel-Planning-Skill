# Intake Checklist

The job of Phase 1 is to reach a confirmed trip spec while asking as few questions
as possible. The discipline: **default aggressively, ask narrowly, confirm always.**

## Parameter list

For each field below: if the user stated it, use it; if not, apply the default and
show it in the confirmation summary as an assumption the user can veto.

| Field | Ask only if... | Default if unstated |
|-------|----------------|---------------------|
| Destination(s) | always needed; ask if missing | — (cannot proceed without it) |
| Origin city | the trip clearly starts in another city | destination itself; only relevant if travel *to* it is implied |
| Inbound leg (when you arrive) | multi-city trip with a transport leg | arrive morning of day 1; confirm the arrival window if stated |
| Return leg (when you head back) | multi-city trip with a transport leg | depart after the last day's plan; confirm the latest acceptable departure |
| Trip length / which day(s) | pacing or hours depend on it | single day, the upcoming weekend |
| Daily start time | — | 9:00 |
| Daily end time | — | 18:00 |
| Day start/end location | route anchoring needs it | city-center hotel / main station; ask if no lodging known |
| Must-go places | always worth confirming | none beyond what's stated |
| Hard exclusions ("won't go") | — | none |
| Pace | it materially changes stop count | relaxed: ~4–5 stops/day + meals |
| Transport mode | it changes travel legs and ordering | walking + public transit |
| Group / who's going | affects pace, kid/elder-friendliness | 1–2 adults |
| Budget level | affects food/venue picks | mid-range |
| Dietary / accessibility needs | affects food and venues | none |
| Interests / vibe | helps fill "rest is up to you" | infer from must-dos + general highlights |
| Weather / season | outdoor-heavy plan | check if a tool is available; else add an indoor backup |

## How to ask (when you must)

- Bundle the few real questions into one short batch. Never drip them one per turn.
- Prefer offering options over open prompts when on a touch/mobile client — e.g.
  "packed or relaxed?", "walk / transit / drive?" — these are faster to answer.
- Don't ask about anything you can reasonably default. "Everything else is up to
  you" is permission to default, not a reason to ask more.

## What "confirm always" looks like

Even when you asked nothing (because everything was inferable), still show the
summary so there are no hidden assumptions. The user should be able to:
- approve in one glance, or
- correct exactly one line.

### Example A — partial request, needs a small batch

User said: "I want to show two friends around Nanjing on Saturday, we like trendy
cafes and dessert, back by evening."

Missing-but-defaultable: start time, anchor, pace, transport. Genuinely worth one
question: must-sees and end time. Respond with defaults + a tight batch:

```
Great — here's my read, correct anything:
• Nanjing, this Saturday, ~9:00 to (when do you want to be back — 18:00? later?)
• Vibe: trendy cafes + dessert, easygoing pace (~4–5 stops)
• Getting around: metro + walking, starting near the city center
• Any must-do spots, or should I pick the highlights for you?
Tell me those two things and I'll build it.
```

### Example B — complete request

User said: "Plan me one day in Kyoto next Tuesday, out by 8:30 back by 19:00, must
do Fushimi Inari and Nishiki Market, relaxed pace, I'll walk and take trains."

Nothing essential is missing. Still confirm first, then offer to build same-turn:

```
Locked in — say go and I'll plot it:
• Kyoto, next Tuesday, 8:30–19:00
• Must-do: Fushimi Inari, Nishiki Market
• Relaxed (~5 stops + meals), walking + trains
• I'll add highlights between your two anchors + lunch and a tea break
Go?
```

## Anti-patterns

- ❌ Producing a full itinerary from a one-line request without confirming.
- ❌ Asking a long questionnaire for a casual day trip.
- ❌ Asking for things already said earlier in the conversation.
- ❌ Hiding assumptions (e.g. silently deciding the day ends at a place far from their hotel).
