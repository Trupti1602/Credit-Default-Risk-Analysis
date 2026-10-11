import pandas as pd

file_path = "D:\PowerBI_Project\data\default+of+credit+card+clients\default of credit card clients.xls"

df = pd.read_excel(file_path, header=1)

print("\nDataset Shape:")
print(df.shape)

print("\nDataset first 5 rows:")
print(df.head())

print("\nDataset last 5 rows:")
print(df.tail())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())