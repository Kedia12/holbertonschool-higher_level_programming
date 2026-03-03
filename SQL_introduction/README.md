## SQL (Structured Query Language) 

**SQL (Structured Query Language)** is the standard language used to interact with **relational database management systems (RDBMS)** such as **MySQL, PostgreSQL, SQLite, SQL Server, and Oracle**.

A relational database stores data in **tables** (rows and columns), and SQL is used to:

* **Define** database structure (schemas, tables, constraints)
* **Manipulate** data (insert, update, delete)
* **Query** data (filter, sort, aggregate, join)
* **Control** access (users, privileges)
* **Manage** transactions (commit/rollback changes safely)

---

## Core SQL Categories (What SQL is made of)

### 1) DDL — Data Definition Language

Used to define and modify database structure.

Common commands:

* `CREATE`
* `ALTER`
* `DROP`
* `TRUNCATE`

Example:

```sql
CREATE DATABASE school;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT,
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 2) DML — Data Manipulation Language

Used to change the data inside tables.

Common commands:

* `INSERT`
* `UPDATE`
* `DELETE`

Examples:

```sql
INSERT INTO students (first_name, last_name, age, email)
VALUES ('Kedia', 'Ihogoza', 22, 'kedia@example.com');

UPDATE students
SET age = 23
WHERE id = 1;

DELETE FROM students
WHERE id = 1;
```

⚠️ **Important:** `UPDATE` and `DELETE` without `WHERE` affect **all rows**.

---

### 3) DQL — Data Query Language

Used to read/query data.

Main command:

* `SELECT`

Examples:

```sql
SELECT * FROM students;

SELECT first_name, age
FROM students
WHERE age >= 18
ORDER BY age DESC;

SELECT COUNT(*) AS total_students
FROM students;
```

---

### 4) DCL — Data Control Language

Used to manage permissions.

Common commands:

* `GRANT`
* `REVOKE`

Example (syntax varies by DBMS):

```sql
GRANT SELECT, INSERT ON school.students TO 'user'@'localhost';
REVOKE INSERT ON school.students FROM 'user'@'localhost';
```

---

### 5) TCL — Transaction Control Language

Used to manage transactions (group of operations treated as one unit).

Common commands:

* `START TRANSACTION`
* `COMMIT`
* `ROLLBACK`

Example:

```sql
START TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

COMMIT;
-- or ROLLBACK; if something fails
```

---

## Relational Database Basics (must know)

### Table

A collection of related data organized in rows and columns.

### Row (record)

One entry in the table.

### Column (field)

One attribute of the data (e.g., `name`, `age`, `email`).

### Primary Key (PK)

A column (or columns) that uniquely identifies each row.

Example:

* `id` is usually the primary key.

### Foreign Key (FK)

A column that links one table to another (creates relationships).

Example:

```sql
CREATE TABLE courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE enrollments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

---

## SQL Query Execution Order (logical order)

Even if you write `SELECT` first, SQL logically processes a query roughly in this order:

1. `FROM`
2. `JOIN`
3. `WHERE`
4. `GROUP BY`
5. `HAVING`
6. `SELECT`
7. `ORDER BY`
8. `LIMIT`

This helps explain why aliases sometimes don't work in `WHERE` (depends on DBMS).

---

## Essential SQL Commands You Should Know First

### Server / Database level (MySQL)

```sql
SHOW DATABASES;
CREATE DATABASE my_db;
USE my_db;
DROP DATABASE my_db;
```

### Table level

```sql
SHOW TABLES;

DESCRIBE students;
-- or
SHOW COLUMNS FROM students;
```

### CRUD (Create, Read, Update, Delete)

#### Create (Insert rows)

```sql
INSERT INTO students (first_name, last_name, age)
VALUES ('Aline', 'M.', 21);
```

#### Read (Query rows)

```sql
SELECT * FROM students;
SELECT first_name, age FROM students WHERE age > 20;
```

#### Update (Modify rows)

```sql
UPDATE students
SET age = 22
WHERE first_name = 'Aline';
```

#### Delete (Remove rows)

```sql
DELETE FROM students
WHERE first_name = 'Aline';
```

---

## Filtering, Sorting, and Limiting Data

### WHERE (filter rows)

```sql
SELECT * FROM students WHERE age = 22;
SELECT * FROM students WHERE age >= 18 AND age <= 25;
SELECT * FROM students WHERE age BETWEEN 18 AND 25;
SELECT * FROM students WHERE age IN (18, 20, 22);
SELECT * FROM students WHERE email IS NULL;
```

### LIKE (pattern matching)

```sql
SELECT * FROM students WHERE first_name LIKE 'K%';   -- starts with K
SELECT * FROM students WHERE first_name LIKE '%a';   -- ends with a
SELECT * FROM students WHERE first_name LIKE '%ed%'; -- contains ed
```

### ORDER BY (sorting)

```sql
SELECT * FROM students ORDER BY age ASC;
SELECT * FROM students ORDER BY age DESC, first_name ASC;
```

### LIMIT (restrict number of rows)

```sql
SELECT * FROM students LIMIT 5;
```

---

## Aggregate Functions (summaries)

Used to compute values from multiple rows.

Common aggregates:

* `COUNT()`
* `SUM()`
* `AVG()`
* `MIN()`
* `MAX()`

Examples:

```sql
SELECT COUNT(*) AS total FROM students;
SELECT AVG(age) AS average_age FROM students;
SELECT MIN(age) AS youngest, MAX(age) AS oldest FROM students;
```

### GROUP BY (group rows before aggregation)

```sql
SELECT age, COUNT(*) AS total
FROM students
GROUP BY age;
```

### HAVING (filter grouped results)

```sql
SELECT age, COUNT(*) AS total
FROM students
GROUP BY age
HAVING COUNT(*) > 1;
```

👉 `WHERE` filters rows **before** grouping, `HAVING` filters groups **after** grouping.

---

## JOINs (combining tables) — very important

JOINs let you combine data from related tables.

### INNER JOIN (matching rows only)

```sql
SELECT s.first_name, c.name AS course_name
FROM enrollments e
INNER JOIN students s ON e.student_id = s.id
INNER JOIN courses c ON e.course_id = c.id;
```

### LEFT JOIN (all rows from left table + matches)

```sql
SELECT s.first_name, c.name AS course_name
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id
LEFT JOIN courses c ON e.course_id = c.id;
```

If a student has no course, course columns may return `NULL`.

---

## Constraints (rules that protect data integrity)

Common constraints:

* `PRIMARY KEY` → unique row identifier
* `FOREIGN KEY` → valid relationship to another table
* `NOT NULL` → value is required
* `UNIQUE` → no duplicates allowed
* `CHECK` → value must satisfy a condition (DB support varies)
* `DEFAULT` → automatic value if none provided

Example:

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10,2) CHECK (salary >= 0),
    status VARCHAR(20) DEFAULT 'active'
);
```

---

## Data Types (common ones you’ll see)

### Numeric

* `INT`
* `BIGINT`
* `DECIMAL(p, s)` (exact decimals, good for money)
* `FLOAT` / `DOUBLE` (approximate decimals)

### Text

* `CHAR(n)` (fixed length)
* `VARCHAR(n)` (variable length)
* `TEXT`

### Date/Time

* `DATE`
* `TIME`
* `DATETIME`
* `TIMESTAMP`

### Boolean

* `BOOLEAN` (often stored as `TINYINT(1)` in MySQL)

---

## NULL (very important concept)

`NULL` means **missing / unknown / no value** (it is not the same as `0` or empty string).

### Correct checks

```sql
SELECT * FROM students WHERE email IS NULL;
SELECT * FROM students WHERE email IS NOT NULL;
```

❌ Wrong:

```sql
email = NULL
```

---

## SQL Best Practices (beginner + professional habits)

* Always use `WHERE` in `UPDATE` / `DELETE` unless you truly want all rows.
* End commands with `;`
* Use clear table/column names (`student_id`, not `sid` unless standardized)
* Prefer explicit column names over `SELECT *` in production code
* Use `DECIMAL` for money (not `FLOAT`)
* Add constraints early (`NOT NULL`, `UNIQUE`, FK)
* Back up data before destructive operations
* Test queries with `SELECT` before running `UPDATE`/`DELETE`
* Format SQL consistently for readability

---

## Example Mini Workflow (end-to-end)

```sql
-- 1) Create database
CREATE DATABASE school;
USE school;

-- 2) Create table
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    age INT
);

-- 3) Insert data
INSERT INTO students (first_name, age) VALUES ('Alice', 20);
INSERT INTO students (first_name, age) VALUES ('Bob', 22);
INSERT INTO students (first_name, age) VALUES ('Charlie', 22);

-- 4) Query data
SELECT * FROM students;

-- 5) Filter + sort
SELECT first_name, age
FROM students
WHERE age >= 21
ORDER BY age DESC, first_name ASC;

-- 6) Aggregate
SELECT age, COUNT(*) AS total
FROM students
GROUP BY age;

-- 7) Update
UPDATE students
SET age = 23
WHERE first_name = 'Bob';

-- 8) Delete
DELETE FROM students
WHERE first_name = 'Alice';
```

---

## Quick Summary (What you need to know first)

If you're starting SQL, focus on these in order:

1. **Database vs Table vs Row vs Column**
2. `SHOW DATABASES;`, `USE db_name;`, `SHOW TABLES;`
3. `CREATE TABLE`
4. `INSERT INTO`
5. `SELECT ... FROM ...`
6. `WHERE`, `ORDER BY`, `LIMIT`
7. `UPDATE ... WHERE ...`
8. `DELETE ... WHERE ...`
9. Aggregate functions: `COUNT`, `AVG`, `SUM`, `MIN`, `MAX`
10. `GROUP BY` and `HAVING`
11. `JOIN` (especially `INNER JOIN` and `LEFT JOIN`)
12. Keys and constraints (`PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`)
13. Transactions (`COMMIT`, `ROLLBACK`)
14. Safe habits (always check `WHERE`)

---

## One-line definition (technical)

SQL is a declarative language for defining, querying, and managing data in relational databases using structured statements such as `CREATE`, `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.
