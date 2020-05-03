import os
import sys
from io import StringIO
from .context import hangman
from hangman.interface import Interface

def test_read_player_guess(monkeypatch):
    """
    Data Value Test
    """
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": "M")
        interface = Interface()
        assert interface.read_player_guess().isupper()
    
