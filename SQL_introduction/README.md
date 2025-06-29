# SQL - Introduction

This directory contains a set of SQL scripts that introduce the basics of relational databases and SQL queries. Each file demonstrates a specific concept or operation using MySQL.

## Learning Objectives

- Understand what a database is
- Learn how to create and delete databases
- Learn how to create and delete tables
- Learn how to insert data into a table
- Learn how to retrieve data using `SELECT`
- Learn how to filter data using `WHERE`
- Understand `GROUP BY`, `ORDER BY`, and aggregate functions
- Understand basic data manipulation and constraints

## Files

| Filename                     | Description                                |
|-----------------------------|--------------------------------------------|
| 0-list_databases.sql        | List all databases                         |
| 1-create_database_if_missing.sql | Create a database if it doesn't exist  |
| 2-remove_database.sql       | Delete a database                          |
| 3-list_tables.sql           | List all tables in a database              |
| 4-first_table.sql           | Create a table in a database               |
| 5-full_table.sql            | Print full table description               |
| 6-list_values.sql           | List all rows from a table                 |
| 7-insert_value.sql          | Insert a new row into a table              |
| 8-count_89.sql              | Count rows where id = 89                   |
| 9-full_creation.sql         | Create a full table with multiple fields   |
| 10-top_score.sql            | Get the top score from a table             |
| 11-best_score.sql           | List all scores ordered by best first      |
| 12-no_cheating.sql          | Filter out rows with NULL or empty names   |
| 13-change_class.sql         | Update the class of a specific record      |
| 14-average.sql              | Calculate the average score                |
| 15-groups.sql               | Group rows and apply aggregate function    |
| 16-no_link.sql              | List all records without a foreign link    |

## Usage

To execute a SQL file, use the following command:

```bash
cat <filename.sql> | mysql -hlocalhost -uroot -p <database_name>

Replace <filename.sql> with the script name and <database_name> with your target database.

---

## ✍️ Author
[Meshari - M0simi](https://github.com/M0simi)
