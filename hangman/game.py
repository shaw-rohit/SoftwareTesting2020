import random
import time
from hangman.words import words
from hangman.guess import Guess


class Game:
    def __init__(self, player, interface):
        self.player    = player
        self.interface = interface
        self.theme     = random.choice(list(words.keys()))
        self.word      = random.choice(words.get(self.theme)).upper()
        self.hint      = "_" * len(self.word)
        self.hist      = self.create_hist()

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
        while self.player.isalive():
            self.print_graphics()
            guess = Guess(self.interface.read_player_guess())

            if not guess.isvalid():
                self.interface.write_invalid_guess()

            elif guess.isguessed(self.player.getguesses()):
                self.interface.write_already_guessed()

            elif not guess.iscorrect(self.word):
                self.player.setguesses(guess.getvalue())
                self.player.health.sethealth()
                self.interface.write_incorrect_guess(guess.getvalue(),
                        self.player.health.gethealth())

            else:
                self.interface.write_correct_guess()
                self.player.setguesses(guess.getvalue())
                self.sethint(guess.getvalue())

                if "_" not in self.hint:
                    self.won()
                    return

            time.sleep(0.5)

        self.lost()

    def lost(self):
        self.print_graphics()
        self.interface.write_lost(self.word)

    def won(self):
        self.print_graphics()
        self.interface.write_won(self.word)

    def sethint(self, guess):
        for index in self.hist[guess]:
            self.hint = self.hint[:index] + guess + self.hint[index + 1 :]

    def print_graphics(self):
        self.interface.clear_screen()
        self.interface.ins_newline()
        self.interface.draw_hangman(self.player.health.gethealth())
        self.interface.ins_newline()
        self.interface.write_hint(self.hint, self.theme)
        self.interface.write_health(self.player.health.gethealth())
        self.interface.write_guessed_letters(self.player.getguesses())
