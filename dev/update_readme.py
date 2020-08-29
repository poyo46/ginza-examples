#  PYTHONPATH=./ python dev/update_readme.py

from typing import Optional, Dict
from pathlib import Path
import yaml
from dev.util import table_md, get_function_source
from examples import token_information, split_text


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


def rep_def() -> Dict[str, str]:
    file_path = Path(__file__).parent / 'data' / 'rep.yml'
    with open(file_path, mode='rt', encoding='utf-8') as f:
        text = f.read()
    yml = yaml.safe_load(text)
    return yml


def updated_rep(dic) -> Dict:
    print('token_information - tokenize')
    token_information_src = basic_src(
        token_information.tokenize, token_information.TEXT, import_ginza=True
    ) + 'print(attrs_list)'
    dic['$token_information_src'] = token_information_src
    dic['$token_information_res'] = table_md(
        token_information.HEADER,
        token_information.tokenize(token_information.TEXT)
    )

    print('split_text - split_text_into_list_of_sentences')
    split_text_src = basic_src(
        split_text.split_text_into_list_of_sentences,
        split_text.TEXT
    ) + 'print(sentences)'
    dic['$split_text_src'] = split_text_src
    dic['$split_text_res'] = split_text.split_text_into_list_of_sentences(
        split_text.TEXT
    ).__str__()
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
