#!/usr/bin/env python

import math
import string

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)


def length_global(vector):
    return math.sqrt(vector.x**2 + vector.y**2)


Vector.length_new = length_global
v = Vector(3, 4)
print v.length_new()
print v.length()


