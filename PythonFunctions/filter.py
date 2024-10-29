# it will take every single item in our iterable object &
# it will pass it to some function  - it's a filter function
# / if that function returns true, it will keep that item in the list
# / if that function returns false, it will filter it out of the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))  # [2, 4, 6, 8, 10]


def longer_than_4(string):
    return len(string) > 4


strings = ["hello", "my", "name", "is", "abhishek"]
long_strings = filter(longer_than_4, strings)
print(list(long_strings))
# ['hello', 'abhishek']
