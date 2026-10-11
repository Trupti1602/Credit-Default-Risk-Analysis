
CREATE DATABASE credit_default_db;

USE credit_default_db;

SELECT DATABASE();


USE credit_default_db;

CREATE TABLE credit_customers (
    ID INT PRIMARY KEY,
    Gender_Code INT,
    Gender VARCHAR(20),
    Education_Code INT,
    Education VARCHAR(30),
    Marriage_Code INT,
    Marriage VARCHAR(20),
    `Default` INT,
    Default_Status VARCHAR(20),
    Credit_Limit DECIMAL(12,2),
    Age INT,
    Pay_Status_Sep INT,
    Pay_Status_Aug INT,
    Pay_Status_Jul INT,
    Pay_Status_Jun INT,
    Pay_Status_May INT,
    Pay_Status_Apr INT,
    Bill_Amount_Sep DECIMAL(14,2),
    Bill_Amount_Aug DECIMAL(14,2),
    Bill_Amount_Jul DECIMAL(14,2),
    Bill_Amount_Jun DECIMAL(14,2),
    Bill_Amount_May DECIMAL(14,2),
    Bill_Amount_Apr DECIMAL(14,2),
    Payment_Amount_Sep DECIMAL(14,2),
    Payment_Amount_Aug DECIMAL(14,2),
    Payment_Amount_Jul DECIMAL(14,2),
    Payment_Amount_Jun DECIMAL(14,2),
    Payment_Amount_May DECIMAL(14,2),
    Payment_Amount_Apr DECIMAL(14,2),
    Max_Delay_Months INT,
    Delayed_Month_Count INT,
    Recent_Delay_Status INT
);


DESCRIBE credit_customers;

USE credit_default_db;

select * from credit_customers limit 5;


USE credit_default_db;

-- Check the total number of records
SELECT COUNT(*) AS total_customers
FROM credit_customers;

-- Check the default distribution
SELECT
    `Default`,
    Default_Status,
    COUNT(*) AS customer_count
FROM credit_customers
GROUP BY `Default`, Default_Status
ORDER BY `Default`;

-- Preview the imported records
SELECT
    ID,
    Gender,
    Education,
    Marriage,
    Credit_Limit,
    Max_Delay_Months,
    Delayed_Month_Count,
    `Default`
FROM credit_customers
LIMIT 10;



-- Calculate the overall default rate 
SELECT COUNT(*) AS total_customers, SUM(CASE WHEN `Default` = 1 THEN 1 ELSE 0 END) AS defaulted_customers, ROUND( 100.0 * SUM(CASE WHEN `Default` = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS default_rate_percentage
FROM credit_customers;

-- comparing default and non-default customers
select Default_Status , count(*) AS customer_count, round( 100.0 * count(*) / (select count(*) from credit_customers), 2) as Percentage from credit_customers
group by default_status
order by customer_count desc;


-- Analyze default rate by education level
SELECT
    Education,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN `Default` = 1 THEN 1 ELSE 0 END)
        AS defaulted_customers,
    ROUND(
        100.0 * SUM(CASE WHEN `Default` = 1 THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS default_rate_percentage
FROM credit_customers
GROUP BY Education
ORDER BY default_rate_percentage DESC;

-- Analyze default rate by age group

SELECT
    CASE
        WHEN Age < 25 THEN 'Under 25'
        WHEN Age BETWEEN 25 AND 34 THEN '25-34'
        WHEN Age BETWEEN 35 AND 44 THEN '35-44'
        WHEN Age BETWEEN 45 AND 54 THEN '45-54'
        ELSE '55 and above'
    END AS age_group,

    COUNT(*) AS total_customers,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaulted_customers,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate_percentage

FROM credit_customers

GROUP BY age_group

ORDER BY
    CASE age_group
        WHEN 'Under 25' THEN 1
        WHEN '25-34' THEN 2
        WHEN '35-44' THEN 3
        WHEN '45-54' THEN 4
        ELSE 5
    END;
    
-- Analyze default rate by gender

SELECT
    Gender,
    COUNT(*) AS total_customers,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaulted_customers,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate_percentage

FROM credit_customers

GROUP BY Gender

ORDER BY default_rate_percentage DESC;

-- Analyze default rates by credit limit

SELECT
    CASE
        WHEN Credit_Limit < 50000 THEN 'Below 50K'
        WHEN Credit_Limit < 100000 THEN '50K-100K'
        WHEN Credit_Limit < 200000 THEN '100K-200K'
        WHEN Credit_Limit < 300000 THEN '200K-300K'
        ELSE '300K and above'
    END AS credit_limit_group,

    COUNT(*) AS total_customers,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaulted_customers,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate_percentage

FROM credit_customers

GROUP BY credit_limit_group

ORDER BY
    CASE credit_limit_group
        WHEN 'Below 50K' THEN 1
        WHEN '50K-100K' THEN 2
        WHEN '100K-200K' THEN 3
        WHEN '200K-300K' THEN 4
        ELSE 5
    END;
    
-- Analyze repayment behaviour

SELECT
    Pay_Status_Sep AS september_payment_status,

    COUNT(*) AS total_customers,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaulted_customers,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate_percentage

FROM credit_customers

GROUP BY Pay_Status_Sep

ORDER BY Pay_Status_Sep;


-- Compare default rates by number of delayed months

SELECT
    Delayed_Month_Count AS delayed_months,

    COUNT(*) AS total_customers,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaulted_customers,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate_percentage

FROM credit_customers

GROUP BY Delayed_Month_Count

ORDER BY Delayed_Month_Count;

-- Analyze the relationship between maximum delay and default

SELECT
    Max_Delay_Months AS maximum_delay_months,

    COUNT(*) AS total_customers,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaulted_customers,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate_percentage

FROM credit_customers

GROUP BY Max_Delay_Months

ORDER BY Max_Delay_Months;


-- Compare default rates by marriage status

SELECT
    Marriage,
    COUNT(*) AS total_customers,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaulted_customers,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate_percentage

FROM credit_customers

GROUP BY Marriage

ORDER BY default_rate_percentage DESC;


-- compare default rate by education and gender

SELECT
    Education,
    Gender,

    COUNT(*) AS total_customers,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaulted_customers,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate_percentage

FROM credit_customers

GROUP BY Education, Gender

ORDER BY Education, default_rate_percentage DESC;



-- Compare default rates by credit limit and repayment delay
SELECT
    CASE
        WHEN Credit_Limit < 50000 THEN 'Below 50K'
        WHEN Credit_Limit < 100000 THEN '50K-100K'
        WHEN Credit_Limit < 200000 THEN '100K-200K'
        WHEN Credit_Limit < 300000 THEN '200K-300K'
        ELSE '300K and above'
    END AS credit_limit_group,

    Pay_Status_Sep AS september_payment_status,

    COUNT(*) AS total_customers,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaulted_customers,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate_percentage

FROM credit_customers

GROUP BY
    credit_limit_group,
    Pay_Status_Sep

ORDER BY
    CASE credit_limit_group
        WHEN 'Below 50K' THEN 1
        WHEN '50K-100K' THEN 2
        WHEN '100K-200K' THEN 3
        WHEN '200K-300K' THEN 4
        ELSE 5
    END,
    Pay_Status_Sep;
    
-- Analyze default rates by recent delay and delay frequency
SELECT
    Recent_Delay_Status,
    Delayed_Month_Count,

    COUNT(*) AS total_customers,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaulted_customers,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate_percentage

FROM credit_customers

GROUP BY
    Recent_Delay_Status,
    Delayed_Month_Count

HAVING COUNT(*) >= 30

ORDER BY
    Recent_Delay_Status,
    Delayed_Month_Count;
    
-- Build a consolidated risk summary

SELECT
    Default_Status,
    COUNT(*) AS total_customers,

    ROUND(
        100.0 * COUNT(*) /
        (SELECT COUNT(*) FROM credit_customers),
        2
    ) AS percentage_of_customers,

    ROUND(AVG(Credit_Limit), 2) AS average_credit_limit,

    ROUND(AVG(Age), 2) AS average_age,

    ROUND(AVG(Delayed_Month_Count), 2)
        AS average_delayed_months,

    ROUND(AVG(Max_Delay_Months), 2)
        AS average_maximum_delay

FROM credit_customers

GROUP BY Default_Status

ORDER BY Default_Status;

-- Validate the SQL results before moving on
SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT ID) AS unique_customer_ids,
    SUM(CASE WHEN ID IS NULL THEN 1 ELSE 0 END)
        AS missing_ids,
    SUM(CASE WHEN `Default` = 1 THEN 1 ELSE 0 END)
        AS defaulted_customers,
    SUM(CASE WHEN `Default` = 0 THEN 1 ELSE 0 END)
        AS non_defaulted_customers,
    SUM(
        CASE
            WHEN `Default` NOT IN (0, 1)
                 OR `Default` IS NULL
            THEN 1
            ELSE 0
        END
    ) AS invalid_default_values
FROM credit_customers;