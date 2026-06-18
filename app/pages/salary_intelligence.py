import streamlit as st
import pandas as pd
from db import get_connection
if st.button("⬅ Back to Home"):
    st.switch_page("streamlit_app.py")
st.title("Salary Intelligence")
st.divider()

conn = get_connection()

with st.container():
    
    # Top 10 highest paying companies 
    col1,col2=st.columns(2)
    query_salary = """
    SELECT TOP 10
        company,
        ROUND(AVG(salary_lpa), 1) AS avg_salary
    FROM jobs
    GROUP BY company
    ORDER BY avg_salary DESC;
    """

    salary_df = pd.read_sql(query_salary, conn)
    col1.markdown("### Top 10 Highest Paying Companies")
    col1.bar_chart(salary_df, x="company", y="avg_salary")

    st.divider()
    query_role_salary = """
SELECT TOP 10
    job_title,
    ROUND(AVG(salary_lpa), 1) AS avg_salary
FROM jobs
GROUP BY job_title
ORDER BY avg_salary DESC;
"""

    role_salary_df = pd.read_sql(query_role_salary, conn)

    col2.markdown("### Top 10 Highest Paying Job Roles")
    col2.bar_chart(role_salary_df, x="job_title", y="avg_salary")


col1,col2,col3 =st.columns(3)
query_ss = """
SELECT skills, salary_lpa
FROM jobs
WHERE skills IS NOT NULL
"""
df_ss = pd.read_sql(query_ss, conn)
skills_df = df_ss.copy()
skills_df["skills"] = skills_df["skills"].str.split(",")
skills_df = skills_df.explode("skills")
skills_df["skills"] = skills_df["skills"].str.strip()
skill_salary = skills_df.groupby("skills")["salary_lpa"].mean().reset_index()
skill_salary = skill_salary.sort_values(by="salary_lpa", ascending=False)

col1.markdown("### Top 10 Highest Paying Skills")
col1.bar_chart(skill_salary.head(10), x="skills", y="salary_lpa")

query_location = """
SELECT TOP 10
    location,
    ROUND(AVG(salary_lpa), 1) AS avg_salary
FROM jobs
WHERE location IS NOT NULL
GROUP BY location
ORDER BY avg_salary DESC;
"""

location_df = pd.read_sql(query_location, conn)
col2.markdown("### Top 10 Highest Paying Locations")
col2.bar_chart(location_df, x="location", y="avg_salary")

cities = ("Bangalore", "Hyderabad", "Pune")

query_compare = f"""
SELECT
    location,
    ROUND(AVG(salary_lpa), 1) AS avg_salary
FROM jobs
WHERE location IN {cities}
GROUP BY location
ORDER BY avg_salary DESC;
"""

compare_df = pd.read_sql(query_compare, conn)
col3.markdown("### Salary Comparison: Bangalore vs Hyderabad vs Pune")
col3.bar_chart(compare_df, x="location", y="avg_salary")