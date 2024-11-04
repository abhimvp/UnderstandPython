# file = open("file.txt", "w")
# file.write("Hello World\n")
# file.close()

# In the above code even if we add some x after f.write or file mode as read , when we run the code
# it doesn't get closed at all , another way to do that is using try and finally

# yet we can deal with above issue better way by using context managers

# with open("file.txt", "r") as file:
#     file.write(
#         "Hello World\n"
#     )  # here regardless of exception raised or not , the file will be closed automatically , will be calling
# exit method which closes our file properly
# essentially context manager is kind of like a hidden way to make sure that whenever we do one operation we do
# another operation as well regardless of what happens in between , another example is for unlocking and locking
# shared resources

# another example of context manager
from threading import Lock

# we can write our own context managers


class File:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __enter__(self):  # return us some value that we will use in context manager
        print("Enter")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):  # tb traceback
        print(f"{exc_type},{exc_val},{exc_tb}")
        print("Exit")
        self.file.close()
        return True  # if we return true , it suppresses the exception


with File("file.txt", "w") as file:
    print("Middle")
    file.write("Hello World\n")

# $ python contextmanagers.py
# Enter
# Middle
# Exit


# below we can see , we raise exeception and yet it calls the exit method , closes the file , even though exception was raised
with File("files.txt", "w") as file:
    print("Middle")
    file.write("Hello World\n")
    raise Exception("Something went wrong")
# Enter
# Middle
# Exit
# Traceback (most recent call last):
#   File "C:\Users\abhis\Desktop\PythonDev\LearnPython\UnderstandPython\ExpertPython\ContextManagers\contextmanagers.py", line 50, in <module>
#     raise Exception("Something went wrong")
# Exception: Something went wrong

# usage of type and value & traceback in exit method
# Any exception raised inside of File , gets sent to the exit function where it could be handled
# print(f"{exc_type},{exc_val},{exc_tb}")
# Enter
# Middle
# <class 'Exception'>,Something went wrong,<traceback object at 0x000001F4BC98AFC0>
# Exit
# Traceback (most recent call last):
#   File "C:\Users\abhis\Desktop\PythonDev\LearnPython\UnderstandPython\ExpertPython\ContextManagers\contextmanagers.py", line 53, in <module>
#     raise Exception("Something went wrong")
# Exception: Something went wrong
