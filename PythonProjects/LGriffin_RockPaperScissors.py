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

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid input. Try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "Its a tie!"
    elif (user == "rock" and computer == "scissors") or \
            (user == "scissors" and computer == "paper") or \
            (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"
    
def scoreboard(user_score, computer_score):
    print(f"Score - You: {user_score} | Computer: {computer_score}")
    
def play_game():
    user_score = 0
    computer_score = 0
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if "You win!" in result:
        user_score += 1
    elif "Computer wins!" in result:
        computer_score += 1

    scoreboard(user_score, computer_score)

    if input("Play again? (yes/no): ").lower() == "yes":
        play_game()

if __name__ == "__main__":
    play_game()