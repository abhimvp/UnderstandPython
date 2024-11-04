# we can create context managers using generators
import contextlib


# or from contextlib import contextmanagerF
# from contextlib there's a decorator , that allows us to decorate a generator that becomes a context manager
@contextlib.contextmanager
def file(filename, mode):
    # entry
    print("Enter")
    file = open(filename, mode)
    yield file
    # exit
    file.close()
    print("Exit")


with file("text.txt", "w") as f:
    print("Middle")
    f.write("Hello World")

# $ python contextmanager_using_generators.py
# Enter
# Middle
# Exit

# the decorator allows us to turn this generator object into a context manager
# recommended way is to use class syntax , allows you to do some more things
