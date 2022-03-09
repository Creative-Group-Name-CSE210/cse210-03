# Jumper Class

class Jumper:

    def __init__(self):
        self.is_alive = True
        self.parachute = [" ___", "/___\\", "\\   /", " \\ /"]
        self.live_jumper = """  0
 /|\\
 / \\

^^^^^^^
"""
        self.dead_jumper = """  X
 /|\\
 / \\

^^^^^^^
""" 


    def return_jumper(self):
        if self.is_alive:
            return self.parachute, self.live_jumper
        else:
            return self.parachute, self.dead_jumper
    

    def remove_line(self):
        self.parachute.pop(0)
        if len(self.parachute) == 0:
            self.is_alive = False