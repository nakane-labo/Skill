# 保守手順（MAINTENANCE）

`academic-research-skills-nakanelabo/` を保守するための手順です。本家との関係と改変の一覧は UPSTREAM.md にあります。

## 前提

- 正本は、このリポジトリ（nakane-labo/Skill）の `academic-research-skills-nakanelabo/` です。
- 配布先は3つです。GitHub（正本）、claude.ai、Cursor。
- claude.ai 側の `~/.claude/skills/synced/...` は、アップロードした zip が同期されたものです。**直接編集しません。**
- スキル1本あたりのファイル数は200未満にします。
- `SKILL.md` はスキルフォルダのルートに1本だけです。サブフォルダは `SUBSKILL.md` にします。
- UPSTREAM.md と MAINTENANCE.md は `docs/` に置き、スキルのファイル数に数えません。

## 月1回の本家チェック

月の初めに次を確かめます。

```
git ls-remote --tags https://github.com/Imbad0202/academic-research-skills | tail -5
```

- 最新タグが、UPSTREAM.md の「ラボ版の基準」より新しいかを見る。
- 新しければ、本家の CHANGELOG を読み、文章の中身（SKILL、agents、references）が変わったかを見る。スクリプトやテストだけの変更なら、取り込まなくてよい。
- 結果を UPSTREAM.md の「本家の最新」に書く。取り込む・見送るの判断も一言残す。

## 本家の更新を取り込む手順

1. 作業ブランチを切る。

   ```
   git switch -c maint/upstream-sync-YYYY-MM
   ```

2. 本家を clone し、取り込みたい版に固定する。

   ```
   git clone https://github.com/Imbad0202/academic-research-skills "$TMPDIR/upstream"
   cd "$TMPDIR/upstream" && git checkout <タグ または commit>
   ```

3. 前回の基準版との差分を取る。何が変わったかを先に読む。

   ```
   git -C "$TMPDIR/upstream" diff --stat <前回の版> <今回の版>
   ```

4. ラボ版と今回の本家を比べ、ラボ改変（UPSTREAM.md の一覧）を確かめる。本家の `SKILL.md` は、ラボ版では `SUBSKILL.md` なので、読み替えて比べる。
5. 本家で変わったファイルを取り込む。ラボ改変があるファイルは、上書きせず、本家の変更を手で当ててから、ラボ改変を当て直す。
6. 本家のファイルを新しく足すときは、先頭に出典コメント（版、CC BY-NC 4.0、補充日）を付ける。
7. ファイル数が200未満であることを確かめる。

   ```
   find academic-research-skills-nakanelabo -type f | wc -l
   ```

   超えるときは、足すファイルを減らすか、重要度の低いファイルを外す。外したものは UPSTREAM.md の「削ったファイル」に書く。
8. `SKILL.md` のバンドル版メモと、`README.md` の版の記載を更新する。
9. UPSTREAM.md の取り込み履歴に1行足す（日付、本家の版、本家の commit、取り込んだ内容）。
10. commit して push し、PR を出す。レビューを受けてから main に入れる。

## 配布の手順

正本が main に入ってから配布します。配布は、次の順で行います。

### 1. zip を作る

リポジトリのルートで、main を最新にしてから実行します。`.DS_Store` と `.git` は入れません。`-D` は、フォルダだけの項目を zip に入れないための指定です（入れるとファイル数の表示が実際より多くなります）。

```
git switch main && git pull --ff-only
zip -qrD academic-research-skills-nakanelabo.zip academic-research-skills-nakanelabo -x '*.DS_Store' '*/.git/*'
```

作ったら、中身を確かめます。ファイル数が189前後（200未満）で、`SKILL.md` がルートの1本だけであればよいです。

```
unzip -l academic-research-skills-nakanelabo.zip | tail -1
unzip -Z1 academic-research-skills-nakanelabo.zip | grep -E '(^|/)SKILL\.md$'
```

zip の中は `academic-research-skills-nakanelabo/SKILL.md` のように、スキル名のフォルダが入った状態にします。解凍して中身だけを再圧縮しないでください。GitHub の Releases に載せる zip も、同じ方法で作ります（README のダウンロードリンクが指す先）。

### 2. claude.ai にアップロードする

1. Claude デスクトップで **Customize → Skills** を開く。
2. 既存の同名スキルがあれば、置き換える形でアップロードする。
3. 一覧のスイッチがオンのままかを確かめる。
4. 同期先は `~/.claude/skills/synced/<ID>_<ID>/academic-research-skills-nakanelabo/` です。`<ID>` は環境ごとに違うので、手順4の `find` で探します。直接編集しない。アップロードしてから同期されるまで少し待ちます。

### 3. Cursor 側へコピーする

Cursor 側は、git clone ではなく、正本からのコピーで更新します（旧リポジトリ academic-research-skills-nakanelabo はアーカイブ済みです）。`~/.cursor/skills/academic-research-skills-nakanelabo` は、下の `DST` へのシンボリックリンクです。リンクはそのまま残し、`DST` の中身だけを入れ替えます。

```
SRC=<リポジトリ>/academic-research-skills-nakanelabo
DST="/Users/naruhisa/Library/CloudStorage/OneDrive-学校法人立命館/.cursor/skills/academic-research-skills-nakanelabo"

# 書く前の確認: リンクの先が DST と一致すること
[ "$(realpath ~/.cursor/skills/academic-research-skills-nakanelabo)" = "$(realpath "$DST")" ] && echo OK

# 控え（元に戻せるように）
tar -czf <控えの置き場>/cursor_skill_before_YYYY-MM-DD.tar.gz -C "$(dirname "$DST")" academic-research-skills-nakanelabo

rsync -a --delete "$SRC/" "$DST/"
```

- `--delete` は、正本に無いファイルを消します。`.git` も消えます（正本と完全に同じにするため、`--exclude` は付けません）。実行前に、`DST` が上の文字列のとおりかを確かめてください。
- OneDrive 配下への書き込みは、Claude Code のサンドボックスで拒否されることがあります（`unable to escalate mode`、`Operation not permitted`）。そのときは、このコマンドだけサンドボックス外で実行します。途中まで書かれた状態は、再実行で正本どおりになります。

### 4. 3か所の一致を確かめる

```
# 正本と Cursor 側
diff -rq "$SRC" "$DST"

# 正本と zip の展開物
rm -rf "$TMPDIR/unzipped" && mkdir "$TMPDIR/unzipped"
unzip -q academic-research-skills-nakanelabo.zip -d "$TMPDIR/unzipped"
diff -rq "$SRC" "$TMPDIR/unzipped/academic-research-skills-nakanelabo"

# 正本と claude.ai の同期先（場所は find で探す）
SYNCED=$(find ~/.claude/skills/synced -maxdepth 3 -type d -name academic-research-skills-nakanelabo | head -1)
diff -rq --exclude='.DS_Store' "$SRC" "$SYNCED"

# ファイル数
for d in "$SRC" "$DST" "$SYNCED"; do find "$d" -type f ! -name .DS_Store | wc -l; done
```

差分が出なければ、一致しています。claude.ai の同期先は、アップロードして同期されたあとでないと一致しません（それまでは前の版のままです）。出たときは、正本を基準に配り直します。claude.ai 側がずれているときは、zip を作り直してアップロードし直します。

## 困ったとき

- claude.ai がアップロードを受け付けない: ファイル数が200以上、`SKILL.md` が2本以上、zip の階層が違う、のどれかを疑う。
- 本家のライセンスが変わった: 取り込む前に LICENSE を確認する。改変・再配布は、CC BY-NC 4.0 の帰属表示と非営利の条件に従う。
