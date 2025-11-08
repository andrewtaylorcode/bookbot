from stats import get_num_words
from stats import get_num_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")
    num_of_characters = get_num_characters(get_book_text("books/frankenstein.txt"))
    print(num_of_characters)

main()

