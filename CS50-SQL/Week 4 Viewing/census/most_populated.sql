-- Create a view that contain, in order from greatest to least, the most populated districts in Nepal. Ensure the view contains each of the following columns:

CREATE VIEW "most_populated" AS
SELECT district, SUM(families) AS "families", SUM(households) AS "households", SUM(population) AS "population", SUM(male) AS "male", SUM(female) AS "female"
FROM census
GROUP BY district
ORDER BY "population" DESC;

