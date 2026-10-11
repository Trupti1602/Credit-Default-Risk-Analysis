
import pandas as pd
from pathlib import Path

# ============================================================
# 1. Set project paths reliably
# ============================================================

# Project root is the parent of the python folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = PROJECT_DIR / "data" / "clean" / "clean_data.csv"
OUTPUT_PATH = PROJECT_DIR / "data" / "clean" / "credit_default_features.csv"

# ============================================================
# 2. Load cleaned dataset
# ============================================================

df = pd.read_csv(INPUT_PATH)

print("Original Dataset Shape:", df.shape)


# ============================================================
# 3. Define monthly payment status columns
# ============================================================

payment_status_columns = [
    "Pay_Status_Sep",
    "Pay_Status_Aug",
    "Pay_Status_Jul",
    "Pay_Status_Jun",
    "Pay_Status_May",
    "Pay_Status_Apr"
]

# ============================================================
# 4. Feature 1: Maximum delay across six months
# ============================================================

df["Max_Delay_Months"] = (
    df[payment_status_columns]
    .clip(lower=0)
    .max(axis=1)
)

# ============================================================
# 5. Feature 2: Number of months with positive delay
# ============================================================

df["Delayed_Month_Count"] = (
    df[payment_status_columns]
    .gt(0)
    .sum(axis=1)
)

# ============================================================
# 6. Feature 3: Most recent month's payment status
# ============================================================

df["Recent_Delay_Status"] = df["Pay_Status_Sep"]

# ============================================================
# 7. Display feature distributions
# ============================================================

print("\nMaximum Delay in Months Distribution")
print("=" * 60)
print(df["Max_Delay_Months"].value_counts().sort_index())

print("\nDelayed Month Count Distribution")
print("=" * 60)
print(df["Delayed_Month_Count"].value_counts().sort_index())

print("\nRecent Delay Status Distribution")
print("=" * 60)
print(df["Recent_Delay_Status"].value_counts().sort_index())

# ============================================================
# 8. Validate engineered features
# ============================================================

feature_columns = [
    "Max_Delay_Months",
    "Delayed_Month_Count",
    "Recent_Delay_Status"
]

print("\nFeature Validation")
print("=" * 60)

print("Total records:", len(df))

print(
    "Missing values in engineered features:",
    df[feature_columns].isnull().sum().sum()
)

print(
    "Delayed month count valid:",
    df["Delayed_Month_Count"].between(0, 6).all()
)

print(
    "Maximum delay valid:",
    df["Max_Delay_Months"].between(0, 8).all()
)

print(
    "Original cleaned dataset exists:",
    INPUT_PATH.exists()
)

# ============================================================
# 9. Save feature-engineered dataset
# ============================================================

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(OUTPUT_PATH, index=False)

print("\nFeature-Engineered Dataset Saved Successfully!")
print("Output Path:", OUTPUT_PATH)
print("Final Dataset Shape:", df.shape)

# ============================================================
# 10. Verify saved dataset
# ============================================================

saved_df = pd.read_csv(OUTPUT_PATH)

print("\nSaved File Verification")
print("=" * 60)

print("Saved dataset shape:", saved_df.shape)

print(
    "All engineered features present:",
    all(column in saved_df.columns for column in feature_columns)
)

print(
    "Saved dataset has 30,000 records:",
    len(saved_df) == 30000
)