# Calculator project
# This program will perform mathematical operations based on user input.
# Some of the advanced features include:
# - Basic arithmetic operations (+, -, *, /)
# - Exponentiation
# - Square root
# - Trigonometric functions (sin, cos, tan)

import math

# Dialogue with the user
print("Welcome to the Calculator!")
print("Enter username: ")
username = input()
print(f"Hello, {username}! Let's get started with some calculations.")

# Function to perform basic operations
print("Enter the first number: ")
num1 = float(input())
print("Enter the second number: ")
num2 = float(input())
print("Choose the operation (+, -, *, /, ^ for exponents, sqrt for square root, sin, cos, tan)")
operation = input()

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
elif operation == '^':
    result = num1 ** num2
elif operation == 'sqrt':
    if num1 >= 0:
        result = math.sqrt(num1)
    else:
        result = "Error: Cannot take the square root of a negative number."
elif operation == 'sin':
    result = math.sin(math.radians(num1))
elif operation == 'cos':
    result = math.cos(math.radians(num1))
elif operation == 'tan':
    result = math.tan(math.radians(num1))
else:
    result = "Error: Invalid operation selected."

print(f"The result of the operation is: {result}")
print("Do you want to perform another calculation? (yes/no)")

continue_calculating = input().lower()
if continue_calculating == 'yes':
    print("Restarting the calculator...")
    exec(open("LGriffin_Calculator.py").read())
else:
    print("Thank you for using the calculator.")