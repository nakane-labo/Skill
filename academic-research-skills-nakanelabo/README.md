# academic-research-skills-nakanelabo

研究から論文執筆・査読までをカバーする **Claude デスクトップ用**スキルバンドル（中根ラボ版）。

ZIP 内の `SKILL.md` は**ルートに1つだけ**です（各サブフォルダは `SUBSKILL.md`）。ファイル数が多くなりすぎないよう、開発用スクリプト・設計ドキュメント・サンプル PDF は含みません。

## クイックスタート

1. **このスキルの ZIP だけ**をダウンロードする（カタログ全体の `Skill-main.zip` は使わない。**解凍もしない**）
   - [academic-research-skills-nakanelabo.zip](https://github.com/nakane-labo/Skill/releases/latest/download/academic-research-skills-nakanelabo.zip)
2. Claude デスクトップで **Settings → Capabilities** の **Code execution and file creation** をオンにする
3. **Customize → Skills** → **+** → **Create skill** → **Upload a skill** で ZIP をアップロードする
4. 一覧のスイッチをオンにする
5. ルートの `SKILL.md` がエントリポイント。人間向けの全体像は **[概要.md](概要.md)** を参照

公式手順: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## 構成（4 サブスキル）

| フォルダ | 用途 |
|----------|------|
| `deep-research/` | 学術調査・文献レビュー |
| `academic-paper/` | 論文執筆（日本語段落・流れ: `references/academic_writing_advice_ja.md`） |
| `academic-paper-reviewer/` | 模擬ピアレビュー |
| `academic-pipeline/` | 全工程オーケストレーション |
| `shared/` | スキル間の共有プロトコル・スキーマ |

**バンドル版**: v3.14.0 系（academic-paper **3.2.0**、`academic_writing_advice_ja` 含む）

## 出典とライセンス

このスキルは、Cheng-I Wu 氏の [academic-research-skills](https://github.com/Imbad0202/academic-research-skills)（Imbad0202/academic-research-skills）をもとに、中根ラボが**改変**したものです。

- 原著作者: Cheng-I Wu
- ライセンス: [Creative Commons 表示-非営利 4.0 国際（CC BY-NC 4.0）](https://creativecommons.org/licenses/by-nc/4.0/deed.ja)。全文は [LICENSE](LICENSE)
- 改変の内容: ルート `SKILL.md` の新設とサブスキルの `SUBSKILL.md` への改名、日本語の段落・流れの指針と社会学評論スタイルガイドの追加、参考文献形式の変更、日本語トリガーの追加、ファイル数の削減（本家の一部ファイルを除外）
- 非営利の利用に限ります。営利目的での利用・配布はできません。

本家との関係と改変の一覧は、リポジトリの `docs/academic-research-skills-nakanelabo/UPSTREAM.md` にあります。
