# Coding Challenge 3

# Using loops to ask the user for 5 numbers
numbers = []
for i in range(5):
    num = float(input(f"Enter number: "))
    numbers.append(num)

#Invalid input handling
try:
    integers = [int(num) for num in numbers]
except ValueError:
    print("Invalid input. Enter a valid number.")

# Sum and average of the numbers
total_sum = sum(numbers)
average = total_sum / len(numbers)
print(f"The sum of the numbers is: {total_sum}")
print(f"The average of the numbers is: {average}")

# Ignoring negative numbers
positive_numbers = [num for num in numbers if num >= 0]
# if positive_numbers:
#     positive_sum = sum(positive_numbers)
#     positive_average = positive_sum / len(positive_numbers)
#     print(f"The sum of the positive numbers is: {positive_sum}")
#     print(f"The average of the positive numbers is: {positive_average}")
# else:
#     print("No positive numbers entered.")

# -------------------- Q&A --------------------
#1. When a function is called that has the right data type but wrong value
#2. loop is used when the number of iterations is known ahead of time
# while loop is used when the number of iterations is not known
#3. It prevents the program from crashing