#  PYTHONPATH=./ python dev/update_readme.py

from typing import Optional, Dict
from pathlib import Path
import yaml
from dev.util import table_md, basic_src
from examples import token_information, split_text, displacy


def rep_def() -> Dict[str, str]:
    file_path = Path(__file__).parent / 'data' / 'rep.yml'
    with open(file_path, mode='rt', encoding='utf-8') as f:
        text = f.read()
    yml = yaml.safe_load(text)
    return yml


def updated_rep(dic) -> Dict:
    print('token_information - tokenize')
    dic['$token_information_src'] = basic_src(
        token_information.tokenize, token_information.TEXT, ['import ginza']
    ) + 'print(attrs_list)'
    dic['$token_information_res'] = table_md(
        token_information.HEADER,
        token_information.tokenize(token_information.TEXT)
    )

    print('split_text - split_text_into_list_of_sentences')
    dic['$split_text_src'] = basic_src(
        split_text.split_text_into_list_of_sentences,
        split_text.TEXT
    ) + 'print(sentences)'
    dic['$split_text_res'] = split_text.split_text_into_list_of_sentences(
        split_text.TEXT
    ).__str__()

    print('displacy - visualize')
    dic['$displacy_src'] = basic_src(
        displacy.visualize,
        displacy.TEXT,
        ['from spacy import displacy']
    ).strip('\n')
    displacy_save_to = Path(__file__).parents[1] / 'examples' / 'displacy.svg'
    displacy.save_as_image(displacy.TEXT, displacy_save_to)
    return dic


def readme_template() -> str:
    file_path = Path(__file__).parent / 'data' / 'README.md.tpl'
    with open(file_path, mode='rt', encoding='utf-8') as f:
        return f.read()


def replace_vars(md: str) -> str:
    for k, v in rep.items():
        md = md.replace(k, v)
    return md


def save_readme(md: str) -> None:
    file_path = Path(__file__).parents[1] / 'README.md'
    with open(file_path, mode='wt', encoding='utf-8') as f:
        f.write(md)


if __name__ == '__main__':
    rep = rep_def()
    rep = updated_rep(rep)
    template = readme_template()
    readme = replace_vars(template)
    save_readme(readme)
