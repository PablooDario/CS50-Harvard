-- Write a SQL query to find the 5 lowest paying teams (by average salary) in 2001.

SELECT t.name, ROUND(AVG(s.salary), 2) as "average salary"
FROM salaries s
JOIN teams t ON t.id = s.team_id
WHERE s.year = 2001
GROUP BY s.team_id
ORDER BY s.salary ASC
LIMIT 5;
