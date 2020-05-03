from .context import hangman
from hangman.player import Player
from unittest import TestCase

class TestPlayer(TestCase):
    """
    Unit tests for Player class.
    """

    def setUp(self):
        self.player = Player()

    def test_setguesses(self):
        """
        1. setguesses adds given guess to self.guesses when it is empty.
        2. setguesses adds given guess to self.guesses when it is not empty.
        """

        # 1.
        self.player.setguesses('A')
        self.assertEqual(self.player.guesses, ['A'])

        # 2.
        self.player.setguesses('A')
        self.assertEqual(self.player.guesses, ['A', 'A'])
