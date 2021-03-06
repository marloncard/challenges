#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random
import string

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return "".join([random.choice(string.ascii_uppercase) for n in range(NUM_LETTERS)])


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    while True:
        word = input("Enter word: ")
        try:
            _validation(word, draw)
            return word
        except ValueError:
            continue


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    for l in word:
        if l.upper() not in draw:
            print("Invalid letter: " + l)
            raise ValueError
    if word not in DICTIONARY:
        print("Invalid word: " + word)
        raise ValueError


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    """
    possible_words = []
    for word in _get_permutations_draw(draw):
        if word in DICTIONARY:
            possible_words.append(word)
    """
    s1 = set("".join(i).lower() for i in _get_permutations_draw(draw))
    s2 = set(DICTIONARY)
    return list(s1.intersection(s2))


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    permu_list = []
    for n in range(1, NUM_LETTERS+1):
        permu_list.extend(itertools.permutations(draw, n))
    return permu_list


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
