# This script creates 100 random points in a unit square [0,1)x[0,1). If the
# distance of (x,y) from (0,0) is less than 1, the point is green, otherwise is
# red. The marker size is proportional to |x|+|y|.

import numpy as np
import matplotlib.pyplot as plt

n = 100
x = np.random.uniform(0, 1, n)
y = np.random.uniform(0, 1, n)

# 1 is not included in the above generations. I don't think this is a problem
# because the chance of obtaining 1.0 would be small anyway. I've checked a
# few similar methods from np.random and in all of them the high value is
# excluded. However, if one really needs 1.0, this can be done artificially,
# e.g. by using np.random.randint(0, 1000000) and then dividing the result by
# 1000000 (or whichever precision is needed).

colors = np.where(np.sqrt(x**2 + y**2) < 1, "g", "r")  # np.where is like
# if...else but for arrays (in this case x and y); it returns an array colors[n]

area = 100 * (abs(x) + abs(y))

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
