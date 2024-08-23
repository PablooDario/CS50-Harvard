-- Ceate a view named june_vacancies. This view should contain all listings and the number of days in June of 2023 that they remained vacant.

CREATE VIEW "june_vacancies" AS
SELECT l.id, l.property_type, l.host_name, COUNT(*) AS "days_vacant"
FROM availabilities a
JOIN listings l ON l.id = a.listing_id
WHERE ("date" BETWEEN "2023-06-01" AND "2023-06-31") AND (available = "TRUE")
GROUP BY (listing_id);
