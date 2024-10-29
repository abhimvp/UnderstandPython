#  range function - iterate throught the values in a for loop
#  can use it to generate a list of numbers
rng = range(10)

print(list(rng))
# python range.py
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

rng2 = range(5, 10) # start value -> stop value
print(list(rng2))
# [5, 6, 7, 8, 9]

rng3 = range(5, 10, 2) # start value -> stop value -> step value
print(list(rng3))
# [5, 7, 9]

#  range function can be used in a for loop
for i in range(10):
    print(i, end=' ')
    
print()
# 0 1 2 3 4 5 6 7 8 9

rng4 = range(10, -10, -2) # start value -> stop value -> step value
print(list(rng4))
# [10, 8, 6, 4, 2, 0, -2, -4, -6, -8]

#  range function can be used in a for loop to iterate through a string
for ch in "hello":
    print(ch, end=' ') # h e l l o
print()

#  range returns to a iterator 
rng5 = range(10)
print(rng5)
# range(0, 10)