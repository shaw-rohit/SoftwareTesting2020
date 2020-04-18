import random
from hangman.words import cities

class Game:
    def __init__(self, player, interface):
        self.player    = player
        self.interface = interface
        self.word      = random.choice(cities).upper()
        self.hint      = "_" * len(self.word)
        self.hist      = self.create_hist()
        self.guessed   = False

    def create_hist(self):
        hist = {}
        for index, letter in enumerate(self.word):
            if letter in hist.keys():
                hist[letter].append(index)
            else:
                hist[letter] = []
                hist[letter].append(index)

        return hist

    def start(self):
        while not self.guessed and self.player.health.gethealth() > 0:
            self.interface.clear()
            self.interface.write_hint(self.hint)
            self.interface.write_health(self.player.health.gethealth())
            self.interface.write_guessed_letters(self.player.guesses)
            guess = self.interface.read_player_guess()

            if(len(guess) == 1 and guess.isalpha()):
                if guess in self.player.guesses:
                    self.interface.write_already_guessed()
                elif guess not in self.word:
                    self.interface.write_incorrect_guess(guess)
                    self.player.setguesses(guess)
                    self.player.health.sethealth()
                else:
                    self.interface.write_correct_guess()
                    self.player.setguesses(guess)
                    self.sethint(guess)
                    if "_" not in self.hint: self.guessed = True
            else:
                self.interface.write_invalid_guess()

        if self.guessed:
            self.interface.write_won()
        else:
            self.interface.write_lost(self.word)

    def end(self):
        pass

    def restart(self):
        pass

    def sethint(self, guess):
        for index in self.hist[guess]:
            self.hint = self.hint[:index] + guess + self.hint[index+1:]
