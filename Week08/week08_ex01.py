# This script creates the following NumPy arrays:
# (1) float from 0.0 to 1.0 step 0.1, shape=(11,)
# (2) int zeros (1 byte) with shape=(5,6)
# (3) complex with shape=(9,), powers of x = complex(0, 1): 1, x, x**2,..., x**8

import numpy as np

first_array = np.arange(0., 1.1, 0.1)
print(f"First array: {first_array}")
print(f"Shape of the first array: {first_array.shape}")

second_array = np.zeros( (5, 6), dtype="b")
print(f"Second array: {second_array}")
print(f"Shape of the second array: {second_array.shape}")
print(f"Type of the second array: {second_array.dtype}")

third_array = np.power(complex(0,1), np.arange(9))
print(f"Third array: {third_array}")
print(f"Shape of the third array: {third_array.shape}")
