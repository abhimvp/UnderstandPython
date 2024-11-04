# metaclasses is above the class you're creating yourself
# creating own metaclass


class Meta(type):  # when we create a metaclass , we inherit from type
    def __new__(self, cls_name, bases, attrs):  # this is called before the init method
        # first thing called when a object is created
        # new method constructs the object and init method initializes it
        print(attrs)

        return type(cls_name, bases, attrs)


class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("hello")


d = Dog()

# $ python metaclasses3.py
# {'__module__': '__main__', '__qualname__': 'Dog', 'x': 5, 'y': 8, 'hello': <function Dog.hello at 0x0000027087C7AA20>}
