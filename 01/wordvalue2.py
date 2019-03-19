# unittest Ran 3 tests in 0.676s
from data import DICTIONARY, LETTER_SCORES

def load_words():
    """ 'with' is safest way to open files because of built-in methods that
    automatically open and close; using a list comprehension allows us to strip
    whitespace"""
    with open(DICTIONARY) as l:
        return [word.strip() for word in l.read().split()]

def calc_word_value(word):
    """Dictionary method 'get' returns value of matching key, zero is specified
    as default if key is not found which accounts for nonexistant keys"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words=None):
    """'key' is a callable that returns a value used for sorting;
    the value of key should be a function that takes a single argument
    and returns a key for sorting purposes"""
    if words is None:
        words = load_words()
    return max(words, key=calc_word_value)


if __name__ == "__main__":
    pass # run unittests to validate
