import pandas as pd

import pandas as pd

file_path = "D:\PowerBI_Project\data\default+of+credit+card+clients\default of credit card clients.xls"

df = pd.read_excel(file_path, header=1)

df = df.rename(columns={
     "LIMIT_BAL": "Credit_Limit",
    "SEX": "Gender_Code",
    "EDUCATION": "Education_Code",
    "MARRIAGE": "Marriage_Code",
    "AGE": "Age",

    "PAY_0": "Pay_Status_Sep",
    "PAY_2": "Pay_Status_Aug",
    "PAY_3": "Pay_Status_Jul",
    "PAY_4": "Pay_Status_Jun",
    "PAY_5": "Pay_Status_May",
    "PAY_6": "Pay_Status_Apr",

    "BILL_AMT1": "Bill_Amount_Sep",
    "BILL_AMT2": "Bill_Amount_Aug",
    "BILL_AMT3": "Bill_Amount_Jul",
    "BILL_AMT4": "Bill_Amount_Jun",
    "BILL_AMT5": "Bill_Amount_May",
    "BILL_AMT6": "Bill_Amount_Apr",

    "PAY_AMT1": "Payment_Amount_Sep",
    "PAY_AMT2": "Payment_Amount_Aug",
    "PAY_AMT3": "Payment_Amount_Jul",
    "PAY_AMT4": "Payment_Amount_Jun",
    "PAY_AMT5": "Payment_Amount_May",
    "PAY_AMT6": "Payment_Amount_Apr",

    "default payment next month": "Default"
})

df["Gender"] = df["Gender_Code"].map({
    1: "Male",
    2: "Female"
})

df["Education"] = df["Education_Code"].map({
    0: "Other / Unknown",
    1: "Graduate School",
    2: "University",
    3: "High School",
    4: "Other / Unknown",
    5: "Other / Unknown",
    6: "Other / Unknown"
})


df["Marriage"] = df["Marriage_Code"].map({
    0:"Unknown",
    1:"Married",
    2:"Single",
    3:"Other"
})

df["Default_Status"] = df["Default"].map({
    0: "No Default",
    1: "Default"
})



print("\nCleaned dataset shape:", df.shape)

print("\nGender distribution:")
print(df["Gender"].value_counts())

print("\nEducation distribution:")
print(df["Education"].value_counts())

print("\nMarriage distribution:")
print(df["Marriage"].value_counts())

print("\nDefault distribution:")
print(df["Default_Status"].value_counts())

output_path = "D:\PowerBI_Project\data\clean\clean_data.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print(output_path)

