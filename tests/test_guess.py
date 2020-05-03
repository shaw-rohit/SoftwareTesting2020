from .context import hangman
from hangman.guess import Guess
from unittest import TestCase

class TestPlayer(TestCase):
    """
    Unit tests for Guess class.
    """

    def setUp(self):
        self.guess = Guess('A')

    def test_isvalid(self):
        """
        Test cases:
        1. isvalid returns False if len(value) is lesser than 1.
        2. isvalid returns False if len(value) is more than 1.
        3. isvalid returns False if value is numeric.
        4. isvalid returns False if value is symbol.
        5. FIXME isvalid returns False if value is not English alphabet.
        6. isvalid returns False if len(value) is 1 but value is not English
           alphabet.
        7. isvalid returns False if len(value) is not 1 and value is a English
           alphabet.
        8. isvalid returns True if len(value) is 1 and value is an English
           alphabet.

        Assumptions:
        1. guess is uppercase.
        2. value is uppercase.
        """

        invalid_guesses = ['', 'AA', '1', 'A12', '!', '{}']

        for guess in invalid_guesses:
            self.guess.value = guess
            self.assertFalse(self.guess.isvalid())

        self.guess.value = 'A'
        self.assertTrue(self.guess.isvalid())

    def test_isguessed(self):
        """
        1. isguessed returns False if len(guesses) is 0.
        2. isguessed returns False if value not in guesses.
        3. isguessed return True if value in guesses.

        Assumptions:
        1. guesses contains uppercase letters.
        2. value is uppercase.
        """

        self.assertFalse(self.guess.isguessed([]))
        self.assertFalse(self.guess.isguessed(['B']))
        self.assertFalse(self.guess.isguessed(['B', 'C']))
        self.assertTrue(self.guess.isguessed(['A']))
        self.assertTrue(self.guess.isguessed(['B', 'C', 'A']))

    def test_iscorrect(self):
        """
        1. iscorrect returns False if len(word) is 0.
        2. iscorrect returns False if value not in word.
        3. iscorrect returns True if value occurs in word once.
        3. iscorrect returns True if value occurs in word multiple times.

        Assumptions:
        1. word is uppercase.
        2. value is uppercase.
        """

        self.assertFalse(self.guess.iscorrect(''))
        self.assertFalse(self.guess.iscorrect('FOO'))

        self.guess.value = 'F'
        self.assertTrue(self.guess.iscorrect('FOO'))

        self.guess.value = 'O'
        self.assertTrue(self.guess.iscorrect('FOO'))



