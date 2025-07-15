# This takes the user path found in [main.py] and converts it into a string. 
def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

# Returns the length of the txt for the total work count. 
def word_count(words):
    return len(words)

# Adds each individual char to a dictionary and adds the count of it. Ex. {char, count}, etc
def char_count(chars):
    char_dict = {}
    for char in chars:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

# Key for the sort function necessary to make the chars in order of largest to smallest amount. 
def sort_key(list):
    return list["count"]

# Converts the chars in {chars_dict} to individual dictionaries in a list, then ignores the non-alphabetic characters and sorts them from largest to smallest count. 
def sort_char_count(chars):
    char_dict = char_count(chars)
    char_dict_list = []
    for char in char_dict:
        if char.isalpha() == True:
            char_dict_list.append({"char": char, "count": char_dict[char]})
    char_dict_list.sort(reverse=True, key=sort_key)
    return char_dict_list
