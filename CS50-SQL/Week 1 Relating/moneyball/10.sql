-- All player’s first names
-- All player’s last names
-- All player’s salaries
-- All player’s home runs
-- The year in which the player was paid that salary and hit those home runs

SELECT p.first_name, p.last_name, s.salary, per.hr, s.year
FROM players p
JOIN salaries s ON s.player_id = p.id
JOIN performances per ON per.player_id = s.player_id AND per.year = s.year
ORDER BY p.id ASC, s.year DESC, per.hr DESC, s.salary DESC;
