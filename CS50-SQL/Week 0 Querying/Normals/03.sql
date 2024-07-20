-- Choose a location of your own and write a SQL query to find the normal temperature at 0 meters, 100 meters, and 200 meters. 

SELECT "0m", "100m", "200m"
FROM normals
WHERE latitude = 42.5 AND longitude = -69.5;