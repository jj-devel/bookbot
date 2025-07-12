from stats import get_book_text, path_to_book, word_count, char_count, sort_char_count

def main():
    book_text = get_book_text(path_to_book)
    num_words = word_count()
    num_chars = char_count()
    sorted_num_chars = sort_char_count()
    printed_word_count = print(f"{num_words} words found in the document")
    # Don't know if this works yet, doubt it ;). 
    for char in sorted_num_chars:
        if char.isalpha() == True:
            print(sorted_num_chars(char))

main()
