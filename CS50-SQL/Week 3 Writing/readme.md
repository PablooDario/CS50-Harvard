# Writing

The Boston MFA (Museum of Fine Arts) is a century-old museum in Boston. The MFA manages a vast collection of historical and contemporary artifacts and artwork. They likely use a database of some kind to store data about their art and artifacts.
We will focus now on the creation (or insertion) of data in a Boston MFA database, where the schema is:

```SQL
CREATE TABLE "collections" (
    "id" INTEGER,
    "title" TEXT NOT NULL,
    "accession_number" TEXT NOT NULL UNIQUE,
    "acquired" NUMERIC,
    PRIMARY KEY("id")
);
```

## Inserting Data


The SQL statement INSERT INTO is used to insert a row of data into a given table.

```SQL
INSERT INTO "collections" ("id", "title", "accession_number", "acquired")
VALUES (1, 'Profusion of flowers', '56.257', '1956-04-12');
```

We can try to add a row with a **NULL title, violating the NOT NULL constraint**.
```SQL
INSERT INTO "collections" ("title", "accession_number", "acquired")
VALUES(NULL, NULL, '1900-01-10');
```

On running this, we will see an error that looks like **Runtime error:** `NOT NULL constraint failed: collections.title (19).`

### Inserting Multiple Rows

We may need to **insert more than one row at a time** while writing into a database. One way to do this is to separate out the rows using commas in the INSERT INTO command. Inserting multiple rows at once in this manner allows the programmer some convenience. It is also a faster, more efficient way of inserting rows into a database.

```SQL
INSERT INTO "collections" ("title", "accession_number", "acquired") 
VALUES 
('Imaginative landscape', '56.496', NULL),
('Peonies and butterfly', '06.1899', '1906-01-01');
```

### Importing

Our data could also be stored in a comma-separated values format. SQLite makes it possible to import a CSV file directly into our database. we can import the CSV by running a SQLite command.

`.import --csv --skip 1 mfa.csv collections`

The first argument, `--csv` indicates to SQLite that we are importing a CSV file. This will help SQLite parse the file correctly. The second argument indicates that the first row of the CSV file (**the header row**) needs to be skipped, or not inserted into the table.

Sometimes our data won't have and `id` or **primary key** values, i.e.:

```csv
title,accession_number,acquired
Profusion of flowers,56.257,1956-04-12
Farmers working at dawn,11.6152,1911-08-03
Spring outing,14.76,1914-01-08
Imaginative landscape,56.496,
Peonies and butterfly,06.1899,1906-01-01
```

So we can insert the data into a temporal table and then insert that data in the table we want, which must have the `autoincrement` constraint for the `id` or **primary key**

Insert the data in a temporal table:
```SQL
.import --csv mfa.csv temp
```
Insert into the desire table:
``` SQL
INSERT INTO "collections" ("title", "accession_number", "acquired") 
SELECT "title", "accession_number", "acquired" FROM "temp";
```

## Deleting Data

With the `DELETE` command we can delete the rows we want, but we have to be aware to always use the `WHERE` command or we will delete all the rows at once. 

```SQL
DELETE FROM <table>;
```

Delete the painting "Spring outing" from the collections table
```SQL
DELETE FROM "collections"
WHERE "title" = 'Spring outing';
```

Delete rows pertaining to paintings older than 1909:
```SQL
DELETE FROM "collections"
WHERE "acquired" < '1909-01-01';
``` 

### Deleting Constraints

There might be cases where deleting some data **could impact the integrity of a database**. Foreign key constraints are a good example. A foreign key column references the primary key of a different table. If we were to delete the primary key, the foreign key column would have nothing to reference! We would have the following error:

`Runtime error: FOREIGN KEY constraint failed (19).` This error notifies us that deleting this data would violate the foreign key constraint.

How do we ensure that the constraint is not violated? One possibility is to **delete** the corresponding rows from the **table that has the foreign key before deleting from the referenced table.**

In another possibility, we can specify the action to be taken when an `ID` referenced by a foreign key is deleted. To do this, we use the keyword `ON DELETE` followed by the action to be taken.

- `ON DELETE RESTRICT`: This restricts us from deleting IDs when the foreign key constraint is violated.
- `ON DELETE NO ACTION`: This allows the deletion of IDs that are referenced by a foreign key and nothing happens.
- `ON DELETE SET NULL`: This allows the deletion of IDs that are referenced by a foreign key and sets the foreign key references to NULL.
- `ON DELETE SET DEFAULT`: This does the same as the previous, but allows us to set a default value instead of NULL.
- `ON DELETE CASCADE`: This allows the deletion of IDs that are referenced by a foreign key and also proceeds to cascadingly delete the referencing foreign key rows. For example, if we used this to delete an artist ID, all the artist’s affiliations with the artwork would also be deleted from the created table.

Example:
```SQL
CREATE TABLE Created(
    ...
FOREIGN KEY("artist_id") REFERENCES "artists"("id") ON DELETE CASCADE
FOREIGN KEY("collection_id") REFERENCES "collections"("id") ON DELETE CASCADE
);
```

## Updating Data

The UPDATE statement is used to modify existing records in a table.

Syntax
```sql
UPDATE <table_name>
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

```sql
-- Update the salary and department of an employee with employee_id 5
UPDATE employees
SET salary = 65000, department = 'Marketing'
WHERE employee_id = 5;
```
This updates both salary and department columns for the specified employee.

Updating Multiple Rows
```sql
-- Increase the salary by 10% for all employees in the 'Sales' department
UPDATE employees
SET salary = salary * 1.10
WHERE department = 'Sales';
```
This increases the salary of all employees in the 'Sales' department by 10%.

## TRIGGER

A TRIGGER is a special type of **stored procedure** that is automatically executed when certain events occur on a table, such as `INSERT`, `UPDATE`, or `DELETE`.

```sql
CREATE TRIGGER <trigger_name>
<trigger_time> <trigger_event> ON <table_name>
FOR EACH ROW
BEGIN
    <SQL Statement(s)>
END
```
- trigger_name: The name of the trigger.
- trigger_time: When the trigger should fire (`BEFORE` or `AFTER`).
- trigger_event: The event that activates the trigger (`INSERT`, `UPDATE`, or `DELETE`).
- table_name: The table on which the trigger is defined.


Example 1: BEFORE DELETE Trigger
```sql
-- Create a trigger to set sold a piece of art when is deleted from the collections table
CREATE TRIGGER sold
BEFORE DELETE ON collections
FOR EACH ROW
BEGIN
    INSERT INTO transactions ("title", "transaction")
    VALUES (OLD.title, "sold");
END;
```

Example 2: AFTER UPDATE Trigger
```sql
-- Create a trigger to log changes to the salary column after an update
CREATE TRIGGER after_employee_update
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    IF OLD.salary <> NEW.salary THEN
        INSERT INTO salary_changes (employee_id, old_salary, new_salary, change_date)
        VALUES (OLD.employee_id, OLD.salary, NEW.salary, NOW());
    END IF;
END;
```
This trigger logs the change in salary to a salary_changes table after an `UPDATE` on the employees table, but only if the salary actually changes.

Example 3: BEFORE DELETE Trigger
```sql
-- Create a trigger to prevent deletion of employees with certain conditions
CREATE TRIGGER before_employee_delete
BEFORE DELETE ON employees
FOR EACH ROW
BEGIN
    IF OLD.department = 'Management' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot delete employees from the Management department';
    END IF;
END;
```
This trigger prevents the deletion of employees who belong to the 'Management' department by raising an error.
