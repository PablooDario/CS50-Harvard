-- Create a view named frequently_reviewed. This view should contain the 100 most frequently reviewed listings, sorted from most- to least-frequently reviewed.

CREATE VIEW "frequently_reviewed" AS
SELECT l.id, l.property_type, l.host_name, COUNT(r.listing_id) AS "reviews"
FROM listings l
JOIN reviews r ON l.id=r.listing_id
GROUP BY r.listing_id
ORDER BY reviews DESC, l.property_type, l.host_name;
