'''
np.delete(array, index, axis = None)
'''
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

new_arr = np.delete(arr,3, axis = None)

print(new_arr)
