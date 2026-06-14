use JobMarketAnalyzer;

-- total no. of records
select count(*) from jobs;

--Check first few rows
select top 6 * from jobs ;

-- Check if any columns contain NULL values
SELECT * FROM jobs
WHERE salary_max IS NULL;

SELECT * FROM jobs
WHERE location IS NULL;
-- Check if salary values look reasonable
select top 20 salary_min ,salary_max from jobs;

-- Check if dates are stored correctly
SELECT TOP 20 posted_date
FROM jobs;

