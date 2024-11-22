#! /usr/bin/env python3
# Author: EarlE
# Version: 1.0
# Description: This script will
"""
    Docstring:
"""

class Tank:
    def __init__(self, country, model):
        self.country = country
        self.model = model
        self._speed = 0
        self._direction = 0
        self._location = {'x': 0, 'y': 0, 'z': 0}
        self._shells = 20
        self._health = 100
        # No EXPLICIT return as it's called implicitly

    def accel(self, increase):
        self._speed += increase
        return None

    def decel(self, decrease):
        self._speed -= decrease
        return None

    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage
        return None

    # Special methods
    def __add__(self, other):
        return self._health + other._health

    def get_health(self):
        return self._health

    def set_health(self, newhealth):
        self._health = newhealth
        return None

    tank_health = property(get_health, set_health)
