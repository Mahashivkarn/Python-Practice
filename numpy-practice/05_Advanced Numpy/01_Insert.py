"""
np.insert(array, index, value, axis = None)
Array - what array u wanna work on
index -
value - 
axis - 0, row-wise,
axis - 1, column-wise
"""
import numpy as np

arr = np.array([10,20, 30, 40])
print(arr)

new_arr = np.insert(arr, 1, 100)
print(new_arr)