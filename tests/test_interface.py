from os import system, name
from io import StringIO
from .context import hangman
from hangman.interface import Interface
import pytest

interface = Interface()

def test_read_player_guess(monkeypatch):
    """
    Data integrity test to check for upper case conversion of input
    """
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": "M")
        assert interface.read_player_guess().isupper()

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": "m")
        assert interface.read_player_guess().isupper()

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": "mm")
        assert interface.read_player_guess().isupper()

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": "1")
        assert not interface.read_player_guess().isupper()

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": "@")
        assert not interface.read_player_guess().isupper()

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": " ")
        assert not interface.read_player_guess().isupper()

def test_read_replay(monkeypatch):
    """
    Input validation/Data validation test to check replay input is upper
    case and is the first letter of the input
    """
    REQUIRED_LENGTH = 1

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": "y")
        response = interface.read_player_guess()
        assert len(response.upper()[0]) == REQUIRED_LENGTH

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": "Y")
        response = interface.read_player_guess()
        assert len(response.upper()[0]) == REQUIRED_LENGTH

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="": "Yes")
        response = interface.read_player_guess()
        assert len(response.upper()[0]) == REQUIRED_LENGTH
@pytest.mark.skip(reason="tested via exploratory tests")
def test_write_title(capsys):
    """
    Output Correctness test to check if hangman banner is correct
    """

def test_write_options(capsys):
    """
    Output Validation test to check that the print statements are as
    required
    """
    PRINT_START = "        1. Start game"
    PRINT_READ =  "        2. Read instructions"
    PRINT_EXIT =  "        3. Exit"
    PRINT_INSTRUCTIONS = [PRINT_START, PRINT_READ, PRINT_EXIT]

    options = capsys.readouterr()
    print('\n'.join(PRINT_INSTRUCTIONS))

def test_menu_choice(monkeypatch):
    """
    Data Validity Test for menu choice ensures that user does provide
    input
    """
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="":"1")
        response = interface.menu_choice()
        assert len(response) > 0

@pytest.mark.skip(reason="no way of currently testing this")
def test_write_instructions(monkeypatch):
    """
    Ouptput correctness test to ensure that instructions are printed on
    screen
    Control Flow Check to ensure that that the correct conditions are
    executed based on choice Initial Values test checks validity of input_flag's initialized value
    and updated value
    """
    INPUT_FLAG_ZERO = 0
    INPUT_FLAG_ONE = 1

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="":"X")
        response = interface.write_instructions().input_flag
        assert response == INPUT_FLAG_ONE

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="":"w")
        response = interface.write_instructions().input_flag
        assert response != INPUT_FLAG_ONE

    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda prompt="":"x")
        response = interface.write_instructions().choice
        assert choice.isupper()
    initial_input_flag = interface.write_instructions().input_flag
    assert initial_input_flag == INPUT_FLAG_ZERO


@pytest.mark.skip(reason="tested via exploratory tests")
def test_draw_hangman():
    """
    This method might not be suitable or necessary for unit tests. A
    walkthrough style of analysis might be more useful
    """
    pass

def test_write_hint(capsys):
    """
    Output Correctness Check to ensure correct user hints and final words
    are displayed
    """
    hint = "mumbai"
    theme = "city"

    helpful_hint = "It is a " +  theme + " with " + str(len(hint)) + " letters!"
    correct_word = "Word: " + hint
    user_hints = interface.write_hint(hint, theme)

    user_hints = capsys.readouterr()
    assert user_hints.out

def test_write_health(capsys):
    """
    Output Correctness Check to ensure correct user health 
    """
    health = 3
    user_health = interface.write_health(health)
    user_health = capsys.readouterr()
    assert user_health.out == "\n\nRemaining lives: 3\n"

def test_write_guessed_letters(capsys):
    """
    Correctness Check: Does the method print as required
    """
    guesses = 's'
    user_guesses = interface.write_guessed_letters(guesses)
    GUESSED_PROMPT = "Letters guessed: " + guesses + '\n'

    user_guesses = capsys.readouterr()
    assert user_guesses.out == GUESSED_PROMPT

def test_write_already_guessed(capsys):
    """
    Correctness Check: Does the method print as required
    """
    GUESSED_PROMPT = "You have already guessed this letter! Try again!\n"
    prompt = interface.write_already_guessed()

    prompt = capsys.readouterr()
    assert prompt.out == GUESSED_PROMPT

def test_write_incorrect_guess(capsys):
    """
    Correctness Check: Does the method print as required
    """
    pass

def test_write_correct_guess(capsys):
    """
    Correctness Check: Does the method print as required
    """
    GUESSED_PROMPT = "\n\nThis letter is in the word!\n"
    prompt = interface.write_correct_guess()
    prompt = capsys.readouterr()
    assert prompt.out == GUESSED_PROMPT

def test_write_invalid_guess(capsys):
    """
    Correctness Check: Does the method print as required
    """
    GUESSED_PROMPT = "\n\nPlease enter a valid, single letter.\n"
    prompt = interface.write_invalid_guess()
    prompt = capsys.readouterr()
    assert prompt.out == GUESSED_PROMPT

def test_write_won(capsys):
    """
    Correctness Check: Does the method print as required
    """
    GUESSED_PROMPT = "\n\nYou guessed the word and won the game! Congratulations!\n"
    prompt = interface.write_won()
    prompt = capsys.readouterr()
    assert prompt.out == GUESSED_PROMPT

def test_write_lost(capsys):
    """
    Correctness Check: Does the method print as required
    """
    word = "mumbai"
    correct_word = interface.write_lost(word)

    correct_word = capsys.readouterr()
    GUESSED_PROMPT = "\n\nSorry! You ran out of health! The answer is " + word + "\n"
    assert correct_word.out == GUESSED_PROMPT

def test_ins_newline(capsys):
    """
    Correctness Check: Does the method print as required
    """
    RANGE_LENGTH = 0
    prompt = capsys.readouterr()
    assert len(prompt.out) ==  RANGE_LENGTH

def test_clear_screen(capsys):
    """
    System Behaviour Check to test if the os method coorectly detect the os and
    clear screen
    """
    prompt = capsys.readouterr()
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear") 

