from typing import List
import spacy
import ginza
from rich.console import Console
from rich.table import Table

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


def print_table(header: List[str], rows: List[List[str]]) -> None:
    console = Console()
    table = Table(*header)
    for r in rows:
        table.add_row(*r)
    console.print(table)


sample_text = '田中部長に伝えてください。'

if __name__ == '__main__':
    print_table(
        ['i', 'text', 'lemma_', 'reading_form', 'pos_', 'tag_', 'inflection',
         'ent_type_'],
        tokenize(sample_text)
    )
