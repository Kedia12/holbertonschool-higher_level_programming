# Python Object-Relational Mapping (ORM) — README

## Overview

This chapter introduces **Object-Relational Mapping (ORM)** in Python: a way to work with SQL databases using **Python classes and objects** instead of writing raw SQL everywhere.

You’ll learn how to:

- map Python classes to database tables
- create and query records using objects
- define relationships (One-to-Many, Many-to-Many)
- understand sessions/transactions
- avoid common SQL pitfalls (SQL injection, inconsistent schemas)

---

## Table of Contents

### [1. What is an ORM?](#1-what-is-an-orm)
### [2. Why use an ORM?](#2-why-use-an-orm)
### [3. Key concepts and vocabulary](#3-key-concepts-and-vocabulary)
### [4. ORM vs Raw SQL (when to use each)](#4-orm-vs-raw-sql-when-to-use-each)
### [5. SQLAlchemy ORM basics](#5-sqlalchemy-orm-basics)
### [6. Defining models (tables)](#6-defining-models-tables)
### [7. CRUD operations (Create, Read, Update, Delete)](#7-crud-operations-create-read-update-delete)
### [8. Relationships (One-to-Many, Many-to-Many)](#8-relationships-one-to-many-many-to-many)
### [9. Sessions, transactions, and commits](#9-sessions-transactions-and-commits)
### [10. Common query patterns](#10-common-query-patterns)
### [11. Best practices](#11-best-practices)
### [12. Quick cheat sheet](#12-quick-cheat-sheet)

---

## 1) What is an ORM?

An **ORM (Object-Relational Mapper)** is a layer that maps:

- **Tables** ↔ **Python classes**
- **Rows** ↔ **Python objects**
- **Columns** ↔ **Object attributes**

Instead of writing SQL like:

```sql
SELECT * FROM states ORDER BY id;

You write Python like:

session.query(State).order_by(State.id).all()

The ORM generates the SQL and executes it for you.

2) Why use an ORM?
Benefits

Cleaner code: less raw SQL string handling

Safer: helps prevent SQL injection via parameter binding

Reusable models: database tables become well-structured Python classes

Relationships: easy navigation between related tables (user.posts, post.user)

Maintainability: queries become easier to read, update, and test

Tradeoffs

Less direct control than handcrafted SQL

Learning curve (sessions, relationships, lazy loading)

Complex queries may still require raw SQL or advanced ORM usage

3) Key concepts and vocabulary
Models

Python classes that represent database tables.

Engine

The connection configuration to the database (MySQL, PostgreSQL, etc.).

Session

A unit-of-work manager used to query and persist objects.

Mapping

The definition that connects a class attribute to a table column.

Primary Key / Foreign Key

Used to uniquely identify rows and to create relationships between tables.

4) ORM vs Raw SQL (when to use each)
Use ORM when:

you’re doing standard CRUD

you want clean maintainable code

you need relationships between tables

you want safer query building

Use Raw SQL when:

you need advanced performance tuning

you’re writing complex queries (window functions, vendor-specific SQL)

you need full control over query execution

In real projects, it’s common to use both.

5) SQLAlchemy ORM basics

SQLAlchemy is the most popular Python ORM toolkit.

Typical ORM components:

create_engine() → database connection setup

declarative_base() → base class for models

Session() → create a session for queries and writes

6) Defining models (tables)

Example: a states table mapped to a State class.

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
Key points

__tablename__ = actual table name in SQL

Column(...) defines column type + constraints

primary_key=True marks the primary key

7) CRUD operations (Create, Read, Update, Delete)
Create (INSERT)
new_state = State(name="California")
session.add(new_state)
session.commit()
Read (SELECT)
states = session.query(State).order_by(State.id).all()
for state in states:
    print(state.id, state.name)
Update (UPDATE)
state = session.query(State).filter_by(name="California").first()
state.name = "New California"
session.commit()
Delete (DELETE)
state = session.query(State).filter_by(name="New California").first()
session.delete(state)
session.commit()
8) Relationships (One-to-Many, Many-to-Many)

Relationships let you link tables and navigate data naturally.

One-to-Many example (State → City)

One State has many City

Each City belongs to one State

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State", back_populates="cities")

Now you can do:

state = session.query(State).first()
for city in state.cities:
    print(city.name)
Many-to-Many (advanced)

Requires an association table (link table). Common for: students↔courses, posts↔tags.

9) Sessions, transactions, and commits
Session = workspace

A Session keeps track of:

objects you loaded

objects you changed

objects you added/deleted

Commit vs Rollback

commit() saves changes permanently

rollback() cancels changes if something fails

Example:

try:
    session.add(obj)
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()
10) Common query patterns
Filter
session.query(State).filter(State.name == "Texas").all()
Like (pattern matching)
session.query(State).filter(State.name.like("N%")).all()
Order + Limit
session.query(State).order_by(State.id.desc()).limit(5).all()
Join (query across tables)
session.query(State, City).join(City).filter(State.name == "California").all()
11) Best practices

Use environment variables for credentials (don’t hardcode passwords)

Always close sessions (session.close()), especially in scripts

Prefer ORM parameter binding (avoid string SQL concatenation)

Use migrations (e.g., Alembic) in real projects to track schema changes

Keep models in a dedicated models/ package for clarity

Add indexes for frequently queried columns

12) Quick cheat sheet
Map class to table

__tablename__ = "table_name"

Create record

session.add(obj) + session.commit()

Read records

session.query(Model).all()

Update record

modify attributes + session.commit()

Delete record

session.delete(obj) + session.commit()

Relationships

relationship() + ForeignKey()

Final Summary

Python ORM lets you work with SQL databases using Python objects.
It improves maintainability, safety, and readability, especially for CRUD and relationships.
SQLAlchemy is the standard ORM in Python projects, and understanding models + sessions is the core skill.
