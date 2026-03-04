# SQL More Queries — README

## Overview

This chapter covers intermediate SQL concepts in **MySQL**, including:

* MySQL users and privileges
* Constraints (`PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`)
* Retrieving data from multiple tables
* `JOIN`s
* `DISTINCT`
* Subqueries
* `UNION`

The goal is to understand how relational databases work in real projects and how to write clean, safe SQL queries.

---

## Table of Contents

### [1. What is SQL?](#1-what-is-sql)

### [2. Learning Objectives](#2-learning-objectives)

### [3. MySQL Users and Privileges](#3-mysql-users-and-privileges)

### [4. Constraints in MySQL](#4-constraints-in-mysql)

### [5. Retrieving Data from Multiple Tables](#5-retrieving-data-from-multiple-tables)

### [6. JOINs](#6-joins)

### [7. DISTINCT](#7-distinct)

### [8. Subqueries](#8-subqueries)

### [9. JOIN vs Subquery](#9-join-vs-subquery)

### [10. UNION](#10-union)

### [11. MINUS / EXCEPT in MySQL](#11-minus--except-in-mysql)

### [12. Multiple JOINs](#12-multiple-joins)

### [13. SQL Style Guide](#13-sql-style-guide)

### [14. Common Mistakes](#14-common-mistakes)

### [15. Quick Cheat Sheet](#15-quick-cheat-sheet)

### [16. Mini Practice](#16-mini-practice)

### [17. Key Definitions](#17-key-definitions)

### [18. Final Summary](#18-final-summary)

---

## 1) What is SQL?

**SQL (Structured Query Language)** is the standard language used to communicate with relational databases such as **MySQL**.

### What SQL allows you to do

* Create databases and tables
* Insert, update, and delete data
* Query and filter data
* Connect related tables
* Manage users and permissions

### Simple examples

```sql
SHOW DATABASES;
CREATE DATABASE school;
USE school;
SELECT * FROM students;
```

---

## 2) Learning Objectives

By the end of this chapter, you should be able to explain:

### User and privilege management

* How to create a new MySQL user
* How to grant privileges to a user on a database or table
* How to revoke privileges

### Constraints and relationships

* What a `PRIMARY KEY` is
* What a `FOREIGN KEY` is
* How `NOT NULL` and `UNIQUE` work

### Querying across tables

* How to retrieve data from multiple tables in one query
* What `JOIN`s are
* What subqueries are
* What `UNION` is

---

## 3) MySQL Users and Privileges

### Create a new user

```sql
CREATE USER 'student_user'@'localhost' IDENTIFIED BY 'MyPassword123!';
```

### Grant all privileges on a database

```sql
GRANT ALL PRIVILEGES ON hbtn_0d_2.* TO 'student_user'@'localhost';
```

### Grant specific privileges

```sql
GRANT SELECT, INSERT, UPDATE ON hbtn_0d_2.* TO 'student_user'@'localhost';
```

### Grant privileges on one table only

```sql
GRANT SELECT ON hbtn_0d_2.my_table TO 'student_user'@'localhost';
```

### Revoke privileges

```sql
REVOKE INSERT, UPDATE ON hbtn_0d_2.* FROM 'student_user'@'localhost';
```

### Show current grants

```sql
SHOW GRANTS FOR 'student_user'@'localhost';
```

### Apply changes (commonly used in learning environments)

```sql
FLUSH PRIVILEGES;
```

### Why this matters

Privileges control what each user can do. This improves:

* security
* separation of roles
* safe collaboration

---

## 4) Constraints in MySQL

Constraints are rules applied to columns to maintain **data integrity**.

### `PRIMARY KEY`

A `PRIMARY KEY` uniquely identifies each row in a table.

#### Main rules

* Must be unique
* Cannot be `NULL`
* A table has one primary key (it can contain multiple columns)

#### Example

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);
```

---

### `FOREIGN KEY`

A `FOREIGN KEY` creates a relationship between two tables by referencing another table’s primary key.

#### Example

```sql
CREATE TABLE cities (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    city_id INT,
    FOREIGN KEY (city_id) REFERENCES cities(id)
);
```

#### Why it matters

It prevents invalid references and keeps relationships consistent.

---

### `NOT NULL`

This means the column must always have a value.

```sql
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);
```

---

### `UNIQUE`

This prevents duplicate values in a column.

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) UNIQUE
);
```

---

## 5) Retrieving Data from Multiple Tables

Relational databases often store data in separate related tables to avoid repetition.

### Example scenario

You may have:

* a `students` table
* a `classes` table

If you want to display **student name + class name** in one result, you need a `JOIN`.

---

## 6) JOINs

A `JOIN` combines rows from two or more tables using related columns.

### `INNER JOIN`

Returns only matching rows from both tables.

```sql
SELECT students.name, classes.class_name
FROM students
INNER JOIN classes ON students.class_id = classes.id;
```

### When to use `INNER JOIN`

Use it when you only want rows that have valid matches in both tables.

---

### `LEFT JOIN`

Returns all rows from the left table and matching rows from the right table.

```sql
SELECT students.name, classes.class_name
FROM students
LEFT JOIN classes ON students.class_id = classes.id;
```

### What happens if there is no match?

The left row still appears, and columns from the right table become `NULL`.

---

### `RIGHT JOIN`

Returns all rows from the right table and matching rows from the left table.

```sql
SELECT students.name, classes.class_name
FROM students
RIGHT JOIN classes ON students.class_id = classes.id;
```

---

### `CROSS JOIN`

Returns every combination of rows (Cartesian product).

```sql
SELECT students.name, classes.class_name
FROM students
CROSS JOIN classes;
```

### Caution

`CROSS JOIN` can produce very large results if the tables are big.

---

## 7) DISTINCT

`DISTINCT` removes duplicates from query results.

### Example

```sql
SELECT DISTINCT class_id
FROM students;
```

### Use case

Useful when joins produce repeated values and you only want unique results.

---

## 8) Subqueries

A subquery is a query inside another query.

### Subquery in `WHERE`

```sql
SELECT name
FROM students
WHERE class_id = (
    SELECT id
    FROM classes
    WHERE class_name = 'Robotics'
);
```

### Subquery with `IN`

```sql
SELECT name
FROM students
WHERE class_id IN (
    SELECT id
    FROM classes
    WHERE class_name IN ('Robotics', 'AI')
);
```

### Subquery with aggregation

```sql
SELECT name, age
FROM students
WHERE age > (
    SELECT AVG(age) FROM students
);
```

### Why subqueries are useful

They help when you need:

* a value from another query
* a list of IDs
* a filtered set before the main query runs

---

## 9) JOIN vs Subquery

Both can solve similar problems, but they are used differently.

### Use a `JOIN` when

* You need columns from multiple tables
* You want to combine related rows directly
* You want a single relational result set

### Use a subquery when

* You need a value/list first
* You want step-by-step filtering logic
* You are comparing against aggregate results (`AVG`, `MAX`, `COUNT`, etc.)

---

## 10) UNION

`UNION` combines the results of two `SELECT` queries into one result set.

### Rules for `UNION`

Both queries must return:

* the same number of columns
* compatible data types in the same positions

---

### `UNION` (removes duplicates)

```sql
SELECT name FROM students
UNION
SELECT class_name FROM classes;
```

---

### `UNION ALL` (keeps duplicates)

```sql
SELECT name FROM students
UNION ALL
SELECT class_name FROM classes;
```

### Difference between `UNION` and `UNION ALL`

* `UNION` removes duplicates
* `UNION ALL` keeps duplicates and is usually faster

---

## 11) MINUS / EXCEPT in MySQL

### Important MySQL note

MySQL does **not** support `MINUS`.

Some SQL databases use:

* `MINUS` (Oracle)
* `EXCEPT` (other systems)

### MySQL alternatives

Use one of these patterns:

* `LEFT JOIN ... WHERE ... IS NULL`
* `NOT IN`
* `NOT EXISTS`

### Example (`LEFT JOIN ... IS NULL`)

```sql
SELECT s.name
FROM students s
LEFT JOIN classes c ON s.class_id = c.id
WHERE c.id IS NULL;
```

This returns students with no matching class.

---

## 12) Multiple JOINs

You can join more than two tables in one query.

### Example with 3 tables

```sql
SELECT s.name AS student_name, c.course_name
FROM enrollments e
INNER JOIN students s ON e.student_id = s.id
INNER JOIN courses c ON e.course_id = c.id;
```

### Why this matters

This is very common in backend development and real database schemas.

---

## 13) SQL Style Guide

Good SQL style makes your queries easier to read, debug, and maintain.

### Recommended habits

* Write SQL keywords in uppercase (`SELECT`, `FROM`, `WHERE`)
* Put each clause on a new line
* Use meaningful aliases (`s`, `c`, `e`)
* Format joins clearly
* Add comments when useful

### Example (clean formatting)

```sql
SELECT s.name, c.class_name
FROM students AS s
INNER JOIN classes AS c
    ON s.class_id = c.id
WHERE c.class_name = 'Robotics'
ORDER BY s.name;
```

---

## 14) Common Mistakes

### Mistakes to avoid

* Forgetting the `ON` clause in a `JOIN`
* Using `UPDATE` or `DELETE` without `WHERE`
* Confusing `PRIMARY KEY` and `FOREIGN KEY`
* Using `= NULL` instead of `IS NULL`
* Using `UNION` when `UNION ALL` is the better choice
* Assuming all SQL dialects support the same syntax (`MINUS`, `EXCEPT`, etc.)

---

## 15) Quick Cheat Sheet

### Users and privileges

```sql
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT, INSERT ON db_name.* TO 'user'@'localhost';
REVOKE INSERT ON db_name.* FROM 'user'@'localhost';
SHOW GRANTS FOR 'user'@'localhost';
FLUSH PRIVILEGES;
```

### Constraints

```sql
id INT PRIMARY KEY AUTO_INCREMENT
name VARCHAR(100) NOT NULL
email VARCHAR(100) UNIQUE
FOREIGN KEY (city_id) REFERENCES cities(id)
```

### JOINs

```sql
SELECT ...
FROM a
INNER JOIN b ON a.id = b.a_id;

SELECT ...
FROM a
LEFT JOIN b ON a.id = b.a_id;
```

### Subqueries

```sql
SELECT ...
WHERE col IN (SELECT ...);
```

### Union

```sql
SELECT ... UNION SELECT ...;
SELECT ... UNION ALL SELECT ...;
```

---

## 16) Mini Practice

### Practice tasks

1. Create two related tables using `PRIMARY KEY` and `FOREIGN KEY`
2. Insert sample data into both tables
3. Retrieve combined data using `INNER JOIN`
4. Retrieve all rows from one table using `LEFT JOIN`
5. Use `DISTINCT` on repeated values
6. Write a subquery with `IN`
7. Write a subquery using `AVG()` or `COUNT()`
8. Combine two query results with `UNION`
9. Compare `UNION` vs `UNION ALL`
10. Create a user and grant only `SELECT` privilege

---

## 17) Key Definitions

### `PRIMARY KEY`

A column (or set of columns) that uniquely identifies each row in a table and cannot be `NULL`.

### `FOREIGN KEY`

A column that references the primary key of another table to create a relationship.

### `NOT NULL`

A constraint that requires a value in a column.

### `UNIQUE`

A constraint that prevents duplicate values in a column.

### `JOIN`

An SQL operation that combines rows from multiple tables using related columns.

### Subquery

A query nested inside another query.

### `UNION`

An SQL operation that combines the results of multiple `SELECT` queries into one result set.

---

## 18) Final Summary

This chapter moves beyond basic SQL and introduces the core ideas of relational database work:

### What you learn here

* Managing MySQL users and permissions
* Enforcing data integrity with constraints
* Creating relationships between tables
* Querying across tables with `JOIN`s
* Using subqueries for advanced filtering
* Combining results with `UNION`

These concepts are essential for:

* backend development
* API development
* database design
* production systems

---
