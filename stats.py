def get_num_words(f):
    num_words = len(f.split())
    return num_words

def get_num_chars(f):
    char_dict = {}

    for char in f.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:  
            char_dict[char] += 1

    return char_dict

def sort_on(char_dict):
    filtered_dict = {}
    for key, value in char_dict.items():
        if key.isalpha():
            filtered_dict[key] = value

    items = list(filtered_dict.items())
    items.sort(reverse=True, key=lambda item: item[1])

    output = [f"{char}: {count}" for char, count in items]
    return output
    
