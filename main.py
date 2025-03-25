"""
def get_book_text(filepath):
    with open(filepath) as f:
        document_text = f.read()
    #print(document_text)
    return document_text

def count_words(document_string):
    list_of_words = document_string.split()
    num_words = len(list_of_words)
    print(f"{num_words} words found in the document")
"""

from stats import get_book_text, count_words, count_character

def main():
    document_text = get_book_text("books/frankenstein.txt")
    count_words(document_text)
    count_character(document_text)
    return



main()

