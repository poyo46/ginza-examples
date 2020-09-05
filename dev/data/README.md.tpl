# 日本語NLPライブラリGiNZAのすゝめ

## この記事について

本記事は、日本語の自然言語処理ライブラリである {{ginza}} の紹介記事です。
{{ge-qiita}} と {{ge-github}} の二箇所に同じものを公開しています。

<details>
<summary>記事を書いた経緯</summary>
<div>

筆者は {{ginza}} の開発者の方々と何の利害関係もありません。
自然言語処理系の最新技術を検索していてたまたま見つけ、その簡単さに感動したので勝手に宣伝しています。

> 全ての開発は感動から始まる。

コンピュータ産業の父であり筆者の尊敬するエンジニアである池田敏雄さんはこのように言いました。この記事の目的は {{ginza}} の感動を共有することです。
自然言語処理という難解な分野でありますが、なるべく事前知識なしで {{ginza}} を楽しめるようにと願っています。

</div>
</details>

**想定する読者**

* 自然言語処理ってどんなことができるの？という初学者の方
  * 筆者もまだまだ初学者ですが {{ginza}} は簡単にすごいことができるのでぜひ見ていってください。
* Pythonを学びたての方やこれから学ぼうとしている方
  * Python学習のモチベーションになると思います。
* {{mecab}} などの形態素解析器を使ったことはあるが {{ginza}} は初めて聞いたという方
  * 簡単に比較できるものではありませんが新たに {{ginza}} を知る価値はあると思います。

## GiNZAとは

{{ginza-logo}}

{{ginza}} は **日本語の** 自然言語処理ライブラリです。
もともと {{spacy}} という自然言語処理のフレームワークがあり、英語など主要な言語に対応していました。 {{ginza}} は言わば {{spacy}} の日本語対応版です。
詳細については {{ginza-hp}} をご覧ください。

<details>
<summary>GiNZAを選ぶ理由</summary>
<div>

日本語の形態素解析器として有名なものに {{mecab}} があります（形態素解析って何？という方は {{chamame}} にて実行してみてください）。 {{ginza}} も同様に日本語の文を分かち書きすることができます。単に日本語を分かち書きしたいだけなら {{mecab}} の方が圧倒的に速いです。
それでも {{ginza}} には次のメリットがあると思います。

* 簡単に導入できる
  * {{mecab}} はOSに応じた環境構築を行わねばなりません。
  * {{ginza}} の導入はOSに関係なく `$ pip install ginza` でできます。
* {{spacy}} フレームワークを採用している
  * 英語などの言語で {{spacy}} を利用した機械学習の実践例が見つかります。
  * {{ginza}} の登場で同じことが日本語でもできるようになりました。
  * 例えばチャットボットAIのフレームワークで有名な {{rasa}} は {{ginza}} のおかげで日本語でも使えるようになりました。
* [最新の研究](https://github.com/megagonlabs/ginza#training-data-sets) を反映している

なお、決して {{mecab}} をディスっているわけではないことを強調しておきます。状況や目的によって最適な選択は変わります。
{{mecab}} はすでに長期間使用されており、高速というだけでなく高い信頼性、そして豊富な実践例があります。
また、最新の語彙に随時対応し続ける {{neologd}} や、国立国語研究所が開発した {{unidic}} を利用することができるのも {{mecab}} のメリットだと思います。

</div>
</details>

## GiNZAを動かす

ここで紹介するコードは {{github-virtualenv}} のubuntu-latest, macos-latest, windows-latestとPython 3.6, 3.7, 3.8の組み合わせ（計9通り）で動作検証しています。

**動作検証結果**

[![TestOnUbuntu](https://github.com/poyo46/ginza-examples/workflows/TestOnUbuntu/badge.svg)](https://github.com/poyo46/ginza-examples/actions?query=workflow%3ATestOnUbuntu) [![TestOnMac](https://github.com/poyo46/ginza-examples/workflows/TestOnMac/badge.svg)](https://github.com/poyo46/ginza-examples/actions?query=workflow%3ATestOnMac) [![TestOnWindows](https://github.com/poyo46/ginza-examples/workflows/TestOnWindows/badge.svg)](https://github.com/poyo46/ginza-examples/actions?query=workflow%3ATestOnWindows)

[![TestOther](https://github.com/poyo46/ginza-examples/workflows/TestOther/badge.svg)](https://github.com/poyo46/ginza-examples/actions?query=workflow%3ATestOther) （リンク切れのチェックなど）

**動作環境構築**

Pythonに親しみのない方や手っ取り早く動作環境がほしい方向けにオンラインの実行環境を用意しています。
ブラウザで {{repl}} を開いて実行してください。
ローカル環境で試行したい方は {{ge-github}} をcloneしてご利用ください。

どちらの環境でもセットアップに `$ poetry install` が必要です。大きめの辞書をダウンロードするため5分程度かかる可能性があります。

### 形態素解析

{{token_information}}

<details>
<summary>説明を開く</summary>
<div>

日本語の文を単語ごとに分け、各単語の解析結果を表示しています。

`Token.pos_` は [Universal Part-of-speech Tags](https://spacy.io/api/annotation#pos-universal) と呼ばれるもので、言語に依存せず全世界的に単語の品詞を表そうというものです（Part-of-speech = 品詞）。

`Token.ent_type_` は固有表現と呼ばれるもので、例えば人名には `Person` が、料理名には `Dish` が割り当てられます。
詳細な定義については [こちら](http://liat-aip.sakura.ne.jp/ene/ene8/definition_jp/html/enedetail.html) をご覧ください。

`Token` の他の属性については [spaCy API doc](https://spacy.io/api/token#attributes) をご覧ください。

</div>
</details>

**応用**
この解析結果を使って例えば次のようなことができます。

* 文中に含まれる単語から動詞と形容詞の原形を抽出する。
* 文中に含まれる食べ物を抽出してカウントする。
* 文中の個人情報をマスキングする。

### テキストを文のリストに分割する

{{split_text}}

<details>
<summary>説明を開く</summary>
<div>

{{spacy}} の [Doc.sents](https://spacy.io/api/doc#sents) を利用してテキストを文のリストに変換しています。

</div>
</details>

### 依存構造解析・可視化

{{displacy}}

ブラウザで http://localhost:5000 を開くと解析結果が表示されます。
同時に、サンプルコードでは画像を {{displacy_img}} に保存しています。

### 文章要約

LexRankアルゴリズムを用いて抽出型要約を実行します。
抽出型要約とは、元の文から重要な文を（無加工で）抽出するものです。
サンプル文として [『走れメロス』](https://github.com/poyo46/ginza-examples/blob/master/examples/data/run_melos.txt) を用意しました。

{{lexrank_summary}}

LexRankアルゴリズムによって抽出された、重要度の高い上位 {{lexrank_summary_n}} 文です。
重要度のスコアは一度だけ計算すればよいため、抽出する文の数を変更したい場合は `lexrank_scoring` の結果を再利用すると速いです。

## ライセンス

### GiNZA
{{ginza}} そのものは {{ginza-license}} で利用できます。詳しくは [ライセンス条項](https://github.com/megagonlabs/ginza#license) をご覧ください。

### GiNZA examples
筆者の {{ge-qiita}} および {{ge-github}} も同様に [MIT License](https://github.com/poyo46/ginza-examples/blob/master/LICENSE) で利用できます。

## 参考文献
* [株式会社リクルートの発表](https://www.recruit.co.jp/newsroom/2019/0402_18331.html)
* {{ginza-hp}}
* [spaCy API doc](https://spacy.io/api)
* {{mecab}}

## ご意見・ご要望など
ご意見・ご要望などは随時受け付けています。 {{ge-qiita}} へコメント、または {{ge-issues}} へ投稿をお願いします。


