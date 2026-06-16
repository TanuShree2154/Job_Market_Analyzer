import streamlit as st
import pandas as pd
import pyodbc 
st.set_page_config(layout="wide")
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    r"Server=localhost\SQLEXPRESS;"
    "Database=JobMarketAnalyzer;"
    "Trusted_Connection=yes;"
)

st.title("Job Market Analyzer")

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

#dynamic query
query = f"SELECT * FROM jobs WHERE 1=1"
if location != "All":
   query += f" AND location ='{location}'"
if experience!="All":
    query += f" AND experience_level ='{experience}'"
if job_type!= "All":
    query+= f" AND job_type ='{job_type}'"


#filtered data table
temp_df = pd.read_sql(query, conn)                  #filterd data


#Salary sidebar silder
min_salary= temp_df['salary_lpa'].min()
max_salary = temp_df['salary_lpa'].max()
selected_salary=st.sidebar.slider(
    'Select Salary (lpa)',
    min_salary,
    max_salary,
    min_salary
)
query += f" AND salary_lpa >= {selected_salary}"
df = pd.read_sql(query, conn)

#Sidebar Summary
st.sidebar.markdown("---")
st.sidebar.subheader("Dashboard Summary")
st.sidebar.write(f"Total Jobs: {len(df)}")
st.sidebar.write(f"Total Companies: {df['company'].nunique()}")
st.sidebar.write(f"Total Location: {df['location'].nunique()}")


#KPI
st.subheader("📊 Dashboard Overview")
st.divider()

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
    st.markdown("## 💰 Salary Intelligence")
    # Top 10 highest paying companies 
    query_salary = """
    SELECT TOP 10
        company,
        ROUND(AVG(salary_lpa), 1) AS avg_salary
    FROM jobs
    GROUP BY company
    ORDER BY avg_salary DESC;
    """

    salary_df = pd.read_sql(query_salary, conn)
    st.markdown("### Top 10 Highest Paying Companies")
    st.bar_chart(salary_df, x="company", y="avg_salary")

st.divider()

with st.container():
    st.markdown("## 📋 Data Explorer")

    st.write(f"Showing {len(df)} jobs")
    st.dataframe(df)