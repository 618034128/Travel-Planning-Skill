# Contributing

Thanks for your interest. This is a [Claude Agent Skill](https://docs.claude.com) —
mostly Markdown instructions plus one helper script.

## Ways to help

- Improve the heuristics in `references/*.md` — better defaults, pacing, or meal
  logic.
- Add transport or maps providers in `scripts/build_map_links.py`.
- Contribute a real itinerary the skill produced to `examples/`.

## Before opening a PR

- Keep `SKILL.md` and the files it points to in sync. Every `references/...` or
  `scripts/...` path mentioned in `SKILL.md` must exist — CI checks this.
- If you change the folder structure, rebuild the packaged `.skill` file.
- Run the smoke test locally:
  ```
  python scripts/build_map_links.py --china --city Test --stops "A,Test" "B,Test"
  ```

## Style

- Plain, concrete prose. The skill's voice is honest and specific, not salesy.
- No emojis in the skill files.
