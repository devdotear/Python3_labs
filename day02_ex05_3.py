#! /usr/bin/env python3
# Author: EarlE
# Version: 1.0
# Description: This script will
"""
    Docstring:
"""
# Question 3
import random
import sys
from platform import machine

lottery = []

for _ in range(6):
    lottery.append(random.randint(1,50))

print(lottery)

print("-" * 60)

# Question 4
import pprint
machines = {'user100': 'yogi',
            'user1': 'booboo',
            'user2': 'rupert',
            'user3': 'teddy',
            'user4': 'care',
            'user5': 'winnie',
            'user6': 'sooty',
            'user7': 'padders',
            'user8': 'polar',
            'user9': 'grizzly',
            'user10': 'baloo',
            'user11': 'bungle',
            'user12': 'fozzie',
            'user13': 'huggy',
            'user14': 'barnaby',
            'user15': 'hair',
            'user16': 'greppy'
            }

machines['user14'] = None
pprint.pprint(machines)

print("-" * 60)
machines['user15'] = 'cinnamon'
pprint.pprint(machines)

print("-" * 60)
machines['user17'] = machines.pop('user16')
pprint.pprint(machines)

print("-" * 60)
unallocated =[]
for user in ('user4', 'user5', 'user6'):
    unallocated += [machines.pop(user)]

pprint.pprint(machines)
pprint.pprint(unallocated)

print("-" * 60)
machines['user8'] = [machines['user8'], 'kodiak']
pprint.pprint(machines)

print("-" * 60)
for kv in machines.items():
    pprint.pprint(kv)

print("-" * 60)
print("Unallocated machines:", sorted(unallocated))


sys.exit(0)