from hangman.game import Game
from hangman.interface import Interface
from hangman.player import Player

if __name__ == "__main__":
    interface = Interface()
    interface.write_credits()

    replay = "Y"

    while replay[0].upper() == "Y":
        player = Player()
        game = Game(player, interface)
        game.start()
        replay = interface.read_replay()
