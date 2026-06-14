import pandas as pd
import pyodbc
import json

# Step 1: Load JSON file
with open("data/dataset.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)
df.columns = df.columns.str.lower()

print(df.columns)
print(df.head())
# Step 4: Handle missing columns (safety layer)
df = df[[
    "job_id",
    "job_title",
    "company",
    "location",
    "salary_lpa",
    "experience_level",
    "job_type",
    "skills",
    "posted_date",
    "industry"
]]

# Step 4.1: Clean skills column (convert list → string)
df["skills"] = df["skills"].apply(
    lambda x: ", ".join(x) if isinstance(x, list) else x
)

# Step 5: Convert date column (important for SQL)
df["posted_date"] = pd.to_datetime(df["posted_date"]).dt.date

# Step 6: Connect to SQL Server
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    r"Server=localhost\SQLEXPRESS;"
    "Database=JobMarketAnalyzer;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

# Step 7: Insert query
insert_query = """
INSERT INTO jobs (
    job_id, job_title, company, location,
    salary_lpa,experience_level,job_type, skills,
    posted_date, industry
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# Step 8: Insert row by row
print(df.dtypes)
for _, row in df.iterrows():
    cursor.execute(insert_query,
        row.job_id,
        row.job_title,
        row.company,
        row.location,
        row.salary_lpa,
        row.experience_level,
        row.job_type,
        row.skills,
        row.posted_date,
        row.industry
    )

conn.commit()
conn.close()

print("✅ Data loaded successfully into SQL Server!")



