import pandas as pd
#Read data from CSF file in dataframe

# db = pd.read_csv("sales_data_sample.csv")
# db = pd.read_csv("sales_data_sample.csv", encoding="latin1")
# db = pd.read_csv("sales_data_sample.csv", encoding="utf-8")

#These are three ways to read a csv file.

# db = pd.read_excel("SampleSuperstore.xlsx")
db = pd.read_json("sample_Data.json")

print(db)

#gcsfs to read cloud data.