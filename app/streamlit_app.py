import streamlit as st
import pandas as pd
import pyodbc 

st.title("Job Market Analyst")

#sidebar
st.sidebar.title("Filters")
# Location filter
location = st.sidebar.selectbox(
    "Select Location",
    ["All", "Bangalore", "Pune", "Delhi", "Hyderabad", "Mumbai"]
)

# Experience filter
experience = st.sidebar.selectbox(
    "Select Experience Level",
    ["All", "Fresher", "1-3 Years", "3-5 Years"]
)

# Job type filter
job_type = st.sidebar.selectbox(
    "Select Job Type",
    ["All", "Full Time", "Internship", "Contract", "Hybrid"]
)

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    r"Server=localhost\SQLEXPRESS;"
    "Database=JobMarketAnalyzer;"
    "Trusted_Connection=yes;"
)

#dynamic query
query = f"SELECT * FROM jobs WHERE 1=1"
if location != "All":
   query += f" AND location ='{location}'"
if experience!="All":
    query += f" AND experience_level ='{experience}'"
if job_type!= "All":
    query+= f"AND job_type ='{job_type}'"


#filtered data table
df = pd.read_sql(query, conn)                  #filterd data
st.subheader("Filtered Jobs")

#KPI
col1,col2,col3 = st.columns(3)
# KPI (total_jobs) 
col1.metric(label="Total Jobs" , value=len(df))

#KPI (top hiring company)
top_company = df['company'].value_counts().head(1)
if not top_company.empty:
    col2.metric(
        label="Top Hiring Company",
        value=top_company.index[0],
        delta=f"{top_company.values[0]} jobs"
    )
else:
    col2.metric(
        label="Top Company",
        value="not found"
    )

#top skill kpi
all_skill= df['skills'].str.split(',').explode().str.strip()
top_skill=all_skill.value_counts().head(1)
if not top_skill.empty:
    col3.metric(
        label="Top Skill",
        value=top_skill.index[0],
        delta= f"{top_skill.values[0]} mention"
    )
else:
    col3.metric(
        label="Top Skill",
        value="no data found",
        delta="0 mentions"
    )


#graphs
#top company
graph_data= (df['company'].value_counts().head(10)).reset_index()
# st.write(graph_data)
graph_data.columns=('company','job')
st.subheader("Top Company")
st.bar_chart(graph_data, x='company' , y='job')

#top skill
graph2_data= all_skill.value_counts().head(10)
graph2_data=graph2_data.reset_index()
# st.write(graph2_data)
graph2_data.columns=('skills' , 'count')
st.subheader("Top Skills")
st.bar_chart(graph2_data , x='skills' ,y='count' )

# job type distribution
st.subheader("Job Type Distribution")
graph3_data=df["job_type"].value_counts()
graph3_data = graph3_data.reset_index()
st.bar_chart(graph3_data , x='job_type' , y='count')

#location 
loc_data = df["location"].value_counts().head(10)
st.subheader("Top Locations")
st.bar_chart(loc_data)


st.dataframe(df)
  