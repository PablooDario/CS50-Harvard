-- Write a SQL query to find all teams that Satchel Paige played for.

SELECT DISTINCT(name)
FROM teams t
JOIN performances pe ON pe.team_id = t.id
JOIN players pl ON pl.id = pe.player_id
WHERE pl.first_name = "Satchel";
