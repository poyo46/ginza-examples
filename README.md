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

なお、最初にこの記事を書いたのは2019年の8月です。 [GiNZA](https://github.com/megagonlabs/ginza) の更新に追いつけなくなっていたので改めて書き直しました。

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
また、最新の語彙に随時対応し続ける [NEologd](https://github.com/neologd/mecab-ipadic-neologd) や、国立国語研究所が開発した [UniDic](https://unidic.ninjal.ac.jp/about_unidic) を利用することができるのも [MeCab](https://taku910.github.io/mecab/) のメリットだと思います。

</div>
</details>

## GiNZAを動かす

ここで紹介するコードは [GitHubホストランナーの仮想環境](https://docs.github.com/ja/actions/reference/virtual-environments-for-github-hosted-runners#supported-runners-and-hardware-resources) のubuntu-latest, macos-latest, windows-latestとPython 3.6, 3.7, 3.8の組み合わせ（計9通り）で動作検証しています。

**動作検証結果**

[![TestOnUbuntu](https://github.com/poyo46/ginza-examples/workflows/TestOnUbuntu/badge.svg)](https://github.com/poyo46/ginza-examples/actions?query=workflow%3ATestOnUbuntu) [![TestOnMac](https://github.com/poyo46/ginza-examples/workflows/TestOnMac/badge.svg)](https://github.com/poyo46/ginza-examples/actions?query=workflow%3ATestOnMac) [![TestOnWindows](https://github.com/poyo46/ginza-examples/workflows/TestOnWindows/badge.svg)](https://github.com/poyo46/ginza-examples/actions?query=workflow%3ATestOnWindows)

[![TestOther](https://github.com/poyo46/ginza-examples/workflows/TestOther/badge.svg)](https://github.com/poyo46/ginza-examples/actions?query=workflow%3ATestOther) （リンク切れのチェックなど）

### セットアップ

**オンライン**

Pythonに親しみのない方や手っ取り早く動作環境がほしい方向けにオンラインの実行環境を用意しています。ブラウザで [GiNZA examples - Repl.it](https://repl.it/github/poyo46/ginza-examples) を開いて `Run` をクリックしてください。セットアップ完了までに5分程度かかります。

**ローカル環境**

```
git clone https://github.com/poyo46/ginza-examples.git
cd ginza-examples
poetry install
```

もし `poetry` が未導入であれば `$ pip install poetry` でインストールしてください。

### 形態素解析

<details><summary>ソースコードを開く</summary><div>

```python:examples/token_information.py
import sys
from typing import List
from pprint import pprint
import spacy
import ginza

nlp = spacy.load('ja_ginza')


def tokenize(text: str) -> List[List[str]]:
    """
    日本語文を形態素解析する。

    Parameters
    ----------
    text : str
        解析対象の日本語テキスト。

    Returns
    -------
    List[List[str]]
        形態素解析結果。

    Notes
    -----
    * Token 属性の詳細については次のリンク先をご覧ください。
      https://spacy.io/api/token#attributes
    * Token.lemma_ の値は SudachiPy の Morpheme.dictionary_form() です。
    * Token.ent_type_ の詳細については次のリンク先をご覧ください。
      http://liat-aip.sakura.ne.jp/ene/ene8/definition_jp/html/enedetail.html
    """
    doc = nlp(text)

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

    return attrs_list


EXAMPLE_TEXT = '田中部長に伝えてください。'
EXAMPLE_SCRIPT = f'python examples/token_information.py {EXAMPLE_TEXT}'

ATTRS = [
    'i', 'text', 'lemma_', 'reading_form', 'pos_', 'tag_',
    'inflection', 'ent_type_'
]

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_text = sys.argv[1]
        pprint(tokenize(input_text))
    else:
        print('Please run as follows: \n$ ' + EXAMPLE_SCRIPT)
```

</div></details>

[ソースコードをGitHubで見る](https://github.com/poyo46/ginza-examples/blob/master/examples/token_information.py)

**実行**

```
python examples/token_information.py 田中部長に伝えてください。
```

**結果**

| i | text | lemma_ | reading_form | pos_ | tag_ | inflection | ent_type_ |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 0 | 田中 | 田中 | タナカ | PROPN | 名詞-固有名詞-人名-姓 |  | Person |
| 1 | 部長 | 部長 | ブチョウ | NOUN | 名詞-普通名詞-一般 |  | Position_Vocation |
| 2 | に | に | ニ | ADP | 助詞-格助詞 |  |  |
| 3 | 伝え | 伝える | ツタエ | VERB | 動詞-一般 | 下一段-ア行,連用形-一般 |  |
| 4 | て | て | テ | SCONJ | 助詞-接続助詞 |  |  |
| 5 | ください | くださる | クダサイ | AUX | 動詞-非自立可能 | 五段-ラ行,命令形 |  |
| 6 | 。 | 。 | 。 | PUNCT | 補助記号-句点 |  |  |


※結果は見やすいように加工しています。

<details>
<summary>説明を開く</summary>
<div>

日本語の文を単語ごとに分け、各単語の解析結果を表示しています。

`Token.pos_` は [Universal Part-of-speech Tags](https://spacy.io/api/annotation#pos-universal) と呼ばれるもので、言語に依存せず全世界的に単語の品詞を表そうというものです（Part-of-speech = 品詞）。

`Token.ent_type_` は固有表現と呼ばれるもので、例えば人名には `Person` が、料理名には `Dish` が割り当てられます。詳細な定義については [こちら](http://liat-aip.sakura.ne.jp/ene/ene8/definition_jp/html/enedetail.html) をご覧ください。

`Token` の他の属性については [spaCy API doc](https://spacy.io/api/token#attributes) をご覧ください。

</div>
</details>

**応用**
この解析結果を使って例えば次のようなことができます。

* 文中に含まれる単語から動詞と形容詞の原形を抽出する。
* 文中に含まれる食べ物を抽出してカウントする。
* 文中の個人情報をマスキングする。

### テキストを文のリストに分割する

<details><summary>ソースコードを開く</summary><div>

```python:examples/split_text.py
import sys
from typing import List
import spacy

nlp = spacy.load('ja_ginza')


def get_sentences(text: str) -> List[str]:
    """
    文のリストに分割したテキストを取得する。

    Parameters
    ----------
    text : str
        分割対象の日本語テキスト。

    Returns
    -------
    List[str]
        文のリスト。結合すると `text` に一致する。

    See Also
    --------
    https://spacy.io/api/doc#sents
    """
    doc = nlp(text)
    sentences = [s.text for s in doc.sents]
    return sentences


EXAMPLE_TEXT = 'はい、そうです。ありがとうございますよろしくお願いします。'
EXAMPLE_SCRIPT = f'python examples/split_text.py {EXAMPLE_TEXT}'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_text = sys.argv[1]
        print('\n'.join(get_sentences(input_text)))
    else:
        print('Please run as follows: \n$ ' + EXAMPLE_SCRIPT)
```

</div></details>

[ソースコードをGitHubで見る](https://github.com/poyo46/ginza-examples/blob/master/examples/split_text.py)

**実行**

```
python examples/split_text.py はい、そうです。ありがとうございますよろしくお願いします。
```

**結果**

```
はい、そうです。
ありがとうございます
よろしくお願いします。
```

<details>
<summary>説明を開く</summary>
<div>

[spaCy](https://spacy.io/) の [Doc.sents](https://spacy.io/api/doc#sents) を利用してテキストを文のリストに変換しています。

</div>
</details>

### 依存構造解析・可視化

<details><summary>ソースコードを開く</summary><div>

```python:examples/displacy.py
import sys
from pathlib import Path
import spacy
from spacy import displacy

nlp = spacy.load('ja_ginza')


def visualize(text: str) -> None:
    """
    日本語文の文法的構造を解析し、可視化する。

    Parameters
    ----------
    text : str
        解析対象の日本語テキスト。

    Notes
    -----
    実行後、 ブラウザで http://localhost:5000 を開くと画像が表示される。
    """
    doc = nlp(text)
    displacy.serve(doc, style='dep')


def save_as_image(text: str, path) -> None:
    """
    日本語文の文法的構造を解析し、結果を画像として保存する。

    Parameters
    ----------
    text : str
        解析対象の日本語テキスト。
    path
        保存先のファイルパス。

    Notes
    -----
    画像はSVG形式で保存される。
    """
    doc = nlp(text)
    svg = displacy.render(doc, style='dep')
    with open(path, mode='w') as f:
        f.write(svg)


EXAMPLE_TEXT = 'あのラーメン屋にはよく行く。'
EXAMPLE_SCRIPT = f'python examples/displacy.py {EXAMPLE_TEXT}'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_text = sys.argv[1]
        save_to = Path(__file__).with_name('displacy.svg')
        save_as_image(input_text, save_to)
        visualize(input_text)
    else:
        print('Please run as follows: \n$ ' + EXAMPLE_SCRIPT)
```

</div></details>

[ソースコードをGitHubで見る](https://github.com/poyo46/ginza-examples/blob/master/examples/displacy.py)

**実行**

```
python examples/displacy.py あのラーメン屋にはよく行く。
```

**結果**

```
Using the 'dep' visualizer
Serving on http://0.0.0.0:5000 ...
```

![結果の画像](https://raw.githubusercontent.com/poyo46/ginza-examples/master/examples/displacy.svg)

ブラウザで http://localhost:5000 を開くと解析結果が表示されます。同時に、サンプルコードでは画像を [examples/displacy.svg](https://raw.githubusercontent.com/poyo46/ginza-examples/master/examples/displacy.svg) に保存しています。

### 文章要約

LexRankアルゴリズムを用いて抽出型要約を実行します。抽出型要約とは、元の文から重要な文を（無加工で）抽出するものです。サンプル文として [『走れメロス』](https://github.com/poyo46/ginza-examples/blob/master/examples/data/run_melos.txt) を用意しました。

<details><summary>ソースコードを開く</summary><div>

```python:examples/lexrank_summary.py
import sys
import re
from typing import Tuple, List
from pathlib import Path
import numpy as np
import spacy
from sumy.summarizers.lex_rank import LexRankSummarizer

nlp = spacy.load('ja_ginza')


def preprocess(text: str) -> str:
    """
    要約の前処理を実施する。
    * 全角スペースや括弧、改行を削除する。
    * ！？を。に置換する

    Parameters
    ----------
    text : str
        日本語のテキスト。

    Returns
    -------
    str
        前処理が実施されたtext
    """
    text = re.sub('[　「」『』【】\r\n]', '', text)
    text = re.sub('[！？]', '。', text)
    text = text.strip()
    return text


def lexrank_scoring(text: str) -> Tuple[List[str], np.ndarray]:
    """
    LexRankアルゴリズムによって文に点数をつける。
    この点数は文の重要度とみなすことができる。

    Parameters
    ----------
    text : str
        分析対象のテキスト。

    Returns
    -------
    List[str]
        text を文のリストに分解したもの。
    np.ndarray
        文のリストに対応する重要度のリスト。
    """
    doc = nlp(text)

    # 文のリストと単語のリストをつくる
    sentences = []
    corpus = []
    for sent in doc.sents:
        sentences.append(sent.text)
        tokens = []
        for token in sent:
            # 文に含まれる単語のうち, 名詞・副詞・形容詞・動詞に限定する
            if token.pos_ in ('NOUN', 'ADV', 'ADJ', 'VERB'):
                # ぶれをなくすため, 単語の見出し語 Token.lemma_ を使う
                tokens.append(token.lemma_)
        corpus.append(tokens)
    # sentences = [文0, 文1, ...]
    # corpus = [[文0の単語0, 文0の単語1, ...], [文1の単語0, 文1の単語1, ...], ...]

    # sumyライブラリによるLexRankスコアリング
    lxr = LexRankSummarizer()
    tf_metrics = lxr._compute_tf(corpus)
    idf_metrics = lxr._compute_idf(corpus)
    matrix = lxr._create_matrix(corpus, lxr.threshold, tf_metrics, idf_metrics)
    scores = lxr.power_method(matrix, lxr.epsilon)
    # scores = [文0の重要度, 文1の重要度, ...]

    return sentences, scores


def extract(sentences: List[str], scores: np.ndarray, n: int) -> List[str]:
    """
    スコアの高い順にn個の文を抽出する。

    Parameters
    ----------
    sentences : List[str]
        文のリスト。
    scores : np.ndarray
        スコアのリスト。
    n : int
        抽出する文の数。

    Returns
    -------
    List[str]
        sentencesから抽出されたn個の文のリスト。
    """
    assert len(sentences) == len(scores)

    # scoresのインデックスリスト
    indices = range(len(scores))

    # スコアの大きい順に並べ替えたリスト
    sorted_indices = sorted(indices, key=lambda i: scores[i], reverse=True)

    # スコアの大きい順からn個抽出したリスト
    extracted_indices = sorted_indices[:n]

    # インデックスの並び順をもとに戻す
    extracted_indices.sort()

    # 抽出されたインデックスに対応する文のリストを返す
    return [sentences[i] for i in extracted_indices]


def get_summary(path, n) -> List[str]:
    with open(path, mode='rt', encoding='utf-8') as f:
        text = f.read()
    text = preprocess(text)
    sentences, scores = lexrank_scoring(text)
    return extract(sentences, scores, n)


EXAMPLE_PATH = Path(__file__).with_name('data') / 'run_melos.txt'
N = 15
EXAMPLE_SCRIPT = f'python examples/lexrank_summary.py examples/data/run_melos.txt {N}'

if __name__ == '__main__':
    if len(sys.argv) > 2:
        input_path = sys.argv[1]
        input_n = int(sys.argv[2])
        extracted_sentences = get_summary(input_path, input_n)
        print('\n'.join(extracted_sentences))
    else:
        print('Please run as follows: \n$ ' + EXAMPLE_SCRIPT)
```

</div></details>

[ソースコードをGitHubで見る](https://github.com/poyo46/ginza-examples/blob/master/examples/lexrank_summary.py)

**実行**

```
python examples/lexrank_summary.py examples/data/run_melos.txt 15
```

**結果**

```
人を、信ずる事が出来ぬ、というのです。
三日のうちに、私は村で結婚式を挙げさせ、必ず、ここへ帰って来ます。
そうして身代りの男を、三日目に殺してやるのも気味がいい。
ものも言いたくなくなった。
そうして、少し事情があるから、結婚式を明日にしてくれ、と頼んだ。
あれが沈んでしまわぬうちに、王城に行き着くことが出来なかったら、あの佳い友達が、私のために死ぬのです。
何をするのだ。
けれども、今になってみると、私は王の言うままになっている。
王は、ひとり合点して私を笑い、そうして事も無く私を放免するだろう。
私を、待っている人があるのだ。
死んでお詫び、などと気のいい事は言って居られぬ。
メロス。
その人を殺してはならぬ。
メロスが帰って来た。
メロスだ。
```

LexRankアルゴリズムによって抽出された、重要度の高い上位 15 文です。重要度のスコアは一度だけ計算すればよいため、抽出する文の数を変更したい場合は [lexrank_scoring](https://github.com/poyo46/ginza-examples/blob/master/examples/lexrank_summary.py#L34) の結果を再利用すると速いです。

### 文の類似度

<details><summary>ソースコードを開く</summary><div>

```python:examples/similarity.py
import sys
from typing import List
from pprint import pprint
import spacy
import numpy as np

nlp = spacy.load('ja_ginza')


def similarity_matrix(texts: List[str]) -> List[List[np.float64]]:
    """
    テキスト同士の類似度を計算する。

    Parameters
    ----------
    texts : str
        日本語文のリスト。

    Returns
    -------
    List[List[np.float64]]
        文同士の類似度。

    Notes
    -----
    spaCy の Doc.similarity (https://spacy.io/api/doc#similarity) を使っている。
    """
    docs = [nlp(text) for text in texts]
    rows = [[a.similarity(b) for a in docs] for b in docs]
    return rows


EXAMPLE_TEXTS = [
    '今日はとても良い天気です。',
    '昨日の天気は大雨だったのに。',
    'ラーメンを食べました。'
]
EXAMPLE_SCRIPT = f'python examples/similarity.py ' + ' '.join(EXAMPLE_TEXTS)

if __name__ == '__main__':
    if len(sys.argv) > 2:
        input_texts = sys.argv[1:]
        pprint(similarity_matrix(input_texts))
    else:
        print('Please run as follows: \n$ ' + EXAMPLE_SCRIPT)
```

</div></details>

[ソースコードをGitHubで見る](https://github.com/poyo46/ginza-examples/blob/master/examples/similarity.py)

**実行**

```
python examples/similarity.py 今日はとても良い天気です。 昨日の天気は大雨だったのに。 ラーメンを食べました。
```

**結果**

|  | 今日はとても良い天気です。 | 昨日の天気は大雨だったのに。 | ラーメンを食べました。 |
| :-- | :-- | :-- | :-- |
| 今日はとても良い天気です。 | 1.0 | 0.9085916084662856 | 0.7043564497093551 |
| 昨日の天気は大雨だったのに。 | 0.9085916084662856 | 1.0 | 0.7341796340817486 |
| ラーメンを食べました。 | 0.7043564497093551 | 0.7341796340817486 | 1.0 |


※結果は見やすいように加工しています。

<details>
<summary>説明を開く</summary>
<div>

[spaCy](https://spacy.io/) の [Doc.similarity()](https://spacy.io/api/doc#similarity) を利用して文同士の類似度を計算しています。自分自身との類似度は1で、類似度の値が大きいほど似ているということです。

</div>
</details>

## ライセンス

### GiNZA

[GiNZA](https://github.com/megagonlabs/ginza) そのものは [MIT License](https://github.com/megagonlabs/ginza/blob/develop/LICENSE) で利用できます。詳しくは [ライセンス条項](https://github.com/megagonlabs/ginza#license) をご覧ください。

### GiNZA examples

筆者の [Qiitaの記事](https://qiita.com/poyo46/items/7a4965455a8a2b2d2971) および [GiNZA examples - GitHub](https://github.com/poyo46/ginza-examples) も同様に [MIT License](https://github.com/poyo46/ginza-examples/blob/master/LICENSE) で利用できます。

## 注意事項

* [GiNZA](https://github.com/megagonlabs/ginza) を利用できる言語はPythonのみです。しかしフレームワークである [spaCy](https://spacy.io/) にはJavaScript版やR版など [Python以外の言語での実装](https://spacy.io/universe/category/nonpython) があるため、すごい人たちが移植してくれることを期待します。
* 単語のネガティブ・ポジティブを数値化する [Token.sentiment](https://spacy.io/api/token#attributes) は現時点で実装されていませんが、 [GiNZA](https://github.com/megagonlabs/ginza) 開発者の方から直々にコメントをいただき、今後実装を計画していただけるとのことです。

## ご意見・ご要望など
ご意見・ご要望などは随時受け付けています。 [Qiitaの記事](https://qiita.com/poyo46/items/7a4965455a8a2b2d2971) へコメント、または [GitHubのIssues](https://github.com/poyo46/ginza-examples/issues) へ投稿をお願いします。
