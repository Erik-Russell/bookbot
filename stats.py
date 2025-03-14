import time

def get_num_words(book):
    word_count = len(book.split())
    return word_count

def get_char_count(book):
    # convert all chars to lowercase
    chars = list(book.lower())

    dict_of_chars = dict.fromkeys(chars, 0)

    for char in chars:
        dict_of_chars[char] += 1

    return dict_of_chars

def sort_char_count(dictionary):
    sorted_by_value = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}

    for key, value in sorted_by_value.items():
        if key.isalpha():
            print(f"{key}: {value}")
            time.sleep(0.03)
