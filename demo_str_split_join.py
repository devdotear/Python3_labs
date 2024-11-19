#! /usr/bin/env python3
# Author: EarlE
# Version: 1.0
# Description: This script will
"""
    Docstring:
"""

line = "root:x:0:0:My Super User:/root:/bin/ksh"

fields = line.split(":")
print(fields)

fields[4] = "The Admin"
fields[6] = "/bin/bash"
new_line = ":".join(fields)

print(new_line)