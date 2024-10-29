# help() - function -> allows to print out the documentation of a python function
help(print)  # prints out all of the documentation for print
"""
$ python help.py
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.
"""


# Works for our on function as well
def my_function():
    """
    This function does nothing
    """
    pass


help(my_function)
"""
Help on function my_function in module __main__:

my_function()
    This function does nothing

"""
