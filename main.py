from stats import get_num_words
from stats import get_num_characters
from stats import sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")
    num_of_characters = get_num_characters(get_book_text("books/frankenstein.txt"))
    sorted_dictionary = sort_dictionary(num_of_characters)
    i = 0
    for j in sorted_dictionary:
        char = j["char"]
        num = j["num"]
        i += 1
        if char.isalpha():
            print(f"{char}: {num}")

main()

