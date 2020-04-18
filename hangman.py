import os
from hangman.game import Game
from hangman.interface import Interface
from hangman.player import Player
from hangman.menu import Menu

if __name__ == "__main__":
    interface = Interface()
    menu = Menu()

    menu_input_flag = 0
    instructions_input_flag = 0

    while menu_input_flag == 0:
        os.system("cls")
        menu.write_title()
        menu.write_options()
        menu_choice = menu.menu_choice()

        if menu_choice == "1":
            menu_input_flag = 1
            os.system("cls")
            player = Player()
            game = Game(player, interface)
            game.start()

        elif menu_choice == "2":
            os.system("cls")
            menu.write_title()
            menu.write_instructions()

        elif menu_choice == "3":
            exit()

        else:
            print("Invalid input. Please try again.")
