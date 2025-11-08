def get_number_of_words(book_text):
    number_of_words = 0
    list_of_words = book_text.split()
    for word in list_of_words:
        number_of_words += 1
    return number_of_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    num_words = get_number_of_words(get_book_text("books/frankenstein.txt"))
    print(f"Foudn {num_words} total words")
main()

