import stanza
stanza.download('en')

"""
Notes:
using recent dev version of Stanza (contains fixes for constituency parsing issues)
-had issues before where constituency parsing took different sentence in document
than current sentence

pip install git+https://github.com/stanfordnlp/stanza.git@dev
"""

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
