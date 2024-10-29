# the property decorator used for various methods inside of a class 
# idea here is we can treat a method as if it was an attribute & we can get 
#  access to a specific field or attribute in python
# In python we don't have access modifiers like private public and protected
# we use property to control access of  a private attribute inside of a function 

class Circle:
    def __init__(self,radius) :
        self._radius = radius
        
    @property
    def radius(self):
        print('Getter Called')
        return self._radius
    
    @radius.setter
    def radius(self, value):
        print('Setter Called')
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")
    
    @property
    def diameter(self):
        print('Diameter Getter Called')
        return 2 * self._radius
    
    @radius.deleter
    def radius(self):
        print('Radius Deleter Called')
        del self._radius
    
#Usage
c = Circle(5)
print(c.radius)  # Output: 5
print(c.diameter)  # Output: 10
c.radius = 10
print(c.radius)  # Output: 10
print(c.diameter)  # Output: 20
del c.radius
    