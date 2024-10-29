values = []
for x in range(10):
    values.append(x)
print(values) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# we can do the above in much faster way to go about writing code & little bit easier to read
# using list comprehension - syntax allows for loop inside of a list
values_L_C = [x for x in range(10)]
print(values_L_C) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
values_L_C_1 = [x+1 for x in range(10)]
print(values_L_C_1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]