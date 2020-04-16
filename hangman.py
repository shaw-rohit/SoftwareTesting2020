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
    print_dashes = '_' * no_of_dashes 
    print(print_dashes, '\n')
    print('Hint: It\'s a city!') 
    return print_dashes

def play_hangman():
    user_guess = input("Please guess a letter! ").upper()
    return user_guess

def hangman_algorithm(word):
    """
    Some text here
    """
    user_guess_list = []
    attempts = 9
    guessed = False
    print_dashes = hangman_game_display(word)
    print_dashes_list = list(print_dashes)


    word_list = list(word)
    print(word_list)

    while not guessed and attempts > 0:
        user_guess = play_hangman()
        if (len(user_guess) == 1 and user_guess.isalpha()):
            print("User Guessed: ", user_guess)
            if user_guess in user_guess_list:
                print(" You've already guessed this word! Try another valid letter ")
            elif user_guess not in word:
                print(" Sorry! ", user_guess, " is not in the word. Try again!")
                user_guess_list.append(user_guess)
                attempts -= 1
            else:
                print("User entered a correct guess!")
                user_guess_list.append(user_guess)

                valid_indices = []

                for index, letter in enumerate(word):
                    if letter == user_guess:
                        valid_indices += [index]
                print(valid_indices)


                for index in valid_indices:
                    print_dashes_list[index] = user_guess

                print_dashes = " ".join(print_dashes_list)
                print(print_dashes)
                
                if '_' not in print_dashes:
                    guessed = True

        else:
            print("Please enter a valid input. Only a single English letter is allowed.")

    if guessed:
        print("Yay! You won the game!")
    else:
        print("Sorry! You ran out of lives!")

if __name__ == '__main__':
    hangman_algorithm(pick_word())
