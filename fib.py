# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the Nth number in the fibonacci sequence.
# https://en.wikipedia.org/wiki/Fibonacci_number
# For this function, the first two fibonacci numbers are 1 and 1
from functools import lru_cache
@lru_cache(maxsize = 100)
def fib(n):
    if type(n) != int:
        raise TypeError('Value must be a number')
    elif n < 1:
        raise ValueError('Number must be positive and non-zero')
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fib(n - 1) + fib(n - 2)

number = input('Enter a number: ')
fibnum = int(number)
print(f"{fibnum} => {fib(fibnum)}")
