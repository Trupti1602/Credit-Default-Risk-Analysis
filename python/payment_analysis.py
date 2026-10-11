import pandas as pd

file_path = "D:\PowerBI_Project\data\default+of+credit+card+clients\default of credit card clients.xls"

df = pd.read_excel(file_path, header=1)

payment_columns = [
    "PAY_0",
    "PAY_2",
    "PAY_3",
    "PAY_4",
    "PAY_5",
    "PAY_6"
]

for column in payment_columns:
    print("\n" + "=" * 50)
    print(f"{column} VALUES")
    print("=" * 50)
    print(df[column].value_counts().sort_index())

