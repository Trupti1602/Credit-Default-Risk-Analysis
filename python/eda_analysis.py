
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. PROJECT PATHS
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = (
    PROJECT_DIR
    / "data"
    / "clean"
    / "credit_default_features.csv"
)

CHART_DIR = PROJECT_DIR / "outputs" / "charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# 2. LOAD DATASET
# --------------------------------------------------

df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("CREDIT DEFAULT RISK ANALYSIS")
print("=" * 60)

# --------------------------------------------------
# 3. BASIC DATA VALIDATION
# --------------------------------------------------

print("\n1. DATASET SHAPE")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n2. COLUMN NAMES")
print(df.columns.tolist())

print("\n3. FIRST FIVE RECORDS")
print(df.head())

print("\n4. DATA TYPES")
print(df.dtypes)

print("\n5. MISSING VALUES")
print(df.isnull().sum().sort_values(ascending=False))

print("\n6. DUPLICATE CUSTOMER IDs")
print(f"Duplicate IDs: {df['ID'].duplicated().sum()}")

print("\n7. DEFAULT DISTRIBUTION")
print(df["Default_Status"].value_counts())

print("\n8. DEFAULT RATE")
default_rate = (df["Default"] == 1).mean() * 100
print(f"Default rate: {default_rate:.2f}%")

print("\n9. NUMERICAL SUMMARY")
print(df.describe().round(2))

print("\n" + "=" * 60)
print("INITIAL DATA VALIDATION COMPLETED")
print("=" * 60)

# --------------------------------------------------
# 4. DEFAULT DISTRIBUTION AND CHART
# --------------------------------------------------

default_counts = df["Default_Status"].value_counts()

print("\n10. DEFAULT DISTRIBUTION WITH PERCENTAGES")

for status, count in default_counts.items():
    percentage = count / len(df) * 100
    print(f"{status}: {count:,} customers ({percentage:.2f}%)")

fig, ax = plt.subplots(figsize=(8, 5))

default_counts.plot(kind="bar", ax=ax)

ax.set_title("Credit Card Customer Default Distribution")
ax.set_xlabel("Customer Status")
ax.set_ylabel("Number of Customers")
ax.tick_params(axis="x", rotation=0)

fig.tight_layout()

chart_path = CHART_DIR / "default_distribution.png"
fig.savefig(chart_path, dpi=300, bbox_inches="tight")
plt.close(fig)

print(f"\nChart saved to: {chart_path}")

# --------------------------------------------------
# 5. DEFAULT RATE BY GENDER
# --------------------------------------------------

print("\n11. DEFAULT RATE BY GENDER")

gender_analysis = (
    df.groupby("Gender")
    .agg(
        Total_Customers=("Default", "count"),
        Defaults=("Default", "sum"),
        Default_Rate=("Default", "mean"),
    )
    .reset_index()
)

gender_analysis["Default_Rate"] *= 100

print(gender_analysis.round(2).to_string(index=False))

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(
    gender_analysis["Gender"],
    gender_analysis["Default_Rate"],
)

ax.set_title("Default Rate by Gender")
ax.set_xlabel("Gender")
ax.set_ylabel("Default Rate (%)")

fig.tight_layout()

chart_path = CHART_DIR / "default_rate_by_gender.png"
fig.savefig(chart_path, dpi=300, bbox_inches="tight")
plt.close(fig)

print(f"\nChart saved to: {chart_path}")

# --------------------------------------------------
# 6. COMPLETION
# --------------------------------------------------

print("\n" + "=" * 60)
print("PYTHON EDA STEPS COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nTEST: Python reached the end of the file")




# --------------------------------------------------
# 7. DEFAULT RATE BY EDUCATION
# --------------------------------------------------

print("\n12. DEFAULT RATE BY EDUCATION")

education_analysis = (
    df.groupby("Education")
    .agg(
        Total_Customers=("Default", "count"),
        Defaults=("Default", "sum"),
        Default_Rate=("Default", "mean"),
    )
    .reset_index()
)

education_analysis["Default_Rate"] *= 100

print(education_analysis.round(2).to_string(index=False))

# Create the chart
fig, ax = plt.subplots(figsize=(9, 5))

ax.bar(
    education_analysis["Education"],
    education_analysis["Default_Rate"],
)

ax.set_title("Default Rate by Education Level")
ax.set_xlabel("Education Level")
ax.set_ylabel("Default Rate (%)")
ax.tick_params(axis="x", rotation=20)

fig.tight_layout()

chart_path = CHART_DIR / "default_rate_by_education.png"
fig.savefig(chart_path, dpi=300, bbox_inches="tight")
plt.close(fig)

print(f"\nChart saved to: {chart_path}")




# --------------------------------------------------
# 8. DEFAULT RATE BY AGE GROUP
# --------------------------------------------------

print("\n13. DEFAULT RATE BY AGE GROUP")

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 24, 34, 44, 54, float("inf")],
    labels=[
        "Under 25",
        "25-34",
        "35-44",
        "45-54",
        "55+",
    ],
)

age_analysis = (
    df.groupby("Age_Group", observed=False)
    .agg(
        Total_Customers=("Default", "count"),
        Defaults=("Default", "sum"),
        Default_Rate=("Default", "mean"),
    )
    .reset_index()
)

age_analysis["Default_Rate"] *= 100

print(age_analysis.round(2).to_string(index=False))

# Create the chart
fig, ax = plt.subplots(figsize=(9, 5))

ax.bar(
    age_analysis["Age_Group"].astype(str),
    age_analysis["Default_Rate"],
)

ax.set_title("Default Rate by Age Group")
ax.set_xlabel("Age Group")
ax.set_ylabel("Default Rate (%)")

fig.tight_layout()

chart_path = CHART_DIR / "default_rate_by_age_group.png"
fig.savefig(chart_path, dpi=300, bbox_inches="tight")
plt.close(fig)

print(f"\nChart saved to: {chart_path}")



# --------------------------------------------------
# 9. DEFAULT RATE BY CREDIT LIMIT
# --------------------------------------------------

print("\n14. DEFAULT RATE BY CREDIT LIMIT")

df["Credit_Limit_Group"] = pd.cut(
    df["Credit_Limit"],
    bins=[0, 50000, 100000, 200000, 300000, float("inf")],
    labels=[
        "Below 50K",
        "50K-100K",
        "100K-200K",
        "200K-300K",
        "300K+",
    ],
    include_lowest=True,
)

credit_analysis = (
    df.groupby("Credit_Limit_Group", observed=False)
    .agg(
        Total_Customers=("Default", "count"),
        Defaults=("Default", "sum"),
        Default_Rate=("Default", "mean"),
    )
    .reset_index()
)

credit_analysis["Default_Rate"] *= 100

print(credit_analysis.round(2).to_string(index=False))

# Create the chart
fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(
    credit_analysis["Credit_Limit_Group"].astype(str),
    credit_analysis["Default_Rate"],
)

ax.set_title("Default Rate by Credit Limit")
ax.set_xlabel("Credit Limit Group")
ax.set_ylabel("Default Rate (%)")

fig.tight_layout()

chart_path = CHART_DIR / "default_rate_by_credit_limit.png"
fig.savefig(chart_path, dpi=300, bbox_inches="tight")
plt.close(fig)

print(f"\nChart saved to: {chart_path}")



# ============================================================
# 8. DEFAULT RATE BY DELAYED MONTH COUNT
# ============================================================

print("\n15. DEFAULT RATE BY DELAYED MONTH COUNT")

delay_analysis = (
    df.groupby("Delayed_Month_Count")
    .agg(
        Total_Customers=("Default", "count"),
        Defaults=("Default", "sum"),
        Default_Rate=("Default", "mean"),
    )
    .reset_index()
)

delay_analysis["Default_Rate"] *= 100

print(delay_analysis.round(2).to_string(index=False))

# Create chart
fig, ax = plt.subplots(figsize=(9, 5))

ax.bar(
    delay_analysis["Delayed_Month_Count"].astype(str),
    delay_analysis["Default_Rate"],
)

ax.set_title("Default Rate by Number of Delayed Months")
ax.set_xlabel("Number of Delayed Months")
ax.set_ylabel("Default Rate (%)")

fig.tight_layout()

chart_path = CHART_DIR / "default_rate_by_delayed_months.png"
fig.savefig(chart_path, dpi=300, bbox_inches="tight")
plt.close(fig)

print(f"\nChart saved to: {chart_path}")





# ============================================================
# 9. DEFAULT RATE BY MAXIMUM PAYMENT DELAY
# ============================================================

print("\n16. DEFAULT RATE BY MAXIMUM PAYMENT DELAY")

max_delay_analysis = (
    df.groupby("Max_Delay_Months")
    .agg(
        Total_Customers=("Default", "count"),
        Defaults=("Default", "sum"),
        Default_Rate=("Default", "mean"),
    )
    .reset_index()
)

max_delay_analysis["Default_Rate"] *= 100

print(max_delay_analysis.round(2).to_string(index=False))

# Create and save chart
fig, ax = plt.subplots(figsize=(9, 5))

ax.bar(
    max_delay_analysis["Max_Delay_Months"].astype(str),
    max_delay_analysis["Default_Rate"],
)

ax.set_title("Default Rate by Maximum Payment Delay")
ax.set_xlabel("Maximum Payment Delay Status")
ax.set_ylabel("Default Rate (%)")

fig.tight_layout()

chart_path = CHART_DIR / "default_rate_by_max_delay.png"

fig.savefig(
    chart_path,
    dpi=300,
    bbox_inches="tight",
)

plt.close(fig)

print(f"\nChart saved to: {chart_path}")




# ============================================================
# 10. CONSOLIDATED BUSINESS INSIGHTS
# ============================================================

print("\n" + "=" * 65)
print("CONSOLIDATED BUSINESS INSIGHTS")
print("=" * 65)

total_customers = len(df)
total_defaults = int(df["Default"].sum())
overall_default_rate = df["Default"].mean() * 100

print(f"\nTotal customers: {total_customers:,}")
print(f"Total defaults: {total_defaults:,}")
print(f"Overall default rate: {overall_default_rate:.2f}%")

# Highest default-rate gender
gender_summary = (
    df.groupby("Gender")["Default"]
    .mean()
    .mul(100)
)

print(
    "\nGender with higher default rate: "
    f"{gender_summary.idxmax()} "
    f"({gender_summary.max():.2f}%)"
)

# Highest default-rate education category
education_summary = (
    df.groupby("Education")["Default"]
    .mean()
    .mul(100)
)

print(
    "\nEducation category with highest default rate: "
    f"{education_summary.idxmax()} "
    f"({education_summary.max():.2f}%)"
)

# Highest default-rate age group
age_summary = (
    df.groupby("Age_Group")["Default"]
    .mean()
    .mul(100)
)

print(
    "\nAge group with highest default rate: "
    f"{age_summary.idxmax()} "
    f"({age_summary.max():.2f}%)"
)

# Highest default-rate credit-limit group
credit_summary = (
    df.groupby("Credit_Limit_Group")["Default"]
    .mean()
    .mul(100)
)

print(
    "\nCredit-limit group with highest default rate: "
    f"{credit_summary.idxmax()} "
    f"({credit_summary.max():.2f}%)"
)

# Highest default-rate maximum delay category
delay_summary = (
    df.groupby("Max_Delay_Months")["Default"]
    .mean()
    .mul(100)
)

highest_delay = delay_summary.idxmax()

print(
    "\nMaximum-delay category with highest default rate: "
    f"{highest_delay} "
    f"({delay_summary.max():.2f}%)"
)

print("\n" + "=" * 65)
print("BUSINESS INSIGHTS GENERATED SUCCESSFULLY")
print("=" * 65)
