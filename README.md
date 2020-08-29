# 日本語NLPライブラリGiNZAのすゝめ

## この記事について

本記事は、日本語の自然言語処理ライブラリである [GiNZA](https://github.com/megagonlabs/ginza) の紹介記事です。
[Qiitaの記事](https://qiita.com/poyo46/items/7a4965455a8a2b2d2971) と [GiNZA examples - GitHub](https://github.com/poyo46/ginza-examples) の二箇所に同じものを公開しています。

<details>
<summary>記事を書いた経緯</summary>
<div>

筆者は [GiNZA](https://github.com/megagonlabs/ginza) の開発者の方々と何の利害関係もありません。
自然言語処理系の最新技術を検索していてたまたま見つけ、その簡単さに感動したので勝手に宣伝しています。

> 全ての開発は感動から始まる。

コンピュータ産業の父であり筆者の尊敬するエンジニアである池田敏雄さんはこのように言いました。この記事の目的は [GiNZA](https://github.com/megagonlabs/ginza) の感動を共有することです。
自然言語処理という難解な分野でありますが、なるべく事前知識なしで [GiNZA](https://github.com/megagonlabs/ginza) を楽しめるようにと願っています。

</div>
</details>

**想定する読者**

* 自然言語処理ってどんなことができるの？という初学者の方
  * 筆者もまだまだ初学者ですが [GiNZA](https://github.com/megagonlabs/ginza) は簡単にすごいことができるのでぜひ見ていってください。
* Pythonを学びたての方やこれから学ぼうとしている方
  * Python学習のモチベーションになると思います。
* [MeCab](https://taku910.github.io/mecab/) などの形態素解析器を使ったことはあるが [GiNZA](https://github.com/megagonlabs/ginza) は初めて聞いたという方
  * 簡単に比較できるものではありませんが新たに [GiNZA](https://github.com/megagonlabs/ginza) を知る価値はあると思います。

## GiNZAとは

![GiNZAのロゴ](https://raw.githubusercontent.com/megagonlabs/ginza/static/docs/images/GiNZA_logo_4c_y.png)

[GiNZA](https://github.com/megagonlabs/ginza) は **日本語の** 自然言語処理ライブラリです。
もともと [spaCy](https://spacy.io/) という自然言語処理のフレームワークがあり、英語など主要な言語に対応していました。 [GiNZA](https://github.com/megagonlabs/ginza) は言わば [spaCy](https://spacy.io/) の日本語対応版です。
詳細については [GiNZAの公開ページ](https://megagonlabs.github.io/ginza/) をご覧ください。

<details>
<summary>GiNZAを選ぶ理由</summary>
<div>

日本語の形態素解析器として有名なものに [MeCab](https://taku910.github.io/mecab/) があります（形態素解析って何？という方は [Web茶まめ ©国立国語研究所](https://chamame.ninjal.ac.jp/) にて実行してみてください）。 [GiNZA](https://github.com/megagonlabs/ginza) も同様に日本語の文を分かち書きすることができます。単に日本語を分かち書きしたいだけなら [MeCab](https://taku910.github.io/mecab/) の方が圧倒的に速いです。
それでも [GiNZA](https://github.com/megagonlabs/ginza) には次のメリットがあると思います。

* 簡単に導入できる
  * [MeCab](https://taku910.github.io/mecab/) はOSに応じた環境構築を行わねばなりません。
  * [GiNZA](https://github.com/megagonlabs/ginza) の導入はOSに関係なく `$ pip install ginza` でできます。
* [spaCy](https://spacy.io/) フレームワークを採用している
  * 英語などの言語で [spaCy](https://spacy.io/) を利用した機械学習の実践例が見つかります。
  * [GiNZA](https://github.com/megagonlabs/ginza) の登場で同じことが日本語でもできるようになりました。
  * 例えばチャットボットAIのフレームワークで有名な [Rasa](https://rasa.com/) は [GiNZA](https://github.com/megagonlabs/ginza) のおかげで日本語でも使えるようになりました。
* [最新の研究](https://github.com/megagonlabs/ginza#training-data-sets) を反映している

なお、決して [MeCab](https://taku910.github.io/mecab/) をディスっているわけではないことを強調しておきます。状況や目的によって最適な選択は変わります。
[MeCab](https://taku910.github.io/mecab/) はすでに長期間使用されており、高速というだけでなく高い信頼性、そして豊富な実践例があります。
また、最新の語彙に随時対応し続ける [NEologd](https://github.com/neologd/mecab-ipadic-neologd) や、国立国語研究所が開発した [UniDic](https://unidic.ninjal.ac.jp/about_unidic) を利用することもできます。

</div>
</details>

## GiNZAを動かす
TODO: 動作確認環境とその日付

Pythonに親しみのない方や手っ取り早く動作環境がほしい方向けにオンラインの実行環境を用意しています。
本格的に動作検証したい方は [GiNZA examples - GitHub](https://github.com/poyo46/ginza-examples) をcloneしてご利用ください。

**オンラインで動かす（環境構築不要）**
TODO:

**ローカル環境で動かす**

セットアップ

```
$ git clone https://github.com/poyo46/ginza-examples.git
$ cd ginza-examples
$ poetry install
```

実行
```
$ python examples/***.py
```

### 形態素解析

**ソースコード**

```python
import spacy
import ginza

nlp = spacy.load('ja_ginza')

doc = nlp('田中部長に伝えてください。')
attrs_list = []
for token in doc:
    token_attrs = [
        token.i,  # トークン番号
        token.text,  # テキスト
        token.lemma_,  # 基本形
        ginza.reading_form(token),  # 読みカナ
        token.pos_,  # 品詞
        token.tag_,  # 品詞詳細
        ginza.inflection(token),  # 活用情報
        token.ent_type_  # 固有表現
    ]
    attrs_list.append([str(a) for a in token_attrs])

print(attrs_list)
```

**結果（整形済み）**

| i | text | lemma_ | reading_form | pos_ | tag_ | inflection | ent_type_ |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 0 | 田中 | 田中 | タナカ | PROPN | 名詞-固有名詞-人名-姓 |  | Person |
| 1 | 部長 | 部長 | ブチョウ | NOUN | 名詞-普通名詞-一般 |  | Position_Vocation |
| 2 | に | に | ニ | ADP | 助詞-格助詞 |  |  |
| 3 | 伝え | 伝える | ツタエ | VERB | 動詞-一般 | 下一段-ア行,連用形-一般 |  |
| 4 | て | て | テ | SCONJ | 助詞-接続助詞 |  |  |
| 5 | ください | くださる | クダサイ | AUX | 動詞-非自立可能 | 五段-ラ行,命令形 |  |
| 6 | 。 | 。 | 。 | PUNCT | 補助記号-句点 |  |  |


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

**ソースコード**

```python
import spacy

nlp = spacy.load('ja_ginza')

doc = nlp('はい、そうです。ありがとうございますよろしくお願いします。')
sentences = [s.text for s in doc.sents]

print(sentences)
```

**結果**

```
['はい、そうです。', 'ありがとうございます', 'よろしくお願いします。']
```

<details>
<summary>説明を開く</summary>
<div>

[spaCy](https://spacy.io/) の [Doc.sents](https://spacy.io/api/doc#sents) を利用してテキストを文のリストに変換しています。

</div>
</details>

## ライセンス

### GiNZA
[GiNZA](https://github.com/megagonlabs/ginza) そのものは [MIT License](https://github.com/megagonlabs/ginza/blob/develop/LICENSE) で利用できます。詳しくは [ライセンス条項](https://github.com/megagonlabs/ginza#license) をご覧ください。

### GiNZA examples
筆者の [Qiitaの記事](https://qiita.com/poyo46/items/7a4965455a8a2b2d2971) および [GiNZA examples - GitHub](https://github.com/poyo46/ginza-examples) も同様に [MIT License](https://github.com/poyo46/ginza-examples/blob/master/LICENSE) で利用できます。

## 参考文献
* [株式会社リクルートの発表](https://www.recruit.co.jp/newsroom/2019/0402_18331.html)
* [GiNZAの公開ページ](https://megagonlabs.github.io/ginza/)
* [spaCy API doc](https://spacy.io/api)
* [MeCab](https://taku910.github.io/mecab/)

## ご意見・ご要望など
ご意見・ご要望などは随時受け付けています。 [Qiitaの記事](https://qiita.com/poyo46/items/7a4965455a8a2b2d2971) へコメント、または [GitHubのIssues](https://github.com/poyo46/ginza-examples/issues) へ投稿をお願いします。


