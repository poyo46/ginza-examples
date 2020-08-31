import sys
from typing import Optional
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
    日本語文の文法的構造を解析し、画像として保存する。

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


TEXT = 'あのラーメン屋にはよく行く。'


def main(text: Optional[str] = None):
    if text is None:
        text = TEXT
    visualize(text)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
