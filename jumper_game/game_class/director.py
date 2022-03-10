# director Class 
# imports 
from game_class.word import Word
from game_class.terminal_service import TerminalService
from game_class.jumper import Jumper

class Director:

    def __init__(self):
        self._is_playing = True
        self._word = Word()
        self._jumper = Jumper()
        self._terminal = TerminalService()
        self._guess_letter = ''


    def game_loop(self):
        self.do_outputs()
        while (self._jumper._is_alive == True) and (self._word.check_completion() == False):
            self.get_input()
            self.do_updates()
            self.do_outputs()
    

    def get_input(self):
        self.guess_letter = self._terminal.get_letter_guess()    

    def do_updates(self):
        if self._word.check_letter(self.guess_letter) == True:
            self._word.add_correct_letter(self.guess_letter)
        else: 
            self._jumper.remove_line()
    
    def do_outputs(self):
        self._terminal.print_word(self._word._guessed_word_list)
        print()
        parachute, jumper = self._jumper.return_jumper()
        self._terminal.display_jumper(parachute, jumper)


