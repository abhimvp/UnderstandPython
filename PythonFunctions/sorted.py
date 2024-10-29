# sort an iterable object in ascending
def sort_ascending(iterable, reverse=False):
    """Sorts the given iterable in ascending order."""
    sorted_list = sorted(iterable, reverse=reverse)
    return sorted_list


print(sort_ascending([5, 3, 8, 1, 2]))  # [1, 2, 3, 5, 8]
print(sort_ascending(["apple", "cherry", "banana"]))  # ['apple', 'banana', 'cherry']
print(sort_ascending((5, 3, 8, 1, 2), True))  # [8, 5, 3, 2, 1]


# pass a key - key will be a python function & apply this python function to every
# single item inside of our iterable & sort the items based on what's returned from the key function

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 20},
]

sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)
# [{'name': 'David', 'age': 20}, {'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

sorted_people_reverse = sorted(people, key=lambda person: person["age"], reverse=True)
print(sorted_people_reverse)
# [{'name': 'Charlie', 'age': 35}, {'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'David', 'age': 20}]
