class Meta(type):
    def __new__(self, cls_name, bases, attrs):
        print(attrs)

        a = {}
        for name, value in attrs.items():
            if name.startswith("__"):
                a[name] = value
            else:
                a[name.upper()] = value

        print(a)

        return type(cls_name, bases, a)


class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("hello")


d = Dog()

# $ python metaclasses4.py 
# {'__module__': '__main__', '__qualname__': 'Dog', 'x': 5, 'y': 8, 'hello': <function Dog.hello at 0x000001EC5467AA20>}
# {'__module__': '__main__', '__qualname__': 'Dog', 'X': 5, 'Y': 8, 'HELLO': <function Dog.hello at 0x0000026B3B97AA20>}

# print(d.x) # gives us the following error
# Traceback (most recent call last):
#   File "C:\Users\abhis\Desktop\PythonDev\LearnPython\UnderstandPython\ExpertPython\MetaClasses\metaclasses4.py", line 31, in <module>
#     print(d.x)
#           ^^^
# AttributeError: 'Dog' object has no attribute 'x'. Did you mean: 'X'?

# because we changed it to capitol X

print(d.X) #5