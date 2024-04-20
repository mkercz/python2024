# This script creates two vectors (implemented last week) and calculates the
# unit vector perpendicular to them. If the vectors are parallel (or zero),
# the ValueError exception is raised.

# It needs to be run from one folder above and the folder Week06 is needed.

from Week06.week06_ex01 import Vector


def find_axis(v1, v2):
    v3 = v1.cross(v2)
    if v3.length() != 0:
        v3 = v3 / v3.length()
        return v3
    else:
        raise ValueError("Vectors are parallel or zero!")


vec1 = Vector(1, 3, 5)
vec2 = Vector(4, -2, 4)

result = find_axis(vec1, vec2)

print("The unit vector perpendicular to {} and {} is {}"
      .format(vec1, vec2, result))
