import sys
from typing import List, Optional
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
