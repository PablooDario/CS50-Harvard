-- Create Index to Oprimize the following query
CREATE INDEX "search_messages_by_from_user_id"
ON "messages"("from_user_id");

-- Find the user IDs of the top 3 users to whom creativewisdom377 sends messages most frequently
-- EXPLAIN QUERY PLAN
SELECT to_user_id
FROM messages
WHERE from_user_id = (
    SELECT id FROM users WHERE username = "creativewisdom377"
)
GROUP BY to_user_id
ORDER BY COUNT(*) DESC
LIMIT 3;
