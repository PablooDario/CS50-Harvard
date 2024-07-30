-- Write a SQL query to find the 10 public school districts with the highest per-pupil expenditures.

SELECT d.name, e.per_pupil_expenditure
FROM districts as d
JOIN expenditures as e ON e.district_id = d.id
WHERE d.type LIKE "Public%"
ORDER BY e.per_pupil_expenditure DESC
LIMIT 10;
