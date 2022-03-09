class TerminalService:
    def print_word(self, word_list):
        for letter in word_list:
            print(letter, end = ' ')

    def display_jumper(self, parachute, jumper):
        for piece in parachute:
            print(piece)
        print(jumper)
    
    def get_letter_guess(self):
        letter = input('Guess a letter [a-z]: ')
        return letter



