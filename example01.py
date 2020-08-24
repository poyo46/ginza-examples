import spacy

nlp = spacy.load('ja_ginza')
doc = nlp('あのラーメン屋にはよく行く。美味しいんだ。')

for sent in doc.sents:
    for token in sent:
        info = [
            token.i,  # トークン番号
            token.orth_,  # テキスト
            # token._.reading,  # 読みカナ
            token.lemma_,  # 基本形
            token.pos_,  # 品詞
            token.tag_,  # 品詞詳細
            # token._.inf  # 活用情報
        ]
        print(info)
