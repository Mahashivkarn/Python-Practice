import pandas as pd

data={
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}

n=pd.DataFrame(data)
print('Before Interpolation:\n')
print(n)

n['Value']=n['Value'].interpolate(method="linear")             
print("After Interpolation:\n")
print(n)