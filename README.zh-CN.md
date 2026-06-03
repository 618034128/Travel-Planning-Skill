# 旅行规划技能（Travel Planning Skill）— 一个 Claude Agent Skill

[English](README.md) | **简体中文**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Agent Skill](https://img.shields.io/badge/Claude-Agent%20Skill-8A2BE2)](https://docs.claude.com)
[![Validate skill](https://github.com/618034128/Travel-Planning-Skill/actions/workflows/validate.yml/badge.svg)](https://github.com/618034128/Travel-Planning-Skill/actions/workflows/validate.yml)
[![GitHub stars](https://img.shields.io/github/stars/618034128/Travel-Planning-Skill?style=social)](https://github.com/618034128/Travel-Planning-Skill/stargazers)

一个 [Claude Agent Skill](https://docs.claude.com)，能把一句模糊的出行愿望，变成
**一条地图路线 + 一份按时间分块的每日行程**——而且最关键的是：**在动手规划之前，
会先跟你确认每一个出行参数**，绝不闷头做出一个错的行程。

你说：*“我想周六在南京玩，带两个朋友，大概 9 点出门、傍晚回来，我们喜欢网红咖啡和
甜点，剩下的你看着办。”*
技能会先把缺口补全（用合理的默认值）、回显给你确认，然后给出一条排好序的路线和一份
逐小时的计划。哪个点不喜欢？说一声，它就重新把这一天串起来。

## 实际效果

一次真实运行（连云港 → 南京周末游，含 12306 列车推荐和无地图工具时的高德链接回退）：
见 **[examples/nanjing-weekend.md](examples/nanjing-weekend.md)**。

## 目录结构

```
travel-planning-skill/
├── SKILL.md                          # 工作流：意图采集 → 确认 → 构建 → 修订
├── references/
│   ├── intake-checklist.md           # 要确认什么、默认值、确认话术示例
│   ├── maps-and-routing.md           # 地图工具探测 + 链接生成（国内 vs 国际）
│   ├── scheduling-heuristics.md      # 节奏、通行时间、用餐、营业时间
│   └── transport-and-booking.md      # 城际交通、12306 MCP、查询与购票的边界
└── scripts/
    └── build_map_links.py            # 生成 Google 地图 / 高德 / 百度 路线链接
```

## 设计亮点

- **确认门槛。** 技能的立身之本：不确认完出行参数，就不出路线、不出行程。“剩下的你
  看着办”意味着*用默认值填好、回显给你批准*，而不是*跳过确认*。
- **大胆默认，精准提问。** 把没说的字段用合理默认值填上，只就少数真正会改变方案的事项
  发问。
- **自适应地图工具。** 宿主 agent 若带交互式地图/地点工具，就渲染可交互路线；否则生成
  可分享链接——国际行程用 Google 地图，中国大陆用高德/百度（大陆 Google 地图不可靠）。
- **懂城际，且对购票边界很诚实。** 对于从外地出发的行程，它会查询往返车次的真实选项
  （若连接了 12306 MCP 则用它查大陆铁路），并推荐一趟具体的车。但它绝不替你买票：购票
  需要实名认证和支付，它会把确切的车次和日期交还给你自行购买。
- **行程贴近现实。** 通行时间、用餐时段、停留时长、营业时间核查、缓冲余量——不是一份
  无视耗时的幻想计划。
- **以修订为常态。** 删点、加点、重新调节奏、重新排序都被当作正常循环，只重算受影响的
  部分。

## 安装

把 `travel-planning-skill/` 文件夹放进你 agent 的 skills 目录；或在支持技能的客户端里
安装打包好的 `.skill` 文件。

## 许可证

MIT —— 见 [LICENSE](LICENSE)。
