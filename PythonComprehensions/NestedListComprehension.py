# Building a 3D list
import pprint
printer = pprint.PrettyPrinter() # gives us an output easier to read

lst = []
for a in range(5):
    l1 = []
    for b in range(5):
        l2 = []
        for c in range(5):
            l2.append(c)
        l1.append(l2)
    lst.append(l1)

printer.pprint(lst)
# [[[0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4]],
#  [[0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4]],
#  [[0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4]],
#  [[0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4]],
#  [[0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4]]]

# using list comprehension - less intimidating than above for loop
lst_lc = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]
printer.pprint(lst_lc)