# dataclass-decorator automatically fill in the boiler plate code that you're used to writing yourself 
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str

def main():
    person = Person(name="John Doe", age=30, email="john@example.com")
    print(person)

if __name__ == "__main__":
    main()