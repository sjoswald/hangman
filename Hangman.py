import time

name = input("What is your name? ")

print("Hello, " + name + " your game is about to begin!")
print('')

time.sleep(1)

print("Get ready to start guessing...")
time.sleep(1)

word = "Anaconda"

word = word.lower()

guesses = ""
turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, )
        else:
            print("-, ")
            failed += 1
    if failed == 0:
        print("Well done! You guessed right")
        break

    guess =  input("Guess a letter:")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong Guess")
        print("You have " + str(turns) + " guesses left")
        if turns == 0:
            print("You Lose. The word was " + word)