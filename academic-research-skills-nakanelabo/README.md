# academic-research-skills-nakanelabo

研究から論文執筆・査読までをカバーする **Claude Code / Cursor 用スキルバンドル**（中根ラボ版）。

> **Claude Code**: ZIP 内の `SKILL.md` は**ルートに1つだけ**（各サブフォルダは `SUBSKILL.md`）。ファイル上限（200）に収めるため、開発用スクリプト・設計ドキュメント・サンプル PDF は含みません。

## クイックスタート

1. **このスキルの ZIP だけ**をダウンロードする（カタログ全体の `Skill-main.zip` は使わない）
   - [academic-research-skills-nakanelabo.zip](https://github.com/nakane-labo/Skill/releases/latest/download/academic-research-skills-nakanelabo.zip)
2. 解凍した `academic-research-skills-nakanelabo` フォルダをスキル配置先に置く
   - Claude Code: `.claude/skills/academic-research-skills-nakanelabo/` または `~/.claude/skills/academic-research-skills-nakanelabo/`
   - Cursor: `.cursor/skills/academic-research-skills-nakanelabo/` または `~/.cursor/skills/academic-research-skills-nakanelabo/`
3. フォルダ直下の `SKILL.md` がエントリポイント。人間向けの全体像は **[概要.md](概要.md)** を参照

## 構成（4 サブスキル）

| フォルダ | 用途 |
|----------|------|
| `deep-research/` | 学術調査・文献レビュー |
| `academic-paper/` | 論文執筆（日本語段落・流れ: `references/academic_writing_advice_ja.md`） |
| `academic-paper-reviewer/` | 模擬ピアレビュー |
| `academic-pipeline/` | 全工程オーケストレーション |
| `shared/` | スキル間の共有プロトコル・スキーマ |

**バンドル版**: v3.14.0 系（academic-paper **3.2.0**、`academic_writing_advice_ja` 含む）

## ライセンス

[CC BY-NC 4.0](LICENSE)（上流 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 由来部分に準拠）
