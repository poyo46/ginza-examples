from typing import Optional, List
import inspect
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString


def table_md(header: List[str], rows: List[List[str]]) -> str:
    head_md = '| ' + ' | '.join(header) + ' |\n'
    hr_md = '| ' + ' | '.join([':--'] * len(header)) + ' |\n'
    body_md = ''
    for row in rows:
        row = [str(r) for r in row]
        body_md += '| ' + ' | '.join(row) + ' |\n'
    return head_md + hr_md + body_md


def blob_url(path: str) -> str:
    base = 'https://github.com/poyo46/ginza-examples/blob/master/'
    if path.startswith('/'):
        return base + path[1:]
    else:
        return base + path


def raw_url(path: str) -> str:
    base = 'https://raw.githubusercontent.com/poyo46/ginza-examples/master/'
    if path.startswith('/'):
        return base + path[1:]
    else:
        return base + path


def template(module,
             result_console: Optional[str] = None,
             result_markdown: Optional[str] = None,
             result_img_url: Optional[str] = None) -> str:
    module_path = f'{module.__name__.replace(".", "/")}.py'
    lines = [
        '<details><summary>ソースコードを開く</summary><div>',
        '',
        f'```python:{module_path}',
        inspect.getsource(module).strip('\n'),
        '```',
        '',
        '</div></details>',
        '',
        f'[ソースコードをGitHubで見る]({blob_url(module_path)})',
        '',
        '**実行**',
        '',
        '```',
        '$ ' + module.EXAMPLE_SCRIPT,
        '```',
        '',
        '**結果**',
        ''
    ]
    if result_console is not None:
        lines.append('```')
        lines.append(result_console)
        lines.append('```')
        lines.append('')
    if result_markdown is not None:
        lines.append(result_markdown)
        lines.append('')
    if result_img_url is not None:
        lines.append(f'![結果の画像]({result_img_url})')
        lines.append('')
    lines = lines[:-1]
    return '\n'.join(lines)


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
    pass
