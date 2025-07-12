path_to_book = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text


words = get_book_text(path_to_book).split()
chars_list = list(get_book_text(path_to_book))
chars = [char.lower() for char in chars_list]

def word_count():
    return len(words)

def char_count():
    char_dict = {}
    for char in chars:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

# NEEDS FIXED! 
def sort_char_count():
    char_dict_list = []
    char_dict = char_count()
    for char in chars:
        dict_template = {"char": "", "count": 0}
        dict_template["char"] = char
        dict_template["count"] = char_dict[char]
        char_dict_list.append(dict_template)
    char_dict_list.sort(reverse=True, key=char_dict)
    return char_dict_list
    
