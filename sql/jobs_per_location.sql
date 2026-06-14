USE JobMarketAnalyzer;

SELECT location , count(*) AS jobs_available
FROM jobs 
GROUP BY location
ORDER BY jobs_available desc;