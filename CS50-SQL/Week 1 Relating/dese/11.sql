-- Write a SQL query to display the names of schools, their per-pupil expenditure, and their graduation rate.

-- Sort the schools from greatest per-pupil expenditure to least. If two schools have the same per-pupil expenditure, sort by school name.

SELECT s.name, e.per_pupil_expenditure, g.graduated
FROM schools s
JOIN districts d ON d.id = s.district_id
JOIN graduation_rates g ON g.school_id = s.id
JOIN expenditures e ON e.district_id = d.id
ORDER BY e.per_pupil_expenditure DESC, s.name;
