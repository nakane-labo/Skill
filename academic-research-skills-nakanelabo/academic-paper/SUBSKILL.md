---
name: academic-paper
description: >-
  12-agent academic paper writing pipeline. 10 modes (full/plan/outline/revision/revision-coach/abstract/lit-review/format-convert/citation-check/disclosure). 6 paper types, bilingual abstracts (JA + EN), LaTeX/DOCX-via-Pandoc/PDF/Markdown output. Style Calibration + Writing Quality Check + Japanese paragraph/flow guide (academic_writing_advice_ja) + Anti-Patterns with IRON RULE markers. Cursor bundle default: citation and reference list work should follow the Japan Sociological Society *Shakai Gakkyo Ron* (社会学評論) Style Guide (3rd ed.) when the user requests JSS/Japanese sociology venue norms; otherwise follow the configured citation style from intake. Triggers: write paper, academic paper, paper outline, write abstract, revise paper, check citations, convert to LaTeX, guide my paper, parse reviews, revision roadmap, 論文執筆, 学術論文, 論文構成, 要旨作成, 査読コメント対応, 修訂計画, 段落構成, パラグラフ, 文章の流れ, 序論, 考察, 読みやすい文章. Japanese: 論文執筆、学術論文、抄録、要旨、修訂、引用チェック、LaTeX変換、論文構成、査読コメント対応、修訂計画、IMRaD、文献レビュー論文、社会学評論スタイルガイド、段落・流れの書き方。
metadata:
  version: "3.1.2"
  last_updated: "2026-05-17"
  status: active
  data_access_level: redacted
  task_type: open-ended
  related_skills:
    - deep-research
    - academic-paper-reviewer
    - academic-pipeline
---

# Academic Paper — Academic Paper Writing Agent Team

**Skill version 3.1.2 · 2026-05-17**（Cursor 用スキル）

A general-purpose academic paper writing tool — 12-agent pipeline covering all disciplines, with higher education domain as the default reference.

**v2.5** adds two writing quality features:
- **Style Calibration** (intake Step 10, optional) — Provide 3+ past papers and the pipeline learns your writing voice (sentence rhythm, vocabulary preferences, citation integration style). Applied as a soft guide during drafting; discipline conventions always take priority. See `shared/style_calibration_protocol.md`.
- **Writing Quality Check** (`references/writing_quality_check.md`) — A writing quality checklist applied during the draft self-review step. Catches overused AI-typical terms, em dash overuse, throat-clearing openers, uniform paragraph lengths, and monotonous sentence rhythm. These are good writing rules, not detection evasion.
- **Japanese paragraph & flow guide** (`references/academic_writing_advice_ja.md`) — Topic/support/concluding sentences, intro broad→narrow, discussion narrow→broad, forward-linking sentences, minimal connectives (bundled from アカデミックライティングアドバイス v1).

**Cursor bundle note (JSS):** When the user or intake selects Japanese sociology / 社会学評論 venue norms, treat **[『社会学評論スタイルガイド』第3版](https://jss-sociology.org/bulletin/guide/)** as the citation and reference-list authority (summary: `deep-research/references/jss_shakai_gakkyo_style_guide.md`). Journal articles need **DOI** when assigned; books need **ISBN**.

## 日本語ガイド（運用概要）

**学術論文の執筆**に特化したスキル（12 エージェント）。設定ヒアリングから文献戦略・構成・アーギュメント、章ごとの下書き、引用整合、二言語抄録、模擬査読、LaTeX/DOCX/PDF/Markdown 出力までを扱う。書くときの基本姿勢は、**データで支え、制度的な定義に照らし、現場で読める文章に落とす**こと。本バンドルでは必要に応じて **社会学評論スタイルガイド（第3版）** を引用・参考文献の正本にできる（運用要約: `deep-research/references/jss_shakai_gakkyo_style_guide.md`）。**Style Calibration** と **Writing Quality Check** は `shared/style_calibration_protocol.md` および `references/writing_quality_check.md` を参照（手続きの詳細は英語原文）。

### 日本語の段落・流れ（academic_writing_advice_ja）

原稿の主言語が日本語、またはユーザーが段落・論旨の流れを重視するときは、**必ず** `references/academic_writing_advice_ja.md` を読み、下書き・自己レビュー・模擬査読に反映する（全文・例文は同ファイル）。

| 対象 | ルール（要約） |
|------|----------------|
| 各段落 | トピック・センテンス → サポーティング → コンクルーディング（冗長なら省略） |
| 序論 | 広い話題 → 狭い話題（研究目的・介入まで） |
| 考察 | 狭い話題（結果）→ 広い話題（含意・展望）；限界・結論は末尾が多い |
| 段落間 | 各段落のトピック・センテンスだけ読んで大筋が通ること |
| 文間 | 後文が前文の後半を引き受ける（A→B→C→D） |
| 文の形 | 主語と述語を近づける；一文一義（せめて二義） |
| 接続詞 | 必要最小限（流れがあれば「さらに」「ゆえに」等に頼らない） |

英語の register・hedging は引き続き `references/academic_writing_style.md` を正本とする。AI 典型表現の排除は `references/writing_quality_check.md` と併用する。

### `plan` と `full` の使い分け

- **`plan`**: 完成原稿を一気に欲しいのではなく、**章ごと・段階的に伴走**してほしいとき。初稿が不安、構成が決まらない、初めての論文など。**`full` と迷ったら `plan` 優先**。地味でも順番に積む書き方に向く。
- **`full`**: 設定が揃っており、パイプラインに沿って**一括でドラフト**まで進めたいとき。

意図は言語によらず判定する（英語の "guide my paper" と日本語の「論文の書き方を一緒に考えたい」等が同列）。

### いつ使うか／使わないか

- **使う**: 投稿可能な論文体裁（IMRaD、文献レビュー、理論・ケース・政策ブリーフ、会議論文等）の**執筆・整形・査読コメント対応（revision / revision-coach）**。
- **使わない**: 調査レポートのみ → `deep-research`。国際誌風の**本格的マルチ査読シミュレーション**のみ → `academic-paper-reviewer`。全工程のオーケストレーション → `academic-pipeline`。

### 日本語の依頼例

```
高等教育の質保証におけるAIの影響について、学術論文のドラフトを書いてほしい
```

```
初めてなので、IMRaD で一章ずつ構成から相談しながら進めたい
```

```
査読コメントを貼るので、リビジョンロードマップを整理してほしい
```

### オーケストレーション（8 フェーズの要約）

0. **CONFIG**: 論文タイプ、分野、引用様式、出力形式、言語、字数など（`intake_agent`）。
1. **RESEARCH**: 探索戦略、書誌、マトリクス（`literature_strategist_agent`）。`literature_corpus[]` 利用時は `academic-pipeline/references/literature_corpus_consumers.md` に従う。
2. **ARCHITECTURE**: アウトラインと証拠マップ（`structure_architect_agent`）。
3. **ARGUMENTATION**: 主張–証拠の連鎖（`argument_builder_agent`）。
4. **DRAFTING**: 章ごと下書き（`draft_writer_agent`）。必要に応じ図表（`visualization_agent`）。
5. **CITATIONS + ABSTRACT**: 引用監査と二言語抄録（**日本語＋英語**）（`citation_compliance_agent` / `abstract_bilingual_agent`）。
6. **PEER REVIEW**: 5 次元スコアの模擬査読（`peer_reviewer_agent`）。
7. **OUTPUT**: 形式変換・カバーレター等（`formatter_agent`）。

**Plan モード**では `socratic_mentor_agent` が章ごとのガイドを担当（英語本文の Plan Step を参照）。

### エージェント一覧（日本語一行）

| エージェント ID | 役割（要約） |
|-----------------|-------------|
| `intake_agent` | 設定ヒアリング、ハンドオフ検知、Plan 時の簡易ヒアリング |
| `literature_strategist_agent` | 探索設計、スクリーニング、書誌、マトリクス |
| `structure_architect_agent` | 構成パターン選択、詳細アウトライン、字数配分 |
| `argument_builder_agent` | 主張・反論・論理展開、Plan 時のストレステスト |
| `draft_writer_agent` | セクション別フルドラフト、レジスター調整 |
| `citation_compliance_agent` | 本文–参考文献の整合、様式、DOI 等 |
| `abstract_bilingual_agent` | 日本語＋英語の抄録・キーワード |
| `peer_reviewer_agent` | 模擬ダブルブラインド査読（最大 2 ラウンド） |
| `formatter_agent` | LaTeX/DOCX/PDF/Markdown、引用形式の相互変換 |
| `socratic_mentor_agent` | Plan モードのソクラテス型メンター |
| `visualization_agent` | 図表用コードと LaTeX 連携 |
| `revision_coach_agent` | 査読コメントの構造化・ロードマップ化（単独利用可） |

### 参照（詳細は英語原文）

- 各エージェント: `academic-paper/agents/*.md`
- 構成パターン・可視化・品質: `academic-paper/references/*.md`（日本語段落・流れ: `academic_writing_advice_ja.md`）
- Style Calibration: `../shared/style_calibration_protocol.md`
- ハンドオフ: `../shared/handoff_schemas.md`

---

## Quick Start

**Minimal command:**
```
Write a paper on the impact of AI on higher education quality assurance
```

```
Write a paper on the impact of declining birth rates on private university management strategies
```

**Execution flow:**
1. Configuration interview — paper type, discipline, citation format, output format
2. Literature search — systematic search strategy, source screening
3. Architecture design — paper structure, outline, word count allocation
4. Argumentation construction — claim-evidence chains, logical flow
5. Full-text drafting — section-by-section draft, register adjustment
6. Citation compliance + bilingual abstract (parallel)
7. Peer review — five-dimension scoring, revision suggestions
8. Output formatting — LaTeX/DOCX (via Pandoc)/PDF/Markdown

---

## Trigger Conditions

### Trigger Keywords

**English**: write paper, academic paper, paper outline, write abstract, revise paper, literature review paper, check citations, convert to LaTeX, convert format, format paper, conference paper, journal article, thesis chapter, research paper, guide my paper, help me plan my paper, step by step paper, draft manuscript, write methodology, write discussion, parse reviews, revision roadmap, help me with my revision, I got reviewer comments, convert citations

### Plan Mode Activation

Activate `plan` mode when the user wants guidance, step-by-step planning, or expresses uncertainty about paper structure. **Default rule**: when ambiguous between `plan` and `full`, prefer `plan`.

> See `references/plan_mode_protocol.md` for full intent signals and activation rules.

### Does NOT Trigger

| Scenario | Use Instead |
|----------|-------------|
| Deep research / fact-checking (not paper writing) | `deep-research` |
| Reviewing a paper (structured review) | `academic-paper-reviewer` |
| Full research-to-paper pipeline | `academic-pipeline` |

### Distinction from `deep-research`

| Feature | `academic-paper` | `deep-research` |
|---------|-------------------|-----------------|
| Primary output | Publishable paper draft | Research report |
| Structure | Journal-ready (IMRaD, etc.) | APA 7.0 report |
| Citation | Multi-format (APA/Chicago/MLA/IEEE/Vancouver) | APA 7.0 only |
| Abstract | Bilingual (JA + EN) | Single language |
| Peer review | Simulated 5-dimension review | Editorial review |
| Output format | LaTeX/DOCX (via Pandoc)/PDF/Markdown | Markdown only |
| Revision loop | Max 2 rounds with targeted feedback | Max 2 rounds |

---

## Agent Team (12 Agents)

| # | Agent | Role | Phase |
|---|-------|------|-------|
| 1 | `intake_agent` | Configuration interview: paper type, discipline, journal, citation format, output format, language, word count; Handoff detection; Plan mode simplified interview | Phase 0 |
| 2 | `literature_strategist_agent` | Search strategy design, source screening, annotated bibliography, literature matrix | Phase 1 |
| 3 | `structure_architect_agent` | Paper structure selection, detailed outline, word count allocation, evidence mapping | Phase 2 |
| 4 | `argument_builder_agent` | Argument construction, claim-evidence chains, logical flow, counter-argument handling; Plan mode argument stress test | Phase 3 / Plan Step 3 |
| 5 | `draft_writer_agent` | Section-by-section full draft writing, discipline register adjustment, word count tracking | Phase 4 |
| 6 | `citation_compliance_agent` | Citation format verification, reference list completeness, DOI checking | Phase 5a |
| 7 | `abstract_bilingual_agent` | Bilingual abstract (JA + EN), 5-7 keywords each | Phase 5b |
| 8 | `peer_reviewer_agent` | Simulated double-blind review, five-dimension scoring, revision suggestions (max 2 rounds) | Phase 6 |
| 9 | `formatter_agent` | Convert to LaTeX/DOCX (via Pandoc)/PDF/Markdown, journal formatting, cover letter, citation format conversion (APA 7 / Chicago / MLA / IEEE / Vancouver) | Phase 7 |
| 10 | `socratic_mentor_agent` | Plan mode Socratic mentor: chapter-by-chapter guidance, convergence criteria (4 signals), question taxonomy (4 types), INSIGHT extraction | Plan Step 0-3 |
| 11 | `visualization_agent` | Parse paper data and generate publication-quality figure code (Python matplotlib / R ggplot2) with APA 7.0 formatting, colorblind-safe palettes, and LaTeX integration | Phase 4 / Phase 7 |
| 12 | `revision_coach_agent` | Parse unstructured reviewer comments into structured Revision Roadmap; classify, map, and prioritize comments; works standalone without prior pipeline execution | Revision-Coach mode |

---

## Output Formats

### Text Formats
LaTeX (.tex + .bib), DOCX (via Pandoc), PDF (via LaTeX or Pandoc), Markdown.

### Figures
When the paper contains quantitative results, the `visualization_agent` can generate publication-ready figures in Python (matplotlib/seaborn) or R (ggplot2) with APA 7.0 formatting and colorblind-safe palettes. Figures are delivered as runnable code + LaTeX `\includegraphics` integration code. See `references/statistical_visualization_standards.md` for chart type decision trees and code templates.

### Citation Formats
APA 7.0 (default), Chicago (Author-Date or Notes-Bibliography), MLA 9, IEEE, Vancouver. The `formatter_agent` supports late-stage citation format conversion between any two supported formats via "Convert citations to [format]".

---

## Orchestration Workflow (8 Phases)

```
Phase 0: CONFIG        -> [intake_agent]              -> Paper Configuration Record
Phase 1: RESEARCH      -> [literature_strategist]      -> Search Strategy + Source Corpus
Phase 2: ARCHITECTURE  -> [structure_architect]        -> Paper Outline + Evidence Map
Phase 3: ARGUMENTATION -> [argument_builder]           -> Argument Blueprint
Phase 4: DRAFTING      -> [draft_writer]               -> Complete Draft
Phase 5a: CITATIONS    -> [citation_compliance] ──┐    -> Citation Audit Report
Phase 5b: ABSTRACT     -> [abstract_bilingual]   ─┘    -> Bilingual Abstract + Keywords  (parallel)
Phase 6: PEER REVIEW   -> [peer_reviewer]              -> Review Report (max 2 revision loops)
Phase 7: FORMAT        -> [formatter]                  -> Final Output Package
```

> See `references/workflow_phase_details.md` for detailed per-phase agent behavior and output descriptions.

### Checkpoint Rules

1. ⚠️ **IRON RULE**: User must confirm Paper Configuration Record before proceeding to Phase 1
2. **Phase 2 -> 3**: User must approve outline (can request restructuring)
3. ⚠️ **IRON RULE**: Max 2 revision loops; unresolved items -> "Acknowledged Limitations"
4. **Peer Review** Critical-severity issues block progression to Phase 7
5. User can skip Phase 1 (literature) if providing own sources

---

> **v3.4.0 compliance (applies to `full` mode):** Before finalization, `compliance_agent` runs RAISE principles-only check (warn-only; primary research is outside PRISMA-trAIce scope). Warnings are listed in the disclosure statement but never block the pipeline. See `shared/raise_framework.md §Scope disclaimer`.

## Operational Modes (10 Modes)

See `references/mode_selection_guide.md` for details.

| Mode | Trigger | Agents | Output |
|------|---------|--------|--------|
| `full` | "Write a paper" | All 9 (+ 11 if quantitative) | Complete paper draft (with figures if applicable) |
| `outline-only` | "Paper outline" | 1->2->3 | Detailed outline + evidence map |
| `revision` | "Revise paper" | 8->5->6 | Revised draft with tracked changes (uses `templates/revision_tracking_template.md`) |
| `abstract-only` | "Write abstract" | 1->7 | Bilingual abstract + keywords |
| `lit-review` | "Literature review" | 1->2 | Annotated bibliography + synthesis |
| `format-convert` | "Convert to LaTeX" / "Convert citations to [format]" | 9 only | Formatted document; includes citation format conversion (APA 7 / Chicago / MLA / IEEE / Vancouver) |
| `citation-check` | "Check citations" | 6 only | Citation error report |
| `plan` | "guide my paper" / "help me plan my paper" | 1->10->3->4 | Chapter Plan + INSIGHT Collection |
| `revision-coach` | "parse reviews" / "revision roadmap" / "I got reviewer comments" | 12 only | Revision Roadmap + optional Tracking Template + Response Letter Skeleton |
| **`disclosure`** (v3.2) | **"AI disclosure for Nature" / "generate AI usage statement"** | **9 only** | **Venue-specific AI-usage disclosure paragraph(s) + placement instructions** |

### Quick Mode Selection Guide

| Your Situation | Recommended Mode | Spectrum |
|----------------|-----------------|----------|
| Starting from scratch with a clear RQ | `full` | balanced |
| Need help planning before writing | `plan` | originality |
| Just need an outline | `outline-only` | balanced |
| Have a draft, received review feedback | `revision` | fidelity |
| Have unstructured reviewer comments | `revision-coach` | balanced |
| Just need an abstract | `abstract-only` | fidelity |
| Need to check/fix citations | `citation-check` | fidelity |
| Need to convert format (LaTeX, DOCX) or citation style | `format-convert` | fidelity |
| Want a systematic literature review paper | `lit-review` | fidelity |
| Need a venue-specific AI-usage disclosure statement for submission | `disclosure` | fidelity |

**Spectrum** (v3.2): *fidelity* = template-heavy, predictable output; *balanced* = default; *originality* = exploratory, template-light. See `shared/mode_spectrum.md` for the full cross-skill spectrum table.

Not sure? Start with `plan` — it will guide you step by step. `disclosure` is a finishing step — run it after the paper is drafted, targeting the venue you plan to submit to.

### Mode Selection Logic

> See `references/mode_selection_guide.md` for trigger-to-mode mappings and the full selection flowchart.

---

## Plan Mode: Chapter-by-Chapter Guided Planning

Socratic mode that guides users through paper planning one chapter at a time. Builds a complete Paper Blueprint through structured dialogue.

> See `references/plan_mode_protocol.md` for the full chapter-by-chapter dialogue flow and Paper Blueprint structure.

---

## Handoff Protocol: deep-research -> academic-paper

`intake_agent` automatically detects deep-research materials (RQ Brief / Bibliography / Synthesis / INSIGHT Collection) and skips redundant steps. See `deep-research/SUBSKILL.md` Handoff Protocol for the complete handoff material format.

---

## Failure Paths

See `references/failure_paths.md` for details. Quick reference:

| Failure Scenario | Handling Strategy |
|---------|---------|
| Insufficient research foundation | Recommend running `deep-research` first |
| Wrong paper structure selected | Return to Phase 2, suggest alternative structure |
| Word count significantly over/under target | Identify problematic chapters, suggest trimming/expansion |
| Citation format entirely wrong | Re-run the entire citation phase |
| Peer review rejection | Analyze rejection reasons, suggest major revision or restructuring |
| Plan mode not converging | Suggest switching to outline-only mode |
| Incomplete handoff materials | List missing items, suggest supplementing or re-running |
| User abandons midway | Save completed Chapter Plan |

---

## Full Academic Pipeline

See `academic-pipeline/SUBSKILL.md` for the complete workflow.

---

## Phase 0: Configuration Interview

See `agents/intake_agent.md` for the complete field definitions of the Phase 0 configuration interview. The interview covers 9 items: paper type, discipline, target journal, citation format, output format, language, abstract, word count, and existing materials. Outputs a Paper Configuration Record, awaiting user confirmation.

---

## File Structure

**Agent definitions**: `agents/{agent_name}.md` — one file per agent (12 total, matching Agent Team table above).

**References** (20 files in `references/`):
- Citation: `apa7_extended_guide`, `citation_format_switcher`
- Writing: `academic_writing_style`, `academic_writing_advice_ja`, `writing_quality_check`, `writing_judgment_framework`
- Structure: `paper_structure_patterns` (6 types), `abstract_writing_guide`
- Domain: `hei_domain_glossary` (bilingual), `journal_submission_guide`, `latex_template_reference`
- Process: `failure_paths` (12 scenarios), `mode_selection_guide` (10 modes), `plan_mode_protocol`, `workflow_phase_details`
- Ethics: `credit_authorship_guide` (CRediT 14 roles), `funding_statement_guide`, `statistical_visualization_standards`
- Disclosure (v3.2): `disclosure_mode_protocol` (venue-specific AI-usage statement generation), `venue_disclosure_policies` (v1 database: ICLR, NeurIPS, Nature, Science, ACL, EMNLP)
- Also: `deep-research/references/apa7_style_guide.md` (base reference, extended here)

**Templates** (11 files in `templates/`): `imrad`, `literature_review`, `case_study`, `theoretical_paper`, `policy_brief`, `conference_paper`, `latex_article_template.tex`, `bilingual_abstract`, `credit_statement`, `funding_statement`, `revision_tracking` (4 status types).

**Examples** (4 files in `examples/`): `imrad_hei_example`, `literature_review_example`, `plan_mode_guided_writing`, `revision_mode_example`.

---

## Anti-Patterns

Explicit prohibitions to prevent common failure modes:

| # | Anti-Pattern | Why It Fails | Correct Behavior |
|---|-------------|-------------|-----------------|
| 1 | **AI-typical overused terms** | "delve into", "crucial", "it is important to note" = instant AI detection | Use discipline-specific vocabulary; see `references/writing_quality_check.md` |
| 2 | **Em dash abuse** | More than 2 em dashes per page signals AI writing | Use parentheses, commas, or restructure the sentence |
| 3 | **Throat-clearing openers** | "In this section, we will discuss..." adds no information | Start with the claim or finding directly |
| 4 | **Uniform paragraph lengths** | Every paragraph is 4-5 sentences = monotonous AI rhythm | Vary paragraph length naturally (2-8 sentences) |
| 5 | **⚠️ IRON RULE: Fabricated citations** | Inventing plausible-sounding references that don't exist | Every citation must be verified via DOI or WebSearch; see `academic-pipeline/agents/integrity_verification_agent.md` |
| 6 | **Sycophantic revision** | Accepting all reviewer feedback without critical evaluation | Use REVIEWER_DISAGREE status when reviewer is wrong; justify with evidence |
| 7 | **Scope creep during revision** | Adding unrequested sections/analyses to "improve" the paper | Revision addresses reviewer concerns only; new content requires explicit user approval |
| 8 | **Ignoring failure paths** | Continuing despite desk-reject signals or fatal methodology flaws | Check `references/failure_paths.md`; invoke F11 Desk-Reject Recovery when triggered |

---

## Quality Standards

### Writing Quality
1. **Every claim must have a citation** or be supported by the paper's own data
2. **Zero citation orphans** — in-text citations <-> reference list must perfectly match
3. **Consistent register** — academic tone appropriate for the discipline
4. **Logical flow** — clear transitions between paragraphs and sections
5. **Word count compliance** — within +/-10% of target

### Bilingual Abstract Quality
6. **Independent writing** — JA and EN abstracts are independently composed, NOT mechanical translations
7. **Structural alignment** — both abstracts cover the same key points in the same order
8. **Keywords** — 5-7 per language, reflecting the paper's core concepts
9. **Word count** — EN: 150-300 words; JA: 300-500 characters

### Citation Quality
10. **Format compliance** — 100% adherence to selected citation style
11. ⚠️ IRON RULE: **DOI inclusion** — every source with a DOI must include it; every citation must be verified via DOI or WebSearch
12. **Currency** — flag sources older than 10 years (unless seminal works)
13. **Self-citation ratio** — flag if >15%

### Peer Review
14. **Five dimensions** — Originality (20%), Methodological Rigor (25%), Evidence Sufficiency (25%), Argument Coherence (15%), Writing Quality (15%)
15. **Actionable feedback** — every criticism must include a specific suggestion
16. **Max 2 revision rounds** — unresolved items become Acknowledged Limitations

### Mandatory Inclusions
⚠️ **IRON RULE**: Every paper MUST include: Data Availability Statement, Ethics Declaration, Author Contributions (CRediT), Conflict of Interest Statement, Funding Acknowledgment.
17. **AI disclosure statement** — every paper must include a statement on AI tool usage
18. **Limitations section** — explicitly discuss study limitations
19. **Ethics statement** — when applicable (human subjects, sensitive data)

---

## Output Language

Follows the user's language. Academic terminology is kept in English. Bilingual abstracts are always provided regardless of the main text language.

---

## Integration with Other Skills

```
academic-paper + tw-hei-intelligence  -> Evidence-based HEI paper with real MOE data
academic-paper + deep-research        -> Deep research phase -> paper writing phase (auto-handoff)
academic-paper + report-to-website    -> Interactive web version of the paper
academic-paper + notebooklm-slides-generator -> Presentation slides from paper
academic-paper + academic-paper-reviewer -> Peer review -> revision loop
```

---

## Version Info

| Item | Content |
|------|---------|
| Skill Version | 3.1.2 |
| Last Updated | 2026-04-27 |
| Maintainer | Cheng-I Wu |
| Dependent Skills | deep-research v1.0+ (upstream), academic-paper-reviewer v1.0+ (downstream) |

---

## Version History

> See `references/changelog.md` for full version history.
