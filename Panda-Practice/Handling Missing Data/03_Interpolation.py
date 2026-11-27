import pandas as pd

data = {
    "Name" : ['Ram', 'Shayam', 'Ghanshyam', 'Kali', 'Durga', 'Mata', 'Danav'],
    "Age" : [23, None, 45, 54, 7, 1000 ,342],
    "Salary" : [25000, None, 45000, 87000, 120000, 500000, 1000000],
    "Score" : [45, None, 54, 68, 75, 81,67]
    
}

n =pd.DataFrame(data)
print(n)
#method's of interpolation : linear, polynomial, time

n.interpolate(method="linear",axis =0, inplace=True)
#axis = 0 means rows mai change aur axis = 1 means coloums mai change