import unittest
import hangman 

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        word = hangman.pick_word()
        self.assertTrue(word.upper())

    def test_no_of_dashes(self):
        word = hangman.pick_word()
        dash_length = hangman.hangman_game_display(word)
        self.assertTrue(dash_length == len(word))

    def test_valid_user_guess(self):
        user_guess = hangman.hangman_algorithm(self, self)
        self.assertTrue(user_guess.isalpha()) 

if __name__ == '__main__':
    unittest.main()
