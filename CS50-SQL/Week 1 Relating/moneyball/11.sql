-- Write a SQL query to find the 10 least expensive players per hit in 2001.

SELECT p.first_name, p.last_name, (s.salary / per.H) AS "dollars per hit"
FROM players p
JOIN salaries s ON s.player_id = p.id
JOIN performances per ON per.player_id = s.player_id AND per.year = s.year
WHERE s.year = 2001 AND per.H <> 0
ORDER BY "dollars per hit" ASC, p.first_name, p.last_name
LIMIT 10;
