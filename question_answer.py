import stanza
from document_parser import DocumentParser


def load_text(filename):
    with open(filename) as textFile:
        text = textFile.read()
        parser = DocumentParser(text)
        parser.print_token_data()


load_text("text/pie.txt")
