--Write a SQL query to find the players among the 10 least expensive players per hit and among the 10 least expensive players per RBI in 2001.

SELECT p.first_name, p.last_name
FROM players p
JOIN salaries s ON s.player_id = p.id
JOIN performances per ON per.player_id = s.player_id AND per.year = s.year
WHERE s.year = 2001 AND per.H <> 0
ORDER BY (s.salary / per.H), (s.salary / per.RBI), p.id
LIMIT 10;
