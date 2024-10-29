# Used to denote a method inside of a class as static
#  static means it's something belongs to a class but not to an instance of the class
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")
        
    @staticmethod
    def add(x,y):
        return x + y
        #  static methods don't have access to the instance of the class
        #  and they don't have access to the class variables

print(MyClass.add(2, 3))  # Output: 5

# To call a static method, you don't need to create an instance of the class
MyClass.static_method()  # Output: This is a static method.
