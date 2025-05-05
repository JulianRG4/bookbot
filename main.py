from stats import get_book_text, count_book_words

def main():
    file_text = get_book_text("books/frankenstein.txt")
    num_words = count_book_words(file_text)
    print(f"{num_words} words found in the document")


if __name__ == "__main__":
    main()