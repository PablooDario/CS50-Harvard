-- Write a SQL query to find public school districts with above-average per-pupil expenditures and an above-average percentage of teachers rated

-- Sort the results first by the percentage of teachers rated exemplary (high to low), then by the per-pupil expenditure (high to low).

SELECT d.name, e.per_pupil_expenditure, s.exemplary
FROM districts d
JOIN expenditures e ON e.district_id = d.id
JOIN staff_evaluations s ON s.district_id = d.id
WHERE d.type LIKE "Public%" AND e.per_pupil_expenditure > (
        SELECT AVG(per_pupil_expenditure) FROM expenditures
) AND s.exemplary > (
        SELECT AVG(exemplary) FROM staff_evaluations
) ORDER BY s.exemplary DESC, e.per_pupil_expenditure DESC;
