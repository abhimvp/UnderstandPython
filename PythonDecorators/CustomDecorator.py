import time


def timer(func):
    """
    Takes the function as first argument and returns a new function that will replace given function
    """

    def wrapper(*args, **kwargs):
        """
        *args, **kwargs : tells the function we don't know how many arguments are going to be passed to it
        because the timer function could be used to decorate any function
        so we're going to accept any number of positional arguments and keyword arguments and pass them along
        to the original function

        """
        start_time = time.time()  # start the timer
        result = func(*args, **kwargs)  # call the function
        end_time = time.time()  # end the timer
        print(
            f"Function {func.__name__!r} took {end_time - start_time:.4f} seconds to run."
        )
        return result

    return wrapper  # returns another function


@timer
def example_function(n):
    return f"The sum is {sum(range(n))}"


print(example_function(1000000))

# without decorator


def example_function_no_decorator(n):
    return f"The sum is {sum(range(n))}"


no_decorator = timer(example_function_no_decorator)
print(no_decorator(1000000))

# $ python CustomDecorator.py
# Function 'example_function' took 0.0105 seconds to run.
# The sum is 499999500000
# Function 'example_function_no_decorator' took 0.0103 seconds to run.
# The sum is 499999500000
