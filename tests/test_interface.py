import os
import sys
from io import StringIO
from .context import hangman
from hangman.interface import Interface


def test_read_player_guess(monkeypatch):
    """
    Data integrity test to check for upper case conversion of input
    """
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": "M")
        interface = Interface()
        assert interface.read_player_guess().isupper()

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": "m")
        interface = Interface()
        assert interface.read_player_guess().isupper()

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": "mm")
        interface = Interface()
        assert interface.read_player_guess().isupper()

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": "1")
        interface = Interface()
        assert not interface.read_player_guess().isupper()

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": "@")
        interface = Interface()
        assert not interface.read_player_guess().isupper()

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": " ")
        interface = Interface()
        assert not interface.read_player_guess().isupper()

    def test_read_replay(monkeypatch):
        """
        Input validation/Data validation test to check replay input is upper
        case and is the first letter of the input
        """
        REQUIRED_LENGTH = 1

        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda prompt="": "y")
            interface = Interface()
            response = interface.read_player_guess()
            assert len(response.isupper()[0]) == REQUIRED_LENGTH

        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda prompt="": "Y")
            interface = Interface()
            response = interface.read_player_guess()
            assert len(response.isupper()[0]) == REQUIRED_LENGTH

        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda prompt="": "Yes")
            interface = Interface()
            response = interface.read_player_guess()
            assert len(response.isupper()[0]) == REQUIRED_LENGTH

    def test_write_title():
        """
        Output Correctness test to check if hangman banner is correct
        """
        title_line1 = " _                                           "
        title_line2 = "| |                                            "
        title_line3 = "| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  "
        title_line4 = "| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ "
        title_line5 = "| | | | (_| | | | | (_| | | | | | | (_| | | | |"
        title_line6 = "|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|"
        title_line7 = "                    __/ |                      "
        title_line8 = "                   |___/                       "
        HANGMAN_TITLE = title_line1 + title_line2 + title_line3 + \
                title_line4 + title_line5 + title_line6 + \
                title_line7 + title_line8
        interface = Interface()
        title = capsys.readouterr()
        assert title.out == HANGMAN_TITLE

    def test_write_options(capsys):
        """
        Output Validation test to check that the print statements are as
        required
        """
        interface = Interface()
        PRINT_START = "        1. Start game"
        PRINT_READ = "        2. Read instructions"
        PRINT_EXIT = "        3. Exit"
        PRINT_INSTRUCTIONS = PRINT_START + PRINT_READ + PRINT_EXIT

        options = capsys.readouterr()
        assert options.out == PRINT_INSTRUCTIONS

    def test_menu_choice(monkeypatch):
        """
        Data Validity Test for menu choice ensures that user does provide
        input
        """
        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda prompt="":"1")
            interface = Interface()
            response = interface.menu_choice()
            assert len(response) > 0


    def test_write_instructions(capsys, monkeypatch):
        """
        Ouptput correctness test to ensure that instructions are printed on
        screen
        Control Flow Check to ensure that that the correct conditions are
        executed based on choice
        Initial Values test checks validity of input_flag's initialized value
        and updated value
        """

        interface = Interface()
        INPUT_FLAG_ZERO = 0
        INPUT_FLAG_ONE = 1

        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda prompt="":"x")
            interface = Interface()
            response = interface.write_instructions().input_flag
            assert response == INPUT_FLAG_ONE

        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda prompt="":"w")
            interface = Interface()
            response = interface.write_instructions().input_flag
            assert response != INPUT_FLAG_ONE

        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda prompt="":"x")
            interface = Interface()
            response = interface.write_instructions().choice
            assert choice.isupper()
        
        initial_input_flag = interface.write_instructions.input_flag
        assert initial_input_flag == INPUT_FLAG_ZERO

    def test_write_instructions():
        """
        """
        pass

