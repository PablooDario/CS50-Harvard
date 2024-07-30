-- Write a SQL query to find the 5 schools with the highest excluded rate

SELECT s.name, g.excluded
FROM schools s
JOIN graduation_rates g ON g.school_id = s.id
ORDER BY g.excluded DESC
LIMIT 5;
