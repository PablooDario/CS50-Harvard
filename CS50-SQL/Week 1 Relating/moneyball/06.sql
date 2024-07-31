-- Write a SQL query to return the top 5 teams, sorted by the total number of hits by players in 2001.

SELECT t.name, SUM(h) as "total hits"
FROM performances p
JOIN teams t ON t.id = p.team_id
WHERE p.year = 2001
GROUP BY team_id
ORDER BY "total hits" DESC
LIMIT 5;
