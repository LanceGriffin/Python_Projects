# Coding Challenge Five
# Lance Griffin

# Steps
# 1. Add 5 student names to the list
# 2. Convert the list to a set to remove duplicates
# 3. Store student names and grades in a dictionary
# 4. Print all students with grades above 70
# Q&A
# 1. Difference between list and tuple?
# 2. Why are sets unordered?
# 3. When should dictionaries be used?
# Modding
# ● Calculate class average
# ● Sort students by grade

students = [
    "Alice", "Bob", "James", "Alice", "Emily"
]

# removing duplicates by converting to a set
unique_students = set(students)

student_grades = {
    "Alice": 85,
    "Bob": 68,
    "James": 92,
    "Emily": 87
}
print(f"Students with grades above 70: {[name for name, grade in student_grades.items() if grade > 70]}")

# Calculate class average
average_grade = sum(student_grades.values()) / len(student_grades)
print(f"Class average: {average_grade:.2f}")

# --------------------------- Q&N ---------------------------
# Q1: The difference between a list and a tuple is that a list can be changed while a tuple cannot.
# Q2: Sets are unordered because they are implemented as hash tables, which do not maintain any order.
# Q3: Dictionaries should be used when you need to store key value pairs.