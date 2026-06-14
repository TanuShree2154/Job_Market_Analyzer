use JobMarketAnalyzer;

SELECT  company , count(company) as no_of_hirings FROM jobs group by company
order by count(company) desc;