from typing import List
from pathlib import Path
import re
import requests


def extracted_urls() -> List[str]:
    """
    README.mdからURLを抽出する。

    Returns
    -------
    List[str]
        README.mdに含まれるURLのリスト。重複は除かれている。
    """
    file_path = Path(__file__).parents[1] / 'README.md'
    with open(file_path, mode='rt', encoding='utf-8') as f:
        readme = f.read()
    urls = re.findall(r'https?://[\w/:%#$&?~.=+-]+', readme)
    return list(set(urls))


def test_url():
    for url in extracted_urls():
        response = requests.get(url)
        assert 200 <= response.status_code < 400, url
