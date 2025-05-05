def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
    return file_contents


def count_book_words(file):
    word_count = file.split()
    words = len(word_count)
    return words