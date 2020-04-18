class Menu:
    def __init__(self):
        pass

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
            "4. You have 6 tries (lives) to guess the word. You lose the game when you run out of lives and the character is hung.\n\n"
        )

        input_flag = 0

        while input_flag == 0:
            choice = input("  Enter X to go back to main menu: ").upper()

            if choice == "X":
                input_flag = 1

            else:
                print("  Invalid input. Please try again.\n")
