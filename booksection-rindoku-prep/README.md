# 本輪読プレップ（booksection-rindoku-prep）

ゼミの「本の輪読」（書籍・テキスト講読・章担当発表）の事前準備を、対話型クイズと発表スライド作成までガイドするスキルです。

担当章だけをつぎはぎで読ませない。**本全体の中での章の位置づけ**と、前の章・次の章との接続を意識しながら、問いかけとクイズで **1ステップずつ** 進めます。

## こんなときに使う

- ゼミの本輪読で担当章の発表準備
- 書籍・テキストの1章分（PDF・スキャン）を読み解きたい
- 担当章のレジュメやスライドを作りたい
- 今週は聞く側。発表への質問を考えたい（聞き手モード）
- 前回の「進捗メモ」を貼って「続きから」再開したい

## 対応範囲

| 本のタイプ | 記号 | 例 |
|-----------|------|-----|
| 単著モノグラフ | M | 1つの調査・議論を本全体で展開 |
| 論集・編著 | E | 章ごとに著者が違う |
| 理論書・古典 | T | 理論の展開・古典の読解 |
| 教科書・概説書 | K | テーマごとに章が独立 |

> **雑誌論文1本**の購読準備は姉妹スキル [`paper-kodoku-prep`](../paper-kodoku-prep/) を使います。論集の章でも、本の一部として渡されたらこのスキルで進めます。

## ダウンロード

本スキルは [`nakane-labo/Skill`](https://github.com/nakane-labo/Skill) リポジトリの `booksection-rindoku-prep/` に収録されています。

### 方法A：リポジトリ全体を ZIP で取得（おすすめ）

1. [Skill リポジトリ](https://github.com/nakane-labo/Skill) を開く
2. 緑色の **Code** ボタン → **Download ZIP** をクリック
3. ZIP を解凍する（フォルダ名は `Skill-main` など）
4. 中の `booksection-rindoku-prep` フォルダだけを使う

ZIP の直接リンク（main ブランチ）:

https://github.com/nakane-labo/Skill/archive/refs/heads/main.zip

### 方法B：Git で clone する

```bash
git clone https://github.com/nakane-labo/Skill.git
cd Skill/booksection-rindoku-prep
```

## インストール先

| ツール | 配置先 |
|--------|--------|
| **Claude Code**（プロジェクト用） | プロジェクト直下の `.claude/skills/booksection-rindoku-prep/` |
| **Claude Code**（全プロジェクト共通） | `~/.claude/skills/booksection-rindoku-prep/` |
| **Cursor**（プロジェクト用） | プロジェクト直下の `.cursor/skills/booksection-rindoku-prep/` |
| **Cursor**（全プロジェクト共通） | `~/.cursor/skills/booksection-rindoku-prep/` |

### 手順（Claude Code の例）

1. 上記のいずれかの配置先に `booksection-rindoku-prep` フォルダを丸ごとコピーする
2. 次のファイルが存在することを確認する  
   `…/booksection-rindoku-prep/SKILL.md`
3. **新しいセッション**を開く（初回でスキルフォルダを作った場合は再起動が必要なことがあります）

参考:

- [Claude Code — Extend Claude with skills](https://code.claude.com/docs/en/skills)
- [Cursor — Agent Skills](https://cursor.com/docs/context/skills)

## 使い方

担当章の PDF をエージェントに渡し、例えば次のように依頼してください。

- 「第3章の輪読準備をしたい」
- 「担当章の発表スライドを一緒に作って」
- 「この章が本全体のどこに位置するか整理したい」
- 「今週は聞く側。質問を考えたい」
- 「前回の進捗メモを貼るので、続きからお願いします」

章の PDF だけしかない場合、スキルは書誌情報や目次の確認を促します。手元の本の目次を教えてもらうか、web 検索で目次を調べて進めます。

## 同梱ファイル

| ファイル | 内容 |
|----------|------|
| `SKILL.md` | スキル本体（対話の進め方・聞き手モード・中断再開など） |
| `references/book_types.md` | 本のタイプ別（M/E/T/K）の問いのパターン |
| `references/slide_guidelines.md` | 発表スライド作成時の参照ガイド |

## ライセンス・注意

立命館大学 中根研究室のゼミ・講義向け教材です。授業外への再配布は指導教員の指示に従ってください。
