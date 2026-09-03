# Skill（配布用エージェントスキル集）

[nakane-labo](https://github.com/nakane-labo) から配布する AI エージェント用スキルをまとめたリポジトリです。

Cursor / Claude Code の GitHub インストールは、**リポジトリ直下に `SKILL.md` が1つ**あることを前提にします。このリポジトリにはスキルが3つ入っているので、**リポジトリ全体の URL や全体 ZIP は使わないでください。** 使いたいスキルのフォルダだけを、下の個別 ZIP から入れてください。

## 収録スキル

| フォルダ | 対象 | 用途 | 個別 ZIP |
|----------|------|------|----------|
| [`academic-research-skills-nakanelabo/`](academic-research-skills-nakanelabo/) | Claude Code / Cursor | 研究〜論文執筆・査読の学術スキルバンドル（中根ラボ版） | [academic-research-skills-nakanelabo.zip](https://github.com/nakane-labo/Skill/releases/latest/download/academic-research-skills-nakanelabo.zip) |
| [`paper-kodoku-prep/`](paper-kodoku-prep/) | Claude Code / Cursor | 論文購読（輪読・抄読・ジャーナルクラブ）の対話型準備ガイド | [paper-kodoku-prep.zip](https://github.com/nakane-labo/Skill/releases/latest/download/paper-kodoku-prep.zip) |
| [`booksection-rindoku-prep/`](booksection-rindoku-prep/) | Claude Code / Cursor | 本の輪読（章担当発表・テキスト講読）の対話型準備ガイド | [booksection-rindoku-prep.zip](https://github.com/nakane-labo/Skill/releases/latest/download/booksection-rindoku-prep.zip) |

### 購読準備スキルの使い分け

| 渡すもの | 使うスキル |
|----------|-----------|
| 雑誌論文・学会論文（PDF 1本） | [`paper-kodoku-prep`](paper-kodoku-prep/) |
| 書籍・テキストの **1章分** | [`booksection-rindoku-prep`](booksection-rindoku-prep/) |

### 購読準備スキルの主な機能（2026年7月版）

両スキルとも、AI に要約だけもらって終わりにしない **対話型の精読ガイド** です。共通の設計思想は次のとおりです。

- **STEP 0〜7 を1ステップずつ**進める（要約を先に全部出さない）
- **本文に戻らないと答えられない選択式クイズ**（A/B/C/D）を中心に出題
- **進捗メモ**で中断・再開（別日に「続きから」で再開可能）
- **発表用スライド（.pptx）**まで仕上げ、説明できるか最終確認
- **1〜2回生向けの組み立て選択肢方式**（自由記述で詰まったときの補助）

| 機能 | paper-kodoku-prep | booksection-rindoku-prep |
|------|-------------------|--------------------------|
| 対象 | 論文1本（量的・質的・レビュー・英語） | 本の1章（M/E/T/K タイプ） |
| 所要時間 | 1〜2時間 | 担当1〜2時間／聞き手15〜30分 |
| 固有機能 | 英語論文モード、論文タイプ別（A/B/C/D） | 聞き手モード、章間参照、目次マップ |
| 詳細 | [`paper-kodoku-prep/README.md`](paper-kodoku-prep/README.md) | [`booksection-rindoku-prep/README.md`](booksection-rindoku-prep/README.md) |

## ダウンロード（初学者向け）

### 1. 使いたいスキルの ZIP だけ取得する

上の表の「個別 ZIP」をクリックします。リポジトリ全体（`Skill-main.zip`）は入れないでください。

### 2. 解凍する

ZIP をダブルクリックで解凍します。中にスキル名のフォルダ（例: `paper-kodoku-prep`）があり、その直下に `SKILL.md` があります。

### 3. インストール先を選ぶ

| ツール | プロジェクトだけで使う | すべてのプロジェクトで使う |
|--------|------------------------|---------------------------|
| **Claude Code** | プロジェクト直下 `.claude/skills/` | `~/.claude/skills/` |
| **Cursor** | プロジェクト直下 `.cursor/skills/` | `~/.cursor/skills/` |

例（論文購読プレップを Claude Code のプロジェクト用に入れる場合）:

```
あなたのゼミフォルダ/
└── .claude/
    └── skills/
        └── paper-kodoku-prep/
            ├── SKILL.md
            ├── README.md
            └── references/
```

Cursor の Skills 画面に GitHub URL を貼る場合も、**このカタログの URL は使わない**で、上の個別 ZIP を解凍してフォルダを置いてください。

### 4. 動作確認

- コピー先に `SKILL.md` があることを確認する
- **新しいエージェントセッション**を開く（初回はツールの再起動が必要なことがあります）
- 論文 PDF や章の PDF を渡し、「購読の準備をしたい」と依頼する

## Git で1スキルだけ取る場合

リポジトリ全体を clone したあと、使うフォルダだけコピーしても構いません。

```bash
git clone --depth 1 https://github.com/nakane-labo/Skill.git
cp -R Skill/paper-kodoku-prep ~/.cursor/skills/paper-kodoku-prep
```

`sparse-checkout` で最初から1フォルダだけ取る例:

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/nakane-labo/Skill.git
cd Skill
git sparse-checkout set paper-kodoku-prep
```

## インストール先（スキルごとの詳細）

### academic-research-skills-nakanelabo

| ツール | 配置先 |
|--------|--------|
| Claude Code | `.claude/skills/academic-research-skills-nakanelabo/` または `~/.claude/skills/` |
| Cursor | `.cursor/skills/academic-research-skills-nakanelabo/` または `~/.cursor/skills/` |

詳細は [`academic-research-skills-nakanelabo/README.md`](academic-research-skills-nakanelabo/README.md) および [`概要.md`](academic-research-skills-nakanelabo/概要.md) を参照。

### paper-kodoku-prep（論文購読プレップ）

| ツール | 配置先 |
|--------|--------|
| Claude Code | `.claude/skills/paper-kodoku-prep/` または `~/.claude/skills/paper-kodoku-prep/` |
| Cursor | `.cursor/skills/paper-kodoku-prep/` または `~/.cursor/skills/paper-kodoku-prep/` |

詳細は [`paper-kodoku-prep/README.md`](paper-kodoku-prep/README.md) を参照。

### booksection-rindoku-prep（本輪読プレップ）

| ツール | 配置先 |
|--------|--------|
| Claude Code | `.claude/skills/booksection-rindoku-prep/` または `~/.claude/skills/booksection-rindoku-prep/` |
| Cursor | `.cursor/skills/booksection-rindoku-prep/` または `~/.cursor/skills/booksection-rindoku-prep/` |

詳細は [`booksection-rindoku-prep/README.md`](booksection-rindoku-prep/README.md) を参照。

## 旧リポジトリ・旧名について

以下は本リポジトリへ統合済みです（アーカイブ）。

- `academic-research-skills-nakanelabo` → `academic-research-skills-nakanelabo/`
- `ronbun-kodoku-prep` → **`paper-kodoku-prep/`**（2026年7月に改名・大幅拡張）

`ronbun-kodoku-prep` フォルダは削除されています。最新版は `paper-kodoku-prep` を使ってください。
