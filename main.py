import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = get_num_words(get_book_text(sys.argv[1]))
    print(f"Found {num_words} total words")
    num_of_characters = get_num_characters(get_book_text(sys.argv[1]))
    sorted_dictionary = sort_dictionary(num_of_characters)
    for i in sorted_dictionary:
        char = i["char"]
        num = i["num"]
        if char.isalpha():
            print(f"{char}: {num}")

main()

