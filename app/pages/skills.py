import streamlit as st
import pandas as pd
import pyodbc 
from streamlit_searchbox import st_searchbox

st.set_page_config(
    layout="wide")
from db import get_connection
conn = get_connection()
if st.button("⬅ Back to Home"):
    st.switch_page("streamlit_app.py")


st.title("Skills Intelligence")
st.divider()
st.caption(
    "Analyze skill demand for a specific role based on job posting data."
)
df = pd.read_sql("SELECT DISTINCT job_title FROM jobs", conn)
all_roles = sorted(df["job_title"].dropna().unique())
def search_roles(searchterm):
    if not searchterm:
        return all_roles[:10]  

    return [
        role for role in all_roles
        if searchterm.lower() in role.lower()
    ][:10]

selected_role = st_searchbox(
    search_roles,
    placeholder="Search job role (e.g. Data Analyst)"
)

query_job = """
    SELECT *
    FROM jobs
    WHERE job_title = ?
"""

if selected_role:
    skill_df = pd.read_sql(query_job, conn, params=[selected_role])
    skills_name= (skill_df['skills'].dropna().str.split(',').explode().str.strip())
    top_skills = skills_name.value_counts().head(10)

    st.subheader(f"Top Skills for {selected_role}")
    col1,col2 =st.columns(2)
    col1.bar_chart(top_skills)

    col2.dataframe(
        top_skills.reset_index().rename(
            columns={"index": "Skill", 0: "Count"}
        )
    )
