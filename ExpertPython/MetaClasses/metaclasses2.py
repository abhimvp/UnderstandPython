class Test:
    def show(self):
        print("hi")

    pass


print(Test)
# $ python metaclasses2.py
# <class '__main__.Test'> -> here this class is an object ,
# even though it doesn't explicitly say object as below for it's instance
print(Test())
# $ python metaclasses2.py
# <__main__.Test object at 0x0000022BB5A57A10>
print(type(Test()))  # <class '__main__.Test'>


def func(self):
    self.z = 10


print(type(func))  # <class 'function'>

# so what is the type of a class
print(type(Test))  # <class 'type'>
# so essentially type is a metaclass
# so this `type` is what essentially defines rules and creates this class(Test) for us
# we type this class syntax , we will call a type constructor

# we can make a class by doing this
Test_type = type("Test_type", (), {})
# the above line is equivalent to as follows:
# class Test_type:
#     pass
print(Test_type())  # <__main__.Test_type object at 0x000001E504F57F20>
print(Test_type)  # <class '__main__.Test_type'>

Test_attributes = type("Test_attributes", (), {"x": 5})

t = Test_attributes()
t.wy = "hello"  # create attributes
print(t.x)  # 5

print(t.wy)  # hello

# inheritance
Test_inheritance = type("Test_inheritance", (Test,), {"func": func})
i = Test_inheritance()
i.show()  # hi
i.func()  # adding functions
print(i.z)  # 10
