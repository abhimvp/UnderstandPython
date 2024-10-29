age = 23
name = "Abhi"

# prints by seperated by space
print("My name is" , name  ,"and I am" , str(age) , "years old.") 
# $ python print.py
# My name is Abhi and I am 23 years old.

# pass additional arguments to print function , modify how it works
print("My name is" , name  ,"and I am" , str(age) , "years old.",sep="|")
# rather than using space as delimiter as default it now use pipe(|) as delimiter
# $ python print.py
# My name is|Abhi|and I am|23|years old.
print("My name is" , name  ,"and I am" , str(age) , "years old.",sep=",")
# My name is,Abhi,and I am,23,years old.

# How we change what gets printed at the end of a line
print("hello world") # here by default it add new line - force the terminal to go to next line
print("hello world", name)
# hello world
# hello world Abhi

# if we want to print two things on same line
print("hello world", end=" continuation ")
print("hello world", name)
# hello world continuation hello world Abhi