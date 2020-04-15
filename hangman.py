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

def hangman_algorithm(word, user_guess):
    """
    Some text here
    """
    user_guess_list = []
    word_list = list(word)
    print(word_list)
    if (len(user_guess) == 1 and user_guess.isalpha()):
        print("Valid Input")
    else:
        print("Please enter a valid input. Only a single English letter is allowed.")
    return user_guess


if __name__ == '__main__':
    # print("RANDOM WORD:", pick_word())
    # hangman_game_display(pick_word())
    hangman_algorithm(pick_word(), "A")
