# This scripts creates three arrays which contain:
# v1: 10 random elements from the range 0-9
# v2: every second element from v1 (odd indices)
# v3: the same elements as in v1 but in reverse order

import numpy as np

v1 = np.random.randint(1, 9, size=10)
v2 = v1[1::2]  # slicing: start from index = 1 and take every 2nd element
v3 = v1[::-1]  # slicing method, -1 means reverse order

# alternatively, using numpy:
# v3 = np.flip(v1)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v3: {v3}")
