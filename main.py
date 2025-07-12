import sys
from stats import get_book_text, word_count, char_count, sort_char_count

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]

def main():
    words = get_book_text(path_to_book).split()
    chars_list = list(get_book_text(path_to_book))
    chars = [char.lower() for char in chars_list]

    num_words = word_count(words)
    sorted_char_list = sort_char_count(chars)
    print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...\n
----------- Word Count ----------
Found {num_words} total words\n
--------- Character Count -------
          """)
    for i in range(0, len(sorted_char_list)):
        print(f"{sorted_char_list[i]["char"]}: {sorted_char_list[i]["count"]}")
    print("============= END ===============")

main()
