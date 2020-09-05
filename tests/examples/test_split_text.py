import subprocess
from examples.split_text import get_sentences, EXAMPLE_TEXT, EXAMPLE_SCRIPT


def test_split_text_into_list_of_sentences():
    sentences = get_sentences(EXAMPLE_TEXT)
    expected = ['はい、そうです。', 'ありがとうございます', 'よろしくお願いします。']
    assert sentences == expected


def test_script():
    return_code = subprocess.call(EXAMPLE_SCRIPT.split(' '))
    assert return_code == 0
