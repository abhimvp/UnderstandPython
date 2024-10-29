# usage of zip function


# without zip?
def add_numbers(a, b, c):
    return a + b + c


numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [7, 8, 9]

result = []
for i in range(len(numbers1)):
    result.append(add_numbers(numbers1[i], numbers2[i], numbers3[i]))

print(result)  # Output: [10, 15, 22]


# with zip

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [7, 8, 9]

result = []
for numbers in zip(numbers1, numbers2, numbers3):
    result.append(add_numbers(*numbers))

print(result)  # Output: [10, 15, 22]

# Another example

names = ["Alice", "Bob", "Charlie", "david"]
ages = [30, 25, 35, 20]

# using min in range because we may get index out of bounds exception when we try to access
#  the corresponding position in other list
for idx in range(min(len(names), len(ages))):
    print(f"Name: {names[idx]}, Age: {ages[idx]}")
# Name: Alice, Age: 30
# Name: Bob, Age: 25
# Name: Charlie, Age: 35
# Name: david, Age: 20

# with zip - combine different iterable objects together
# it will stop at the shortest iterable object
# it will not throw index out of bounds exception

names_with_tim = ["Alice", "Bob", "Charlie", "david", "Tim"]
combined = list(zip(names_with_tim, ages))
print(combined)  # [('Alice', 30), ('Bob', 25), ('Charlie', 35), ('david', 20)]
# it didn't include tim because it was not in the ages list
# we can use * to unpack the tuple
for name, age in combined:
    print(f"Name: {name}, Age: {age}")
    
# Another example with gender
gender = ["Female","male","Male"]
combined_gender = list(zip(names_with_tim, ages,gender))
print(combined_gender)
# [('Alice', 30, 'Female'), ('Bob', 25, 'male'), ('Charlie', 35, 'Male')]

for name, age, gender in combined_gender:
    print(f"Name: {name}, Age: {age}, Gender: {gender}")
