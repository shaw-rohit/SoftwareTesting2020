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

    def test_write_instructions():
        """
        """

