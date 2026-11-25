<!-- 出典: 本家 https://github.com/Imbad0202/academic-research-skills v3.24.4 の引用実在ゲート（v3.11 #182 以降）の三値規則と API の引き方を、スクリプト抜きの手順書に書き直したもの。CC BY-NC 4.0。中根ラボ版で新設（2026-11-26）。「ラボ独自」と書いた節は本家に無い -->

# Citation Existence Gate（引用の実在確認の手順書）

参考文献の1件ごとに「その文献は実在するか」を、外部の書誌 API で確かめ、`true` / `false` / `unresolvable` のどれかを付ける手順。スクリプトは使わない。Web 取得ツール（WebFetch など）で下の URL を取り、結果を読んで判定する。

この手順書が作る判定は、次の2か所が読む。
- `academic-paper/agents/formatter_agent.md` の rule 11/12（`lookup_verified`、`terminal_policies.citation_existence`）
- `academic-pipeline/agents/pipeline_orchestrator_agent.md` の Final-Output Pre-Check

つまり、これまでは「判定の出し方」の文章だけがあり、判定を作る手順がなかった。この手順書がその手順にあたる。

## 1. 三値の規則（本家ゲートの規則。英語の用語はそのまま使う）

各照会先の結果を、まず次の4つのどれかにする。

| 結果 | 意味 |
|---|---|
| `matched` | 照会先で同じ文献が見つかった |
| `unmatched` | 照会先に届き、見つからなかった |
| `unreachable` | 照会先に届かなかった（通信失敗、制限、タイムアウト、取得ツールが使えない） |
| `skipped` | その照会先は使わない（対象外、登録機関が違うなど） |

次に、全照会先の結果を1つの `lookup_verified` にまとめる。

1. `skipped` は判定から除く。
2. `matched` が1つでもあれば `true`。
3. `matched` が無く、**DOI か arXiv ID を指定した照会**が `unmatched` なら `false`。
4. それ以外はすべて `unresolvable`。（全部 `unreachable`、タイトルだけの照会が `unmatched`、全部 `skipped`、など）

守ること。
- `false` にしてよいのは、DOI か arXiv ID を指定して照会し、見つからなかった場合だけ。タイトルや著者名で検索して見つからなかっただけでは、`false` にしない（`unresolvable`）。
- 本家のゲートの限界: DOI も arXiv ID も無い文献は、偽造でも `unresolvable` になり、ブロックされない。日本語文献でも同じ。`unresolvable` は「確認できなかった」であって「実在しない」ではない。報告では `false` と分けて書く。
- Web 取得が使えない環境（claude.ai の一部など）では、すべて `unreachable` とし、`unresolvable` にする。推測で `true` にも `false` にもしない。

### タイトルの照合

- タイトルは「大文字小文字と句読点を畳んだうえで完全一致」で同じとみなす。`Attention Is All You Need` と `Attention Is Not All You Need` は、字面が近くても別の文献。
- DOI で引いて見つかった文献のタイトルが、引用側のタイトルと明らかに違う（類似度の目安 0.70 未満）ときは `DOI_MISMATCH`（DOI を取り違えている疑い）として SERIOUS に上げる。integrity_verification_agent の A0 と同じ扱い。
- 日本語タイトルでは、全角と半角、括弧（「」『』）、スペースの有無を畳んでから比べる。

## 2. 照会先の引き方

URL はすべて GET。キーは要らない。

### Crossref（DOI の照会）

- `https://api.crossref.org/works/<DOI>`
- 見つかれば `message.title[0]` がタイトル、`message.author`、`message.issued` が刊行年。404 なら Crossref に無い（ただし後述の登録機関に注意）。

### OpenAlex（DOI、タイトル）

- DOI: `https://api.openalex.org/works/doi:<DOI>`
- タイトル: `https://api.openalex.org/works?search=<タイトル>`（結果の `display_name` を上の規則で比べる）
- 404 なら OpenAlex に無い。

### arXiv（arXiv ID、タイトル）

- ID: `https://export.arxiv.org/api/query?id_list=<arXiv ID>`
- タイトル: `https://export.arxiv.org/api/query?search_query=ti:"<タイトル>"`
- 3秒に1回までにする。結果が 0 件なら `unmatched`。

### Semantic Scholar

- 既存の `deep-research/references/semantic_scholar_api_protocol.md` に従う（`S2_VERIFIED` / `S2_NOT_FOUND` / `DOI_MISMATCH` / `API_UNAVAILABLE`）。この手順書の用語に直すと、`S2_VERIFIED` は `matched`、`S2_NOT_FOUND` は `unmatched`、`API_UNAVAILABLE` は `unreachable`。

## 3. ラボ独自の規則（本家に無い。日本語文献のために足した）

この節は中根ラボ版の独自追記。社会学評論形式の参考文献には日本語文献が多く、本家の規則をそのまま当てると、実在する日本語文献が `false` になる危険があるため。

### 3-1. DOI は先に登録機関を確かめる

DOI は、登録機関（RA）が Crossref とは限らない。J-STAGE や国立国会図書館などの DOI は JaLC の登録で、Crossref の API からは見えないことが多い。

1. DOI があれば、先に `https://doi.org/doiRA/<DOI>` を引く。返ってくる `RA` が登録機関。
2. `RA` が `Crossref` なら、上の Crossref と OpenAlex の照会をそのまま使う。
3. `RA` が `Crossref` 以外（`JaLC` など）なら、Crossref と OpenAlex の照会結果で `false` にしない。この2つの結果は `skipped` として扱い、次の 3-2 の照会先で確かめる。
4. `doiRA` の照会そのものに失敗したときは、登録機関が分からないので、Crossref の `unmatched` を `false` の根拠にしない（`unresolvable`）。

### 3-2. 日本語文献の照会先

日本語文献は、次の照会先も使う。どれかで同じ文献が見つかれば `matched`（`true`）。

| 照会先 | 引き方 |
|---|---|
| CiNii Research | `https://cir.nii.ac.jp/` の検索（論文・図書・雑誌）。タイトル、著者、刊行年で探す |
| J-STAGE | `https://www.jstage.jst.go.jp/` の検索。DOI があれば `https://doi.org/<DOI>` の移動先で確かめる |
| NDL サーチ | `https://ndlsearch.ndl.go.jp/` の検索。図書、雑誌記事、博士論文に強い |

- どの照会先でも確認できなければ `unresolvable` とし、`false` にしない。日本語文献は、DOI が JaLC のものを除けば、DOI も arXiv ID も無いことが多い。タイトル検索で見つからないことは `false` の根拠にならない。
- 日本語文献で `false` にしてよいのは、登録機関が Crossref と確かめられた DOI を指定して Crossref で 404 になった場合に限る。
- これらの検索ページは Web 取得で結果を読めないことがある。読めなければ `unreachable` と書く。

## 4. 使い方（既存の照合に足す）

- `academic-pipeline/agents/integrity_verification_agent.md` の Phase A には、すでに WebSearch による全件照合（A1）と、Semantic Scholar の一括照合（A0）がある。この手順書は、それを置き換えない。A0 と A1 に**足す形**で使い、Crossref / OpenAlex / arXiv（と、日本語文献なら 3-2 の照会先）の結果と三値の判定を、監査記録（audit trail）に並べて残す。
- A1 の `NOT_FOUND` と、この手順書の `false` は同じではない。`false` は ID を指定した照会で見つからなかったときだけ。A1 で3回検索しても見つからず、ID での照会もできないものは、`unresolvable` に `NOT_FOUND` の所見を添えて報告する。
- 査読者が薦めた文献（`domain_reviewer` などの推薦）も、決定のあとにこの手順で実在を確かめてよい。

## 5. 報告の形

文献ごとに、1行で次を書く。

```
[引用の短い識別] | 登録機関: Crossref/JaLC/なし | 照会: Crossref=matched, OpenAlex=skipped, CiNii=unmatched | lookup_verified: true/false/unresolvable | 所見
```
