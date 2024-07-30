-- Write a SQL query to display the names of all school districts and the number of pupils enrolled in each.

SELECT d.name, e.pupils
FROM districts as d
JOIN expenditures as e ON e.district_id = d.id;
