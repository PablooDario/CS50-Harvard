-- Create Index
CREATE INDEX "search_messages_by_to_user_id"
ON "messages"("to_user_id");

-- Find the username of the most popular user, defined as the user who has had the most messages sent to them
-- EXPLAIN QUERY PLAN
SELECT username
FROM users
WHERE id = (
    SELECT to_user_id
    FROM messages
    GROUP BY to_user_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
);
