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


    def game_loop(self):
        self.do_outputs()
        while self.is_playing:
            self.get_input()
            self.do_updates()
            self.do_outputs()
    

    def get_input(self):
        pass
    

    def do_updates(self):
        pass
    

    def do_outputs(self):
        pass