import pandas as pd

file_path = "D:\PowerBI_Project\data\default+of+credit+card+clients\default of credit card clients.xls"

df = pd.read_excel(file_path, header=1)

print("Age Analysis")
print("=" * 60)

print("\nAge Statistics")
print("-" * 60)
print(df["AGE"].describe())

print("\nAge Frequency")
print("-" * 60)
print(df["AGE"].value_counts().sort_index())

print("\nCustomers Above Age 60")
print("-" * 60)
print(df[df["AGE"] > 60][["AGE", "LIMIT_BAL", "default payment next month"]])

print("\nNumber of Customers Above Age 60:")
print((df["AGE"] > 60).sum())