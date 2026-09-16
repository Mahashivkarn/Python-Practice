import numpy as np

arr =np.array([1,2,np.nan,5,np.nan])

clean_arr = np.nan_to_num(arr,nan =20)
print(clean_arr)

