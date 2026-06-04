# Skill（配布用エージェントスキル集）

[nakane-labo](https://github.com/nakane-labo) から配布する AI エージェント用スキルをまとめたリポジトリです。

## 収録スキル

| フォルダ | 対象 | 用途 |
|----------|------|------|
| [`academic-research-skills-nakanelabo/`](academic-research-skills-nakanelabo/) | **Claude Code / Cursor** | 研究〜論文執筆・査読の学術スキルバンドル（中根ラボ版） |
| [`ronbun-kodoku-prep/`](ronbun-kodoku-prep/) | **Claude Code のみ** | ゼミ論文購読（輪読・抄読）の対話型準備ガイド |

## ダウンロード

リポジトリ全体の ZIP:

https://github.com/nakane-labo/Skill/archive/refs/heads/main.zip

解凍後、使うスキルのフォルダだけを、下記の **対象ツールに応じた** スキル配置先にコピーしてください。

## インストール先（スキルごと）

### academic-research-skills-nakanelabo

| ツール | 配置先 |
|--------|--------|
| Claude Code | `.claude/skills/academic-research-skills-nakanelabo/` または `~/.claude/skills/` |
| Cursor | `.cursor/skills/academic-research-skills-nakanelabo/` または `~/.cursor/skills/` |

詳細は [`academic-research-skills-nakanelabo/README.md`](academic-research-skills-nakanelabo/README.md) および [`概要.md`](academic-research-skills-nakanelabo/概要.md) を参照。

### ronbun-kodoku-prep（Claude Code 専用）

| ツール | 配置先 |
|--------|--------|
| Claude Code | `.claude/skills/ronbun-kodoku-prep/` または `~/.claude/skills/ronbun-kodoku-prep/` |
| Cursor | **非対応**（本スキルは Claude Code 向けに設計） |

詳細は [`ronbun-kodoku-prep/README.md`](ronbun-kodoku-prep/README.md) を参照。

## 旧リポジトリについて

以下は本リポジトリへ統合済みです（アーカイブ）。

- `academic-research-skills-nakanelabo` → `academic-research-skills-nakanelabo/`
- `ronbun-kodoku-prep` → `ronbun-kodoku-prep/`
