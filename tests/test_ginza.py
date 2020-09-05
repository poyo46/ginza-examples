import requests


def test_ginza_license():
    """
    GitHub licenses API を使ってGiNZAのライセンスをチェックする
    """
    url = 'https://api.github.com/repos/megagonlabs/ginza/license'
    response = requests.get(url)
    json = response.json()
    assert json['license']['key'] == 'mit'
