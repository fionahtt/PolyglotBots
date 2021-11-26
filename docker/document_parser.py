import stanza
stanza.download('en',logging_level='WARN')


class DocumentParser:
    nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse,constituency,ner', verbose=False)

    def __init__(self, text):
        self.text = text
        self.doc = self.nlp(text)
        self.sentences = self.doc.sentences

    def print_token_data(self):
        for i, sentence in enumerate(self.doc.sentences):
            print(f'====== Sentence {i+1} Words =======')
            for word in sentence.words:
                print(
                    f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}')
            print("\n")

