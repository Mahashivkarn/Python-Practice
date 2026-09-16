import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

new_arr = np.delete(arr_2d, 1, axis =0)

print(new_arr)