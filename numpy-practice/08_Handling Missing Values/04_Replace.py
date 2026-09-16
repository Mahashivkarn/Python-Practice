#np.isinf(array)
import numpy as np

arr =np.array([1,2,np.inf,4])

print(np.isinf(arr))

clean_arr =np.nan_to_num(arr,posinf=100,neginf=-100)

print(clean_arr)