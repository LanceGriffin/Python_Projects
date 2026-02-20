# Lance Griffin
# ------------------ Practice activity 1 ------------------
import math
num = int(input("Enter a number: "))
answer = math.sqrt(num)
print(f"The square root of {num} is {answer}")

# ------------------ Practice activity 2 ------------------
word = input("\nEnter a word: ")
for i in range(len(word)):
    print(word[i])

# ------------------ Practice activity 3 ------------------
import random
print("\nRolling two dice...")
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
print(f"You rolled a {num1} and a {num2}.")