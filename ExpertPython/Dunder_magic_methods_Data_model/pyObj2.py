class Person:
    def __init__(
        self, name
    ):  # this is a magic or dunder method or double underscore methods
        # $ python pyObj2.py
        # <__main__.Person object at 0x000001CAF0C57D10>
        #  here we haven't told prson what to do when we print it , so it simply shows its memory location
        self.name = name

    def __repr__(self):  # Allows us to define string representation of the object
        # $ python pyObj2.py
        # <Person: Tim>
        return f"<Person: {self.name}>"

    def __mul__(self, x):  # Allows us to define multiplication of the object
        # p = Person("Tim")
        # p* 2
        # print(p)
        # $ python pyObj2.py
        # <Person: TimTim>
        if type(x) is not int:
            raise Exception("Invalid argument, must be int")
        self.name = self.name * x

    def __call__(self, y):
        # p = Person("Tim")
        # p(4)
        # $ python pyObj2.py
        # Called this function
        # 4
        print("Called this function")
        print(y)
    
    def __len__(self):
        # p = Person("Tim")
        # print(len(p))
        # $ python pyObj2.py 
        # 3
        return len(self.name)


p = Person("Tim")

