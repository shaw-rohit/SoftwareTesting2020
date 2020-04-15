import random
from words import cities

def pick_word():
    """
    Randomly picks a word from the words.py file and converts to upper case.
    """

    word = random.choice(cities).upper()
    return word


if __name__ == '__main__':
    print("RANDOM WORD:", pick_word())
