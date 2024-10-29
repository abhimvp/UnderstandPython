# creating a dictionary
pairs: list[tuple[str, int]] = [("a",1),("b",2),("c",3)]

my_dict: dict[str, int] = {k:v for k,v in pairs}
print(my_dict) #{'a': 1, 'b': 2, 'c': 3}
def square(x):
    return x**2
my_dict : dict[str, int] = {k:square(v) for k,v in pairs}
print(my_dict) #{'a': 1, 'b': 4, 'c': 9}