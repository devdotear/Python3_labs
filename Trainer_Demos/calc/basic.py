#! /usr/bin/env python3
# Author: DCameron
# Description: This script is a basic calc app
"""
    Basic Calculator App with add, multiply, subtract
    and divide functions.
"""
import sys
import adv # SAFER
# from adv import * # Beware of namespace pollution
# from adv import power

def add(*args):
    """ Return SUM of all parameters as a float
    >>> add(4, 3, 2)
    9.0
    """
    total = 0
    for num in args:
        total += num
    return float(total)

def sub(x, z):
    """ Return result of x subtract x as a float
    >>> sub(4, 3)
    1.0
    """
    return float(x-z)

def mul(*args):
    """ Return PRODUCT of all parameters as a float
    >>> mul(4, 3)
    12.0
    >>> mul(4, 3, 2)
    24.0
    """
    total = 1
    for num in args:
        total *= num
    return float(total)

def div(x, z):
    """ Return Quotient of x divided by z to 3 decimal places
    >>> div(4, 3)
    1.333
    """
    return round(x/z, 3)

def main():
    print("***** BASIC Calculator APP *****")
    print(f"4 + 3 = {add(4, 3)}")
    print(f"4 + 3 + 2 + 1 = {add(4, 3, 2, 1)}")
    print(f"4 * 3 = {mul(4, 3)}")
    print(f"4 * 3  * 2 = {mul(4, 3, 2)}")
    print(f"4 - 3 = {sub(4, 3)}")
    print(f"4 / 3 = {div(4, 3)}")

    print(f"Advanced Mode -> 5 to the power 4 = {adv.power(5, 4)}")
    return None

# Namespace Trick
if __name__ == "__main__":
    # EXECUTE only if ran directly as a program.
    # Ignore if imported.
    import doctest
    doctest.testmod() # Scan through Docstrings and automated Tests!
    main()
    sys.exit(0)