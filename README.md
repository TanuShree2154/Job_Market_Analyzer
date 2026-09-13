# Job Market Analyzer

A web-based job market analytics application built using **Python, Streamlit, SQL Server, and Pandas**. The application helps users explore job market trends, salary patterns, in-demand skills, hiring companies, and job opportunities through interactive dashboards and filters.

---

## Overview

**Job Market Analyzer** provides an interactive platform for analyzing job-market data and extracting meaningful insights from job postings.

Users can explore job opportunities based on **location, experience level, job type, skills, and other job-related attributes** while viewing key metrics and visualizations.

---

## Features

- Interactive job market dashboard
- Filter jobs by:
  - Location
  - Experience level
  - Job type
- Analyze in-demand technical skills
- Explore salary trends and salary distribution
- Identify top hiring companies
- Company insights
- Job Explorer for browsing job opportunities
- KPI cards for key job-market metrics
- Interactive charts and visualizations
- Data-driven job-market insights

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Application development and data processing |
| Streamlit | Interactive web application |
| SQL Server | Data storage and querying |
| SQL | Data analysis and aggregation |
| Pandas | Data manipulation and analysis |
| PyODBC | SQL Server connectivity |

---

## Project Structure

```text
Job_Market_Analyzer/
│
├── app/
│   ├── pages/
│   ├── streamlit_app.py
│   └── db.py
│
├── assets/
│   └── load_data.py
│
├── data/
├── sql/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Getting Started

### Prerequisites

Make sure the following are installed on your system:

- Python 3.x
- SQL Server
- ODBC Driver for SQL Server

### Installation

#### 1. Clone the repository

```bash
git clone https://github.com/TanuShree2154/Job_Market_Analyzer.git
```

#### 2. Navigate to the project directory

```bash
cd Job_Market_Analyzer
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Configure SQL Server

Configure your SQL Server database and update the database connection settings in the application according to your local SQL Server setup.

#### 5. Run the application

```bash
cd app
python -m streamlit run streamlit_app.py
```

The application will open in your browser.

---

## Key Analytics

The application provides insights into:

- Job demand across different locations
- In-demand technical skills
- Salary patterns across roles and experience levels
- Top hiring companies
- Job-type distribution
- Experience-level distribution
- Overall job-market trends

---

## Use Cases

Job Market Analyzer can be useful for:

- **Job Seekers** — Explore available opportunities and salary trends
- **Students** — Understand current job-market requirements
- **Developers** — Identify in-demand technical skills
- **Recruiters** — Analyze hiring patterns
- **Analysts** — Explore job-market trends and distributions

---

## Author

**Tanu Shree Soni**

GitHub: [@TanuShree2154](https://github.com/TanuShree2154)