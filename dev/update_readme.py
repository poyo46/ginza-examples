#  PYTHONPATH=./ python dev/update_readme.py

from typing import Dict
from pathlib import Path
import yaml
from dev.util import table_md, template
from examples import token_information, split_text, displacy, lexrank_summary


def rep_def() -> Dict[str, str]:
    file_path = Path(__file__).parent / 'data' / 'rep.yml'
    with open(file_path, mode='rt', encoding='utf-8') as f:
        text = f.read()
    yml = yaml.safe_load(text)
    return yml


def updated_rep(dic) -> Dict:
    print('token_information')
    dic['{{token_information}}'] = template(
        token_information,
        result_markdown=table_md(
            token_information.ATTRS,
            token_information.tokenize(token_information.EXAMPLE_TEXT)
        )
    )

    print('split_text')
    dic['{{split_text}}'] = template(
        split_text,
        result_console='\n'.join(
            split_text.get_sentences(split_text.EXAMPLE_TEXT)
        )
    )

    print('displacy')
    displacy_img_path = 'examples/displacy.svg'
    dic['{{displacy_img_path}}'] = displacy_img_path
    dic['{{displacy}}'] = template(
        displacy,
        result_console='\n'.join([
            "Using the 'dep' visualizer",
            'Serving on http://0.0.0.0:5000 ...'
        ]),
        result_img_path=displacy_img_path
    )

    print('lexrank_summary')
    dic['{{lexrank_summary_n}}'] = str(lexrank_summary.N)
    dic['{{lexrank_summary}}'] = template(
        lexrank_summary,
        result_console='\n'.join(lexrank_summary.main(
            lexrank_summary.EXAMPLE_PATH,
            lexrank_summary.N
        ))
    )

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
