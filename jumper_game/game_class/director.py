# director Class 
# imports 
from game_class.word import Word
from game_class.terminal_service import TerminalService
from game_class.jumper import Jumper

class Director:

    def __init__(self):
        self.is_playing = True
        self.word = Word()
        self.jumper = Jumper()
        self.terminal = TerminalService()
        self.guess_letter = ''


    def game_loop(self):
        self.do_outputs()
        while self.is_alive:
            self.get_input()
            self.do_updates()
            self.do_outputs()
    

    def get_input(self):
        pass
    

    def do_updates(self):
        if self.word.check_letter(self.guess_letter) == True:
            self.word.add_correct_letter(self.guess_letter)
        else: 
            self.jumper.remove_line()
    
    def do_outputs(self):
        print(Word)
        print(Jumper)
