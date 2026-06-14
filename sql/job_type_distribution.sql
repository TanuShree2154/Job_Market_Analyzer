USE JobMarketAnalyzer;

SELECT job_type , count(*)
FROM jobs 
GROUP BY job_type;