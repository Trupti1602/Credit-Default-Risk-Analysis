
from pathlib import Path

import pandas as pd


# ============================================================
# 1. PROJECT PATHS
# ============================================================

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = (
    PROJECT_DIR
    / "data"
    / "clean"
    / "credit_default_features.csv"
)

EXPORT_DIR = PROJECT_DIR / "outputs" / "powerbi"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 2. LOAD DATA
# ============================================================

df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("POWER BI DATA EXPORT")
print("=" * 60)

print(f"\nDataset loaded: {df.shape[0]:,} rows, {df.shape[1]} columns")


# ============================================================
# 3. CREATE AGE GROUPS
# ============================================================

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 24, 34, 44, 54, float("inf")],
    labels=["Under 25", "25-34", "35-44", "45-54", "55+"],
)


# ============================================================
# 4. CREATE CREDIT LIMIT GROUPS
# ============================================================

df["Credit_Limit_Group"] = pd.cut(
    df["Credit_Limit"],
    bins=[0, 50000, 100000, 200000, 300000, float("inf")],
    labels=["Below 50K", "50K-100K", "100K-200K", "200K-300K", "300K+"],
    include_lowest=True,
)


# ============================================================
# 5. CREATE REUSABLE SUMMARY FUNCTION
# ============================================================

def create_summary(data, group_column):
    """Calculate customer counts and default rates by category."""

    summary = (
        data.groupby(group_column, observed=False)
        .agg(
            Total_Customers=("Default", "count"),
            Defaults=("Default", "sum"),
        )
        .reset_index()
    )

    summary["Non_Defaults"] = (
        summary["Total_Customers"] - summary["Defaults"]
    )

    summary["Default_Rate"] = (
        summary["Defaults"] / summary["Total_Customers"] * 100
    ).round(2)

    return summary


# ============================================================
# 6. EXPORT CUSTOMER-LEVEL DATA
# ============================================================

customer_columns = [
    "ID",
    "Credit_Limit",
    "Age",
    "Gender",
    "Education",
    "Marriage",
    "Default",
    "Default_Status",
    "Max_Delay_Months",
    "Delayed_Month_Count",
    "Recent_Delay_Status",
]

customer_data = df[customer_columns].copy()

customer_data.to_csv(
    EXPORT_DIR / "customer_overview.csv",
    index=False,
)

print("\nExported: customer_overview.csv")


# ============================================================
# 7. EXPORT OVERALL KPI SUMMARY
# ============================================================

total_customers = len(df)
total_defaults = int(df["Default"].sum())
total_non_defaults = total_customers - total_defaults

kpi_summary = pd.DataFrame(
    [
        {
            "Total_Customers": total_customers,
            "Total_Defaults": total_defaults,
            "Total_Non_Defaults": total_non_defaults,
            "Default_Rate": round(
                total_defaults / total_customers * 100, 2
            ),
            "Average_Credit_Limit": round(
                df["Credit_Limit"].mean(), 2
            ),
            "Average_Age": round(df["Age"].mean(), 2),
        }
    ]
)

kpi_summary.to_csv(
    EXPORT_DIR / "overall_kpis.csv",
    index=False,
)

print("Exported: overall_kpis.csv")


# ============================================================
# 8. EXPORT CATEGORY-WISE SUMMARIES
# ============================================================

summary_columns = {
    "gender_summary.csv": "Gender",
    "education_summary.csv": "Education",
    "marriage_summary.csv": "Marriage",
    "age_group_summary.csv": "Age_Group",
    "credit_limit_summary.csv": "Credit_Limit_Group",
    "delayed_months_summary.csv": "Delayed_Month_Count",
    "maximum_delay_summary.csv": "Max_Delay_Months",
    "recent_delay_summary.csv": "Recent_Delay_Status",
}

for filename, group_column in summary_columns.items():
    summary = create_summary(df, group_column)

    summary.to_csv(
        EXPORT_DIR / filename,
        index=False,
    )

    print(f"Exported: {filename}")


# ============================================================
# 9. EXPORT COMPLETION REPORT
# ============================================================

print("\n" + "=" * 60)
print("POWER BI EXPORT COMPLETED SUCCESSFULLY")
print("=" * 60)

print(f"\nExport folder: {EXPORT_DIR}")

print("\nGenerated files:")

for file_path in sorted(EXPORT_DIR.glob("*.csv")):
    print(f"- {file_path.name} ({file_path.stat().st_size:,} bytes)")

print("\nTotal CSV files:", len(list(EXPORT_DIR.glob("*.csv"))))
