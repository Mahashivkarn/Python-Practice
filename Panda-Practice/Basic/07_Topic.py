'''
1- how big is your data
2- What are the names of coloum

shape and coloum
'''

import pandas as pd

data = {
    "Name" : ['Ram', 'Shyam', 'Ghanshyam', 'Kali', 'Durga', 'Mata', 'Danav'],
    "Age" : [23, 35, 45, 54, 56, 1000 ,342],
    "Salary" : [25000, 34000, 45000, 87000, 120000, 500000, 1000000],
    "Score" : [45, 67, 54, 68, 75, 81, 90]
    
}

n =pd.DataFrame(data)
print(n)

print(f"Shape of Dataframe is {n.shape} and coloum is {n.columns}")