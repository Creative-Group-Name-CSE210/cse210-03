# Word class

import random

class Word:

    def __init__(self):
        self._list_of_words = ["letter", "word", "manley", "idaho", "classes", "nerd", "python", "sleep"]
        self._chosen_word = self._list_of_words[random.randint(0, len(self._list_of_words) - 1)]
        self._chosen_word_list = []
        self._guessed_word_list = []
        for letter in self._chosen_word:
            self._chosen_word_list.append(letter)
            self._guessed_word_list.append("_")
    

    def add_correct_letter(self, new_letter):
        counter = 0
        for old_letter in self._chosen_word_list:
            if old_letter == new_letter:
                self._guessed_word_list[counter] = new_letter
                self._chosen_word_list[counter] = "_"
            counter += 1
    

    def check_letter(self, new_letter):
        for old_letter in self._chosen_word_list:
            if old_letter == new_letter:
                return True
        return False

    def check_completion(self):
        counter = 0
        for letter in self._guessed_word_list:
            if letter != '_':
                counter += 1
        if counter == len(self._guessed_word_list):
            return True
        else:
            return False