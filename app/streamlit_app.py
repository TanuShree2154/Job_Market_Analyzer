import streamlit as st
import pandas as pd
from db import get_connection

conn = get_connection()

st.set_page_config(
    page_title='Job Market Analyzer',
    layout="wide")

st.title("JOB MARKET ANALYZER")

st.markdown("""
Analyze hiring trends, salary insights, and in-demand technical skills
using job market data.

""")
st.divider()
st.markdown("### Dashboard Overview")




total_jobs = pd.read_sql(
    "SELECT COUNT(*) AS total FROM jobs",
    conn
).iloc[0]["total"]

total_companies = pd.read_sql(
    "SELECT COUNT(DISTINCT company) AS total FROM jobs",
    conn
).iloc[0]["total"]

total_locations = pd.read_sql(
    "SELECT COUNT(DISTINCT location) AS total FROM jobs",
    conn
).iloc[0]["total"]

avg_salary = pd.read_sql(
    "SELECT ROUND(AVG(salary_lpa),1) AS avg_salary FROM jobs",
    conn
).iloc[0]["avg_salary"]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Jobs", total_jobs)
col2.metric("Companies", total_companies)
col3.metric("Locations", total_locations)
col4.metric("Avg Salary", f"{avg_salary} LPA")

st.write("") 

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("## Skills Intelligence")

    st.markdown("""
    **Analyze demand patterns in technical skills.**  
    """)

    st.info("Top Skill: Python")

    if st.button("Explore Skills", use_container_width=True):
        st.switch_page("pages/skills.py")  # adjust file name

with col2:
    st.markdown("## Market Analytics")

    st.markdown("""
    **Understand hiring trends across companies and locations.**  
    """)

    st.success("Top Location: Bangalore")

    if st.button("View Insights", use_container_width=True):
        st.switch_page("pages/filters_analytics.py")



with col3:
    st.markdown("## Salary Intelligence")

    st.markdown("""
    **Compare salaries across roles, skills, and companies.**  
    """)

    st.warning("Avg Salary: 12.4 LPA")

    if st.button("Open Salary", use_container_width=True):
        st.switch_page("pages/salary_intelligence.py")