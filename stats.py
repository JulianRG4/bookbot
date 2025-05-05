def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
    return file_contents


def count_book_words(file):
    word_count = file.split()
    words = len(word_count)
    return words

def count_book_char(file):
    char_count = {}
    lower_case_char = file.lower()
    for char in lower_case_char:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sorted_char_dictionary(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_dict = {"char": char, "num": count}
            char_list.append(char_dict)
    char_list.sort(reverse=True, key=lambda x:x["num"])
    return char_list
   