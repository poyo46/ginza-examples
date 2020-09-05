import subprocess
from examples.token_information import tokenize, EXAMPLE_TEXT, EXAMPLE_SCRIPT


def test_tokenize():
    attrs_list = tokenize(EXAMPLE_TEXT)
    expected = [
        ['0', '田中', '田中', 'タナカ', 'PROPN', '名詞-固有名詞-人名-姓', '',
         'Person'],
        ['1', '部長', '部長', 'ブチョウ', 'NOUN', '名詞-普通名詞-一般', '',
         'Position_Vocation'],
        ['2', 'に', 'に', 'ニ', 'ADP', '助詞-格助詞', '', ''],
        ['3', '伝え', '伝える', 'ツタエ', 'VERB', '動詞-一般',
         '下一段-ア行,連用形-一般', ''],
        ['4', 'て', 'て', 'テ', 'SCONJ', '助詞-接続助詞', '', ''],
        ['5', 'ください', 'くださる', 'クダサイ', 'AUX', '動詞-非自立可能',
         '五段-ラ行,命令形', ''],
        ['6', '。', '。', '。', 'PUNCT', '補助記号-句点', '', '']
    ]
    assert attrs_list == expected


def test_script():
    return_code = subprocess.call(EXAMPLE_SCRIPT.split(' '))
    assert return_code == 0
