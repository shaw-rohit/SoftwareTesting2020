import unittest
import hangman 
from hangman import hangman_algorithm

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        word = hangman.hangman_pick_word()
        self.assertTrue(word.upper())
        # return word

    def test_no_of_dashes(self):
        """
        The number of dashes generated must be equal to the length of the word
        """
        word = hangman.hangman_pick_word()
        dash_length = len(hangman.hangman_print_dashes(word))
        self.assertTrue(dash_length == len(word))

    def test_valid_user_guess(self):
        """
        The user must enter a valid character
        """
        user_guess = hangman.hangman_get_letter()
        self.assertTrue(user_guess.isalpha()) 

    def test_play_game(self):
        pass



if __name__ == '__main__':
    unittest.main()
