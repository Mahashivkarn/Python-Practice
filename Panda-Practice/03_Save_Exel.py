import pandas as pd

data = {
    'Name' : ['Dhruv', 'Ram', 'Vir', 'Shyam'],
    'Age' : ['20','21','23', '34'],
    'Place' : ['Delhi','Mumbai','Rajasthan','Maharasthra']
}

df =pd.DataFrame(data)
print(df)

df.to_excel('output1.xlsx',index = False)