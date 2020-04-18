from hangman.health import Health

class Player:
    def __init__(self):
        self.health        = Health()
        self.guesses       = []

    def setguesses(self, guess):
        self.guesses.append(guess)
