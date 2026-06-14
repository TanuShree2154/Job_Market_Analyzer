use JobMarketAnalyzer;

CREATE TABLE jobs(
    job_id INT PRIMARY KEY,
    job_title VARCHAR(100),
    company VARCHAR(100),
    location VARCHAR(100),
    salary_lpa DECIMAL(4,1),
    experience_level VARCHAR(20),
    job_type VARCHAR(25),
    skills VARCHAR(300),
    posted_date DATE,
    industry VARCHAR(100)
);

