# Example: A weekend in Nanjing (from Lianyungang)

This is a real run of the skill, lightly edited for length. It shows the whole
loop: intake, the confirmation gate, the inter-city train recommendation, a
maps-tool-free route built from `build_map_links.py`, and a couple of revisions.

> The traveler's host agent had **no** interactive maps tool and **no** 12306 MCP
> connected, so the skill fell back to query-then-recommend for the train and to
> shareable Amap links for the in-city routes. That's the worst case — it still
> produces a usable plan.

---

## 1. What the traveler asked for

> "From Lianyungang to Nanjing. Leave the evening of 6/5, come back the evening of
> 6/7. I want to visit **8号黄油面包店** (No.8 Butter Bakery) and **鸡鸣寺**
> (Jiming Temple), and I want good **matcha** — find me a place. Also **夫子庙**
> and **中山陵**, and some local specialty dishes. On the night of 6/6 I want to
> hit **OvO bar**. On 6/7 I'd like a later train back."

## 2. The skill confirmed before planning

It defaulted the unstated fields and showed them back for one approval:

| Field | Value | Source |
|---|---|---|
| Travelers | 1 | default |
| Arrive Nanjing | ~19:00–20:00 on 6/5 | stated |
| Days on the ground | 6/6 (full), 6/7 (until evening train) | derived |
| Pace | Standard, walkable clusters | default |
| Budget | Mid-range | default |
| Must-visits | 8号黄油面包店, 鸡鸣寺, 夫子庙, 中山陵, OvO bar | stated |
| Food wants | Matcha dessert + Nanjing specialties | stated |
| Return | Later train on 6/7 evening | stated |

## 3. Inter-city legs (query, not booking)

No 12306 MCP was connected, so the skill queried public timetables and
**recommended** concrete trains — it did **not** attempt to buy (12306 needs
real-name auth + payment; that stays with the traveler):

- **Inbound 6/5 evening:** Lianyungang → Nanjing, arriving ~20:00.
- **Return 6/7 evening (recommended):** **G1547  南京南 20:36 → 连云港东 23:03**
  (latest sensible departure). Alternate: G7792  20:19 → 23:27.

> Booking boundary: the skill hands you the exact train + date to purchase
> yourself. See `references/transport-and-booking.md`.

## 4. Day-by-day plan

### Day 1 — 6/6 (Sat)

| Time | Stop | Notes |
|---|---|---|
| 08:30 | **8号黄油面包店** (中山南路熙南里13一层) | Opens 08:30; grab breakfast pastries |
| 09:30 | **鸡鸣寺** | 07:00–17:30, ¥10; weekend cap ~600/hr — reserve ahead |
| 11:30 | Lunch — Nanjing specialties | 盐水鸭 / 鸭血粉丝汤 / 皮肚面 |
| 14:00 | **西尾抹茶** (near 新街口) | Dedicated matcha; alts: 怪兽抹茶, 辻利TSUJIRI |
| 16:00 | **夫子庙 / 老门东** | Qinhuai riverside; 悦舍食单 matcha "青苔" if you want more |
| 19:00 | Dinner near 夫子庙 | — |
| 21:30 | **OvO bar** | 🔲 Address unconfirmed — paste the location and the skill re-stitches the evening |

Route link (新街口 → 夫子庙, transit), built by the script:

```
https://uri.amap.com/navigation?from=name:%E6%96%B0%E8%A1%97%E5%8F%A3%2C%E5%8D%97%E4%BA%AC&to=name:%E5%A4%AB%E5%AD%90%E5%BA%99%2C%E5%8D%97%E4%BA%AC&mode=bus&policy=1&src=itinerary&coordinate=gaode
```

### Day 2 — 6/7 (Sun, until the train)

| Time | Stop | Notes |
|---|---|---|
| 09:00 | **中山陵** | Free but **requires advance reservation**; closed Mondays (6/7 Sun = open) |
| 12:00 | Lunch | — |
| 14:00 | Buffer / souvenirs near 新街口 | Matcha to-go if you missed it Day 1 |
| ~19:30 | To 南京南 station | Allow 45–60 min before G1547 (20:36) |
| 20:36 | **G1547 → 连云港东 (23:03)** | Recommended return |

Route link (新街口 → 南京南站, transit):

```
https://uri.amap.com/navigation?from=name:%E6%96%B0%E8%A1%97%E5%8F%A3%2C%E5%8D%97%E4%BA%AC&to=name:%E5%8D%97%E4%BA%AC%E5%8D%97%E7%AB%99&mode=bus&policy=1&src=itinerary&coordinate=gaode
```

## 5. Revisions (the normal loop)

- *"Matcha got buried."* → The skill surfaced dedicated matcha shops (西尾抹茶,
  怪兽抹茶, 麻釉抹茶料理, 辻利TSUJIRI, 大洋百货 B1 宇治茶铺) as a Day-1 afternoon
  block instead of one buried line.
- *"Later train on 6/7."* → Re-queried and moved the recommendation to G1547 20:36.

> Honesty note: **OvO bar** could not be verified from public sources at planning
> time, so it stays a 🔲 placeholder rather than a fabricated address. Paste the
> real location and the skill re-paces that evening.
