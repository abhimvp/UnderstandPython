def func(x):
    if x == 1:

        def rv():
            print("X is equal to 1")

    else:

        def rv():
            print("X is not equal to 1")

    return rv


new_func = func(1)
#  python intro_4.py
# nothing happens
new_func()  # if we call this function ,we get
# $ python intro_4.py
# X is equal to 1

new_func_2 = func(2)
new_func_2()  # if we call this function ,we get
# $ python intro_4.py
# X is equal to 1
# X is not equal to 1

# we can inspect functions and variables as everything is kind of object in python
print(id(new_func))  # 1888838199840 -> gives the memory address of the function
print(id(new_func_2))  # 1876902255232 ->  gives the memory address of the function

# usage of inspect module
import inspect

# print(inspect.getmembers(new_func))
print(inspect.getsource(new_func))  # prints the source code of the function
# $ python intro_4.py
# X is equal to 1
# X is not equal to 1
# 3081539922464
# 3081539918464
#         def rv():
#             print("X is equal to 1")

from queue import Queue  # built in data structure in python

print(inspect.getsource(Queue))  # prints the source code of the function
