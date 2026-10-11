import pandas as pd

file_path = "D:\PowerBI_Project\data\default+of+credit+card+clients\default of credit card clients.xls"

df = pd.read_excel(file_path, header=1)

data_dictionary = {
    "ID": "Unique customer ID",
    "LIMIT_BAL": "Credit limit assigned to the customer",
    "SEX": "Gender of the customer",
    "EDUCATION": "Education level of the customer",
    "MARRIAGE": "Marital status of the customer",
    "AGE": "Age of the customer",

    "PAY_0": "Repayment status in September",
    "PAY_2": "Repayment status in August",
    "PAY_3": "Repayment status in July",
    "PAY_4": "Repayment status in June",
    "PAY_5": "Repayment status in May",
    "PAY_6": "Repayment status in April",

    "BILL_AMT1": "Bill statement amount in September",
    "BILL_AMT2": "Bill statement amount in August",
    "BILL_AMT3": "Bill statement amount in July",
    "BILL_AMT4": "Bill statement amount in June",
    "BILL_AMT5": "Bill statement amount in May",
    "BILL_AMT6": "Bill statement amount in April",

    "PAY_AMT1": "Previous payment amount in September",
    "PAY_AMT2": "Previous payment amount in August",
    "PAY_AMT3": "Previous payment amount in July",
    "PAY_AMT4": "Previous payment amount in June",
    "PAY_AMT5": "Previous payment amount in May",
    "PAY_AMT6": "Previous payment amount in April",

    "default payment next month": "Whether the customer defaulted on the next month's payment"
}

print("DATA DICTIONARY")
print("=" * 80)

for column in df.columns:
    print(f"{column:<30} : {data_dictionary.get(column, 'Description not available')}")