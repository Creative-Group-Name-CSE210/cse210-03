# Word class

import random

class Word:

    def __init__(self):
        self._list_of_words = ["letter"]
        self.chosen_word = self._list_of_words[random.randint(0, len(self._list_of_words) - 1)]
        self.chosen_word_list = []
        self.guessed_word_list = []
        for letter in self.chosen_word:
            self.chosen_word_list.append(letter)
            self.guessed_word_list.append("_")
    

    def add_correct_letter(self, new_letter):
        counter = 0
        for old_letter in self.chosen_word_list:
            if old_letter == new_letter:
                self.guessed_word_list[counter] = new_letter
                self.chosen_word_list[counter] = "_"
            counter += 1
    

    def check_letter(self, new_letter):
        for old_letter in self.chosen_word_list:
            if old_letter == new_letter:
                return True
        return False

    def check_completion(self):
        for letter in self.guessed_word_list:
            if letter != '-':
                return False
        return True
