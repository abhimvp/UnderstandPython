class PlayerCharacter:

    #class Object Attribute
    membership = True
    def __init__(self,name): 
        '''constructor method - Two underscores before and after 'init' -also called dunder methods ,
        this method is automatically called whenever we instantiate the class 
        Here self refers to the playerCharacter object
        '''
        self.name = name #attribute

    # def __repr__(self):
    #     '''This method returns a string representation of the object
    #     '''
    def run(self):
        print('run')

    @classmethod #decorator - allows us to define a class method - Not Used Often
    def adding_things(cls, num1, num2):
        name = 'Teddy'
        return cls(name)
    
    @staticmethod #decorator - allows us to define a static method - Not Used Often
    def adding_things2(num1, num2):
        return num1 + num2

player1 = PlayerCharacter('Abhi')
player2 = PlayerCharacter('Abhi2')
player3 = PlayerCharacter.adding_things(2, 3)
player2.attack = 50
print(player3.name)

# print(player1.membership)
# print(player1.adding_things(2,3))
# print(PlayerCharacter.adding_things(5, 6))
# print(player2.membership)
# print(player1.name)
# print(player2)
# print(player2.name)
# print(type(player1.name))
# print(player1.run())
# print(player2.attack)
# help(player1) - gives us the blueprint
# help(list)