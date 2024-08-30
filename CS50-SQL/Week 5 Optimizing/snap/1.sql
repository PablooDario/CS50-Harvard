-- Create Index to oprimize the query
CREATE INDEX "search_users_by_last_login"
ON "users"("last_login_date");

-- Find all usernames of users who have logged in since 2024-01-01
SELECT username
FROM users
WHERE last_login_date >= "2024-01-01";
