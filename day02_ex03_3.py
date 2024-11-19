#! /usr/bin/env python3
# Author: EarlE
# Version: 1.0
# Description: This script will
"""
    Docstring:
"""
import sys

year = input("Please enter a year: ")

if year.isdecimal():
    year = int(year)
    if year%4 == 0 and (year%400 == 0  or year%100 != 0) :
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
else:
    print("Please enter a year!")

sys.exit(0)