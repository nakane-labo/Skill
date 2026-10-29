#!/usr/bin/env python3
"""少数研究の効果量統合（卒論の発展層用）。

入力CSVの type は r / smd / or のいずれかに統一する（混在不可）。
  r   : study,type,r,n
  smd : study,type,m1,sd1,n1,m2,sd2,n2   （Hedges の g）
  or  : study,type,or,ci_low,ci_high     （95%信頼区間から対数オッズ比のSEを逆算）

出力：各研究の効果量と95%CI、固定効果、ランダム効果（DerSimonian-Laird）、
Hartung-Knapp 補正の95%CI（研究数が少ないときはこちらを主に報告する）、Q・τ²・I²、
フォレストプロット（--out）。

使い方: python pool_effects.py input.csv --out forest.png
"""
import argparse
import csv
import math
import sys

T975 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447,
        7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228}


def t_quantile(df):
    try:
        from scipy.stats import t
        return float(t.ppf(0.975, df))
    except Exception:
        return T975.get(df, 1.96 + 2.4 / df)


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = [r for r in csv.DictReader(
            line for line in f if line.strip() and not line.lstrip().startswith("#"))]
    if len(rows) < 2:
        sys.exit("研究が2本以上必要です。")
    types = {r["type"].strip().lower() for r in rows}
    if len(types) != 1:
        sys.exit(f"type が混在しています: {types}。1種類にそろえてください。")
    return rows, types.pop()


def effect(row, kind):
    """(効果量, 分散) を解析用スケールで返す。"""
    if kind == "r":
        r, n = float(row["r"]), int(row["n"])
        if not -1 < r < 1 or n <= 3:
            sys.exit(f"{row['study']}: r は -1〜1、n は4以上にしてください。")
        return math.atanh(r), 1.0 / (n - 3)
    if kind == "smd":
        m1, sd1, n1 = float(row["m1"]), float(row["sd1"]), int(row["n1"])
        m2, sd2, n2 = float(row["m2"]), float(row["sd2"]), int(row["n2"])
        sp = math.sqrt(((n1 - 1) * sd1 ** 2 + (n2 - 1) * sd2 ** 2) / (n1 + n2 - 2))
        d = (m1 - m2) / sp
        j = 1 - 3 / (4 * (n1 + n2) - 9)
        g = j * d
        v = (n1 + n2) / (n1 * n2) + g ** 2 / (2 * (n1 + n2))
        return g, v
    if kind == "or":
        o, lo, hi = float(row["or"]), float(row["ci_low"]), float(row["ci_high"])
        se = (math.log(hi) - math.log(lo)) / (2 * 1.959964)
        return math.log(o), se ** 2
    sys.exit(f"未対応の type: {kind}")


def back(x, kind):
    if kind == "r":
        return math.tanh(x)
    if kind == "or":
        return math.exp(x)
    return x


def pool(es, vs):
    k = len(es)
    w = [1 / v for v in vs]
    fe = sum(wi * e for wi, e in zip(w, es)) / sum(w)
    fe_se = math.sqrt(1 / sum(w))
    q = sum(wi * (e - fe) ** 2 for wi, e in zip(w, es))
    df = k - 1
    c = sum(w) - sum(wi ** 2 for wi in w) / sum(w)
    tau2 = max(0.0, (q - df) / c) if c > 0 else 0.0
    i2 = max(0.0, (q - df) / q) * 100 if q > 0 else 0.0
    ws = [1 / (v + tau2) for v in vs]
    re = sum(wi * e for wi, e in zip(ws, es)) / sum(ws)
    re_se = math.sqrt(1 / sum(ws))
    # Hartung-Knapp
    hk_var = sum(wi * (e - re) ** 2 for wi, e in zip(ws, es)) / (df * sum(ws))
    hk_se = max(math.sqrt(hk_var), 1e-12)
    tq = t_quantile(df)
    return dict(k=k, fe=fe, fe_se=fe_se, re=re, re_se=re_se, q=q, df=df,
                tau2=tau2, i2=i2, hk_lo=re - tq * hk_se, hk_hi=re + tq * hk_se,
                weights=[wi / sum(ws) * 100 for wi in ws])


def japanese_font():
    try:
        from matplotlib import font_manager
        for name in ["Noto Sans CJK JP", "Noto Sans JP", "IPAexGothic", "IPAGothic",
                     "Hiragino Sans", "Yu Gothic", "Meiryo", "TakaoGothic"]:
            if any(f.name == name for f in font_manager.fontManager.ttflist):
                return name
    except Exception:
        pass
    return None


def forest(path, names, es, vs, res, kind):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    font = japanese_font()
    if font:
        plt.rcParams["font.family"] = font
    label = {"r": "相関係数 r", "smd": "Hedges の g", "or": "オッズ比"}[kind]
    if not font:
        label = {"r": "r", "smd": "Hedges g", "or": "Odds ratio"}[kind]
    k = len(es)
    fig, ax = plt.subplots(figsize=(7, 1.0 + 0.55 * (k + 2)))
    ys = list(range(k + 1, 1, -1))
    for y, e, v, w in zip(ys, es, vs, res["weights"]):
        lo, hi = e - 1.96 * math.sqrt(v), e + 1.96 * math.sqrt(v)
        ax.plot([back(lo, kind), back(hi, kind)], [y, y], color="#333")
        ax.plot(back(e, kind), y, "s", color="#2b6cb0", markersize=4 + w / 8)
    c, lo, hi = res["re"], res["hk_lo"], res["hk_hi"]
    ax.fill([back(lo, kind), back(c, kind), back(hi, kind), back(c, kind)],
            [0.5, 0.75, 0.5, 0.25], color="#c05621")
    ax.axvline(1 if kind == "or" else 0, color="#999", linestyle="--", linewidth=1)
    if kind == "or":
        ax.set_xscale("log")
    ax.set_yticks(ys + [0.5])
    pooled = "統合（ランダム効果・HK）" if font else "Pooled (RE, HK)"
    ax.set_yticklabels(names + [pooled])
    ax.set_xlabel(label)
    ax.set_ylim(0, k + 2)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    return font


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--out", help="フォレストプロットのPNG")
    a = ap.parse_args()
    rows, kind = load(a.csv)
    names = [r["study"] for r in rows]
    es, vs = zip(*(effect(r, kind) for r in rows))
    res = pool(list(es), list(vs))
    unit = {"r": "r", "smd": "g", "or": "OR"}[kind]
    print(f"効果量の種類: {unit}（研究数 k = {res['k']}）\n")
    print("研究ごと（95%CI, ランダム効果の重み）")
    for n, e, v, w in zip(names, es, vs, res["weights"]):
        s = math.sqrt(v)
        print(f"  {n}: {back(e, kind):.3f} [{back(e - 1.96 * s, kind):.3f}, "
              f"{back(e + 1.96 * s, kind):.3f}]  重み {w:.1f}%")
    fe, fs, re, rs = res["fe"], res["fe_se"], res["re"], res["re_se"]
    print(f"\n固定効果: {back(fe, kind):.3f} [{back(fe - 1.96 * fs, kind):.3f}, {back(fe + 1.96 * fs, kind):.3f}]")
    print(f"ランダム効果（DL）: {back(re, kind):.3f} [{back(re - 1.96 * rs, kind):.3f}, {back(re + 1.96 * rs, kind):.3f}]")
    print(f"ランダム効果（Hartung-Knapp 補正CI）: {back(re, kind):.3f} "
          f"[{back(res['hk_lo'], kind):.3f}, {back(res['hk_hi'], kind):.3f}]  ← 主に報告する")
    print(f"異質性: Q = {res['q']:.2f} (df = {res['df']}), τ² = {res['tau2']:.4f}, I² = {res['i2']:.1f}%")
    if res["k"] < 5:
        print("\n注意: 研究数が少ないため、τ² と I² の推定は不安定です。統合結果は参考値として扱い、"
              "限界として明記してください。出版バイアスの検討はできません。")
    if a.out:
        font = forest(a.out, names, list(es), list(vs), res, kind)
        print(f"\nフォレストプロット: {a.out}" + ("" if font else "（日本語フォントが見つからず英語表記）"))


if __name__ == "__main__":
    main()
