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
