USE JobMarketAnalyzer;
-- total jobs
SELECT COUNT(DISTINCT location) AS total FROM jobs;