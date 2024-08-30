# Scaling

## MySQL

If want to create a local connection with MySQL on the terminal we can execute:

```bash
mysql -u root -h 127.0.0.1 -P 3306 -p
```

- In this terminal command, `-u` indicates the user. We provide the user we want to connect to the database as — `root` (synonymous with database admin, in this case).
- `127.0.0.1` is the address of local host on the internet (our own computer).
- `3306` is the port we want to connect to, and this is the default port where MySQL is hosted. 
- `p` at the end of the command indicates that we want to be prompted for a password when connecting.

Since this a full database server with potentially many databases inside it. To show all the existing ones, we use the following MySQL command.

``` bash
SHOW DATABASES;
```

This returns some default databases already in the server.

We will perform some operations to set up the MBTA database. Creating a new database:

```sql
CREATE DATABASE `mbta`;
```

To change the current database to mbta:

```sql
USE `mbta`; 
```

### Data Types

In **MySQL** an integer could be:
- `TINYINT`: 1 byte
- `SMALLINT`: 2 bytes 
- `MEDIUMINT`: 3 bytes 
- `INT`: 4 bytes 
- `BIGINT`: 8 bytes

There is also a way in MySQL to use a **decimal** (fixed precision) type. With this, we would specify the number of digits in the number to be represented, and the number of digits after the decimal point.

```sql
`amount` DECIMAL(5,2) NOT NULL CHECK(`amount` != 0)
```

To handle **text**, MySQL provides many types. Two commonly used ones are `CHAR` — a fixed width string, and `VARCHAR` — a string of variable length. MySQL also has a type `TEXT` but unlike in SQLite, this type is used for longer chunks of text like paragraphs, pages of books etc. Based on the length of the text, it could be one of: `TINYTEXT`, `TEXT`, `MEDIUMTEXT` and `LONGTEXT`. Additionally, we have the `BLOB` type to store binary strings.

MySQL also provides two other text types: `ENUM` and `SET`. 
- **Enum** restricts a column to a single predefined option from a list of options we provide. 
- **Set** allows for multiple options to be stored in a single cell, useful for scenarios like movie genres.

To **store our date and time values** we could use `DATE`, `YEAR`, `TIME`, `DATETIME` and `TIMESTAMP` (for more precise times). The last three allow an optional parameter to specify the precision with which we want to store the time.



### Creating a Table

```sql
CREATE TABLE `stations` (
    `id` INT AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL UNIQUE,
    `line` ENUM('blue', 'green', 'orange', 'red') NOT NULL,
    PRIMARY KEY(`id`)
);
```

We choose a `VARCHAR` for the station name because names might be an unknown length. The line that a station is on, however, is one of the existing subway lines in Boston. Since we know the values this could take, we can use an `ENUM` type.

We also use column constraints `UNIQUE` and `NOT NULL` in the same way as we did with SQLite.

After creating the table, we can see a list of the existing tables by running:
```sql
SHOW TABLES;
```

For further details about a table, we can use the DESCRIBE command.
```
DESCRIBE `cards`;
```

On running the command to describe this table, we see a similar output that lists out each of the columns in the table. Under the Key field, the **primary key** is recognized by `PRI` and any column with **unique values** is recognized by `UNI`. The `NULL` field tells us which columns allow `NULL` values, which none of the columns do for the stations table.

Creating **swipes** table

```sql
CREATE TABLE `swipes` (
    `id` INT AUTO_INCREMENT,
    `card_id` INT,
    `station_id` INT,
    `type` ENUM('enter', 'exit', 'deposit') NOT NULL,
    `datetime` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `amount` DECIMAL(5,2) NOT NULL CHECK(`amount` != 0),
    PRIMARY KEY(`id`),
    FOREIGN KEY(`station_id`) REFERENCES `stations`(`id`),
    FOREIGN KEY(`card_id`) REFERENCES `cards`(`id`)
);
```

### Altering Tables


If we wanted to add a silver line to the possible lines a station could be on, we can do the following.
```sql
ALTER TABLE `stations` 
MODIFY `line` ENUM('blue', 'green', 'orange', 'red', 'silver') NOT NULL;
```

If we want to add a column for soft deletions, we can do:
```sql
ALTER TABLE `collections` 
ADD COLUMN `deleted` TINYINT DEFAULT 0;
```
Given that the **deleted column** only has values of 0 or 1, it is safe to use a TINYINT. We also assign the default as 0 because we want to keep all the collections already in the table.

### Stored Procedures

Stored procedures are a way to **automate SQL statements and run them repeatedly**.

We will now use a stored procedure in MySQL to manage soft deletions.

Before we create a stored procedure, we need to change the delimited from `;` to something else; since MySQL prematurely ends the statement when it encounters a `;`.

`delimiter //`
Now, we write the stored procedure.
```sql
CREATE PROCEDURE `current_collection`()
BEGIN
    SELECT `title`, `accession_number`, `acquired` 
    FROM `collections` 
    WHERE `deleted` = 0;
END//
```

Notice how we use empty parantheses next to the name of the procedure, perhaps reminiscent of functions in other programming languages. Similar to functions, we can also call stored procedures to run them.

After creating this, we must reset the delimited to `;`.

If want to call the procedure, we can do the following:
```sql
CALL current_collection();
```

If we soft-delete “Farmers working at dawn” and call the procedure again, we will find that the deleted row is not included in the output.

#### Stored Procedures with Parameters

If a piece of artwork is deleted from collections because it is being sold, we would also like to update this in the transactions table. Usually, this would be two different queries but with a **stored procedure**, we can give this sequence one name.

`delimiter //`

```sql
CREATE PROCEDURE `sell`(IN `sold_id` INT)
BEGIN
    UPDATE `collections` SET `deleted` = 1 
    WHERE `id` = `sold_id`;
    INSERT INTO `transactions` (`title`, `action`)
    VALUES ((SELECT `title` FROM `collections` WHERE `id` = `sold_id`), 'sold');
END//
```

`delimiter ;`

The choice of the parameter for this procedure is the ID of the painting or artwork because it is a unique identifier.

We can now call the procedure to sell a particular item. Suppose we want to sell “Imaginative landscape”.

```sql
CALL `sell`(2);
```

We can also improve our procedures in logic and complexity by using some regular old programming constructs, like:

- `IF`, `ELSEIF`, `ELSE`
- `LOOP`
- `WHILE`
- `REPEAT`

## Scaling

Consider a database server for an application growing in demand. As the number of reads and writes coming in from the application begin to increase, the wait time for the queries to be processed by the server increases also.

- One approach here is to **scale the database vertically**. Scaling vertically is increasing capacity by increasing the computing power of the database server.
- Another approach is to **scale horizontally**. This means increasing capacity by distributing load across multiple servers. When we scale horizontally, we keep copies of our database on multiple servers (replication).There are three main models of replication: 
    - single-leader: a single database server handling incoming writes and then copying those changes into other servers
    - multi-leader: multiple servers receiving updates
    - leaderless: does not require leaders in this sense.
- Another popular way of scaling is called **sharding**. This involves splitting the database into shards across multiple database servers. A word of caution with sharding: we want to avoid having a database hotspot, or a database server that becomes more frequently accessed than others. This could create an overload on that server.

## Access Controls

We can **create more users** and give them some kind of access to the database.
Let’s create a new user called 'user' 

```sql
CREATE USER 'user' IDENTIFIED BY 'password';
```

We can log into MySQL now using the new user and password, in the same way we did with the root user previously.

```bash
mysql -u user -h 127.0.0.1 -P 3306 -p
```

If we wanted to share the analysis view with the user we just created, we would do the following while logged in as the root user.

```sql
GRANT SELECT ON `rideshare`.`analysis` TO 'user';
```

The only part of the database, however, that this user can access is the analysis view. We can now see the data in this view, but not from the original rides table! 