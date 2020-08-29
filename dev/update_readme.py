#  PYTHONPATH=./ python dev/update_readme.py

from typing import Optional
from pathlib import Path
from dev.util import table_md, get_function_source
from examples import token_information, split_text

rep = {
    '$ginza': '[GiNZA](https://github.com/megagonlabs/ginza)',
    '$qiita': '[Qiitaの記事](https://qiita.com/poyo46/items/7a4965455a8a2b2d2971)',
    '$github': '[GiNZA examples - GitHub](https://github.com/poyo46/ginza-examples)',
    '$spacy': '[spaCy](https://spacy.io/)',
    '$mecab': '[MeCab](https://taku910.github.io/mecab/)'
}


def basic_src(f, text, import_ginza: Optional[bool] = None) -> str:
    if import_ginza is None:
        import_ginza = False
    if import_ginza:
        blocks = [
            'import spacy',
            'import ginza\n',
            "nlp = spacy.load('ja_ginza')\n",
            get_function_source(f).replace('nlp(text)', f"nlp('{text}')")
        ]
    else:
        blocks = [
            'import spacy\n',
            "nlp = spacy.load('ja_ginza')\n",
            get_function_source(f).replace('nlp(text)', f"nlp('{text}')")
        ]
    return '\n'.join(blocks) + '\n\n'


def update_replacements() -> None:
    print('token_information - tokenize')
    token_information_src = basic_src(
        token_information.tokenize, token_information.TEXT, import_ginza=True
    ) + 'print(attrs_list)'
    rep['$token_information_src'] = token_information_src
    rep['$token_information_res'] = table_md(
        token_information.HEADER,
        token_information.tokenize(token_information.TEXT)
    )

    print('split_text - split_text_into_list_of_sentences')
    split_text_src = basic_src(
        split_text.split_text_into_list_of_sentences,
        split_text.TEXT
    ) + 'print(sentences)'
    rep['$split_text_src'] = split_text_src
    rep['$split_text_res'] = split_text.split_text_into_list_of_sentences(
        split_text.TEXT
    ).__str__()


def readme_template() -> str:
    file_path = Path(__file__).parent / 'data' / 'README.md.tpl'
    with open(file_path, mode='rt') as f:
        return f.read()


def replace_vars(md: str) -> str:
    for k, v in rep.items():
        md = md.replace(k, v)
    return md


def save_readme(md: str) -> None:
    file_path = Path(__file__).parents[1] / 'README.md'
    with open(file_path, mode='wt') as f:
        f.write(md)


if __name__ == '__main__':
    update_replacements()
    template = readme_template()
    readme = replace_vars(template)
    save_readme(readme)
