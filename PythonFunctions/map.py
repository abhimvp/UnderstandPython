# Map function allows us to apply a function to every single item in an iterable object
# An iterable object is anything that you can loop through

strings = ["my", "world", "apple", "pear"]
numbers = [1, 2, 3, 4, 5]
bools = [True, False, True, False]
mixed = ["hello", 1, True, 3.14]

# get all of the different lengths of the strings in the list
lengths = map(len, strings)
# first pass the function that i want to apply to all of different items in my iterable
# then pass the iterable object itself
print(list(lengths))
# $ python map.py
# [2, 5, 5, 4]

#  it's common to use what's know as lambda function - which is a one line anonymous function
lengths_lambda = map(lambda x: x + "s", strings)
print(list(lengths_lambda))  # ['mys', 'worlds', 'apples', 'pears']

#  you can also use a lambda function with multiple arguments
add_two = map(lambda x, y: x + y, numbers, numbers)
print(list(add_two))  # [2, 4, 6, 8, 10]


def add_s(string):
    return string + "MaxVerstappen"


add_max_map = map(add_s, strings)
print(
    list(add_max_map)
)  # ['myMaxVerstappen', 'worldMaxVerstappen', 'appleMaxVerstappen', 'pearMaxVerstappen']
