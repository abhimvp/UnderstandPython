def make_class(x):
    class Dog:
        def __init__(self, name):
            self.name = name

        def print_value(self):
            print(x)

    return Dog


cls = make_class(10)
print(cls)

# $ python intro_2.py
# <class '__main__.make_class.<locals>.Dog'>

# here the compiler doesn't check if it's valid or not
# here we can define class inside a function that's just the way python works

d = cls("Abhi")
d.print_value()

# $ python intro_2.py
# <class '__main__.make_class.<locals>.Dog'>
# 10
