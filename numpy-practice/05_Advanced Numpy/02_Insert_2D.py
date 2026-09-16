import numpy as np

arr = np.array([[1, 2],[4, 5]])

#insert a new row at index 1

new_arr = np.insert(arr, 1, [7, 8], axis = 0)

print(new_arr)