# Skill（Claude デスクトップ用スキル集）

[nakane-labo](https://github.com/nakane-labo) から配布する、**Claude デスクトップ**向けスキルのカタログです。ゼミでは Cursor や Claude Code ではなく、Claude デスクトップに入れて使ってください。

このリポジトリにはスキルが4つ入っています。GitHub の **Code → Download ZIP**（リポジトリ全体）は使わないでください。Claude デスクトップは **スキル1つ分の ZIP** をアップロードする前提です。下の個別 ZIP を1つだけ取って、解凍せずにアップロードします。

## 収録スキル

| フォルダ | 用途 | 個別 ZIP |
|----------|------|----------|
| [`academic-research-skills-nakanelabo/`](academic-research-skills-nakanelabo/) | 研究〜論文執筆・査読の学術スキルバンドル（中根ラボ版） | [academic-research-skills-nakanelabo.zip](https://github.com/nakane-labo/Skill/releases/latest/download/academic-research-skills-nakanelabo.zip) |
| [`paper-kodoku-prep/`](paper-kodoku-prep/) | 論文購読（輪読・抄読・ジャーナルクラブ）の対話型準備ガイド | [paper-kodoku-prep.zip](https://github.com/nakane-labo/Skill/releases/latest/download/paper-kodoku-prep.zip) |
| [`booksection-rindoku-prep/`](booksection-rindoku-prep/) | 本の輪読（章担当発表・テキスト講読）の対話型準備ガイド | [booksection-rindoku-prep.zip](https://github.com/nakane-labo/Skill/releases/latest/download/booksection-rindoku-prep.zip) |
| [`lecture-reaction-sheet/`](lecture-reaction-sheet/) | 講義感想シート（リアクションペーパー）の対話型作成ガイド | [lecture-reaction-sheet.zip](https://github.com/nakane-labo/Skill/releases/latest/download/lecture-reaction-sheet.zip) |

### 購読準備スキルの使い分け

| 渡すもの | 使うスキル |
|----------|-----------|
| 雑誌論文・学会論文（PDF 1本） | [`paper-kodoku-prep`](paper-kodoku-prep/) |
| 書籍・テキストの **1章分** | [`booksection-rindoku-prep`](booksection-rindoku-prep/) |

### 購読準備スキルの主な機能（2026年7月版）

両スキルとも、AI に要約だけもらって終わりにしない **対話型の精読ガイド** です。

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

### 講義感想シート作成スキル（lecture-reaction-sheet）

大学の講義の感想シート（リアクションペーパー）を、学生が講義を十分理解し自分の言葉で書けるようになるまで対話的にガイドします。講義資料（必須・音声/動画は任意）をもとに、理解度クイズ→日常体験との接続→他講義・社会学的概念との接続を経てから、学生自身が感想を書き上げます。**完成した感想シートを安易に渡さない**ことを最優先するスキルです。詳細は [`lecture-reaction-sheet/README.md`](lecture-reaction-sheet/README.md) を参照。

## Claude デスクトップへの入れ方

ZIP の中は `paper-kodoku-prep/SKILL.md` のように、**スキル名フォルダが入った状態**になっています。解凍して中身だけを再圧縮すると失敗するので、**ダウンロードした ZIP をそのまま**アップロードしてください。

### 1. 準備

1. Claude デスクトップを開く
2. **Settings → Capabilities** で **Code execution and file creation** をオンにする
3. 左の **Customize → Skills** が開けることを確認する（見えないときは上のスイッチがオフです）

公式の手順は [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) です。

### 2. 使うスキルの ZIP だけ取る

上の表の「個別 ZIP」をクリックします。リポジトリ全体（`Skill-main.zip`）は入れないでください。

### 3. アップロードする

1. **Customize → Skills**
2. **+** → **Create skill** → **Upload a skill**
3. ダウンロードした ZIP を選ぶ（解凍しない）
4. 一覧に出たらスイッチをオンにする

### 4. 動作確認

新しいチャットを開き、論文 PDF・章の PDF・講義資料などを添付して、例えば「購読の準備をしたい」「感想シートを書きたい」と頼む。スキルが使われないときは、Customize → Skills でオンになっているか確認する。

## 旧名

- `ronbun-kodoku-prep` は **`paper-kodoku-prep`** に改名済みです
- 学術スキルは `academic-research-skills-nakanelabo/` を使ってください
