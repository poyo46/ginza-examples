#  PYTHONPATH=./ python dev/update_readme.py

from pathlib import Path
from dev.util import table_md, get_function_source
from examples.token_information import HEADER, TEXT, tokenize

rep = {
    '$ginza': '[GiNZA](https://github.com/megagonlabs/ginza)',
    '$qiita': '[Qiitaの記事](https://qiita.com/poyo46/items/7a4965455a8a2b2d2971)',
    '$github': '[GiNZA examples - GitHub](https://github.com/poyo46/ginza-examples)',
    '$spacy': '[spaCy](https://spacy.io/)',
    '$mecab': '[MeCab](https://taku910.github.io/mecab/)'
}


def update_replacements() -> None:
    print('token_information - tokenize')

    token_information_src = '\n'.join([
        'import spacy',
        'import ginza\n',
        "nlp = spacy.load('ja_ginza')\n",
        get_function_source(tokenize).replace('nlp(text)', f"nlp('{TEXT}')"),
        '\nprint(attrs_list)'
    ])
    rep['$token_information_src'] = token_information_src
    rep['$token_information_result'] = table_md(HEADER, tokenize(TEXT))


def readme_template() -> str:
    file_path = Path(__file__).with_name('README.md.tpl')
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
