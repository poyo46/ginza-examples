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
    str :
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
    sentences : List[str]
        text を文のリストに分解したもの。
    scores : numpy.ndarray
        sentences に重要度のスコアをつけたもの。
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

    # 抽出されたインデックスに対応する文のリスト
    extracted_sentences = [sentences[i] for i in extracted_indices]

    return extracted_sentences


def main(file_path=None) -> List[str]:
    if file_path is None:
        file_path = Path(__file__).parent / 'data' / 'run_melos.txt'
    with open(file_path, mode='rt', encoding='utf-8') as f:
        text = f.read()

    text = preprocess(text)
    sentences, scores = lexrank_scoring(text)
    extracted_sentences = extract(sentences, scores, 15)
    return extracted_sentences


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(main(sys.argv[1]))
    else:
        print(main())
