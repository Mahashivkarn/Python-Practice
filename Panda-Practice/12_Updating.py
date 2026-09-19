import pandas as pd

data = {
    "Name" : ['Ram', 'Shyam', 'Ghanshyam', 'Kali', 'Durga', 'Mata', 'Danav'],
    "Age" : [23, 35, 45, 54, 7, 1000 ,342],
    "Salary" : [25000, 34000, 45000, 87000, 120000, 500000, 1000000],
    "Score" : [45, 67, 54, 68, 75, 81, 90]
    
}

n =pd.DataFrame(data)
print(n)

# .loc[]
#n.loc[row_index,"column_name"] = new_value
n.loc[0,"Age"] = 24
print(n)