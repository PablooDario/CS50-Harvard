-- Write a SQL query to find the names of schools (public or charter!) in the Cambridge school district.

SELECT name
FROM schools
WHERE district_id = (SELECT id
    FROM districts
    WHERE name = "Cambridge"
);
