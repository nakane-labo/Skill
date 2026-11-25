# 本家との関係（UPSTREAM）

`academic-research-skills-nakanelabo/` は、本家のスキルを中根ラボ向けに改変したものです。この文書は、どこから何を取り込み、どこを変えたかの記録です。取り込みのたびに更新します。

このファイルはスキルの外（`docs/`）に置いています。スキルのファイル数（上限200）に数えないためです。

## 本家

| 項目 | 内容 |
|---|---|
| リポジトリ | https://github.com/Imbad0202/academic-research-skills |
| 著者 | Cheng-I Wu |
| ライセンス | CC BY-NC 4.0（表示・非営利）。ライセンス全文は `academic-research-skills-nakanelabo/LICENSE` |
| ラボ版の基準 | v3.14.0（タグ commit 8157a15、2026-07-02） |
| 本家の最新 | v3.24.4（2026-11-19、調査日 2026-11-26） |

## 取り込みの履歴

| 日付 | 本家の版 | 本家の commit | 取り込んだもの |
|---|---|---|---|
| 2026-11-26 | v3.24.4 の27コミット先 | 3eb9f07（作業ツリーのファイルを直接読んだ） | **一部取り込み**。取り込んだもの: 引用の実在確認の手順書 `shared/references/citation_existence_gate.md`（新設。三値規則に、DOI の登録機関の確認と日本語文献の照会先 CiNii / J-STAGE / NDL サーチをラボ独自に追加）、`firm_rules.md` などの参照切れ修正、レビューの小改善（参考文献の創作禁止、`<paper_content>` で原稿をデータ扱い、Top Blocking Issues 節、カード確認待ちと Coverage 節、未確認の掲載誌を勧めない、原稿の日付時点での文献網羅判定）、作者向けレターの日本語版テンプレート `templates/author_letter_template_ja.md`（簡略版）、re-review の「ものさし継続」と改訂原稿・Response to Reviewers のデータ扱い。見送ったもの: 倫理審査向け revision-coach 変種、sr-screener、3ゲート契約と Stage 4→3' の引き渡し変更、すべてのスクリプト |
| 2026-11-26 | v3.14.0 | 8157a15 | academic-paper-reviewer の5本を補充（commit 6e29272）。`references/changelog.md`、`references/guided_mode_protocol.md`、`references/integration_guide.md`、`references/re_review_mode_protocol.md`、`templates/peer_review_report_template.md`。先頭に出典コメントを足してある |
| 2026-11 より前 | v3.14.0 | 8157a15 | 全体を v3.14.0 系に更新（academic-paper 3.2.0 など）。個別の日付と commit は記録が残っていない |
| それ以前 | v3.6.x 系 | 3e953ce（v3.6.5）ほか | 最初の取り込み。個別の記録なし |

補足:

- 補充した5本のうち4本は v3.14.0 と本文が同じです。違いは先頭の出典コメント2行だけです。`re_review_mode_protocol.md` には v3.14.0 の「Commitment Ledger Verification (v3.11)」節を含みます。
- バンドル版のバージョン表記（`SKILL.md` のメモ）は、deep-research 2.11.0、academic-paper 3.2.0、academic-pipeline 3.14.0、academic-paper-reviewer 1.10.0 です。
- 旧リポジトリ `nakane-labo/academic-research-skills-nakanelabo` は 2026-11-26 にアーカイブ済みです。正本はこのリポジトリです。

## v3.24 系の扱い

本家 v3.24 系は、2026-11-26 に**一部だけ取り込む**と決めて取り込みました（上の履歴の表を参照）。版番号は v3.14.0 系のままです。ラボ版の独自採番（academic-paper 3.2.0 など）も変えていません。

取り込まない理由は次のとおりです。

- 本家はプラグイン形式になり、`scripts/`（473ファイル）や `shared/contracts/` が大きく増えた。スキル1本200ファイルの上限に収まらない。
- 追加機能の多くは codex など外部 CLI や Python スクリプトが前提で、Claude だけの環境では動かない。
- 倫理審査向け revision-coach 変種は、使う見込みが立っていないため見送った。sr-screener は、価値の大半がスクリプトと並列エージェントにあり、ラボの用途にも近くないため見送った（必要になれば別スキルとして別ZIPで入れる）。
- re-review の3ゲート契約は、スクリプトの検査が前提のため入れていない。

取り込んだ文には、出典（本家の版や issue 番号）と、ラボ独自の簡略化である旨を残してあります。

## 本家から削ったファイル

スキル1本あたり200ファイルの上限に合わせて、次を含めていません（本家だけにあるファイルは約40本）。

- `scripts/`、`docs/`（開発用スクリプト、設計ドキュメント、テスト）
- `examples/` の一部、サンプル PDF
- `references/` と schemas の多く（例: anti_leakage_protocol、disclosure_mode_protocol、plan_mode_protocol、workflow_phase_details、socratic_mode_protocol、systematic_review_protocol、crossref / openalex / arxiv の API protocol、passport schema 9本）

方針は、「文章の中身（SKILL、agents、授業・研究で使う references）を優先し、開発用の仕組みは削る」です。削ったファイルを必要に応じて戻すときは、200上限を確かめてからにします。

## ラボ改変の一覧

比較の基準は本家 v3.14.0 です。

### A. 構造・追加

| # | 改変 | 場所 |
|---|---|---|
| 1 | ルートの `SKILL.md` を新規作成（「共通の考え方（中根ラボ運用）」節、ルーティング、バンドル版メモ）。サブフォルダの `SKILL.md` は `SUBSKILL.md` に改名（4本） | `SKILL.md`、各サブフォルダ |
| 2 | 日本語の段落・流れの指針を追加（本家に無い） | `academic-paper/references/academic_writing_advice_ja.md` |
| 3 | 日本社会学会『社会学評論』スタイルガイドを追加（本家に無い） | `deep-research/references/jss_shakai_gakkyo_style_guide.md` |
| 4 | Claude デスクトップ向けの `概要.md`、`README.md` を新規作成。`LICENSE` は本家のものを同梱 | スキルフォルダ直下 |
| 5 | 200ファイル上限のため、本家の一部ファイルを除外 | 前節を参照 |

### B. 本家との内容差分があるファイル（43本）

| 区分 | ファイル | 主な改変 |
|---|---|---|
| 大 | 各サブフォルダの `SUBSKILL.md`（deep-research、academic-paper、academic-pipeline、academic-paper-reviewer） | description に日本語トリガーを追加。Cursor 用の表記。reviewer に「日本語ガイド（運用概要）」節。ルーティング注記（intent_clarification_protocol への参照） |
| 大 | `deep-research/agents/bibliography_agent.md` | 参考文献の形式を APA 7 から社会学評論（JSS）形式へ |
| 大 | `academic-pipeline/examples/mid_entry_example.md`、`integrity_failure_recovery.md` | 日本語化・簡約の可能性（差分が大きい。要確認） |
| 中 | `academic-paper/agents/literature_strategist_agent.md`、`deep-research/agents/report_compiler_agent.md` | JSS 形式への対応 |
| 中 | `academic-paper/agents/draft_writer_agent.md` | `academic_writing_advice_ja` への参照を追加 |
| 中 | `academic-pipeline/agents/pipeline_orchestrator_agent.md`、`integrity_verification_agent.md` | ラボ運用への調整 |
| 中 | `deep-research/agents/{research_architect,synthesis,monitoring}_agent.md`、`shared/ground_truth_isolation_pattern.md`、`academic-paper/references/academic_writing_style.md` | 表記・参照の調整 |
| 小 | 約25本（2〜4行） | 見出しや参照の差し替え |
| 出典 | 補充した5本（academic-paper-reviewer） | 先頭に出典コメント（CC BY-NC 4.0、補充日）を追加 |

個別の差分は、本家の v3.14.0 を clone して `diff -r` で出せます（SKILL.md と SUBSKILL.md の名前の違いに注意）。手順は MAINTENANCE.md を参照してください。
