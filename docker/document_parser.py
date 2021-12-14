import stanza
import re
stanza.download('en')

"""
Notes:
using recent dev version of Stanza (contains fixes for constituency parsing issues)
-had issues before where constituency parsing took different sentence in document
than current sentence
pip install git+https://github.com/stanfordnlp/stanza.git@dev
"""


class DocumentParser:
    nlp = stanza.Pipeline(
        lang='en', processors='tokenize,mwt,pos,lemma,depparse,constituency, ner', verbose=False)

    def __init__(self, text):
        def pre_process(text):
            # remove parentheticals
            text = re.sub(r"\([^()]*\)", "", text)
            # replace semi-colons with periods
            text = re.sub(r";", ".", text)
            text = re.sub("\n", ".", text)
            return text

        def find_appositions(sentence):
            def has_apposition(sentence):
                tree = sentence.constituency
                # Check to make sure node is a sentence
                if(tree.children[0].label != 'S'):
                    return False
                if(len(tree.children[0].children) != 3):
                    return False
                if(tree.children[0].children[0].label != 'NP'):
                    return False

                tree_np_labels = tree.children[0].children[0].children

                if (len(tree_np_labels) != 4):
                    return False

                correct_labels = ['NP', ',', 'NP', ',']
                # check to make sure sentence node only has 3 children
                for i in range(4):
                    if tree_np_labels[i].label != correct_labels[i]:
                        return False
                return True

            def get_children(pt):
                phrase = ""
                for elem in pt:
                    if elem.children == ():
                        first = elem.label[0]
                        if elem.label == ",":
                            phrase += elem.label
                        elif first == "'" or first == "-":
                            phrase += elem.label
                        else:
                            phrase += " " + elem.label
                    else:
                        phrase += get_children(elem.children)
                return phrase

            if not has_apposition(sentence):
                return None
            else:
                appos_phrase = sentence.constituency.children[0].children[0].children
                np1 = appos_phrase[0]
                np2 = appos_phrase[2]

                appos_sent_text = get_children(
                    np1.children) + " is" + get_children(np2.children) + "."
                appos_sentence = self.nlp(appos_sent_text)
                return appos_sentence.sentences[0]

        self.text = pre_process(text)
        self.doc = self.nlp(self.text)
        self.sentences = self.doc.sentences
        for sentence in self.sentences:
            appos_sentence = find_appositions(sentence)
            if appos_sentence != None:
                self.sentences.append(appos_sentence)

    def print_token_data(self):
        for i, sentence in enumerate(self.doc.sentences):
            print(f'====== Sentence {i+1} Words =======')
            for word in sentence.words:
                print(
                    f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}')

            print("\n")
