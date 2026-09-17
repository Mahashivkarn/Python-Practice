import pandas as pd

db = pd.read_json("sample_Data.json")

print("Displaying First 10 rows.")
print(db.head(10))

print("Displaying Last 10 rows.")
print(db.tail(10))