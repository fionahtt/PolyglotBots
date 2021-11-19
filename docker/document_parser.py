import stanza
import re
# stanza.download('en', logging_level='WARN')


class DocumentParser:
    nlp = stanza.Pipeline(
        lang='en', processors='tokenize,mwt,pos,lemma,depparse,constituency', verbose=False)

    def __init__(self, text):
        def pre_process(text):
            # remove parentheticals
            text = re.sub(r"\([^()]*\)", "", text)
            # replace semi-colons with periods
            text = re.sub(r";", ".", text)
            return text
        self.text = text
        self.doc = self.nlp(self.text)
        self.sentences = self.doc.sentences
        print("NONSENSE")
        for i, q in enumerate(self.doc.sentences):
            print(q.text)
            print(q.constituency)
        print("FSKDFLJKD")

    def print_token_data(self):
        for i, sentence in enumerate(self.doc.sentences):
            print(f'====== Sentence {i+1} Words =======')
            for word in sentence.words:
                print(
                    f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}')

            print("\n")

    def is_simple_predicate(self, sentence):
        tree = sentence.constituency
        # print(tree)
        # Check to make sure node is a sentence
        if(tree.children[0].label != 'S'):
            print("Not a sentence")
            return False
        tree_labels = tree.children[0].children
        correct_labels = ['NP', 'VP', '.']
        # check to make sure sentence node only has 3 children
        if (len(tree_labels) != 3):
            print("Not 3 childrne")
            print(tree)
            return False
        for i in range(3):
            if tree_labels[i].label != correct_labels[i]:
                return False
        return True

    def find_viable_questions_sentences(self):
        viable_question_sentences = []

        def find_appositions(sentence):
            apposition_sentences = []
            to_be_conjugations_xpos = {'NN': 'is',
                                       'NNS': 'are', 'NNP': 'is', 'NNPS': 'are', 'EX': 'is'}
            to_be_conjugations_pronouns = {
                'i': 'am', 'you': 'are', 'he': 'is', 'she': 'is', 'it': 'is', 'we': 'are', 'they': 'are'}
            for word in sentence.words:
                if word.deprel == 'appos':
                    word_head = sentence.words[word.head - 1]
                    appos_sentence = ''
                    to_be = ''
                    if word_head.xpos in to_be_conjugations_xpos:
                        to_be = to_be_conjugations_xpos[word_head.xpos]
                    else:
                        to_be = to_be_conjugations_pronouns[word_head.text.lower(
                        )]

                    appos_sentence = word_head.text.capitalize() + ' ' + to_be + \
                        ' ' + word.text + '.'
                    appos_sentence_processed = self.nlp(appos_sentence)
                    apposition_sentences.append(
                        appos_sentence_processed.sentences[0])
            return apposition_sentences

        for sentence in self.sentences:
            if(self.is_simple_predicate(sentence)):
                print("VALID")
                print(sentence.text)
                viable_question_sentences.append(sentence)
            else:
                print("INVALID")
                print(sentence.constituency)
                print(sentence.text)
                # viable_question_sentences.extend(find_appositions(sentence))
        return viable_question_sentences


# kangaroo_f = open(
#     '/Users/Rahjshiba/Question_Answer_Dataset_v1.2 2/S08/data/set1/a1.txt')
kangaroo_f = open('text/pie2.txt')
kangaroo_text = kangaroo_f.read()
# print(kangaroo_text)
kangaroo_f.close()

kangaroo_parser = DocumentParser(kangaroo_text)
# print(kangaroo_parser.sentences)
# viable_sentences = kangaroo_parser.find_viable_questions_sentences()
# print("Valids")
# for x in viable_sentences:
#     print(x.text)
#     print(x.constituency)


nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,constituency')
doc = nlp('This is a test. The cow is red')
for i, sentence in enumerate(doc.sentences):
    print(i)
    print(sentence.text)
    print(sentence.parseTree)
    print(sentence.constituency.children[0].children)
