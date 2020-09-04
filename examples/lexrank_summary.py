import sys
import re
from typing import Tuple, List
from pathlib import Path
import numpy
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


def lexrank_scoring(text: str) -> Tuple[List[str], numpy.ndarray]:
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
    numpy.ndarray
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


def extract(sentences: List[str], scores: numpy.ndarray, n: int) -> List[str]:
    """
    スコアの高い順にn個の文を抽出する。

    Parameters
    ----------
    sentences : List[str]
        文のリスト。
    scores : numpy.ndarray
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


def main(path, n) -> List[str]:
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
        extracted_sentences = main(input_path, input_n)
        print('\n'.join(extracted_sentences))
    else:
        print('Please run as follows: \n$ ' + EXAMPLE_SCRIPT)
