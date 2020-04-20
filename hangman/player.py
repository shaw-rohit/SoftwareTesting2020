from hangman.health import Health

class Player:
    def __init__(self):
        self.health        = Health()
        self.guesses       = set()

    def setguesses(self, guess):
        self.guesses.add(guess)
