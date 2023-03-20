import random

class Hangman:
  def __init__(self, word_list, num_lives = 5):
    self.word = word
    self.word_guessed = ['_'] * len(word)
    self.num_letters = len(set(word))
    self.num_lives = num_lives
    self.word_list = word_list
    self.list_of_guesses = list_of_guesses
