#! /usr/bin/env python3
# Author: EarlE
# Version: 1.0
# Description: This script will
"""
    Docstring:
"""
"""
def frange1(start, stop=None, step=0.25):
    curr = float(start)
    while curr < stop:
        yield curr
        curr += step
"""

def frange(start, stop=None, step=0.25):
    if stop is None:
        stop = start
        curr = 0.0
    else:
        curr = float(start)

    while curr < stop:
        yield curr
        curr += step

