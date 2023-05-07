import random

# Define the word to be guessed
word_to_guess = "python"
word_length = len(word_to_guess)

# Set up the game
attempts = 6
correct_letters = []
incorrect_letters = []

# Main game loop
while attempts > 0:
    # Show the current state of the game
    display_word = ""
    for letter in word_to_guess:
        if letter in correct_letters:
            display_word += letter
        else:
            display_word += "_"
    print(display_word)
    print(f"Correct letters: {correct_letters}")
    print(f"Incorrect letters: {incorrect_letters}")
    print(f"Attempts remaining: {attempts}")

    # Get the player's guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is correct
    if guess in word_to_guess:
        print("Correct!")
        correct_letters.append(guess)
    else:
        print("Incorrect.")
        incorrect_letters.append(guess)
        attempts -= 1

    # Check if the player has won or lost
    if set(correct_letters) == set(word_to_guess):
        print(f"You win! The word was {word_to_guess}.")
        break
    elif attempts == 0:
        print(f"You lose. The word was {word_to_guess}.")
        break

