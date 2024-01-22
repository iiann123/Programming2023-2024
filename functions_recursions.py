# Functions and Recursion
# Author: Ubial
# 7 December 2023


def factorial(n: int) -> int:
    """Return the nth factorial.
    Done recursively.
    Example:
        factorial(3) -> 3! -> 6
    """
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return factorial(n - 1) * n


def fib(n: int) -> int:
    """Return the nth Fibonacci number.
    Calculated recursively."""
    if n in [1, 2]:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)

def fib_itr(n: int) -> int:
    """Retyrns the nth fibonacci number
    calculated iteratively"""
    last_num = 0
    num = 1
    result = 1

    for i in range(n):
        result = num + last_num

        temo = last_num
        last_num = 

# print(factorial(100))
print(fib(20))