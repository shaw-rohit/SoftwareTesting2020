import random
from words import words

def hangman_pick_word():
    """
    Returns a randomly selected a theme and word 
    """
    theme = random.choice(list(words.keys()))
    word = random.choice(words.get(theme)).upper()
    return theme, word

def hangman_print_hint(theme, word):
    """
    Generates a hint based on the category randomly chosen
    """
    print("It\'s a {0} with {1} letters!".format(theme, len(word)))


def hangman_print_dashes(word):
    """
    Prints the number of dashes based on the word previously selected 
    """
    hangman_clear_screen()
    no_of_dashes = len(word)
    print_dashes = "_" * no_of_dashes 
    print("Word: {0} ".format(" ".join(print_dashes)))
    return print_dashes


def hangman_get_letter():
    """
    Requests user to input a letter and converts it to upper case
    """
    user_guess = input("Please guess a letter: ").upper()
    hangman_clear_screen()
    return user_guess


def hangman_clear_screen():
    """
    Clears screen based on the range specifed
    """
    for i in range(1):
        print("\n")


def hangman_win_lose(word, guessed):
    """
    Checks if the player won or lost and prints the information
    """
    if guessed:
        print("Congratulations! You won the game!")
    else:
        print("Sorry you ran out of lives! The correct answer is {0} ".format(word))
    return 


def hangman_algorithm(theme, word):
    """
    Sets user attemps and initial state of the game. Obtains user guesses and
    checks for validity. If user guess is correct, displays the appropriate
    letters corresponding to the guess. If the user guess is invalid, decreases
    attempts and informs user. If user guessed a previously guessed letter, no
    penealty for the user.
    """
    user_guess_set = set()
    attempts = 9
    guessed = False
    valid_indices = []

    print_dashes = hangman_print_dashes(word)
    hangman_print_hint(theme, word)

    print_dashes_list = list(print_dashes)
    word_list = list(word)

    while not guessed and attempts > 0:
        print("Remaining Lives: {0} ".format(attempts))
        print("Letters Guessed: {0} ".format(user_guess_set))
        user_guess = hangman_get_letter()

        if (len(user_guess) == 1 and user_guess.isalpha()):
            if user_guess in user_guess_set:
                print("You've already guessed this letter! Try again!")
                print("Word: {0}".format(" ".join(print_dashes)))
                hangman_print_hint(theme, word)
            elif user_guess not in word:
                print("Sorry! {0} is not in the word. Try again!".format(user_guess))
                user_guess_set.add(user_guess)
                attempts -= 1
                print("Word: {0}".format(" ".join(print_dashes)))
                hangman_print_hint(theme, word)
            else:
                print("This letter is in the word!")
                user_guess_set.add(user_guess)

                print_dashes = " ".join(letter if letter in user_guess_set
                        else "_" for letter in word)

                print("Word: {0}".format(print_dashes))
                hangman_print_hint(theme, word)

                if "_" not in print_dashes:
                    guessed = True

        else:
            print("Please enter a valid, single letter.")
            print("Word: {0}".format(" ".join(print_dashes)))
            hangman_print_hint(theme, word)

    hangman_win_lose(word, guessed)


def main():
    replay_trigger = "Y"

    theme, word = hangman_pick_word()
    hangman_algorithm(theme, word)

    replay_question = input("Enter Y to replay the game.\
            Enter any other key to exit game.")

    while replay_question.upper() == replay_trigger:
        theme, word = hangman_pick_word()
        hangman_algorithm(theme, word)

if __name__ == "__main__":
    main()
