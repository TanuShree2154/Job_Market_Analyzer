import pandas as pd
import pyodbc
import json


with open("data/dataset.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    

df = pd.DataFrame(data)
df.columns = df.columns.str.lower()

print(df.columns)
print(df.head())

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


df["skills"] = df["skills"].apply(
    lambda x: ", ".join(x) if isinstance(x, list) else x
)

df["posted_date"] = pd.to_datetime(df["posted_date"]).dt.date

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    r"Server=localhost\SQLEXPRESS;"
    "Database=JobMarketAnalyzer;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()


insert_query = """
INSERT INTO jobs (
    job_id, job_title, company, location,
    salary_lpa,experience_level,job_type, skills,
    posted_date, industry
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""


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



