USE JobMarketAnalyzer;

SELECT experience_level , COUNT(*) AS jobs_available
FROM jobs
GROUP BY experience_level 
ORDER BY jobs_available DESC ;