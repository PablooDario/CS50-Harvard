-- Write a SQL query to find cities with 3 or fewer public schools

SELECT city, count(*)
FROM schools
WHERE type LIKE "Public%"
GROUP BY city
HAVING count(*) < 4
ORDER BY count(*) DESC, city;
