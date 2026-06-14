use JobMarketAnalyzer;

SELECT top 3 location , count(location) as no_of_jobs FROM jobs 
group by location
order by count(location) desc;