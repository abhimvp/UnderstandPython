# removing duplicates from a list while applying a function
nums: list[int] = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares: set[int] = {x**2 for x in nums}
print(unique_squares) #{16, 1, 4, 9}
