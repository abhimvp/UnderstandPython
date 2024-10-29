# list comprehension with functions
def square(x):
    return x**2

squared_numbers = [square(x) for x in range(1,6)]
print(squared_numbers) #[1, 4, 9, 16, 25]