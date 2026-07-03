---
name: deep-research
description: >-
  Universal deep research agent team. 13-agent pipeline for rigorous academic research on any topic. 8 modes: full research, quick brief, paper review, lit-review, fact-check, three-way literature scan, Socratic guided research dialogue, and systematic review with optional meta-analysis. Covers research question formulation, Socratic mentoring, methodology design, systematic literature search, source verification, cross-source synthesis, risk of bias assessment, meta-analysis, report compilation with Japan Sociological Society *Shakai Gakkyo Ron* (社会学評論) Style Guide references (DOI for journal articles, ISBN for books), editorial review, devil's advocate challenges, ethics review, and post-research literature monitoring. Triggers on: research, deep research, literature review, systematic review, meta-analysis, PRISMA, evidence synthesis, fact-check, WHY HOW WHAT papers, 3W literature scan, guide my research, help me think through, 研究, 研究計画, 研究方向, 研究主題. Japanese: 学術調査、文献レビュー、システマティックレビュー、社会学評論スタイルガイド、DOI、ISBN、研究計画、研究課題の整理、ファクトチェック、メタアナリシス、3W文献スキャン、研究の手引き、先行研究調査、研究倫理。
metadata:
  version: "2.11.0"
  last_updated: "2026-06-18"
  status: active
  data_access_level: raw
  task_type: open-ended
  related_skills:
    - academic-paper
    - academic-pipeline
---

# Deep Research — Universal Academic Research Agent Team

**Skill version 2.11.0 · 2026-07-03**（Cursor 用スキル）

Universal deep research tool — a domain-agnostic 13-agent team for rigorous academic research on any topic.

**v2.5** — Bibliography and reference-list format follows the **[『社会学評論スタイルガイド』第3版](https://jss-sociology.org/bulletin/guide/)** (Japan Sociological Society). **Journal articles must include DOI when assigned; books must include ISBN.** Authors, year, title, and journal/publication metadata must be complete per the guide. See `references/jss_shakai_gakkyo_style_guide.md`.

**v2.4** (retained) writing quality for the report compiler:
- **Style Profile consumption** (optional) — If a Style Profile is available from academic-paper intake, the report compiler applies it as a soft guide for the Executive Summary and Synthesis sections. Discipline conventions and report objectivity take priority.
- **Writing Quality Check** — The report compiler runs a writing quality checklist before finalizing: flags AI-typical overused terms, checks sentence/paragraph length variation, removes throat-clearing openers. See `academic-paper/references/writing_quality_check.md`.

> **Routing discipline (v3.9.2):** see `shared/references/intent_clarification_protocol.md` for cross-skill routing rules. This skill assumes routing has already settled — ambiguous cross-phase materials should have been clarified upstream.

## 日本語ガイド（運用概要）

分野横断で使える**学術調査**スキル（13 エージェント）。研究問いの明確化から体系的文献探索・検証・統合、レポート草案までを段階的に進める。運用の軸は、**データ（根拠）・制度（定義）・現場（実装可能性）を往復して判断すること**。**文献の表示・文献リストは [『社会学評論スタイルガイド』第3版](https://jss-sociology.org/bulletin/guide/) に準拠**（運用要約: `references/jss_shakai_gakkyo_style_guide.md`）。**論文は DOI、書籍は ISBN を必ず付す**（著者・年・題名・収録雑誌等のメタデータを揃える）。v2.4 系のレポート編集では任意の Style Profile 反映と Writing Quality Check も利用可能（詳細は英語本文および `academic-paper/references/writing_quality_check.md`）。

### モード一覧

| モード | 用途の目安 | スペクトラム |
|--------|------------|------------|
| `socratic` | 研究問いがまだ曖昧で、対話で整理したいとき（`full` と迷ったらこちら優先） | originality |
| `full` | 明確な研究問いに対し、包括的な調査レポートが欲しいとき | balanced |
| `quick` | 短時間の要約・ブリーフが欲しいとき | fidelity |
| `review` | 引用前に既存論文を評価したいとき | balanced |
| `lit-review` | トピックの文献レビューに特化したいとき | fidelity |
| `three-way-scan` | 複数論文を WHY/HOW/WHAT の枠で素早く比較したいとき | fidelity |
| `fact-check` | 特定の主張・事実の検証に特化したいとき | fidelity |
| `systematic-review` | PRISMA 等に沿ったシステマティックレビュー／メタアナリシス | fidelity |

### いつ使うか／使わないか

- **使う**: 調査・エビデンス統合・方法設計・文献の体系的整理が主目的のとき。思いつきを先に書くより、まず根拠を積む運用に向く。
- **使わない**: 投稿用の論文体裁で書きたいだけ → `academic-paper`。国際誌風の多視点査読だけ → `academic-paper-reviewer`。研究から投稿までの段階管理 → `academic-pipeline`。

### ソクラテス（意図検知）の原則

言語に依存せず**意図**を判定する。問いが曖昧で「導いてほしい」「何から手をつけるか分からない」等があれば `socratic`。`socratic` と `full` で迷ったら **`socratic` 優先**。

### 日本語の依頼例

```
高等教育の質保証におけるAIの影響について学術調査してほしい
```

```
研究テーマがまだはっきりしないので、少子化が私立大学経営に与える影響について一緒に整理したい
```

### オーケストレーション（6 フェーズの要約）

1. **Scoping（対話）**: 研究問い（RQ）ブリーフ、方法論ブループリント → Devil's Advocate チェックポイント1 → ユーザー確認後に Phase 2 へ。
2. **Investigation**: 体系的探索、アノテーション付き書誌、ソース検証・格付け。
3. **Analysis**: 統合ナラティブ、ギャップ分析 → チェックポイント2。
4. **Composition**: レポート草案（`report_compiler_agent`）。**文献・参考文献は社会学評論スタイルガイド準拠**。
5. **Review（並列）**: 編集長視点の査読、倫理レビュー → チェックポイント3。
6. **Revision**: フィードバック反映（最大 2 ループ、残件は限界として明示可）。

Devil's Advocate は複数フェーズで必須チェックポイントを担当。重大問題は進行を止めうる。詳細ルールは英語本文「Checkpoint Rules」を参照。

### エージェント一覧（日本語一行）

| エージェント ID | 役割（要約） |
|-----------------|-------------|
| `research_question_agent` | 曖昧なトピックを FINER 等で精密な研究問いにし、範囲を設定 |
| `research_architect_agent` | パラダイム・方法・データ戦略・分析枠組みの方法論ブループリント |
| `bibliography_agent` | 体系的探索、スクリーニング、社会学評論スタイルのアノテーション付き書誌（DOI／ISBN 必須） |
| `source_verification_agent` | ファクトチェック、エビデンス階層、プレデタリー疑い、COI フラグ |
| `synthesis_agent` | ソース横断の統合、矛盾処理、テーマ別統合、ギャップ分析 |
| `report_compiler_agent` | レポート全体の起草・改訂（**文献リストは社会学評論スタイルガイド**） |
| `editor_in_chief_agent` | 編集長視点の査読・判定（Accept / Revise / Reject 等） |
| `devils_advocate_agent` | 前提の挑戦、論理の穴、代替説明、確認バイアス検査 |
| `ethics_review_agent` | 研究倫理・帰属・デュアルユース・公平な表現 |
| `socratic_mentor_agent` | ソクラテス型の多層対話で研究思考を導く |
| `risk_of_bias_agent` | RoB 2 / ROBINS-I 等によるバイアスリスク（システマティックレビュー） |
| `meta_analysis_agent` | メタアナリシスまたはナラティブ統合、効果量・異質性・GRADE |
| `monitoring_agent` | 調査後の文献モニタリング（任意） |

### 参照（詳細は英語原文）

- 各エージェントの手続き: `deep-research/agents/*.md`
- モード詳細: `deep-research/references/mode_selection_guide.md`
- ハンドオフスキーマ: `../shared/handoff_schemas.md`（バンドルルート基準）

---

---

## Quick Start

**Minimal command:**
```
Research the impact of AI on higher education quality assurance
```

**Socratic mode:**
```
Guide my research on the impact of declining birth rates on private universities
```

**Execution:**
1. Scoping — Research question + methodology blueprint
2. Investigation — Systematic literature search + source verification
3. Analysis — Cross-source synthesis + bias check
4. Composition — Full report (references per *社会学評論スタイルガイド*)
5. Review — Editorial + ethics + vulnerability scan
6. Revision — Final polished report

---

## Trigger Conditions

### Trigger Keywords

**English**: research, deep research, literature review, systematic review, meta-analysis, PRISMA, evidence synthesis, fact-check, methodology, WHY HOW WHAT papers, 3W literature scan, JSS style references, sociology style guide, DOI, ISBN, academic analysis, policy analysis, guide my research, help me think through, monitor this topic, set up alerts

**日本語**: 学術調査, 文献レビュー, システマティックレビュー, メタアナリシス, エビデンス統合, ファクトチェック, 3W文献スキャン, 研究方法, アカデミック分析, 政策分析, 研究をガイドする, 考えを整理したい, このトピックを監視, アラートを設定

### Socratic Mode Activation

Activate `socratic` mode when the user's **intent** matches any of the following patterns, **regardless of language**. Detect meaning, not exact keywords.

**Intent signals** (any one is sufficient):
1. User has no clear research question and wants guided thinking
2. User asks to be "led", "guided", or "mentored" through research
3. User expresses uncertainty about what to research or where to start
4. User wants to brainstorm, explore, or clarify a research direction
5. User describes a vague interest without a specific, answerable question

**Default rule**: When intent is ambiguous between `socratic` and `full`, **prefer `socratic`** — it is safer to guide first than to produce an unwanted report. The user can always switch to `full` later.

**Example triggers** (illustrative, not exhaustive):
"guide my research", "help me think through", or equivalent in any language

### Does NOT Trigger

| Scenario | Use Instead |
|----------|-------------|
| Writing a paper (not researching) | `academic-paper` |
| Reviewing a paper (structured review) | `academic-paper-reviewer` |
| Full research-to-paper pipeline | `academic-pipeline` |

### Quick Mode Selection Guide

| Your Situation | Recommended Mode | Spectrum |
|----------------|-----------------|----------|
| Vague idea, need guidance | `socratic` | originality |
| Clear RQ, need comprehensive research | `full` | balanced |
| Need a quick brief (30 min) | `quick` | fidelity |
| Have a paper to evaluate before citing | `review` | balanced |
| Need literature review for a topic | `lit-review` | fidelity |
| Need a fast paper-comparison scan | `three-way-scan` | fidelity |
| Need to verify specific claims | `fact-check` | fidelity |
| Need systematic review / meta-analysis | `systematic-review` | fidelity |

**Spectrum** (v3.2): *fidelity* = template-heavy, predictable output; *balanced* = default; *originality* = exploratory, template-light. See `shared/mode_spectrum.md` for the full cross-skill spectrum table.

Not sure? Start with `socratic` — it will help you figure out what you need.

---

## Agent Team (13 Agents)

| # | Agent | Role | Phase |
|---|-------|------|-------|
| 1 | `research_question_agent` | Transforms vague topics into precise, FINER-scored research questions with scope boundaries | Phase 1, Socratic Layer 1 |
| 2 | `research_architect_agent` | Designs methodology blueprint: paradigm, method, data strategy, analytical framework, validity criteria | Phase 1 |
| 3 | `bibliography_agent` | Systematic literature search, source screening, annotated bibliography per *社会学評論スタイルガイド* (DOI/ISBN) | Phase 2 |
| 4 | `source_verification_agent` | Fact-checking, source grading (evidence hierarchy), predatory journal detection, conflict-of-interest flagging | Phase 2 |
| 5 | `synthesis_agent` | Cross-source integration, contradiction resolution, thematic synthesis, gap analysis | Phase 3 |
| 6 | `report_compiler_agent` | Drafts complete report (Title -> Abstract -> Intro -> Method -> Findings -> Discussion -> References per JSS style guide) | Phase 4, 6 |
| 7 | `editor_in_chief_agent` | Q1 journal editorial review: originality, rigor, evidence sufficiency, verdict (Accept/Revise/Reject) | Phase 5 |
| 8 | `devils_advocate_agent` | Challenges assumptions, tests for logical fallacies, finds alternative explanations, confirmation bias checks | Phase 1, 3, 5, Socratic Layer 2, 4 |
| 9 | `ethics_review_agent` | AI-assisted research ethics, attribution integrity, dual-use screening, fair representation | Phase 5 |
| 10 | `socratic_mentor_agent` | Q1 journal editor persona; guides research thinking through Socratic questioning across 5 layers | Socratic Mode (Layer 1-5) |
| 11 | `risk_of_bias_agent` | Assesses risk of bias using RoB 2 (RCTs) and ROBINS-I (non-randomized); traffic-light visualization | Systematic Review (Phase 2) |
| 12 | `meta_analysis_agent` | Designs and executes meta-analysis or narrative synthesis; effect sizes, heterogeneity, GRADE | Systematic Review (Phase 3) |
| 13 | `monitoring_agent` | Post-research literature monitoring: digests, retraction alerts, contradictory findings detection | Optional (post-pipeline) |

---

## Mode Selection Guide

See `references/mode_selection_guide.md` for the detailed guide.

```
User Input
    |
    +-- Already have a clear research question?
    |   +-- Yes --> Need PRISMA-compliant systematic review / meta-analysis?
    |   |           +-- Yes --> systematic-review mode
    |   |           +-- No --> Need a full report?
    |   |                      +-- Yes --> full mode
    |   |                      +-- No --> Only need literature?
    |   |                                 +-- Yes --> Need rapid paper comparison?
    |   |                                            +-- Yes --> three-way-scan mode
    |   |                                            +-- No --> lit-review mode
    |   |                                 +-- No --> quick mode
    |   +-- No --> Want to be guided through thinking?
    |              +-- Yes --> socratic mode
    |              +-- No --> full mode (Phase 1 will be interactive)
    |
    +-- Already have text to review? --> review mode
    +-- Only need fact-checking? --> fact-check mode
```

---

## Orchestration Workflow (6 Phases)

```
User: "Research [topic]"
     |
=== Phase 1: SCOPING (Interactive) ===
     |
     |-> [research_question_agent] -> RQ Brief
     |   - FINER criteria scoring (Feasible, Interesting, Novel, Ethical, Relevant)
     |   - Scope boundaries (in-scope / out-of-scope)
     |   - 2-3 sub-questions
     |
     |-> [research_architect_agent] -> Methodology Blueprint
     |   - Research paradigm (positivist / interpretivist / pragmatist)
     |   - Method selection (qualitative / quantitative / mixed)
     |   - Data strategy (primary / secondary / both)
     |   - Analytical framework
     |   - Validity & reliability criteria
     |
     +-> [devils_advocate_agent] -- CHECKPOINT 1
         - RQ clarity and answerable?
         - Method appropriate for question?
         - Scope too broad or too narrow?
         - Verdict: PASS / REVISE (with specific feedback)
     |
     ** User confirmation before Phase 2 **
     |
=== Phase 2: INVESTIGATION ===
     |
     |-> [bibliography_agent] -> Source Corpus + Annotated Bibliography
     |   - Systematic search strategy (databases, keywords, Boolean)
     |   - Inclusion/exclusion criteria
     |   - PRISMA-style flow (if applicable)
     |   - Annotated bibliography (*社会学評論スタイルガイド*; DOI/ISBN)
     |
     +-> [source_verification_agent] -> Verified & Graded Sources
         - Evidence hierarchy grading (Level I-VII)
         - Predatory journal screening
         - Conflict-of-interest flagging
         - Currency assessment (publication date relevance)
         - Source quality matrix
     |
=== Phase 3: ANALYSIS ===
     |
     |-> [synthesis_agent] -> Synthesis Narrative + Gap Analysis
     |   - Thematic synthesis across sources
     |   - Contradiction identification & resolution
     |   - Evidence convergence/divergence mapping
     |   - Knowledge gap analysis
     |   - Theoretical framework integration
     |
     +-> [devils_advocate_agent] -- CHECKPOINT 2
         - Cherry-picking check
         - Confirmation bias detection
         - Logic chain validation
         - Alternative explanations explored?
         - Verdict: PASS / REVISE
     |
=== Phase 4: COMPOSITION ===
     |
     +-> [report_compiler_agent] -> Full draft (JSS references)
         - Title Page
         - Abstract (150-250 words)
         - Introduction (context, problem, purpose, RQ)
         - Literature Review / Theoretical Framework
         - Methodology
         - Findings / Results
         - Discussion (interpretation, implications, limitations)
         - Conclusion & Recommendations
         - References (*社会学評論スタイルガイド* 第3版)
         - Appendices (if applicable)
     |
=== Phase 5: REVIEW (Parallel) ===
     |
     |-> [editor_in_chief_agent] -> Editorial Verdict + Line Feedback
     |   - Originality assessment
     |   - Methodological rigor
     |   - Evidence sufficiency
     |   - Argument coherence
     |   - Writing quality (clarity, conciseness, flow)
     |   - Verdict: ACCEPT / MINOR REVISION / MAJOR REVISION / REJECT
     |
     |-> [ethics_review_agent] -> Ethics Clearance
     |   - AI disclosure compliance
     |   - Attribution integrity
     |   - Dual-use screening
     |   - Fair representation check
     |   - Verdict: CLEARED / CONDITIONAL / BLOCKED
     |
     +-> [devils_advocate_agent] -- CHECKPOINT 3
         - Final vulnerability scan
         - Strongest counter-argument test
         - "So what?" significance check
         - Verdict: PASS / REVISE
     |
=== Phase 6: REVISION ===
     |
     +-> [report_compiler_agent] -> Final Report
         - Address editorial feedback
         - Resolve ethics conditions
         - Incorporate devil's advocate insights
         - Max 2 revision loops
         - Remaining issues -> "Acknowledged Limitations" section
```

### Checkpoint Rules

1. ⚠️ **IRON RULE**: **Devil's Advocate** has 3 mandatory checkpoints; **Critical-severity** issues block progression
2. Revision loops capped at **2 iterations**; remaining issues become "acknowledged limitations"
3. ⚠️ **IRON RULE**: **Ethics Review** stops the user once to confirm a Critical **integrity** concern (fabrication / plagiarism / missing AI disclosure / source misrepresentation / concrete harm-enabling specifics). Overridable with recorded reasoning — it confirms, it does not veto. Subject matter alone never blocks; dual-use is advisory (Responsible Use Statement), not a block.
4. User confirmation required after Phase 1 before proceeding

---

## Phase-by-phase Invocation Contract (v3.9.2)

ARS pipeline runs in 6 phases. Two invocation modes:

**Mode A — orchestrator-driven (default):** `pipeline_orchestrator_agent` (in `academic-pipeline` skill) runs all phases end-to-end with state tracking via Material Passport.

**Mode B — phase-by-phase (cross-session resume):** User invokes one agent per phase across sessions for long-running projects. Common pattern via `ARS_PASSPORT_RESET=1` + `resume_from_passport=<hash>` (see `academic-pipeline/references/passport_as_reset_boundary.md`).

In Mode B, **single-phase agents (Bucket A per `docs/design/2026-05-18-ars-v3.9.2-agent-phase-classification.md`) stay strictly within their assigned phase for writes**. Reads from upstream phases are allowed. Multi-phase agents (Bucket B: `devils_advocate_agent`, `report_compiler_agent`) do exactly the work specified by the caller's invocation for that phase — no extension to other phases in the same call.

Routing into Mode B requires explicit user signal — `/ars-<mode>` slash command or `[direct-mode]` prefix. Ambiguous cross-phase input defaults to clarification per `.claude/CLAUDE.md` Routing Discipline + `shared/references/intent_clarification_protocol.md`.

**Enforcement (v3.9.2):** prompt-level via Phase Boundary blocks on Bucket A agents + advisory verifier (`scripts/check_pipeline_integrity.py`). Deterministic PreToolUse hook + multi-phase envelope deferred to v3.10 active conductor (#134).

---

## Socratic Mode: Guided Research Dialogue

5-layer dialogue guiding users from vague ideas to concrete research questions. Core principle: ⚠️ **IRON RULE**: Never give direct answers.

**Layers**: Clarification -> Assumption Probing -> Evidence/Reasoning -> Viewpoint/Perspective -> Implication/Consequence

> See `references/socratic_mode_protocol.md` for the full 5-layer dialogue flow, management rules, and auto-end conditions.

### Opt-in Reading Probe (v3.5.1)

Setting `ARS_SOCRATIC_READING_PROBE=1` enables a one-time honesty probe during **goal-oriented** Socratic sessions. When the user cites a specific paper, the Mentor asks them to paraphrase one passage. Decline is logged without penalty. Default OFF. See `agents/socratic_mentor_agent.md` §"Optional Reading Probe Layer".

---

## Systematic Review Mode

PRISMA 2020-compliant systematic review with optional meta-analysis. Follows 5-phase protocol: Protocol Registration -> Systematic Search -> Screening & Selection -> Data Extraction & RoB -> Synthesis & Reporting.

> **v3.4.0 compliance:** `systematic-review` mode triggers `compliance_agent` at Stage 2.5 (Methods items) and Stage 4.5 (remaining items + RAISE 8-role matrix). PRISMA-trAIce Mandatory failures block the pipeline. See `shared/compliance_checkpoint_protocol.md`.

> See `references/systematic_review_protocol.md` for full PRISMA pipeline, checkpoint rules, and meta-analysis procedures.

---

## Operational Modes

| Mode | Agents Active | Output | Word Count |
|------|---------------|--------|------------|
| `full` (default) | All 9 core (excluding socratic_mentor, RoB, meta-analysis) | Full report (JSS style references) | 3,000-8,000 |
| `quick` | RQ + Biblio + Verification + Report | Research brief | 500-1,500 |
| `review` | Editor + Devil's Advocate + Ethics | Reviewer report on provided text | N/A |
| `lit-review` | Biblio + Verification + Synthesis | Annotated bibliography + synthesis | 1,500-4,000 |
| `three-way-scan` | Biblio + Verification (retrieval + WHY/HOW/WHAT extract) | Paper shortlist compared by WHY/HOW/WHAT + cross-paper synthesis | 800-2,000 |
| `fact-check` | Source Verification only | Verification report | 300-800 |
| `socratic` | Socratic Mentor + RQ + Devil's Advocate | Research Plan Summary (INSIGHT collection) | N/A (iterative) |
| `systematic-review` | RQ + Architect + Biblio + Verification + RoB + Meta-Analysis + Synthesis + Report + Editor + Ethics + DA | Full PRISMA 2020 report + forest plot data + GRADE table | 5,000-15,000 |

---

## Three-Way Scan Mode (WHY / HOW / WHAT)

Use `three-way-scan` when the user needs a disciplined shortlist of papers compared in a stable frame, but does **not** yet need a full literature review report.

- **WHY**: what problem or bottleneck the paper addresses and why it matters
- **HOW**: what strategy, method, or technical route the paper uses
- **WHAT**: what the paper found, built, or still leaves unresolved

This mode is intentionally lighter than `lit-review`. It prioritizes:

1. candidate retrieval
2. deduplication
3. compact per-paper extraction
4. cross-paper synthesis of shared WHY, divergent HOW, and remaining gaps

Recommended per-paper output:

```markdown
## <paper title>
Source: <provider> | Year: <year> | Link: <url>

- WHY: ...
- HOW: ...
- WHAT: ...
```

Then add:

- common `WHY`
- divergent `HOW`
- strongest `WHAT`
- unresolved global gap

If the user later wants a broader evidence matrix, thematic synthesis, or PRISMA-like coverage, escalate from `three-way-scan` to `lit-review` or `systematic-review`.

---

## Failure Paths

See `references/failure_paths.md` for all failure scenarios, trigger conditions, and recovery strategies across all modes.

Key failure path summary:

| Failure Scenario | Trigger Condition | Recovery Strategy |
|---------|---------|---------|
| RQ cannot converge | Phase 1 / Layer 1 exceeds multiple rounds while still vague | Provide 3 candidate RQs or suggest lit-review |
| Insufficient literature | bibliography_agent finds < 5 sources | Expand search strategy, alternative keywords |
| Methodology mismatch | RQ type misaligned with method capability | Return to Phase 1, suggest 3 alternative methods |
| Devil's Advocate CRITICAL | Fatal logical flaw discovered | STOP, explain the issue, require correction |
| Ethics BLOCKED | Critical integrity issue (not subject matter) | Stop the user once to confirm; list issues + remediation path; overridable with recorded reasoning |
| Socratic non-convergence | > 10 rounds without convergence | Suggest switching to full mode |
| User abandons mid-process | Explicitly states they don't want to continue | Save progress, provide re-entry path |
| Only non-English literature | English search returns empty | Switch to databases in the target language |

---

## Literature Monitoring (Optional Post-Pipeline)

Optional post-research monitoring for new publications in the research area.

> See `references/literature_monitoring_strategies.md` for setup instructions across academic databases.

---

## Handoff Protocol: deep-research → academic-paper

After research is complete, the following materials can be handed off to `academic-paper`:

1. **Research Question Brief** (from research_question_agent)
2. **Methodology Blueprint** (from research_architect_agent)
3. **Annotated Bibliography** (from bibliography_agent)
4. **Synthesis Report** (from synthesis_agent)
5. **[If socratic mode] INSIGHT Collection and Research Plan Summary**

**Trigger**: User says "now help me write a paper" or "write a paper based on this"

`academic-paper`'s `intake_agent` will automatically detect available materials and skip redundant steps:
- Has RQ Brief -> skip topic scoping
- Has Bibliography -> skip literature search
- Has Synthesis -> accelerate findings / discussion writing

See `examples/handoff_to_paper.md` for a detailed handoff example.

---

## Full Academic Pipeline

See `academic-pipeline/SUBSKILL.md` for the complete workflow.

---

## Agent File References

| Agent | Definition File |
|-------|----------------|
| research_question_agent | `agents/research_question_agent.md` |
| research_architect_agent | `agents/research_architect_agent.md` |
| bibliography_agent | `agents/bibliography_agent.md` |
| source_verification_agent | `agents/source_verification_agent.md` |
| synthesis_agent | `agents/synthesis_agent.md` |
| report_compiler_agent | `agents/report_compiler_agent.md` |
| editor_in_chief_agent | `agents/editor_in_chief_agent.md` |
| devils_advocate_agent | `agents/devils_advocate_agent.md` |
| ethics_review_agent | `agents/ethics_review_agent.md` |
| socratic_mentor_agent | `agents/socratic_mentor_agent.md` |
| risk_of_bias_agent | `agents/risk_of_bias_agent.md` |
| meta_analysis_agent | `agents/meta_analysis_agent.md` |
| monitoring_agent | `agents/monitoring_agent.md` |

---

## Reference Files

| Reference | Purpose | Used By |
|-----------|---------|---------|
| `references/jss_shakai_gakkyo_style_guide.md` | 社会学評論スタイルガイド第3版 運用要約（DOI/ISBN 必須） | report_compiler, bibliography, editor_in_chief |
| `references/apa7_style_guide.md` | APA 7th edition quick reference (supplementary) | report_compiler, editor_in_chief |
| `references/source_quality_hierarchy.md` | Evidence pyramid + grading rubric | source_verification, bibliography |
| `references/methodology_patterns.md` | Research design templates | research_architect |
| `references/logical_fallacies.md` | 30+ fallacies catalog | devils_advocate |
| `references/ethics_checklist.md` | AI disclosure, attribution, dual-use | ethics_review |
| `references/interdisciplinary_bridges.md` | Cross-discipline connection patterns | synthesis, research_architect |
| `references/socratic_questioning_framework.md` | 6 types of Socratic questions + 30+ prompt patterns | socratic_mentor |
| `references/failure_paths.md` | 12 failure scenarios with triggers and recovery paths | all agents |
| `references/mode_selection_guide.md` | Mode selection flowchart and comparison table | orchestrator |
| `references/irb_decision_tree.md` | IRB decision tree + HE quick reference | ethics_review, research_architect |
| `references/equator_reporting_guidelines.md` | EQUATOR reporting guideline mapping | research_architect, report_compiler |
| `references/preregistration_guide.md` | Preregistration decision tree + platforms + checklist | research_architect |
| `references/systematic_review_toolkit.md` | Cochrane v6.4, PRISMA 2020, RoB 2, ROBINS-I, I² guide, GRADE, protocol registration | risk_of_bias, meta_analysis, bibliography, report_compiler |
| `references/literature_monitoring_strategies.md` | Google Scholar alerts, PubMed alerts, RSS feeds, Retraction Watch, citation tracking, monitoring cadence | monitoring_agent |
| `references/argumentation_reasoning_framework.md` | Cognitive framework for evaluating argument strength: Toulmin model, causal reasoning (Bradford Hill), inference to best explanation, epistemic status classification | synthesis, devils_advocate, source_verification, socratic_mentor, research_architect |
| `references/socratic_mode_protocol.md` | Full 5-layer Socratic dialogue flow, management rules, auto-end conditions | socratic_mentor, research_question |
| `references/systematic_review_protocol.md` | Full PRISMA pipeline, checkpoint rules, meta-analysis procedures | risk_of_bias, meta_analysis, bibliography, report_compiler |
| `references/cross_agent_quality_definitions.md` | Peer-reviewed source tiers, currency standards, severity definitions | all agents |
| `references/changelog.md` | Full version history | — |

---

## Templates

| Template | Purpose |
|----------|---------|
| `templates/research_brief_template.md` | Quick mode output format |
| `templates/literature_matrix_template.md` | Source x Theme analysis matrix |
| `templates/evidence_assessment_template.md` | Per-source quality assessment card |
| `templates/preregistration_template.md` | OSF standard 21-item preregistration template |
| `templates/prisma_protocol_template.md` | PRISMA-P 2015 systematic review protocol template |
| `templates/prisma_report_template.md` | PRISMA 2020 systematic review report template (27 items) |

---

## Examples

| Example | Demonstrates |
|---------|-------------|
| `examples/exploratory_research.md` | Full 6-phase pipeline walkthrough |
| `examples/systematic_review.md` | PRISMA-style literature review |
| `examples/policy_analysis.md` | Applied comparative policy research |
| `examples/socratic_guided_research.md` | Complete Socratic mode multi-turn dialogue (12 rounds) |
| `examples/handoff_to_paper.md` | deep-research full mode handoff to academic-paper |
| `examples/review_mode.md` | Review mode: 3-agent review pipeline for policy recommendation text |
| `examples/fact_check_mode.md` | Fact-check mode: source verification of HEI claims with per-claim verdicts |
| `examples/idea_diversity_coverage_gap_advisory.md` | #257 Socratic wording-pattern + lit-review distributional-skew advisories |

---

## Output Language

Follows the user's language. Academic terminology kept in English. Socratic mode uses natural conversational style.

---

## Anti-Patterns

Explicit prohibitions to prevent common failure modes:

| # | Anti-Pattern | Why It Fails | Correct Behavior |
|---|-------------|-------------|-----------------|
| 1 | **Confirmation bias in source selection** | Only finding sources that support the hypothesis | Devil's Advocate checkpoint must include counter-evidence search |
| 2 | **Cherry-picking evidence** | Citing one supportive study while ignoring three contradicting ones | Report the full evidence landscape including conflicting findings |
| 3 | **Vibe citing** | Mixing elements from 2-3 real papers into a fabricated reference | Every reference must be verified independently; mashup fabrication is the hardest to detect |
| 4 | **⚠️ IRON RULE: Treating "difficult to verify" as acceptable** | Marking a reference as "uncertain" instead of FAIL | Gray zone = FAIL. If you cannot confirm it exists, it does not go in the report |
| 5 | **Skipping phases** | Jumping to synthesis before completing source verification | Complete each phase fully; Phase N output is Phase N+1 input |
| 6 | **Shallow Socratic mode** | Giving answers disguised as questions ("Wouldn't you say X is true?") | Ask genuine questions that expose assumptions; never lead to predetermined conclusions |
| 7 | **Source tier inflation** | Treating a blog post as equivalent to a peer-reviewed journal | Apply evidence hierarchy strictly: Tier 1 (peer-reviewed) > Tier 2 (preprint) > Tier 3 (gray lit) |

## Quality Standards

1. ⚠️ **IRON RULE**: **Every claim must have a citation** — no unsupported assertions
2. **Evidence hierarchy** — meta-analyses > RCTs > cohort studies > case reports > expert opinion (field-neutral baseline; grading is **discipline-relative** — a source meeting its own field's gold standard can reach Grade A even at a low design level. See `references/source_quality_hierarchy.md` §Grading Rubric + §Field-Specific Adjustments)
3. **Contradiction disclosure** — if sources disagree, report both sides with evidence quality comparison
4. **Limitation transparency** — every report must have an explicit limitations section
5. **AI disclosure** — all reports include a statement that AI-assisted research tools were used
6. **Reproducibility** — search strategies, inclusion criteria, and analytical methods must be documented for replication
7. **Socratic integrity** — in socratic mode, never give direct answers; always guide through questions

## Cross-Agent Quality Alignment

Unified definitions across all agents. ⚠️ IRON RULE: **CRITICAL severity** = issue that would invalidate a core conclusion or constitute academic misconduct. Requires immediate resolution.

> See `references/cross_agent_quality_definitions.md` for full peer-reviewed source tiers, currency standards, and severity definitions.

---

## Integration with Other Skills

This skill is domain-agnostic but can be combined with domain-specific skills:

```
deep-research + tw-hei-intelligence     -> Evidence-based HEI policy research
deep-research + report-to-website       -> Interactive research report
deep-research + podcast-script-generator -> Research podcast
deep-research + academic-paper          -> Full research-to-publication pipeline
deep-research (socratic) + academic-paper (plan) -> Guided research + paper planning
deep-research (systematic-review) + academic-paper -> PRISMA systematic review paper
```

---

## Version Info

| Item | Content |
|------|---------|
| Skill Version | 2.11.0 |
| Last Updated | 2026-06-18 |
| Maintainer | Cheng-I Wu |
| Dependent Skills | academic-paper v1.0+ (downstream) |

---

## Version History

> See `references/changelog.md` for full version history.
