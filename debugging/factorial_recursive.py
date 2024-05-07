#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculate the factorial of a given number using recursion.

    Parameters:
    - n: integer representing the number for which factorial needs to be calculated.

    Returns:
    Integer value representing the factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
