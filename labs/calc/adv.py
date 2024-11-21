#! /usr/bin/env python3
# Author: EarlE
# Version: 1.0
# Description: This script will
"""
    Advanced Calculator app with power, modulus, and square root functions
"""

def power(x, z):
    """ Return the power of x to z """
    return float(x**z)

def mod(x, z):
    """ Return the remainder after the division of x and z as a float"""
    return float(x%z)

def sqrt(x):
    """ Return the square root of x as a float"""
    return round(x**0.5, 3)

print("#### Advanced Calc APP ###")

print(f"5 ** 2 = {power(5, 2)}")
print(f"4 % 3 = {mod(5,2)}")
print(f"\N{square root}5 = {sqrt(5)}")
