def get_num_words(book_text):
    number_of_words = 0
    list_of_words = book_text.split()
    for word in list_of_words:
        number_of_words += 1
    return number_of_words

def get_num_characters(book_text):
    number_of_characters = {}
    book_text = book_text.lower()
    character_list = list(book_text)
    for character in character_list:
        if character in number_of_characters:
            number_of_characters[character] += 1
        else:
            number_of_characters.update({character: 1})
    return number_of_characters

def sort_on(items):
    return items["num"]

def sort_dictionary(book_dictionary):
    sorted_list = []
    for ch, n in book_dictionary.items():
        sorted_list.append({"char": ch, "num": n})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list