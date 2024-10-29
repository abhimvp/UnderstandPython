class User():
    def sign_in(self):
        print('logged in')

class Wizard(User): #Inheritance
    pass

class Archer(User):
    pass

wiz1=Wizard()
print(wiz1.sign_in())

print(isinstance(wiz1,Wizard))
print(isinstance(wiz1,User))
print(isinstance(wiz1,object))