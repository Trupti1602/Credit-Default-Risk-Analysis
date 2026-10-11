# Credit Default Risk Analysis using SQL, Python & Power BI

## Project Overview

This project analyzes credit card customer data to identify patterns associated with payment defaults. It uses **MySQL for data analysis, Python for data cleaning and exploratory data analysis (EDA), and Power BI for visualization**.

The objective is to understand how customer demographics, credit limits, and historical payment delays relate to observed credit default risk.

## Business Problem

Credit risk teams need to understand which customer segments have higher observed default rates. This project explores historical customer data to identify patterns that may support risk assessment and decision-making.

### Key Questions

- What proportion of customers defaulted?
- How do default rates vary by gender, education, and age group?
- How are credit limits associated with default rates?
- How do historical payment delays relate to default rates?

## Tools & Technologies

- **SQL / MySQL:** Data validation, aggregation, grouping, and risk analysis
- **Python:** Pandas, NumPy, Matplotlib, Seaborn
- **Power BI:** KPI cards, charts, slicers, and dashboard design
- **Git & GitHub:** Version control and project sharing

## Dataset

The project uses the **Default of Credit Card Clients** dataset from the UCI Machine Learning Repository.

- **Records:** 30,000 customer records
- **Original attributes:** 25
- **Target variable:** Default payment next month
- **Target labels:** Default and No Default

Dataset source: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients

The original dataset and processed CSV files are excluded from this Git repository to keep it lightweight. Download the dataset from the source above to reproduce the analysis.

## Project Workflow

1. **Data inspection:** Examined the dataset structure, data types, and quality.
2. **Data cleaning:** Prepared the data for analysis using Python and Pandas.
3. **Feature engineering:** Created additional features describing historical payment delays.
4. **MySQL analysis:** Imported 30,000 customer records and performed validation and aggregation queries.
5. **Exploratory data analysis:** Examined distributions and default-rate patterns using Python.
6. **Power BI reporting:** Built KPI cards, charts, and a gender slicer to explore the results.
7. **Version control:** Published project scripts, SQL queries, and the Power BI file on GitHub.

## Key Findings

The analysis produced the following findings:

- **Overall default rate:** 22.12% (6,636 out of 30,000 customers).
- **Gender:** Male customers had a higher observed default rate (24.17%) than female customers (20.78%).
- **Education:** The High School group had an observed default rate of 25.16%, compared with 19.23% for the Graduate School group.
- **Age:** Customers under 25 had an observed default rate of 27.19%. The 25–34 age group had a rate of 20.30%.
- **Credit limit:** The below-50K credit-limit group had an observed default rate of 36.07%, while the 300K+ group had a rate of 13.68%.
- **Payment delays:** Customers with more months of delayed payments generally showed higher observed default rates.

These are descriptive findings from historical data. They indicate associations and should not be interpreted as proof of causation or as a validated predictive model.

## Power BI Dashboard

The Power BI report includes:

- Total Customers
- Total Defaults
- Overall Default Rate
- Average Credit Limit
- Customer Default Distribution
- Default Rate by Gender
- Default Rate by Education
- Default Rate by Age Group
- Default Rate by Credit Limit
- Default Rate by Number of Delayed Months
- Default Rate by Maximum Delay Status
- Gender slicer

**Dashboard file:** `powerbi/Credit_Risk_Analysis.pbix`

Note: The gender slicer filters the customer-level visuals that are connected to the customer overview data. Some charts use separate pre-aggregated summary tables and may not respond to the slicer.

## Repository Structure

```text
Credit-Default-Risk-Analysis/
├── powerbi/
│   └── Credit_Risk_Analysis.pbix
├── python/
│   ├── age_analysis.py
│   ├── categorical_analysis.py
│   ├── clean_data.py
│   ├── data_dictionary.py
│   ├── data_inspection_01.py
│   ├── eda_analysis.py
│   ├── feature_engineering.py
│   ├── import_to_mysql.py
│   ├── numerical_analysis.py
│   ├── outlier_analysis.py
│   ├── payment_analysis.py
│   └── powerbi_exports.py
├── sql/
│   └── queries.sql
├── .gitignore
└── README.md
```

## How to Run

1. Clone or download this repository.
2. Download the original dataset from the UCI source linked above.
3. Install Python and the required packages:

   ```bash
   pip install pandas numpy matplotlib seaborn mysql-connector-python xlrd
   ```

4. Run the Python scripts in the appropriate workflow order, beginning with data inspection and cleaning.
5. Configure your local MySQL connection and create the `credit_default_db` database.
6. Run the SQL queries in `sql/queries.sql` against the prepared database.
7. Open `powerbi/Credit_Risk_Analysis.pbix` in Power BI Desktop. If necessary, update the data-source paths to match your local setup.

The MySQL import script prompts for the password at runtime. Do not commit database credentials or secrets.

## Limitations

- The analysis describes historical associations and does not establish causality.
- The dashboard uses pre-aggregated summary tables for several charts, so not every chart responds to every slicer.
- The project is an exploratory risk analysis, not a production-ready credit-scoring system.
- Predictive modeling and out-of-sample validation are not included in the current version.

## Future Improvements

- Build and validate a credit-default prediction model.
- Add model evaluation using precision, recall, F1-score, and ROC-AUC.
- Improve cross-filtering across all Power BI visuals.
- Add automated data-quality checks and a reproducible pipeline.

## Author

**Trupti Gangavati**

This project demonstrates practical skills in SQL, Python-based data analysis, MySQL, Power BI, and GitHub version control.
