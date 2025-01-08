# Day 2 ---> Advance Python [08th Jan 2025]
# Dictionary Comprehensions

names = ['John', 'Smith', 'Alex', 'Tina']
marks = [85, 90, 82, 93]

# Without Dictionary Comprehension
stInfo = {}
for (key, value) in zip(names, marks):
    stInfo[key] = value

print("Dictionary:", stInfo)


# Dictionary Comprehension
stInfo_comp = {key: value for (key, value) in zip(names, marks)}
print("Dictionary (Comprehension):", stInfo_comp)


numbers = [1, 2, 3, 4, 5]
# {1:1, 2:8, 3:27, 4:64, 5:125}
cubes = {}
for num in numbers:
    cubes[num] = num**3
print("Cubes:", cubes)

# Dictionary Comprehension
cubes_comp = {num: num**3 for num in numbers}
print("Cubes (Comprehension):", cubes_comp)

# set Comprehension ( only unique values contain by keys in dictionary)
numbers2 = [1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9, 10, 10, 9, 3, 5]
cubes_comp2 = {num: num**3 for num in numbers2}
print("Cubes (Comprehension ( unique key )): ", cubes_comp2)


# Conditional Dictionary Comprehension
cond_dict = {num: num**3 for num in numbers if num % 2 == 0}
print("Conditional Cubes (Comprehension):", cond_dict)

# Set Data structure 
set1 = { i for i in numbers2 if i % 2 == 0}
print("Set (Comprehension):", set1)

# Example of Generator comprehension ( not a tuple comprehension)
# is similar to list comprehension, but it returns a generator object instead of a list. (Circular Brackets)
# Memory Efficient
res = (i for i in numbers2 if i % 2 == 0)
print("Generator (Comprehension):", res)
for i in res:
    print(i, end=" ")


# ennumerate() function 
# 0 : 10 
# 1 : 20
# it adds a counter to an iterable and returns it in a form of enumerate object.
list1 = [10, 20, 30, 40, 50]
for index, value in enumerate(list1):
    print(f"Index: {index}, Value: {value}")

# Arrays : Numpy
# Series and DataFrames : Pandas