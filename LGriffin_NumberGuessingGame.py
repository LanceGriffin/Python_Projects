#Lance Griffin
# 2/22/26
# This is a number guessing game in python that allows the user to guess a random number between 1 and 100
# The user will be given a random number of guesses between 5 and 15, and will be prompted to enter their guess
# The user will be given feedback on whether their guess is too low, too high, or correct
# The user will be given feedback on how many attempts it took them to guess the number, and how many attempts they have left
# The user will also be given the option to play again after each game

import random

def main():
    print("This is the Number Guessing Game!")
    while True:
        number_to_guess = random.randint(1, 100)
        attempts = random.randint(5, 15)

        print(f"You have {attempts} attempts to guess the number between 1 and 100")
        for attempt in range(1, attempts + 1):
            guess = int(input("Enter your guess: "))
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high")
            else:
                print(f"Congratulations! You guess the number in {attempt} attempts!")
                break
            print(f"You have {attempts - attempt} attempts left.")
        else:
            print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing! Goodbye!")
            break