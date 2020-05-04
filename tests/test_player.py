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

    def test_getguesses(self):
        """
        getguesses returns player.guesses
        """

        self.assertIsInstance(self.player.getguesses(), list)
        self.assertEqual(self.player.getguesses(), [])

    def test_isalive(self):
        """
        1. isalive returns True if player.health.health > 0
        2. isalive returns False if player.health.health == 0
        3. isalive returns False if player.health.health < 0
        """

        # 1.
        while self.player.health.gethealth() > 0:
            self.assertTrue(self.player.isalive())
            self.player.health.sethealth()

        # 2.
        self.assertFalse(self.player.isalive())

        # 3.
        self.player.health.sethealth()
        self.assertFalse(self.player.isalive())

