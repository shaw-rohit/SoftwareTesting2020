from os import system, name


class Interface:
    def __init__(self):
        pass

    def read_player_guess(self):
        self.ins_newline()
        return input("Please guess a letter: ").upper()

    def read_replay(self):
        self.ins_newline()
        return input("Enter Y to replay the game or any other key to exit: ")

    def write_title(self):
        self.ins_newline()
        print(" _                                           ")
        print("| |                                            ")
        print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
        print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
        print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
        print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
        print("                    __/ |                      ")
        print("                   |___/                       ")
        self.ins_newline()

    def write_options(self):
        print("        1. Start game")
        print("        2. Read instructions")
        print("        3. Exit")

    def menu_choice(self):
        self.ins_newline()
        return input("Enter your choice (number): ")

    def write_instructions(self):
        print(
            "The objective of the game is to guess the word before the character is hung."
        )
        self.ins_newline()
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
            "4. You have 9 tries (lives) to guess the word. You lose the game when you run out of lives and the character is hung."
        )
        self.ins_newline()
        print(
            "You can quit the game at any time by pressing the key combination Ctrl + C."
        )
        self.ins_newline()

        input_flag = 0

        while input_flag == 0:
            choice = input("Enter X to return to main menu: ").upper()

            if choice == "X":
                input_flag = 1

            else:
                self.ins_newline()
                print("Invalid input. Please try again.")

    def draw_hangman(self, health):
        if health == 9:
            print("             ")
            print("             ")
            print("             ")
            print("             ")
            print("             ")
            print("             ")
            print("________     ")

        if health == 8:
            print("             ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("___|____     ")

        if health == 7:
            print("   ________  ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("___|____     ")

        if health == 6:
            print("   ________  ")
            print("   |      |  ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("___|____     ")

        if health == 5:
            print("   ________  ")
            print("   |      |  ")
            print("   |      O  ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("___|____     ")

        if health == 4:
            print("   ________  ")
            print("   |      |  ")
            print("   |      O  ")
            print("   |      |  ")
            print("   |      |  ")
            print("   |         ")
            print("___|____     ")

        if health == 3:
            print("   ________  ")
            print("   |      |  ")
            print("   |      O  ")
            print("   |     \|  ")
            print("   |      |  ")
            print("   |         ")
            print("___|____     ")

        if health == 2:
            print("   ________  ")
            print("   |      |  ")
            print("   |      O  ")
            print("   |     \|/ ")
            print("   |      |  ")
            print("   |         ")
            print("___|____     ")

        if health == 1:
            print("   ________  ")
            print("   |      |  ")
            print("   |      O  ")
            print("   |     \|/ ")
            print("   |      |  ")
            print("   |     /   ")
            print("___|____     ")

        if health == 0:
            print("   ________  ")
            print("   |      |  ")
            print("   |      O  ")
            print("   |     \|/ ")
            print("   |      |  ")
            print("   |     / \ ")
            print("___|____     ")

    def read_replay(self):
        return input("Enter Y to replay the game or any other key to exit: ")

    def write_hint(self, hint, theme):
        print("It is a {0} with {1} letters!".format(theme, len(hint)))
        print("Word: {0}".format(" ".join(hint)))

    def write_health(self, health):
        self.ins_newline()
        print("Remaining lives: {0}".format(health))

    def write_guessed_letters(self, guesses):
        print("Letters guessed: {0}".format(guesses))

    def write_already_guessed(self):
        print("You have already guessed this letter! Try again!")

    def write_incorrect_guess(self, guess, health):
        self.ins_newline()

        if health > 0:
            print("Sorry! {0} is not in the word! Try again!".format(guess))
        else:
            print("Sorry! {0} is not in the word!".format(guess))

    def write_correct_guess(self):
        self.ins_newline()
        print("This letter is in the word!")

    def write_invalid_guess(self):
        self.ins_newline()
        print("Please enter a valid, single letter.")

    def write_won(self, word):
        self.ins_newline()
        print("You guessed the word and won the game! Congratulations!".format(word))

    def write_lost(self, word):
        self.ins_newline()
        print("Sorry! You ran out of health! The answer is {0}".format(word))

    def ins_newline(self):
        for i in range(1):
            print("\n")

    def clear_screen(self):
        if name == "nt":
            _ = system("cls")

        else:
            _ = system("clear")
