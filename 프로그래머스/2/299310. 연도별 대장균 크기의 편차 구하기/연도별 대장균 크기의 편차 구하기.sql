SELECT 
    YEAR(differentiation_date) AS YEAR,
    MAX_SIZE - size_of_colony AS YEAR_DEV,
    ID
FROM ecoli_data
JOIN (
    SELECT YEAR(differentiation_date) AS YEAR, MAX(size_of_colony) AS MAX_SIZE
    FROM ecoli_data
    GROUP BY YEAR(differentiation_date)
) AS yearly_max ON YEAR(ecoli_data.differentiation_date) = yearly_max.YEAR
ORDER BY year , year_dev
