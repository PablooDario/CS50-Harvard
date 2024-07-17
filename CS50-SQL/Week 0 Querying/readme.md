# Querying 

## What is a DataBase ?

A database is a way of organizing data such that you can perform four operations on it: 

- Create
- Read
- Update
- Delete

A database management system (DBMS) is a way to interact with a database using a graphical interface or textual language.

## SQL

SQL stands for Structured Query Language. It is a language used to interact with databases, via which you can create, read, update, and delete data in a database. 

- It is structured.
- It has some keywords that can be used to interact with the database.
- It is a query language — it can be used to ask questions of data inside a database.

### Keywords seen in this lesson:

- **SELECT**
```SQL
SELECT <column1>, <column2>, ... <column_n> FROM <table>;
```
- **LIMIT**
```SQL
SELECT * FROM <table>
LIMIT <number>;
```
- **WHERE**
```SQL
SELECT * FROM <table>
WHERE <condition>; 
```
- **WHERE** with multiple conditions
```SQL
SELECT * FROM <table>
WHERE <condition1> and/or <condition2>
```
- **NULL**
```SQL
SELECT * FROM <table>
WHERE <column> IS NULL; 
```
- **LIKE** (Regex)
```SQL
SELECT * FROM <table>
WHERE <column> LIKE "REGEX"; 
```
- **BETWEEN** (Ranges)
```SQL
SELECT * FROM <table>
WHERE <column> BETWEEN <n> AND <n2>; 
```
- **ORDER BY**
```SQL
SELECT * FROM <table>
ORDER BY <column> ASC/DESC; 
```
- *Aggregate Functions*
```SQL
SELECT COUNT(*), AVG(<column>), MAX(<column2>), MIN(<column3>)
FROM <table>
```

### Example
``` SQL
SELECT title, author, votes
FROM books
WHERE (year BETWEEN 2019 AND 2024) AND (editorial LIKE "%Sea%")
ORDER BY rating DESC
LIMIT 10;
```
