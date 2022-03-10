# Jumper Class

class Jumper:

    def __init__(self):
        self._is_alive = True
        self._parachute = [" ___", "/___\\", "\\   /", " \\ /"]
        self._live_jumper = """  0
 /|\\
 / \\

^^^^^^^
"""
        self._dead_jumper = """  X
 /|\\
 / \\

^^^^^^^
""" 


    def return_jumper(self):
        if self._is_alive:
            return self._parachute, self._live_jumper
        else:
            return self._parachute, self._dead_jumper
    

    def remove_line(self):
        self._parachute.pop(0)
        if len(self._parachute) == 0:
            self.is_alive = False