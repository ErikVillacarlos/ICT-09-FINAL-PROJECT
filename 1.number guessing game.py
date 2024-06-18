
import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the Number Guessing Game! Guess a number between 1 and 100.")

    # Loop until the user guesses the correct number
    while guess != number_to_guess:
        # Get the user's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1
        
        # Provide feedback to the user
        if guess < number_to_guess:
            print("Higher! Try again.")
        elif guess > number_to_guess:
            print("Lower! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")

    # Prompt the user to play again
    while True:
        continue_playing = input("Do you want to play again? (yes/no): ").strip().lower()
        if continue_playing == "yes":
            number_guessing_game()
            break
        elif continue_playing == "no":
            print("Thanks for playing the Number Guessing Game!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

# Start the game
number_guessing_game()
