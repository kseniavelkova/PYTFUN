def lucas(l):
    if l == 0:
        return 2
    if l == 1:
        return 1
    return lucas(l - 1) + lucas(l - 2)


n = 0
print(lucas(n))

from time import time


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


from functools import wraps


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args not in cache:
            print(f"Calling for {func.__name__}({args})")
            cache[args] = func(*args, **kwargs)
        else:
            print(f"Using cached result for {func.__name__}({args})")
        return cache[args]

    return wrapper


# @timer_func
@memoize
def lucas(l):
    if l == 0:
        return 2
    if l == 1:
        return 1
    return lucas(l - 1) + lucas(l - 2)


# n = 0
# print(lucas(n))

# print(lucas(35))

import math


def primefactors(n):
    # even number divisible
    while n % 2 == 0:
        print(2),
        n = n / 2

    # n became odd
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while (n % i == 0):
            print(i)
            n = n / i

    if n > 2:
        print(n)


# --n = int(input("Enter the number for calculating the prime factors :\n"))
primefactors(lucas(60))
