class Interface:
    def __init__(self):
        pass

    def read_player_name(self):
        return input("Please enter your name: ")

    def read_player_guess(self):
        return input("\nPlease guess a letter: ").upper()

    def read_replay(self):
        return input("\nEnter Y to replay the game or any other key to exit: ")

    def write_title(self):
        print("\n _                                           ")
        print("| |                                            ")
        print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
        print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
        print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
        print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
        print("                    __/ |                      ")
        print("                   |___/                     \n")

    def write_options(self):
        print("        1. Start game")
        print("        2. Read instructions")
        print("        3. Exit")

    def menu_choice(self):
        return input("\nEnter your choice (number): ")

    def write_instructions(self):
        print(
            "The objective of the game is to guess the word before the character is hung.\n"
        )
        print(
            "1. You'll be presented with a row of dashes representing each letter of the word you need to guess."
        )
        print(
            "2. Each time a correct letter is guessed from the word, all corresponding empty dashes will be filled with that letter of the word."
        )
        print(
            "3. If the letter you guessed doesn't belong to the word, an appendage to the stickman hangman will be drawn and you will lose one unit of life."
        )
        print(
            "4. You have 9 tries (lives) to guess the word. You lose the game when you run out of lives and the character is hung.\n\n"
        )

        input_flag = 0

        while input_flag == 0:
            choice = input("  Enter X to return to main menu: ").upper()

            if choice == "X":
                input_flag = 1

            else:
                print("  Invalid input. Please try again.\n")

    def read_replay(self):
        return input("Enter Y to replay the game or any other key to exit: ")

    def write_credits(self):
        print("***HANGMAN***")

    def write_hint(self, hint, theme):
        print("It is a {0} with {1} letters!".format(theme, len(hint)))
        print("Word: {0}".format(" ".join(hint)))

    def write_health(self, health):
        print("\nRemaining lives: {0}".format(health))

    def write_guessed_letters(self, guesses):
        print("Letters guessed: {0}".format(guesses))

    def write_already_guessed(self):
        print("You have already guessed this letter! Try again!")

    def write_incorrect_guess(self, guess):
        print("\nSorry! {0} is not in the word! Try again!".format(guess))

    def write_correct_guess(self):
        print("\nThis letter is in the word!")

    def write_invalid_guess(self):
        print("\nPlease enter a valid, single letter.")

    def write_won(self):
        print("Yay! You won the game!")

    def write_lost(self, word):
        print("Sorry! You ran out of health! The answer is {0}".format(word))

    def clear(self):
        for i in range(1):
            print("\n")
