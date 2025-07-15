import sys
from stats import get_book_text, word_count, sort_char_count

# Set a startup condition where the program needs two arguments to continue. 
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Set the txt used for bookbot to the path given by the user in the second system argument. 
path_to_book = sys.argv[1]

# Main function that holds the actions for bookbot. 
def main():
    # Necessary variables for the functions in stats to work. 
    words = get_book_text(path_to_book).split()
    chars_list = list(get_book_text(path_to_book))
    chars = [char.lower() for char in chars_list]

    # Variables holding the stats functions
    num_words = word_count(words)
    sorted_char_list = sort_char_count(chars)

    # Print the intro to bookbot, along with the {num_words} variable. 
    print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...\n
----------- Word Count ----------
Found {num_words} total words\n
--------- Character Count -------
          """)
    
    # Print each character found in the txt, with the corisponding amount of the character found in the txt. Ordered from most to least. 
    for i in range(0, len(sorted_char_list)):
        print(f"{sorted_char_list[i]["char"]}: {sorted_char_list[i]["count"]}")
    print("============= END ===============")

# Run the main function. 
main()
