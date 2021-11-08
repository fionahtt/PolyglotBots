import stanza
stanza.download('en')


class DocumentParser:
    nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos')

    def __init__(self, text):
        self.text = text
        self.doc = self.nlp(text)
        for i, sentence in enumerate(self.doc.sentences):
            for word in sentence.words:
                print(
                    f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}')
            # print(f'====== Sentence {i+1} tokens =======')
            # print(
            #     *[f'id: {token.id}\ttext: {token.text}' for token in sentence.tokens], sep='\n')
