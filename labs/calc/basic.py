#! /usr/bin/env python3
# Author: EarlE
# Version: 1.0
# Description: This script will
"""
    Docstring:
"""
import sys

def add(*args):
    """ Return SUM of all parameters """
    total = 0
    for num in args:
        total += num
    return float(total)


def sub(x, z):
    """ Return result of x subtract z as a float"""
    return float(x - z)


def mul(*args):
    """ Return PRODUCT of all parameters as a float"""
    total = 1
    for num in args:
        total *= num
    return float(total)


def div(x, z) -> float:
    """ Return the QUOTIENT of x divided by z to 3 decimal places"""
    return round(x / z, 3)


print("**** BASIC Calculator APP ***")

print(f"4 + 3 = {add(4, 3)}")
print(f"4 + 3 +2 + 1 = {add(4, 3, 2, 1)}")
print(f"4 * 3 = {mul(4, 3)}")
print(f"4 - 3 = {sub(4, 3)}")
print(f"4 / 3 = {div(4, 3)}")

sys.exit(0)