import os
import time
from hangman.game import Game
from hangman.interface import Interface
from hangman.player import Player

if __name__ == "__main__":
    interface = Interface()

    replay = "Y"

    menu_input_flag = 0
    instructions_input_flag = 0

    while menu_input_flag == 0:
        os.system("cls")
        interface.write_title()
        interface.write_options()
        menu_choice = interface.menu_choice()

        if menu_choice == "1":
            menu_input_flag = 1
            os.system("cls")
            while replay[0].upper() == "Y":
                player = Player()
                game = Game(player, interface)
                game.start()
                replay = interface.read_replay()

        elif menu_choice == "2":
            os.system("cls")
            interface.write_title()
            interface.write_instructions()

        elif menu_choice == "3":
            exit()

        else:
            print("Invalid input. Please try again.")
            time.sleep(1)
