# Personal Voice Creator（あなたの文体スキル作成ツール）

> インストールして使える Claude スキルです。**あなた自身**の文体スキルを作り、Claude が書く記事・手紙・投稿を、本当にあなたが書いたように仕上げます。

**言語：** [English](README.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md)

---

## できること

AI が書く文章は、どうしても「ありがち」な感じになります。**Personal Voice Creator** は、短い対話形式のプロセスを通じて、あなたの文体を再利用できるスキルに変えます。

1. **インタビュー** — Claude があなたの書き方について、いくつか質問します
2. **サンプル** — あなたが書いたものを提供します（リンク・貼り付け・ファイル）
3. **テストと調整** — Claude が下書きを書き、あなたが「自分らしい」と思えるまで直します
4. **パッケージ化** — ずっと使える `personal-voice.skill` ファイルが手に入ります

肝心なのは 3 番目です。「いや、自分ならこう言う」という修正がすべて記録されます。あなたの本当の声は、「自分はこう書くと思っている」のと「実際にこう書いている」の差のなかにあるからです。

## クイックスタート

### 1. 作成ツールのスキルをインストール

[`dist/personal-voice-creator.skill`](dist/personal-voice-creator.skill) をダウンロードし、Claude の **設定 → Skills** からアップロードします。

### 2. 起動する

新しいチャットを開き、こう伝えます：

> 私の文体スキルを作りたい。

Claude がインタビューを始め、文章サンプルを求め、テスト下書きを書き、あなたのフィードバックをもとに調整します。

### 3. あなた専用のスキルを受け取る

プロセスの最後に、Claude があなた専用の `personal-voice.skill` を生成します。同じ方法でインストールし（**設定 → Skills**）、いつでもこう呼び出せます：

> これを私の文体で書いて。

## 必要なもの

- Skills が有効になっている Claude アカウント
- 実際に書いた文章サンプル（本物であるほど良い）
- インタビューと調整のための 15〜20 分

## リポジトリ構成

```
.
├── README.md / README.zh-TW.md / README.ja.md   ドキュメント（英語が正式版）
├── BUILD_LOG.md           このプロジェクトの制作記録（物語＋学び）
├── DESIGN.md              1ページの設計思想
├── CLAUDE.md              Claude Code 用のプロジェクトメモリ
├── skill/
│   └── personal-voice-creator/    スキルのソース（ここを編集）
├── dist/
│   └── personal-voice-creator.skill   ビルド済みファイル（これをダウンロード）
└── examples/              サンプルの流れ
```

## ソースからのビルド

スキルを編集した場合は、`.skill` ファイルを再ビルドします：

```bash
pip install pyyaml
python skill/personal-voice-creator/scripts/package_skill.py skill/personal-voice-creator dist
```

パッケージ化の前に構成を検証するため、壊れたスキルはビルドされません。

## コントリビュート

Issue や Pull Request を歓迎します。すべての PR で、スキルが正しくパッケージ化できるか自動チェックが走ります。プロジェクトの規約は `CLAUDE.md` を参照してください。

## ライセンス

MIT — [LICENSE](LICENSE) を参照。
