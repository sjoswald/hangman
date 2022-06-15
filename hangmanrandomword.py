"""
Runs a game of hangman in the terminal
"""
import random
from words import word_list

def get_random_word():
    """
    Returns a randomly chosen secret_word from a previously generated secret_word list
    """
    secret_word = random.choice(word_list)
    return secret_word.upper()



def play(secret_word):
    """
    Game logic to check validity of guesses and to track secret_word completion.
    """
    word_completion = "_" * len(secret_word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 9
    print("We're going to play some hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("")

    while not guessed and tries > 0:
        guess = input("Please guess a letter/ word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in secret_word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Yes", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(secret_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(secret_word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != secret_word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                word_completion = guess
                guessed = True
        else:
            print("Gues not valid, try again.")
        print(display_hangman(tries))
        print(word_completion)
        print("You have already guessed: " + str(guessed_letters))
        print("")
    if guessed:
        print("Well done you guessed the word!")
    else:
        print("Better luck next time! The word was " + secret_word )



def display_hangman(tries):
    """
    Visual output for the hangman, correlates to number of failed guesses
    """
    stages = [  # head, torso, both arms, and both legs. Game has been lost.
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   --------
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   --------
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   --------
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   --------
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   --------
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   --------
                """,
                # completed hanging structure
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   --------
                """,
                # upright and horizontal in place
                """
                   --------
                   |
                   |
                   |
                   |
                   |
                   --------
                """,
                # upright in place
                """
                   
                   |
                   |
                   |
                   |
                   |
                   --------
                """,
                # initial empty state, only base is present
                """
                   
                   
                   
                   
                   
                   
                   --------
                """
    ]
    return stages[tries]

def main():
    """
    Function to play the game and allow users to play more than one game in a row
    """
    secret_word = get_random_word()
    play(secret_word)
    while input("Play Again? (Y/N)").upper() == "Y":
        secret_word = get_random_word()
        play(secret_word)

if __name__ == "__main__":
    main()
