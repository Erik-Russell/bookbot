from stats import get_num_words
from stats import get_char_count
from stats import sort_char_count
import time
import sys

if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Exit with non-zero indicated error

book_path = sys.argv[1]

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text(book_path)
    char_dict = get_char_count(book_text)

    print("============ BOOKBOT ============")
    time.sleep(0.1)
    print(f"Analyzing book found at {book_path}...")
    time.sleep(0.1)
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    time.sleep(0.1)
    print("--------- Character Count -------")
    time.sleep(0.1)
    sort_char_count(char_dict)
    print("============= END ===============")
if __name__ == "__main__":
    main()
