import random

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
    words_list = "squirrel bear whale coyote hedgehog lioncrocodile  elephant\
    hyena monkey panda deer leopard kangaroo tiger zebra giraffe hippo wolf \
    gorilla snake eagle antelope vulture panther parrot rhino shark reindeer \
    lizard leopard koala frog turtle toucan spider sparrow scorpion iguana \
    capybara butterfly bison raven falcon sheep buffalo wildebeest ostrich \
    flamingo jackal raccoon rabbit moose baboon dolphin".upper().split()
    word = random.choice(words_list)
    return word


# setting the game
def run_game(word):
    word_completion = "_" * len(word) # to create the _ on the game based on the random word from the list
    guessed = False # to run the game
    guessed_letters = [] # list with the letters entered by the user
    moves_left = 6 # number of tries, same number of hangmans
    counter = times_win = 0
    print("\033[92m H A N G M A N \033[m")
    print(hangman(moves_left)) # prints the hangman
    print(word_completion + "\n") # prints the spaces

    while not guessed and moves_left > 0: # guessed must be false and moves_left must be more than 0 so the game runs
        guess = input("Please guess a letter: ").upper() # asking the user for a letter
        if len(guess) == 1 and guess.isalpha(): # guess must be one letter at the time, no numbers or spaces allowed
            if guess in guessed_letters: # to check if the user already guessed that letter
                print("You already guessed this letter. Please try again.")
            elif guess not in word: # to check if the word contains the letter
                print(f"You guessed wrong! Letter {guess} is not in the word.")
                moves_left -= 1 # reduces the moves_left by 1 each time
                guessed_letters.append(guess) # letter is add to the list of guessed letters
            else:
                print(f"You guessed correctly! Letter {guess} is in the word.")
                guessed_letters.append(guess) # letter is add to the list of guessed letters
                list_letters = list(word_completion) # to convert word_completion from a string to a list
                indices = [i for i, letter in enumerate(word) if letter == guess] # list comprehension
                for index in indices:
                    list_letters[index] = guess # replace the space for the guessed letter
                word_completion = "".join(list_letters) # to convert word_completion back to a string
                if "_" not in word_completion: # no more spaces means all letters were guessed correctly
                    guessed = True # stops the game as there is no more letters to be guessed
        else:
            print("Not a valid guess. Please try again.")
        print(hangman(moves_left)) # prints the hangman corresponding with the moves_left
        print(word_completion + "\n") # prints the spaces and/or corresponding guessed letters
        print(str(guessed_letters)[1:-1] + "\n") # prints the list with all the guessed letters

    # end of the game
    if guessed: # guessed=true
        times_win += 1
        print("\033[96mCongratulations! You guessed the word!\033[m")
    else: # moves_left=0
        print(f"\033[91mYou ran out of tries. The word was {word}.\nGame Over!\033[m")
    counter += 1
    print(f"You played {counter} times and have {times_win} victories!")



def keep_playing():
    play_again = input("Do you want to play again? [Y/N] ").upper()
    while play_again != "Y" and play_again != "N":
        print("Not a valid option. Please try again.")
        play_again = input("Do you want to play again? [Y/N] ").upper()
    if play_again == "Y":
        word = get_word()
        run_game(word)  
    else:
        print("See you next time")
            

# main function to run the game
def main():
    word = get_word() # function to pick the random word
    run_game(word) # function that contains the game
    keep_playing()


main()
