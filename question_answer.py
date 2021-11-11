import stanza
from document_parser import DocumentParser

nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')


def load_text(filename):
    with open(filename) as textFile:
        text = textFile.read()
        parser = DocumentParser(text)
        parser.print_token_data()

# if possible return question, if not return None


# fiona
def who(sentence):
    return

# seth


def what(sentence):
    return

# seth


def when(sentence):
    return

# rahjshiba


def howmany(sentence):
    question = "How many"
    nsubj_head = 0
    for word in sentence.words:
        if word.head == 0:
            nsubj_head = word.id - 1
            break

    subject = sentence.words[0:nsubj_head]
    predicate = sentence.words[nsubj_head:]

    (sub_nummod_i, pred_nummod_i) = is_howmany(subject, predicate)

    if (sub_nummod_i, pred_nummod_i) == (None, None):
        return None
    elif pred_nummod_i == None:
        phrase_start = sentence.words[sub_nummod_i].head - 1
        for word in sentence.words[phrase_start:len(sentence.words) - 1]:
            question = question + " " + word.text.lower()
    elif sub_nummod_i == None:
        phrase_start = sentence.words[pred_nummod_i].head - 1
        how_many_noun = sentence.words[phrase_start]
        question = question + " " + how_many_noun.text
        question = question + " " + expl_does_question_phrase(subject, sentence.words[nsubj_head])
        for word in sentence.words[phrase_start + 1: len(sentence.words) -1]:
            question = question + " " + word.text.lower()
    question += '?'
    return question

def expl_does_question_phrase(subject, verb):
    has_expl = None
    conjugated_do = None
    flipped_verb_phrase = ''

    for word in subject:
        if word.deprel == 'expl':
            has_expl = word
            break

    for word in subject:
        if word.xpos == 'PRP':
            if word.text.lower() in ['it','he','she']:
                conjugated_do = 'does'
                break
            elif word.text.lower() in ['i', 'you', 'we', 'they']:
               conjugated_do = 'do'
               break
        elif word.xpos == 'NNP':
            conjugated_do = 'does'
            break
        elif word.xpos == 'NNS':
            conjugated_do = 'do'
            break
        elif word.xpos == 'NN':
            conjugated_do = 'does'
            break
        
    if has_expl != None:
        flipped_verb_phrase = verb.text.lower() + " " + has_expl.text.lower()
    else:
        flipped_verb_phrase = conjugated_do + " "
        for word in subject:
            flipped_verb_phrase = flipped_verb_phrase + word.text.lower() + " "
        
        flipped_verb_phrase += verb.lemma
    return flipped_verb_phrase


def is_howmany(subject, predicate):
    (sub_i, pred_i) = (None, None)
    for word in subject:
        if word.deprel == 'nummod':
            sub_i = word.id - 1
    for word in predicate:
        if word.deprel == 'nummod':
            pred_i = word.id - 1
    return (sub_i, pred_i)



# celestine
def yesno(sentence):
    return


load_text("text/pie.txt")


howmany1 = nlp('Five dogs walk.')
howmany2 = nlp('He has five kids at the house.')
howmany3 = nlp('There are 7 apples.')
howmany4 = nlp('The tall trees laying in the sun have 6 apples.')
howmany5 = nlp('it remains one of the 88 modern constellations today.')
howmany6 = nlp('They have 3 cats.')
howmany7 = nlp('Harriet is walking 3 dogs.')
howmany8 = nlp('You swim 6 miles.')
howmany9 = nlp('The tall trees which they were climbing had 6 apples.')
howmany10 = nlp('The tall tree covered in spiders had 6 apples.')




print(howmany(howmany1.sentences[0]))
print(howmany(howmany2.sentences[0]))
print(howmany(howmany3.sentences[0]))
print(howmany(howmany4.sentences[0]))
print(howmany(howmany5.sentences[0]))
print(howmany(howmany6.sentences[0]))
print(howmany(howmany7.sentences[0]))
print(howmany(howmany8.sentences[0]))
print(howmany(howmany9.sentences[0]))
print(howmany(howmany10.sentences[0]))
