#! /usr/bin/env python3
# Author:
# Version:
# Description:

from math import pi, tan, cos

y_0 = 1
v_0 = 44
deg = 80
x = 0.5
g = 9.81

theta = deg * (pi/180)

y = y_0 + (x * tan(theta)) - ((g * x**2)/(2 * (v_0 * cos(theta)**2)))

print(y)
