import pandas as pd

file_path = "D:\PowerBI_Project\data\default+of+credit+card+clients\default of credit card clients.xls"

df = pd.read_excel(file_path, header=1)

print("=" * 50)
print("SEX VALUES")
print("=" * 50)
print(df["SEX"].value_counts().sort_index())

print("\n" + "=" * 50)
print("EDUCATION VALUES")
print("=" * 50)
print(df["EDUCATION"].value_counts().sort_index())

print("\n" + "=" * 50)
print("MARRIAGE VALUES")
print("=" * 50)
print(df["MARRIAGE"].value_counts().sort_index())

print("\n" + "=" * 50)
print("TARGET VALUES")
print("=" * 50)
print(df["default payment next month"].value_counts().sort_index())