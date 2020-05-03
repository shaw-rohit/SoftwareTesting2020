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
    
