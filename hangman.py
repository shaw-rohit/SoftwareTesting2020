import random
from words import cities

def pick_word():
    """
    Randomly picks a word from the words.py file and converts to upper case.
    """
    word = random.choice(cities).upper()
    return word

def hangman_game_display(word):
    """
    Generates a standard hint and the number of dashes based on the word
    previously selected 
    """
    no_of_dashes = len(word)
    print('_ ' * no_of_dashes, '\n')
    print('Hint: It\'s a city!') 
    return no_of_dashes


if __name__ == '__main__':
    # print("RANDOM WORD:", pick_word())
    hangman_game_display(pick_word())
