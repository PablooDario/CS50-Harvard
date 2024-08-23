-- Create a view that contains the sums for each numeric column in census, across all districts and localities

CREATE VIEW "total" AS
SELECT SUM(families) AS "families", SUM(households) AS "households", SUM(population) AS "population", SUM(male) AS "male", SUM(female) AS "female"
FROM census;
