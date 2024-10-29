import functools # cache the results of various function calls
# useful when we make calls to the same function with the same argumentsespecially in a recursive case


def fib(n):
    # print(n)
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
    # here we are continually calling same function nwith same value multiple times
    # this is inefficient and can be memoized to store the results of previous calls
    # this is done using functools.cache decorator
    
# print(fib(40)) # takes a bit more time to give back 102334155
# 
# @functools.cache
def fib_cache(n,cache={}):
    if n in cache:
        return cache[n]
    
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    cache[n] = fib_cache(n-1, cache) + fib_cache(n-2, cache)
    
    return cache[n]

# print(fib_cache(40)) # this is quick


@functools.cache  # this write a custom cache for us and it will automatically resize the cache
def fib_func_cache(n):
    # print(n)
    if n < 2:
        return n
    else:
        return fib_func_cache(n-1) + fib_func_cache(n-2)
    
print(fib_func_cache(40)) # this is quick

