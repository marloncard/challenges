from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    a_list = []
    with open('dictionary.txt') as dict:
        for word in dict:
            a_list.append(word[:-1])
        return a_list

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        for l, s in LETTER_SCORES.items():
            if letter.upper() == l:
                score += s
    return score

def max_word_value(*args):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_word = ""
    if args:
        if type(args[0])==tuple or type(args[0])==list:
            for word in args[0]:
                if calc_word_value(word) > calc_word_value(max_word):
                    max_word = word
        else:
            for word in args:
                if calc_word_value(word) > calc_word_value(max_word):
                    max_word = word
    else:
        for word in load_words():
            if calc_word_value(word) > calc_word_value(max_word):
                max_word = word
    return max_word

if __name__ == "__main__":
    pass # run unittests to validate
