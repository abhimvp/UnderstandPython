import random

print(random)
# $ python built_in_modules.py
# <module 'random' from 'C:\\Users\\abhis\\AppData\\Roaming\\uv\\python\\cpython-3.12.0-windows-x86_64-none\\Lib\\random.py'>
# help(random)
# print(dir(random))  # gives us all the available methods and attributes of the module
# $ python built_in_modules.py
# <module 'random' from 'C:\\Users\\abhis\\AppData\\Roaming\\uv\\python\\cpython-3.12.0-windows-x86_64-none\\Lib\\random.py'>
# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence',
# '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',
# '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_fabs', '_floor', '_index', '_inst', '_isfinite', '_lgamma',
# '_log', '_log2', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn',
# 'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate',
# 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular',
# 'uniform', 'vonmisesvariate', 'weibullvariate']

print(random.random())  # gives us a random number between 0 and 1
# $ python built_in_modules.py
# 0.8067904205785704
print(random.randint(1, 10))  # gives us a random integer between 1 and 10
print(random.choice([1, 2, 3, 4, 5]))  # gives us a random element from the list
my_list = [1, 2, 3, 4, 5]
print(random.sample(my_list, 3))  # gives us a random sample of 3 elements from the list
print(random.shuffle(my_list))  # shuffles the list in place
print(my_list)  # prints the shuffled list

import sys

print(sys)  # gives us the sys module - <module 'sys' (built-in)>
print(sys.path)  # gives us the list of paths where Python looks for modules - $ python built_in_modules.py

first = sys.argv[1]
second = sys.argv[2]
print(first)  # prints the first argument passed to the script  
print(second)  # prints the second argument passed to the script
