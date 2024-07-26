-- Write SQL query to answer a question of your choice. This query should:

-- Make use of AS to rename a column
-- Involve at least condition, using WHERE
-- Sort by at least one column using ORDER BY

SELECT first_name, last_name AS "apellido", birth_country
FROM players
WHERE birth_country LIKE 'M%'
ORDER BY first_name;