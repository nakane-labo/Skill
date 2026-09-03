---
name: academic-research-skills-nakanelabo
description: >-
  Research-to-publication academic skill bundle (nakanelabo edition).
  4 sub-skills: deep-research (13-agent research), academic-paper (12-agent writing),
  academic-paper-reviewer (7-agent review), academic-pipeline (10-stage orchestrator).
  JSS Style Guide references. Japanese paragraph/flow guide (academic_writing_advice_ja).
  Japanese + English bilingual. Nakane Lab operational voice.
  Triggers: 論文執筆, 学術論文, 段落構成, パラグラフ, 文章の流れ, 序論, 考察, research, write paper, peer review,
  学術スキル一覧, どのスキルを使うか, 研究・論文・査読・パイプラインの使い分け.
---

# academic-research-skills-nakanelabo

研究から投稿までをカバーする学術スキルバンドル（中根ラボ版）。**Claude デスクトップでは本ファイル（ルート `SKILL.md`）のみがスキル定義**です。各サブフォルダの手順・エージェント定義は **`SUBSKILL.md`**（`agents/`・`references/` と併読）。人間向けの全体像は `概要.md` を参照。

## 共通の考え方（中根ラボ運用）

- 主張には**根拠と引用**を必ず付ける。断定よりも、根拠の強さを示して説明する。
- データだけ、理念だけ、現場感覚だけに寄らず、**データ・制度・現場**を往復して判断する。
- 矛盾や不確実性は隠さず、エビデンスの質とあわせて**開示**する。
- 成果物には **AI 利用の開示**を入れる。
- ツールは手段。**「紙に向き合う時間を減らし、人と向き合う時間を増やす」** という目的を外さない。

## サブスキル一覧

| サブスキル | フォルダ | 手順の正本 | 用途 |
|---|---|---|---|
| Deep Research | `deep-research/` | `deep-research/SUBSKILL.md` | 学術調査・文献レビュー・システマティックレビュー |
| Academic Paper | `academic-paper/` | `academic-paper/SUBSKILL.md` | 論文執筆・整形・査読対応 |
| Academic Paper Reviewer | `academic-paper-reviewer/` | `academic-paper-reviewer/SUBSKILL.md` | 査読シミュレーション |
| Academic Pipeline | `academic-pipeline/` | `academic-pipeline/SUBSKILL.md` | 全工程オーケストレーション |

## 振り分けルール

1. **パイプライン vs 単体**: 「研究から投稿まで一気に」→ `academic-pipeline/SUBSKILL.md` を読み、必要に応じて下位フォルダへ。文献調査だけ・執筆だけ・査読だけなら該当 `SUBSKILL.md` のみ。
2. **deep-research と academic-paper**: 上流が調査・下流が論文化。推奨: `deep-research/` → `academic-paper/`。
3. **モードの目安**: 研究課題が曖昧 → `deep-research/` の socratic。構成を一緒に → `academic-paper/` の plan。査読から学ぶ → `academic-paper-reviewer/` の guided。

## 日本語の段落・流れ（academic_writing_advice_ja）

原稿の主言語が日本語、または段落・論旨の流れを重視するときは、**必ず** `academic-paper/references/academic_writing_advice_ja.md` を読み、下書き・自己レビュー・模擬査読に反映する。

| 対象 | ルール（要約） |
|------|----------------|
| 各段落 | トピック・センテンス → サポーティング → コンクルーディング（冗長なら省略） |
| 序論 | 広い話題 → 狭い話題 |
| 考察 | 狭い話題 → 広い話題 |
| 段落間 | トピック・センテンスだけ読んで大筋が通ること |
| 文間 | 後文が前文の後半を引き受ける |
| 文の形 | 主語と述語を近づける；一文一義 |
| 接続詞 | 必要最小限 |

連携: `academic-paper/agents/draft_writer_agent.md`、`peer_reviewer_agent.md`、`references/writing_quality_check.md`、`academic_writing_style.md`。

## ハンドオフ（概要）

- **deep-research → academic-paper**: RQ ブリーフ、方法ブループリント、アノテ付き書誌、統合レポート等（`shared/handoff_schemas.md`、各 `SUBSKILL.md` の Handoff 節）。
- **academic-paper → academic-paper-reviewer**: 完成原稿。
- **査読後 → academic-paper**: 編集決定・リビジョン・ロードマップ。

## 参照パス

- 共有: `shared/handoff_schemas.md`, `shared/style_calibration_protocol.md`
- 日本語概要（人間向け）: `概要.md`
- インストール要点: `README.md`

**バンドル版メモ**: v3.14.0 系（deep-research 2.11.0 / academic-paper **3.2.0** / academic-pipeline 3.14.0 / reviewer 1.10.0、上流 2026-07 時点）。**academic_writing_advice_ja**（2026-05-17）を含む。長いパイプラインはユーザ確認のチェックポイントで分割すること。
