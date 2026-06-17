import streamlit as st

st.set_page_config(
    page_title='Job Market Analyzer',
    layout="wide")

st.title("JOB MARKET ANALYZER")
st.markdown("### Dashboard Overview")

st.write("") 

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("## 🧠 Skills Intelligence")

    st.markdown("""
    **Analyze demand patterns in technical skills.**  
    """)

    st.info("Top Skill: Python")

    if st.button("Explore Skills", use_container_width=True):
        st.switch_page("pages/skills.py")  # adjust file name

with col2:
    st.markdown("## 📊 Market Analytics")

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

    st.warning("📈 Avg Salary: 12.4 LPA")

    if st.button("Open Salary", use_container_width=True):
        st.switch_page("pages/salary_intelligence.py")