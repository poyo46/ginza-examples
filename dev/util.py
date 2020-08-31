from typing import Optional, List
from pathlib import Path
import inspect
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString


def table_md(header: List[str], rows: List[List[str]]) -> str:
    head_md = '| ' + ' | '.join(header) + ' |\n'
    hr_md = '| ' + ' | '.join([':--'] * len(header)) + ' |\n'
    body_md = ''
    for row in rows:
        body_md += '| ' + ' | '.join(row) + ' |\n'
    return head_md + hr_md + body_md


def get_function_source(f):
    try:
        lines_to_skip = len(f.__doc__.split('\n'))
    except AttributeError:
        lines_to_skip = 0

    all_lines = inspect.getsourcelines(f)[0]
    body_lines = all_lines[lines_to_skip + 1:]
    lines = []
    for line in body_lines:
        if 'return ' in line:
            continue
        if line.startswith('    '):
            lines.append(line[4:])
        else:
            lines.append(line)
    return ''.join(lines).strip('\n')


def basic_src(f: object, text: Optional[str] = None,
              imports: Optional[List[str]] = None) -> str:
    if imports is None:
        imports = []
    imports.insert(0, 'import spacy')
    import_block = '\n'.join(imports) + '\n'
    blocks = [
        import_block,
        "nlp = spacy.load('ja_ginza')\n",
        get_function_source(f)
    ]
    if text is not None:
        blocks[-1] = blocks[-1].replace('nlp(text)', f"nlp('{text}')")
    return '\n'.join(blocks) + '\n\n'


def download_aozora(url: str, path) -> None:
    """
    青空文庫の作品をダウンロードする。

    Parameters
    ----------
    url : str
        作品のURL。
    path
        保存先のパス。

    Notes
    -----
    走れメロスのURLは https://www.aozora.gr.jp/cards/000035/files/1567_14913.html
    """
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    html_text = response.text
    soup = BeautifulSoup(html_text, 'html.parser')
    main_text = soup.select_one('.main_text')

    text = ''
    for x in main_text:
        if type(x) == NavigableString:
            text += x
            continue
        text += ''.join([e.text for e in x.find_all('rb')])

    with open(path, mode='wt', encoding='utf-8') as f:
        f.write(text)


if __name__ == '__main__':
    run_meros = 'https://www.aozora.gr.jp/cards/000035/files/1567_14913.html'
    file_path = Path(__file__).parent / 'data' / 'run_melos.txt'
    download_aozora(run_meros, file_path)
