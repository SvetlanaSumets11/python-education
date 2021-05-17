"""This module contains the basic functions for the Hangman game"""
from random import choice


words = ['account', 'baboon', 'badger', 'change', 'camel', 'learning',
         'shellfish', 'cobra', 'servant', 'nature', 'expansion', 'donkey', 'animal',
         'eagle', 'ferret', 'insurance', 'measure', 'human', 'lizard', 'monkey',
         'engineer', 'otter', 'feeling', 'panda', 'parrot', 'summer', 'python',
         'rabbit', 'respect', 'blouse', 'rhino', 'salmon', 'shark', 'snake', 'spider',
         'waterfall', 'tiger', 'trout', 'turkey', 'turtle', 'weasel', 'zebra']


random_word = choice


def correct_letter(correct_letters_in_word, input_letter, word):
    """This function modifies the list of guessed letters based on the entered letter"""
    indices = [item for item, let in enumerate(word) if let == input_letter]
    for item in indices:
        correct_letters_in_word[item] = input_letter
    return correct_letters_in_word


def missed_letters(missed_letters_in_word, input_letter):
    """This function modifies the list of invalid letters based on the entered letter"""
    missed_letters_in_word.append(input_letter)
    return missed_letters_in_word


def word_is_guessed(correct_letters_in_word, word):
    """This function determines if a word is guessed"""
    return all(letter in correct_letters_in_word for letter in word)


def game_is_done(correct_letters_in_word, word, guessed_words):
    """This function determines if the game is over,
    modifies the list of guessed words by adding the current word to it"""
    if word_is_guessed(correct_letters_in_word, word):
        guessed_words.append(''.join(word))
        return True
    return False


def attempts_ended(missed_letters_in_word, attempts):
    """This function determines if possible attempts to guess the letter have been exhausted"""
    return len(missed_letters_in_word) == attempts
