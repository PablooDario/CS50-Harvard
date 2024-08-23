-- Create a view named available. This view should contain all dates that are available at all listings.

CREATE VIEW available AS
SELECT l.id, l.property_type, l.host_name, a.date, a.available
FROM availabilities a
JOIN listings l ON l.id = a.listing_id
WHERE available = "TRUE";
