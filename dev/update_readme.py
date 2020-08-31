#  PYTHONPATH=./ python dev/update_readme.py

from typing import Dict
from pathlib import Path
import yaml
from dev.util import table_md, basic_src, get_function_source
from examples import token_information, split_text, displacy, lexrank_summary


def rep_def() -> Dict[str, str]:
    file_path = Path(__file__).parent / 'data' / 'rep.yml'
    with open(file_path, mode='rt', encoding='utf-8') as f:
        text = f.read()
    yml = yaml.safe_load(text)
    return yml


def updated_rep(dic) -> Dict:
    print('token_information')
    dic['$token_information_src'] = basic_src(
        token_information.tokenize, token_information.TEXT, ['import ginza']
    ) + 'print(attrs_list)'
    dic['$token_information_res'] = table_md(
        token_information.HEADER,
        token_information.tokenize(token_information.TEXT)
    )

    print('split_text')
    dic['$split_text_src'] = basic_src(
        split_text.split_text_into_list_of_sentences,
        split_text.TEXT
    ) + 'print(sentences)'
    dic['$split_text_res'] = split_text.split_text_into_list_of_sentences(
        split_text.TEXT
    ).__str__()

    print('displacy')
    dic['$displacy_src'] = basic_src(
        displacy.visualize,
        displacy.TEXT,
        ['from spacy import displacy']
    ).strip('\n')
    displacy_save_to = Path(__file__).parents[1] / 'examples' / 'displacy.svg'
    displacy.save_as_image(displacy.TEXT, displacy_save_to)

    print('lexrank_summary')
    lexrank_summary_imports = '\n'.join([
        'import spacy',
        'from sumy.summarizers.lex_rank import LexRankSummarizer'
    ]) + '\n'
    num_sents = '15'
    dic['$lexrank_summary_n'] = num_sents
    lexrank_summary_blocks = [
        lexrank_summary_imports,
        "nlp = spacy.load('ja_ginza')\n",
        "with open('/path/to/run_melos.txt', mode='rt') as f:",
        "    text = f.read()\n",
        get_function_source(lexrank_summary.lexrank_scoring),
        '\n' + get_function_source(
            lexrank_summary.extract
        ).replace('[:n]', f'[:{num_sents}]').replace('n個', f'{num_sents}個'),
        "\nprint('\\n'.join(extracted_sentences))"
    ]
    dic['$lexrank_summary_src'] = '\n'.join(lexrank_summary_blocks)
    dic['$lexrank_summary_res'] = '\n'.join(lexrank_summary.main())
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
