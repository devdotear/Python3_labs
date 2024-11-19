#! /usr/bin/env python3
# Author: EarlE
# Version: 1.0
# Description: This script will
"""
    Docstring:
"""
import sys

var = input("Please enter an integer: ")

if var.isdecimal():
    for data in range(int(var), -1, -2):
        print(data)
else:
    print("input is not a valid number")
    sys.exit(-1)

sys.exit(0)