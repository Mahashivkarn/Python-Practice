#np.isnan(array)
import numpy as np

arr =np.array([1,2,np.nan,5,np.nan])

print(np.isnan(arr))

print(np.nan == np.nan)#We cannot compare nan values.