#! /usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
BelgiumList = Belgium.split(",")

print("-" * len(Belgium))
print(":".join(BelgiumList))
print(int(BelgiumList[1]) + int(BelgiumList[3]))
print("-" * len(Belgium))