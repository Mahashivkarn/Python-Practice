import pandas as pd

data = {
    "Name" : ['Ram', None, 'Ghanshyam', 'Kali', 'Durga', 'Mata', 'Danav'],
    "Age" : [23, None, 45, 54, 7, 19 ,34],
    "Salary" : [25000, None, 45000, 87000, 120000, 500000, 1000000],
    "Score" : [45, None, 54, 68, 75, 81,67]
    
}

n =pd.DataFrame(data)
print(n)

print(n.isnull())