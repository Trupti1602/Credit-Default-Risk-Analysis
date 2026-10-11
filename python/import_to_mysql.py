
import pandas as pd
import mysql.connector
from pathlib import Path



PROJECT_DIR = Path(__file__).resolve().parent.parent

CSV_PATH = (
    PROJECT_DIR
    / "data"
    / "clean"
    / "credit_default_features.csv"
)


MYSQL_CONFIG = {
    "host": "localhost",
    "user": "root",
    "database": "credit_default_db"
}



df = pd.read_csv(CSV_PATH)

print("CSV loaded successfully")
print("Rows:", len(df))
print("Columns:", len(df.columns))

if len(df) != 30000:
    raise ValueError("Expected 30,000 records in the CSV.")

if not df.columns.is_unique:
    raise ValueError("CSV contains duplicate column names.")

# Convert pandas missing values to Python None for MySQL.
df = df.astype(object).where(pd.notna(df), None)

columns = df.columns.tolist()



from getpass import getpass

password = getpass("Enter your MySQL password: ")

connection = mysql.connector.connect(
    **MYSQL_CONFIG,
    password=password
)

cursor = connection.cursor()

try:
    # Confirm that the destination table is empty.
    cursor.execute("SELECT COUNT(*) FROM credit_customers")
    existing_rows = cursor.fetchone()[0]

    if existing_rows > 0:
        raise RuntimeError(
            f"Table already contains {existing_rows} rows. "
            "Import cancelled to avoid duplicate records."
        )

    # ========================================================
    # 5. Build an INSERT statement using column names
    # ========================================================

    quoted_columns = ", ".join(
        f"`{column}`" for column in columns
    )

    placeholders = ", ".join(["%s"] * len(columns))

    insert_sql = (
        f"INSERT INTO credit_customers "
        f"({quoted_columns}) "
        f"VALUES ({placeholders})"
    )

    # ========================================================
    # 6. Insert data in batches
    # ========================================================

    batch_size = 1000

    for start in range(0, len(df), batch_size):
        batch = df.iloc[start:start + batch_size]
        records = list(batch.itertuples(index=False, name=None))

        cursor.executemany(insert_sql, records)
        connection.commit()

        print(
            f"Imported {min(start + batch_size, len(df))}"
            f" / {len(df)} records"
        )

    # ========================================================
    # 7. Verify imported records
    # ========================================================

    cursor.execute("SELECT COUNT(*) FROM credit_customers")
    total_rows = cursor.fetchone()[0]

    print("\nImport completed successfully!")
    print("Rows in MySQL:", total_rows)

    cursor.execute(
        "SELECT ID, Gender, Education, Marriage, "
        "`Default`, Max_Delay_Months "
        "FROM credit_customers LIMIT 5"
    )

    print("\nSample imported records:")
    for row in cursor.fetchall():
        print(row)

    if total_rows != len(df):
        raise RuntimeError(
            f"Row count mismatch: CSV={len(df)}, MySQL={total_rows}"
        )

finally:
    cursor.close()
    connection.close()
