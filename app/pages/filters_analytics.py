import streamlit as st
import pandas as pd
from db import get_connection

conn = get_connection()
if st.button("⬅ Back to Home"):
    st.switch_page("streamlit_app.py")
st.title("Market Analytics")
#sidebar
st.sidebar.title("Filters")
st.sidebar.subheader("Search")
#company name serch input
comp_name=st.sidebar.text_input("Search Company " , key='comp_name')
job_title= st.sidebar.text_input("Search Job Title", key='job_title')
st.sidebar.divider()
# Location filter
st.sidebar.subheader("Location Settings")
location = st.sidebar.selectbox(
    "Select Location",
    ["All", "Bangalore", "Pune", "Delhi", "Hyderabad", "Mumbai"],
    key='location'
)
st.sidebar.divider()
# Experience filter
st.sidebar.subheader("Job Settings")
experience = st.sidebar.selectbox(
    "Select Experience Level",
    ["All", "Fresher", "1-3 Years", "3-5 Years"],
    key='experience'
)

# Job type filter
job_type = st.sidebar.selectbox(
    "Select Job Type",
    ["All", "Full Time", "Internship", "Contract", "Hybrid"],
    key='job_type'
)
st.sidebar.divider()
#dynamic query
query = f"SELECT * FROM jobs WHERE 1=1"
if location != "All":
   query += f" AND location ='{location}'"
if experience!="All":
    query += f" AND experience_level ='{experience}'"
if job_type!= "All":
    query+= f" AND job_type ='{job_type}'"
if comp_name not in [None, "", "nan"]:
    query += f" AND company LIKE '%{comp_name}%'"
if job_title not in [None, "", "nan"]:
    query += f" AND job_title LIKE '%{job_title}%'"
    
#filtered data table
temp_df = pd.read_sql(query, conn)                  #filterd data
if temp_df.empty:
    st.warning("No jobs found.")
    st.stop()

#Salary sidebar silder
min_salary= temp_df['salary_lpa'].min()
max_salary = temp_df['salary_lpa'].max()


selected_salary=st.sidebar.slider(
    'Select Salary (lpa)',
    min_salary,
    max_salary,
    min_salary,
    key='salary'
)
query += f" AND salary_lpa >= {selected_salary}"
df = pd.read_sql(query, conn)
if df.empty:
    st.warning("No data available for selected filters.")
    st.stop()
st.sidebar.divider()

#Sidebar Summary
st.sidebar.subheader("Dashboard Summary")
st.sidebar.write(f"Total Jobs: {len(df)}")
st.sidebar.write(f"Total Companies: {df['company'].nunique()}")
st.sidebar.write(f"Total Location: {df['location'].nunique()}")


st.divider()

#KPI
col1,col2,col3,col4 = st.columns(4)
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

#avg salary kpi
avg_salary = df['salary_lpa'].mean()
if pd.notna(avg_salary):
    col4.metric(
        label="Average Salary",
        value=(f"{avg_salary:.1f} lpa")
    )
else:
    col4.metric(
        label="Average Salary",
        value="not found"
    )
st.divider()

#graphs
with st.container():
    st.markdown("### 📈 Analytics")
col1 ,col2 =st.columns(2)
#top company
with col1:
    graph_data= (df['company'].value_counts().head(10)).reset_index()
# st.write(graph_data)
    graph_data.columns=('company','job')
    st.subheader("Top Company")
    st.bar_chart(graph_data, x='company' , y='job')

#top skill
with col2:
    graph2_data= all_skill.value_counts().head(10)
    graph2_data=graph2_data.reset_index()
    # st.write(graph2_data)
    graph2_data.columns=('skills' , 'count')
    st.subheader("Top Skills")
    st.bar_chart(graph2_data , x='skills' ,y='count' )


col3,col4 = st.columns(2)
# job type distribution
with col3:
    st.subheader("Job Type Distribution")
    graph3_data=df["job_type"].value_counts()
    graph3_data = graph3_data.reset_index()
    st.bar_chart(graph3_data , x='job_type' , y='count')

#location 
with col4:
    loc_data = df["location"].value_counts().head(10).reset_index()
    loc_data.columns = ["location", "count"]
    st.subheader("Top Locations")
    st.bar_chart(loc_data , x='location', y='count')

st.divider()

with st.container():
    st.markdown("## 📋 Data Explorer")

    st.write(f"Showing {len(df)} jobs")
    st.dataframe(df)