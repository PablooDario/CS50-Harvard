-- Write a SQL query to find the 10 cities with the most public schools.

SELECT city, count(*)
FROM schools
WHERE type LIKE "Public%"
GROUP BY city
ORDER BY count(*) DESC, city
LIMIT 10;
