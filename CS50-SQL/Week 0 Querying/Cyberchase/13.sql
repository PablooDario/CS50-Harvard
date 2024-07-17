-- Write a SQL query to explore a question of your choice. This query should:
-- Involve at least one condition, using WHERE with AND or OR

SELECT *
FROM episodes
WHERE season = 1 AND (air_date BETWEEN '2002-01-01' AND '2002-12-31');