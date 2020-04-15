import unittest
from hangman import pick_word

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        word = pick_word()
        self.assertTrue(word.upper())

if __name__ == '__main__':
    unittest.main()
