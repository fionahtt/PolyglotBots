import stanza
from document_parser import DocumentParser


def load_text(filename):
    with open(filename) as textFile:
        text = textFile.read()
        parser = DocumentParser(text)
        parser.print_token_data()

#if possible return question, if not return None


#fiona
def who(sentence):
    return

#seth
def what(sentence):
    return

#seth
def when(sentence):
    return

#rahjshiba
def howmany(sentence):
    return

#celestine
def yesno(sentence):
    return


load_text("text/pie.txt")
