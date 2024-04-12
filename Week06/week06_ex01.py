#This script implements a 3D vector class.

import math


class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):  # return string "Vector(x, y, z)"
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):  # v == w (we need to compare x, y, z, not objects)
        return (self.x == other.x) and (self.y == other.y) and (
                    self.z == other.z)

    def __ne__(self, other):  # v != w
        return not self == other

    def __add__(self, other):  # v + w
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):  # v - w
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):  # return the dot product (number)
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):  # return the cross product (Vector)
        return Vector((self.y * other.z) - (self.z * other.y),
                      (self.z * other.x) - (self.x * other.z),
                      (self.x * other.y) - (self.y * other.x))

    def length(self):  # the length of the vector
        return math.sqrt((self.x ** 2 + self.y ** 2 + self.z ** 2))

    def __hash__(self):  # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))  # recommended


# Exemplary tests. Change values in your tests.
import math

v = Vector(4, 2, -4)
w = Vector(1, 6, 3)
assert v != w
assert v + w == Vector(5, 8, -1)
assert v - w == Vector(3, -4, -7)
assert v * w == 4
assert v.cross(w) == Vector(30, -16, 22)
assert v.length() == 6
S = set([v, v, w])
assert len(S) == 2

print("Tests passed")
