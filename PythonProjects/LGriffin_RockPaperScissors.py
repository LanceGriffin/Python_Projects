# Goal:
# Create a game where the user plays Rock-Paper-Scissors against the
# computer. The program should handle input, apply game rules, determine
# the winner, and display results clearly. Optionally, implement multiple rounds
# and track scores.

# Skills Learned:
# ● Using the random module to simulate computer choices
# ● Handling and validating user input
# ● Applying conditional logic to determine the winner
# ● Using loops to allow multiple rounds or replaying the game
# ● Organizing code with functions for readability and reusability
# ● Optional: Keeping track of scores and implementing a “best of 3”
# system

# Concept:
# 1. Program prompts the user for their choice: rock, paper, or scissors.
# 2. Program generates a random choice for the computer.
# 3. Program compares choices and applies the game rules:
# ○ Rock beats Scissors
# ○ Scissors beats Paper
# ○ Paper beats Rock
# 4. Program prints both the user’s and computer’s choices.
# 5. Program announces the winner or declares a tie.
# 6. Program optionally allows multiple rounds and keeps score.

# 7. Program handles invalid input gracefully (e.g., user enters something
# other than rock, paper, or scissors).

# Checklist:
# ✔ Prompts the user for their choice
# ✔ Randomly generates the computer’s choice
# ✔ Applies correct game rules to determine the winner
# ✔ Handles ties correctly
# ✔ Displays both player and computer choices
# ✔ Handles invalid input gracefully

# Project Requirements:
# ● Must allow at least one round
# ● Must display clearly who won each round
# ● Must allow replaying the game (optional)
# ● Must track score across multiple rounds (optional)

# Bonus Challenge (Choose One):
# ● Implement a best-of-3 or best-of-5 system
# ● Add a scoreboard that updates after each round
# ● Allow user-defined number of rounds
# ● Add a play-again feature so the game continues until the user

#Lance Griffin
# This is a rock paper scissors

import random

# Function to get the user's choice of rock, paper, or scissors OR the corresponding numbers
def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid input. Try again.")

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice.split()[0]:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"
    
# Function to keep track of scores
def update_scores(user_choice, computer_choice, scores):
    if user_choice == computer_choice.split()[0]:
        scores['ties'] += 1
    elif (user_choice == 'rock') and (computer_choice == 'scissors'):
        scores['user'] += 1
    elif (user_choice == 'paper') and (computer_choice == 'rock'):
        scores['user'] += 1
    elif (user_choice == 'scissors') and (computer_choice == 'paper'):
        scores['user'] += 1
    else:
        scores['computer'] += 1

# Main function to play the game
def play_game():
    scorse = {'user': 0, 'computer': 0, 'ties': 0}
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        update_scores(user_choice, computer_choice, scorse)
        print(f"Scores - You: {scorse['user']}, Computer: {scorse['computer']}, Ties: {scorse['ties']}")
        if not play_again():
            break

# Function to ask the user if they want to play again
def play_again():
    while True:
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again in ['yes', 'no']:
            return again == 'yes'
        print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    while True:
        play_game()
        if not play_again():
            break