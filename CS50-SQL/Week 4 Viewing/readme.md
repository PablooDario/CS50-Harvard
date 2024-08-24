# Viewing

A view is a **virtual table** defined by a query.

Say we wrote a query to join three tables and then select the relevant columns. The new table created by this query can be saved as a view, to be further queried later on. Views are useful for:

- **simplifying**: putting together data from different tables to be queried more simply,
- **aggregating**: running aggregate functions, like finding the sum, and storing the results,
- **partitioning**: dividing data into logical pieces,
- **securing**: hiding columns that should be kept secure. While there are other ways in which views can be useful, in this lecture we will focus on the above four.

## Simplifying

Suppose we want to retrieve the books written by "Fernanda Melchor", so everytime we wnat this data we must write the following query:

```sql
SELECT "name", "title" FROM "authors"
JOIN "authored" ON "authors"."id" = "authored"."author_id"
JOIN "books" ON "books"."id" = "authored"."book_id";
```

To save the **virtual table** created in the previous step as a view, we need to change the query.

```sql
CREATE VIEW "longlist" AS
SELECT "name", "title" FROM "authors"
JOIN "authored" ON "authors"."id" = "authored"."author_id"
JOIN "books" ON "books"."id" = "authored"."book_id";
```

The view created here is called longlist. This view can now be used exactly as we would use a table in SQL.

Let us write a query to see all the data within this view.

```sql
SELECT * FROM "longlist";
```

Using this view, we can considerably simplify the query needed to find the books written by Fernanda Melchor.

```sql
SELECT "title" FROM "longlist" WHERE "name" = 'Fernanda Melchor';
```

**A view, being a virtual table, does not consume much more disk space to create. Since a view is essentially a saved query. The data within a view is still stored in the underlying tables, but still accessible through this simplfied view. When you query a view, the database engine dynamically retrieves and processes data from the base tables according to the view’s definition.**

### Materialized Views 

There is a type of view called a materialized view (or snapshot) that does store data. A materialized view stores the results of the query physically on disk, which can improve performance for certain queries but will use additional storage space. Materialized views need to be refreshed periodically to stay up-to-date with changes in the underlying tables.

## Aggregating

Views can also help us to store aggregating data; for example if we want to find the average rating of every book, rounded to 2 decimal places, we can saved the **agregated** data in a view:

```sql
CREATE VIEW "average_book_ratings" AS
SELECT "book_id" AS "id", "title", "year", ROUND(AVG("rating"), 2) AS "rating" 
FROM "ratings"
JOIN "books" ON "ratings"."book_id" = "books"."id"
GROUP BY "book_id";
```

## Temporary Views

To create temporary views that are not stored in the database schema, we can use `CREATE TEMPORARY VIEW`. This command creates a view that exists only for the duration of our connection with the database.

```sql
CREATE TEMPORARY VIEW "average_ratings_by_year" AS
SELECT "year", ROUND(AVG("rating"), 2) AS "rating" FROM "average_book_ratings" 
GROUP BY "year";
```

### Common Table Expression (CTE)

**A regular view exists forever in our database schema. A temporary view exists for the duration of our connection with the database. A CTE is a view that exists for a single query alone.**

The syntax of a CTE is the following:

```sql
WITH <name> AS (
    <SQL Query to our Database>
)
<SQL Query to the above table>;
```

EXAMPLE: Retrieve the average book ratings from our database and then select the ratings of each year of the resulting table. Remember the CTE will disappear automatically after the query ends.
```sql
WITH "average_book_ratings" AS (
    SELECT "book_id", "title", "year", ROUND(AVG("rating"), 2) AS "rating" FROM "ratings"
    JOIN "books" ON "ratings"."book_id" = "books"."id"
    GROUP BY "book_id"
)
SELECT "year" ROUND(AVG("rating"), 2) AS "rating" FROM "average_book_ratings"
GROUP BY "year";
```

## Partitioning

Views can be used to **partition data**, or to __break it into smaller pieces__ that will be useful to us or an application. For example, the website for the International Booker Prize has a page of longlisted books for each year the prize was awarded. However, our database stores all the longlisted books in a single table. For the sake of creating the website, or a different purpose, it might be useful to have a different table (or view) of books for each year.
Let us create a view to store books longlisted in 2022.

```sql
CREATE VIEW "2022" AS
SELECT "id", "title" FROM "books"
WHERE "year" = 2022;
```

## Securing

Views can be used to **enhance database security by limiting access to certain data.** If we were to give data to an analyst, it would be irrelevant and indeed, not secure to give them categorized data as Personally Identifiable Information (PII) which companies are not allowed to share indiscriminately.

Views can be handy in this situation, we can share with the analyst a view containing the necessary data.

## Soft Deletions

As we saw in previous weeks, a soft deletion involves marking a row as deleted instead of removing it from the table. So if we are using **soft deletions** in our tables we can create a view for data that is **marked as delete** and another for **undeleted data**