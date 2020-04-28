from .context import hangman
from hangman.game import Game
from hangman.player import Player
from hangman.interface import Interface
from hangman.words import words
from unittest import TestCase

class GameTest(TestCase):
    """
    Unit tests for the Game class.
    """

    def setUp(self):
        interface      = Interface()
        player         = Player()
        self.game      = Game(player, interface)
        self.game.word = "FOOBAR"
        self.game.hist = self.game.create_hist()

    def test_create_hist(self):
        """
        create_hist creates histogram of self.word during
        instantiation of Game.
        1. test if game.hist is created
        2. test if histogram is created correctly based on game.word

        """
        keys = ["F", "O", "B", "A", "R"]

        self.assertIsInstance(self.game.hist, dict)
        self.assertEqual(keys, list(self.game.hist.keys()))
        self.assertEqual(len(self.game.hist["O"]), 2)
        self.assertEqual(len(self.game.hist["B"]), 1)
