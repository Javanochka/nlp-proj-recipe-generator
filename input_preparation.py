from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


def tag_the_pos(_text):
    """Perform word tokenizing POS-tagging unto a given text."""

    words = word_tokenize(_text)
    return pos_tag(words)

# TODO: Function using [X] to identify and separate list elements
# # Universal Dependencies?

# TODO: Implement the English Ambiguities removal.
# # exec(english_ambiguities) & call its main function.

def prepare_input(_text):
    """Perform the input preparation: sanitizing, formatting"""
    text = _text
    pos_tagged = tag_the_pos(_text)
    return text


def prepare_prompted_input():
    return prepare_input(input("Enter the list of recipes"))
