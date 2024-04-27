# This script creates four 2D arrays which contain:
# m1: random elements from the range of 0-9 in a shape of (4,5)
# m2: the same elements that m1 but reversed within each row
# m3: the same elements that m1 but reversed within each column
# m4: m1 with removed the first and last row and the first and last column

import numpy as np

m1 = np.random.randint(1, 9, size=(4,5))
m2 = np.fliplr(m1)  # left-right reverse
m3 = np.flipud(m1)  # up-down reverse
m4 = np.delete(
        np.delete(m1, [0,3], 0),
    [0,4], 1)  # "nested" deletion

print(f"m1:\n {m1}\n")
print(f"m2:\n {m2}\n")
print(f"m3:\n {m3}\n")
print(f"m4:\n {m4}\n")
