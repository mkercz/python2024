# This script creates pairs of points p = (x,y) on a plane and checks their
# properties using lambda functions. I decided to print the results. For
# this, I used the sorted method instead of point_list.sort (as suggested in
# the exercise) because sorted returns the values.

point_list = [(0.2, 3), (0.6, -4), (0.1, 0.7), (0.5, -0.8), (0.4, -0.8)]

# Check if a given point is in the unit circle.
for point in filter(lambda p: p[0] * p[0] + p[1] * p[1] <= 1, point_list):
    print(f"Point {point} belongs to the unit circle")

# Check if a given point has booth coordinates positive.
for point in filter(lambda p: p[0] > 0 and p[1] > 0, point_list):
    print(f"Point {point} has both coordinates positive")

# Sort points firstly by decreasing y, then by increasing x.
print("Points sorted by y decreasing and x increasing):",
      sorted(point_list, key=lambda p: (-p[1], p[0])))

# Sort points by the sum of |x|+|y|.
print("Points sorted by the sum of |x|+|y|):",
      sorted(point_list, key=lambda p: abs(p[0]) + abs(p[1])))