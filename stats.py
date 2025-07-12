def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def word_count(words):
    return len(words)

def char_count(chars):
    char_dict = {}
    for char in chars:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_key(list):
    return list["count"]

def sort_char_count(chars):
    char_dict = char_count(chars)
    char_dict_list = []
    for char in char_dict:
        if char.isalpha() == True:
            char_dict_list.append({"char": char, "count": char_dict[char]})
    char_dict_list.sort(reverse=True, key=sort_key)
    return char_dict_list
