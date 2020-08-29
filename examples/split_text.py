import sys
from typing import List, Optional
import spacy

nlp = spacy.load('ja_ginza')


def split_text_into_list_of_sentences(text: str) -> List[str]:
    """
    日本語のテキストを文のリストに分割する。

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


TEXT = 'はい、そうです。ありがとうございますよろしくお願いします。'


def main(text: Optional[str] = None):
    if text is None:
        text = TEXT
    print(split_text_into_list_of_sentences(text))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
