# 論文購読プレップ（Claude Code スキル）

ゼミの論文購読（輪読・抄読会）の事前準備を、対話型クイズと発表スライド作成までガイドする **Claude Code 向け**スキルです。

> **Cursor 用ではありません。** インストール先は `.claude/skills/` です。

## ダウンロード

本スキルは [`nakane-labo/Skill`](https://github.com/nakane-labo/Skill) リポジトリの `ronbun-kodoku-prep/` に収録されています。

1. [Skill リポジトリ](https://github.com/nakane-labo/Skill) の **Code** → **Download ZIP** で ZIP を取得する  
2. 解凍し、`ronbun-kodoku-prep` フォルダだけを使う（パス例: `Skill-main/ronbun-kodoku-prep/`）

ZIP の直接リンク（リポジトリ全体・main ブランチ）:

https://github.com/nakane-labo/Skill/archive/refs/heads/main.zip

## Claude Code へのインストール

1. ZIP を解凍する  
2. フォルダ `ronbun-kodoku-prep` を、次のいずれかにコピーする  
   - **プロジェクト用**（そのゼミ・研究フォルダだけ）: プロジェクト直下の `.claude/skills/`  
   - **全プロジェクト共通**: `~/.claude/skills/`（Mac はホームの `.claude/skills/`）
3. パス例: `.claude/skills/ronbun-kodoku-prep/SKILL.md` が存在することを確認する  
4. **新しい Claude Code セッション**を開く（初回で `.claude/skills/` を作った場合は再起動が必要なことがあります）

参考: [Claude Code — Extend Claude with skills](https://code.claude.com/docs/en/skills)

## 使い方

Claude Code で論文 PDF を渡し、例えば次のように依頼してください。

- 「この論文の購読の準備をしたい」
- 「輪読会の発表準備を手伝って」
- 「IMRAD で要約しながら理解度を確認したい」

スキルは要約を先に全部出さず、選択式クイズと問いかけで **1ステップずつ** 進みます。

## 同梱ファイル

| ファイル | 内容 |
|----------|------|
| `SKILL.md` | スキル本体 |
| `references/slide_guidelines.md` | 発表スライド作成時の参照ガイド |

## ライセンス・注意

立命館大学 中根研究室のゼミ・講義向け教材です。授業外への再配布は指導教員の指示に従ってください。
