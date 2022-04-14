import random
from time import sleep

# to keep track of times played and victories
counter = times_win = 0


# list with hangmans
def hangman(moves_left):
    hangmans = ['''
    +---+
     O   |
    /|\  |
    / \  |
        ===''', '''
    +---+
     O   |
    /|\  |
    /    |
        ===''', '''
    +---+
     O   |
    /|\  |
         |
        ===''', '''
    +---+
     O   |
    /|   |
         |
        ===''', '''
    +---+
    O   |
    |   |
        |
        ===''', '''
    +---+
    O   |
        |
        |
        ===''', '''
    +---+
        |
        |
        |
        ===''']
    return hangmans[moves_left]


# selecting a random word from a list
def get_word():
    words_list = "squirrel bear whale coyote hedgehog lion crocodile  elephant\
    hyena monkey panda deer leopard kangaroo tiger zebra giraffe hippo wolf \
    gorilla snake eagle antelope vulture panther parrot rhino shark reindeer \
    lizard leopard koala frog turtle toucan spider sparrow scorpion iguana \
    capybara butterfly bison raven falcon sheep buffalo wildebeest ostrich \
    flamingo jackal raccoon rabbit moose baboon dolphin".upper().split()
    word = random.choice(words_list)
    return word


# setting the game
def run_game(word):
    # to create the _ on the game based on the random word from the list
    word_completion = "_" * len(word)
    # to run the game
    guessed = False
    # list with the letters entered by the user
    guessed_letters = []
    # number of tries, same number of hangmans
    moves_left = 6
    print("\033[92m \nH A N G M A N \033[m")
    # prints the hangman
    print(hangman(moves_left))
    # prints the spaces
    print(word_completion + "\n")

    # guessed must be false and moves_left must be more than 0 so the game runs
    while not guessed and moves_left > 0:
        # asking the user for a letter
        guess = input("Please guess a letter: ").upper()
        # guess must be one letter at the time, no numbers or spaces allowed
        if len(guess) == 1 and guess.isalpha():
            # to check if the user already guessed that letter
            if guess in guessed_letters:
                print("You already guessed this letter. Please try again.")
            # to check if the word contains the letter
            elif guess not in word:
                print(f"You guessed wrong! Letter {guess} is not in the word.")
                # reduces the moves_left by 1 each time
                moves_left -= 1
                # letter is add to the list of guessed letters
                guessed_letters.append(guess)
            else:
                print(f"You guessed correctly! Letter {guess} is in the word.")
                # letter is add to the list of guessed letters
                guessed_letters.append(guess)
                # to convert word_completion from a string to a list
                list_letters = list(word_completion)
                # list comprehension
                index = [i for i, letter in enumerate(word) if letter == guess]
                for indice in index:
                    # replace the space for the guessed letter
                    list_letters[indice] = guess
                # to convert word_completion back to a string
                word_completion = "".join(list_letters)
                # no more spaces means all letters were guessed correctly
                if "_" not in word_completion:
                    # stops the game as there is no more letters to be guessed
                    guessed = True
        else:
            print("Not a valid guess. Please try again.")
        # prints the hangman corresponding with the moves_left
        print(hangman(moves_left))
        # prints the spaces and/or corresponding guessed letters
        print(word_completion + "\n")
        # prints the list with all the guessed letters
        print(str(guessed_letters)[1:-1] + "\n")

    # end of the game
    # guessed=true
    if guessed:
        # add 1 to the variable every time player guess the word correctly
        global times_win
        times_win += 1
        print("\033[96mCongratulations! You guessed the word!\033[m")
    # moves_left=0
    else:
        print(f"\033[33mYou ran out of tries. The word was {word}.\033[m")
        #print("\033[91mGame Over!\033[m")
    # add 1 to the variable every time the game is played
    global counter
    counter += 1
    if counter == 1:
        if times_win == 1:
            print(f"You played {counter} time and have {times_win} victory!")
        else:
            print(f"You played {counter} time and have {times_win} victories!")
    elif counter > 1 and times_win == 1:
        print(f"You played {counter} times and have {times_win} victory!")
    else:
        print(f"You played {counter} times and have {times_win} victories!")


# to restart the game
def keep_playing():
    # variable set to start the loop
    play_again = True
    # to keep the game playing
    while play_again:
        # user should enter Y or N as answer
        restart = input("\nDo you want to play again? [Y/N] ").upper()
        # user enters Y and the game restarts
        if restart == "Y":
            word = get_word()
            run_game(word)
        # user enter an invalid answer
        elif restart != "N" and restart != "Y":
            print("Not a valid option. Please try again.")
            continue
        # user enters N and the loop stops
        else:
            play_again = False
    print("\033[91mGame Over!")
    print("See you next time\33[m")


# main function to run the game
def main():
    # function to pick the random word
    word = get_word()
    # function that contains the game
    run_game(word)
    # function to restart the game
    keep_playing()

def before_start():
    print("\033[7m Welcome to H A N G M A N \033[m \n")
    sleep(1)
    print("\033[34m** Game Rules **\033[m")
    print("- All words to be guessed are animal names")
    print("- Type only one letter at the time, even if you already know the word")
    print("- You can have 6 wrong guesses")
    sleep(3)
    print("\nLet's start", end=" ")
    for x in range(3):
        print(".", end=" ")
        sleep(2)

before_start()
main()
