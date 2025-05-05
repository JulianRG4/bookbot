from stats import get_book_text, count_book_words, count_book_char, sorted_char_dictionary
import sys

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    file_text = get_book_text(file_path)
    num_words = count_book_words(file_text)
    num_char = count_book_char(file_text)
    sorted_list = sorted_char_dictionary(num_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    
    for char_dict in sorted_list:
        char = char_dict["char"]
        count = char_dict["num"]
        print(f"{char}: {count}")
    
    print("============= END ===============")


if __name__ == "__main__":
    main() 