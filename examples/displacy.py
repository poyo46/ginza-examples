import sys
from typing import Optional
import spacy
from spacy import displacy

nlp = spacy.load('ja_ginza')


def visualize(text: str) -> None:
    doc = nlp(text)
    displacy.serve(doc, style='dep')


def save_as_image(text: str, path) -> None:
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
