-- Write a SQL query to find the 50 players paid the least in 2001.

SELECT p.first_name, p.last_name, s.salary
FROM players p
JOIN salaries s ON s.player_id = p.id
WHERE year = 2001
ORDER BY s.salary, p.first_name, p.last_name, p.id
LIMIT 50;
