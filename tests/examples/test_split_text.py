from examples.split_text import split_text_into_list_of_sentences, TEXT, main


def test_split_text_into_list_of_sentences():
    sentences = split_text_into_list_of_sentences(TEXT)
    expected = ['はい、そうです。', 'ありがとうございます', 'よろしくお願いします。']
    assert sentences == expected


def test_main():
    main()
