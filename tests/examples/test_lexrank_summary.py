import subprocess
import numpy as np
from examples.lexrank_summary import (
    preprocess, lexrank_scoring, extract, EXAMPLE_PATH, N, EXAMPLE_SCRIPT
)


def test_preprocess():
    text = '''
    あいうえお。　「かきくけこ！」
「さしすせそ？」たちつてと【なにぬねの】は
ひふへほ。
    '''
    expected = 'あいうえお。かきくけこ。さしすせそ。たちつてとなにぬねのはひふへほ。'
    assert preprocess(text) == expected


def test_lexrank_scoring():
    text = 'メロスは激怒した。ほとんど全裸体であった。勇者は、ひどく赤面した。'
    sentences, scores = lexrank_scoring(text)
    assert len(sentences) == len(scores)
    for sentence, score in zip(sentences, scores):
        print(sentence, score)


def test_extract():
    sentences = ['文0', '文1', '文2', '文3', '文4']
    scores = np.array([3.1, 4.1, 5.9, 2.6, 5.3])
    assert extract(sentences, scores, 1) == ['文2']
    assert extract(sentences, scores, 3) == ['文1', '文2', '文4']
    assert extract(sentences, scores, len(sentences)) == sentences


def test_script():
    return_code = subprocess.call(EXAMPLE_SCRIPT.split(' '))
    assert return_code == 0
