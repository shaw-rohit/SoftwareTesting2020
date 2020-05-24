from .context import hangman
from hangman.health import Health
from unittest import TestCase
from unittest.mock import Mock

class TestHealth(TestCase):
    """
    Unit tests for Health class.
    """

    def setUp(self):
        self.health = Health()

    def test_sethealth(self):
        """
        1. sethealth returns 8 (= 9-1) when called for the first time since creation of Health instance
        2. When sethealth has been called 8 times since health instance creation, the remaining health will be 1.
        3. When sethealth has been called 9 times (the initial health) since health instance creation, the remaining health will be 0.
        4. sethealth can continue to decrease health beyond 0.
        5. sethealth can be customized to decrease health by 2 instead of 1: if called once since health instance creation, the remaining health will be 7.
        6. sethealth can be customized to decrease health by 3 instead of 1: if called three times since health instance creation, the remaining health will be 0.
        """

        #1
        self.health.sethealth()
        self.assertEqual(self.health.health, 8)

        #2
        self.setUp()
        wrong_guesses = 8
        for wrong_guess in range(wrong_guesses):
            self.health.sethealth()
        self.assertEqual(self.health.health, 1)

        #3
        self.setUp()
        wrong_guesses = 9
        for wrong_guess in range(wrong_guesses):
            self.health.sethealth()
        self.assertEqual(self.health.health, 0)

        #4
        self.setUp()
        wrong_guesses = 10
        for wrong_guess in range(wrong_guesses):
            self.health.sethealth()
        self.assertLess(self.health.health, 0)

        #5
        self.setUp()
        self.health.sethealth(2)
        self.assertEqual(self.health.health, 7)

        #6
        self.setUp()
        wrong_guesses = 3
        for wrong_guess in range(wrong_guesses):
            self.health.sethealth(3)
        self.assertEqual(self.health.health, 0)

    def test_gethealth(self):
        """
        1. gethealth returns 9 (initial health) when health has not been changed.
        2. gethealth returns 1 when remaining health is 1.
        3. gethealth returns 0 when remaining health is 0.
        """

        #1
        self.assertEqual(self.health.gethealth(), 9)

        #2
        self.health.health = Mock(return_value=1)
        self.assertEqual(self.health.health, self.health.gethealth())

        #3
        self.health.health = Mock(return_value=0)
        self.assertEqual(self.health.health, self.health.gethealth())