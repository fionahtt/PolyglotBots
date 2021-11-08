import stanza
stanza.download('en')


class DocumentParser:
    nlp = stanza.Pipeline(lang='en', processors='tokenize')

    def __init__(self, text):
        self.text = text
        self.doc = self.nlp(text)
        for i, sentence in enumerate(self.doc.sentences):
            print(f'====== Sentence {i+1} tokens =======')
            print(
                *[f'id: {token.id}\ttext: {token.text}' for token in sentence.tokens], sep='\n')
