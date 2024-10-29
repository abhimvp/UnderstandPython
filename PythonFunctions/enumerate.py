#  enumerate returns a tuple with index and value

def enumerate_example(lst):
    """
    Demonstrates the usage of enumerate function.
    Prints the index and value of each element in the given list.
    """
    for i, val in enumerate(lst):
        print(f"Index: {i}, Value: {val}")

# Example usage
my_list = [10, 20, 30, 40]
enumerate_example(my_list)
# $ python enumerate.py
# Index: 0, Value: 10
# Index: 1, Value: 20
# Index: 2, Value: 30
# Index: 3, Value: 40

for index,number in enumerate(my_list):
    print(f"Index: {index}, Value: {number}")

# $ python enumerate.py
# Index: 0, Value: 10
# Index: 1, Value: 20
# Index: 2, Value: 30
# Index: 3, Value: 40

print(list(enumerate(my_list)))# [(0, 10), (1, 20), (2, 30), (3, 40)]