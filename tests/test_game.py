from .context import hangman
from hangman.game import Game
from hangman.player import Player
from hangman.interface import Interface
from hangman.words import words
from unittest import TestCase
from unittest.mock import Mock

class TestGame(TestCase):
    """
    Unit tests for the Game class.
    """

    def setUp(self):
        interface                                 = Interface()
        player                                    = Player()
        self.game                                 = Game(player, interface)
        self.game.print_graphics                  = Mock(return_value=None)
        self.game.interface.write_invalid_guess   = Mock(return_value=None)
        self.game.interface.write_already_guessed = Mock(return_value=None)
        self.game.interface.write_incorrect_guess = Mock(return_value=None)
        self.game.interface.write_correct_guess   = Mock(return_value=None)
        self.game.won                             = Mock(return_value=None)
        self.game.lost                            = Mock(return_value=None)

    def test_create_hist(self):
        """
        1. hist exists
        2. hist.keys() contains all letters of words
        """

        self.assertIsInstance(self.game.hist, dict)
        self.assertTrue(len(self.game.hist.keys()) > 0)

    def test_start_scenario_1(self):
        """
        Scenario 1: All incorrect guesses

        1.1 player is asked to make a guess 9 times
        1.2 player health is 0 at the end of the game
        1.3 player guesses contains the expected letters at the end of the
            game
        1.4 player is informed that they lost at the end of the game
        1.5 player is informed their guess is wrong 9 times
        1.6 hint consists only of dashes at the end of the game
        """

        self.setUpStart()
        incorrect_guesses = ["Q", "W", "E", "T", "Y", "U", "I", "P", "S"]
        self.game.interface.read_player_guess = Mock(side_effect=incorrect_guesses)

        self.game.start()

        # 1.1
        self.assertEqual(self.game.interface.read_player_guess.call_count,
                len(incorrect_guesses))

        # 1.2
        self.assertEqual(self.game.player.health.gethealth(), 0)

        # 1.3
        self.assertEqual(self.game.player.getguesses(), incorrect_guesses)

        # 1.4
        self.game.lost.assert_called_once()

        # 1.5
        self.assertEqual(self.game.interface.write_incorrect_guess.call_count,
                len(incorrect_guesses))

        # 1.6
        self.assertEqual(self.game.hint, "______")

    def test_start_scenario_2(self):
        """
        Scenario 1: All correct guesses

        2.1 player is asked to make a guess 5 times
        2.2 player health is 9 at the end of the game
        2.3 player guesses contains the expected letters at the end of the
            game
        2.4 player is informed that they won at the end of the game
        2.5 player is informed their guess is correct 9 times
        2.6 hint consists of letters and no dashes at the end of the game
        """

        self.setUpStart()
        correct_guesses = ["F", "O", "B", "A", "R"]
        self.game.interface.read_player_guess = Mock(side_effect=correct_guesses)

        self.game.start()

        # 2.1
        self.assertEqual(self.game.interface.read_player_guess.call_count,
                len(correct_guesses))

        # 2.2
        self.assertEqual(self.game.player.health.gethealth(), 9)

        # 2.3
        self.assertEqual(self.game.player.getguesses(), correct_guesses)

        # 2.4
        self.game.won.assert_called_once()

        # 2.5
        self.assertEqual(self.game.interface.write_correct_guess.call_count,
                len(correct_guesses))

        # 2.6
        self.assertEqual(self.game.hint, "FOOBAR")

    def test_start_scenario_3(self):
        """
        Scenario 3: realistic gameplay, game won

        3.1 player is asked to make a guess until word is guessed correctly
        3.2 player health is reduced for each incorrect guess
        3.3 player health is not 0 at the end of the game
        3.4 player guesses contains the expected letters at the end of the
          game
        3.5 player is informed they won at the end of the game
        3.6 player is informed their guess is correct for each correct guess
        3.7 player is informed their guess is incorrect for each incorrect guess
        3.8 player is informed they already guessed the letter for each repeat
          guess
        3.9 hint consists only of dashes at the end of the game
        """

        self.setUpStart()
        player_guesses = ["A", "E", "I", "O", "U", "B", "O", "F", "S", "A", "R"]
        self.game.interface.read_player_guess = Mock(side_effect=player_guesses)

        self.game.start()

        # 3.1
        self.assertEqual(self.game.interface.read_player_guess.call_count,
                len(player_guesses))

        # 3.2 & 3.3
        self.assertEqual(self.game.player.health.gethealth(), 5)

        # 3.4
        end_player_guesses = ["A", "E", "I", "O", "U", "B", "F", "S", "R"]
        self.assertEqual(self.game.player.getguesses(), end_player_guesses)

        # 3.5
        self.game.won.assert_called_once()

        # 3.6
        self.assertEqual(self.game.interface.write_correct_guess.call_count, 5)

        # 3.7
        self.assertEqual(self.game.interface.write_incorrect_guess.call_count, 4)

        # 3.8
        self.assertEqual(self.game.interface.write_already_guessed.call_count, 2)

        # 3.9
        self.assertEqual(self.game.hint, "FOOBAR")

    def test_start_scenario_4(self):
        """
        Scenario 4: realistic gameplay, game lost

        4.1 player is asked to make a guess until they run out of health
        4.3 player health is 0 at the end of the game
        4.4 player guesses contains the expected letters at the end of the
          game
        4.5 player is informed they lost at the end of the game
        4.6 player is informed their guess is correct for each correct guess
        4.7 player is informed their guess is incorrect for each incorrect guess
        4.8 player is informed they already guessed the letter for each repeat
          guess
        4.9 hint consists of dashes and letters at the end of the game
        """

        self.setUpStart()
        player_guesses = ["X", "W", "T", "A", "E", "I", "O", "U", "B", "O",
                "F", "S", "A", "M", "N"]
        self.game.interface.read_player_guess = Mock(side_effect=player_guesses)

        self.game.start()

        # 4.1
        self.assertEqual(self.game.interface.read_player_guess.call_count,
                len(player_guesses))

        # 4.3
        self.assertEqual(self.game.player.health.gethealth(), 0)

        # 4.4
        end_player_guesses = ["X", "W", "T", "A", "E", "I", "O", "U", "B",
                "F", "S", "M", "N"]
        self.assertEqual(self.game.player.getguesses(), end_player_guesses)

        # 4.5
        self.game.lost.assert_called_once()

        # 3.6
        self.assertEqual(self.game.interface.write_correct_guess.call_count, 4)

        # 3.7
        self.assertEqual(self.game.interface.write_incorrect_guess.call_count, 9)

        # 3.8
        self.assertEqual(self.game.interface.write_already_guessed.call_count, 2)

        # 3.9
        self.assertEqual(self.game.hint, "FOOBA_")

    def setUpStart(self):
        mock_word = Mock(return_value="FOOBAR")
        self.game.word = mock_word()
        mock_word_hist = {"F": [0], "O": [1, 2], "B": [3], "A": [4], "R": [5]}
        mock_hist = Mock(return_value=mock_word_hist)
        self.game.hist = mock_hist()
        mock_word_hint = "_" * len(self.game.word)
        mock_hint = Mock(return_value=mock_word_hint)
        self.game.hint = mock_hint()
