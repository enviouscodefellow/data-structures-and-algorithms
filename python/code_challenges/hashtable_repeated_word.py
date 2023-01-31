import re

def first_repeated_word(string):

    words = re.findall(r'\b\w+\b', re.sub(r'[^\w\s]', '', string).lower())

    word_list = []
    for word in words:
        if word in word_list:
            return word
        word_list.append(word)
    return None
