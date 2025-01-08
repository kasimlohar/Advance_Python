# Day 1 -- Advanced Python [06th Jan 2025]

# 1. Using zip() to combine iterables
names = ['John', 'Smith', 'Alex', 'Tina']
marks = [85, 90, 82, 93]

# Combine names and marks using zip
final_info = zip(names, marks)
print("Zipped List:", list(final_info))

# Re-create final_info for unzipping as zip() is exhausted after iteration
final_info = [('John', 85), ('Smith', 90), ('Alex', 82), ('Tina', 93)]

# Unzipping using * operator
names_unzipped, marks_unzipped = zip(*final_info)
print("Unzipped Names:", names_unzipped)
print("Unzipped Marks:", marks_unzipped)

# Looping through combined lists using range
for i in range(len(names)):
    print(f"{names[i]} {marks[i]}")

# Looping through combined lists using zip
for name, mark in zip(names, marks):
    print(f"{name} {mark}")

# 2. List Comprehensions
numbers = [3, 4, 6, 7, 8, 9, 10, 11, 15, 16, 18, 21, 22, 26]

# Create a list of even numbers using a loop
list1 = []
for num in numbers:
    if num % 2 == 0:
        list1.append(num)
print("Even Numbers (Loop):", list1)

# Create a list of even numbers using list comprehension
list1_comp = [num for num in numbers if num % 2 == 0]
print("Even Numbers (List Comprehension):", list1_comp)

# Create a list of squares using list comprehension
squared_numbers = [num**2 for num in numbers[:7]]  # Limiting to 7 numbers for demonstration
print("Squared Numbers:", squared_numbers)

# 3. Nested for loop using list comprehension
str1 = 'abc'
str2 = 'def'

# Nested loop using traditional for-loops
for char1 in str1:
    for char2 in str2:
        print(char1, char2)

# Nested loop using list comprehension
nested_list = [char1 + ' ' + char2 for char1 in str1 for char2 in str2]
print("Nested Combinations:", nested_list)
