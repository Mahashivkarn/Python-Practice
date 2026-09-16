'''
np.concatenate((arr1, arr2, axis = 0))
axis 0 >  vertical stackng
axis 1 > horizontal stacking
'''
import numpy as np

arr1 = np.array([1,2])

arr2 = np.array([3,4])

new_arr = np.concatenate((arr1, arr2), axis = 0)
print(new_arr)