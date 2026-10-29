#!/usr/bin/env python3
"""kintone アプリ「卒論テーマ・候補論文」から書き出したCSVを、references/theme_catalog.md に変換する。

使い方（先生用）:
  1. kintone のアプリ一覧で「…」→「ファイルに書き出す」。全フィールドを選び、文字コードは UTF-8 で書き出す。
  2. python scripts/catalog_from_kintone.py 書き出したファイル.csv --out references/theme_catalog.md
  3. スキルを ZIP にし直して配布する。

「スキルに載せる」が「はい」のレコードだけを載せる。
"""
import argparse
import csv
import re
import sys
from collections import OrderedDict

MAJORS = ["現代社会", "メディア社会", "スポーツ社会", "子ども社会", "人間福祉"]
ROLE_ORDER = {"候補": 0, "予備": 1, "背景": 2}

HEAD = """# テーマ・カタログ（先生が用意したテーマと候補論文）

このファイルは、ゼミの kintone アプリ「卒論テーマ・候補論文」から自動で作っている。
**直接書き換えず、kintone 側を直してから作り直す**（`scripts/catalog_from_kintone.py`）。

## 使い方（AI 向け）

- Phase 1 で「先生が用意したテーマから選ぶ」を選んだ学生に、まず**専攻**を聞き、その専攻のテーマを
  「テーマ名」と「テーマの説明」だけで示して選ばせる（論文リストはまだ見せない）。
  他専攻のテーマを選びたいと言われたら、それも認める。
- テーマが決まったら「従属変数」を確認し、Phase 1 の関門（従属変数と、選んだ理由2文）に進む。
- Phase 2 では、「候補」の論文を示し、学生に各論文の PDF を J-STAGE などから自分で入手させる
  （リンクは示してよい）。3本そろえば検索の Phase は短縮してよいが、**方法の章のために、
  学生自身にも同じ従属変数で1回は検索させ、検索記録を残させる**（候補論文がそのテーマの代表例だと
  確かめる作業になる）。
- 「予備」は、候補の1本が入手できない・合わないときの入れ替え用、または比較の材料。
  「背景」は比較の3本には入れず、序論で使う。
- 表の「本文で確認」は、ページ上で確認できなかった項目。Phase 3 で学生が本文から探す。
- 書誌情報は確認日時点のもの。学生が PDF を入手したら、PDF の表記を正とする。
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--out", default="references/theme_catalog.md")
    a = ap.parse_args()

    with open(a.csv, encoding="utf-8-sig", newline="") as f:
        # kintone の書き出しは項目名（ラベル）が見出しになる。
        # 「テーマの説明（学生に見せる）」のような括弧書きを外して、フィールドコードと同じ名前にそろえる。
        raw = list(csv.DictReader(f))
        rows = [{re.sub(r"[（(].*?[）)]$", "", k.strip()): (v or "") for k, v in r.items() if k}
                for r in raw]
        rows = [r for r in rows if r.get("スキルに載せる", "はい").strip() in ("はい", "")]
    if not rows:
        sys.exit("載せるレコードがありません。")

    themes = OrderedDict()
    for r in sorted(rows, key=lambda r: (r["テーマID"], ROLE_ORDER.get(r["論文の役割"], 9), r["発表年"])):
        themes.setdefault(r["テーマID"], []).append(r)

    out = [HEAD]
    checked = max(r.get("確認日", "") for r in rows)
    out.append(f"最終確認日：{checked}\n")
    majors = MAJORS + sorted({r["専攻"] for r in rows} - set(MAJORS))
    for m in majors:
        tids = [tid for tid, rs in themes.items() if rs[0]["専攻"] == m]
        if not tids:
            continue
        out.append(f"\n## {m}専攻\n")
        for tid in tids:
            rs = themes[tid]
            t = rs[0]
            out.append(f"\n### {tid}　{t['テーマ名']}\n")
            out.append(f"- **従属変数**：{t['従属変数']}")
            out.append(f"- **テーマの説明（学生に見せる）**：{t['テーマの説明']}")
            out.append(f"- **比較の見どころ（AI が問いかけに使う。先に答えを言わない）**：{t['比較の見どころ']}\n")
            out.append("| 役割 | 著者（年） | タイトル | 掲載誌 巻号: ページ | 方法 | 対象者（n） | 従属変数の測り方 | 主な結果 | リンク |")
            out.append("|---|---|---|---|---|---|---|---|---|")
            for r in rs:
                link = r["URL"] or (f"https://doi.org/{r['DOI']}" if r["DOI"] else "")
                note = f"（注：{r['注意点']}）" if r.get("注意点") else ""
                cells = [r["論文の役割"], f"{r['著者']}（{r['発表年']}）", r["論文タイトル"],
                         f"{r['掲載誌']} {r['巻号']}: {r['ページ']}", r["研究方法"],
                         f"{r['対象者']}（{r['対象者数']}）", r["従属変数の測り方"],
                         r["主な結果"] + note, link]
                out.append("| " + " | ".join(c.replace("|", "／").replace("\n", " ") for c in cells) + " |")
    with open(a.out, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"{a.out}: テーマ {len(themes)} 件、論文 {len(rows)} 本")


if __name__ == "__main__":
    main()
