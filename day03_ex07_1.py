#! /usr/bin/env python3
# Author: EarlE
# Version: 1.0
# Description: This script will
"""
    Docstring:
"""
import re

all_ports = set(range(1, 201))
used_ports = set()

with open(r"C:\Windows\System32\drivers\etc\services") as fh_in:
    for line in fh_in:
        if line.isspace() or line.startswith(r"#"): continue
            #port = re.search(r"")
        # print(line, end="")
        match = re.search(r"\d{1,3}/", line)

        if match:
            #used_ports.add(line[match.start(), match.end()])
            used_ports.add(int(re.sub(r"/", "", match.group())))

unused_ports = all_ports - used_ports
print((unused_ports))