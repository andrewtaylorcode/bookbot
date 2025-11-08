def get_num_words(book_text):
    number_of_words = 0
    list_of_words = book_text.split()
    for word in list_of_words:
        number_of_words += 1
    return number_of_words