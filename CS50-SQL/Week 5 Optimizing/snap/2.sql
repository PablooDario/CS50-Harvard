-- Find when the message with ID 151 expires

-- EXPLAIN QUERY PLAN
SELECT expires_timestamp
FROM messages
WHERE id = 151;
