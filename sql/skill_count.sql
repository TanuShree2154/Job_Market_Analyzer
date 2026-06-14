USE JobMarketAnalyzer;

SELECT  value as each_skill , count(*) as skill_count 
FROM jobs
CROSS APPLY string_split(skills ,',')  
group by value 
order by skill_count desc;

