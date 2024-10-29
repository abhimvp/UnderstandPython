# flattening a matrix (list of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = []

for row in matrix:
    for element in row:
        flattened.append(element)
print(matrix) 
print(flattened)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# using list comprehension
matrix_LC = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_LC = [element for row in matrix_LC for element in row]
print(matrix_LC)
print(flattened_LC)