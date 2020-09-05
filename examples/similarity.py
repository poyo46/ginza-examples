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
