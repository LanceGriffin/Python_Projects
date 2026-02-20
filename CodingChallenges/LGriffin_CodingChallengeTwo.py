user_input = input("Enter a word: ")
if len(user_input) > 5:
    print(f"Your long word is: {user_input}")
else:
    print(f"Your short word is: {user_input}")

print(f"Your word uppercased is: {user_input.upper()}")
print(f"Your word lowercased is: {user_input.lower()}")

# ------------------- Q&A -------------------
#1: len() is a built in function that returns the numbers of items in an object.
#2: Input must be cast before a math operation because input() returns a string,
#  and math operations require numbers.
#3: == Checks for equality between two values