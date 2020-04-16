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

def play_hangman():
    user_guess = input("Please guess a letter! ").upper()
    return user_guess

def hangman_algorithm(word):
    """
    Some text here
    """
    user_guess_list = []
    attempts = 9

    word_list = list(word)
    print(word_list)

    while not user_guess_list and attempts > 0:
        user_guess = play_hangman()
        if (len(user_guess) == 1 and user_guess.isalpha()):
            print("User Guessed: ", user_guess)
        else:
            print("Please enter a valid input. Only a single English letter is allowed.")


if __name__ == '__main__':
    hangman_algorithm(pick_word())
