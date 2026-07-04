# 論文購読プレップ（paper-kodoku-prep）

ゼミの論文購読（輪読・抄読会・ジャーナルクラブ・論文紹介）の事前準備を、対話型クイズと発表スライド作成までガイドするスキルです。

AI に要約だけもらって終わりにしない。選択式クイズと問いかけで **1ステップずつ** 進み、本文・図表を自分で探して答えさせ、最後に発表用スライド（.pptx）まで仕上げます。

## こんなときに使う

- ゼミの輪読・抄読会・論文紹介の発表準備
- 論文 PDF を渡して「読み解きたい」「理解度を確認したい」
- IMRAD 形式で要約しながら精読したい
- 前回の「進捗メモ」を貼って「続きから」再開したい

## 対応範囲

| 種類 | 例 |
|------|-----|
| 量的研究 | アンケート調査、実験研究 |
| 質的研究 | インタビュー、M-GTA、事例研究 |
| 混合研究法 | 質量併用 |
| レビュー・理論論文 | 制度分析、理論的考察 |
| 英語論文 | 段落単位で一緒に読むモードあり |

> **本の1章の輪読**は姉妹スキル [`booksection-rindoku-prep`](../booksection-rindoku-prep/) を使います。

## ダウンロード

本スキルは [`nakane-labo/Skill`](https://github.com/nakane-labo/Skill) リポジトリの `paper-kodoku-prep/` に収録されています。

### 方法A：リポジトリ全体を ZIP で取得（おすすめ）

1. [Skill リポジトリ](https://github.com/nakane-labo/Skill) を開く
2. 緑色の **Code** ボタン → **Download ZIP** をクリック
3. ZIP を解凍する（フォルダ名は `Skill-main` など）
4. 中の `paper-kodoku-prep` フォルダだけを使う

ZIP の直接リンク（main ブランチ）:

https://github.com/nakane-labo/Skill/archive/refs/heads/main.zip

### 方法B：Git で clone する

```bash
git clone https://github.com/nakane-labo/Skill.git
cd Skill/paper-kodoku-prep
```

## インストール先

| ツール | 配置先 |
|--------|--------|
| **Claude Code**（プロジェクト用） | プロジェクト直下の `.claude/skills/paper-kodoku-prep/` |
| **Claude Code**（全プロジェクト共通） | `~/.claude/skills/paper-kodoku-prep/` |
| **Cursor**（プロジェクト用） | プロジェクト直下の `.cursor/skills/paper-kodoku-prep/` |
| **Cursor**（全プロジェクト共通） | `~/.cursor/skills/paper-kodoku-prep/` |

### 手順（Claude Code の例）

1. 上記のいずれかの配置先に `paper-kodoku-prep` フォルダを丸ごとコピーする
2. 次のファイルが存在することを確認する  
   `…/paper-kodoku-prep/SKILL.md`
3. **新しいセッション**を開く（初回でスキルフォルダを作った場合は再起動が必要なことがあります）

参考:

- [Claude Code — Extend Claude with skills](https://code.claude.com/docs/en/skills)
- [Cursor — Agent Skills](https://cursor.com/docs/context/skills)

## 使い方

論文 PDF をエージェントに渡し、例えば次のように依頼してください。

- 「この論文の購読の準備をしたい」
- 「輪読会の発表準備を手伝って」
- 「IMRAD で要約しながら理解度を確認したい」
- 「前回の進捗メモを貼るので、続きからお願いします」

スキルは STEP 0〜7 を **一度に1ステップずつ** 進めます。要約を先に全部出しません。

## 同梱ファイル

| ファイル | 内容 |
|----------|------|
| `SKILL.md` | スキル本体（対話の進め方・クイズ設計・中断再開など） |
| `references/paper_types.md` | 論文タイプ別（量的・質的・レビュー等）の問いのパターン |
| `references/slide_guidelines.md` | 発表スライド作成時の参照ガイド |

## 旧名について

旧リポジトリ名 `ronbun-kodoku-prep` は **`paper-kodoku-prep` に改名**しました。中身は大幅に拡張されています（質的研究・英語論文・進捗メモ再開など）。

## ライセンス・注意

立命館大学 中根研究室のゼミ・講義向け教材です。授業外への再配布は指導教員の指示に従ってください。
