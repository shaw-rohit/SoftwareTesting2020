class Interface:
    def __init__(self):
        pass

    def read_player_name(self):
        return input("Please enter your name: ")

    def read_player_guess(self):
        return input("Please guess a letter: ").upper()

    def read_replay(self):
        return input("Enter Y to replay the game or any other key to exit: ")

    def write_credits(self):
        print("***HANGMAN***")

    def write_hint(self, hint, theme):
        print("It is a {0} with {1} letters!".format(theme, len(hint)))
        print("Word: {0}".format(" ".join(hint)))

    def write_health(self, health):
        print("Remaining lives: {0}".format(health))

    def write_guessed_letters(self, guesses):
        print("Letters guessed: {0}".format(guesses))

    def write_already_guessed(self):
        print("You have already guessed this letter! Try again!")

    def write_incorrect_guess(self, guess):
        print("Sorry! {0} is not in the word! Try again!".format(guess))

    def write_correct_guess(self):
        print("This letter is in the word!")

    def write_invalid_guess(self):
        print("Please enter a valid, single letter.")

    def write_won(self):
        print("Yay! You won the game!")

    def write_lost(self, word):
        print("Sorry! You ran out of health! The answer is {0}".format(word))

    def clear(self):
        for i in range(1): print("\n")
