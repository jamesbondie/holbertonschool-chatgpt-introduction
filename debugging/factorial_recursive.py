#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number recursively.

    Function Description:
    - This function calculates the factorial of a given number using recursion.
    - The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
    - For example, factorial(4) returns 4 * 3 * 2 * 1 = 24.

    Parameters:
    - n (int): The number for which the factorial is to be calculated.

    Returns:
    - int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Command-line argument input
f = factorial(int(sys.argv[1]))
print(f)

