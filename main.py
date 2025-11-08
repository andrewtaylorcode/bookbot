from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")
main()

