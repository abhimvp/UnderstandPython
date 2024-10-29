# Generator comprehension


# generate the sum from all of the squares of the numbers from 0 to 999999
# Above i would need access to all of the numbers in the range 0 to 1 million,
# so it would be a very large list
# This is a generator comprehension, which allows us to generate the values on the fly , no need  of access to those values at the exact same time
# without storing them in memory all at once
# in the above example we will storing million different values in memory

# so we need one at a time and so we can add them instead of wasting memory

# that's where generator comes in - gives quick summary and returns value when needed & 
# gives next value when we ask for it and generate it on fly
# that's what this does :
sum_of_squares: int = sum(i**2 for i in range(100)) # generate value one by one - a generator expression

print(sum_of_squares) #328350