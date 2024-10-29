# used for a method inside of a class & it will transform the first implicit parameter or argument
#  to be name or instance of class & not an individual object
#  to access class attributes

class Person:
    species = "Homo Sapiens"
    
    @classmethod
    def get_species(cls):
        print(cls)
        return cls.species
    
    def get_name(self):
        return self.species
    
    
# Usage
print(Person.get_species())  # Output: Homo Sapiens
print(Person().get_name())  # Output: Homo Sapiens
p =Person()
print(p.get_name())
print(p.get_species())