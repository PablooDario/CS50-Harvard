# Relationships in DataBases

Databases can have multiple tables; these tables may have some relationships between them, and hence we call the database a relational database.

## Entity Relationship Diagram (ER)

Consists is a perception of the real world; it consists of basic objects called entities and relationships between those objects. Represents the overall logical structure of the database. 

Each table is an entity in our database. The relationships between the tables, or entities, are represented by the verbs that mark the lines connecting entities.

![TypesOfRelation](imgs\Relations.png)

### Examples

An author writes one book (or, every author can have one book associated with them).
![One2One](imgs\One.png)

Now, not only does an author write one book but a book is also written by one author.
![One2One](imgs\one2one.png)

Now an author could be associated with one or multiple books and a book can be written by one or multiple authors.
![Many2Many](imgs\many2many.png)

### Example of a Complete Diagram
![ER-Diagram](imgs\ERdiagram.png)

- An **author** can write one or more **books**
- A **book** can have one or more **authors**
- A **book** must only be published by one **publisher**
- A **publisher** can pulish one or more **books**
- A **book** can have zero or more **translators**
- A **translator** can translate one or more **books**
- A **book** can have zero or more **ratings**
- A **rating** must be related to only one **book**


## Main Concepts

### Primary Key

A primary key is a u**nique identifier for a record in a table**. It ensures that each record can be uniquely identified by its value, which is crucial for retrieving and managing data efficiently. Primary keys have the following characteristics:

- **Uniqueness**: Each value in the primary key column must be unique across the table.
- **Non-nullability**: The primary key column cannot contain NULL values.
- **Immutability**: The value of a primary key should rarely be changed because it identifies a record uniquely.

### Foreign Key

A foreign key is a **column or a set of columns** in one table **that refers to the primary key in another table**. The purpose of the foreign key is to **ensure referential integrity between the two tables**, meaning it maintains the logical relationship between the records in the tables. Foreign keys have the following characteristics:

- **Referential Integrity**: A foreign key value must match an existing primary key value in the referenced table or be NULL.
- **Relationships:** Establishes a relationship between the data in two tables

**One to Many Foreign Key**
![ForeignKey](imgs\ForeignKey.png)

**Many to Many Realtionship**
![Many2Many](imgs\N2Mrelationship.png)

### Subqueries

A subquery, also known as an inner query or nested query, is a query embedded within another SQL query. It is used to perform operations that require results from one query to be used as input for another query. 

**Subquery in SELECT clause**
```sql
SELECT 
    EmployeeID, 
    (SELECT DepartmentName 
     FROM Departments 
     WHERE Departments.DepartmentID = Employees.DepartmentID) AS DepartmentName
FROM Employees;
```

**Subquery in WHERE clause**
```sql
SELECT EmployeeID, EmployeeName
FROM Employees
WHERE DepartmentID = (SELECT DepartmentID 
                      FROM Departments 
                      WHERE DepartmentName = 'Sales');
```

**Subquery in FROM clause**
```sql
SELECT AVG(Salary)
FROM (SELECT Salary 
      FROM Employees 
      WHERE DepartmentID = 3) AS DepartmentSalaries;
```
### JOIN

A JOIN clause in SQL is used to **combine rows from two or more tables based on a related column between them**. There are several types of JOINs, each serving different purposes:

- **INNER JOIN**: Returns only the rows that have matching values in both tables.
- **LEFT (OUTER) JOIN**: Returns all the rows from the left table, and the matched rows from the right table. If no match is found, NULL values are returned for columns from the right table.
- **RIGHT (OUTER) JOIN**: Returns all the rows from the right table, and the matched rows from the left table. If no match is found, NULL values are returned for columns from the left table.
- **FULL (OUTER) JOIN**: Returns all the rows when there is a match in either the left or right table. Rows without a match in either table are included as well, with NULLs in columns from the table without a match.
**CROSS JOIN**: Returns the Cartesian product of the two tables, meaning it returns all possible combinations of rows from both tables.

Example:
```sql
SELECT Employees.EmployeeID, Employees.EmployeeName, Departments.DepartmentName
FROM Employees
INNER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
```

### Groups

The `GROUP BY` clause in SQL is used to a**rrange identical data into groups.** It is often used with aggregate functions (COUNT, MAX, MIN, SUM, AVG) to perform calculations on each group of rows.

```sql
SELECT DepartmentID, COUNT(EmployeeID) AS NumberOfEmployees
FROM Employees
GROUP BY DepartmentID;
```

#### Having
The `HAVING` clause in SQL is used in combination with the `GROUP BY` clause to **filter groups based on a condition**. Unlike the `WHERE` clause, which filters rows before grouping, `HAVING` filters groups after the aggregation has been performed.

```sql
SELECT d.DepartmentName, AVG(e.Salary) AS AverageSalary
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DepartmentID
GROUP BY d.DepartmentName
HAVING AVG(e.Salary) > 70000;
```